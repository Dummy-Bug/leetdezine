---
title: WhatsApp — Deep Dives
hide:
  - navigation
  - toc
---

<div class="cs-level-hero cs-lv5">
  <div class="cs-level-bg-num">DD</div>
  <div class="cs-level-inner">
    <p class="cs-level-eyebrow">WhatsApp · Deep Dives</p>
    <h1 class="cs-level-title">Deep Dives</h1>
    <p class="cs-level-sub">Eight deep dives — database, message ordering, offline delivery, message status, inbox, caching, peak traffic, and fault isolation.</p>
  </div>
</div>

<div class="cs-concepts-grid cs-concepts-index-grid">

  <a href="../db-choice/" class="cs-concept-card cs-concept-c4">
    <div class="cs-concept-card-title">Database</div>
    <div class="cs-concept-card-desc">DB choice, schema, tiered storage, sharding, and hot partition detection and salting.</div>
    <div class="cs-concept-chips">
      <span>DynamoDB</span><span>Sharding</span><span>Hot Partition</span><span>Salting</span>
    </div>
    <div class="cs-concept-cta">Open <span>→</span></div>
  </a>

  <a href="../message-ordering-the-problem/" class="cs-concept-card cs-concept-c4">
    <div class="cs-concept-card-title">Message Ordering</div>
    <div class="cs-concept-card-desc">Client vs server timestamps, the time machine problem, and per-conversation sequence with Redis INCR.</div>
    <div class="cs-concept-chips">
      <span>Per-Conv. Seq</span><span>Redis INCR</span><span>Clock Skew</span>
    </div>
    <div class="cs-concept-cta">Open <span>→</span></div>
  </a>

  <a href="../offline-delivery-the-problem/" class="cs-concept-card cs-concept-c4">
    <div class="cs-concept-card-title">Offline Delivery</div>
    <div class="cs-concept-card-desc">Detecting offline users, pending deliveries table, push notification flow, and reconnect sync.</div>
    <div class="cs-concept-chips">
      <span>Offline Queue</span><span>Push Notification</span><span>Pending Deliveries</span>
    </div>
    <div class="cs-concept-cta">Open <span>→</span></div>
  </a>

  <a href="../message-status-the-three-ticks/" class="cs-concept-card cs-concept-c4">
    <div class="cs-concept-card-title">Message Status</div>
    <div class="cs-concept-card-desc">Three ticks implementation, status table, delivered ack, read receipts, and privacy settings.</div>
    <div class="cs-concept-chips">
      <span>Read Receipts</span><span>Three Ticks</span><span>Privacy</span><span>Last Seen</span>
    </div>
    <div class="cs-concept-cta">Open <span>→</span></div>
  </a>

  <a href="../inbox-load-flow/" class="cs-concept-card cs-concept-c4">
    <div class="cs-concept-card-title">Inbox</div>
    <div class="cs-concept-card-desc">Inbox load flow, N+1 problem, denormalization, Redis sorted set for conversation list.</div>
    <div class="cs-concept-chips">
      <span>N+1 Problem</span><span>Denormalization</span><span>Redis Sorted Set</span>
    </div>
    <div class="cs-concept-cta">Open <span>→</span></div>
  </a>

  <a href="../caching-message-history-cache/" class="cs-concept-card cs-concept-c4">
    <div class="cs-concept-card-title">Caching</div>
    <div class="cs-concept-card-desc">Message history cache, profile cache, cache invalidation, cold start, and coalescing.</div>
    <div class="cs-concept-chips">
      <span>Message Cache</span><span>Profile Cache</span><span>Cold Start</span><span>Invalidation</span>
    </div>
    <div class="cs-concept-cta">Open <span>→</span></div>
  </a>

  <a href="../peak-traffic-thundering-herd-redis-sharding/" class="cs-concept-card cs-concept-c4">
    <div class="cs-concept-card-title">Peak Traffic</div>
    <div class="cs-concept-card-desc">Thundering herd, connection storm, rate limiting, backpressure, and load shedding.</div>
    <div class="cs-concept-chips">
      <span>Thundering Herd</span><span>Backpressure</span><span>Connection Storm</span><span>Load Shedding</span>
    </div>
    <div class="cs-concept-cta">Open <span>→</span></div>
  </a>

  <a href="../xx-fault-isolation-connection-server-failure-client-reconnect/" class="cs-concept-card cs-concept-c4">
    <div class="cs-concept-card-title">Fault Isolation</div>
    <div class="cs-concept-card-desc">Connection server failure, DynamoDB failure, Redis failure — each isolated with circuit breakers.</div>
    <div class="cs-concept-chips">
      <span>Reconnect Storm</span><span>Circuit Breaker</span><span>Redis Failure</span>
    </div>
    <div class="cs-concept-cta">Open <span>→</span></div>
  </a>

</div>
