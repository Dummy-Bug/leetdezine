---
title: Distributed Systems
hide:
  - navigation
  - toc
---

<div class="cs-level-hero cs-lv-concepts">
  <div class="cs-level-bg-num">06</div>
  <div class="cs-level-inner">
    <p class="cs-level-eyebrow">Concepts</p>
    <h1 class="cs-level-title">Distributed Systems</h1>
    <p class="cs-level-sub">What changes when your system runs on more than one machine. The problems, the algorithms, and the guarantees that make distributed computing tractable.</p>
  </div>
</div>

<div class="cs-cards">

  <a class="cs-card" href="01-Problems/01-2General-Problem/">
    <div class="cs-card-title">Why Distributed Systems Are Hard</div>
    <div class="cs-card-desc">The Two Generals Problem and network partitions. The fundamental uncertainty that makes distributed computing different from everything that came before.</div>
    <div class="cs-topics">
      <span>Two Generals</span><span>Network Uncertainty</span><span>Partial Failure</span><span>Split Brain</span>
    </div>
    <div class="cs-card-cta">Open topic <span>→</span></div>
  </a>

  <a class="cs-card" href="02-Consistent-Hashing/01-Consistent-Hashing/">
    <div class="cs-card-title">Consistent Hashing</div>
    <div class="cs-card-desc">How to distribute data across nodes so that adding or removing a node only moves a fraction of keys. The algorithm behind Cassandra, DynamoDB, and every CDN.</div>
    <div class="cs-topics">
      <span>Hash Ring</span><span>Virtual Nodes</span><span>Minimal Disruption</span><span>Hotspots</span>
    </div>
    <div class="cs-card-cta">Open topic <span>→</span></div>
  </a>

  <a class="cs-card" href="03-Replication/01-Replication-Strategies/">
    <div class="cs-card-title">Replication Strategies</div>
    <div class="cs-card-desc">Leader-follower, multi-leader, leaderless. The tradeoffs between write availability, consistency, and the complexity of conflict resolution.</div>
    <div class="cs-topics">
      <span>Leader-Follower</span><span>Multi-Leader</span><span>Leaderless</span><span>Quorum</span>
    </div>
    <div class="cs-card-cta">Open topic <span>→</span></div>
  </a>

  <a class="cs-card" href="04-Idempotency/01-Idempotency/">
    <div class="cs-card-title">Idempotency</div>
    <div class="cs-card-desc">Making operations safe to retry. The pattern that turns at-least-once delivery into exactly-once behavior without a coordination service.</div>
    <div class="cs-topics">
      <span>Idempotency Keys</span><span>Safe Retries</span><span>Deduplication</span><span>At-Least-Once</span>
    </div>
    <div class="cs-card-cta">Open topic <span>→</span></div>
  </a>

  <a class="cs-card" href="05-Delivery-Guarantees/01-Delivery-Guarantees/">
    <div class="cs-card-title">Delivery Guarantees</div>
    <div class="cs-card-desc">At-most-once, at-least-once, exactly-once at the distributed systems level — how these guarantees compose across network hops and node failures.</div>
    <div class="cs-topics">
      <span>At-Most-Once</span><span>At-Least-Once</span><span>Exactly-Once</span><span>ACK Semantics</span>
    </div>
    <div class="cs-card-cta">Open topic <span>→</span></div>
  </a>

  <a class="cs-card" href="06-Distributed-Transactions/01-Distributed-Transactions/">
    <div class="cs-card-title">Distributed Transactions</div>
    <div class="cs-card-desc">The problem of atomic commits across multiple nodes. 2PC, Saga choreography, Saga orchestration — and when each one is the right answer.</div>
    <div class="cs-topics">
      <span>2PC</span><span>Saga</span><span>Choreography</span><span>Orchestration</span>
    </div>
    <div class="cs-card-cta">Open topic <span>→</span></div>
  </a>

  <a class="cs-card" href="07-Consensus/01-What-Is-Consensus/">
    <div class="cs-card-title">Consensus</div>
    <div class="cs-card-desc">Raft, Paxos, and ZooKeeper. How distributed nodes agree on a single value despite failures — the algorithm that underpins leader election and log replication.</div>
    <div class="cs-topics">
      <span>Raft</span><span>Paxos</span><span>Leader Election</span><span>Log Replication</span>
    </div>
    <div class="cs-card-cta">Open topic <span>→</span></div>
  </a>

  <a class="cs-card" href="08-Distributed-Clocks/01-Clock-Drift/">
    <div class="cs-card-title">Distributed Clocks</div>
    <div class="cs-card-desc">Clock drift, NTP, Lamport clocks, vector clocks, and TrueTime. Why wall clocks can't order events in a distributed system and what to use instead.</div>
    <div class="cs-topics">
      <span>Clock Drift</span><span>Lamport Clocks</span><span>Vector Clocks</span><span>TrueTime</span>
    </div>
    <div class="cs-card-cta">Open topic <span>→</span></div>
  </a>

  <a class="cs-card" href="09-CRDTs/01-The-Problem/">
    <div class="cs-card-title">CRDTs</div>
    <div class="cs-card-desc">Conflict-free Replicated Data Types. Data structures that merge concurrent updates automatically — no locks, no consensus, no conflicts.</div>
    <div class="cs-topics">
      <span>G-Counter</span><span>Operational Transform</span><span>OT vs CRDT</span><span>Convergence</span>
    </div>
    <div class="cs-card-cta">Open topic <span>→</span></div>
  </a>

  <a class="cs-card" href="10-Failure-Detection/01-Heartbeats/">
    <div class="cs-card-title">Failure Detection</div>
    <div class="cs-card-desc">Heartbeats, gossip protocol, and the Phi Accrual Failure Detector. How nodes decide a peer is dead without being certain — and the cost of getting it wrong.</div>
    <div class="cs-topics">
      <span>Heartbeats</span><span>Gossip Protocol</span><span>Phi Accrual</span><span>False Positives</span>
    </div>
    <div class="cs-card-cta">Open topic <span>→</span></div>
  </a>

  <a class="cs-card" href="11-Merkle-Trees/01-The-Problem/">
    <div class="cs-card-title">Merkle Trees</div>
    <div class="cs-card-desc">Hash trees for detecting data inconsistency across replicas. How Cassandra and DynamoDB use Merkle Trees to run anti-entropy repair efficiently.</div>
    <div class="cs-topics">
      <span>Hash Tree</span><span>Anti-Entropy</span><span>Replica Sync</span><span>Bucket Hashing</span>
    </div>
    <div class="cs-card-cta">Open topic <span>→</span></div>
  </a>

  <a class="cs-card" href="12-Coordination-Services/01-The-Problem/">
    <div class="cs-card-title">Coordination Services</div>
    <div class="cs-card-desc">etcd, leases, TTL, fencing tokens, lock vs job tracking. The primitives that let distributed services elect leaders and claim exclusive work safely.</div>
    <div class="cs-topics">
      <span>etcd</span><span>Leases</span><span>Fencing Tokens</span><span>Distributed Lock</span>
    </div>
    <div class="cs-card-cta">Open topic <span>→</span></div>
  </a>

</div>
