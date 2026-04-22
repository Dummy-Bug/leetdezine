# Reliability — Overview

> Availability means the system is reachable. Reliability means it gives correct answers. These are different problems with different solutions.

> [!abstract] A system can be perfectly available and completely broken at the same time — returning wrong data, stale responses, or corrupt results. This folder covers reliability as a separate concern from availability, and the metrics (MTBF, MTTR, RTO, RPO) used to design and measure it.

---

## Files in this folder

| File | Topic |
|---|---|
| [Reliability](01-Reliability.md) | What reliability is and available-but-wrong examples |
| [MTBF and MTTR](02-MTBF-and-MTTR.md) | How often things break vs how fast you recover |
| [RTO and RPO](03-RTO-and-RPO.md) | Maximum acceptable downtime vs maximum acceptable data loss |
| [MTTR vs RTO](04-MTTR-RTO.md) | Why fast recovery time and acceptable downtime are related but not identical |
| [Reliability vs Availability](05-Reliability-vs-Availability.md) | Why a reachable system can still be incorrect |
| [Interview Cheatsheet](06-Interview-Cheatsheet.md) | How to use reliability concepts in a design interview |
