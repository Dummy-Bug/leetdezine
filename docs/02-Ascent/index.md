---
hide:
  - navigation
  - toc
---

<div class="cs-hero" markdown>
<p class="cs-hero-label">LEVEL 2</p>
<h1 class="cs-hero-title">Ascent</h1>
<p class="cs-hero-sub">Blob storage, content deduplication, async pipelines, expiry management.</p>
</div>

<p class="cs-path-label">CASE STUDIES</p>

<div class="cs-cards">
  <a class="cs-card" href="01-Notification-System/00-System-Overview/">
    <div class="cs-card-header"><span class="cs-badge ascent">ASCENT</span></div>
    <div class="cs-card-title">Notification System</div>
    <div class="cs-card-desc">Design a notification system — push, SMS, and email delivery at 5M sends/sec. Multi-channel fan-out, retry/DLQ, scheduled delivery, fault isolation per provider.</div>
    <div class="cs-topics">
      <span>Kafka Fan-out</span>
      <span>Per-Channel Workers</span>
      <span>Retry / DLQ</span>
      <span>Bloom Filter</span>
      <span>Scheduling</span>
      <span>Circuit Breaker</span>
    </div>
  </a>
  <a class="cs-card" href="02-Pastebin/">
    <div class="cs-card-header"><span class="cs-badge ascent">ASCENT</span></div>
    <div class="cs-card-title">Pastebin</div>
    <div class="cs-card-desc">Design pastebin.com — paste text, get a short link, retrieve by anyone. 10M DAU, expiring pastes, large blobs.</div>
    <div class="cs-topics">
      <span>Content-Addressable Storage</span>
      <span>Ref Counting</span>
      <span>Async S3 Upload</span>
      <span>Expiry Jobs</span>
      <span>State Machine</span>
    </div>
  </a>
</div>
