# SQS FIFO vs Standard Queue: Differences, Tradeoffs, and When to Use Each

## Platform: DEV.to
## Canonical URL: https://leetdezine.com/notification-system/?utm_source=devto
## Tags: systemdesign, distributedsystems, backend, aws

---

The SQS FIFO vs Standard decision sounds simple: need ordering? Use FIFO. Don't care? Use Standard.

That framing leads to the wrong answer more often than not. The real question isn't "do I need ordering?" — it's "what actually breaks if messages arrive out of order or more than once?"

---

## The Core Difference

**SQS Standard:**
- Throughput: high (can scale via sharding, region defaults are generous)
- Delivery: at-least-once — the same message can appear more than once
- Ordering: best-effort — messages might arrive out of order

**SQS FIFO:**
- Throughput: 3,000 messages/sec per queue (300 per message group without batching)
- Delivery: exactly-once — deduplication built in via `MessageDeduplicationId`
- Ordering: strict — messages within a group are delivered in send order

FIFO looks better on every axis except throughput. That exception is the one that kills you at scale.

---

## The Throughput Wall

A notification system handling 5M messages/sec — Instagram-scale, celebrity post, 10M followers needing push notifications — runs into a hard wall with FIFO.

At 3K/sec per queue, you need 1,667 queues to absorb the peak. Now you need routing logic: which notification goes to which queue? You need to partition users, maintain queue mappings, handle rebalancing. You've built Kafka, badly.

Even at moderate scale — 50K/sec — that's 17 FIFO queues with custom routing on top. The operational complexity eats the simplicity SQS was supposed to give you.

The ceiling is architectural, not configurable. FIFO queues don't scale horizontally the way Kafka partitions do.

---

## The Ordering Trap

Most engineers reach for FIFO because ordering *sounds* important. It's usually the wrong diagnosis.

Ordering matters when out-of-order processing corrupts state. A bank ledger where debit must follow credit. An event sourcing system where aggregate state is reconstructed from events in sequence. A stock trading system where order execution has legal ordering requirements.

For a notification system? Notification B arriving before notification A doesn't break anything. The user sees both.

What engineers actually want when they say "ordering" is usually **idempotency** — the ability to process a message twice without sending duplicate notifications. That's not a queue property, that's a consumer design property.

An idempotent consumer checks: "have I already sent this notification?" If yes, skip. Now you get SQS Standard's throughput with the same safety guarantee — and you're not fighting a 3K/sec ceiling.

The question to ask before picking FIFO: *"What breaks if this message arrives twice or slightly out of order?"* If the answer is "nothing, as long as the consumer handles it" — you don't need FIFO.

---

## What Neither Gives You: Replay

Both FIFO and Standard share one critical limitation nobody talks about enough.

Messages are deleted after consumption.

You deploy a bug that silently sends wrong notifications for 2 hours. By the time you notice, SQS has deleted every message from that window — consumed and acknowledged, gone. You cannot rewind. You cannot re-process the affected window with fixed code. The data doesn't exist in the queue anymore.

This is not a theoretical edge case. Silent bugs in notification systems happen. The right response is to replay the message stream with fixed code — SQS makes that impossible.

Kafka retains messages on disk for a configurable window (7 days by default). Rewind the consumer offset to 2 hours ago, re-process the entire window. Every message that went out wrong gets corrected.

---

## The Decision Framework

| | SQS Standard | SQS FIFO | Kafka |
|---|---|---|---|
| Throughput | High | 3K/sec/queue | 500K–1M/sec/broker |
| Ordering | Best-effort | Strict per group | Strict per partition |
| Delivery | At-least-once | Exactly-once | At-least-once |
| Replay | No | No | Yes |
| Fan-out | Manual (multiple queues) | Manual | Consumer groups (free) |
| Right for | Task queues, moderate volume | Ledgers, ordered state machines | High-throughput, fan-out, replay |

**Use Standard when:** task distribution, idempotent consumers, moderate throughput, operational simplicity is the priority.

**Use FIFO when:** you genuinely need strict ordering and exactly-once semantics — financial ledgers, event sourcing — and your peak throughput fits within 3K messages/sec per queue.

**Use Kafka when:** you need fan-out to multiple independent consumers, replay capability for failure recovery, or throughput that SQS can't handle without building complexity yourself.

---

The wrong answer at scale isn't using SQS Standard when you should have used FIFO. It's using either when your actual requirements — throughput, fan-out, replay — are requirements that Kafka was built for.

Full notification system case study → https://leetdezine.com/notification-system/?utm_source=devto
