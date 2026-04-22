# Post 4 — Why LPOP Is Atomic
# Platform: Twitter/X + Peerlist (screenshot this as image)
# Day: Day 4

---

```
20 app servers, same millisecond, all calling LPOP

App Server 01 ──┐
App Server 02 ──┤
App Server 03 ──┤
App Server 04 ──┤
     ...        ├──→  Redis (single-threaded event loop)
App Server 17 ──┤
App Server 18 ──┤        Key pool:
App Server 19 ──┤        ["x7k2p9", "k2m8q1", "p9n3r7", "n4q8r2", ...]
App Server 20 ──┘
                              ↓ processed one at a time

                    Server 01  →  "x7k2p9"  (removed from pool)
                    Server 02  →  "k2m8q1"  (removed from pool)
                    Server 03  →  "p9n3r7"  (removed from pool)
                    Server 04  →  "n4q8r2"  (removed from pool)
                       ...

                    Zero locks. Zero duplicates. Impossible to collide.

─────────────────────────────────────────────────────────────────────

Compare: same pool in Postgres

App Server 01 ──→  SELECT short_code FROM key_pool LIMIT 1
App Server 02 ──→  SELECT short_code FROM key_pool LIMIT 1
                        ↓
                   Both read "x7k2p9" before either deletes it
                        ↓
                   DUPLICATE ✗

Fix requires: SELECT FOR UPDATE SKIP LOCKED
              → row-level locking on every creation request
              → expensive, blocks under high concurrency
```
