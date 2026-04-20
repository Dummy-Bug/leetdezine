---
title: WhatsApp
hide:
  - navigation
  - toc
---

<div class="cs-level-hero cs-lv5">
  <div class="cs-level-bg-num">01</div>
  <div class="cs-level-inner">
    <p class="cs-level-eyebrow">Battleground · Case Study 1</p>
    <h1 class="cs-level-title">WhatsApp</h1>
    <p class="cs-level-sub">Design a real-time messaging system at 500M DAU — persistent WebSocket connections, guaranteed delivery, offline queuing, message ordering, read receipts, and inbox at scale.</p>
  </div>
</div>


<div class="cs-concepts-grid cs-concepts-index-grid">

  <a href="01-System-Requirements/01-FR/" class="cs-concept-card cs-concept-c4">
    <div class="cs-concept-card-title">System Requirements</div>
    <div class="cs-concept-card-desc">Functional requirements, back-of-envelope estimation, NFRs, and API design.</div>
    <div class="cs-concept-chips">
      <span>FR</span><span>Estimation</span><span>NFR</span><span>API</span>
    </div>
    <div class="cs-concept-cta">Open <span>→</span></div>
  </a>

  <a href="02-Real-Time-Comms/01-The-Problem/" class="cs-concept-card cs-concept-c4">
    <div class="cs-concept-card-title">Real-Time Comms</div>
    <div class="cs-concept-card-desc">Why HTTP polling fails, WebSocket mechanics, connection lifecycle, and the connection server model.</div>
    <div class="cs-concept-chips">
      <span>WebSocket</span><span>Long Polling</span><span>Connection Server</span>
    </div>
    <div class="cs-concept-cta">Open <span>→</span></div>
  </a>

  <a href="03-Base-Architecture/01-Overview/" class="cs-concept-card cs-concept-c4">
    <div class="cs-concept-card-title">Base Architecture</div>
    <div class="cs-concept-card-desc">High-level system diagram — connection servers, message router, storage layer, and notification path.</div>
    <div class="cs-concept-chips">
      <span>Architecture</span><span>Message Router</span><span>Storage</span>
    </div>
    <div class="cs-concept-cta">Open <span>→</span></div>
  </a>

  <a href="04-Deep-Dives/" class="cs-concept-card cs-concept-c4">
    <div class="cs-concept-card-title">Deep Dives</div>
    <div class="cs-concept-card-desc">Database, message ordering, offline delivery, message status, inbox, caching, peak traffic, and fault isolation.</div>
    <div class="cs-concept-chips">
      <span>DynamoDB</span><span>Ordering</span><span>Offline Queue</span><span>Three Ticks</span>
    </div>
    <div class="cs-concept-cta">Open <span>→</span></div>
  </a>

  <a href="05-Observability/01-SLI-SLO-Connection/" class="cs-concept-card cs-concept-c4">
    <div class="cs-concept-card-title">Observability</div>
    <div class="cs-concept-card-desc">SLIs and SLOs for a messaging system, latency measurement, availability tracking, alerting, and error budgets.</div>
    <div class="cs-concept-chips">
      <span>SLI / SLO</span><span>Alerting</span><span>Error Budget</span>
    </div>
    <div class="cs-concept-cta">Open <span>→</span></div>
  </a>

  <a href="06-Final-Design/01-Final-Architecture/" class="cs-concept-card cs-concept-c4">
    <div class="cs-concept-card-title">Final Design</div>
    <div class="cs-concept-card-desc">The complete architecture after all deep dives — every component justified, every tradeoff resolved, full system diagram.</div>
    <div class="cs-concept-chips">
      <span>Final Diagram</span><span>Full Architecture</span>
    </div>
    <div class="cs-concept-cta">Open <span>→</span></div>
  </a>

</div>
