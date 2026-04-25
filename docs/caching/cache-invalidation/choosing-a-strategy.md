---
title: How to Choose a Cache Invalidation Strategy
---

# Cache Invalidation — Choosing a Strategy

> [!abstract] "There are only two hard things in computer science: cache invalidation and naming things." The reason it's hard: the cache doesn't automatically know when the DB changes. You have to tell it — or wait for time to expire it. Every strategy is a different trade-off between freshness, complexity, and performance.

## The spectrum

```
TTL-based              → simplest, stale window up to TTL duration
Event-driven           → instant, needs infrastructure
Write-through          → no miss after write, slower writes
Cache versioning       → no invalidation needed, two cache lookups per read
Stale-while-revalidate → one stale response, then fresh
```
