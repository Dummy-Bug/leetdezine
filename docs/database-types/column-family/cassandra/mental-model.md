---
title: Cassandra Architecture — Read Path and Write Path Mental Model
---

# Cassandra — The Mental Model

> [!abstract] Cassandra is a distributed column-family store built for massive write throughput and predictable low-latency reads — as long as you know your partition key. Every internal design decision flows from that constraint.

## The mental model

```
Client Write
     │
     ├──→ Coordinator Node (routes to correct node via ring)
     │         │
     │         ├──→ CommitLog (disk, append-only, durability)
     │         └──→ MemTable (memory, sorted, fast)
     │                   │ (when full)
     │                   ↓
     │               SSTable (disk, sorted, immutable)
     │                   │ (over time)
     │                   ↓
     │               Compaction (merge SSTables, keep latest version)
     │
     └──→ Replicated to N nodes (RF=3 means 3 copies)

Client Read
     │
     ├──→ Coordinator routes to replica nodes
     ├──→ Bloom Filter per SSTable → skip files that don't have the key
     └──→ Read MemTable + remaining SSTables → merge → return latest
```
