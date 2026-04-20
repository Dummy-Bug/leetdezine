---
title: Caching
hide:
  - navigation
  - toc
---

<div class="cs-level-hero cs-lv-concepts">
  <div class="cs-level-bg-num">03</div>
  <div class="cs-level-inner">
    <p class="cs-level-eyebrow">Concepts</p>
    <h1 class="cs-level-title">Caching</h1>
    <p class="cs-level-sub">How systems remember expensive answers. Every caching decision is a tradeoff between freshness, memory, and complexity.</p>
  </div>
</div>

<div class="cs-cards">

  <a class="cs-card" href="01-Fundamentals/">
    <div class="cs-card-title">Fundamentals</div>
    <div class="cs-card-desc">What a cache is, why it exists, and where it sits in a system. The mental model before you touch any strategy.</div>
    <div class="cs-topics">
      <span>Cache Hit</span><span>Cache Miss</span><span>Hit Rate</span><span>Cache Aside</span>
    </div>
    <div class="cs-card-cta">Open topic <span>→</span></div>
  </a>

  <a class="cs-card" href="02-Writing-Strategies/00-Overview/">
    <div class="cs-card-title">Writing Strategies</div>
    <div class="cs-card-desc">Read-through, write-through, write-back, write-around. When data changes, these strategies decide which copy gets updated first.</div>
    <div class="cs-topics">
      <span>Write-Through</span><span>Write-Back</span><span>Read-Through</span><span>Write-Around</span>
    </div>
    <div class="cs-card-cta">Open topic <span>→</span></div>
  </a>

  <a class="cs-card" href="03-Eviction-Policies/00-Overview/">
    <div class="cs-card-title">Eviction Policies</div>
    <div class="cs-card-desc">LRU, LFU, FIFO, TTL. When the cache is full, eviction policy decides what gets thrown out — and getting it wrong is a performance cliff.</div>
    <div class="cs-topics">
      <span>LRU</span><span>LFU</span><span>FIFO</span><span>TTL</span>
    </div>
    <div class="cs-card-cta">Open topic <span>→</span></div>
  </a>

  <a class="cs-card" href="04-Population-Strategies/00-Overview/">
    <div class="cs-card-title">Population Strategies</div>
    <div class="cs-card-desc">Refresh-ahead and cache warming. How you pre-fill a cache so users never hit a cold miss on a hot path.</div>
    <div class="cs-topics">
      <span>Refresh-Ahead</span><span>Cache Warming</span><span>Lazy Loading</span><span>Pre-Population</span>
    </div>
    <div class="cs-card-cta">Open topic <span>→</span></div>
  </a>

  <a class="cs-card" href="05-Cache-Invalidation/00-Overview/">
    <div class="cs-card-title">Cache Invalidation</div>
    <div class="cs-card-desc">TTL, event-driven, write-through, versioning, stale-while-revalidate. The hardest problem in caching — keeping the cache honest without killing performance.</div>
    <div class="cs-topics">
      <span>TTL</span><span>Event-Driven</span><span>Versioning</span><span>Stale-While-Revalidate</span>
    </div>
    <div class="cs-card-cta">Open topic <span>→</span></div>
  </a>

  <a class="cs-card" href="06-Distributed-Caching/00-Overview/">
    <div class="cs-card-title">Distributed Caching</div>
    <div class="cs-card-desc">Why a single cache node fails at scale. Consistent hashing, cache coherence, replication, two-level caching, and node failure handling.</div>
    <div class="cs-topics">
      <span>Consistent Hashing</span><span>Cache Coherence</span><span>Replication</span><span>Two-Level Cache</span>
    </div>
    <div class="cs-card-cta">Open topic <span>→</span></div>
  </a>

  <a class="cs-card" href="07-Cache-Problems/00-Overview/">
    <div class="cs-card-title">Cache Problems</div>
    <div class="cs-card-desc">Stampede, cold start, penetration, avalanche. The failure modes that hit hardest when traffic spikes or the cache restarts.</div>
    <div class="cs-topics">
      <span>Cache Stampede</span><span>Cold Start</span><span>Penetration</span><span>Avalanche</span>
    </div>
    <div class="cs-card-cta">Open topic <span>→</span></div>
  </a>

  <a class="cs-card" href="08-Redis/01-Data-Structures/">
    <div class="cs-card-title">Redis</div>
    <div class="cs-card-desc">Data structures, patterns, persistence, streams, and the single-threaded event loop. Redis internals that explain why it's fast and where it breaks.</div>
    <div class="cs-topics">
      <span>Data Structures</span><span>Persistence</span><span>Streams</span><span>Event Loop</span>
    </div>
    <div class="cs-card-cta">Open topic <span>→</span></div>
  </a>

</div>
