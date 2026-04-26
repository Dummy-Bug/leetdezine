# Why Did We Pick Kafka Over SQS FIFO for 5M Notifications per Second?

## Platform: Peerlist

---

The default instinct when you need a queue: reach for SQS. When you care about ordering: reach for FIFO.

FIFO sounds safer — exactly-once delivery, strict ordering. What's not to like?

The throughput ceiling. SQS FIFO is capped at 3,000 messages/sec per queue. At 5M notifications/sec — a celebrity posts on Instagram, 10M followers each need a push — you'd need hundreds of SQS queues, custom routing logic, and you've built a poor man's Kafka.

The deeper problem: most systems that reach for FIFO don't actually need strict ordering. They need idempotent processing — if a message gets delivered twice, the consumer handles it gracefully. That's not an ordering problem. That's a consumer design problem. SQS Standard handles it fine at far higher throughput.

What neither FIFO nor Standard gives you is replay. SQS deletes messages after consumption. Deploy a bug that sends wrong notifications for 2 hours and those messages are gone. No rewind. No recovery. Kafka retains messages on disk for 7 days — rewind the offset and reprocess the entire window with fixed code.

Know what the queue actually gives you before you reach for it.

→ https://leetdezine.com/notification-system/?utm_source=peerlist
