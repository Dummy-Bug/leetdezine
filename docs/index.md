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
    <div class="cs-hero-stat"><span class="cs-hero-stat-value">5</span><span class="cs-hero-stat-label">Case studies</span></div>
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
      <h3 class="cs-step-title">URL Shortener</h3>
      <p class="cs-step-desc">Short-code generation, sharding fundamentals, read-heavy cache strategy.</p>
      <div class="cs-step-chips">
        <span class="cs-chip">Bloom filters</span>
        <span class="cs-chip">KGS</span>
        <span class="cs-chip">Consistent hashing</span>
        <span class="cs-chip">Tiered storage</span>
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
      <h3 class="cs-step-title">Pastebin</h3>
      <p class="cs-step-desc">Blob storage, content-addressable dedup, async S3 pipelines, expiry sweepers.</p>
      <div class="cs-step-chips">
        <span class="cs-chip">CAS</span>
        <span class="cs-chip">Ref counting</span>
        <span class="cs-chip">State machines</span>
        <span class="cs-chip">Circuit breaker</span>
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
      <h3 class="cs-step-title">Rate Limiter</h3>
      <p class="cs-step-desc">Token / leaky / sliding windows, atomic counters, Lua scripts, DDoS defense.</p>
      <div class="cs-step-chips">
        <span class="cs-chip">Token bucket</span>
        <span class="cs-chip">Lua scripts</span>
        <span class="cs-chip">Redis cluster</span>
        <span class="cs-chip">Rule storage</span>
      </div>
    </div>
    <div class="cs-step-cta">Open <span>→</span></div>
  </a>

  <a href="04-Summit/02-KV-Store/01-FR/" class="cs-journey-step cs-step-lv4">
    <div class="cs-step-marker"><span class="cs-step-num">04</span></div>
    <div class="cs-step-body">
      <div class="cs-step-head">
        <span class="cs-step-tag">Summit</span>
        <span class="cs-step-difficulty">● ● ● ● ○</span>
      </div>
      <h3 class="cs-step-title">Key-Value Store</h3>
      <p class="cs-step-desc">Leaderless replication, LSM trees, gossip protocol, conflict resolution, anti-entropy.</p>
      <div class="cs-step-chips">
        <span class="cs-chip">LSM trees</span>
        <span class="cs-chip">Gossip</span>
        <span class="cs-chip">Quorum</span>
        <span class="cs-chip">Hinted handoff</span>
      </div>
    </div>
    <div class="cs-step-cta">Open <span>→</span></div>
  </a>

  <a href="05-Battleground/01-WhatsApp/" class="cs-journey-step cs-step-lv5">
    <div class="cs-step-marker"><span class="cs-step-num">05</span></div>
    <div class="cs-step-body">
      <div class="cs-step-head">
        <span class="cs-step-tag">Battleground</span>
        <span class="cs-step-difficulty">● ● ● ● ●</span>
      </div>
      <h3 class="cs-step-title">WhatsApp</h3>
      <p class="cs-step-desc">Real-time WebSockets, per-conversation ordering, offline delivery, connection storms, message status.</p>
      <div class="cs-step-chips">
        <span class="cs-chip">WebSockets</span>
        <span class="cs-chip">Kafka</span>
        <span class="cs-chip">Backpressure</span>
        <span class="cs-chip">Hot partitions</span>
      </div>
    </div>
    <div class="cs-step-cta">Open <span>→</span></div>
  </a>

</section>

<section class="cs-footer-note">
  <p>Each case study is a progression: <b>requirements → estimation → base architecture → deep dives → final design → observability</b>. Read top-to-bottom, or jump straight to the deep dive you want.</p>
</section>

</div>
