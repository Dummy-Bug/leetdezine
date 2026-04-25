# SEO Improvement — Execution Plan

## Goal

Improve search presentation and crawl clarity for leetdezine.com without changing the site structure again.

Primary focus:
- page-specific meta descriptions
- clean head tags without duplicate social metadata
- stronger structured data for content pages
- better image/snippet directives for Google

---

## Phase 0 — Baseline

- [x] Confirm current strict build status
- [x] Inspect generated page head output for duplicate `og:*` / Twitter tags
- [x] Confirm canonical tags already exist before changing anything

---

## Phase 1 — Clean the HTML head

- [x] Remove custom duplicate Open Graph / Twitter tags from `overrides/main.html`
- [x] Keep custom `<title>` behavior
- [x] Add `{{ super() }}` in `extrahead` so Material keeps canonical and theme/social output
- [x] Add a robots directive for richer previews: `max-image-preview:large`
- [x] Rebuild and confirm only one `og:title`, `og:description`, `twitter:title`, and `twitter:description` remain per page

---

## Phase 2 — Generate page-specific fallback descriptions

- [x] Add a hook that derives a description from Markdown content when frontmatter `description:` is missing
- [x] Preserve existing hand-written descriptions and only fill gaps
- [x] Normalize the generated summary so it is clean, single-line, and snippet-sized
- [x] Rebuild and inspect a few pages that previously used the generic site description

---

## Phase 3 — Add structured data

- [x] Keep existing `BreadcrumbList` schema
- [x] Add `BlogPosting` / `Article` schema for leaf content pages
- [x] Add `WebPage` schema for section index pages
- [x] Add `WebSite` + `Organization` schema for the homepage / site identity
- [x] Include title, description, canonical URL, image, and published / modified dates where available
- [x] Rebuild and inspect generated JSON-LD on representative pages

---

## Phase 4 — Verification

- [x] Run `source .venv/bin/activate && mkdocs build --strict`
- [x] Inspect generated HTML for:
  - [x] canonical present
  - [x] no duplicate social tags
  - [x] page-specific meta description on pages missing frontmatter description before
  - [x] JSON-LD emitted for representative leaf and index pages
- [x] Spot-check representative pages:
  - [x] `/caching/quick-decision-map/`
  - [x] `/event-broker/why-kafka-exists/`
  - [x] `/distributed-systems/what-is-consensus/`
  - [x] `/event-driven-patterns/what-is-cdc/`

---

## Done When

- [x] strict build passes
- [x] duplicate social tags are removed
- [x] generic description fallback is no longer used for most content pages without frontmatter descriptions
- [x] structured data is present and page-specific
