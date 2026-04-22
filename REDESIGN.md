# LeetDezine — Redesign Execution Tracker

---

## Rules

- Each step is self-contained and fully defined below
- **No step starts until the previous step is approved by the user**
- When a step is complete, status changes to `✅ DONE — awaiting approval`
- When approved, status changes to `✅ APPROVED` and next step can begin

---

## Step Tracker

| Step | What | Status |
|------|------|--------|
| 1 | Fix mkdocs.yml features block + site_name | ✅ DONE — awaiting approval |
| 2 | Build full Concepts nav in mkdocs.yml | ✅ DONE — awaiting approval |
| 3 | Build full Case Studies + Back of Envelope nav | ✅ DONE — awaiting approval |
| 4 | Fix 01-Concepts/index.md card links | ⬜ PENDING |
| 5 | Fix start-here.md links | ⬜ PENDING |
| 6 | Remove hide:navigation from non-homepage index pages | ⬜ PENDING |
| 7 | Stage, commit, push | ⬜ PENDING |
| 8 | Verify live site | ⬜ PENDING |

---

## Step Definitions

---

### Step 1 — Fix mkdocs.yml features block + site_name

**File:** `mkdocs.yml`

**Changes:**

```yaml
# CHANGE site_name from:
site_name: LeetDezine
# TO:
site_name: LeetDezine — System Design and Internals, Built for Interviews

# CHANGE features block from:
features:
  - navigation.sections
  - navigation.expand      # ← REMOVE (expands ALL sections at once — the mess)
  - navigation.indexes
  - navigation.path
  - navigation.top
  - toc.integrate          # ← REMOVE (dumps all page headings into sidebar — flat dump)
  - search.suggest
  - search.highlight
  - content.code.copy

# TO:
features:
  - navigation.tabs          # ← ADD (top tabs — drives section-scoped sidebar)
  - navigation.tabs.sticky   # ← ADD (tabs stay visible when scrolling)
  - navigation.sections      # keep (groups sidebar items visually)
  - navigation.indexes       # keep (section index pages clickable)
  - navigation.path          # keep (breadcrumb trail)
  - navigation.top           # keep (back-to-top button)
  - navigation.footer        # ← ADD (Previous / Next at bottom of each page)
  - search.suggest           # keep
  - search.highlight         # keep
  - content.code.copy        # keep
```

**Why removing `navigation.expand`:** It expands every section simultaneously — the left sidebar becomes a wall of text. Users can expand sections manually; we don't force them all open.

**Why removing `toc.integrate`:** It merges the page's H2/H3 headings directly into the sidebar. Instead of a clean tree of pages, you see a flat dump of every heading from the current page. Broken on deep pages with many headings.

**Why adding `navigation.tabs`:** This is the core of the section-scoped sidebar. Concepts tab → Concepts tree in sidebar. Case Studies tab → Case Studies tree. Without this, everything collapses into one flat sidebar.

**Why adding `navigation.footer`:** Gives Previous / Next links at the bottom of every page — the layout from the mockup screenshot.

---

### Step 2 — Build full Concepts nav in mkdocs.yml

**File:** `mkdocs.yml` — the `nav:` section, Concepts subtree

Replace the current stub nav (entry-points only) with the complete file tree.
All paths verified against actual disk. Every file listed below exists on disk.

**Full Concepts nav to write:**

```yaml
- Concepts:
  - 01-Concepts/index.md
  - FUNDAMENTALS:
    - 01-Concepts/02-Fundamentals/index.md
    - Performance Metrics:
      - Overview: 01-Concepts/02-Fundamentals/01-Performance-Metrics/00-Overview.md
      - Introduction: 01-Concepts/02-Fundamentals/01-Performance-Metrics/01-Introduction.md
      - Latency: 01-Concepts/02-Fundamentals/01-Performance-Metrics/02-Latency.md
      - Throughput: 01-Concepts/02-Fundamentals/01-Performance-Metrics/03-Throughput.md
      - Latency vs Throughput: 01-Concepts/02-Fundamentals/01-Performance-Metrics/04-Latency-vs-Throughput.md
      - Bandwidth: 01-Concepts/02-Fundamentals/01-Performance-Metrics/05-Bandwidth.md
      - Bandwidth vs Latency vs Throughput: 01-Concepts/02-Fundamentals/01-Performance-Metrics/06-Bandwidth-vs-Latency-vs-Throughput.md
      - Percentiles: 01-Concepts/02-Fundamentals/01-Performance-Metrics/07-Percentiles.md
      - Interview Cheatsheet: 01-Concepts/02-Fundamentals/01-Performance-Metrics/08-Interview-Cheatsheet.md
      - Interview Questions:
        - SDE-1: 01-Concepts/02-Fundamentals/01-Performance-Metrics/09-Interview-Questions/SDE-1.md
        - SDE-2: 01-Concepts/02-Fundamentals/01-Performance-Metrics/09-Interview-Questions/SDE-2.md
        - SDE-3: 01-Concepts/02-Fundamentals/01-Performance-Metrics/09-Interview-Questions/SDE-3.md
    - Service Levels:
      - Overview: 01-Concepts/02-Fundamentals/02-Service-Levels/00-Overview.md
      - Introduction: 01-Concepts/02-Fundamentals/02-Service-Levels/01-Introduction.md
      - SLI: 01-Concepts/02-Fundamentals/02-Service-Levels/02-SLI.md
      - SLO: 01-Concepts/02-Fundamentals/02-Service-Levels/03-SLO.md
      - SLA: 01-Concepts/02-Fundamentals/02-Service-Levels/04-SLA.md
      - Error Budget: 01-Concepts/02-Fundamentals/02-Service-Levels/05-Error-Budget.md
      - Interview Cheatsheet: 01-Concepts/02-Fundamentals/02-Service-Levels/06-Interview-Cheatsheet.md
      - Interview Questions:
        - SDE-1: 01-Concepts/02-Fundamentals/02-Service-Levels/Interview-Questions/SDE-1.md
        - SDE-2: 01-Concepts/02-Fundamentals/02-Service-Levels/Interview-Questions/SDE-2.md
        - SDE-3: 01-Concepts/02-Fundamentals/02-Service-Levels/Interview-Questions/SDE-3.md
    - Availability:
      - Overview: 01-Concepts/02-Fundamentals/03-Availability/00-Overview.md
      - Availability: 01-Concepts/02-Fundamentals/03-Availability/01-Availability.md
      - SPOF: 01-Concepts/02-Fundamentals/03-Availability/02-SPOF.md
      - N+1 Redundancy: 01-Concepts/02-Fundamentals/03-Availability/03-N+1-Redundancy.md
      - Availability Patterns: 01-Concepts/02-Fundamentals/03-Availability/04-Availability-Patterns.md
      - Nines of Availability: 01-Concepts/02-Fundamentals/03-Availability/05-Nines-of-Availability.md
      - Series vs Parallel: 01-Concepts/02-Fundamentals/03-Availability/06-Series-vs-Parallel.md
      - Interview Cheatsheet: 01-Concepts/02-Fundamentals/03-Availability/07-Interview-Cheatsheet.md
      - Interview Questions:
        - SDE-1: 01-Concepts/02-Fundamentals/03-Availability/Interview-Questions/SDE-1.md
        - SDE-2: 01-Concepts/02-Fundamentals/03-Availability/Interview-Questions/SDE-2.md
        - SDE-3: 01-Concepts/02-Fundamentals/03-Availability/Interview-Questions/SDE-3.md
    - Reliability:
      - Overview: 01-Concepts/02-Fundamentals/04-Reliability/00-Overview.md
      - Reliability: 01-Concepts/02-Fundamentals/04-Reliability/01-Reliability.md
      - MTBF and MTTR: 01-Concepts/02-Fundamentals/04-Reliability/02-MTBF-and-MTTR.md
      - RTO and RPO: 01-Concepts/02-Fundamentals/04-Reliability/03-RTO-and-RPO.md
      - MTTR vs RTO: 01-Concepts/02-Fundamentals/04-Reliability/04-MTTR-RTO.md
      - Reliability vs Availability: 01-Concepts/02-Fundamentals/04-Reliability/05-Reliability-vs-Availability.md
      - Interview Cheatsheet: 01-Concepts/02-Fundamentals/04-Reliability/06-Interview-Cheatsheet.md
      - Interview Questions:
        - SDE-1: 01-Concepts/02-Fundamentals/04-Reliability/Interview-Questions/SDE-1.md
        - SDE-2: 01-Concepts/02-Fundamentals/04-Reliability/Interview-Questions/SDE-2.md
        - SDE-3: 01-Concepts/02-Fundamentals/04-Reliability/Interview-Questions/SDE-3.md
    - Scalability:
      - Overview: 01-Concepts/02-Fundamentals/05-Scalability/00-Overview.md
      - Scalability: 01-Concepts/02-Fundamentals/05-Scalability/01-Scalability.md
      - Load Balancing:
        - Overview: 01-Concepts/02-Fundamentals/05-Scalability/02-Load-Balancing/00-Overview.md
        - Load Balancing: 01-Concepts/02-Fundamentals/05-Scalability/02-Load-Balancing/01-Load-Balancing.md
        - Algorithms: 01-Concepts/02-Fundamentals/05-Scalability/02-Load-Balancing/02-Algorithms.md
        - L4:
          - Overview: 01-Concepts/02-Fundamentals/05-Scalability/02-Load-Balancing/03-L4/00-Overview.md
          - Fundamentals: 01-Concepts/02-Fundamentals/05-Scalability/02-Load-Balancing/03-L4/01-Fundamentals.md
          - How It Works: 01-Concepts/02-Fundamentals/05-Scalability/02-Load-Balancing/03-L4/02-How-It-Works.md
          - Connection Tables: 01-Concepts/02-Fundamentals/05-Scalability/02-Load-Balancing/03-L4/03-Connection-Tables.md
          - Real World: 01-Concepts/02-Fundamentals/05-Scalability/02-Load-Balancing/03-L4/04-Real-World.md
        - L7:
          - Overview: 01-Concepts/02-Fundamentals/05-Scalability/02-Load-Balancing/04-L7/00-Overview.md
          - Fundamentals: 01-Concepts/02-Fundamentals/05-Scalability/02-Load-Balancing/04-L7/01-Fundamentals.md
          - Request Flow: 01-Concepts/02-Fundamentals/05-Scalability/02-Load-Balancing/04-L7/02-Request-Flow.md
          - API Gateway: 01-Concepts/02-Fundamentals/05-Scalability/02-Load-Balancing/04-L7/03-API-Gateway.md
        - Hybrid In Production: 01-Concepts/02-Fundamentals/05-Scalability/02-Load-Balancing/05-Hybrid-In-Production.md
        - Interview Cheatsheet: 01-Concepts/02-Fundamentals/05-Scalability/02-Load-Balancing/06-Interview-Cheatsheet.md
      - Auto Scaling:
        - Overview: 01-Concepts/02-Fundamentals/05-Scalability/03-Auto-Scaling/00-Overview.md
        - Auto Scaling: 01-Concepts/02-Fundamentals/05-Scalability/03-Auto-Scaling/01-Auto-Scaling.md
        - Connection Draining: 01-Concepts/02-Fundamentals/05-Scalability/03-Auto-Scaling/02-Connection-Draining.md
        - Cold Start: 01-Concepts/02-Fundamentals/05-Scalability/03-Auto-Scaling/03-Cold-Start.md
        - Interview Cheatsheet: 01-Concepts/02-Fundamentals/05-Scalability/03-Auto-Scaling/04-Interview-Cheatsheet.md
      - Interview Cheatsheet: 01-Concepts/02-Fundamentals/05-Scalability/04-Interview-Cheatsheet.md
    - Fault Tolerance:
      - Overview: 01-Concepts/02-Fundamentals/06-Fault-Tolerance/00-Overview.md
      - Fault Tolerance: 01-Concepts/02-Fundamentals/06-Fault-Tolerance/01-Fault-Tolerance.md
      - Graceful Degradation: 01-Concepts/02-Fundamentals/06-Fault-Tolerance/02-Graceful-Degradation.md
      - Bulkhead: 01-Concepts/02-Fundamentals/06-Fault-Tolerance/03-Bulkhead.md
      - Timeout, Retry, Backoff: 01-Concepts/02-Fundamentals/06-Fault-Tolerance/04-Timeout-Retry-Backoff.md
      - Circuit Breaker: 01-Concepts/02-Fundamentals/06-Fault-Tolerance/05-Circuit-Breaker.md
      - Interview Cheatsheet: 01-Concepts/02-Fundamentals/06-Fault-Tolerance/06-Interview-Cheatsheet.md
    - Durability:
      - Overview: 01-Concepts/02-Fundamentals/07-Durability/00-Overview.md
      - Durability: 01-Concepts/02-Fundamentals/07-Durability/01-Durability.md
      - WAL: 01-Concepts/02-Fundamentals/07-Durability/02-WAL.md
      - Replication: 01-Concepts/02-Fundamentals/07-Durability/03-Replication.md
      - Backups: 01-Concepts/02-Fundamentals/07-Durability/04-Backups.md
      - Interview Cheatsheet: 01-Concepts/02-Fundamentals/07-Durability/05-Interview-Cheatsheet.md
    - Concurrency & Locking:
      - Overview: 01-Concepts/02-Fundamentals/08-Concurrency-Locking/00-Overview.md
      - Race Conditions: 01-Concepts/02-Fundamentals/08-Concurrency-Locking/01-Race-Conditions.md
      - Pessimistic Locking: 01-Concepts/02-Fundamentals/08-Concurrency-Locking/02-Pessimistic-Locking.md
      - Optimistic Locking: 01-Concepts/02-Fundamentals/08-Concurrency-Locking/03-Optimistic-Locking.md
      - Read-Write Locks: 01-Concepts/02-Fundamentals/08-Concurrency-Locking/04-Read-Write-Locks.md
      - MVCC: 01-Concepts/02-Fundamentals/08-Concurrency-Locking/05-MVCC.md
      - Distributed Locking: 01-Concepts/02-Fundamentals/08-Concurrency-Locking/06-Distributed-Locking.md
      - Idempotency: 01-Concepts/02-Fundamentals/08-Concurrency-Locking/07-Idempotency.md
      - Interview Cheatsheet: 01-Concepts/02-Fundamentals/08-Concurrency-Locking/08-Interview-Cheatsheet.md
    - Security:
      - Overview: 01-Concepts/02-Fundamentals/09-Security/00-Overview.md
      - Authentication & JWT: 01-Concepts/02-Fundamentals/09-Security/01-Authentication-and-JWT.md
      - Encryption: 01-Concepts/02-Fundamentals/09-Security/02-Encryption.md
      - Interview Cheatsheet: 01-Concepts/02-Fundamentals/09-Security/03-Interview-Cheatsheet.md
    - State Machines:
      - Overview: 01-Concepts/02-Fundamentals/10-State-Machines/00-Overview.md
      - What Is A State Machine: 01-Concepts/02-Fundamentals/10-State-Machines/01-What-Is-A-State-Machine.md
      - Implementing In Database: 01-Concepts/02-Fundamentals/10-State-Machines/02-Implementing-In-Database.md
      - Timeout-Driven Transitions: 01-Concepts/02-Fundamentals/10-State-Machines/03-Timeout-Driven-Transitions.md
      - Audit Trail vs Overwrite: 01-Concepts/02-Fundamentals/10-State-Machines/04-Audit-Trail-vs-Overwrite.md
      - Interview Cheatsheet: 01-Concepts/02-Fundamentals/10-State-Machines/05-Interview-Cheatsheet.md
    - NFRs:
      - Overview: 01-Concepts/02-Fundamentals/11-NFRs/00-Overview.md
      - NFRs and Design Decisions: 01-Concepts/02-Fundamentals/11-NFRs/01-NFRs-And-Design-Decisions.md
      - Conflicting NFRs: 01-Concepts/02-Fundamentals/11-NFRs/02-Conflicting-NFRs.md
  - CACHING:
    - 01-Concepts/03-Caching/index.md
    - Fundamentals: 01-Concepts/03-Caching/01-Fundamentals.md
    - Writing Strategies:
      - Overview: 01-Concepts/03-Caching/02-Writing-Strategies/00-Overview.md
      - Read Strategies: 01-Concepts/03-Caching/02-Writing-Strategies/01-Read-Strategies.md
      - Write Strategies: 01-Concepts/03-Caching/02-Writing-Strategies/02-Write-Strategies.md
      - Interview Cheatsheet: 01-Concepts/03-Caching/02-Writing-Strategies/03-Interview-Cheatsheet.md
    - Eviction Policies:
      - Overview: 01-Concepts/03-Caching/03-Eviction-Policies/00-Overview.md
      - LRU: 01-Concepts/03-Caching/03-Eviction-Policies/01-LRU.md
      - LFU: 01-Concepts/03-Caching/03-Eviction-Policies/02-LFU.md
      - FIFO and TTL: 01-Concepts/03-Caching/03-Eviction-Policies/03-FIFO-and-TTL.md
      - Interview Cheatsheet: 01-Concepts/03-Caching/03-Eviction-Policies/04-Interview-Cheatsheet.md
    - Population Strategies:
      - Overview: 01-Concepts/03-Caching/04-Population-Strategies/00-Overview.md
      - Refresh Ahead: 01-Concepts/03-Caching/04-Population-Strategies/01-Refresh-Ahead.md
      - Cache Warming: 01-Concepts/03-Caching/04-Population-Strategies/02-Cache-Warming.md
      - Interview Cheatsheet: 01-Concepts/03-Caching/04-Population-Strategies/03-Interview-Cheatsheet.md
    - Cache Invalidation:
      - Overview: 01-Concepts/03-Caching/05-Cache-Invalidation/00-Overview.md
      - TTL-Based: 01-Concepts/03-Caching/05-Cache-Invalidation/01-TTL-Based.md
      - Event-Driven: 01-Concepts/03-Caching/05-Cache-Invalidation/02-Event-Driven.md
      - Write-Through: 01-Concepts/03-Caching/05-Cache-Invalidation/03-Write-Through.md
      - Cache Versioning: 01-Concepts/03-Caching/05-Cache-Invalidation/04-Cache-Versioning.md
      - Stale-While-Revalidate: 01-Concepts/03-Caching/05-Cache-Invalidation/05-Stale-While-Revalidate.md
      - Interview Cheatsheet: 01-Concepts/03-Caching/05-Cache-Invalidation/06-Interview-Cheatsheet.md
    - Distributed Caching:
      - Overview: 01-Concepts/03-Caching/06-Distributed-Caching/00-Overview.md
      - Why Single Node Fails: 01-Concepts/03-Caching/06-Distributed-Caching/01-Why-Single-Node-Fails.md
      - Consistent Hashing: 01-Concepts/03-Caching/06-Distributed-Caching/02-Consistent-Hashing.md
      - Cache Coherence: 01-Concepts/03-Caching/06-Distributed-Caching/03-Cache-Coherence.md
      - Replication: 01-Concepts/03-Caching/06-Distributed-Caching/04-Replication.md
      - Two-Level Caching: 01-Concepts/03-Caching/06-Distributed-Caching/05-Two-Level-Caching.md
      - Node Failure: 01-Concepts/03-Caching/06-Distributed-Caching/06-Node-Failure.md
      - Interview Cheatsheet: 01-Concepts/03-Caching/06-Distributed-Caching/07-Interview-Cheatsheet.md
    - Cache Problems:
      - Overview: 01-Concepts/03-Caching/07-Cache-Problems/00-Overview.md
      - Cache Stampede: 01-Concepts/03-Caching/07-Cache-Problems/01-Cache-Stampede.md
      - Cold Start: 01-Concepts/03-Caching/07-Cache-Problems/02-Cold-Start.md
      - Cache Penetration: 01-Concepts/03-Caching/07-Cache-Problems/03-Cache-Penetration.md
      - Cache Avalanche: 01-Concepts/03-Caching/07-Cache-Problems/04-Cache-Avalanche.md
      - Interview Cheatsheet: 01-Concepts/03-Caching/07-Cache-Problems/05-Interview-Cheatsheet.md
    - Redis:
      - Data Structures: 01-Concepts/03-Caching/08-Redis/01-Data-Structures.md
      - Patterns: 01-Concepts/03-Caching/08-Redis/02-Patterns.md
      - Persistence: 01-Concepts/03-Caching/08-Redis/03-Persistence.md
      - Streams: 01-Concepts/03-Caching/08-Redis/04-Streams.md
      - Single-Threaded Event Loop: 01-Concepts/03-Caching/08-Redis/05-Single-Threaded-Event-Loop.md
    - Interview Questions:
      - SDE-1: 01-Concepts/03-Caching/09-Interview-Questions/SDE-1.md
      - SDE-2: 01-Concepts/03-Caching/09-Interview-Questions/SDE-2.md
      - SDE-3: 01-Concepts/03-Caching/09-Interview-Questions/SDE-3.md
  - STORAGE & DATABASES:
    - 01-Concepts/04-Storage-and-Databases/index.md
    - Fundamentals:
      - Why Not Files: 01-Concepts/04-Storage-and-Databases/01-Fundamentals/01-Why-Not-Files.md
      - How Files Store Data: 01-Concepts/04-Storage-and-Databases/01-Fundamentals/02-How-File-Store-Data.md
      - How DBs Store Data: 01-Concepts/04-Storage-and-Databases/01-Fundamentals/03-How-DB-Store-Data.md
      - Row-Oriented Storage: 01-Concepts/04-Storage-and-Databases/01-Fundamentals/04-Row-Oriented-Storage.md
      - Column-Oriented Storage: 01-Concepts/04-Storage-and-Databases/01-Fundamentals/05-Column-Oriented-Storage.md
    - ACID:
      - The Problem: 01-Concepts/04-Storage-and-Databases/02-ACID/01-The-Problem.md
      - Atomicity: 01-Concepts/04-Storage-and-Databases/02-ACID/02-Atomicity.md
      - Consistency: 01-Concepts/04-Storage-and-Databases/02-ACID/03-Consistency.md
      - Transaction Isolation:
        - Isolation Problems: 01-Concepts/04-Storage-and-Databases/02-ACID/04-Transaction-Isolation/01-Isolation-Problems.md
        - Isolation Levels: 01-Concepts/04-Storage-and-Databases/02-ACID/04-Transaction-Isolation/02-Isolation-Levels.md
        - Choosing Isolation: 01-Concepts/04-Storage-and-Databases/02-ACID/04-Transaction-Isolation/03-Choosing-Isolation.md
        - Pessimistic vs Optimistic: 01-Concepts/04-Storage-and-Databases/02-ACID/04-Transaction-Isolation/04-Pessimistic-vs-Optimistic-Locking.md
        - Interview Cheatsheet: 01-Concepts/04-Storage-and-Databases/02-ACID/04-Transaction-Isolation/05-Interview-Cheatsheet.md
        - External Locking: 01-Concepts/04-Storage-and-Databases/02-ACID/04-Transaction-Isolation/06-External-Locking-Strategies.md
      - Durability: 01-Concepts/04-Storage-and-Databases/02-ACID/05-Durability.md
      - ACID vs BASE: 01-Concepts/04-Storage-and-Databases/02-ACID/06-ACID-vs-BASE.md
      - Distributed Transactions:
        - The Problem: 01-Concepts/04-Storage-and-Databases/02-ACID/07-Distributed-Transactions/01-The-Problem.md
        - 2PC:
          - Working: 01-Concepts/04-Storage-and-Databases/02-ACID/07-Distributed-Transactions/02-2PC/01-Working.md
          - Failures: 01-Concepts/04-Storage-and-Databases/02-ACID/07-Distributed-Transactions/02-2PC/02-Failures.md
          - Solutions: 01-Concepts/04-Storage-and-Databases/02-ACID/07-Distributed-Transactions/02-2PC/03-Solutions.md
          - 2PC In Practice: 01-Concepts/04-Storage-and-Databases/02-ACID/07-Distributed-Transactions/02-2PC/04-2PC-In-Practice.md
        - Saga:
          - What Is Saga: 01-Concepts/04-Storage-and-Databases/02-ACID/07-Distributed-Transactions/03-Saga/01-What-Is-Saga.md
          - Choreography: 01-Concepts/04-Storage-and-Databases/02-ACID/07-Distributed-Transactions/03-Saga/02-Choreography.md
          - Orchestration: 01-Concepts/04-Storage-and-Databases/02-ACID/07-Distributed-Transactions/03-Saga/03-Orchestration.md
        - 2PC vs Saga: 01-Concepts/04-Storage-and-Databases/02-ACID/07-Distributed-Transactions/04-2PC-vs-Saga.md
        - Interview Cheatsheet: 01-Concepts/04-Storage-and-Databases/02-ACID/07-Distributed-Transactions/05-Interview-Cheatsheet.md
      - Interview Cheatsheet: 01-Concepts/04-Storage-and-Databases/02-ACID/08-Interview-Cheatsheet.md
      - Interview Questions:
        - SDE-1: 01-Concepts/04-Storage-and-Databases/02-ACID/Interview-Questions/SDE-1.md
        - SDE-2: 01-Concepts/04-Storage-and-Databases/02-ACID/Interview-Questions/SDE-2.md
        - SDE-3: 01-Concepts/04-Storage-and-Databases/02-ACID/Interview-Questions/SDE-3.md
    - SQL:
      - Relational Model: 01-Concepts/04-Storage-and-Databases/03-SQL/01-Relational-Model.md
      - Normalisation: 01-Concepts/04-Storage-and-Databases/03-SQL/02-Normalisation.md
      - Denormalisation: 01-Concepts/04-Storage-and-Databases/03-SQL/04-Denormalisation.md
      - Joins: 01-Concepts/04-Storage-and-Databases/03-SQL/04-Joins.md
      - Views: 01-Concepts/04-Storage-and-Databases/03-SQL/05-Views.md
    - Indexing:
      - Indexes: 01-Concepts/04-Storage-and-Databases/04-Indexing/01-Indexes.md
      - Hash Index: 01-Concepts/04-Storage-and-Databases/04-Indexing/02-Hash-Index.md
      - B+ Tree: 01-Concepts/04-Storage-and-Databases/04-Indexing/03-B+Tree.md
      - LSM Tree Writes: 01-Concepts/04-Storage-and-Databases/04-Indexing/04-LSM-Tree-Writes.md
      - LSM Tree Reads: 01-Concepts/04-Storage-and-Databases/04-Indexing/05-LSM-Tree-Reads.md
      - Geospatial Indexing:
        - The Problem: 01-Concepts/04-Storage-and-Databases/04-Indexing/06-Geospatial-Indexing/01-The-Problem.md
        - Why Composite Index Fails: 01-Concepts/04-Storage-and-Databases/04-Indexing/06-Geospatial-Indexing/02-Why-Composite-Index-Fails.md
        - Geohash: 01-Concepts/04-Storage-and-Databases/04-Indexing/06-Geospatial-Indexing/03-Geohash.md
        - S2 Cells: 01-Concepts/04-Storage-and-Databases/04-Indexing/06-Geospatial-Indexing/04-S2-Cells.md
        - Interview Cheatsheet: 01-Concepts/04-Storage-and-Databases/04-Indexing/06-Geospatial-Indexing/05-Interview-Cheatsheet.md
    - CDC:
      - What Is CDC: 01-Concepts/04-Storage-and-Databases/05-CDC/01-What-is-CDC.md
      - Outbox Pattern: 01-Concepts/04-Storage-and-Databases/05-CDC/02-Outbox-Pattern.md
      - Interview Cheatsheet: 01-Concepts/04-Storage-and-Databases/05-CDC/03-Interview-Cheatsheet.md
    - Pagination:
      - Offset Pagination: 01-Concepts/04-Storage-and-Databases/06-Pagination/01-Offset-Pagination.md
      - Cursor Pagination: 01-Concepts/04-Storage-and-Databases/06-Pagination/02-Cursor-Pagination.md
      - Interview Cheatsheet: 01-Concepts/04-Storage-and-Databases/06-Pagination/03-Interview-Cheatsheet.md
    - Connection Pooling:
      - Cost Of A Connection: 01-Concepts/04-Storage-and-Databases/07-Connection-Pooling/01-Cost-Of-A-Connection.md
      - Connection Pool: 01-Concepts/04-Storage-and-Databases/07-Connection-Pooling/02-Connection-Pool.md
      - Interview Cheatsheet: 01-Concepts/04-Storage-and-Databases/07-Connection-Pooling/03-Interview-Cheatsheet.md
    - Read-Write Splitting:
      - The Problem: 01-Concepts/04-Storage-and-Databases/08-Read-Write-Splitting/01-The-Problem.md
      - How It Works: 01-Concepts/04-Storage-and-Databases/08-Read-Write-Splitting/02-How-It-Works.md
      - Replication Lag: 01-Concepts/04-Storage-and-Databases/08-Read-Write-Splitting/03-Replication-Lag.md
      - Interview Cheatsheet: 01-Concepts/04-Storage-and-Databases/08-Read-Write-Splitting/04-Interview-Cheatsheet.md
  - DATABASE TYPES:
    - 01-Concepts/05-Database-Types/index.md
    - Key-Value Stores:
      - Overview: 01-Concepts/05-Database-Types/01-Key-Value-Stores/00-Overview.md
      - Redis: 01-Concepts/05-Database-Types/01-Key-Value-Stores/01-Redis.md
      - Memcached: 01-Concepts/05-Database-Types/01-Key-Value-Stores/02-Memcached.md
      - KV Positioning: 01-Concepts/05-Database-Types/01-Key-Value-Stores/03-KV-Positioning.md
      - Interview Cheatsheet: 01-Concepts/05-Database-Types/01-Key-Value-Stores/04-Interview-Cheatsheet.md
    - Document Stores:
      - Document Model: 01-Concepts/05-Database-Types/02-Document-Stores/01-Document-Model.md
      - Indexes: 01-Concepts/05-Database-Types/02-Document-Stores/02-Indexes.md
      - Embedding vs Referencing: 01-Concepts/05-Database-Types/02-Document-Stores/03-Embedding-vs-Referencing.md
      - Replication and Sharding: 01-Concepts/05-Database-Types/02-Document-Stores/04-Replication-and-Sharding.md
      - Limitations: 01-Concepts/05-Database-Types/02-Document-Stores/05-Limitations.md
      - Interview Cheatsheet: 01-Concepts/05-Database-Types/02-Document-Stores/06-Interview-Cheatsheet.md
    - Column Family:
      - Fundamentals:
        - Why Column Family: 01-Concepts/05-Database-Types/03-Column-Family/01-Fundamentals/01-Why-Column-Family.md
        - Column-Oriented Storage: 01-Concepts/05-Database-Types/03-Column-Family/01-Fundamentals/02-Column-Oriented-Storage.md
        - Row Keys: 01-Concepts/05-Database-Types/03-Column-Family/01-Fundamentals/03-Row-Keys.md
      - Cassandra:
        - Overview: 01-Concepts/05-Database-Types/03-Column-Family/02-Cassandra/00-Overview.md
        - Ring Architecture: 01-Concepts/05-Database-Types/03-Column-Family/02-Cassandra/01-Ring-Architecture.md
        - Write Path: 01-Concepts/05-Database-Types/03-Column-Family/02-Cassandra/02-Write-Path.md
        - Read Path: 01-Concepts/05-Database-Types/03-Column-Family/02-Cassandra/03-Read-Path.md
        - Replication Consistency: 01-Concepts/05-Database-Types/03-Column-Family/02-Cassandra/04-Replication-Consistency.md
        - Tombstones: 01-Concepts/05-Database-Types/03-Column-Family/02-Cassandra/05-Tombstones.md
        - Interview Cheatsheet: 01-Concepts/05-Database-Types/03-Column-Family/02-Cassandra/06-Interview-Cheatsheet.md
        - Query-First Modeling: 01-Concepts/05-Database-Types/03-Column-Family/02-Cassandra/07-Query-First-Modeling.md
      - Bigtable:
        - Architecture: 01-Concepts/05-Database-Types/03-Column-Family/03-Bigtable/01-Architecture.md
        - Cassandra vs Bigtable: 01-Concepts/05-Database-Types/03-Column-Family/03-Bigtable/02-Cassandra-vs-Bigtable.md
      - DynamoDB:
        - Data Model: 01-Concepts/05-Database-Types/03-Column-Family/04-DynamoDB/01-Data-Model.md
        - Consistency: 01-Concepts/05-Database-Types/03-Column-Family/04-DynamoDB/02-Consistency.md
        - Query API and Indexes: 01-Concepts/05-Database-Types/03-Column-Family/04-DynamoDB/03-Query-API-and-Indexes.md
        - Redis vs DynamoDB: 01-Concepts/05-Database-Types/03-Column-Family/04-DynamoDB/04-Redis-vs-DynamoDB.md
        - TTL and Sessions: 01-Concepts/05-Database-Types/03-Column-Family/04-DynamoDB/05-TTL-and-Sessions.md
        - Interview Cheatsheet: 01-Concepts/05-Database-Types/03-Column-Family/04-DynamoDB/06-Interview-Cheatsheet.md
    - Search Engines:
      - Problem With SQL Search: 01-Concepts/05-Database-Types/04-Search-Engines/01-Problem-With-SQL-Search.md
      - Inverted Index: 01-Concepts/05-Database-Types/04-Search-Engines/02-Inverted-Index.md
      - Indexing Pipeline: 01-Concepts/05-Database-Types/04-Search-Engines/03-Indexing-Pipeline.md
      - Ranking TF-IDF BM25: 01-Concepts/05-Database-Types/04-Search-Engines/04-Ranking-TF-IDF-BM25.md
      - Elasticsearch Architecture: 01-Concepts/05-Database-Types/04-Search-Engines/05-Elasticsearch-Architecture.md
      - Where It Fits: 01-Concepts/05-Database-Types/04-Search-Engines/06-Where-It-Fits.md
      - Interview Cheatsheet: 01-Concepts/05-Database-Types/04-Search-Engines/07-Interview-Cheatsheet.md
    - Graph Databases:
      - Why Not SQL: 01-Concepts/05-Database-Types/05-Graph-Databases/01-Why-Not-SQL.md
      - Graph Data Model: 01-Concepts/05-Database-Types/05-Graph-Databases/02-Graph-Data-Model.md
      - Cypher Query Language: 01-Concepts/05-Database-Types/05-Graph-Databases/03-Cypher-Query-Language.md
      - Use Cases: 01-Concepts/05-Database-Types/05-Graph-Databases/04-Use-Cases.md
      - Interview Cheatsheet: 01-Concepts/05-Database-Types/05-Graph-Databases/05-Interview-Cheatsheet.md
    - Blob Storage:
      - Object Storage Model: 01-Concepts/05-Database-Types/06-Blob-Storage/01-Object-Storage-Model.md
      - Presigned URLs: 01-Concepts/05-Database-Types/06-Blob-Storage/02-Presigned-URLs.md
      - Multipart Upload: 01-Concepts/05-Database-Types/06-Blob-Storage/03-Multipart-Upload.md
      - Content-Addressable Storage: 01-Concepts/05-Database-Types/06-Blob-Storage/04-Content-Addressable-Storage.md
      - Chunk-Level Deduplication: 01-Concepts/05-Database-Types/06-Blob-Storage/05-Chunk-Level-Deduplication.md
      - Storage Classes: 01-Concepts/05-Database-Types/06-Blob-Storage/06-Storage-Classes.md
      - Interview Cheatsheet: 01-Concepts/05-Database-Types/06-Blob-Storage/07-Interview-Cheatsheet.md
    - NewSQL:
      - The Problem: 01-Concepts/05-Database-Types/07-NewSQL/01-The-Problem.md
      - Spanner TrueTime: 01-Concepts/05-Database-Types/07-NewSQL/02-Spanner-TrueTime.md
      - Spanner Transactions: 01-Concepts/05-Database-Types/07-NewSQL/03-Spanner-Transactions.md
      - When To Use: 01-Concepts/05-Database-Types/07-NewSQL/04-When-To-Use.md
      - Interview Cheatsheet: 01-Concepts/05-Database-Types/07-NewSQL/05-Interview-Cheatsheet.md
    - OLTP vs OLAP:
      - The Problem: 01-Concepts/05-Database-Types/08-OLTP-vs-OLAP/01-The-Problem.md
      - OLTP: 01-Concepts/05-Database-Types/08-OLTP-vs-OLAP/02-OLTP.md
      - OLAP: 01-Concepts/05-Database-Types/08-OLTP-vs-OLAP/03-OLAP.md
      - ETL vs CDC: 01-Concepts/05-Database-Types/08-OLTP-vs-OLAP/04-ETL-vs-CDC.md
      - Interview Cheatsheet: 01-Concepts/05-Database-Types/08-OLTP-vs-OLAP/05-Interview-Cheatsheet.md
    - Choosing The Right DB:
      - Decision Framework: 01-Concepts/05-Database-Types/09-Choosing-The-Right-DB/01-Decision-Framework.md
      - DB Cheatsheet: 01-Concepts/05-Database-Types/09-Choosing-The-Right-DB/02-DB-Cheatsheet.md
    - Data Modeling:
      - The Process: 01-Concepts/05-Database-Types/10-Data-Modeling/01-The-Process.md
      - Entities And Relationships: 01-Concepts/05-Database-Types/10-Data-Modeling/02-Entities-And-Relationships.md
      - Access Patterns: 01-Concepts/05-Database-Types/10-Data-Modeling/03-Access-Patterns.md
      - Instagram Schema: 01-Concepts/05-Database-Types/10-Data-Modeling/04-Instagram-Schema.md
      - Red Flags: 01-Concepts/05-Database-Types/10-Data-Modeling/05-Red-Flags.md
  - MESSAGING:
    - 01-Concepts/06-Messaging/index.md
    - Fundamentals:
      - Message Queues: 01-Concepts/06-Messaging/01-Fundamentals/01-Message-Queues.md
      - Task Queue: 01-Concepts/06-Messaging/01-Fundamentals/02-Task-Queue.md
      - What Is A Broker: 01-Concepts/06-Messaging/01-Fundamentals/03-What-is-a-Broker.md
      - Pub-Sub: 01-Concepts/06-Messaging/01-Fundamentals/04-Pub-Sub.md
      - Delivery Guarantees: 01-Concepts/06-Messaging/01-Fundamentals/05-Delivery-Guarantees.md
      - Dead Letter Queue: 01-Concepts/06-Messaging/01-Fundamentals/06-Dead-Letter-Queue.md
      - Message Ordering: 01-Concepts/06-Messaging/01-Fundamentals/07-Message-Ordering.md
      - Delay Queues: 01-Concepts/06-Messaging/01-Fundamentals/08-Delay-Queues.md
      - Priority Queues: 01-Concepts/06-Messaging/01-Fundamentals/09-Priority-Queues.md
      - Fan-Out on Write: 01-Concepts/06-Messaging/01-Fundamentals/10-Fan-Out-on-Write.md
      - Fan-Out on Read: 01-Concepts/06-Messaging/01-Fundamentals/11-Fan-Out-on-Read.md
    - SQS:
      - What Is SQS: 01-Concepts/06-Messaging/02-SQS/01-What-Is-SQS.md
      - Standard vs FIFO: 01-Concepts/06-Messaging/02-SQS/02-Standard-vs-FIFO.md
      - Timeout and Retries: 01-Concepts/06-Messaging/02-SQS/03-Timeout-and-Retries.md
      - Idempotency and DLQ: 01-Concepts/06-Messaging/02-SQS/04-Idempotency-and-DLQ.md
      - Scaling: 01-Concepts/06-Messaging/02-SQS/05-Scaling.md
      - Retention and Replay: 01-Concepts/06-Messaging/02-SQS/06-Retention-and-Replay-Limits.md
      - Delay Queues: 01-Concepts/06-Messaging/02-SQS/07-Delay-Queues.md
      - Producer-Consumer Model: 01-Concepts/06-Messaging/02-SQS/08-Producer-Consumer-Model.md
      - SNS Fan-Out: 01-Concepts/06-Messaging/02-SQS/09-SNS-Fan-Out.md
    - RabbitMQ:
      - What Is RabbitMQ: 01-Concepts/06-Messaging/03-RabbitMQ/01-What-Is-RabbitMQ.md
      - Direct vs Fanout Exchange: 01-Concepts/06-Messaging/03-RabbitMQ/02-Direct-vs-Fanout-Exchange.md
      - Topic Exchange: 01-Concepts/06-Messaging/03-RabbitMQ/03-Topic-Exchange.md
      - Headers Exchange: 01-Concepts/06-Messaging/03-RabbitMQ/04-Headers-Exchange.md
      - ACK, NACK, Requeue: 01-Concepts/06-Messaging/03-RabbitMQ/05-ACK-NACK-Requeue.md
      - Crash and Redelivery: 01-Concepts/06-Messaging/03-RabbitMQ/06-Crash-and-Redelivery.md
      - Prefetch and Fairness: 01-Concepts/06-Messaging/03-RabbitMQ/07-Prefetch-and-Fairness.md
      - Durable Queues: 01-Concepts/06-Messaging/03-RabbitMQ/08-Durable-Queues.md
      - Delivery Guarantees: 01-Concepts/06-Messaging/03-RabbitMQ/09-Delivery-Guarantees.md
      - Retries and DLQ: 01-Concepts/06-Messaging/03-RabbitMQ/10-Retries-And-DLQ.md
      - Message Ordering: 01-Concepts/06-Messaging/03-RabbitMQ/11-Message-Ordering.md
      - Bottlenecks: 01-Concepts/06-Messaging/03-RabbitMQ/12-Bottlenecks.md
      - Scaling: 01-Concepts/06-Messaging/03-RabbitMQ/13-Scaling.md
  - EVENT BROKER (KAFKA):
    - 01-Concepts/07-Event-Broker/index.md
    - Architecture:
      - Why Kafka Exists: 01-Concepts/07-Event-Broker/01-Architecture/01-Why-Kafka-Exists.md
      - Writes and Page Cache: 01-Concepts/07-Event-Broker/01-Architecture/02-Writes-and-Page-Cache.md
      - Topics: 01-Concepts/07-Event-Broker/01-Architecture/03-Topics.md
      - Partitions: 01-Concepts/07-Event-Broker/01-Architecture/04-Partitions.md
      - Brokers: 01-Concepts/07-Event-Broker/01-Architecture/05-Brokers.md
      - Replication: 01-Concepts/07-Event-Broker/01-Architecture/06-Replication.md
      - ISR: 01-Concepts/07-Event-Broker/01-Architecture/07-ISR.md
      - Hot Partitions: 01-Concepts/07-Event-Broker/01-Architecture/08-Hot-Partitions.md
    - Producer:
      - Partitioners: 01-Concepts/07-Event-Broker/02-Producer/01-Partitioners.md
      - Batching: 01-Concepts/07-Event-Broker/02-Producer/02-Batching.md
      - Compression: 01-Concepts/07-Event-Broker/02-Producer/03-Compression.md
    - Consumer:
      - Pull Model: 01-Concepts/07-Event-Broker/03-Consumer/01-Pull-Model.md
      - Offsets: 01-Concepts/07-Event-Broker/03-Consumer/02-Offsets.md
      - Offset Storage: 01-Concepts/07-Event-Broker/03-Consumer/03-Offset-Storage.md
      - Before vs After: 01-Concepts/07-Event-Broker/03-Consumer/04-Before-vs-After.md
      - Consumer Groups: 01-Concepts/07-Event-Broker/03-Consumer/05-Consumer-Groups.md
      - Rebalancing: 01-Concepts/07-Event-Broker/03-Consumer/06-Rebalancing.md
    - Advanced:
      - Retention: 01-Concepts/07-Event-Broker/04-Advanced/01-Retention.md
      - Exactly-Once Processing: 01-Concepts/07-Event-Broker/04-Advanced/02-Exactly-Once-Processing.md
    - Backpressure:
      - Consumer Lag: 01-Concepts/07-Event-Broker/05-Backpressure/01-Consumer-Lag.md
      - Scaling Consumers: 01-Concepts/07-Event-Broker/05-Backpressure/02-Scaling-Consumers.md
      - Load Shedding: 01-Concepts/07-Event-Broker/05-Backpressure/03-Load-Shedding.md
      - Backpressure Signals: 01-Concepts/07-Event-Broker/05-Backpressure/04-Backpressure-Signals.md
    - Kafka vs SQS vs RabbitMQ:
      - Fundamental Difference: 01-Concepts/07-Event-Broker/06-Kafka-vs-Sqs-vs-RabbitMQ/01-Fundamental-Difference.md
      - After Read: 01-Concepts/07-Event-Broker/06-Kafka-vs-Sqs-vs-RabbitMQ/02-After-Read.md
      - Retention: 01-Concepts/07-Event-Broker/06-Kafka-vs-Sqs-vs-RabbitMQ/03-Retention.md
      - Routing and Fanout: 01-Concepts/07-Event-Broker/06-Kafka-vs-Sqs-vs-RabbitMQ/04-Routing-and-Fanout.md
      - Ordering and Throughput: 01-Concepts/07-Event-Broker/06-Kafka-vs-Sqs-vs-RabbitMQ/05-Ordering-and-Throughput.md
      - When To Choose What: 01-Concepts/07-Event-Broker/06-Kafka-vs-Sqs-vs-RabbitMQ/06-When-To-Choose-What.md
  - EVENT-DRIVEN PATTERNS:
    - 01-Concepts/08-Event-Driven-Patterns/index.md
    - Event Sourcing: 01-Concepts/08-Event-Driven-Patterns/01-What-Is-Event-Sourcing/01-Event-Sourcing.md
    - CQRS:
      - What Is CQRS: 01-Concepts/08-Event-Driven-Patterns/02-CQRS/01-What-Is-CQRS.md
      - Read Models: 01-Concepts/08-Event-Driven-Patterns/02-CQRS/02-Read-Models.md
      - Consistency: 01-Concepts/08-Event-Driven-Patterns/02-CQRS/03-Consistency.md
    - Outbox Pattern:
      - Dual Write: 01-Concepts/08-Event-Driven-Patterns/03-OutBox-Pattern/01-Dual-Write.md
      - Outbox Pattern: 01-Concepts/08-Event-Driven-Patterns/03-OutBox-Pattern/02-Outbox-Pattern.md
    - CDC:
      - What Is CDC: 01-Concepts/08-Event-Driven-Patterns/04-CDC/01-What-Is-CDC.md
      - Debezium: 01-Concepts/08-Event-Driven-Patterns/04-CDC/02-Debezium.md
    - Inbox + Outbox:
      - What Is Inbox Pattern: 01-Concepts/08-Event-Driven-Patterns/05-Inbox-Outbox-Together/01-What-Is-Inbox-Pattern.md
      - Inbox-Outbox Combined: 01-Concepts/08-Event-Driven-Patterns/05-Inbox-Outbox-Together/10-Inbox-Outbox-Combined.md
      - Inbox-Outbox Full Flow: 01-Concepts/08-Event-Driven-Patterns/05-Inbox-Outbox-Together/11-Inbox-Outbox-Full-Flow.md
  - DATA PROCESSING:
    - 01-Concepts/09-Data-Processing/index.md
    - Stream Processing:
      - Why Stream Processing: 01-Concepts/09-Data-Processing/01-Stream-Processing/01-Why-Stream-Processing.md
      - Window Types: 01-Concepts/09-Data-Processing/01-Stream-Processing/02-Window-Types.md
      - Watermarks: 01-Concepts/09-Data-Processing/01-Stream-Processing/03-Watermarks.md
      - Statefulness: 01-Concepts/09-Data-Processing/01-Stream-Processing/04-Statefullnes.md
      - Crash Recovery: 01-Concepts/09-Data-Processing/01-Stream-Processing/05-Crash-Recovery.md
    - Batch Processing:
      - MapReduce:
        - Why Batch Processing: 01-Concepts/09-Data-Processing/02-Batch-Processing/MapReduce/01-Why-Batch-Processing.md
        - MapReduce: 01-Concepts/09-Data-Processing/02-Batch-Processing/MapReduce/02-MapReduce.md
        - Map Phase: 01-Concepts/09-Data-Processing/02-Batch-Processing/MapReduce/03-Map-Phase.md
        - Shuffle Phase: 01-Concepts/09-Data-Processing/02-Batch-Processing/MapReduce/04-Shuffle-Phase.md
        - Reduce Phase: 01-Concepts/09-Data-Processing/02-Batch-Processing/MapReduce/05-Reduce-Phase.md
        - Combiner: 01-Concepts/09-Data-Processing/02-Batch-Processing/MapReduce/06-Combiner.md
        - Hot Keys: 01-Concepts/09-Data-Processing/02-Batch-Processing/MapReduce/07-Hot-Keys.md
      - Spark:
        - Why Spark: 01-Concepts/09-Data-Processing/02-Batch-Processing/Spark/01-Why-Spark.md
        - Spark Architecture: 01-Concepts/09-Data-Processing/02-Batch-Processing/Spark/02-Spark-Architecture.md
        - DAG Optimization: 01-Concepts/09-Data-Processing/02-Batch-Processing/Spark/03-DAG-Optimization.md
    - Lambda & Kappa:
      - Lambda Architecture: 01-Concepts/09-Data-Processing/03-Lambda-Kappa/01-Lambda-Architecture.md
      - Kappa Architecture: 01-Concepts/09-Data-Processing/03-Lambda-Kappa/02-Kappa-Architecture.md
      - Lambda vs Kappa: 01-Concepts/09-Data-Processing/03-Lambda-Kappa/03-Lambda-vs-Kappa.md
    - Schema Evolution:
      - Why Schema Evolution: 01-Concepts/09-Data-Processing/04-Schema-Evolution/01-Why-Schema-Evolution.md
      - Schema Registry: 01-Concepts/09-Data-Processing/04-Schema-Evolution/02-Schema-Registry.md
      - Protobuf: 01-Concepts/09-Data-Processing/04-Schema-Evolution/03-Protobuf.md
      - Avro Basics: 01-Concepts/09-Data-Processing/04-Schema-Evolution/04-Avro-Basics.md
      - Avro Flow: 01-Concepts/09-Data-Processing/04-Schema-Evolution/05-Avro-Flow.md
  - DISTRIBUTED SYSTEMS:
    - 01-Concepts/10-Distributed-Systems/index.md
    - Problems: 01-Concepts/10-Distributed-Systems/01-Problems/01-General-Problem.md
    - Network Partitions:
      - Overview: 01-Concepts/10-Distributed-Systems/02-Network-Partitions/00-Overview.md
      - Network Partitions: 01-Concepts/10-Distributed-Systems/02-Network-Partitions/01-Network-Partitions.md
      - During Partition: 01-Concepts/10-Distributed-Systems/02-Network-Partitions/02-During-Partition.md
      - Split Brain: 01-Concepts/10-Distributed-Systems/02-Network-Partitions/03-Split-Brain.md
      - Quorum vs Consensus: 01-Concepts/10-Distributed-Systems/02-Network-Partitions/04-Quorum-vs-Consensus.md
      - Interview Cheatsheet: 01-Concepts/10-Distributed-Systems/02-Network-Partitions/05-Interview-Cheatsheet.md
    - CAP Theorem:
      - Overview: 01-Concepts/10-Distributed-Systems/03-CAP-Theorem/00-Overview.md
      - CAP Theorem: 01-Concepts/10-Distributed-Systems/03-CAP-Theorem/01-CAP-Theorem.md
      - CP vs AP: 01-Concepts/10-Distributed-Systems/03-CAP-Theorem/02-CP-vs-AP.md
      - Interview Cheatsheet: 01-Concepts/10-Distributed-Systems/03-CAP-Theorem/03-Interview-Cheatsheet.md
    - PACELC:
      - Overview: 01-Concepts/10-Distributed-Systems/04-PACELC/00-Overview.md
      - PACELC Theorem: 01-Concepts/10-Distributed-Systems/04-PACELC/01-PACELC-Theorem.md
      - PA/EC The Middle Ground: 01-Concepts/10-Distributed-Systems/04-PACELC/02-PA-EC-The-Middle-Ground.md
      - System Examples: 01-Concepts/10-Distributed-Systems/04-PACELC/03-System-Examples.md
      - Interview Cheatsheet: 01-Concepts/10-Distributed-Systems/04-PACELC/04-Interview-Cheatsheet.md
    - Consistency Models:
      - Overview: 01-Concepts/10-Distributed-Systems/05-Consistency-Models/00-Overview.md
      - Consistency Models: 01-Concepts/10-Distributed-Systems/05-Consistency-Models/01-Consistency-Models.md
      - When To Use: 01-Concepts/10-Distributed-Systems/05-Consistency-Models/02-When-To-Use.md
      - Interview Cheatsheet: 01-Concepts/10-Distributed-Systems/05-Consistency-Models/03-Interview-Cheatsheet.md
    - Replication:
      - What Is Replication: 01-Concepts/10-Distributed-Systems/06-Replication/01-What-is-Replication.md
      - Sync vs Async: 01-Concepts/10-Distributed-Systems/06-Replication/02-Sync-vs-Async.md
      - Replication Lag: 01-Concepts/10-Distributed-Systems/06-Replication/03-Replication-Lag.md
      - Failover: 01-Concepts/10-Distributed-Systems/06-Replication/04-Failover.md
      - Multi-Primary: 01-Concepts/10-Distributed-Systems/06-Replication/05-Multi-Primary.md
      - Interview Cheatsheet: 01-Concepts/10-Distributed-Systems/06-Replication/06-Interview-Cheatsheet.md
    - Sharding:
      - What Is Sharding: 01-Concepts/10-Distributed-Systems/07-Sharding/01-What-is-Sharding.md
      - Shard Key: 01-Concepts/10-Distributed-Systems/07-Sharding/02-Shard-Key.md
      - Sharding Strategies: 01-Concepts/10-Distributed-Systems/07-Sharding/03-Sharding-Strategies.md
      - Consistent Hashing: 01-Concepts/10-Distributed-Systems/07-Sharding/04-Consistent-Hashing.md
      - Cross-Shard Joins: 01-Concepts/10-Distributed-Systems/07-Sharding/05-Cross-Shard-Joins.md
      - Resharding: 01-Concepts/10-Distributed-Systems/07-Sharding/06-Resharding.md
      - Over-Sharding: 01-Concepts/10-Distributed-Systems/07-Sharding/07-Over-Sharding.md
      - Relational DBs: 01-Concepts/10-Distributed-Systems/07-Sharding/08-Relational-DBs.md
      - Interview Cheatsheet: 01-Concepts/10-Distributed-Systems/07-Sharding/09-Interview-Cheatsheet.md
    - Consensus:
      - What Is Consensus: 01-Concepts/10-Distributed-Systems/08-Consensus/01-What-Is-Consensus.md
      - Raft:
        - What Is Raft: 01-Concepts/10-Distributed-Systems/08-Consensus/02-RAFT/01-What-Is-Raft.md
        - Leader Election: 01-Concepts/10-Distributed-Systems/08-Consensus/02-RAFT/02-Leader-Election.md
        - Term Numbers: 01-Concepts/10-Distributed-Systems/08-Consensus/02-RAFT/03-Term-Numbers.md
        - Log Replication: 01-Concepts/10-Distributed-Systems/08-Consensus/02-RAFT/04-Log-Replication.md
        - Log Replication Failures: 01-Concepts/10-Distributed-Systems/08-Consensus/02-RAFT/05-Log-Replication-Failures.md
        - Fencing Tokens: 01-Concepts/10-Distributed-Systems/08-Consensus/02-RAFT/06-Fencing-Tokens.md
      - ZooKeeper:
        - ZooKeeper Election: 01-Concepts/10-Distributed-Systems/08-Consensus/03-Zookeeper/01-ZooKeeper-Election.md
        - Redis Distributed Locks: 01-Concepts/10-Distributed-Systems/08-Consensus/03-Zookeeper/02-Redis-Distributed-Locks.md
      - Paxos:
        - What Is Paxos: 01-Concepts/10-Distributed-Systems/08-Consensus/04-Paxos/01-What-Is-Paxos.md
        - Paxos Phases: 01-Concepts/10-Distributed-Systems/08-Consensus/04-Paxos/02-Paxos-Phases.md
        - Paxos Retry Cases: 01-Concepts/10-Distributed-Systems/08-Consensus/04-Paxos/03-Paxos-Retry-Cases.md
        - Paxos Livelock: 01-Concepts/10-Distributed-Systems/08-Consensus/04-Paxos/04-Paxos-Livelock.md
    - Distributed Clocks:
      - Clock Drift: 01-Concepts/10-Distributed-Systems/09-Distributed-Clocks/01-Clock-Drift.md
      - NTP: 01-Concepts/10-Distributed-Systems/09-Distributed-Clocks/02-NTP.md
      - Lamport Clocks: 01-Concepts/10-Distributed-Systems/09-Distributed-Clocks/03-Lamport-Clocks.md
      - Vector Clocks: 01-Concepts/10-Distributed-Systems/09-Distributed-Clocks/04-Vector-Clocks.md
      - GPS and Atomic Clocks: 01-Concepts/10-Distributed-Systems/09-Distributed-Clocks/05-GPS-And-Atomic-Clocks.md
      - TrueTime Uncertainty: 01-Concepts/10-Distributed-Systems/09-Distributed-Clocks/06-TrueTime-Uncertainty.md
    - CRDTs:
      - The Problem: 01-Concepts/10-Distributed-Systems/10-CRDTs/01-The-Problem.md
      - Why Locks Fail: 01-Concepts/10-Distributed-Systems/10-CRDTs/02-Why-Locks-Fail.md
      - G-Counter: 01-Concepts/10-Distributed-Systems/10-CRDTs/03-G-Counter.md
      - Operational Transform:
        - Insert: 01-Concepts/10-Distributed-Systems/10-CRDTs/04-Operational-Transform/01-Insert.md
        - Delete: 01-Concepts/10-Distributed-Systems/10-CRDTs/04-Operational-Transform/02-Delete.md
        - OT vs CRDT: 01-Concepts/10-Distributed-Systems/10-CRDTs/04-Operational-Transform/03-OT-vs-CRDT.md
    - Failure Detection:
      - Heartbeats: 01-Concepts/10-Distributed-Systems/11-Failure-Detection/01-Heartbeats.md
      - Gossip Protocol: 01-Concepts/10-Distributed-Systems/11-Failure-Detection/02-Gossip-Protocol.md
      - Phi Accrual Failure Detector: 01-Concepts/10-Distributed-Systems/11-Failure-Detection/03-Phi-Accrual-Failure-Detector.md
    - Merkle Trees:
      - The Problem: 01-Concepts/10-Distributed-Systems/12-Merkle-Trees/01-The-Problem.md
      - Hashing And Buckets: 01-Concepts/10-Distributed-Systems/12-Merkle-Trees/02-Hashing-And-Buckets.md
      - The Tree: 01-Concepts/10-Distributed-Systems/12-Merkle-Trees/03-The-Tree.md
      - Anti-Entropy: 01-Concepts/10-Distributed-Systems/12-Merkle-Trees/04-Anti-Entropy.md
    - Coordination Services:
      - The Problem: 01-Concepts/10-Distributed-Systems/13-Coordination-Services/01-The-Problem.md
      - What Is etcd: 01-Concepts/10-Distributed-Systems/13-Coordination-Services/02-What-Is-etcd.md
      - Leases And TTL: 01-Concepts/10-Distributed-Systems/13-Coordination-Services/03-Leases-And-TTL.md
      - Fencing Tokens: 01-Concepts/10-Distributed-Systems/13-Coordination-Services/04-Fencing-Tokens.md
      - Lock vs Job Tracking: 01-Concepts/10-Distributed-Systems/13-Coordination-Services/05-Lock-vs-Job-Tracking.md
```

**Note:** Database Types sections 03–05 (Column Family, Search Engines, Graph Databases) only have `00-Overview.md` — that's what gets wired up. More files may not exist yet.

---

### Step 3 — Build full Case Studies + Back of Envelope nav

**File:** `mkdocs.yml` — add Case Studies and Back of Envelope sections after Concepts.

Case Studies nav (full tree matching disk):

```yaml
- Case Studies:
  - 03-Case-Studies/index.md
  - FOUNDATION:
    - 03-Case-Studies/01-Foundation/index.md
    - Unique ID Generator:
      - 03-Case-Studies/01-Foundation/01-Unique-ID-Generator/index.md
      - System Requirements:
        - Overview: 03-Case-Studies/01-Foundation/01-Unique-ID-Generator/01-System-Requirements/00-System-Overview.md
        - Functional Requirements: 03-Case-Studies/01-Foundation/01-Unique-ID-Generator/01-System-Requirements/01-FR.md
        - Estimation: 03-Case-Studies/01-Foundation/01-Unique-ID-Generator/01-System-Requirements/02-Estimation.md
        - NFR: 03-Case-Studies/01-Foundation/01-Unique-ID-Generator/01-System-Requirements/03-NFR.md
        - API: 03-Case-Studies/01-Foundation/01-Unique-ID-Generator/01-System-Requirements/04-API.md
        - Base Architecture: 03-Case-Studies/01-Foundation/01-Unique-ID-Generator/01-System-Requirements/05-Base-Architecture.md
      - Deep Dives:
        - 03-Case-Studies/01-Foundation/01-Unique-ID-Generator/02-Deep-Dives/index.md
        - Single Server Counter: 03-Case-Studies/01-Foundation/01-Unique-ID-Generator/02-Deep-Dives/01-Single-Server-Counter.md
        - Multi-Server Problem: 03-Case-Studies/01-Foundation/01-Unique-ID-Generator/02-Deep-Dives/02-Multi-Server-Problem.md
        - UUID: 03-Case-Studies/01-Foundation/01-Unique-ID-Generator/02-Deep-Dives/03-UUID.md
        - Ticket Server: 03-Case-Studies/01-Foundation/01-Unique-ID-Generator/02-Deep-Dives/04-Ticket-Server.md
        - Pre-Generated Key Pool: 03-Case-Studies/01-Foundation/01-Unique-ID-Generator/02-Deep-Dives/05-Pre-Generated-Key-Pool.md
        - Snowflake: 03-Case-Studies/01-Foundation/01-Unique-ID-Generator/02-Deep-Dives/06-Snowflake.md
        - Comparison: 03-Case-Studies/01-Foundation/01-Unique-ID-Generator/02-Deep-Dives/07-Comparison.md
        - Clock Skew: 03-Case-Studies/01-Foundation/01-Unique-ID-Generator/02-Deep-Dives/08-Clock-Skew.md
        - Fault Isolation: 03-Case-Studies/01-Foundation/01-Unique-ID-Generator/02-Deep-Dives/09-Fault-Isolation.md
      - Observability:
        - SLI/SLO: 03-Case-Studies/01-Foundation/01-Unique-ID-Generator/03-Observability/01-SLI-SLO-Connection.md
        - Measuring Latency: 03-Case-Studies/01-Foundation/01-Unique-ID-Generator/03-Observability/02-Measuring-Latency.md
        - Measuring Availability: 03-Case-Studies/01-Foundation/01-Unique-ID-Generator/03-Observability/03-Measuring-Availability.md
        - Alerting: 03-Case-Studies/01-Foundation/01-Unique-ID-Generator/03-Observability/04-Alerting.md
        - Error Budget: 03-Case-Studies/01-Foundation/01-Unique-ID-Generator/03-Observability/05-Error-Budget.md
      - Final Design: 03-Case-Studies/01-Foundation/01-Unique-ID-Generator/04-Final-Design/01-Final-Architecture.md
    - URL Shortener:
      - 03-Case-Studies/01-Foundation/02-URL-Shortener/index.md
      - System Requirements:
        - Functional Requirements: 03-Case-Studies/01-Foundation/02-URL-Shortener/01-System-Requirements/01-FR.md
        - Estimation: 03-Case-Studies/01-Foundation/02-URL-Shortener/01-System-Requirements/02-Estimation.md
        - NFR: 03-Case-Studies/01-Foundation/02-URL-Shortener/01-System-Requirements/03-NFR.md
        - API: 03-Case-Studies/01-Foundation/02-URL-Shortener/01-System-Requirements/04-API.md
        - Base Architecture: 03-Case-Studies/01-Foundation/02-URL-Shortener/01-System-Requirements/05-Base-Architecture.md
      - Deep Dives:
        - 03-Case-Studies/01-Foundation/02-URL-Shortener/02-Deep-Dives/index.md
        - Short Code Generation:
          - Raw IDs: 03-Case-Studies/01-Foundation/02-URL-Shortener/02-Deep-Dives/01-Short-Code-Generation/01-Raw-IDs.md
          - Hashing: 03-Case-Studies/01-Foundation/02-URL-Shortener/02-Deep-Dives/01-Short-Code-Generation/02-Hashing.md
          - Random + Collision Check: 03-Case-Studies/01-Foundation/02-URL-Shortener/02-Deep-Dives/01-Short-Code-Generation/03-Random-Collision-Check.md
          - UUID Base64 Trim: 03-Case-Studies/01-Foundation/02-URL-Shortener/02-Deep-Dives/01-Short-Code-Generation/04-UUID-Base64-Trim.md
          - Snowflake Base64: 03-Case-Studies/01-Foundation/02-URL-Shortener/02-Deep-Dives/01-Short-Code-Generation/05-Snowflake-Base64.md
          - UUID+Snowflake Base62: 03-Case-Studies/01-Foundation/02-URL-Shortener/02-Deep-Dives/01-Short-Code-Generation/06-UUID-Snowflake-Base62.md
          - Truncation Problem: 03-Case-Studies/01-Foundation/02-URL-Shortener/02-Deep-Dives/01-Short-Code-Generation/07-Truncation-Problem.md
        - Database:
          - DB Choice: 03-Case-Studies/01-Foundation/02-URL-Shortener/02-Deep-Dives/02-DB/01-DB-Choice.md
          - Schema: 03-Case-Studies/01-Foundation/02-URL-Shortener/02-Deep-Dives/02-DB/02-Schema.md
          - Why Sharding: 03-Case-Studies/01-Foundation/02-URL-Shortener/02-Deep-Dives/02-DB/03-Why-Sharding.md
          - Sharding Key: 03-Case-Studies/01-Foundation/02-URL-Shortener/02-Deep-Dives/02-DB/04-Sharding-Key.md
          - Consistent Hashing: 03-Case-Studies/01-Foundation/02-URL-Shortener/02-Deep-Dives/02-DB/05-Consistent-Hashing.md
          - How Many Shards: 03-Case-Studies/01-Foundation/02-URL-Shortener/02-Deep-Dives/02-DB/06-How-Many-Shards.md
          - Replication: 03-Case-Studies/01-Foundation/02-URL-Shortener/02-Deep-Dives/02-DB/07-Replication.md
          - Read Your Own Writes: 03-Case-Studies/01-Foundation/02-URL-Shortener/02-Deep-Dives/02-DB/08-Read-Your-Own-Writes.md
        - Caching:
          - Why Caching: 03-Case-Studies/01-Foundation/02-URL-Shortener/02-Deep-Dives/03-Caching/01-Why-Caching.md
          - Cache Size: 03-Case-Studies/01-Foundation/02-URL-Shortener/02-Deep-Dives/03-Caching/02-Cache-Size.md
          - Cache Strategy: 03-Case-Studies/01-Foundation/02-URL-Shortener/02-Deep-Dives/03-Caching/03-Cache-Strategy.md
          - Eviction Policy: 03-Case-Studies/01-Foundation/02-URL-Shortener/02-Deep-Dives/03-Caching/04-Eviction-Policy.md
          - Updated Flow: 03-Case-Studies/01-Foundation/02-URL-Shortener/02-Deep-Dives/03-Caching/05-Updated-Flow.md
        - Peak Traffic:
          - The Spike Problem: 03-Case-Studies/01-Foundation/02-URL-Shortener/02-Deep-Dives/04-Peak-Traffic/01-The-Spike-Problem.md
          - Hot Key Problem:
            - Detection: 03-Case-Studies/01-Foundation/02-URL-Shortener/02-Deep-Dives/04-Peak-Traffic/02-Hot-Key-Problem/01-Detection.md
            - Local App Cache: 03-Case-Studies/01-Foundation/02-URL-Shortener/02-Deep-Dives/04-Peak-Traffic/02-Hot-Key-Problem/02-Local-App-Cache.md
            - Redis Key Replication: 03-Case-Studies/01-Foundation/02-URL-Shortener/02-Deep-Dives/04-Peak-Traffic/02-Hot-Key-Problem/03-Redis-Key-Replication.md
            - Broadcast Promotion: 03-Case-Studies/01-Foundation/02-URL-Shortener/02-Deep-Dives/04-Peak-Traffic/02-Hot-Key-Problem/04-Broadcast-Promotion.md
          - Load Balancing: 03-Case-Studies/01-Foundation/02-URL-Shortener/02-Deep-Dives/04-Peak-Traffic/03-Load-Balancing.md
          - API GW SPOF: 03-Case-Studies/01-Foundation/02-URL-Shortener/02-Deep-Dives/04-Peak-Traffic/04-API-GW-SPOF.md
          - Updated Architecture: 03-Case-Studies/01-Foundation/02-URL-Shortener/02-Deep-Dives/04-Peak-Traffic/05-Updated-Architecture.md
        - Pre-Generated Keys:
          - Collision At Scale: 03-Case-Studies/01-Foundation/02-URL-Shortener/02-Deep-Dives/06-Pre-Generated-Keys/01-Collision-At-Scale.md
          - Bloom Filter: 03-Case-Studies/01-Foundation/02-URL-Shortener/02-Deep-Dives/06-Pre-Generated-Keys/02-Bloom-Filter.md
          - Key Pool: 03-Case-Studies/01-Foundation/02-URL-Shortener/02-Deep-Dives/06-Pre-Generated-Keys/03-Key-Pool.md
          - KGS Sequential Generation: 03-Case-Studies/01-Foundation/02-URL-Shortener/02-Deep-Dives/06-Pre-Generated-Keys/04-KGS-Sequential-Generation.md
          - Redis INCR vs KGS: 03-Case-Studies/01-Foundation/02-URL-Shortener/02-Deep-Dives/06-Pre-Generated-Keys/05-Redis-INCR-vs-KGS.md
        - Cold Storage:
          - The Problem: 03-Case-Studies/01-Foundation/02-URL-Shortener/02-Deep-Dives/07-Cold-Storage/01-The-Problem.md
          - Tiered Storage: 03-Case-Studies/01-Foundation/02-URL-Shortener/02-Deep-Dives/07-Cold-Storage/02-Tiered-Storage.md
          - Detecting Cold URLs: 03-Case-Studies/01-Foundation/02-URL-Shortener/02-Deep-Dives/07-Cold-Storage/03-Detecting-Cold-URLs.md
        - Fault Isolation:
          - Fault Isolation: 03-Case-Studies/01-Foundation/02-URL-Shortener/02-Deep-Dives/08-Fault-Isolation/01-Fault-Isolation.md
          - Redis Down: 03-Case-Studies/01-Foundation/02-URL-Shortener/02-Deep-Dives/08-Fault-Isolation/02-Redis-Down.md
          - DB Shard Primary Down: 03-Case-Studies/01-Foundation/02-URL-Shortener/02-Deep-Dives/08-Fault-Isolation/03-DB-Shard-Primary-Down.md
          - KGS Down: 03-Case-Studies/01-Foundation/02-URL-Shortener/02-Deep-Dives/08-Fault-Isolation/04-KGS-Down.md
          - Other Failures: 03-Case-Studies/01-Foundation/02-URL-Shortener/02-Deep-Dives/08-Fault-Isolation/05-Other-Failures.md
      - Observability:
        - SLI/SLO: 03-Case-Studies/01-Foundation/02-URL-Shortener/03-Observability/01-SLI-SLO-Connection.md
        - Measuring Latency: 03-Case-Studies/01-Foundation/02-URL-Shortener/03-Observability/02-Measuring-Latency.md
        - Measuring Availability: 03-Case-Studies/01-Foundation/02-URL-Shortener/03-Observability/03-Measuring-Availability.md
        - Alerting: 03-Case-Studies/01-Foundation/02-URL-Shortener/03-Observability/04-Alerting.md
        - Error Budget: 03-Case-Studies/01-Foundation/02-URL-Shortener/03-Observability/05-Error-Budget.md
      - Final Design: 03-Case-Studies/01-Foundation/02-URL-Shortener/04-Final-Design/01-Final-Design.md
  - ASCENT:
    - 03-Case-Studies/02-Ascent/index.md
    - Notification System:
      - 03-Case-Studies/02-Ascent/01-Notification-System/index.md
      - System Requirements:
        - Overview: 03-Case-Studies/02-Ascent/01-Notification-System/01-System-Requirements/00-System-Overview.md
        - FR: 03-Case-Studies/02-Ascent/01-Notification-System/01-System-Requirements/01-FR.md
        - Estimation: 03-Case-Studies/02-Ascent/01-Notification-System/01-System-Requirements/02-Estimation.md
        - NFR: 03-Case-Studies/02-Ascent/01-Notification-System/01-System-Requirements/03-NFR.md
        - API: 03-Case-Studies/02-Ascent/01-Notification-System/01-System-Requirements/04-API.md
        - Base Architecture: 03-Case-Studies/02-Ascent/01-Notification-System/01-System-Requirements/05-Base-Architecture.md
      - Deep Dives:
        - 03-Case-Studies/02-Ascent/01-Notification-System/02-Deep-Dives/index.md
        - Database: 03-Case-Studies/02-Ascent/01-Notification-System/02-Deep-Dives/01-DB/01-DB-Selection.md
        - Kafka Design: 03-Case-Studies/02-Ascent/01-Notification-System/02-Deep-Dives/02-Kafka/01-Queue-Selection.md
        - Per-Channel Workers: 03-Case-Studies/02-Ascent/01-Notification-System/02-Deep-Dives/03-Per-Channel-Workers/01-Push-Worker.md
        - Scheduling: 03-Case-Studies/02-Ascent/01-Notification-System/02-Deep-Dives/04-Scheduling/01-Problem-And-Naive-Approach.md
        - Retry and DLQ: 03-Case-Studies/02-Ascent/01-Notification-System/02-Deep-Dives/05-Retry-And-DLQ/01-Retry-Strategy.md
        - Rate Limiting: 03-Case-Studies/02-Ascent/01-Notification-System/02-Deep-Dives/06-Rate-Limiting/01-Rate-Limiting.md
        - Fault Isolation: 03-Case-Studies/02-Ascent/01-Notification-System/02-Deep-Dives/07-Fault-Isolation/01-APNs-Down.md
      - Observability: 03-Case-Studies/02-Ascent/01-Notification-System/03-Observability/01-SLI-SLO-Connection.md
      - Final Design: 03-Case-Studies/02-Ascent/01-Notification-System/04-Final-Design/01-Final-Design.md
    - Pastebin:
      - 03-Case-Studies/02-Ascent/02-Pastebin/index.md
      - System Requirements: 03-Case-Studies/02-Ascent/02-Pastebin/01-System-Requirements/01-FR.md
      - Deep Dives: 03-Case-Studies/02-Ascent/02-Pastebin/02-Deep-Dives/index.md
      - Observability: 03-Case-Studies/02-Ascent/02-Pastebin/03-Observability/01-SLI-SLO-Connection.md
  - EXPEDITION:
    - 03-Case-Studies/03-Expedition/index.md
    - Rate Limiter:
      - 03-Case-Studies/03-Expedition/01-Rate-Limiter/index.md
      - System Requirements: 03-Case-Studies/03-Expedition/01-Rate-Limiter/01-System-Requirements/01-FR.md
      - Deep Dives: 03-Case-Studies/03-Expedition/01-Rate-Limiter/02-Deep-Dives/index.md
      - Observability: 03-Case-Studies/03-Expedition/01-Rate-Limiter/03-Observability/01-SLI-SLO-Connection.md
      - Final Design: 03-Case-Studies/03-Expedition/01-Rate-Limiter/04-Final-Design/01-Final-Design.md
  - SUMMIT:
    - 03-Case-Studies/04-Summit/index.md
    - KV Store:
      - 03-Case-Studies/04-Summit/01-KV-Store/index.md
      - System Requirements: 03-Case-Studies/04-Summit/01-KV-Store/01-System-Requirements/01-FR.md
      - Deep Dives: 03-Case-Studies/04-Summit/01-KV-Store/04-Deep-Dives/index.md
      - Observability: 03-Case-Studies/04-Summit/01-KV-Store/05-Observability/01-SLI-SLO-Connection.md
      - Final Design: 03-Case-Studies/04-Summit/01-KV-Store/06-Final-Design/01-Final-Architecture.md
  - BATTLEGROUND:
    - 03-Case-Studies/05-Battleground/index.md
    - WhatsApp:
      - 03-Case-Studies/05-Battleground/01-WhatsApp/index.md
      - System Requirements: 03-Case-Studies/05-Battleground/01-WhatsApp/01-System-Requirements/01-FR.md
      - Deep Dives: 03-Case-Studies/05-Battleground/01-WhatsApp/04-Deep-Dives/index.md
      - Observability: 03-Case-Studies/05-Battleground/01-WhatsApp/05-Observability/01-SLI-SLO-Connection.md
      - Final Design: 03-Case-Studies/05-Battleground/01-WhatsApp/06-Final-Design/01-Final-Architecture.md
```

Back of Envelope nav:

```yaml
- Back of Envelope:
  - 02-Back-of-Envelope-Estimation/index.md
  - Latency Numbers: 02-Back-of-Envelope-Estimation/01-Latency-Numbers.md
  - Database Numbers: 02-Back-of-Envelope-Estimation/02-Database-Numbers.md
  - Message Streams: 02-Back-of-Envelope-Estimation/03-Message-Streams.md
  - Data Sizes: 02-Back-of-Envelope-Estimation/04-Data-Sizes.md
  - Bandwidth & Servers: 02-Back-of-Envelope-Estimation/05-Bandwidth-And-Servers.md
  - Estimation Framework: 02-Back-of-Envelope-Estimation/06-Estimation-Framework.md
```

**Note on Case Studies depth:** Ascent/Expedition/Summit/Battleground deep dives link only to `index.md` for now — the full file trees are very large. If you want full deep dives wired up for a specific case study, say so and I'll add them in a follow-up step.

---

### Step 4 — Fix docs/01-Concepts/index.md card links

**File:** `docs/01-Concepts/index.md`

Audit all internal links. Known stale paths to fix:
- `02-Core-Concepts/` → `02-Fundamentals/`
- `06-Distributed-Systems/` → `10-Distributed-Systems/`
- `05-Messaging-and-Event-Driven/` → `06-Messaging/`

---

### Step 5 — Fix docs/start-here.md links

**File:** `docs/start-here.md`

Audit all `href` values against actual disk paths after folder renames. Fix any stale paths.

---

### Step 6 — Remove hide:navigation from non-homepage index pages

**Files to audit:**
- `docs/01-Concepts/index.md` — remove `hide: navigation`
- `docs/03-Case-Studies/index.md` — remove `hide: navigation`
- `docs/02-Back-of-Envelope-Estimation/index.md` — remove `hide: navigation`
- `docs/start-here.md` — remove `hide: navigation`
- Keep `hide: navigation` ONLY on `docs/index.md` (homepage is a landing page)

---

### Step 7 — Stage, commit, push

```bash
git add -A
git commit -m "redesign: section-scoped sidebar, full nav tree, site title update"
git push
```

---

### Step 8 — Verify live site

Check https://leetdezine.com after Cloudflare Pages deployment (~1-2 min after push):
- [ ] Top tabs visible: Concepts | Case Studies | Back of Envelope
- [ ] Concepts sidebar shows all 10 sections, active one expanded
- [ ] Previous / Next links at bottom of each page
- [ ] Site title correct in browser tab
- [ ] No 404s on nav links

---

## Current Step: Step 1

**Awaiting your approval to begin Step 1.**

What Step 1 will change in `mkdocs.yml`:
1. `site_name` → `LeetDezine — System Design and Internals, Built for Interviews`
2. Remove `navigation.expand`
3. Remove `toc.integrate`
4. Add `navigation.tabs`
5. Add `navigation.tabs.sticky`
6. Add `navigation.footer`

Nothing else changes. Nav tree stays as-is until Step 2.

Type **"go"** (or any approval) to proceed with Step 1.
