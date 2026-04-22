# Availability — Overview

> Availability is not just "is the server on" — it's whether the entire path from user to response is working.

> [!abstract] Every system design interview asks about failure. "What happens if this server goes down?" is an availability question. This folder teaches you how to identify single points of failure, eliminate them with redundancy, and calculate the real impact of your design choices on uptime.

---

## Files in this folder

| File | Topic |
|---|---|
| [Availability](01-Availability.md) | What availability is, formula, causes of unavailability |
| [SPOF](02-SPOF.md) | Single points of failure, redundancy, automatic failover |
| [N+1 Redundancy](03-N+1-Redundancy.md) | How much redundancy is enough — the N+1 formula |
| [Availability Patterns](04-Availability-Patterns.md) | Active-Active vs Active-Passive, stateless vs stateful |
| [Nines of Availability](05-Nines-of-Availability.md) | 99% to 99.999% in real downtime numbers |
| [Series vs Parallel](06-Series-vs-Parallel.md) | How combining components affects overall availability |
| [Interview Cheatsheet](07-Interview-Cheatsheet.md) | How to use availability in a design interview |
