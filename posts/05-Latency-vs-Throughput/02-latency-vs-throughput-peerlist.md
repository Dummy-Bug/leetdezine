# Why Does Making Your System Faster Sometimes Make It Handle Less Load?

## Platform: Peerlist

---

I was debugging a Kafka producer once — messages were arriving to consumers too late. The fix felt obvious: turn off batching, set `linger.ms` to 0, make everything immediate.

Throughput collapsed.

That's when it clicked: latency and throughput aren't the same axis. Optimizing one often hurts the other.

The intuition: when you batch, you make individual requests wait — but you serve far more of them per second. When you process immediately, every request gets a fast response — but your infrastructure handles fewer of them overall.

Netflix accepts a loading spinner at startup (higher latency) to serve millions of users efficiently (higher throughput). DB batch writes trade individual write speed for total capacity. Kafka's `linger.ms` is literally a dial between the two extremes.

The question to ask: what does a bad experience look like for this system?

Waiting 5 seconds for a chat message? Optimize for latency. Processing billions of analytics events overnight? Optimize for throughput. Pick the wrong axis and you're solving the wrong problem entirely.

→ https://leetdezine.com/performance-metrics/latency-vs-throughput/?utm_source=peerlist
