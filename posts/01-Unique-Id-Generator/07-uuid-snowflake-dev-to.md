---
title: Why Random UUIDs are Killing Your Database Performance (and what to use instead)
published: false
description: Why standard UUIDs cause page splits and how Snowflake IDs solve for scale.
tags: architecture, database, backend, systemdesign
---

# Why Random UUIDs are Killing Your Database Performance (and what to use instead)

Every developer starts with a UUID. It’s the industry standard for a reason: zero coordination, zero DB checks, and zero single point of failure. Any machine can generate one and be 100% sure it’s unique.

But as your system scales, that "standard" choice starts to hurt.

### The Problem: UUIDs vs. Databases
If you're using **UUID v4** (completely random), you're essentially handing your database a grenade. 

Because the IDs are random, every new insert lands in a random spot in your B-Tree index. This causes **page splits**, fragments your storage, and slows down your writes as the table grows. Plus, at 128 bits (16 bytes), they're twice as large as a standard `BIGINT`.

### The Evolution of ID Generation

1.  **Single Server Counter:** Simple, but if the server dies, your ID generation stops (SPOF).
2.  **UUID v4:** Globally unique, but random and huge. No time-sortability.
3.  **UUID v7:** The modern middle ground. It's still 16 bytes, but it's **time-sortable**, which fixes the database page-split problem.
4.  **Ticket Server (Redis):** Centralized counter. Fast, but now your ID generation depends on Redis availability.
5.  **Snowflake IDs:** The "Big Tech" solution (used by Twitter, Discord, and Instagram).

### Why Snowflake Wins
Snowflake IDs pack everything you need into just **64 bits (8 bytes)**. They fit perfectly into a standard `BIGINT`, making them fast to index and easy to store.

Here is the "just enough" breakdown of how those 64 bits are structured:

*   **1 bit (Sign):** Always 0 (keeps the number positive).
*   **41 bits (Timestamp):** Milliseconds since a custom epoch. This gives you ~69 years of IDs and makes them **natively time-sortable**.
*   **10 bits (Machine ID):** Allows up to 1,024 independent nodes to generate IDs simultaneously without talking to each other.
*   **12 bits (Sequence):** A counter for IDs generated in the same millisecond on the same machine (up to 4,096 IDs/ms).

### The Comparison

| Property | UUID v4 | UUID v7 | Snowflake |
| :--- | :--- | :--- | :--- |
| **Size** | 128-bit | 128-bit | **64-bit** |
| **Sortable** | ❌ No | ✅ Yes | ✅ Yes |
| **Coordination** | ✅ None | ✅ None | ✅ None |
| **DB Friendly** | ❌ No | ✅ Yes | ✅ **Best** |

### Which one should you choose?

*   **Quick Prototypes:** Stick with **UUID v4**. It’s easy and requires zero setup.
*   **Modern Web Apps:** Move to **UUID v7**. You get the simplicity of UUIDs with the performance of time-sortable IDs.
*   **High-Scale Systems:** Go with **Snowflake**. When every byte and every millisecond of database latency matters, 64-bit sortable IDs are the only way to go.

**The Golden Rule:** You can't just "trim" a UUID to make it shorter. Trimming 128 bits down to 6 characters for a "short link" throws away 92 bits of entropy, turning a global guarantee into a collision nightmare.

*For a full deep dive into the math and architecture behind distributed IDs, check out the case study at [LeetDezine](https://leetdezine.com/03-Case-Studies/01-Foundation/01-Unique-ID-Generator/)
