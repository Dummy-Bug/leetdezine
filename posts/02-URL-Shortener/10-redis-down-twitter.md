# Post 3 — What Happens When Redis Dies
# Platform: Twitter/X
# Day: Day 3

---

**Tweet 1** (hook)

Redis fails in your URL shortener.

80% cache coverage → gone. 1M reads/sec now hits DB nodes sized for 200k/sec.

Auto-scaling won't save you — new replicas take minutes. The surge is immediate.

#SystemDesign #SoftwareEngineering #DistributedSystems

---

**Tweet 2** (insight + link)

The fix: circuit breaker + API Gateway throttling.

Circuit opens immediately → requests skip Redis, go straight to DB. No 500ms timeout stall per request.
API GW throttles reads → returns 503 to some percentage → DB survives.

Partial availability beats total cascade.

https://leetdezine.com/03-Case-Studies/01-Foundation/02-URL-Shortener/02-Deep-Dives/?utm_source=twitter
