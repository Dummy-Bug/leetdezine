# Post 1 — The Truncation Trap
# Platform: Peerlist
# Day: Day 1

---

Here's the interview trap nobody warns you about.

A Snowflake ID is 64 bits. You need only 36 bits to address 50 billion URLs — 2^36 = 68 billion covers a 10-year URL space. Encode 36 bits in base62 and you get exactly 6 characters.

The natural move: drop the rightmost 28 bits and keep the rest. You're keeping the timestamp, which feels like the important part. 36 bits → base62 → 6-char code with no collision check needed.

Except it breaks.

A Snowflake ID is structured like this:

```
[ timestamp — 41 bits ][ machine ID — 10 bits ][ sequence — 12 bits ]
 ←────── keep 36 bits ─────────────────────────→ ←── drop 28 bits ──→
```

The rightmost 28 bits you dropped contain the machine ID and the sequence number. The sequence number is what differentiates two Snowflake IDs generated on the same server within the same millisecond. Drop it, and those two IDs become identical after truncation — even though they were different before.

Two URL creation requests arriving at the same server within the same millisecond get the same 6-char code. At 1000 creations/sec, that millisecond window gets hit constantly.

The math was right. The truncation was wrong.

You cannot get both uniqueness and shortness by dropping bits from a Snowflake. Every section of those 64 bits contributes to the uniqueness guarantee. Drop any of them and you break it.

Full breakdown: https://leetdezine.com/case-studies/?utm_source=peerlist
