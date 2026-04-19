# LeetDezine — Claude Code Workflow

## What This Project Is
System design case studies published at https://dummy-bug.github.io/leetdezine/

Case studies live in `docs/` as markdown files, organized by tier (Foundation, Ascent, Battleground, etc.).

## Content Generation Workflow

When the user says **"generate content for [case study name]"**:

1. Read all relevant markdown files for that case study from `docs/`
2. Generate and output directly in chat:
   - **Twitter/X thread** — 3-4 tweets, punchy, insight-driven, no fluff
   - **Dev.to blog post** — full deep dive, markdown formatted, with tags
   - **Medium post** — same content, Medium-friendly formatting
   - **Peerlist post** — short, 2-3 paragraphs, community-focused tone
3. User manually copies and pastes to each platform

No API keys. No scripts. No cost beyond Claude Code Pro subscription.

## Content Funnel Strategy

```
Twitter/Peerlist (daily or every 2 days) → Dev.to/Medium blog (weekly/bi-weekly) → Website
```

Content is built around **specific topics**, not entire case studies:
- User picks a topic (e.g. "Hot Key Problem", "Consistent Hashing", "KGS")
- Claude finds the relevant docs, picks the sharpest angle
- Every piece of content ends with a link back to the full case study on the website
- Website is the destination, everything else is a teaser

**Batching strategy for blogs:**
- Post 3-4 short topics on Twitter/Peerlist first
- Then combine related ones into one blog post on Dev.to/Medium
- Blog title wraps the theme (e.g. "How distributed systems generate IDs at scale")
- Blog links back to individual tweets + full website case study

When user says "generate blog combining [topic1], [topic2], [topic3]" — weave them into one cohesive narrative, don't just concatenate.

Website URL: https://dummy-bug.github.io/leetdezine/

## Distribution Notes

- Twitter/X threads — proven, prioritize these
- Dev.to — good SEO value, always publish here
- Peerlist — unverified, test and see
- Medium — unverified, test and see

## Case Study Structure (for reference)

Each case study typically covers:
- Functional & Non-Functional Requirements
- Estimation
- API Design
- Base Architecture
- Deep Dives (DB, Caching, Peak Traffic, Fault Isolation, etc.)
- Observability (SLI/SLO, Alerting, Error Budget)
- Final Design

## Quality Gates (enforced before every output)

Before delivering any content, self-evaluate on these metrics. All must score >8/10 or rewrite:

| Metric | What it means |
|--------|--------------|
| Catchiness | Would someone stop scrolling for this? |
| Readability | Can a tired dev read it in one pass? |
| Human feel | Does it sound like a real person wrote it? |
| Technical accuracy | Is everything correct per the docs? |

**Anti-AI checklist** — never use:
- "Delve", "it's worth noting", "in conclusion", "furthermore"
- Passive voice overload
- Generic openers like "In today's world..."
- Perfect symmetrical bullet points that feel like a listicle
- Overly balanced "on one hand / on the other hand" structure

Write like an opinionated engineer who just solved a hard problem and wants to tell someone about it.

## Diagrams & Visuals

- **Twitter** — include a clean ASCII diagram as a separate block (user screenshots and attaches as image)
- **Peerlist** — same ASCII diagram attached as image
- **Dev.to** — Mermaid diagram (rendered natively)
- **Medium** — describe where a diagram goes, user screenshots from the website or Excalidraw

Always generate a diagram where the topic has a visual component (bit layouts, flows, architecture, comparisons).

## Content Length Hierarchy

From shortest to longest — each platform is a stepping stone to the next:

| Platform | Length | Purpose |
|----------|--------|---------|
| Twitter/X | 1-3 tweets (280 chars each) | Hook, one key insight |
| Peerlist | 150-200 words | Short story behind the insight |
| Dev.to / Medium | 500-800 words | Full deep dive blog post |
| Website | Complete case study | Everything, already published |

## Tone Guidelines for Generated Content

- **Tweets** — One sharp insight or counterintuitive problem. No threads. No "🧵" cringe. Just the hook.
- **Peerlist** — Conversational, peer-to-peer. Expand on the tweet, tell the story briefly.
- **Dev.to / Medium** — Technical but readable. Explain the why behind every decision. Headers + bullet points.
- **Website** — Already written in docs/, this is the source of truth.
