---
title: Key-Value Store
description: "How to design a distributed key-value store like DynamoDB or Cassandra. Covers consistent hashing, quorum reads/writes, LSM trees, gossip protocol, and conflict resolution."
hide:
  - navigation
  - toc
---

<div class="cs-level-hero cs-lv4">
  <div class="cs-level-bg-num">04</div>
  <div class="cs-level-inner">
    <p class="cs-level-eyebrow">Summit · Case Study 1</p>
    <h1 class="cs-level-title">Key-Value Store</h1>
    <p class="cs-level-sub">Design a distributed KV store — leaderless replication, quorum reads/writes, LSM tree internals, gossip membership, vector clock conflict resolution.</p>
  </div>
</div>


<div class="cs-concepts-grid cs-concepts-index-grid">

  <a href="01-System-Requirements/01-FR/" class="cs-concept-card cs-concept-c4">
    <div class="cs-concept-card-title">System Requirements</div>
    <div class="cs-concept-card-desc">Problem statement, functional requirements, back-of-envelope estimation, and non-functional requirements.</div>
    <div class="cs-concept-chips">
      <span>FR</span><span>Estimation</span><span>NFR</span>
    </div>
    <div class="cs-concept-cta">Open <span>→</span></div>
  </a>

  <a href="02-API/01-API-Design/" class="cs-concept-card cs-concept-c4">
    <div class="cs-concept-card-title">API Design</div>
    <div class="cs-concept-card-desc">API surface for a KV store — get, put, delete — and the reasoning behind Base64 encoding for keys.</div>
    <div class="cs-concept-chips">
      <span>API Design</span><span>Why Base64</span>
    </div>
    <div class="cs-concept-cta">Open <span>→</span></div>
  </a>

  <a href="03-Base-Architecture/01-Why-Not-Single-Leader/" class="cs-concept-card cs-concept-c4">
    <div class="cs-concept-card-title">Base Architecture</div>
    <div class="cs-concept-card-desc">Why leaderless replication wins for a KV store — single-leader vs multi-leader vs leaderless tradeoffs, and the base design.</div>
    <div class="cs-concept-chips">
      <span>Leaderless</span><span>Replication</span><span>Base Design</span>
    </div>
    <div class="cs-concept-cta">Open <span>→</span></div>
  </a>

  <a href="04-Deep-Dives/" class="cs-concept-card cs-concept-c4">
    <div class="cs-concept-card-title">Deep Dives</div>
    <div class="cs-concept-card-desc">Consistent hashing, quorum writes, hinted handoff, LSM tree internals, compaction strategies, gossip protocol, vector clock conflict resolution, TTL, and fault isolation.</div>
    <div class="cs-concept-chips">
      <span>LSM Trees</span><span>Compaction</span><span>Quorum W/R</span><span>Gossip Protocol</span><span>Vector Clocks</span>
    </div>
    <div class="cs-concept-cta">Open <span>→</span></div>
  </a>

  <a href="05-Observability/01-SLI-SLO-Connection/" class="cs-concept-card cs-concept-c4">
    <div class="cs-concept-card-title">Observability</div>
    <div class="cs-concept-card-desc">SLIs and SLOs for a KV store, latency and availability measurement, alerting strategy, and error budgets.</div>
    <div class="cs-concept-chips">
      <span>SLI / SLO</span><span>Alerting</span><span>Error Budget</span>
    </div>
    <div class="cs-concept-cta">Open <span>→</span></div>
  </a>

  <a href="06-Final-Design/01-Final-Architecture/" class="cs-concept-card cs-concept-c4">
    <div class="cs-concept-card-title">Final Design</div>
    <div class="cs-concept-card-desc">The complete architecture after all deep dives — every component justified, every tradeoff resolved.</div>
    <div class="cs-concept-chips">
      <span>Final Architecture</span><span>Full Diagram</span>
    </div>
    <div class="cs-concept-cta">Open <span>→</span></div>
  </a>

</div>
