---
title: Deep Dives
hide:
  - navigation
  - toc
---

<div class="cs-level-hero cs-lv3">
  <div class="cs-level-bg-num">DD</div>
  <div class="cs-level-inner">
    <p class="cs-level-eyebrow">Rate Limiter · Deep Dives</p>
    <h1 class="cs-level-title">Deep Dives</h1>
    <p class="cs-level-sub">Four deep dives — algorithms from scratch, distributed enforcement, rule storage, and fault isolation including DDoS layered defence.</p>
  </div>
</div>

<div class="cs-concepts-grid cs-concepts-index-grid">

  <a href="01-Algorithms/01-Fixed-Window-Counter/" class="cs-concept-card cs-concept-c4">
    <div class="cs-concept-card-title">Algorithms</div>
    <div class="cs-concept-card-desc">Fixed window, sliding window log/counter, token bucket, leaky bucket — built from scratch and compared.</div>
    <div class="cs-concept-chips">
      <span>Token Bucket</span><span>Leaky Bucket</span><span>Sliding Window</span><span>Fixed Window</span>
    </div>
    <div class="cs-concept-cta">Open <span>→</span></div>
  </a>

  <a href="02-Distributed-Rate-Limiting/01-Atomicity-Problem/" class="cs-concept-card cs-concept-c4">
    <div class="cs-concept-card-title">Distributed Rate Limiting</div>
    <div class="cs-concept-card-desc">Atomicity problem with naïve counters, Lua scripts for atomicity, and Redis cluster enforcement.</div>
    <div class="cs-concept-chips">
      <span>Lua Atomicity</span><span>Redis Cluster</span><span>Race Condition</span>
    </div>
    <div class="cs-concept-cta">Open <span>→</span></div>
  </a>

  <a href="03-Rule-Storage/01-Rule-Storage/" class="cs-concept-card cs-concept-c4">
    <div class="cs-concept-card-title">Rule Storage</div>
    <div class="cs-concept-card-desc">How rate limiting rules are stored, loaded into workers, and refreshed without restart.</div>
    <div class="cs-concept-chips">
      <span>Rule DB</span><span>Config Refresh</span><span>Worker Cache</span>
    </div>
    <div class="cs-concept-cta">Open <span>→</span></div>
  </a>

  <a href="04-Fault-Isolation/01-Rate-Limiter-Node-Down/" class="cs-concept-card cs-concept-c4">
    <div class="cs-concept-card-title">Fault Isolation</div>
    <div class="cs-concept-card-desc">Rate limiter down, Redis down, Rule DB down, API gateway down, and DDoS layered defence.</div>
    <div class="cs-concept-chips">
      <span>Redis Down</span><span>Fail Open</span><span>DDoS Defence</span><span>API GW</span>
    </div>
    <div class="cs-concept-cta">Open <span>→</span></div>
  </a>

</div>
