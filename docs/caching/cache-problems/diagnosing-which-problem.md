---
title: How to Diagnose Cache Problems — Stampede vs Avalanche vs Penetration vs Cold Start
---

# Diagnosing Cache Problems — Which One Is It?

> [!abstract] Four failure modes that all look the same on the outside — the DB gets hammered — but have completely different causes and require different fixes. Diagnosing which one you have determines which solution to reach for.

## The diagnostic question

```
DB is being hammered. Which problem is it?

Is the cache empty?                           → Cold Start
Does one specific popular key keep expiring?  → Cache Stampede
Are requests for non-existent keys flooding?  → Cache Penetration
Did many keys expire at the same time?        → Cache Avalanche
```
