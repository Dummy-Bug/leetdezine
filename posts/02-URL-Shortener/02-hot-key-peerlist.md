# Hot Key Problem — Peerlist Post

Consistent hashing maps each short code to one Redis node. Works great — until a link goes viral.

800k reads/sec, all hitting the same node. Rest of your cluster is idle. One node is on fire.

The naive fix is more Redis. But you can't move a key without rehashing.

The real fix: stop the hot key from reaching Redis at all.

Each app server keeps an in-memory counter. When reads for a key cross ~50k/sec, that server caches the URL locally. The request never leaves the machine.

Why it's safe: short URL mappings are immutable. Once `x7k2p9 → long-url.com`, that never changes. No cache invalidation problem. Just a 60s TTL for memory management.

For mutable data you'd need key salting — N copies of the hot key spread across different Redis nodes. But for a URL shortener, local cache is cleaner, zero extra infra, and handles the spike.

Full breakdown → https://leetdezine.com/03-Case-Studies/01-Foundation/02-URL-Shortener/?utm_source=peerlist
