# Latency vs Throughput — Twitter Thread

## Tweet 1 (Hook)

Kafka has a config: `linger.ms`. Set it to 0 — messages fire instantly. Low latency. Terrible throughput.

Set it higher — throughput skyrockets. But messages now wait in a buffer before they go out.

This isn't a bug. It's the same tradeoff hiding inside every distributed system.

#SystemDesign #SoftwareEngineering #DistributedSystems

---

## Tweet 2 (Reply to Tweet 1)

Making your system faster ≠ making it handle more load.

Batching = make individuals wait → serve more of them overall (high throughput, high latency)
Immediate processing = respond fast → use resources inefficiently (low latency, lower throughput)

DB writes, Netflix buffering, Kafka — same tradeoff, different problem.

→ https://leetdezine.com/01-Concepts/02-Fundamentals/01-Performance-Metrics/04-Latency-vs-Throughput/?utm_source=twitter
