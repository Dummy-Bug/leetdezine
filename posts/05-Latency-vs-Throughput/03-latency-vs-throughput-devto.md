# Low Latency vs High Throughput: What's the Difference and When Does Each Matter?

## Platform: DEV.to
## Canonical URL: https://leetdezine.com/performance-metrics/latency-vs-throughput/?utm_source=devto
## Tags: systemdesign, distributedsystems, backend, programming

---

The first time I heard "optimize for latency," I thought it meant "make it fast." So I turned off batching, flushed writes immediately, set Kafka's `linger.ms` to 0.

The system responded faster. And handled way less load.

Latency and throughput pull in opposite directions. Making your system faster for individual requests usually means it handles fewer of them per second. Handling more per second usually means individual requests wait longer. This tradeoff shows up everywhere — and misidentifying which axis to optimize is one of the most common architecture mistakes.

---

## DB Batch Writes

Your database is getting hammered with writes. Each write goes to disk immediately.

- Latency per write: 10ms
- One thread handles: 100 writes per second

Change the approach: collect 100 records, flush in one batch. One disk operation instead of 100.

**Throughput** went up — the disk does the same work with 100× fewer operations.

**Latency** went up — the first record now waits for 99 more before anything gets written.

You traded fast individual responses for higher total capacity.

---

## Netflix's Loading Spinner

Netflix needs to send you a video. Two options:

**Option A:** stream one tiny chunk the moment it's ready. Low latency, you start watching fast. But thousands of tiny chunks = thousands of network trips per second = inefficient. Fewer users served.

**Option B:** buffer and send larger chunks. Fewer network trips, more users served per second. But you wait a few seconds before playback starts.

That loading spinner isn't a bug. Netflix deliberately accepts higher startup latency to serve more users efficiently. Same tradeoff, product-level decision.

---

## Kafka's linger.ms

This one makes the tradeoff explicit. Kafka producers have a config called `linger.ms` — how long the producer waits before flushing a batch.

```
linger.ms = 0:
  Every event fires immediately — one network call per event
  At 100K events/sec = 100K network calls/sec
  Low latency per event, terrible network efficiency

linger.ms = 5:
  Producer accumulates events for 5ms, flushes together
  At 100K events/sec ≈ 20K batch calls/sec
  Slightly higher latency per event, 5× better throughput
```

`linger.ms` is a literal dial between the two extremes. Kafka doesn't choose for you — it expects you to understand the tradeoff and set it intentionally.

---

## The Pattern

Every example is the same thing:

> Make individuals wait → serve more of them overall.

| Scenario | What you traded | What you got |
|---|---|---|
| DB batch writes | Per-record speed | Total capacity |
| Netflix buffering | Startup speed | User capacity |
| Kafka linger.ms > 0 | Message delay | Network efficiency |

The inverse is also true: processing immediately = low latency, lower throughput. You're always on this spectrum.

---

## How to Decide

Ask: **what does a bad experience look like for this system?**

- Chat message takes 5 seconds to send → users leave. **Optimize for latency.**
- Analytics pipeline runs overnight → nobody cares if a log arrived 2 seconds late. **Optimize for throughput.**
- Payment confirmation → user is staring at a loading screen. **Optimize for latency.**
- Log processing → you're crunching billions of events in bulk. **Optimize for throughput.**

In an interview, say the tradeoff out loud: *"I'm choosing batch writes here — that increases throughput but adds latency per write. Acceptable for an analytics pipeline, wrong for a payment API."*

Naming the axis is what separates a junior answer from a senior one.

---

Full performance metrics breakdown → https://leetdezine.com/performance-metrics/latency-vs-throughput/?utm_source=devto
