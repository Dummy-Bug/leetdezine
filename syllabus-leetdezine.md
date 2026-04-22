# LeetDezine — Syllabus Architecture Reference

## Overview

Three completely self-contained learning paths. Each path covers everything the tier below it has, plus its own layer on top. A reader picks ONE path and never needs to touch another.

```
SDE-1 (0–2 YOE)   → docs/00-SDE-1/
SDE-2 (2–6 YOE)   → docs/00-SDE-2/
SDE-3 (6+ YOE)    → docs/00-SDE-3/
```

**Key rule:** SDE-2 = SDE-1 content + SDE-2 layer. SDE-3 = SDE-2 content + SDE-3 layer. No path depends on another.

---

## SDE-1 Path — docs/00-SDE-1/

**Audience:** 0–2 YOE. Freshers, junior devs, small startup engineers.
**Bar:** Know what things are, why they exist, and how to design simple systems.

### Files

```
docs/00-SDE-1/
  00-Syllabus.md
  01-Networking.md
  02-APIs.md
  03-Databases.md
  04-Caching.md
  05-Scalability-Basics.md
  06-Storage.md
  07-Security-Basics.md
  08-Estimation.md
  09-Message-Queues.md
  Case-Studies/
    01-URL-Shortener.md
    02-Pastebin.md
    03-Leaderboard.md
    04-Simple-Social-Feed.md
```

### Topics Per File

**01-Networking**
- How the Internet Works (IP, packets, routers, NAT)
- OSI Model (7 layers, why it matters for L4 vs L7)
- TCP vs UDP (handshake, reliability, when to use which, connection pooling)
- HTTP and HTTPS (request/response, methods, status codes, HTTP/1.1 vs HTTP/2, TLS)
- DNS (resolution flow, record types, TTL)
- CDN (edge servers, cache-control, static vs dynamic)
- Proxies (forward, reverse, API gateway)
- WebSockets and Real-Time (WebSocket upgrade, long polling, SSE, when to use each)

**02-APIs**
- REST Fundamentals (stateless, uniform interface, URL design, JSON)
- API Design (versioning, pagination offset vs cursor, error format, idempotency keys)
- gRPC (awareness — what it is, when to prefer over REST)
- Async API Pattern (202 Accepted + job ID, webhooks)
- Webhooks (push-based, HMAC verification, idempotent handler)
- Authentication in APIs (API keys, basic auth, Bearer tokens, JWT basics)
- Rate Limiting (consumer perspective — 429 handling, Retry-After)

**03-Databases**
- SQL Fundamentals (tables, PKs/FKs, queries, JOINs, aggregations)
- ACID Properties (all four, ACID vs BASE)
- Indexing Basics (B+ Tree concept, composite index leftmost prefix, covering index, when not to index)
- NoSQL Introduction (key-value, document, column-family awareness, SQL vs NoSQL choice)
- Schema Design (normalization, relationships, junction tables, no float for money, soft vs hard deletes)
- Basic Scaling (read replicas, replication lag, connection pooling, don't shard on day one)

**04-Caching**
- What Caching Is (hit vs miss, hit ratio > 90%, what not to cache)
- Where to Cache (browser, local in-process, distributed Redis, two-level)
- Cache Population Strategies (cache-aside, read-through, write-through, write-back, write-around)
- Cache Eviction Policies (LRU, LFU, FIFO, TTL, LRU vs LFU distinction, TTL vs eviction distinction)
- Cache Invalidation (TTL, manual, why it's hard)
- Cache Problems (stampede, avalanche, penetration, cold start — awareness + fix)
- Redis Basics (data structures + use cases, TTL, RDB vs AOF)

**05-Scalability-Basics**
- Vertical vs Horizontal (cost, limits, tradeoffs)
- Stateless Services (what stateless means, sessions via JWT/Redis, common mistake)
- Auto-Scaling (reactive vs predictive, cold start, why it doesn't fix DB bottleneck)
- Load Balancing (round-robin, least connections, IP hash, health checks, sticky sessions, active-active vs active-passive)
- Single Points of Failure (what a SPOF is, N+1 rule, load balancer itself needs redundancy)
- API Gateway (single entry point, what it handles, vs load balancer)
- Replication Basics (primary-replica, read scaling, replication lag, read-your-own-writes)

**06-Storage**
- Types of Storage (block, file, object — what each is for)
- Object Storage (S3 model, why files don't belong in DB, metadata in DB + binary in S3, pre-signed URLs)
- Storage Classes (hot/warm/cold, lifecycle policies, cost vs access speed)
- File Uploads (direct upload to S3, multipart, resumable, chunk size 4-8 MB)
- Content-Addressable Storage (SHA256 as key, deduplication concept)

**07-Security-Basics**
- Authentication vs Authorization (who you are vs what you can do)
- Authentication Methods (session-based, JWT, OAuth 2.0, API keys, when to use each)
- JWT Basics (header.payload.signature, stateless, not encrypted, access + refresh token pattern)
- Authorization Models (RBAC, ACL, when to use which)
- Password Security (never plaintext, hashing vs encryption, bcrypt, salting)
- Encryption (in transit = TLS, at rest = AES-256, both required)
- HTTPS and TLS (why HTTP is unsafe, what TLS provides, certificates, HSTS)
- Common Vulnerabilities (SQL injection, XSS, CSRF, least privilege)

**08-Estimation**
- Numbers to Know (latency table, data sizes, traffic rules of thumb, seconds in a day)
- Estimation Framework (DAU → QPS → storage → bandwidth → memory → server count)
- Read vs Write Ratio (why systems are read-heavy, how ratio drives architecture)
- When Estimation Changes Architecture (QPS thresholds for caching, sharding, CDN)
- Worked Examples (URL shortener, photo sharing app)

**09-Message-Queues**
- Why Async Processing (sync vs async, request path problem, spike absorption, decoupling)
- Queue Basics (producer/consumer, point-to-point vs pub-sub, acknowledgement)
- Visibility Timeout (message lease, crash recovery, heartbeat extension)
- DLQ (what it is, why messages end up there, why you need one)
- Retry and Backoff (exponential backoff, jitter, max retry limit)
- Common Use Cases (email/notifications, image processing, order pipelines)
- Tools (Redis queue, SQS, RabbitMQ, Kafka awareness only)

### Case Studies (SDE-1)
- URL Shortener — simplified (no pre-generated keys, no cold storage, hash + base62, caching)
- Pastebin — simplified (short ID, S3 for content, TTL expiry, background cleanup)
- Leaderboard — Redis sorted set, DB as source of truth, handling ties
- Simple Social Feed — pull model, pagination, when fanout becomes a problem (teaser to SDE-2)

---

## SDE-2 Path — docs/00-SDE-2/

**Audience:** 2–6 YOE. Mid-level engineers targeting SDE-2 at product companies.
**Bar:** Know tradeoffs, design mid-complexity systems with depth, justify every choice.

### Files (Gemini-generated, cleaned up)

```
docs/00-SDE-2/
  01-Networking-Fundamentals.md
  02-Back-of-Envelope-Estimation.md
  03-Core-Concepts.md
  04-Caching.md
  05-Storage-and-Databases.md
  06-Messaging-and-Event-Driven.md
  07-Distributed-Systems.md
  08-Infrastructure-and-Reliability.md
  09-Supplementary-Topics.md
  10-Interview-Framework.md
  11-Case-Studies.md
```

### What Was Stripped From SDE-2 (Moved to SDE-3)

The original Gemini-generated SDE-2 syllabus contained ~30% SDE-3 content. The following were removed:

**From Networking:**
- QUIC / HTTP/3 internals
- WebRTC / STUN / TURN / ICE
- GSLB / Anycast
- Email protocols (SMTP, IMAP, POP3)

**From Core Concepts:**
- Redlock (multi-node distributed lock)
- Full consistency spectrum (linearizable → sequential → causal → monotonic → RYW → eventual)
- PACELC theorem
- Snapshot isolation internals, write skew

**From Storage:**
- B+ Tree page splits and write amplification
- LSM compaction strategies (leveled vs tiered)
- CDC log-based (Debezium, WAL reading), outbox/inbox pattern
- Cassandra write/read path internals (CommitLog, MemTable, SSTable, tombstones)
- Bigtable/HBase internals
- S2 geometry deep dive
- 2PC blocking problem (coordinator crash = in-doubt transactions)
- Spanner/TrueTime details
- Data migration at scale (dual-write, shadow reads, cutover)
- Schema migration on live tables (gh-ost, expand-and-contract)

**From Messaging:**
- Backpressure (consumer lag monitoring, producer load shedding)
- Event Sourcing
- CQRS
- Stream processing (windowing, watermarks, checkpointing)
- MapReduce / Spark
- Lambda / Kappa architecture
- Schema evolution (Avro, Schema Registry, Protobuf)

**From Distributed Systems:**
- Entire Raft section (leader election, log replication, failure cases)
- Entire Paxos section (proposer/acceptor/learner, two phases, livelock)
- ZooKeeper ZAB protocol details
- etcd leases and fencing tokens
- Lamport clocks
- Vector clocks
- TrueTime
- CRDTs
- Gossip protocol
- Phi Accrual failure detector
- Merkle trees

**From Infrastructure:**
- Service mesh / sidecar pattern (Istio, Envoy)
- Data migration at scale
- HLS / DASH adaptive bitrate streaming
- Multi-region conflict resolution deep dive

**From Supplementary:**
- Lambda / Kappa architecture

**From Case Studies:**
- Tier 4: Google Maps, Google Docs, Gmail, Kafka from scratch, Redis from scratch, DynamoDB from scratch

### What SDE-2 Retains

Everything SDE-1 has, plus:
- Full TCP/UDP, HTTP/1.1 + HTTP/2, DNS load balancing, CDN push vs pull
- gRPC (4 streaming modes), GraphQL N+1, async API, webhooks, idempotency keys
- Jeff Dean latency numbers, estimation framework with server count
- Tail latency amplification, jitter, SLO/SLA/error budget
- MTBF/MTTR/RTO/RPO, active-active vs active-passive
- Circuit breaker, retry + jitter, bulkhead, deadline propagation
- WAL, sync vs async replication
- Optimistic vs pessimistic locking, MVCC basic, idempotency keys
- Four isolation anomalies, READ COMMITTED → SERIALIZABLE
- CAP theorem (CP vs AP), eventual vs strong consistency (basic)
- State machines with WHERE guard
- Full caching section (all write strategies, LRU vs LFU, all cache problems)
- SQL normalization, materialized views, B+ Tree concept, LSM awareness
- Replication, sharding (all strategies), cross-shard queries, hotspot
- Cassandra (partition key, clustering key, consistency levels, query-first modeling)
- Elasticsearch (inverted index, TF-IDF, BM25)
- S3, pre-signed URLs, multipart upload, content-addressable storage
- NewSQL (awareness level — Spanner, Aurora, Cosmos DB)
- Connection pooling, read/write splitting, cursor pagination, OLTP vs OLAP
- Geospatial (Geohash, Quadtree, PostGIS), 2PC + Saga (concept level)
- Full Kafka deep dive (partitions, offsets, consumer groups, ISR, retention, compacted topics)
- Kafka vs RabbitMQ vs SQS comparison
- Outbox pattern (added back at SDE-2 level as it's needed here)
- Consistent hashing + vnodes, replication strategies, quorum basics
- Distributed locking (Redis SET NX PX), failure detection awareness
- Microservices vs monolith, BFF pattern
- All 5 rate limiting algorithms, distributed rate limiting with Lua
- Bloom filter, HyperLogLog, Count-Min Sketch, Skip List
- Geospatial indexing, Snowflake ID generation
- Multi-region architecture (active-active, GeoDNS, read local write global)
- Storage tiers, chunked/resumable upload, delta sync (Dropbox)
- Rolling/blue-green/canary deployment
- Observability (logging, metrics, distributed tracing, alerting)
- Reconciliation, graceful degradation, feature flags
- Full interview framework (45-min structure, NFR cheat sheet, tradeoffs)
- Case studies Tier 1–3 (26 case studies, up to Netflix and Stock Broker)

---

## SDE-3 Path — docs/00-SDE-3/

**Audience:** 6+ YOE. Targeting L5/L6 at FAANGM (Google, Meta, Amazon, Apple, Netflix, Microsoft).
**Bar:** Strong hire. Correctness boundary, operational ownership, migration path, multi-region implications, disaster recovery.

### Files

```
docs/00-SDE-3/
  00-Syllabus.md
  01-Networking.md
  02-Estimation.md
  03-Core-Concepts.md
  04-Caching.md
  05-Storage-and-Databases.md
  06-Messaging-and-Event-Driven.md
  07-Distributed-Systems.md
  08-Infrastructure-and-Reliability.md
  09-Observability.md
  10-Interview-Framework.md
  Case-Studies/
    00-Overview.md
```

### Bold = SDE-3 Additions

In all SDE-3 files, **bold text marks topics that are new at SDE-3** — not present in SDE-1 or SDE-2. Everything else is carried from SDE-2.

### Key SDE-3 Additions Per File

**01-Networking (SDE-3 additions)**
- QUIC / HTTP/3 (0-RTT, UDP-based HOL fix)
- WebRTC (STUN/TURN/ICE, peer-to-peer media)
- GSLB / Anycast (cross-datacenter routing)
- mTLS (mutual authentication, certificate rotation)
- TCP congestion control internals (CUBIC, BBR)
- CDN internals (origin shield, PoP hierarchy, CDN-to-CDN peering)
- Email protocols (SMTP, IMAP, POP3, MX records)
- Multi-region networking (private backbone vs public internet)

**03-Core-Concepts (SDE-3 additions)**
- Redlock (multi-node, Kleppmann's critique, when to use)
- Full consistency spectrum (all 6 levels with guarantees)
- PACELC theorem (PA/EL, PC/EC, PA/EC)
- Snapshot isolation internals (version chains, transaction ID watermarks)
- Write skew (what it is, why MVCC doesn't prevent it, fix)
- Predicate locking

**05-Storage-and-Databases (SDE-3 additions)**
- B+ Tree internals (page structure, page splits, write amplification)
- LSM internals (compaction strategies — leveled vs tiered, write amplification comparison)
- CDC log-based (Debezium, WAL reading, what it captures)
- Outbox pattern / Inbox pattern
- Cassandra write path (CommitLog → MemTable → SSTable)
- Cassandra read path (Bloom filter → SSTable scan)
- Cassandra compaction and tombstones
- Bigtable/HBase (tablet server, compaction, row key design)
- S2 geometry (Hilbert curve, cell hierarchy, levels, used by Google/Uber)
- 2PC blocking problem (coordinator crash = in-doubt transactions)
- Spanner (TrueTime uncertainty window, commit wait, 2PC with Paxos groups)
- Data migration at scale (dual-write, backfill, shadow reads, cutover, rollback)
- Schema migration on live tables (gh-ost, pg_repack, expand-and-contract)

**06-Messaging (SDE-3 additions)**
- Kafka internals (segment files, ISR guarantee, acks=all/1/0, transactional exactly-once)
- Backpressure (consumer lag, threshold-based scaling, producer load shedding)
- Event sourcing (immutable log, projection, snapshot, vs CDC)
- CQRS (write model vs read model, sync via event handler)
- Stream processing (tumbling/sliding/session windows, watermarks, stateful, checkpointing)
- MapReduce (map/shuffle/reduce, Hadoop)
- Spark (DAG, in-memory, 10-100x faster)
- Lambda architecture (batch + speed + serving, two codebases problem)
- Kappa architecture (stream-only, Kafka replay)
- Schema evolution (backward/forward compatibility, Avro + Schema Registry, Protobuf field numbers)

**07-Distributed-Systems (SDE-3 additions)**
- FLP Impossibility (no deterministic consensus with one failure in async system)
- Raft full deep dive (randomized timeouts, election safety, log replication AppendEntries, ghost leader, fencing tokens, all failure cases)
- ZooKeeper ZAB protocol, ephemeral nodes, watches, leader election flow
- etcd (Raft-based, leases, fencing tokens, Kubernetes backbone)
- Paxos (proposer/acceptor/learner, two phases, value inheritance, livelock fix)
- Lamport clocks (3 rules, happens-before, limitation)
- Vector clocks (per-node counters, causality vs concurrency detection)
- TrueTime (GPS + atomic clocks, uncertainty interval, commit wait)
- CRDTs (G-Counter, OT vs CRDT, Google Docs vs Figma)
- Gossip protocol (epidemic propagation, O(log n), counter tables)
- Phi Accrual failure detector (suspicion score, sliding window, φ=8 in Cassandra)
- Merkle trees (hash tree, O(log n) replica comparison, anti-entropy in leaderless)

**08-Infrastructure (SDE-3 additions)**
- Service mesh / sidecar (Istio, Envoy, mTLS without code changes, traffic splitting)
- Multi-region conflict resolution deep (LWW, CRDT, app merge)
- Data residency / GDPR
- Delta sync deep dive (chunk-level diff, Dropbox flow, conflict copy vs CRDT)
- HLS / DASH (manifest file, segment delivery, buffer management, CDN, storage cost)
- Count-Min Sketch internals (2D array, always overestimates)
- HyperLogLog internals (max leading zeros, O(log log n) memory)
- Bloom filter internals (bit array, false positive rate calculation)
- S2 geometry in infrastructure context

**09-Observability (SDE-3 additions)**
- Metrics at scale (cardinality explosion, downsampling, Prometheus federation, remote write)
- Sampling strategies (head-based vs tail-based, tradeoffs, practical approach)
- Chaos engineering (Chaos Monkey, game days, blast radius)

**10-Interview-Framework (SDE-3 additions)**
- What strong hire means at FAANGM (correctness boundary, operational ownership, migration path)
- SDE-3 specific question types (migration, multi-region, disaster recovery, correctness)

### Case Studies (SDE-3)

All 26 SDE-2 case studies carried forward at SDE-3 depth, plus:
- Tier 1 cases revisited with multi-region, migration path, observability
- Tier 3 cases get correctness boundary, compensating transaction idempotency, operational recovery
- **Tier 4 (new at SDE-3):**
  - Google Maps (A*, S2, hierarchical routing, traffic stream processing)
  - Google Docs (OT vs CRDT, operational log, offline merge)
  - Gmail (SMTP/IMAP, threading algorithm, search at scale, storage quotas)
  - Kafka from Scratch (segment files, ISR, consumer groups, compaction, KRaft)
  - Redis from Scratch (consistent hashing, LRU, AOF, Sentinel, 16384 hash slots, gossip)
  - DynamoDB from Scratch (vnodes, vector clocks, quorum, Merkle trees, gossip, hinted handoff)

---

## Content Generation Status

| Path | Syllabus Files | Content Files |
|---|---|---|
| SDE-1 | ✅ Complete (9 topic files + 4 case studies) | ❌ Not generated yet |
| SDE-2 | ✅ Complete (11 files, cleaned of SDE-3) | ✅ Partially generated (existing docs/) |
| SDE-3 | ✅ Complete (10 topic files + case studies overview) | ❌ Not generated yet |

---

## Folder Structure Summary

```
docs/
  00-SDE-1/               ← SDE-1 syllabus (skeleton files only)
    00-Syllabus.md
    01-Networking.md
    02-APIs.md
    03-Databases.md
    04-Caching.md
    05-Scalability-Basics.md
    06-Storage.md
    07-Security-Basics.md
    08-Estimation.md
    09-Message-Queues.md
    Case-Studies/
      01-URL-Shortener.md
      02-Pastebin.md
      03-Leaderboard.md
      04-Simple-Social-Feed.md

  00-SDE-2/               ← SDE-2 syllabus (Gemini-generated, cleaned up)
    01-Networking-Fundamentals.md
    02-Back-of-Envelope-Estimation.md
    03-Core-Concepts.md
    04-Caching.md
    05-Storage-and-Databases.md
    06-Messaging-and-Event-Driven.md
    07-Distributed-Systems.md
    08-Infrastructure-and-Reliability.md
    09-Supplementary-Topics.md
    10-Interview-Framework.md
    11-Case-Studies.md

  00-SDE-3/               ← SDE-3 syllabus (skeleton files only)
    00-Syllabus.md
    01-Networking.md
    02-Estimation.md
    03-Core-Concepts.md
    04-Caching.md
    05-Storage-and-Databases.md
    06-Messaging-and-Event-Driven.md
    07-Distributed-Systems.md
    08-Infrastructure-and-Reliability.md
    09-Observability.md
    10-Interview-Framework.md
    Case-Studies/
      00-Overview.md

  01-Concepts/            ← Existing SDE-2 level content (source material)
  03-Case-Studies/        ← Existing SDE-2 case studies (source material)
```

---

## Key Design Decisions

1. **Three self-contained paths** — no cross-path dependencies. A user picks one path and reads it start to finish.

2. **Bold = SDE-3 additions** — in SDE-3 files, bold text marks topics not present in SDE-1 or SDE-2. Lets users and content reviewers identify what's genuinely new at each tier.

3. **SDE-1 case studies are simpler versions** — URL Shortener and Pastebin exist at all three levels but with different depth. SDE-1 = pull model, basic caching. SDE-2 = full deep dives with failure modes. SDE-3 = multi-region, migration, correctness boundary.

4. **Monetization boundary (planned):**
   - SDE-1 → free (top-of-funnel)
   - SDE-2 → 50% free, 50% paid
   - SDE-3 → 25% free, 75% paid

5. **Content generation next steps:**
   - SDE-1 content needs to be generated from scratch (syllabus exists, content does not)
   - SDE-2 content partially exists in docs/01-Concepts/ and docs/03-Case-Studies/ and needs to be mapped/refactored to match the syllabus structure
   - SDE-3 content needs to be generated from scratch (syllabus exists, content does not)
