---
title: URL Shortener
description: "How to design a scalable URL shortener like bit.ly. Covers 100M DAU estimation, Base62 encoding, KGS architecture, hot key problem, and Redis caching strategy."
hide:
  - navigation
  - toc
---

<div class="cs-level-hero cs-lv1">
  <div class="cs-level-bg-num">02</div>
  <div class="cs-level-inner">
    <p class="cs-level-eyebrow">Foundation · Case Study 2</p>
    <h1 class="cs-level-title">URL Shortener</h1>
    <p class="cs-level-sub">Design bit.ly — takes a long URL, returns a short code, redirects at scale. 100M DAU, 1B redirects/day.</p>
  </div>
</div>


<div class="cs-concepts-grid cs-concepts-index-grid">

  <a href="functional-requirements/" class="cs-concept-card cs-concept-c4">
    <div class="cs-concept-card-title">System Requirements</div>
    <div class="cs-concept-card-desc">Functional requirements, back-of-envelope estimation, NFRs, API design, and base architecture.</div>
    <div class="cs-concept-chips">
      <span>FR</span><span>Estimation</span><span>NFR</span><span>API</span><span>Base Architecture</span>
    </div>
    <div class="cs-concept-cta">Open <span>→</span></div>
  </a>

  <a href="deep-dives/" class="cs-concept-card cs-concept-c4">
    <div class="cs-concept-card-title">Deep Dives</div>
    <div class="cs-concept-card-desc">Short code generation, database sharding, caching strategy, peak traffic handling, pre-generated keys, cold storage, and fault isolation.</div>
    <div class="cs-concept-chips">
      <span>Short Code Gen</span><span>Sharding</span><span>Caching</span><span>Pre-Gen Keys</span><span>Cold Storage</span>
    </div>
    <div class="cs-concept-cta">Open <span>→</span></div>
  </a>

  <a href="sli-slo-connection/" class="cs-concept-card cs-concept-c4">
    <div class="cs-concept-card-title">Observability</div>
    <div class="cs-concept-card-desc">SLIs and SLOs for a redirect service, latency P99 measurement, availability tracking, alerting, and error budgets.</div>
    <div class="cs-concept-chips">
      <span>SLI / SLO</span><span>Alerting</span><span>Error Budget</span>
    </div>
    <div class="cs-concept-cta">Open <span>→</span></div>
  </a>

  <a href="architecture/" class="cs-concept-card cs-concept-c4">
    <div class="cs-concept-card-title">Final Design</div>
    <div class="cs-concept-card-desc">The complete architecture after all deep dives — every component justified, every tradeoff resolved, full system diagram.</div>
    <div class="cs-concept-chips">
      <span>Final Architecture</span><span>Full Diagram</span>
    </div>
    <div class="cs-concept-cta">Open <span>→</span></div>
  </a>

</div>
