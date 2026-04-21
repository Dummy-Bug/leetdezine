# Snowflake — Peerlist Post

Most ID generation schemes have a dirty secret: they need a central coordinator. Someone has to say "this ID hasn't been used yet." That coordinator becomes your bottleneck. Your SPOF.

Twitter hit this in 2010. Millions of tweets, hundreds of servers — they needed globally unique IDs without any server talking to another.

Snowflake was the fix: a 64-bit integer, split three ways. 41 bits for timestamp, 10 for machine ID, 12 for a per-millisecond sequence counter. Each machine generates IDs on its own. No coordination whatsoever.

The clever part: timestamp sits in the most significant bits, so sorting IDs numerically gives you chronological order. No separate `created_at` column. The ID is the timestamp.

Discord, Instagram, and most large platforms copied this exact design.

Full breakdown → https://leetdezine.com?utm_source=peerlist
