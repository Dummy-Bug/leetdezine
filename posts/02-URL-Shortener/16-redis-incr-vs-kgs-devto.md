# Why Is Redis INCR a Bad Fit for a Public URL Shortener?

# Platform: DEV.to
# Canonical URL: https://leetdezine.com/?utm_source=devto
# Tags: systemdesign, distributedsystems, backend, redis

---

Redis INCR is one of those solutions that looks perfect the first time you see it. Atomic counter increments. Every call returns a unique integer. Base62-encode it and you have a short code — zero collision checks, zero retries, no background service.

It's cleaner than anything else on the board. So why does every serious URL shortener reject it?

The answer has nothing to do with code generation.

---

## How Redis INCR Works (And Why It's Technically Correct)

The mechanics are clean:

```
Creation request arrives
→ Redis: INCR url_counter → returns 1000000
→ Base62 encode 1000000:

  Divide repeatedly, collect remainders, stop when quotient = 0:

  1000000 ÷ 62 = 16129  remainder 22 → 'M'  (quotient != 0, keep going)
  16129   ÷ 62 = 260    remainder 9  → '9'  (quotient != 0, keep going)
  260     ÷ 62 = 4      remainder 12 → 'C'  (quotient != 0, keep going)
  4       ÷ 62 = 0      remainder 4  → '4'  (quotient = 0, stop)

  Read remainders bottom to top: "4C9M" → pad to 6 chars → "004C9M"

→ INSERT short_code = "004C9M"
→ Done.
```

Redis is single-threaded. `INCR` is atomic — it increments and returns in a single operation. Two simultaneous calls always get different values:

```
App server 1: INCR → 1000000
App server 2: INCR → 1000001  ← different, guaranteed
App server 3: INCR → 1000002  ← different, guaranteed
```

No race condition. No collision. No retry loop. Encoding a unique number always produces a unique code. The math is correct.

So what's the problem?

---

## Problem 1 — Sequential Codes Are a Privacy Violation

Counter values are sequential. If your user receives `yoursite.com/004C9M`, they immediately know:

```
yoursite.com/004C9L  ← previous URL, someone else's
yoursite.com/004C9N  ← next URL, someone else's
yoursite.com/004C9K  ← keep going...
yoursite.com/004C9J  ← and going...
```

They can walk the entire database. Every URL in your system is discoverable by incrementing one character.

For an internal tool where all users are trusted, this might be fine. For a public shortener — where someone might shorten a pre-announcement link, an internal doc, a private file, a personal photo album — it's a real privacy violation. Your users have a reasonable expectation that their short link isn't guessable.

Sequential codes make that expectation impossible to satisfy.

---

## Problem 2 — Redis Becomes a Hard Dependency on Every Creation

With INCR, the hot path looks like this:

```
Request → INCR Redis → encode → INSERT DB
```

Redis is in the critical path of every single URL creation. If Redis goes down:

```
Redis down
→ INCR fails
→ No counter value
→ Creation fails immediately
→ Zero fallback
```

There's no graceful degradation. No buffer. No local state to drain. The moment Redis is unreachable, your creation endpoint returns errors.

---

## The Fix: KGS + Pre-Generated Key Pool

The Key Generation Service approach flips the model. Instead of generating a key at request time, keys are generated in advance and stored in a Redis pool. When a request arrives, the app server just pops one.

```
Before any request arrives:
→ KGS generates random base62 codes offline
→ Loads them into Redis list (RPUSH)

When creation request arrives:
→ App server pops key from local batch
→ INSERT into DB
→ Done — zero Redis call on hot path
```

**Why LPOP is atomic:** Redis is single-threaded. Even if 20 app servers call LPOP at the same millisecond, Redis processes them one at a time:

```
App server 1: LPOP → "x7k2p9" (removed)
App server 2: LPOP → "k2m8q1" (removed)
App server 3: LPOP → "p9n3r7" (removed)
```

Physically impossible for two LPOP calls to return the same key. No locks needed. No `SELECT FOR UPDATE`. Atomicity comes from the architecture.

**The batch pre-fetch:** Each app server grabs 100 keys at startup and keeps them in local memory. At 1k creations/sec across 20 servers, Redis traffic drops from 1000 LPOP/sec to ~10 batch refills/sec. 100x reduction.

```
App server starts:
→ LPOP 100 keys → store in local queue

Creation request:
→ Pop from local queue (zero network call)
→ Queue empty → refill from Redis
```

**What this fixes for Redis failure:**

```
Redis down
→ App servers drain local batch (100 keys × 20 servers = 2000 keys)
→ At 1k creations/sec → ~2 seconds of local runway
→ Circuit breaker engages, Redis recovers
→ Graceful degradation instead of hard failure
```

---

## Side by Side

| | Redis INCR | KGS + Pool |
|---|---|---|
| Collision checks | None | None |
| Code predictability | Sequential — enumerable | Random — private |
| Redis failure | Creation fails instantly | Local batch buys time |
| Operational cost | Very simple | Small background worker |
| Right for | Internal tools | Public URL shortener |

---

## The Pattern

Redis INCR fails not because of what it does, but because of what it leaks. Sequential uniqueness and privacy are in direct conflict. You can't have both with a counter.

The KGS + pool approach keeps the "no collision checks, no retries" guarantee while adding randomness and resilience. The operational cost is a 50-line background worker and one metric to monitor. The privacy and fault tolerance gains are worth it for any public-facing system.

The full URL shortener case study — including requirements, DB design, caching, peak traffic, and every failure mode — is at:

→ https://leetdezine.com?utm_source=devto
