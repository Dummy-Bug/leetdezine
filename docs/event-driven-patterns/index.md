---
title: Event-Driven Patterns
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
  <div class="cs-level-bg-num">08</div>
  <div class="cs-level-inner">
    <p class="cs-level-eyebrow">Concepts</p>
    <h1 class="cs-level-title">Event-Driven Patterns</h1>
    <p class="cs-level-sub">The patterns that make distributed systems reliable — from the dual-write problem to guaranteed event delivery across service boundaries.</p>
  </div>
</div>
  </div>
</div>

<div class="cs-cards">

  <a class="cs-card" href="what-is-event-sourcing/event-sourcing/">
    <div class="cs-card-title">Event Sourcing</div>
    <div class="cs-card-desc">Store state as a sequence of events instead of a current snapshot. Every state transition becomes auditable and replayable.</div>
    <div class="cs-topics">
      <span>Event Log</span><span>Replay</span><span>Audit Trail</span><span>Snapshots</span>
    </div>
    <div class="cs-card-cta">Open topic <span>→</span></div>
  </a>

  <a class="cs-card" href="cqrs/what-is-cqrs/">
    <div class="cs-card-title">CQRS</div>
    <div class="cs-card-desc">Separate the write model from the read model. Read replicas, projections, and the eventual consistency trade-off this forces.</div>
    <div class="cs-topics">
      <span>Command Model</span><span>Read Models</span><span>Projections</span><span>Consistency</span>
    </div>
    <div class="cs-card-cta">Open topic <span>→</span></div>
  </a>

  <a class="cs-card" href="outbox-pattern/dual-write/">
    <div class="cs-card-title">Outbox Pattern</div>
    <div class="cs-card-desc">The dual-write problem and how the transactional outbox solves it — writing to DB and publishing an event atomically.</div>
    <div class="cs-topics">
      <span>Dual Write</span><span>Transactional Outbox</span><span>Atomicity</span><span>At-Least-Once</span>
    </div>
    <div class="cs-card-cta">Open topic <span>→</span></div>
  </a>

  <a class="cs-card" href="cdc/what-is-cdc/">
    <div class="cs-card-title">CDC</div>
    <div class="cs-card-desc">Change Data Capture — reading the database write-ahead log to stream changes downstream without polling or dual writes.</div>
    <div class="cs-topics">
      <span>WAL Tailing</span><span>Debezium</span><span>Log Mining</span><span>Streaming</span>
    </div>
    <div class="cs-card-cta">Open topic <span>→</span></div>
  </a>

  <a class="cs-card" href="inbox-outbox-together/what-is-inbox-pattern/">
    <div class="cs-card-title">Inbox + Outbox</div>
    <div class="cs-card-desc">Combining inbox and outbox for end-to-end reliable delivery — idempotent consumers, deduplication, and the full event flow.</div>
    <div class="cs-topics">
      <span>Inbox Pattern</span><span>Idempotency</span><span>Deduplication</span><span>Full Flow</span>
    </div>
    <div class="cs-card-cta">Open topic <span>→</span></div>
  </a>

</div>
