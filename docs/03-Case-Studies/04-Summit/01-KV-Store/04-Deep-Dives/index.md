---
title: Deep Dives
hide:
  - navigation
  - toc
---

<div class="cs-level-hero cs-lv4">
  <div class="cs-level-bg-num">DD</div>
  <div class="cs-level-inner">
    <p class="cs-level-eyebrow">KV Store · Deep Dives</p>
    <h1 class="cs-level-title">Deep Dives</h1>
    <p class="cs-level-sub">Seven deep dives — consistent hashing, quorum replication, LSM storage engine, cluster membership, conflict resolution, TTL, and fault isolation.</p>
  </div>
</div>

<div class="cs-concepts-grid cs-concepts-index-grid">

  <a href="01-Consistent-Hashing/01-Terminology/" class="cs-concept-card cs-concept-c4">
    <div class="cs-concept-card-title">Consistent Hashing</div>
    <div class="cs-concept-card-desc">Ring terminology, virtual nodes, and how data maps to nodes as the cluster scales.</div>
    <div class="cs-concept-chips">
      <span>Hash Ring</span><span>Virtual Nodes</span><span>Data Distribution</span>
    </div>
    <div class="cs-concept-cta">Open <span>→</span></div>
  </a>

  <a href="02-Replication/01-Quorum-Writes/" class="cs-concept-card cs-concept-c4">
    <div class="cs-concept-card-title">Replication</div>
    <div class="cs-concept-card-desc">Quorum writes, hinted handoff, read repair, and anti-entropy for eventual consistency.</div>
    <div class="cs-concept-chips">
      <span>Quorum W/R</span><span>Hinted Handoff</span><span>Read Repair</span><span>Anti-Entropy</span>
    </div>
    <div class="cs-concept-cta">Open <span>→</span></div>
  </a>

  <a href="03-Storage-Engine/01-B+Tree-vs-LSM-Tree/" class="cs-concept-card cs-concept-c4">
    <div class="cs-concept-card-title">Storage Engine</div>
    <div class="cs-concept-card-desc">B+Tree vs LSM tree, LSM internals, compaction strategies, and bloom filters for read optimisation.</div>
    <div class="cs-concept-chips">
      <span>LSM Tree</span><span>Compaction</span><span>Bloom Filters</span><span>SSTables</span>
    </div>
    <div class="cs-concept-cta">Open <span>→</span></div>
  </a>

  <a href="04-Cluster-Membership/01-The-Problem/" class="cs-concept-card cs-concept-c4">
    <div class="cs-concept-card-title">Cluster Membership</div>
    <div class="cs-concept-card-desc">The membership problem, gossip protocol for propagation, and failure detection.</div>
    <div class="cs-concept-chips">
      <span>Gossip Protocol</span><span>Failure Detection</span><span>Membership</span>
    </div>
    <div class="cs-concept-cta">Open <span>→</span></div>
  </a>

  <a href="05-Conflict-Resolution/01-The-Problem/" class="cs-concept-card cs-concept-c4">
    <div class="cs-concept-card-title">Conflict Resolution</div>
    <div class="cs-concept-card-desc">Why conflicts occur in leaderless replication and vector clock solution.</div>
    <div class="cs-concept-chips">
      <span>Vector Clocks</span><span>Leaderless</span><span>Conflict</span>
    </div>
    <div class="cs-concept-cta">Open <span>→</span></div>
  </a>

  <a href="06-TTL-And-Data-Expiry/01-How-TTL-Works/" class="cs-concept-card cs-concept-c4">
    <div class="cs-concept-card-title">TTL & Data Expiry</div>
    <div class="cs-concept-card-desc">How TTL works in a distributed KV store — lazy deletion vs active expiry.</div>
    <div class="cs-concept-chips">
      <span>TTL</span><span>Lazy Deletion</span><span>Active Expiry</span>
    </div>
    <div class="cs-concept-cta">Open <span>→</span></div>
  </a>

  <a href="07-Fault-Isolation/01-Node-Failure/" class="cs-concept-card cs-concept-c4">
    <div class="cs-concept-card-title">Fault Isolation</div>
    <div class="cs-concept-card-desc">Node failure, disk failure, network partition, cascading failures, and coordinator failure.</div>
    <div class="cs-concept-chips">
      <span>Node Failure</span><span>Disk Failure</span><span>Network Partition</span><span>Cascading</span>
    </div>
    <div class="cs-concept-cta">Open <span>→</span></div>
  </a>

</div>
