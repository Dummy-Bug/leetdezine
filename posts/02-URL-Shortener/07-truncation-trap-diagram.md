# Post 1 — The Truncation Trap
# Platform: Twitter/X + Peerlist (screenshot this as image)
# Day: Day 1

---

```
64-bit Snowflake ID layout
┌─────────────────────────┬──────────────────┬─────────────────┐
│   timestamp (41 bits)   │ machine (10 bits) │ sequence (12 b) │
└─────────────────────────┴──────────────────┴─────────────────┘

"I only need 36 bits — drop the rightmost 28..."

┌─────────────────────────────────────┬──────────────────────────┐
│         keep 36 bits                │     drop 28 bits         │
│  (most of timestamp)                │  (machine ID + sequence) │
└─────────────────────────────────────┴──────────────────────────┘

Request A  — same server, t=1700000001ms, seq=1
┌─────────────────────────────────────┬──────────────────────────┐
│     0 1 1 0 1 0 0 1 0 1 0 1 ...     │    machine=3, seq=1      │
└─────────────────────────────────────┴──────────────────────────┘
                    ↓ base62
                 "x7k2p9"

Request B  — same server, t=1700000001ms, seq=2
┌─────────────────────────────────────┬──────────────────────────┐
│     0 1 1 0 1 0 0 1 0 1 0 1 ...     │    machine=3, seq=2      │
└─────────────────────────────────────┴──────────────────────────┘
                    ↓ base62
                 "x7k2p9"  ✗  COLLISION

The sequence number (seq=1 vs seq=2) was the only difference.
You dropped it.
```
