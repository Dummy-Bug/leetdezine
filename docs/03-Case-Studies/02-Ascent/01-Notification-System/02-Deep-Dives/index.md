---
title: Deep Dives
hide:
  - toc
---

<div class="cs-level-hero cs-lv2">
  <div class="cs-level-bg-num">DD</div>
  <div class="cs-level-inner">
    <p class="cs-level-eyebrow">Notification System · Deep Dives</p>
    <h1 class="cs-level-title">Deep Dives</h1>
    <p class="cs-level-sub">Seven deep dives — database, Kafka fan-out, per-channel workers, scheduled dispatch, retry/DLQ, rate limiting, and fault isolation.</p>
  </div>
</div>

<div class="cs-concepts-grid cs-concepts-index-grid">

  <a href="01-DB/01-DB-Selection/" class="cs-concept-card cs-concept-c4">
    <div class="cs-concept-card-title">Database</div>
    <div class="cs-concept-card-desc">DB selection for notification storage and schema design for high write throughput.</div>
    <div class="cs-concept-chips">
      <span>Cassandra</span><span>Schema</span><span>Write Throughput</span>
    </div>
    <div class="cs-concept-cta">Open <span>→</span></div>
  </a>

  <a href="02-Kafka/01-Queue-Selection/" class="cs-concept-card cs-concept-c4">
    <div class="cs-concept-card-title">Kafka</div>
    <div class="cs-concept-card-desc">Queue selection rationale and Kafka fan-out design for multi-channel delivery.</div>
    <div class="cs-concept-chips">
      <span>Kafka</span><span>Fan-out</span><span>Queue Selection</span>
    </div>
    <div class="cs-concept-cta">Open <span>→</span></div>
  </a>

  <a href="03-Per-Channel-Workers/01-Push-Worker/" class="cs-concept-card cs-concept-c4">
    <div class="cs-concept-card-title">Per-Channel Workers</div>
    <div class="cs-concept-card-desc">Push, SMS, and email worker architecture — isolation, third-party adapters, and failure containment.</div>
    <div class="cs-concept-chips">
      <span>Push</span><span>SMS</span><span>Email</span><span>Worker Isolation</span>
    </div>
    <div class="cs-concept-cta">Open <span>→</span></div>
  </a>

  <a href="04-Scheduling/01-Problem-And-Naive-Approach/" class="cs-concept-card cs-concept-c4">
    <div class="cs-concept-card-title">Scheduling</div>
    <div class="cs-concept-card-desc">Scheduled notifications, naive approaches, scheduler DB design, jitter, and dispatch flow.</div>
    <div class="cs-concept-chips">
      <span>Scheduler DB</span><span>Jitter</span><span>Dispatch Flow</span>
    </div>
    <div class="cs-concept-cta">Open <span>→</span></div>
  </a>

  <a href="05-Retry-And-DLQ/01-Retry-Strategy/" class="cs-concept-card cs-concept-c4">
    <div class="cs-concept-card-title">Retry & DLQ</div>
    <div class="cs-concept-card-desc">Retry strategy with exponential backoff, dead letter queue design, and failure handling.</div>
    <div class="cs-concept-chips">
      <span>Retry</span><span>DLQ</span><span>Backoff</span><span>Failure Handling</span>
    </div>
    <div class="cs-concept-cta">Open <span>→</span></div>
  </a>

  <a href="06-Rate-Limiting/01-Rate-Limiting/" class="cs-concept-card cs-concept-c4">
    <div class="cs-concept-card-title">Rate Limiting</div>
    <div class="cs-concept-card-desc">Per-provider rate limiting to avoid throttling APNs, FCM, and SMS gateways.</div>
    <div class="cs-concept-chips">
      <span>APNs</span><span>FCM</span><span>Provider Throttle</span>
    </div>
    <div class="cs-concept-cta">Open <span>→</span></div>
  </a>

  <a href="07-Fault-Isolation/01-APNs-Down/" class="cs-concept-card cs-concept-c4">
    <div class="cs-concept-card-title">Fault Isolation</div>
    <div class="cs-concept-card-desc">APNs down, Cassandra down, Kafka down, Redis down, and Scheduler down — each failure isolated.</div>
    <div class="cs-concept-chips">
      <span>APNs Down</span><span>Kafka Down</span><span>Cassandra Down</span><span>Circuit Breaker</span>
    </div>
    <div class="cs-concept-cta">Open <span>→</span></div>
  </a>

</div>
