# LeetDezine — Claude Code Workflow

## What This Project Is
System design case studies published at https://leetdezine.com

Case studies live in `docs/` as markdown files, organized by tier (Foundation, Ascent, Battleground, etc.).

## Infrastructure
- **Domain:** leetdezine.com (registered on Namecheap, DNS on Cloudflare)
- **Hosting:** Cloudflare Pages (auto-deploys on every push to `master`)
- **Analytics:** Google Analytics (G-KZPQKH7FSK)
- **Repository:** github.com/Dummy-Bug/leetdezine
- **Deploy:** just `git push` — Cloudflare handles the rest

## Social Presence
- **Twitter/X:** @leetdezine (personal name, LeetDezine banner)
- **Dev.to:** leetdezine
- **Peerlist:** peerlist.io/laxit (personal profile, LeetDezine as project)

## Content Generation Workflow

When the user says **"generate content on [topic]"**:

1. Read all relevant markdown files for that topic from `docs/`
2. Pick the sharpest angle — one insight, one problem, one counterintuitive thing
3. Generate and output directly in chat:
   - **Twitter thread** — 2 tweets max
   - **Peerlist post** — 150-200 words
   - **ASCII diagram** — if the topic has a visual component
4. Save files to `posts/` folder under the relevant case study subfolder
5. User manually copies and pastes to each platform

No API keys. No scripts. No cost beyond Claude Code Pro subscription.

## Content Funnel Strategy

```
Twitter/Peerlist (daily or every 2 days) → Dev.to blog (weekly/bi-weekly) → Website
```

Content is built around **specific topics**, not entire case studies:
- User picks a topic (e.g. "Hot Key Problem", "Consistent Hashing", "Clock Skew")
- Claude finds the relevant docs, picks the sharpest angle
- Every piece of content ends with a link back to `https://leetdezine.com`
- Website is the destination, everything else is a teaser

**Batching strategy for blogs:**
- Post 3-4 short topics on Twitter/Peerlist first
- Then combine related ones into one Dev.to blog post
- Blog title wraps the theme (e.g. "How distributed systems generate IDs at scale")
- Blog links back to full website case study

When user says "generate blog combining [topic1], [topic2], [topic3]" — weave them into one cohesive narrative, don't just concatenate.

## Posts Folder Structure

```
posts/
  01-Unique-Id-Generator/
    01-snowflake-twitter.md
    02-snowflake-peerlist.md
    03-snowflake-diagram.md
```

Naming convention: `[number]-[topic]-[platform].md`

## Distribution Notes

- **Twitter/X** — 2-tweet thread, attach diagram as image, 3 hashtags max
- **Dev.to** — full blog with Mermaid diagrams, free API available for future automation
- **Peerlist** — manual only, no public API
- **Medium** — skip for now, revisit when traction is there

## ⚠️ Title Rule for Dev.to and Peerlist (ALWAYS ENFORCE)

**Every Dev.to article and Peerlist post title MUST be framed as a question someone would actually type into a search engine or AI.**

This is not optional — it's the proven playbook. The UUID article ranked #1 on Perplexity for "why UUID might be killing my database" within 4 days of publishing because the title matched real search intent exactly.

**Wrong:**
- "Understanding Consistent Hashing"
- "Snowflake ID Architecture"
- "How Kafka Works"

**Right:**
- "Why Does Consistent Hashing Actually Work?"
- "What Happens When a Cassandra Node Goes Down?"
- "Why Is Kafka So Fast? The Architecture Behind It"

Before generating any Dev.to or Peerlist title, ask: "Would a real engineer type this exact phrase when they're stuck or curious?" If no — rewrite it.

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

- **Twitter** — clean ASCII diagram as separate block (user screenshots and attaches as image)
- **Peerlist** — same ASCII diagram
- **Dev.to** — Mermaid diagram (rendered natively)

Always generate a diagram where the topic has a visual component (bit layouts, flows, architecture, comparisons).

## Content Length Hierarchy

| Platform | Length | Purpose |
|----------|--------|---------|
| Twitter/X | 2 tweets (280 chars each) | Hook + one key insight |
| Peerlist | 150-200 words | Short story behind the insight |
| Dev.to | 500-800 words | Full deep dive blog post |
| Website | Complete case study | Everything, already published |

## Tone Guidelines

- **Tweets** — Sharp, story-driven. Tweet 1 is the hook, Tweet 2 is the insight + link.
- **Peerlist** — Conversational, peer-to-peer. Expand on the tweet, tell the story briefly.
- **Dev.to** — Technical but readable. Explain the why behind every decision. Headers + bullet points.
- **Website** — Already written in docs/, this is the source of truth.

## Hashtags

Twitter: `#SystemDesign #SoftwareEngineering #DistributedSystems` (max 3, at end of Tweet 1)
