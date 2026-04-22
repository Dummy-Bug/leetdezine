# Post 4 — Why LPOP Is Atomic
# Platform: Twitter/X
# Day: Day 4

---

**Tweet 1** (hook)

20 app servers call Redis LPOP at the exact same millisecond.

They all get different keys. No locks. No transactions. No coordination layer.

This is why LPOP is the right primitive for a URL shortener key pool.

#SystemDesign #SoftwareEngineering #DistributedSystems

---

**Tweet 2** (insight + link)

Redis is single-threaded. Two LPOP calls at the exact same ms get different keys — guaranteed.

With a DB, you'd need SELECT FOR UPDATE SKIP LOCKED. Row-level locking on every creation.

One model. Orders of magnitude simpler.

https://leetdezine.com/03-Case-Studies/01-Foundation/02-URL-Shortener/02-Deep-Dives/?utm_source=twitter
