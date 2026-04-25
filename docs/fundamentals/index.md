---
title: Core Concepts
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
  <div class="cs-level-bg-num">02</div>
  <div class="cs-level-inner">
    <p class="cs-level-eyebrow">Concepts</p>
    <h1 class="cs-level-title">Core Concepts</h1>
    <p class="cs-level-sub">The vocabulary of distributed systems. Every architecture decision traces back to one of these.</p>
  </div>
</div>
  </div>
</div>

<div class="cs-cards">

  <a class="cs-card" href="../performance-metrics/overview/">
    <div class="cs-card-title">Performance Metrics</div>
    <div class="cs-card-desc">Latency, throughput, bandwidth, and percentiles — the four measurements that appear in every design discussion.</div>
    <div class="cs-topics">
      <span>Latency</span><span>Throughput</span><span>Bandwidth</span><span>P99</span>
    </div>
    <div class="cs-card-cta">Open topic <span>→</span></div>
  </a>

  <a class="cs-card" href="../service-levels/overview/">
    <div class="cs-card-title">Service Levels</div>
    <div class="cs-card-desc">SLIs, SLOs, SLAs, and error budgets. How you define and commit to system behavior — and what happens when you breach it.</div>
    <div class="cs-topics">
      <span>SLI</span><span>SLO</span><span>SLA</span><span>Error Budget</span>
    </div>
    <div class="cs-card-cta">Open topic <span>→</span></div>
  </a>

  <a class="cs-card" href="../availability/overview/">
    <div class="cs-card-title">Availability</div>
    <div class="cs-card-desc">SPOF, redundancy, nines, active-active vs active-passive. What "highly available" actually requires you to build.</div>
    <div class="cs-topics">
      <span>SPOF</span><span>Redundancy</span><span>Nines</span><span>Active-Active</span>
    </div>
    <div class="cs-card-cta">Open topic <span>→</span></div>
  </a>

  <a class="cs-card" href="../reliability/overview/">
    <div class="cs-card-title">Reliability</div>
    <div class="cs-card-desc">MTBF, MTTR, RTO, RPO. The difference between a system that rarely fails and one that recovers fast when it does.</div>
    <div class="cs-topics">
      <span>MTBF</span><span>MTTR</span><span>RTO</span><span>RPO</span>
    </div>
    <div class="cs-card-cta">Open topic <span>→</span></div>
  </a>

  <a class="cs-card" href="../scalability/overview/">
    <div class="cs-card-title">Scalability</div>
    <div class="cs-card-desc">Horizontal vs vertical scaling, load balancing at L4 and L7, auto-scaling, and connection draining. How systems grow without breaking.</div>
    <div class="cs-topics">
      <span>Load Balancing</span><span>L4 / L7</span><span>Auto-Scaling</span><span>Cold Start</span>
    </div>
    <div class="cs-card-cta">Open topic <span>→</span></div>
  </a>

  <a class="cs-card" href="../fault-tolerance/overview/">
    <div class="cs-card-title">Fault Tolerance</div>
    <div class="cs-card-desc">Graceful degradation, bulkheads, circuit breakers, retries with backoff. How systems survive partial failure without cascading.</div>
    <div class="cs-topics">
      <span>Circuit Breaker</span><span>Bulkhead</span><span>Retry</span><span>Backoff</span>
    </div>
    <div class="cs-card-cta">Open topic <span>→</span></div>
  </a>

  <a class="cs-card" href="../durability/overview/">
    <div class="cs-card-title">Durability</div>
    <div class="cs-card-desc">WAL, replication, and backups. The mechanisms that ensure data survives node failure, crash, or disaster.</div>
    <div class="cs-topics">
      <span>WAL</span><span>Replication</span><span>Backups</span><span>Crash Recovery</span>
    </div>
    <div class="cs-card-cta">Open topic <span>→</span></div>
  </a>

  <a class="cs-card" href="../concurrency-locking/overview/">
    <div class="cs-card-title">Concurrency & Locking</div>
    <div class="cs-card-desc">Race conditions, pessimistic and optimistic locking, MVCC, and distributed locks. How systems handle parallel writes without corruption.</div>
    <div class="cs-topics">
      <span>Optimistic Locking</span><span>MVCC</span><span>Distributed Lock</span><span>Idempotency</span>
    </div>
    <div class="cs-card-cta">Open topic <span>→</span></div>
  </a>

  <a class="cs-card" href="../security/overview/">
    <div class="cs-card-title">Security</div>
    <div class="cs-card-desc">Auth, JWT, encryption at rest and in transit. The security primitives that belong in every system design, not just the ones marked "sensitive."</div>
    <div class="cs-topics">
      <span>JWT</span><span>OAuth</span><span>Encryption</span><span>TLS</span>
    </div>
    <div class="cs-card-cta">Open topic <span>→</span></div>
  </a>

  <a class="cs-card" href="../state-machines/overview/">
    <div class="cs-card-title">State Machines</div>
    <div class="cs-card-desc">Modeling order flows, workflows, and status transitions as explicit states. The pattern that makes async systems auditable and debuggable.</div>
    <div class="cs-topics">
      <span>State Transitions</span><span>DB Implementation</span><span>Audit Trail</span><span>Timeout Events</span>
    </div>
    <div class="cs-card-cta">Open topic <span>→</span></div>
  </a>

  <a class="cs-card" href="../nfrs/overview/">
    <div class="cs-card-title">NFRs</div>
    <div class="cs-card-desc">Non-functional requirements: the hidden constraints that shape every architecture decision before you draw a single box.</div>
    <div class="cs-topics">
      <span>Scalability NFRs</span><span>Availability NFRs</span><span>Conflicting NFRs</span><span>Design Decisions</span>
    </div>
    <div class="cs-card-cta">Open topic <span>→</span></div>
  </a>

</div>
