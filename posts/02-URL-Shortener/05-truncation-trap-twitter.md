# Post 1 — The Truncation Trap
# Platform: Twitter/X
# Day: Day 1

---

**Tweet 1** (hook)

Snowflake ID is 64 bits. You only need 36 to cover 50B URLs.

Natural move: drop the rightmost 28 bits, encode the rest → 6-char code. Timestamp is intact. Looks unique.

Two requests on the same server in the same millisecond get the same code.

#SystemDesign #SoftwareEngineering #DistributedSystems

---

**Tweet 2** (insight + link)

The rightmost bits you dropped were the sequence number — the only thing that separates two Snowflakes born in the same millisecond.

Timestamp alone doesn't guarantee uniqueness. All 64 bits do, together.

Full URL shortener deep dive:
https://leetdezine.com/03-Case-Studies/01-Foundation/02-URL-Shortener/02-Deep-Dives/?utm_source=twitter
