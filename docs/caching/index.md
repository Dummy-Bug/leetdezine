---
title: Caching
description: "How caching actually works — write-through vs write-back, eviction policies (LRU, LFU), cache invalidation, distributed caching with Redis, and the failure patterns that kill production systems."
hide:
  - navigation
  - toc
---

<div class="ph-window">
  <div class="ph-window-bar" aria-hidden="true">
    <div class="ph-window-controls">
      <span class="ph-dot ph-dot-red"></span>
      <span class="ph-dot ph-dot-yellow"></span>
      <span class="ph-dot ph-dot-green"></span>
    </div>
    <span class="ph-window-title">leetdezine.com</span>
  </div>
  <div class="ph-window-body">
    <div class="cs-level-hero cs-lv-concepts">
  <div class="cs-level-bg-num">03</div>
  <div class="cs-level-inner">
    <p class="cs-level-eyebrow">Concepts</p>
    <h1 class="cs-level-title">Caching</h1>
    <p class="cs-level-sub">The fastest database query is one that never hits the database. Everything here is about making that work reliably at scale.</p>
  </div>
</div>
  </div>
</div>

<div class="cs-cards">

  <a class="cs-card" href="fundamentals/">
    <div class="cs-card-title">Fundamentals</div>
    <div class="cs-card-desc">What a cache is, where it lives, and the core trade-offs between hit rate, freshness, and memory cost.</div>
    <div class="cs-topics">
      <span>Hit Rate</span><span>Cache Miss</span><span>Freshness</span><span>Memory Cost</span>
    </div>
    <div class="cs-card-cta">Open topic <span>→</span></div>
  </a>

  <a class="cs-card" href="writing-strategies/quick-decision-map/">
    <div class="cs-card-title">Writing Strategies</div>
    <div class="cs-card-desc">Read-through, write-through, write-behind, and write-around — how data gets into the cache and what breaks when it doesn't.</div>
    <div class="cs-topics">
      <span>Write-Through</span><span>Write-Behind</span><span>Read-Through</span><span>Write-Around</span>
    </div>
    <div class="cs-card-cta">Open topic <span>→</span></div>
  </a>

  <a class="cs-card" href="eviction-policies/eviction-vs-ttl/">
    <div class="cs-card-title">Eviction Policies</div>
    <div class="cs-card-desc">LRU, LFU, FIFO, and TTL. What gets evicted when memory fills up and how to pick the right policy for your workload.</div>
    <div class="cs-topics">
      <span>LRU</span><span>LFU</span><span>FIFO</span><span>TTL</span>
    </div>
    <div class="cs-card-cta">Open topic <span>→</span></div>
  </a>

  <a class="cs-card" href="population-strategies/warming-vs-refresh-ahead/">
    <div class="cs-card-title">Population Strategies</div>
    <div class="cs-card-desc">Refresh-ahead and cache warming — how to keep caches populated without a thundering herd on every cold start.</div>
    <div class="cs-topics">
      <span>Refresh-Ahead</span><span>Cache Warming</span><span>Lazy Loading</span><span>Pre-Population</span>
    </div>
    <div class="cs-card-cta">Open topic <span>→</span></div>
  </a>

  <a class="cs-card" href="cache-invalidation/choosing-a-strategy/">
    <div class="cs-card-title">Cache Invalidation</div>
    <div class="cs-card-desc">TTL-based, event-driven, write-through, and versioning strategies. The hardest problem in caching is knowing when to throw data away.</div>
    <div class="cs-topics">
      <span>TTL</span><span>Event-Driven</span><span>Versioning</span><span>Stale-While-Revalidate</span>
    </div>
    <div class="cs-card-cta">Open topic <span>→</span></div>
  </a>

  <a class="cs-card" href="distributed-caching/why-single-node-fails/">
    <div class="cs-card-title">Distributed Caching</div>
    <div class="cs-card-desc">Consistent hashing, cache coherence, replication, two-level caching, and what happens when a cache node dies mid-traffic.</div>
    <div class="cs-topics">
      <span>Consistent Hashing</span><span>Cache Coherence</span><span>Replication</span><span>Node Failure</span>
    </div>
    <div class="cs-card-cta">Open topic <span>→</span></div>
  </a>

  <a class="cs-card" href="cache-problems/diagnosing-which-problem/">
    <div class="cs-card-title">Cache Problems</div>
    <div class="cs-card-desc">Cache stampede, cold start, penetration, and avalanche — the failure modes that turn a cache from a fix into the cause of the outage.</div>
    <div class="cs-topics">
      <span>Stampede</span><span>Cold Start</span><span>Penetration</span><span>Avalanche</span>
    </div>
    <div class="cs-card-cta">Open topic <span>→</span></div>
  </a>

  <a class="cs-card" href="redis/data-structures/">
    <div class="cs-card-title">Redis</div>
    <div class="cs-card-desc">Data structures, patterns, persistence options, streams, and the single-threaded event loop that makes Redis predictably fast.</div>
    <div class="cs-topics">
      <span>Data Structures</span><span>Persistence</span><span>Streams</span><span>Event Loop</span>
    </div>
    <div class="cs-card-cta">Open topic <span>→</span></div>
  </a>

</div>
