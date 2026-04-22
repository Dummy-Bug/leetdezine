# Concurrency & Locking — Overview

> Two users. Same data. Same moment. Only one can win cleanly.

> [!abstract] The moment two requests touch the same data simultaneously, you have a concurrency problem. This folder covers how to detect it, prevent it, and design systems that handle simultaneous access correctly — from single database rows to distributed operations across multiple servers.

---

## Files in this folder

| File | Topic |
|---|---|
| [Race Conditions](01-Race-Conditions.md) | What goes wrong when two operations interfere |
| [Pessimistic Locking](02-Pessimistic-Locking.md) | Lock first, act second — deadlocks and prevention |
| [Optimistic Locking](03-Optimistic-Locking.md) | Act first, verify after — version numbers and CAS |
| [Read Write Locks](04-Read-Write-Locks.md) | Multiple readers, single writer |
| [MVCC](05-MVCC.md) | Snapshot isolation — readers never block writers |
| [Distributed Locking](06-Distributed-Locking.md) | Redis locks across multiple servers |
| [Idempotency](07-Idempotency.md) | Safe retries — idempotency keys across service hops |
| [Interview Cheatsheet](08-Interview-Cheatsheet.md) | Decision framework, what to say, full checklist |
