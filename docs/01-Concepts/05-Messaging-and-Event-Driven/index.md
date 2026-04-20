---
title: Messaging & Event Driven
hide:
  - navigation
  - toc
---

<div class="cs-level-hero cs-lv-concepts">
  <div class="cs-level-bg-num">05</div>
  <div class="cs-level-inner">
    <p class="cs-level-eyebrow">Concepts</p>
    <h1 class="cs-level-title">Messaging & Event Driven</h1>
    <p class="cs-level-sub">How systems talk to each other without blocking. Queues, brokers, streams, and the patterns that make async pipelines reliable.</p>
  </div>
</div>

<div class="cs-cards">

  <a class="cs-card" href="01-Message-Queues/">
    <div class="cs-card-title">Message Queues</div>
    <div class="cs-card-desc">Why queues exist, what problem they solve, and the core model: producer puts work in, consumer takes it out, durably.</div>
    <div class="cs-topics">
      <span>Producer</span><span>Consumer</span><span>Durability</span><span>Async Processing</span>
    </div>
    <div class="cs-card-cta">Open topic <span>→</span></div>
  </a>

  <a class="cs-card" href="02-Task-Queue/">
    <div class="cs-card-title">Task Queue</div>
    <div class="cs-card-desc">Background job execution — offloading CPU-heavy or slow work from the request path into a worker pool that processes at its own pace.</div>
    <div class="cs-topics">
      <span>Background Jobs</span><span>Worker Pool</span><span>Job Scheduling</span><span>Celery</span>
    </div>
    <div class="cs-card-cta">Open topic <span>→</span></div>
  </a>

  <a class="cs-card" href="03-Pub-Sub/">
    <div class="cs-card-title">Pub / Sub</div>
    <div class="cs-card-desc">One publisher, many subscribers. The model that decouples event producers from consumers and enables fan-out without direct coupling.</div>
    <div class="cs-topics">
      <span>Publisher</span><span>Subscriber</span><span>Topic</span><span>Fan-Out</span>
    </div>
    <div class="cs-card-cta">Open topic <span>→</span></div>
  </a>

  <a class="cs-card" href="04-Delivery-Guarantees/">
    <div class="cs-card-title">Delivery Guarantees</div>
    <div class="cs-card-desc">At-most-once, at-least-once, exactly-once. What each guarantee costs and which systems actually deliver exactly-once end-to-end.</div>
    <div class="cs-topics">
      <span>At-Most-Once</span><span>At-Least-Once</span><span>Exactly-Once</span><span>Idempotency</span>
    </div>
    <div class="cs-card-cta">Open topic <span>→</span></div>
  </a>

  <a class="cs-card" href="05-Dead-Letter-Queue/">
    <div class="cs-card-title">Dead Letter Queue</div>
    <div class="cs-card-desc">What happens to messages that can't be processed. DLQs prevent poison pills from blocking a queue and give you a recovery path for failed messages.</div>
    <div class="cs-topics">
      <span>DLQ</span><span>Poison Pill</span><span>Retry Limit</span><span>Message Recovery</span>
    </div>
    <div class="cs-card-cta">Open topic <span>→</span></div>
  </a>

  <a class="cs-card" href="06-Message-Ordering/">
    <div class="cs-card-title">Message Ordering</div>
    <div class="cs-card-desc">Why ordering is hard in distributed queues, when it matters, and the tradeoff between strict ordering and throughput.</div>
    <div class="cs-topics">
      <span>FIFO</span><span>Partition Key</span><span>Ordering Guarantees</span><span>Throughput Tradeoff</span>
    </div>
    <div class="cs-card-cta">Open topic <span>→</span></div>
  </a>

  <a class="cs-card" href="07-Delay-Queues/">
    <div class="cs-card-title">Delay Queues</div>
    <div class="cs-card-desc">Scheduling messages to be visible after a delay. The pattern behind retry backoff, scheduled jobs, and time-based workflows.</div>
    <div class="cs-topics">
      <span>Visibility Timeout</span><span>Scheduled Messages</span><span>Retry Backoff</span><span>SQS Delay</span>
    </div>
    <div class="cs-card-cta">Open topic <span>→</span></div>
  </a>

  <a class="cs-card" href="08-Priority-Queues/">
    <div class="cs-card-title">Priority Queues</div>
    <div class="cs-card-desc">Processing high-priority messages before low-priority ones. The implementation patterns and the starvation problem that comes with them.</div>
    <div class="cs-topics">
      <span>Priority Levels</span><span>Starvation</span><span>Multi-Queue</span><span>Heap-Based</span>
    </div>
    <div class="cs-card-cta">Open topic <span>→</span></div>
  </a>

  <a class="cs-card" href="09-Fan-Out-on-Write/">
    <div class="cs-card-title">Fan-Out on Write</div>
    <div class="cs-card-desc">Push updates to all followers at write time. Fast reads, expensive writes — the pattern Twitter uses for most users.</div>
    <div class="cs-topics">
      <span>Write Amplification</span><span>Push Model</span><span>Inbox Pattern</span><span>Celebrity Problem</span>
    </div>
    <div class="cs-card-cta">Open topic <span>→</span></div>
  </a>

  <a class="cs-card" href="10-Fan-Out-on-Read/">
    <div class="cs-card-title">Fan-Out on Read</div>
    <div class="cs-card-desc">Aggregate the feed at read time instead of write time. Cheaper writes, more expensive reads — used for celebrity accounts where fan-out on write breaks.</div>
    <div class="cs-topics">
      <span>Pull Model</span><span>Read Aggregation</span><span>Hybrid Fan-Out</span><span>Hot Users</span>
    </div>
    <div class="cs-card-cta">Open topic <span>→</span></div>
  </a>

  <a class="cs-card" href="11-Message-Brokers/01-What-is-a-Broker/">
    <div class="cs-card-title">Message Brokers</div>
    <div class="cs-card-desc">SQS and RabbitMQ in depth — architecture, delivery guarantees, routing, ACK/NACK, DLQ, scaling, and when to use each.</div>
    <div class="cs-topics">
      <span>SQS</span><span>RabbitMQ</span><span>ACK / NACK</span><span>Exchange Types</span>
    </div>
    <div class="cs-card-cta">Open topic <span>→</span></div>
  </a>

  <a class="cs-card" href="12-Kafka/01-Architecture/01-Why-Kafka-Exists/">
    <div class="cs-card-title">Kafka</div>
    <div class="cs-card-desc">Architecture, producers, consumers, partitions, ISR, offsets, consumer groups, rebalancing, retention, and exactly-once processing.</div>
    <div class="cs-topics">
      <span>Partitions</span><span>Consumer Groups</span><span>Offsets</span><span>ISR</span>
    </div>
    <div class="cs-card-cta">Open topic <span>→</span></div>
  </a>

  <a class="cs-card" href="13-Comparison/01-Fundamental-Difference/">
    <div class="cs-card-title">Broker Comparison</div>
    <div class="cs-card-desc">Kafka vs SQS vs RabbitMQ — what fundamentally differs, when to choose what, and the tradeoffs around retention, ordering, and throughput.</div>
    <div class="cs-topics">
      <span>Kafka vs SQS</span><span>Retention</span><span>Ordering</span><span>Throughput</span>
    </div>
    <div class="cs-card-cta">Open topic <span>→</span></div>
  </a>

  <a class="cs-card" href="14-Backpressure/01-Consumer-Lag/">
    <div class="cs-card-title">Backpressure</div>
    <div class="cs-card-desc">Consumer lag, scaling consumers, load shedding, and backpressure signals. What to do when your consumers can't keep up with your producers.</div>
    <div class="cs-topics">
      <span>Consumer Lag</span><span>Load Shedding</span><span>Scaling</span><span>Backpressure Signals</span>
    </div>
    <div class="cs-card-cta">Open topic <span>→</span></div>
  </a>

  <a class="cs-card" href="15-Event-Driven-Architecture/01-Event-Sourcing/">
    <div class="cs-card-title">Event-Driven Architecture</div>
    <div class="cs-card-desc">Event sourcing, CQRS, dual-write problem, outbox pattern, inbox pattern, and CDC. The full toolkit for reliable event-driven systems.</div>
    <div class="cs-topics">
      <span>Event Sourcing</span><span>CQRS</span><span>Outbox Pattern</span><span>Inbox Pattern</span>
    </div>
    <div class="cs-card-cta">Open topic <span>→</span></div>
  </a>

  <a class="cs-card" href="16-Stream-Processing/01-Why-Stream-Processing/">
    <div class="cs-card-title">Stream Processing</div>
    <div class="cs-card-desc">Window types, watermarks, statefulness, and crash recovery. Processing infinite event streams in real time without losing data.</div>
    <div class="cs-topics">
      <span>Windowing</span><span>Watermarks</span><span>Stateful Processing</span><span>Crash Recovery</span>
    </div>
    <div class="cs-card-cta">Open topic <span>→</span></div>
  </a>

  <a class="cs-card" href="17-Batch-Processing/MapReduce/01-Why-Batch-Processing/">
    <div class="cs-card-title">Batch Processing</div>
    <div class="cs-card-desc">MapReduce and Spark — how to process petabytes of data in bounded jobs. Map, shuffle, reduce, DAG optimization, and hot key handling.</div>
    <div class="cs-topics">
      <span>MapReduce</span><span>Spark</span><span>DAG</span><span>Hot Keys</span>
    </div>
    <div class="cs-card-cta">Open topic <span>→</span></div>
  </a>

  <a class="cs-card" href="18-Lambda-Kappa/01-Lambda-Architecture/">
    <div class="cs-card-title">Lambda & Kappa</div>
    <div class="cs-card-desc">Architectures for combining batch and stream processing. Lambda's two-layer approach vs Kappa's stream-only simplification.</div>
    <div class="cs-topics">
      <span>Lambda Architecture</span><span>Kappa Architecture</span><span>Batch Layer</span><span>Speed Layer</span>
    </div>
    <div class="cs-card-cta">Open topic <span>→</span></div>
  </a>

  <a class="cs-card" href="19-Schema-Evolution/01-Why-Schema-Evolution/">
    <div class="cs-card-title">Schema Evolution</div>
    <div class="cs-card-desc">Schema Registry, Protobuf, and Avro. How you change message formats over time without breaking producers and consumers that deploy independently.</div>
    <div class="cs-topics">
      <span>Schema Registry</span><span>Protobuf</span><span>Avro</span><span>Backward Compatibility</span>
    </div>
    <div class="cs-card-cta">Open topic <span>→</span></div>
  </a>

</div>
