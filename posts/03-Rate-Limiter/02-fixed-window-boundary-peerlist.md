# Why Does Your Rate Limiter Silently Allow 2× the Requests You Set?

## Platform: Peerlist

---

There's a bug in Fixed Window Counter that most candidates miss — and most production systems ship anyway.

The rule is "5 requests per minute." The implementation groups timestamps into 60-second buckets and counts per bucket. Looks correct. Works in testing.

Here's what breaks at runtime: buckets reset at fixed clock boundaries. Send 5 requests at 00:58, then 5 at 01:02. Window one sees 5 — fine. Window two sees 5 — fine. But in the actual 60-second span from 00:58 to 01:58, you let through 10 requests. The "per minute" rule you configured is silent about this.

It gets worse. When the window flips at 01:00, every user who was blocked in the previous window gets a fresh counter simultaneously. At scale, that's thousands of requests hitting your service in the same second. Your own rate limiter just created a thundering herd — periodic, predictable, synchronized by your window boundaries.

The algorithm isn't broken — it's the wrong tool for specific endpoints. For /search or /feed, a 2× burst is harmless. For /login or /password-reset, you've doubled the brute-force attack surface for anyone who knows your window size.

Know which one you're deploying.

→ https://leetdezine.com/03-Case-Studies/03-Expedition/01-Rate-Limiter/?utm_source=peerlist
