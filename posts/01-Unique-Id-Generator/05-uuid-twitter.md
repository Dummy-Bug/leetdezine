# UUID — Twitter Thread

## Tweet 1 (Hook)

UUIDs are the "set it and forget it" of ID generation. 128 bits of pure, distributed uniqueness with zero coordination and zero single point of failure.

But if you’re building a URL shortener, a UUID is actually your worst enemy. 🧵

---

## Tweet 2 (Reply to Tweet 1)

Even Base64-encoded, a UUID is 22 chars. Not a short link.

Trim it to 6 chars and you throw away 92 bits of entropy. Two UUIDs can share the same first 36 bits—now you need the DB check you were trying to skip.

Full breakdown → https://leetdezine.com
