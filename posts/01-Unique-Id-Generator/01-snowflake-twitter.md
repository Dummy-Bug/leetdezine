# Snowflake — Twitter Thread

## Tweet 1 (Hook)

In 2010, Twitter needed to generate IDs fast enough to handle millions of tweets — without a shared counter that every server had to check. So they designed Snowflake.

---

## Tweet 2 (Reply to Tweet 1)

64 bits. Timestamp in the top 41, machine ID next, sequence last. Timestamp being first means: sort by ID = sort by time. Zero coordination. Zero SPOF. Discord and Instagram still use the same layout.

Full breakdown → https://dummy-bug.github.io/leetdezine/
