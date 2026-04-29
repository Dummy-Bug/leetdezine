# 4 What Actually Breaks in a URL Shortener Design at Scale?

# Platform: DEV.to
# Canonical URL: https://leetdezine.com/?utm_source=devto
# Tags: systemdesign, distributedsystems, backend, programming

---

Everyone can describe a URL shortener. Write a row to the DB, generate a short code, cache it on reads. The base design fits on a napkin.

The interesting part is what happens when you push on any one of those steps. Where does it break? Why? And what's the fix that actually holds at scale?

Here are four traps I've seen candidates walk straight into — each one looks correct on the surface.

---

## 1. The Truncation Trap

A Snowflake ID is 64 bits. You only need 36 bits to cover 50 billion URLs (2^36 = 68 billion). Encode 36 bits in base62 and you get exactly 6 characters. Clean short code, no collision check needed.

The natural move: drop the rightmost 28 bits, encode what's left. You're keeping the timestamp, which feels like the important part.

```
[ timestamp — 41 bits ][ machine ID — 10 bits ][ sequence — 12 bits ]
 ←────── keep 36 bits ─────────────────────────→ ←── drop 28 bits ──→
                                                  (machine + sequence)
```

Here's what breaks: the rightmost 28 bits you dropped contain the **sequence number** — the counter that differentiates two Snowflake IDs generated on the **same server in the same millisecond**.

```
Request A — server 3, t=1700000001ms, seq=1
keep 36 bits → "x7k2p9"

Request B — server 3, t=1700000001ms, seq=2
keep 36 bits → "x7k2p9"  ✗  collision
```

The only difference between A and B was `seq=1` vs `seq=2`. You dropped that. At 1000 creations/sec, two requests landing in the same millisecond is not an edge case — it's constant.

**The rule:** you cannot get both uniqueness and shortness by truncating a Snowflake. All three sections — timestamp, machine ID, sequence — contribute to the guarantee. Drop any of them and you break it.

The options that actually work: accept 11-char codes from the full Snowflake, use random 6-char base62 with a collision check, or pre-generate keys where uniqueness is native to the key size.

---

## 2. Redis INCR Looks Perfect. It Has One Fatal Flaw.

For collision-free short code generation, Redis INCR is elegant. Atomic counter increments — every call returns a unique integer. Base62-encode it. Done. No collision checks, no retries, no background service.

```
INCR url_counter  →  1000000
Base62(1000000)   →  "004C9M"
INSERT short_code = "004C9M"
```

The problem has nothing to do with code generation. It's about what sequential codes leak.

If a user receives `yoursite.com/004C9M`, they know the previous URL was `yoursite.com/004C9L` and the next will be `yoursite.com/004C9N`. They can walk the entire sequence and enumerate every URL in your system.

For an internal tool, this is fine. For a public shortener — where someone might shorten a pre-announcement, an internal doc, or a private file — it's a privacy violation.

The second problem: Redis INCR makes Redis a hard dependency on every creation request. Redis down → creation fails immediately, zero fallback.

**The fix: KGS + pre-generated key pool.** A Key Generation Service pre-generates random base62 codes offline and loads them into a Redis list. App servers pop keys with LPOP. Codes are in random order — no enumerability. App servers pre-fetch a local batch of 100 keys, so Redis going down doesn't immediately stop creation.

Redis INCR is right for internal tools. KGS + pool is right for public shorteners.

---

## 3. What Actually Happens When Redis Dies

Most failure mode answers in interviews stop at "Redis is replicated." That's a configuration, not a plan.

Redis absorbs ~80% of all redirect reads. At 1M reads/sec, the DB only sees 200k/sec. Redis dies. 1M reads/sec hits DB nodes sized for 200k/sec.

**Without a circuit breaker**, every request tries Redis, waits 500ms for the connection timeout, then falls back to DB. At 1M requests/sec, that's your thread pool stalled for 500ms each. No request completes. The DB never gets a clean chance to respond. Total cascade.

```
Redis down, no circuit breaker:
Request → try Redis → wait 500ms → timeout → fallback to DB
× 1,000,000 requests/sec
= thread pool exhausted, DB never reached
```

**Circuit breaker** fixes the timeout overhead. After N failures in T seconds, the circuit opens — requests skip Redis entirely and go straight to DB. Latency rises but the system stays alive.

Still not enough. DB peak capacity is ~800k reads/sec. The API Gateway throttles the overflow, returning 503 to some percentage of redirect requests. The system degrades — but doesn't collapse.

The trap that kills most answers: **"auto-scaling handles this."** A new Postgres replica takes minutes to provision and catch up WAL replication. Your traffic surge is immediate. Auto-scaling is for gradual growth, not cache failure.

**Partial availability beats total cascade.** Always.

---

## 4. LPOP Is Atomic by Architecture, Not by Lock

If you build a pre-generated key pool in Redis, a natural interview question is: "how do you prevent two app servers from popping the same key simultaneously?"

You don't have to. Redis handles it.

Redis is single-threaded. Every command executes one at a time. If 20 app servers call LPOP at the exact same millisecond, Redis processes them sequentially:

```
App Server 1  →  LPOP  →  "x7k2p9"  (removed)
App Server 2  →  LPOP  →  "k2m8q1"  (removed)
App Server 3  →  LPOP  →  "p9n3r7"  (removed)
```

Physically impossible for two calls to return the same value. Not because of a lock — because of the execution model.

Compare to a Postgres key pool. You'd need `SELECT FOR UPDATE SKIP LOCKED` — row-level locking on every creation request. Expensive, complex, and a bottleneck under high concurrency.

**The batch pre-fetch makes it even better.** Each app server grabs 100 keys at startup and refills when empty. At 1k creations/sec across 20 servers, Redis traffic drops from 1000 LPOP calls/sec to ~10 batch refills/sec. 100x reduction. Same correctness guarantee.

A crashed server loses its local batch — at most 100 keys out of a 100M key pool. That's 0.0001%. Don't bother recovering them.

---

## The Pattern Across All Four

Each trap comes from a decision that's locally correct but breaks a property you assumed was safe: uniqueness, privacy, fault tolerance, atomicity.

The way to catch these in an interview isn't to memorize solutions. It's to ask "what does this break?" for every component you add.

The full URL shortener case study walks through every deep dive in this sequence — requirements, estimation, base architecture, then each failure mode in detail:

→ https://leetdezine.com?utm_source=devto
