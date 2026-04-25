---
title: Cache Eviction vs TTL — How They Differ and When Each Fires
---

# Eviction vs TTL — Two Different Mechanisms

> [!abstract] Eviction and TTL are two separate mechanisms that both delete keys from a cache. They're easy to confuse but operate on completely different triggers, and both can apply to the same key.

> [!important] Eviction and TTL are two separate mechanisms
> **TTL** — time-based. Key deleted when its timer runs out, regardless of memory pressure.
> **Eviction** — memory-based. Triggered only when cache is full and needs space for a new key.
> Both can apply to the same key. Whichever fires first wins.
