---
title: Event Broker
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
  <div class="cs-level-bg-num">07</div>
  <div class="cs-level-inner">
    <p class="cs-level-eyebrow">Concepts</p>
    <h1 class="cs-level-title">Event Broker</h1>
    <p class="cs-level-sub">Kafka from the ground up — why it exists, how it stores data, and the design decisions behind partitions, offsets, and consumer groups.</p>
  </div>
</div>
  </div>
</div>

<div class="cs-cards">

  <a class="cs-card" href="architecture/why-kafka-exists/">
    <div class="cs-card-title">Architecture</div>
    <div class="cs-card-desc">Why Kafka exists, page cache writes, topics, partitions, brokers, replication, ISR, and hot partition problems.</div>
    <div class="cs-topics">
      <span>Topics</span><span>Partitions</span><span>Replication</span><span>ISR</span>
    </div>
    <div class="cs-card-cta">Open topic <span>→</span></div>
  </a>

  <a class="cs-card" href="producer/partitioners/">
    <div class="cs-card-title">Producer</div>
    <div class="cs-card-desc">Partitioner strategies, batching, and compression — how producers balance throughput against ordering guarantees.</div>
    <div class="cs-topics">
      <span>Partitioners</span><span>Batching</span><span>Compression</span><span>Acks</span>
    </div>
    <div class="cs-card-cta">Open topic <span>→</span></div>
  </a>

  <a class="cs-card" href="consumer/pull-model/">
    <div class="cs-card-title">Consumer</div>
    <div class="cs-card-desc">Pull model, offsets, offset storage, consumer groups, and the rebalancing problem when group membership changes.</div>
    <div class="cs-topics">
      <span>Offsets</span><span>Consumer Groups</span><span>Rebalancing</span><span>Lag</span>
    </div>
    <div class="cs-card-cta">Open topic <span>→</span></div>
  </a>

  <a class="cs-card" href="advanced/retention/">
    <div class="cs-card-title">Advanced</div>
    <div class="cs-card-desc">Retention policies and exactly-once processing — the hardest guarantees to get right in a distributed log.</div>
    <div class="cs-topics">
      <span>Retention</span><span>Exactly-Once</span><span>Idempotent Producer</span><span>Transactions</span>
    </div>
    <div class="cs-card-cta">Open topic <span>→</span></div>
  </a>

  <a class="cs-card" href="backpressure/consumer-lag/">
    <div class="cs-card-title">Backpressure</div>
    <div class="cs-card-desc">Consumer lag, scaling consumers, load shedding, and the signals that tell you a consumer is falling behind.</div>
    <div class="cs-topics">
      <span>Consumer Lag</span><span>Scaling</span><span>Load Shedding</span><span>Backpressure Signals</span>
    </div>
    <div class="cs-card-cta">Open topic <span>→</span></div>
  </a>

  <a class="cs-card" href="kafka-vs-sqs-vs-rabbitmq/fundamental-difference/">
    <div class="cs-card-title">Kafka vs SQS vs RabbitMQ</div>
    <div class="cs-card-desc">The fundamental difference between a log and a queue. Retention, routing, ordering, throughput — when to choose what.</div>
    <div class="cs-topics">
      <span>Log vs Queue</span><span>Retention</span><span>Routing</span><span>When To Choose</span>
    </div>
    <div class="cs-card-cta">Open topic <span>→</span></div>
  </a>

</div>
