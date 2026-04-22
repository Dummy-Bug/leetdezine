# Post 3 — What Happens When Redis Dies
# Platform: Peerlist
# Day: Day 3

---

Most system design answers for "what if Redis fails" stop at: "we have Redis replication." That's a configuration, not a plan.

Here's what actually happens when Redis goes down in a URL shortener at scale.

Redis absorbs roughly 80% of all redirect reads. At 1M reads/sec, the DB only sees 200k/sec — manageable across 16 read nodes. Redis dies. 1M reads/sec hits the DB directly.

Without a circuit breaker, every request first tries Redis, waits 500ms for the timeout, then falls back to DB. At 1M requests/sec, that's not a fallback — that's your entire thread pool stalled for half a second each. Connection queues pile up. DB never even gets a clean shot at the traffic.

The circuit breaker fixes this. After five Redis failures in ten seconds, the circuit opens — all requests skip Redis immediately and go straight to DB. No timeout overhead. DB load is high but the cascade is stopped.

Still not enough. DB capacity at full load is around 800k reads/sec. The remaining 200k need to be shed. The API Gateway throttles redirect requests and returns 503 to that overflow. The system degrades — but doesn't collapse.

The trap engineers fall into: "auto-scaling handles this." A new Postgres replica takes minutes to provision, catch up WAL, and pass health checks. Your traffic spike is immediate. Auto-scaling is for gradual growth, not cache failure.

Full breakdown: https://leetdezine.com/03-Case-Studies/01-Foundation/02-URL-Shortener/02-Deep-Dives/?utm_source=peerlist
