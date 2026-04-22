# Load Balancing — Overview

> A load balancer is what makes horizontal scaling actually work — without it, adding servers solves nothing.

> [!abstract] Once you have multiple servers, something needs to decide which server handles each request. This folder covers how load balancers work, how they pick servers, and the difference between routing at the network layer (L4) vs the application layer (L7) — with full end-to-end walkthroughs for both.

---

## Files in this folder

| File | Topic |
|---|---|
| [Load Balancing](01-Load-Balancing.md) | What it is, health checks, SPOF problem, auto-scaling |
| [Algorithms](02-Algorithms.md) | Round robin, least connections, IP hashing, weighted |
| [L4](03-L4/00-Overview.md) | Layer 4 — OSI model, NAT, connection tables, and real world examples |
| [L7](04-L7/00-Overview.md) | Layer 7 — SSL termination, URL routing, API Gateway, and request-aware routing |
| [Hybrid In Production](05-Hybrid-In-Production.md) | How L4, L7, and API Gateway work together in production |
| [Interview Cheatsheet](06-Interview-Cheatsheet.md) | Algorithm choice, L4 vs L7, SPOF fix, API Gateway decision, three-layer architecture |
