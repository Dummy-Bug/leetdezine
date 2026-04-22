# End Goal — LeetDezine

The destination: a system design learning platform that engineers pay for because
it's the best resource for interview depth anywhere on the internet.

---

## North Star Design (Claude Design mockup — April 2026)

> Save the 6 screenshots to `design-mockups/` to see them rendered below.

| Screen | What it shows |
|--------|--------------|
| ![Homepage](design-mockups/01-homepage.png) | Dark theme, teal accent, "Design systems you could actually build." hero, stats strip |
| ![Pathways](design-mockups/02-pathways.png) | Three tracks — Apprentice / Builder / Architect with content preview cards |
| ![Subway Map](design-mockups/03-subway-map.png) | Progress tracker — completed / in-progress / locked nodes, subway map layout |
| ![Interview Mode Theory](design-mockups/04-interview-mode-theory.png) | Theory / Split / Interview toggle — default theory view |
| ![Interview Mode Split](design-mockups/05-interview-mode-split.png) | Split view — theory on left, interview questions + signal rubrics + company tags on right |
| ![Coming Soon](design-mockups/06-coming-soon.png) | Expansion tracks — DDIA, DB Internals, ML Systems Design |

**Key features to build when traction hits:**
- Three learning tracks scoped by experience level
- Subway map progress with completed / in-progress / locked states
- Interview Mode toggle — same content reframed as FAANG interview questions (paid feature)
- Signal rubrics + company tags (Meta / Amazon / Stripe / Uber) per concept
- Expansion tracks: DDIA, DB Internals, ML Systems Design

---

## Sub-Goal 1 — Ship a site worth reading

- [ ] Fix the nav (section-scoped sidebar, full deep tree) — in progress
- [ ] Every concept section has a complete, readable flow start to finish
- [ ] Every case study has the full arc: requirements → deep dives → final design
- [ ] Previous / Next navigation works on every page
- [ ] Site title and SEO metadata correct

**Done when:** A stranger can land on any page, orient themselves immediately, and
read through an entire case study without hitting a dead end.

---

## Sub-Goal 2 — Build a content engine

- [ ] Twitter/X: posting 3-4x per week consistently
- [ ] Peerlist: posting 2-3x per week
- [ ] Dev.to: one blog post per week combining 3-4 topics
- [ ] Each post ends with a link back to the site
- [ ] UTM tracking on all links so we know what drives traffic

**Done when:** Content is on autopilot — new case study ships → content batch
generates → posts go out over the next 2 weeks.

---

## Sub-Goal 3 — Get discovered

- [ ] Google indexing all pages (Search Console set up, sitemap submitted)
- [ ] Ranking for at least 10 long-tail queries ("url shortener system design deep dive", etc.)
- [ ] 500+ monthly organic visitors from search
- [ ] At least one piece of content goes semi-viral (500+ impressions on a single post)

**Done when:** Traffic comes in without posting. People find the site by searching,
not just from social links.

---

## Sub-Goal 4 — Build an audience

- [ ] 500 Twitter/X followers who are engineers or engineering students
- [ ] 200 Peerlist followers
- [ ] Email list with 200+ subscribers (add a newsletter signup to the site)
- [ ] At least 5 people have shared or quoted a piece of content organically

**Done when:** When you post something, people actually see it without paid reach.

---

## Sub-Goal 5 — Become the reference, not just another resource

- [ ] Cover every major system design topic (all 10 concept sections complete)
- [ ] Cover every canonical interview case study (Unique ID, URL Shortener,
  Notification, Pastebin, Rate Limiter, KV Store, WhatsApp, Web Crawler, Twitter Feed)
- [ ] DDIA-level depth on database internals (B+ trees, LSM trees, MVCC, WAL)
- [ ] Engineers are linking to specific pages as references in Discord/Slack/Reddit
- [ ] Site is mentioned in "best system design resources" threads

**Done when:** LeetDezine is the answer people give when asked "where do I study
system design seriously?"

---

## Sub-Goal 6 — Ship the PWA

- [ ] Site installable as a PWA (offline reading, home screen icon)
- [ ] Works well on mobile (readable, no broken layouts)
- [ ] Progress tracking per case study ("3 of 8 pages read")
- [ ] Bookmarks / save for later

**Done when:** Reading on phone feels as good as reading on desktop.

---

## Sub-Goal 7 — Prove people will pay

- [ ] Launch a "Pro" tier concept (advanced content, practice questions, mock answers)
- [ ] Add SDE-1 / SDE-2 / Senior interview question sets behind a paywall
- [ ] Or: premium case studies (Twitter Feed, YouTube, Uber) not available for free
- [ ] Run a waitlist / early access campaign
- [ ] 50 people sign up for the waitlist without paid promotion

**Done when:** There is clear evidence that people want to pay before you build
the payment infrastructure.

---

## Sub-Goal 8 — First revenue

- [ ] Stripe or Lemon Squeezy integrated
- [ ] First paid plan live ($9/month or $79/year — rough target)
- [ ] First 10 paying customers
- [ ] MRR covers hosting costs (currently $0 — Cloudflare Pages is free)

**Done when:** The site makes its first dollar.

---

## The Final Goal — Enough traction to ask for money at scale

**Target state:**
- 5,000+ monthly active readers
- 500+ email subscribers
- $500+ MRR from early adopters
- Clear demand signal for a native app or expanded content library

At this point you have proof: real engineers are reading, some are paying, and
the content is worth building a proper product around. This is when you either
raise a small round, launch a Kickstarter-style campaign, or go full-time on it.

---

## Current Position

Finishing Sub-Goal 1. Everything else follows from here.
