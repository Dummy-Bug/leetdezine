---
title: Distributed Systems
hide:
  - navigation
  - toc
---

<div class="cs-level-hero cs-lv-concepts">
  <div class="cs-level-bg-num">10</div>
  <div class="cs-level-inner">
    <p class="cs-level-eyebrow">Concepts</p>
    <h1 class="cs-level-title">Distributed Systems</h1>
    <p class="cs-level-sub">The failure modes, trade-offs, and coordination problems that emerge the moment you have more than one node.</p>
  </div>
</div>

<div class="cs-cards">

  <a class="cs-card" href="01-Problems/01-General-Problem/">
    <div class="cs-card-title">The Problem</div>
    <div class="cs-card-desc">Why distributed systems are fundamentally harder than single-node ones — partial failures, network uncertainty, and no shared clock.</div>
    <div class="cs-topics">
      <span>Partial Failures</span><span>Network Uncertainty</span><span>No Global Clock</span><span>Fallacies</span>
    </div>
    <div class="cs-card-cta">Open topic <span>→</span></div>
  </a>

  <a class="cs-card" href="02-Network-Partitions/00-Overview/">
    <div class="cs-card-title">Network Partitions</div>
    <div class="cs-card-desc">What happens when nodes can't talk. Split brain, quorum decisions, and why partition handling defines your entire consistency strategy.</div>
    <div class="cs-topics">
      <span>Split Brain</span><span>Quorum</span><span>Fencing</span><span>Partition Recovery</span>
    </div>
    <div class="cs-card-cta">Open topic <span>→</span></div>
  </a>

  <a class="cs-card" href="03-CAP-Theorem/00-Overview/">
    <div class="cs-card-title">CAP Theorem</div>
    <div class="cs-card-desc">Consistency vs availability when a partition happens. CP vs AP — and why every distributed system is forced to choose during a split.</div>
    <div class="cs-topics">
      <span>CAP</span><span>CP Systems</span><span>AP Systems</span><span>Partition Tolerance</span>
    </div>
    <div class="cs-card-cta">Open topic <span>→</span></div>
  </a>

  <a class="cs-card" href="04-PACELC/00-Overview/">
    <div class="cs-card-title">PACELC</div>
    <div class="cs-card-desc">Extends CAP to cover normal operation. Even without a partition, you still trade latency against consistency — PACELC names that trade-off.</div>
    <div class="cs-topics">
      <span>PACELC</span><span>Latency vs Consistency</span><span>PA/EL</span><span>PC/EC</span>
    </div>
    <div class="cs-card-cta">Open topic <span>→</span></div>
  </a>

  <a class="cs-card" href="05-Consistency-Models/00-Overview/">
    <div class="cs-card-title">Consistency Models</div>
    <div class="cs-card-desc">Strong, eventual, causal, and monotonic. What "up to date" means in a distributed system and when each model is the right call.</div>
    <div class="cs-topics">
      <span>Strong Consistency</span><span>Eventual</span><span>Causal</span><span>Monotonic</span>
    </div>
    <div class="cs-card-cta">Open topic <span>→</span></div>
  </a>

  <a class="cs-card" href="06-Replication/01-What-is-Replication/">
    <div class="cs-card-title">Replication</div>
    <div class="cs-card-desc">Sync vs async replication, replication lag, failover, and multi-primary — how data stays consistent across nodes.</div>
    <div class="cs-topics">
      <span>Sync vs Async</span><span>Replication Lag</span><span>Failover</span><span>Multi-Primary</span>
    </div>
    <div class="cs-card-cta">Open topic <span>→</span></div>
  </a>

  <a class="cs-card" href="07-Sharding/01-What-is-Sharding/">
    <div class="cs-card-title">Sharding</div>
    <div class="cs-card-desc">Shard keys, consistent hashing, cross-shard joins, resharding, and the over-sharding trap that kills performance.</div>
    <div class="cs-topics">
      <span>Shard Key</span><span>Consistent Hashing</span><span>Resharding</span><span>Cross-Shard Joins</span>
    </div>
    <div class="cs-card-cta">Open topic <span>→</span></div>
  </a>

  <a class="cs-card" href="08-Consensus/01-What-Is-Consensus/">
    <div class="cs-card-title">Consensus</div>
    <div class="cs-card-desc">Raft leader election, log replication, Paxos phases, ZooKeeper, and Redis distributed locks — how nodes agree on a single value.</div>
    <div class="cs-topics">
      <span>Raft</span><span>Paxos</span><span>Leader Election</span><span>ZooKeeper</span>
    </div>
    <div class="cs-card-cta">Open topic <span>→</span></div>
  </a>

  <a class="cs-card" href="09-Distributed-Clocks/01-Clock-Drift/">
    <div class="cs-card-title">Distributed Clocks</div>
    <div class="cs-card-desc">Clock drift, NTP, Lamport clocks, vector clocks, and TrueTime — how distributed systems reason about time without a shared clock.</div>
    <div class="cs-topics">
      <span>Lamport Clocks</span><span>Vector Clocks</span><span>NTP</span><span>TrueTime</span>
    </div>
    <div class="cs-card-cta">Open topic <span>→</span></div>
  </a>

  <a class="cs-card" href="10-CRDTs/01-The-Problem/">
    <div class="cs-card-title">CRDTs</div>
    <div class="cs-card-desc">Conflict-free replicated data types — the math that lets replicas merge without coordination, and why locks fail at global scale.</div>
    <div class="cs-topics">
      <span>G-Counter</span><span>Operational Transform</span><span>OT vs CRDT</span><span>Merge Semantics</span>
    </div>
    <div class="cs-card-cta">Open topic <span>→</span></div>
  </a>

  <a class="cs-card" href="11-Failure-Detection/01-Heartbeats/">
    <div class="cs-card-title">Failure Detection</div>
    <div class="cs-card-desc">Heartbeats, gossip protocol, and the phi accrual failure detector — how nodes know when other nodes are dead.</div>
    <div class="cs-topics">
      <span>Heartbeats</span><span>Gossip Protocol</span><span>Phi Accrual</span><span>Timeouts</span>
    </div>
    <div class="cs-card-cta">Open topic <span>→</span></div>
  </a>

  <a class="cs-card" href="12-Merkle-Trees/01-The-Problem/">
    <div class="cs-card-title">Merkle Trees</div>
    <div class="cs-card-desc">Hash trees for efficient data comparison across replicas. Anti-entropy repair and how Dynamo-style systems detect divergence.</div>
    <div class="cs-topics">
      <span>Hash Trees</span><span>Anti-Entropy</span><span>Replica Sync</span><span>Buckets</span>
    </div>
    <div class="cs-card-cta">Open topic <span>→</span></div>
  </a>

  <a class="cs-card" href="13-Coordination-Services/01-The-Problem/">
    <div class="cs-card-title">Coordination Services</div>
    <div class="cs-card-desc">etcd, leases, TTL-based fencing tokens, and the difference between distributed locks and job tracking.</div>
    <div class="cs-topics">
      <span>etcd</span><span>Leases</span><span>Fencing Tokens</span><span>Lock vs Job Tracking</span>
    </div>
    <div class="cs-card-cta">Open topic <span>→</span></div>
  </a>

</div>
