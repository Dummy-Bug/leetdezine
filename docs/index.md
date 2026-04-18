---
title: ""
hide:
  - navigation
  - toc
---

<div class="cs-landing">

<section class="cs-hero">
  <div class="cs-hero-eyebrow">System Design · Deep Dives</div>
  <h1 class="cs-hero-title">Design systems <span class="cs-hero-accent">beyond the whiteboard.</span></h1>
  <p class="cs-hero-sub">Interview-depth case studies where every decision is justified. Built as a progression — start from first principles, climb to distributed systems.</p>
  <div class="cs-hero-meta">
    <div class="cs-hero-stat"><span class="cs-hero-stat-value">5</span><span class="cs-hero-stat-label">Levels</span></div>
    <div class="cs-hero-stat"><span class="cs-hero-stat-value">6</span><span class="cs-hero-stat-label">Case studies</span></div>
    <div class="cs-hero-stat"><span class="cs-hero-stat-value">200+</span><span class="cs-hero-stat-label">Deep dives</span></div>
  </div>
</section>

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
      <h3 class="cs-step-title">Blob storage & async pipelines</h3>
      <p class="cs-step-desc">Content deduplication, async upload flows, expiry at scale, distributed cleanup workers, fault tolerance patterns.</p>
      <div class="cs-step-chips">
        <span class="cs-chip">Content-addressable storage</span>
        <span class="cs-chip">Ref counting</span>
        <span class="cs-chip">Async S3 upload</span>
        <span class="cs-chip">State machines</span>
        <span class="cs-chip">Circuit breaker</span>
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
