# Post 2 — Redis INCR vs KGS
# Platform: Twitter/X
# Day: Day 2

---

**Tweet 1** (hook)

Redis INCR for URL shortening: atomic, zero collisions, no background service. Elegant.

Also wrong for a public shortener.

Sequential codes let any user enumerate every URL in the system by incrementing one character.

#SystemDesign #SoftwareEngineering #DistributedSystems

---

**Tweet 2** (insight + link)

You get bit.ly/004C9M. The previous URL is bit.ly/004C9L. The next is bit.ly/004C9N.

Anyone can walk your entire URL database.

KGS + Redis pool fixes both: random code order, local batch pre-fetch, Redis failure doesn't block creation.

https://leetdezine.com?utm_source=twitter
