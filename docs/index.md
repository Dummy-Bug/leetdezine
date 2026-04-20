---
title: "LeetDezine — System Design Deep Dives"
hide:
  - navigation
  - toc
---

<div class="cs-landing">

<section class="cs-hero">
  <div class="cs-hero-eyebrow">System Design · Deep Dives</div>
  <h1 class="cs-hero-title">Design systems <span class="cs-hero-accent">beyond the whiteboard.</span></h1>
  <p class="cs-hero-sub">Interview-depth case studies where every decision is justified. Built as a progression — start from first principles, climb to distributed systems.</p>
</section>

<section class="cs-concepts">
  <div class="cs-concepts-label">Concepts</div>
  <div class="cs-concepts-grid">
    <a href="Concepts/" class="cs-concept-card cs-concept-c1">
      <div class="cs-concept-card-title">Core Concepts</div>
      <div class="cs-concept-card-desc">Availability, reliability, scalability, CAP theorem, consistency models, fault tolerance, PACELC.</div>
    </a>
    <a href="Concepts/" class="cs-concept-card cs-concept-c2">
      <div class="cs-concept-card-title">Storage & Databases</div>
      <div class="cs-concept-card-desc">ACID, indexing, sharding, replication, database types, data modeling, CDC, pagination.</div>
    </a>
    <a href="Concepts/" class="cs-concept-card cs-concept-c3">
      <div class="cs-concept-card-title">Caching</div>
      <div class="cs-concept-card-desc">Write strategies, eviction policies, cache invalidation, distributed caching, Redis, cache problems.</div>
    </a>
  </div>
</section>

<div class="cs-section-divider">
  <span class="cs-section-divider-label">Back of Envelope Estimation</span>
</div>

<section class="cs-concepts">
  <div class="cs-concepts-grid cs-concepts-grid-wide">
    <a href="Back-of-Envelope-Estimation/01-Latency-Numbers/" class="cs-concept-card cs-concept-c4">
      <div class="cs-concept-card-title">Latency Numbers</div>
      <div class="cs-concept-card-desc">Every number you need to know — memory, disk, network.</div>
    </a>
    <a href="Back-of-Envelope-Estimation/02-Database-Numbers/" class="cs-concept-card cs-concept-c4">
      <div class="cs-concept-card-title">Database Numbers</div>
      <div class="cs-concept-card-desc">Read/write throughput, storage sizes, query costs.</div>
    </a>
    <a href="Back-of-Envelope-Estimation/03-Message-Streams/" class="cs-concept-card cs-concept-c4">
      <div class="cs-concept-card-title">Message Streams</div>
      <div class="cs-concept-card-desc">Kafka throughput, queue sizing, consumer lag.</div>
    </a>
    <a href="Back-of-Envelope-Estimation/06-Estimation-Framework/" class="cs-concept-card cs-concept-c4">
      <div class="cs-concept-card-title">Estimation Framework</div>
      <div class="cs-concept-card-desc">A reusable framework for any system design estimation.</div>
    </a>
  </div>
</section>

<div class="cs-section-divider">
  <span class="cs-section-divider-label">Apply the Concepts — Case Studies</span>
</div>

<section class="cs-journey">

  <div class="cs-journey-rail" aria-hidden="true"></div>

  <a href="01-Foundation/" class="cs-journey-step cs-step-lv1">
    <div class="cs-step-marker"><span class="cs-step-num">01</span></div>
    <div class="cs-step-body">
      <div class="cs-step-head">
        <span class="cs-step-tag">Foundation</span>
        <span class="cs-step-difficulty">● ○ ○ ○ ○</span>
      </div>
      <h3 class="cs-step-title">First principles of scale</h3>
      <p class="cs-step-desc">Unique ID schemes, sharding strategies, read-heavy caching, hot key mitigation, pre-generated key pools, tiered storage.</p>
      <div class="cs-step-chips">
        <span class="cs-chip">Snowflake ID</span>
        <span class="cs-chip">UUID</span>
        <span class="cs-chip">Clock skew</span>
        <span class="cs-chip">Consistent hashing</span>
        <span class="cs-chip">Bloom filters</span>
        <span class="cs-chip">KGS</span>
        <span class="cs-chip">Hot key problem</span>
        <span class="cs-chip">Cold storage</span>
      </div>
    </div>
    <div class="cs-step-cta">Start <span>→</span></div>
  </a>

  <a href="02-Ascent/" class="cs-journey-step cs-step-lv2">
    <div class="cs-step-marker"><span class="cs-step-num">02</span></div>
    <div class="cs-step-body">
      <div class="cs-step-head">
        <span class="cs-step-tag">Ascent</span>
        <span class="cs-step-difficulty">● ● ○ ○ ○</span>
      </div>
      <h3 class="cs-step-title">Async pipelines & multi-channel delivery</h3>
      <p class="cs-step-desc">Kafka fan-out, per-channel workers, retry/DLQ, scheduled dispatch, content deduplication, async uploads, expiry at scale.</p>
      <div class="cs-step-chips">
        <span class="cs-chip">Kafka fan-out</span>
        <span class="cs-chip">Retry / DLQ</span>
        <span class="cs-chip">Bloom filter</span>
        <span class="cs-chip">Circuit breaker</span>
        <span class="cs-chip">Content-addressable storage</span>
        <span class="cs-chip">Async S3 upload</span>
        <span class="cs-chip">TTL sweeper</span>
        <span class="cs-chip">Watchdog</span>
      </div>
    </div>
    <div class="cs-step-cta">Open <span>→</span></div>
  </a>

  <a href="03-Expedition/" class="cs-journey-step cs-step-lv3">
    <div class="cs-step-marker"><span class="cs-step-num">03</span></div>
    <div class="cs-step-body">
      <div class="cs-step-head">
        <span class="cs-step-tag">Expedition</span>
        <span class="cs-step-difficulty">● ● ● ○ ○</span>
      </div>
      <h3 class="cs-step-title">Distributed rate control</h3>
      <p class="cs-step-desc">Rate limiting algorithms from scratch, atomic Redis counters, distributed enforcement, rule management, DDoS layered defence.</p>
      <div class="cs-step-chips">
        <span class="cs-chip">Token bucket</span>
        <span class="cs-chip">Leaky bucket</span>
        <span class="cs-chip">Sliding window</span>
        <span class="cs-chip">Fixed window</span>
        <span class="cs-chip">Lua atomicity</span>
        <span class="cs-chip">Redis cluster</span>
        <span class="cs-chip">DDoS defence</span>
      </div>
    </div>
    <div class="cs-step-cta">Open <span>→</span></div>
  </a>

  <a href="04-Summit/" class="cs-journey-step cs-step-lv4">
    <div class="cs-step-marker"><span class="cs-step-num">04</span></div>
    <div class="cs-step-body">
      <div class="cs-step-head">
        <span class="cs-step-tag">Summit</span>
        <span class="cs-step-difficulty">● ● ● ● ○</span>
      </div>
      <h3 class="cs-step-title">Storage engine internals</h3>
      <p class="cs-step-desc">Leaderless replication, quorum reads/writes, LSM tree internals, compaction strategies, gossip membership, conflict resolution.</p>
      <div class="cs-step-chips">
        <span class="cs-chip">LSM trees</span>
        <span class="cs-chip">Compaction</span>
        <span class="cs-chip">Bloom filters</span>
        <span class="cs-chip">Quorum W/R</span>
        <span class="cs-chip">Gossip protocol</span>
        <span class="cs-chip">Hinted handoff</span>
        <span class="cs-chip">Vector clocks</span>
        <span class="cs-chip">Anti-entropy</span>
      </div>
    </div>
    <div class="cs-step-cta">Open <span>→</span></div>
  </a>

  <a href="05-Battleground/" class="cs-journey-step cs-step-lv5">
    <div class="cs-step-marker"><span class="cs-step-num">05</span></div>
    <div class="cs-step-body">
      <div class="cs-step-head">
        <span class="cs-step-tag">Battleground</span>
        <span class="cs-step-difficulty">● ● ● ● ●</span>
      </div>
      <h3 class="cs-step-title">Real-time systems at scale</h3>
      <p class="cs-step-desc">WebSocket connection management, per-conversation sequencing, offline queues, thundering herd, backpressure, hot partition salting.</p>
      <div class="cs-step-chips">
        <span class="cs-chip">WebSockets</span>
        <span class="cs-chip">Per-conv. sequencing</span>
        <span class="cs-chip">Offline delivery</span>
        <span class="cs-chip">Thundering herd</span>
        <span class="cs-chip">Backpressure</span>
        <span class="cs-chip">Hot partition salting</span>
        <span class="cs-chip">Reconnect storm</span>
        <span class="cs-chip">Read receipts</span>
      </div>
    </div>
    <div class="cs-step-cta">Open <span>→</span></div>
  </a>

</section>

<section class="cs-footer-note">
  <p>Each case study is a progression: <b>requirements → estimation → base architecture → deep dives → final design → observability</b>. Read top-to-bottom, or jump straight to the deep dive you want.</p>
</section>

</div>
