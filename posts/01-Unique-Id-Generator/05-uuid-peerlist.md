# UUID — Peerlist Post

If you want distributed ID generation, everyone starts with a UUID. It’s the industry standard for a reason: zero coordination, zero DB check, and zero single point of failure. Any machine can generate one and be 100% sure it’s unique.

But when I was looking into URL shorteners, I realized why they’re the wrong choice for "short" IDs. 

A standard UUID is 128 bits. If you encode it with Base64, you're still looking at a 22-character string. That's not a short URL—it's a path.

The temptation is to just trim it. Take the first 6 characters of that Base64 string and call it a day. But the math doesn't work. By trimming, you’re throwing away most of the entropy that makes a UUID unique in the first place. Two different UUIDs can easily share the same first 36 bits, and suddenly you’re dealing with collisions you can’t fix without a central DB check.

For URL shorteners, the rule is simple: You cannot trim your way to uniqueness. 

You need something designed for the scale you're actually at. For most use cases, 36 bits is all you need to cover 50 billion URLs—but you have to structure those bits intentionally. 

Full breakdown on why Snowflake > UUID for short IDs:
https://leetdezine.com
