---
title: Pastebin
description: "How to design a Pastebin-like system at scale. Covers content-addressable storage, short code generation, expiration, and read-heavy caching strategies."
hide:
  - navigation
  - toc
---

<div class="cs-level-hero cs-lv2">
  <div class="cs-level-bg-num">02</div>
  <div class="cs-level-inner">
    <p class="cs-level-eyebrow">Ascent · Case Study 2</p>
    <h1 class="cs-level-title">Pastebin</h1>
    <p class="cs-level-sub">Design pastebin.com — paste text, get a short link, retrieve content at scale. 10M DAU, expiring pastes, large content blobs.</p>
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
    <div class="cs-concept-card-desc">Short code generation, database, caching, peak traffic, fault isolation, async S3 upload, expiry cleanup, and final architecture.</div>
    <div class="cs-concept-chips">
      <span>Short Code Gen</span><span>CAS</span><span>Caching</span><span>Async S3</span><span>TTL Cleanup</span>
    </div>
    <div class="cs-concept-cta">Open <span>→</span></div>
  </a>

  <a href="sli-slo-connection/" class="cs-concept-card cs-concept-c4">
    <div class="cs-concept-card-title">Observability</div>
    <div class="cs-concept-card-desc">SLIs and SLOs for a paste service, latency measurement, availability tracking, alerting, and error budgets.</div>
    <div class="cs-concept-chips">
      <span>SLI / SLO</span><span>Alerting</span><span>Error Budget</span>
    </div>
    <div class="cs-concept-cta">Open <span>→</span></div>
  </a>

</div>
