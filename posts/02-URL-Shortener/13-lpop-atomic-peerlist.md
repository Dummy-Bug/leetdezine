# Post 4 — Why LPOP Is Atomic
# Platform: Peerlist
# Day: Day 4

---

Here's a question that trips people in interviews: how do you prevent two app servers from grabbing the same key from a Redis pool simultaneously?

The answer: you don't have to. Redis handles it.

Redis is single-threaded. Every command — including LPOP — executes one at a time, in order. If 20 app servers call LPOP at the exact same millisecond, Redis processes them sequentially. Server 1 gets key A, which is removed. Server 2 gets key B, which is removed. It's physically impossible for two LPOP calls to return the same value.

This is the insight worth internalizing: atomicity doesn't always require locks. Sometimes it comes from the concurrency model of the tool itself.

For comparison, building the same key pool in Postgres would require `SELECT FOR UPDATE SKIP LOCKED` — row-level locking on every single creation request. Expensive, complex, and a bottleneck under high load.

Redis gives you the same correctness guarantee at O(1) with zero locking.

The batch pre-fetch compounds this: each app server grabs 100 keys at startup and refills when empty. At 1k creations/sec across 20 servers, that drops Redis traffic from 1000 LPOP calls/sec down to roughly 10 batch refills/sec. Same correctness, 100x fewer Redis round-trips.

Full breakdown: https://leetdezine.com/03-Case-Studies/01-Foundation/02-URL-Shortener/02-Deep-Dives/?utm_source=peerlist
