# SQS FIFO vs Standard — Twitter Thread

## Tweet 1 (Hook)

SQS FIFO sounds like the safe choice. It's not always.

Standard: high throughput, at-least-once delivery, no ordering guarantee.
FIFO: ordered, exactly-once, but capped at 3K messages/sec per queue.

At 5M notifications/sec — FIFO can't keep up. And you probably don't need ordering anyway.

#SystemDesign #SoftwareEngineering #DistributedSystems

---

## Tweet 2 (Reply to Tweet 1)

The trap: choosing FIFO because "ordering sounds important."

Most async systems don't need strict ordering — they need idempotent processing. If your consumer handles duplicates safely, Standard + idempotent handler beats FIFO at 10× the throughput.

And neither gives you replay. → https://leetdezine.com/03-Case-Studies/02-Ascent/01-Notification-System/?utm_source=twitter
