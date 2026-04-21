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

- **Twitter/X** — 2-tweet thread, attach diagram as image, 3 hashtags max. Use `?utm_source=twitter` on all links — Twitter converts URLs to card previews so the raw URL is never visible.
- **Dev.to** — full blog with Mermaid diagrams, free API available for future automation
- **Peerlist** — manual only, no public API
- **Medium** — skip for now, revisit when traction is there

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

## Twitter Hook Rules (critical — bad hooks kill reach)

Tweet 1 must pass this test: **would an engineer stop scrolling for this specific line?**

**The hook must be concrete and specific, not a vague tease.**

Bad (generic, conveys nothing):
> "One viral tweet can take down your URL shortener."

Good (specific, implies knowledge, creates curiosity):
> "Consistent hashing maps every short code to exactly one Redis node. That's also why one viral link can melt your cache."

Rules:
- Open with a technical fact, not a dramatic claim
- The reader should learn something just from Tweet 1, even if they don't click
- Tweet 2 delivers the counterintuitive fix or insight
- No "here's why 🧵" — just say the thing
- Hashtags at the end of Tweet 1, never mid-sentence

## Hashtags

Twitter: `#SystemDesign #SoftwareEngineering #DistributedSystems` (max 3, at end of Tweet 1)
