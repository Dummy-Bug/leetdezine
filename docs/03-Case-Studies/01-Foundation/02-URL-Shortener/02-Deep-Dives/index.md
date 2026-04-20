---
title: Deep Dives
hide:
  - navigation
  - toc
---

<div class="cs-level-hero cs-lv1">
  <div class="cs-level-bg-num">DD</div>
  <div class="cs-level-inner">
    <p class="cs-level-eyebrow">URL Shortener · Deep Dives</p>
    <h1 class="cs-level-title">Deep Dives</h1>
    <p class="cs-level-sub">Seven focused deep dives — short code generation, database sharding, caching, hot key mitigation, pre-generated keys, cold storage, and fault isolation.</p>
  </div>
</div>

<div class="cs-concepts-grid cs-concepts-index-grid">

  <a href="01-Short-Code-Generation/01-Raw-IDs/" class="cs-concept-card cs-concept-c4">
    <div class="cs-concept-card-title">Short Code Generation</div>
    <div class="cs-concept-card-desc">Raw IDs, hashing, collision handling, UUID variants, Snowflake, and truncation tradeoffs.</div>
    <div class="cs-concept-chips">
      <span>Raw IDs</span><span>Hashing</span><span>UUID</span><span>Snowflake</span><span>Collision</span>
    </div>
    <div class="cs-concept-cta">Open <span>→</span></div>
  </a>

  <a href="02-DB/01-DB-Choice/" class="cs-concept-card cs-concept-c4">
    <div class="cs-concept-card-title">Database</div>
    <div class="cs-concept-card-desc">DB choice, schema design, sharding strategy, consistent hashing, replication, and read-your-own-writes.</div>
    <div class="cs-concept-chips">
      <span>Sharding</span><span>Consistent Hashing</span><span>Replication</span><span>Schema</span>
    </div>
    <div class="cs-concept-cta">Open <span>→</span></div>
  </a>

  <a href="03-Caching/01-Why-Caching/" class="cs-concept-card cs-concept-c4">
    <div class="cs-concept-card-title">Caching</div>
    <div class="cs-concept-card-desc">Why to cache, cache sizing, eviction policy, and updated redirect flow with Redis.</div>
    <div class="cs-concept-chips">
      <span>Redis</span><span>Cache Size</span><span>Eviction</span><span>Read Path</span>
    </div>
    <div class="cs-concept-cta">Open <span>→</span></div>
  </a>

  <a href="04-Peak-Traffic/01-The-Spike-Problem/" class="cs-concept-card cs-concept-c4">
    <div class="cs-concept-card-title">Peak Traffic</div>
    <div class="cs-concept-card-desc">The spike problem, hot key detection, local app cache, Redis key replication, and broadcast promotion.</div>
    <div class="cs-concept-chips">
      <span>Hot Key</span><span>Local Cache</span><span>Redis Replication</span><span>Broadcast</span>
    </div>
    <div class="cs-concept-cta">Open <span>→</span></div>
  </a>

  <a href="06-Pre-Generated-Keys/01-Collision-At-Scale/" class="cs-concept-card cs-concept-c4">
    <div class="cs-concept-card-title">Pre-Generated Keys</div>
    <div class="cs-concept-card-desc">Bloom filter for collision avoidance, pre-generated key pool, KGS design, Redis INCR vs KGS tradeoffs.</div>
    <div class="cs-concept-chips">
      <span>Bloom Filter</span><span>KGS</span><span>Key Pool</span><span>Redis INCR</span>
    </div>
    <div class="cs-concept-cta">Open <span>→</span></div>
  </a>

  <a href="07-Cold-Storage/01-The-Problem/" class="cs-concept-card cs-concept-c4">
    <div class="cs-concept-card-title">Cold Storage</div>
    <div class="cs-concept-card-desc">Tiered storage for inactive URLs, detecting cold URLs, and storage cost reduction at scale.</div>
    <div class="cs-concept-chips">
      <span>Tiered Storage</span><span>Cold URLs</span><span>S3</span><span>Cost</span>
    </div>
    <div class="cs-concept-cta">Open <span>→</span></div>
  </a>

  <a href="08-Fault-Isolation/01-Fault-Isolation/" class="cs-concept-card cs-concept-c4">
    <div class="cs-concept-card-title">Fault Isolation</div>
    <div class="cs-concept-card-desc">Redis down, DB shard primary down, KGS down, and other failure scenario mitigations.</div>
    <div class="cs-concept-chips">
      <span>Redis Down</span><span>Shard Failure</span><span>KGS Down</span><span>Circuit Breaker</span>
    </div>
    <div class="cs-concept-cta">Open <span>→</span></div>
  </a>

</div>
