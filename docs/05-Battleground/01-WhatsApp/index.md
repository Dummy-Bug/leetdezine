# WhatsApp

Design a real-time messaging system at 500M DAU — persistent WebSocket connections, guaranteed message delivery, offline queuing, message ordering, read receipts, and inbox at scale.

---

<div class="grid cards" markdown>

-   **Requirements & Base Architecture**

    ---

    - [Functional Requirements](01-FR.md)
    - [Estimation](02-Estimation.md)
    - [Non-Functional Requirements](03-NFR.md)
    - [API Design](04-API.md)
    - [Real-Time Comms](04-Real-Time-Comms/01-The-Problem.md)
    - [Base Architecture](05-Base-Architecture/01-Overview.md)

-   **Deep Dives**

    ---

    - [Database](06-Deep-Dives/01-DB/01-DB-Choice.md)
    - [Message Ordering](06-Deep-Dives/02-Message-Ordering/01-The-Problem.md)
    - [Offline Delivery](06-Deep-Dives/03-Offline-Delivery/01-The-Problem.md)
    - [Message Status](06-Deep-Dives/04-Message-Status/01-The-Three-Ticks.md)
    - [Inbox](06-Deep-Dives/05-Inbox/01-Inbox-Load-Flow.md)
    - [Caching](06-Deep-Dives/06-Caching/01-Message-History-Cache.md)
    - [Peak Traffic](06-Deep-Dives/07-Peak-Traffic/01-Thundering-Herd/01-Redis-Sharding.md)
    - [Fault Isolation](06-Deep-Dives/XX-Fault-Isolation/01-Connection-Server-Failure/01-Client-Reconnect.md)

-   **Final Design & Observability**

    ---

    - [Final Architecture](07-Final-Design/01-Final-Architecture.md)
    - [SLIs & SLOs](08-Observability/01-SLI-SLO-Connection.md)
    - [Measuring Latency](08-Observability/02-Measuring-Latency.md)
    - [Measuring Availability](08-Observability/03-Measuring-Availability.md)
    - [Alerting](08-Observability/04-Alerting.md)
    - [Error Budget](08-Observability/05-Error-Budget.md)

</div>
