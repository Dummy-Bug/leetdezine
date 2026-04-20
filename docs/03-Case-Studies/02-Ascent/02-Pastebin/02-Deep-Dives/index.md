---
title: Deep Dives
hide:
  - navigation
  - toc
---

<div class="cs-level-hero cs-lv2">
  <div class="cs-level-bg-num">DD</div>
  <div class="cs-level-inner">
    <p class="cs-level-eyebrow">Pastebin · Deep Dives</p>
    <h1 class="cs-level-title">Deep Dives</h1>
    <p class="cs-level-sub">Eight deep dives — short code generation, database, caching, peak traffic, fault isolation, async S3 upload, expiry cleanup, and final architecture.</p>
  </div>
</div>

<div class="cs-concepts-grid cs-concepts-index-grid">

  <a href="01-Short-Code-Generation/01-Requirements/" class="cs-concept-card cs-concept-c4">
    <div class="cs-concept-card-title">Short Code Generation</div>
    <div class="cs-concept-card-desc">Requirements, generation approaches, Redis counter, and custom alias support.</div>
    <div class="cs-concept-chips">
      <span>Redis Counter</span><span>Custom Alias</span><span>Collision</span>
    </div>
    <div class="cs-concept-cta">Open <span>→</span></div>
  </a>

  <a href="02-DB/01-DB-Choice/" class="cs-concept-card cs-concept-c4">
    <div class="cs-concept-card-title">Database</div>
    <div class="cs-concept-card-desc">DB choice, content-addressable storage, ref counting, schema design, write/read/delete flows, and sharding.</div>
    <div class="cs-concept-chips">
      <span>CAS</span><span>Ref Counting</span><span>Schema</span><span>Sharding</span>
    </div>
    <div class="cs-concept-cta">Open <span>→</span></div>
  </a>

  <a href="03-Caching/01-Why-Cache/" class="cs-concept-card cs-concept-c4">
    <div class="cs-concept-card-title">Caching</div>
    <div class="cs-concept-card-desc">Why cache, what to cache, cache sizing, and invalidation strategy.</div>
    <div class="cs-concept-chips">
      <span>Redis</span><span>Cache Sizing</span><span>Invalidation</span>
    </div>
    <div class="cs-concept-cta">Open <span>→</span></div>
  </a>

  <a href="04-Peak-Traffic/01-Hot-Key-Problem/" class="cs-concept-card cs-concept-c4">
    <div class="cs-concept-card-title">Peak Traffic</div>
    <div class="cs-concept-card-desc">Hot key problem for viral pastes — detection, mitigation, and local cache approach.</div>
    <div class="cs-concept-chips">
      <span>Hot Key</span><span>Viral Paste</span><span>Local Cache</span>
    </div>
    <div class="cs-concept-cta">Open <span>→</span></div>
  </a>

  <a href="05-Fault-Isolation/01-Why-Fault-Isolation/" class="cs-concept-card cs-concept-c4">
    <div class="cs-concept-card-title">Fault Isolation</div>
    <div class="cs-concept-card-desc">Service split, DB standby, and circuit breaker to contain failures.</div>
    <div class="cs-concept-chips">
      <span>Service Split</span><span>DB Standby</span><span>Circuit Breaker</span>
    </div>
    <div class="cs-concept-cta">Open <span>→</span></div>
  </a>

  <a href="06-Async-S3-Upload/01-Why-Async-Upload/" class="cs-concept-card cs-concept-c4">
    <div class="cs-concept-card-title">Async S3 Upload</div>
    <div class="cs-concept-card-desc">Why async, failure problem, state machine, retry strategy, and read path behaviour.</div>
    <div class="cs-concept-chips">
      <span>S3</span><span>State Machine</span><span>Async</span><span>Retry</span>
    </div>
    <div class="cs-concept-cta">Open <span>→</span></div>
  </a>

  <a href="07-Expiry-Cleanup-Job/01-Why-Cleanup-Job/" class="cs-concept-card cs-concept-c4">
    <div class="cs-concept-card-title">Expiry Cleanup Job</div>
    <div class="cs-concept-card-desc">Cleanup flow, distributed workers, watchdog process, and indexing strategy for expired pastes.</div>
    <div class="cs-concept-chips">
      <span>TTL</span><span>Distributed Workers</span><span>Watchdog</span><span>Indexing</span>
    </div>
    <div class="cs-concept-cta">Open <span>→</span></div>
  </a>

  <a href="08-Updated-Architecture/01-Updated-Architecture/" class="cs-concept-card cs-concept-c4">
    <div class="cs-concept-card-title">Updated Architecture</div>
    <div class="cs-concept-card-desc">Full system diagram after all deep dives applied — every component justified.</div>
    <div class="cs-concept-chips">
      <span>Final Diagram</span><span>Full Architecture</span>
    </div>
    <div class="cs-concept-cta">Open <span>→</span></div>
  </a>

</div>
