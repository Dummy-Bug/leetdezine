# LeetDezine — Action Plan

## Product Positioning (north star)
> Don't sell "system design notes."
> Sell this: Most candidates memorize diagrams. LeetDezine teaches the reasoning chain — requirements, estimates, tradeoffs, failure modes, and observability.
> The missing step: make the user feel "This is a guided path that will get me interview-ready."



## Site Basics
- [x] Fix empty `site_name` in `mkdocs.yml` (currently `""`)
- [x] Fix empty title in `docs/index.md`
- [x] Add OG image / social preview metadata
- [x] Add `robots.txt` and verify sitemap in Google Search Console
- [ ] Add `README.md` with local setup and product intent
- [ ] Decide whether `site/` should be committed or generated only
- [ ] Verify Cloudflare build command is documented

## Navigation
- [x] Add `Concepts` top-level section to nav with:
  - [x] Core Concepts
  - [x] Caching
  - [x] Storage & Databases
  - [x] Back-of-Envelope Estimation
- [x] Create `Concepts/index.md` overview page

## Pages
- [ ] Create "Start Here" page with interview-goal-based paths:
  - "Getting in" path (Foundation + Ascent)
  - "Leveling up" path (Expedition + Summit + Battleground)
  - "Deep mastery" path (Concepts + Cheatsheets + Observability)
- [ ] Rework homepage around:
  - Who it is for
  - What outcome it gives
  - What is inside
  - Sample case studies
  - "Start Here" CTA

## Distribution
- [ ] Use UTM parameters on all social links (deferred — do after 10 real users)
- [ ] Post Twitter/Peerlist content consistently to drive traffic

## Monetization (deferred — free for all now)
- [ ] Define paid tiers by interview goal (not years of experience):
  - Free: all current content
  - Paid Starter: cheatsheets + interview questions bundle
  - Full Product: roadmap + all case studies + mock interviews
- [ ] Validate demand with lead magnet first (Back-of-Envelope Cheatsheet)
