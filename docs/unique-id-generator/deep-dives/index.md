---
title: Deep Dives
hide:
  - navigation
  - toc
---

<div class="cs-level-hero cs-lv1">
  <div class="cs-level-bg-num">DD</div>
  <div class="cs-level-inner">
    <p class="cs-level-eyebrow">Unique ID Generator · Deep Dives</p>
    <h1 class="cs-level-title">Deep Dives</h1>
    <p class="cs-level-sub">Nine deep dives — single-server counter, multi-server problem, UUID, ticket server, pre-generated key pool, Snowflake, algorithm comparison, clock skew, and fault isolation.</p>
  </div>
</div>

<div class="cs-concepts-grid cs-concepts-index-grid">

  <a href="../single-server-counter/" class="cs-concept-card cs-concept-c4">
    <div class="cs-concept-card-title">Single Server Counter</div>
    <div class="cs-concept-card-desc">The simplest approach — auto-increment on a single DB. Works until it doesn't.</div>
    <div class="cs-concept-chips">
      <span>Auto-Increment</span><span>Single DB</span>
    </div>
    <div class="cs-concept-cta">Open <span>→</span></div>
  </a>

  <a href="../multi-server-problem/" class="cs-concept-card cs-concept-c4">
    <div class="cs-concept-card-title">Multi-Server Problem</div>
    <div class="cs-concept-card-desc">Why a single counter breaks at scale and what the distributed ID problem actually is.</div>
    <div class="cs-concept-chips">
      <span>Distributed</span><span>Uniqueness</span><span>Coordination</span>
    </div>
    <div class="cs-concept-cta">Open <span>→</span></div>
  </a>

  <a href="../uuid/" class="cs-concept-card cs-concept-c4">
    <div class="cs-concept-card-title">UUID</div>
    <div class="cs-concept-card-desc">128-bit random IDs — no coordination needed, but no ordering either.</div>
    <div class="cs-concept-chips">
      <span>UUID</span><span>128-bit</span><span>No Ordering</span>
    </div>
    <div class="cs-concept-cta">Open <span>→</span></div>
  </a>

  <a href="../ticket-server/" class="cs-concept-card cs-concept-c4">
    <div class="cs-concept-card-title">Ticket Server</div>
    <div class="cs-concept-card-desc">Centralised counter server — ordered IDs, but a single point of failure.</div>
    <div class="cs-concept-chips">
      <span>Ticket Server</span><span>Central Counter</span><span>SPOF</span>
    </div>
    <div class="cs-concept-cta">Open <span>→</span></div>
  </a>

  <a href="../pre-generated-key-pool/" class="cs-concept-card cs-concept-c4">
    <div class="cs-concept-card-title">Pre-Generated Key Pool</div>
    <div class="cs-concept-card-desc">Pre-generate IDs in bulk and hand them out — trades coordination for latency.</div>
    <div class="cs-concept-chips">
      <span>Key Pool</span><span>Pre-Generation</span><span>Bulk Allocation</span>
    </div>
    <div class="cs-concept-cta">Open <span>→</span></div>
  </a>

  <a href="../snowflake/" class="cs-concept-card cs-concept-c4">
    <div class="cs-concept-card-title">Snowflake</div>
    <div class="cs-concept-card-desc">Twitter's 64-bit ID — timestamp + datacenter + worker + sequence. Sorted, distributed, fast.</div>
    <div class="cs-concept-chips">
      <span>Snowflake</span><span>64-bit</span><span>Timestamp</span><span>Sortable</span>
    </div>
    <div class="cs-concept-cta">Open <span>→</span></div>
  </a>

  <a href="../comparison/" class="cs-concept-card cs-concept-c4">
    <div class="cs-concept-card-title">Comparison</div>
    <div class="cs-concept-card-desc">All five approaches side-by-side — uniqueness, ordering, coordination, scalability, and tradeoffs.</div>
    <div class="cs-concept-chips">
      <span>Tradeoffs</span><span>Comparison</span>
    </div>
    <div class="cs-concept-cta">Open <span>→</span></div>
  </a>

  <a href="../clock-skew/" class="cs-concept-card cs-concept-c4">
    <div class="cs-concept-card-title">Clock Skew</div>
    <div class="cs-concept-card-desc">Why wall-clock timestamps break distributed ordering and how NTP drift causes duplicate IDs.</div>
    <div class="cs-concept-chips">
      <span>Clock Skew</span><span>NTP</span><span>Monotonic Clock</span>
    </div>
    <div class="cs-concept-cta">Open <span>→</span></div>
  </a>

  <a href="../fault-isolation/" class="cs-concept-card cs-concept-c4">
    <div class="cs-concept-card-title">Fault Isolation</div>
    <div class="cs-concept-card-desc">Worker node failure, clock going backward, and sequence exhaustion — each isolated and handled.</div>
    <div class="cs-concept-chips">
      <span>Node Failure</span><span>Clock Backward</span><span>Sequence Exhaustion</span>
    </div>
    <div class="cs-concept-cta">Open <span>→</span></div>
  </a>

</div>
