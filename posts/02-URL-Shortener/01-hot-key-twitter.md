# Hot Key Problem — Twitter Thread

## Tweet 1 (Hook)

Consistent hashing maps every short code to exactly one Redis node. That's also why one viral link can melt your cache — 800k reads/sec, all hitting the same node, while the rest of your cluster sits idle.

#SystemDesign #SoftwareEngineering #DistributedSystems

---

## Tweet 2 (Reply to Tweet 1)

The fix isn't more Redis. You can't move a key without rehashing.

Cache the hot URL inside the app server's own memory. Request never leaves the machine. Redis sees zero reads for that key.

Works because short URL mappings are immutable — nothing to invalidate.

Full breakdown → https://leetdezine.com/url-shortener/?utm_source=twitter
