# Snowflake ID — Diagram (screenshot and attach to Twitter + Peerlist)

```
┌─────────────────────────────────────────────────────────────────────┐
│                      SNOWFLAKE ID  —  64 bits                       │
├────┬────────────────────────────────────────┬───────────┬───────────┤
│ 1  │              41 bits                   │  10 bits  │  12 bits  │
│    │            Timestamp                   │ Machine ID│ Sequence  │
│    │       ms since custom epoch            │1024 nodes │ 4096 /ms  │
│sign│           ~69 years                    │           │           │
└────┴────────────────────────────────────────┴───────────┴───────────┘
  │                  │                               │           │
  │                  └── sorts by time automatically │           │
  │                                                  │           │
  └── always 0                        uniqueness ───┘           │
                                  across machines     within ms ─┘
```

Sort by ID = Sort by time. No extra column. No central server. No coordination.
