# Fixed Window Counter — Boundary Bug & Thundering Herd — Twitter Thread

## Tweet 1 (Hook)

Fixed Window Counter silently lets users through at 2× the limit. Every time.

5 requests at 00:58. 5 at 01:02. Both windows say "within limit." That's 10 requests in 60 seconds — double.

And when the window resets at 01:00, every blocked user fires at once. Thundering herd.

#SystemDesign #SoftwareEngineering #DistributedSystems

---

## Tweet 2 (Reply to Tweet 1)

The fix isn't always a better algorithm.

For /search or /feed — a brief 2× burst causes no real harm. Fixed Window is fast, simple, one Redis op.

For /login or /payment — an attacker who knows your window resets at :00 can time their burst to double their brute-force attempts every minute.

Full Rate Limiter deep dive → https://leetdezine.com/03-Case-Studies/03-Expedition/01-Rate-Limiter/?utm_source=twitter
