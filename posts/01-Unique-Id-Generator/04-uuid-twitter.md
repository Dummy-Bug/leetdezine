# UUID — Twitter Thread

## Tweet 1 (Hook)

UUIDs are the "set it and forget it" of ID generation. 128 bits of pure, distributed uniqueness with zero coordination and zero single point of failure.

But if you’re building a URL shortener, a UUID is actually your worst enemy. 🧵

---

## Tweet 2 (Reply to Tweet 1)

The math is brutal. Even with Base64 encoding, a UUID is 22 characters long—hardly a "short" link. 

The trap? Trimming it to 6 characters. You think you're being clever, but you just threw away 92 bits of entropy. You've traded a global guarantee for a collision nightmare.

Full breakdown → https://leetdezine.com
