# Performance Metrics — Overview

> Every architecture decision is a response to one of these metrics being bad. Know them before designing anything.

> [!abstract] Before you can design a system, you need a vocabulary for what "good" looks like. This folder builds that vocabulary — latency, throughput, bandwidth, and percentiles are the four measurements that appear in every design discussion. Without them you can't define requirements, justify decisions, or identify bottlenecks.

---

## Files in this folder

| File | Topic |
|---|---|
| [Introduction](01-Introduction.md) | What performance metrics are and why they matter |
| [Latency](02-Latency.md) | Round trip time, sources of delay, RAM vs disk numbers |
| [Throughput](03-Throughput.md) | RPS/QPS, threads, what happens under load |
| [Latency vs Throughput](04-Latency-vs-Throughput.md) | Why optimizing one can hurt the other |
| [Bandwidth](05-Bandwidth.md) | Data flow per second, the speed of light misconception |
| [Bandwidth vs Latency vs Throughput](06-Bandwidth-vs-Latency-vs-Throughput.md) | Three different bottlenecks, three different solutions |
| [Percentiles](07-Percentiles.md) | P50/P95/P99/P999, why averages lie |
| [Interview Cheatsheet](08-Interview-Cheatsheet.md) | How to apply all of this in a design interview |
| [SDE-1](09-Interview-Questions/SDE-1.md), [SDE-2](09-Interview-Questions/SDE-2.md), [SDE-3](09-Interview-Questions/SDE-3.md) | SDE-1, SDE-2, SDE-3 questions with full answers |
