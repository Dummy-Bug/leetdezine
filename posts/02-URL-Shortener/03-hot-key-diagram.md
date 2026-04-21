# Hot Key Problem — ASCII Diagram

```
BEFORE (hot key problem):
─────────────────────────────────────────────────────
Request: x7k2p9?  →  App Server  →  Redis Node 2 
Request: x7k2p9?  →  App Server  →  Redis Node 2 
Request: x7k2p9?  →  App Server  →  Redis Node 2 
                                     (800k reads/sec)

AFTER (local app server cache):
─────────────────────────────────────────────────────
Request: x7k2p9?  →  App Server
                      │
                      ▼
                 Local Cache ✓  →  return URL
                 (Redis never involved)

Detection: in-memory counter per key
           x7k2p9 > 50k reads/sec → HOT → cache locally
```
