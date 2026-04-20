# Consistent Hashing

Consistent hashing maps keys to nodes on a virtual ring so that adding or removing a node only remaps a small fraction of keys — not the entire dataset. It's the foundation of how distributed caches and sharded databases scale horizontally.

This topic is covered in two places depending on your angle:

**[→ Read: Consistent Hashing](../../03-Caching/06-Distributed-Caching/02-Consistent-Hashing.md)** — Caching perspective (cache nodes, hot keys)

**[→ Read: Consistent Hashing](../../04-Storage-and-Databases/06-Sharding/04-Consistent-Hashing.md)** — Storage perspective (shard rebalancing, vnodes)
