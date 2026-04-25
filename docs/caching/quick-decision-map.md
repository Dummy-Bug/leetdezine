---
title: Cache Writing Strategies — Quick Decision Map (Cache-Aside, Write-Through, Write-Back)
---

# Cache Writing Strategies — Quick Decision Map

> [!abstract] When does data enter the cache? When does it get written back to the DB? Five patterns — each with a different answer to these two questions. Choosing the wrong one means either stale data, slow writes, or data loss.

## The quick decision map

```
Read-heavy, app controls cache?        → Cache-Aside (most common)
Read-heavy, want cleaner app code?     → Read-Through
Write-heavy, consistency matters?      → Write-Through
Write-heavy, speed matters most?       → Write-Back (accept data loss risk)
Write-once data, rarely read back?     → Write-Around
```
