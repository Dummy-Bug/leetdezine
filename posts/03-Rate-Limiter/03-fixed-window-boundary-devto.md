# Fixed Window Counter Rate Limiting: How It Works, the Boundary Bug, and the Thundering Herd Problem

## Platform: DEV.to
## Canonical URL: https://leetdezine.com/03-Case-Studies/03-Expedition/01-Rate-Limiter/?utm_source=devto
## Tags: systemdesign, distributedsystems, backend, programming

---

Most engineers implement Fixed Window Counter, call it "rate limiting," and move on. It works in tests. It works in prod — until someone learns exactly when your windows reset.

Here's what's actually happening.

---

## The Algorithm

Fixed Window Counter is dead simple. One rule: 5 requests per minute for user A.

Every request, take the Unix timestamp and divide by 60:

```
window_id = floor(unix_timestamp / 60)
```

All timestamps in the same 60-second block get the same `window_id`. Store a counter per user per window in Redis. INCR on each request, check if it's over the limit.

```
INCR user:abc:/search:28350000
if count > 5 → block
else         → allow
```

One Redis operation. Simple to reason about. Fast.

In testing, it looks correct.

---

## The Boundary Bug

Here's what actually happens at runtime.

User sends 5 requests at **00:58**. Window W logs 5 — at the limit. Window W ends.

User sends 5 requests at **01:02**. Window W+1 logs 5 — at the limit.

Both windows are individually "correct." Both are within the rule.

```
Window W   (00:00–01:00): 5 requests ✓
Window W+1 (01:00–02:00): 5 requests ✓

Real 60-second span 00:58 → 01:58: 10 requests ✗
```

You allowed 10 requests in a genuine 60-second window — double the limit you set.

This is deterministically exploitable. Wait until 00:58, burst 5, wait 4 seconds for the window to flip, burst 5 more. You double your effective rate every minute, and the rate limiter never flags it.

---

## The Thundering Herd at Window Reset

The boundary bug has a second effect that only shows up in production at scale.

At 01:00:00, every counter in your system resets. Every user who was blocked in Window W gets a fresh counter the same second. At 100K active users hitting their limit and waiting for the reset, you get a coordinated surge — thousands of requests firing simultaneously, triggered by your own rate limiter.

This is a thundering herd. Except it's periodic and predictable: every 60 seconds, exactly when your window flips.

In testing with single users, you never see it. In prod under load, it creates a spike pattern that's hard to diagnose because it looks like organic traffic.

---

## Is This a Dealbreaker?

Depends on what you're protecting.

**For /search, /feed, general API access:**
A brief 2× burst at window edges causes no meaningful harm. Your infrastructure handles a momentary spike. Fixed Window Counter is the right choice — fast, simple, cheap on Redis ops, easy to explain.

**For /login, /payment, /password-reset:**
The 2× burst is a security issue. An attacker who knows your window size (it's often guessable or documented) can time requests to double their brute-force attempts every window. That's not acceptable for sensitive endpoints.

---

## The Fix: Sliding Window Counter

Sliding Window Counter keeps two integers per user — the current window counter and the previous window counter. When a request arrives:

```
seconds_elapsed  = timestamp % 60
overlap_fraction = (60 - seconds_elapsed) / 60
estimate         = (prev_count × overlap_fraction) + curr_count
```

It estimates how many requests fell in the true rolling 60-second window, weighted by how much of the previous window overlaps. No boundary bug. No 2× burst.

```
Memory cost: 2 integers per user = 16MB for 1M users (same as Fixed Window)
Redis ops:   GET + GET + INCR wrapped in a Lua script for atomicity
Accuracy:    approximate, assumes uniform distribution in prev window
             error is small and non-exploitable — can't be gamed by timing
```

This is what Nginx and Cloudflare use in production. Same memory footprint as Fixed Window, meaningfully better accuracy for sensitive endpoints.

---

## The Rule

Fixed Window Counter for general access. Sliding Window Counter (or Sliding Window Log) for anything sensitive.

The mistake isn't using Fixed Window Counter — it's using it everywhere without thinking about what the boundary bug costs you on specific endpoints.

Full Rate Limiter case study → https://leetdezine.com/03-Case-Studies/03-Expedition/01-Rate-Limiter/?utm_source=devto
