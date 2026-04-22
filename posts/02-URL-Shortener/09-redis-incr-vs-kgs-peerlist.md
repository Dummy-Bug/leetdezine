# Post 2 — Redis INCR vs KGS
# Platform: Peerlist
# Day: Day 2

---

Redis INCR looks like the perfect shortcode generator. Technically, it is.

Atomic counter increments — every call returns a unique integer. Encode it in base62 and you get a unique short code with zero collision checks, zero retries, and no background service to operate. It's significantly simpler than running a Key Generation Service.

The reason it fails in a public URL shortener has nothing to do with code generation.

Counter values are sequential. If your user receives `bit.ly/004C9M`, they immediately know the previous URL is `bit.ly/004C9L` and the next is `bit.ly/004C9N`. They can walk the entire list. Every URL in your system is discoverable by incrementing one character.

For an internal tool, that might be fine. For a public shortener — where someone might shorten a pre-announcement link, an internal doc, or a private file — it's a real privacy violation.

The second problem: Redis INCR makes Redis a hard dependency on every creation request. No Redis, no new URLs. The KGS + pool approach pre-fetches 100 keys per app server locally, so Redis going down doesn't immediately break creation — you drain the local batch first.

Redis INCR is the right call for internal tools. KGS + pool is the right call for a public shortener.

Full breakdown: https://leetdezine.com/03-Case-Studies/01-Foundation/02-URL-Shortener/02-Deep-Dives/?utm_source=peerlist
