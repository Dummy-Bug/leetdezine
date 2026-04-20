---
title: Storage & Databases
hide:
  - navigation
  - toc
---

<div class="cs-level-hero cs-lv-concepts">
  <div class="cs-level-bg-num">04</div>
  <div class="cs-level-inner">
    <p class="cs-level-eyebrow">Concepts</p>
    <h1 class="cs-level-title">Storage & Databases</h1>
    <p class="cs-level-sub">How data is stored, indexed, replicated, and queried at scale. The layer every system design eventually has to justify.</p>
  </div>
</div>

<div class="cs-cards">

  <a class="cs-card" href="01-Fundamentals/01-Why-Not-Files/">
    <div class="cs-card-title">Fundamentals</div>
    <div class="cs-card-desc">Why not files? How databases actually store data — row vs column orientation, heap files, and the storage engine basics that explain everything above.</div>
    <div class="cs-topics">
      <span>Row Storage</span><span>Column Storage</span><span>Heap Files</span><span>Storage Engine</span>
    </div>
    <div class="cs-card-cta">Open topic <span>→</span></div>
  </a>

  <a class="cs-card" href="02-ACID/01-The-Problem/">
    <div class="cs-card-title">ACID</div>
    <div class="cs-card-desc">Atomicity, consistency, isolation, durability. Transaction isolation levels, distributed transactions, 2PC, and Saga — everything about keeping data correct under concurrency.</div>
    <div class="cs-topics">
      <span>Isolation Levels</span><span>2PC</span><span>Saga</span><span>ACID vs BASE</span>
    </div>
    <div class="cs-card-cta">Open topic <span>→</span></div>
  </a>

  <a class="cs-card" href="03-SQL/01-Relational-Model/">
    <div class="cs-card-title">SQL</div>
    <div class="cs-card-desc">Relational model, normalisation, denormalisation tradeoffs, joins, and views. The fundamentals before you decide SQL isn't enough.</div>
    <div class="cs-topics">
      <span>Normalisation</span><span>Denormalisation</span><span>Joins</span><span>Views</span>
    </div>
    <div class="cs-card-cta">Open topic <span>→</span></div>
  </a>

  <a class="cs-card" href="04-Indexing/01-Indexes/">
    <div class="cs-card-title">Indexing</div>
    <div class="cs-card-desc">Hash indexes, B+ Trees, LSM Trees, and geospatial indexing. The data structures that make reads fast and writes expensive — and when each one wins.</div>
    <div class="cs-topics">
      <span>B+ Tree</span><span>LSM Tree</span><span>Hash Index</span><span>Geospatial</span>
    </div>
    <div class="cs-card-cta">Open topic <span>→</span></div>
  </a>

  <a class="cs-card" href="05-Replication/01-What-is-Replication/">
    <div class="cs-card-title">Replication</div>
    <div class="cs-card-desc">Sync vs async replication, replication lag, failover, and multi-primary. How you keep multiple copies of data consistent without destroying write throughput.</div>
    <div class="cs-topics">
      <span>Sync vs Async</span><span>Replication Lag</span><span>Failover</span><span>Multi-Primary</span>
    </div>
    <div class="cs-card-cta">Open topic <span>→</span></div>
  </a>

  <a class="cs-card" href="06-Sharding/01-What-is-Sharding/">
    <div class="cs-card-title">Sharding</div>
    <div class="cs-card-desc">Shard keys, sharding strategies, consistent hashing, cross-shard joins, resharding, and over-sharding. How you split a database that's too big for one node.</div>
    <div class="cs-topics">
      <span>Shard Key</span><span>Consistent Hashing</span><span>Resharding</span><span>Cross-Shard Joins</span>
    </div>
    <div class="cs-card-cta">Open topic <span>→</span></div>
  </a>

  <a class="cs-card" href="07-MVCC/01-Concurrency-Control/">
    <div class="cs-card-title">MVCC</div>
    <div class="cs-card-desc">Multi-Version Concurrency Control. How databases serve reads without blocking writes by keeping multiple versions of the same row alive simultaneously.</div>
    <div class="cs-topics">
      <span>MVCC</span><span>Snapshot Isolation</span><span>Version Chains</span><span>Garbage Collection</span>
    </div>
    <div class="cs-card-cta">Open topic <span>→</span></div>
  </a>

  <a class="cs-card" href="08-CDC/01-What-is-CDC/">
    <div class="cs-card-title">CDC</div>
    <div class="cs-card-desc">Change Data Capture and the outbox pattern. How you stream database changes to downstream systems without dual-write bugs.</div>
    <div class="cs-topics">
      <span>CDC</span><span>Outbox Pattern</span><span>Debezium</span><span>Log Tailing</span>
    </div>
    <div class="cs-card-cta">Open topic <span>→</span></div>
  </a>

  <a class="cs-card" href="09-Pagination/01-Offset-Pagination/">
    <div class="cs-card-title">Pagination</div>
    <div class="cs-card-desc">Offset vs cursor pagination. Why offset pagination breaks at scale and how cursor-based pagination solves it without re-scanning the whole table.</div>
    <div class="cs-topics">
      <span>Offset Pagination</span><span>Cursor Pagination</span><span>Keyset Pagination</span><span>Deep Pages</span>
    </div>
    <div class="cs-card-cta">Open topic <span>→</span></div>
  </a>

  <a class="cs-card" href="10-Connection-Pooling/01-Cost-Of-A-Connection/">
    <div class="cs-card-title">Connection Pooling</div>
    <div class="cs-card-desc">The real cost of a database connection and how connection pools amortize it. What happens when the pool is exhausted and how to size it correctly.</div>
    <div class="cs-topics">
      <span>Connection Cost</span><span>Pool Sizing</span><span>Pool Exhaustion</span><span>PgBouncer</span>
    </div>
    <div class="cs-card-cta">Open topic <span>→</span></div>
  </a>

  <a class="cs-card" href="11-Read-Write-Splitting/01-The-Problem/">
    <div class="cs-card-title">Read / Write Splitting</div>
    <div class="cs-card-desc">Routing reads to replicas and writes to primary. The replication lag problem that follows, and when read/write splitting actually helps vs hurts.</div>
    <div class="cs-topics">
      <span>Read Replicas</span><span>Replication Lag</span><span>Stale Reads</span><span>Routing</span>
    </div>
    <div class="cs-card-cta">Open topic <span>→</span></div>
  </a>

  <a class="cs-card" href="12-Database-Types/01-Key-Value-Stores/00-Overview/">
    <div class="cs-card-title">Database Types</div>
    <div class="cs-card-desc">Key-value, document, column-family, search engines, graph, blob storage, NewSQL, OLTP vs OLAP. Every database type, when it wins, and when it doesn't.</div>
    <div class="cs-topics">
      <span>Redis</span><span>Cassandra</span><span>MongoDB</span><span>Elasticsearch</span>
    </div>
    <div class="cs-card-cta">Open topic <span>→</span></div>
  </a>

  <a class="cs-card" href="13-Choosing-The-Right-DB/01-Decision-Framework/">
    <div class="cs-card-title">Choosing the Right DB</div>
    <div class="cs-card-desc">A decision framework and cheatsheet for picking the right database given your access patterns, consistency needs, and scale requirements.</div>
    <div class="cs-topics">
      <span>Decision Framework</span><span>Access Patterns</span><span>DB Cheatsheet</span><span>Tradeoffs</span>
    </div>
    <div class="cs-card-cta">Open topic <span>→</span></div>
  </a>

  <a class="cs-card" href="14-Data-Modeling/01-The-Process/">
    <div class="cs-card-title">Data Modeling</div>
    <div class="cs-card-desc">Entities, relationships, access patterns, and red flags. How to model data for a real system — with a worked Instagram schema as the example.</div>
    <div class="cs-topics">
      <span>ER Modeling</span><span>Access Patterns</span><span>Instagram Schema</span><span>Red Flags</span>
    </div>
    <div class="cs-card-cta">Open topic <span>→</span></div>
  </a>

</div>
