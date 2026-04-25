# URL Restructure — Migration Plan

## Goal

Migrate every URL on leetdezine.com from this:
```text
/03-Case-Studies/03-Expedition/01-Rate-Limiter/02-Deep-Dives/02-Distributed-Rate-Limiting/01-Atomicity-Problem/
```
To this:
```text
/rate-limiter/atomicity-problem/
```

Why: Google reads URL paths as keywords. Numeric prefixes are noise. 6-level nesting buries content. Topic-only URLs rank better.

## Scope

- 835 markdown files in `docs/`
- Manual `nav:` defined in `mkdocs.yml` means sidebar order is controlled by config, not folder names
- Empty scaffolded folders (`docs/case-studies/`, `docs/concepts/`) from an abandoned attempt should be removed first
- No redirects planned because the site is still very new and reindexing clean URLs is likely the better trade
- All code-generated edits should be manually reviewed before any manual git action

---

## Phase 0 — Decisions and Baseline (do this first, 30 min)

### 0.1 Pick the URL strategy

Choose between:

**A. Flat, topic-only** *(recommended)*
```text
/rate-limiter/atomicity-problem/
/url-shortener/hot-key-problem/
/caching/cache-aside/
```

**B. Section-prefixed**
```text
/case-studies/rate-limiter/atomicity-problem/
/concepts/caching/cache-aside/
```

Decision: ____________

Recommendation: **A**. Tier names like Foundation or Expedition are LeetDezine-specific framing. They belong in navigation or page UI, not in the URL.

Substeps:
- [ ] Confirm whether the URL should communicate only topic, or topic plus section
- [ ] Check 10-15 representative pages across concepts and case studies
- [ ] Verify the chosen scheme works for both overview pages and deep-dive pages
- [ ] Note any exceptions that may require one extra folder level
- [ ] Write the final strategy decision at the top of this file

### 0.2 Record the current site baseline

Substeps:
- [ ] Run `mkdocs serve` once before changing anything
- [ ] Confirm the local site builds successfully
- [ ] Note any existing warnings so they are not confused with migration regressions
- [ ] Open the homepage and at least 3 deep pages to confirm the current site works
- [ ] Take screenshots of the current sidebar and one representative case-study page
- [ ] Save a copy of the current `mkdocs.yml` for side-by-side review during migration

### 0.3 Define manual review checkpoints

Substeps:
- [ ] Decide when manual review happens: after pilot, after each batch, and before deploy
- [ ] Decide what must be reviewed each time: file moves, internal links, nav paths, and built pages
- [ ] Decide who signs off on production deployment after local verification

---

## Phase 1 — Cleanup (15 min)

### 1.1 Verify the scaffold folders are truly empty

Substeps:
- [ ] Inspect `docs/case-studies/`
- [ ] Inspect `docs/concepts/`
- [ ] Confirm they contain no markdown files
- [ ] Confirm they are not referenced in `mkdocs.yml`
- [ ] Confirm they are not referenced by internal links elsewhere in `docs/`

### 1.2 Remove the abandoned scaffolds

Substeps:
- [ ] Delete `docs/case-studies/`
- [ ] Delete `docs/concepts/`
- [ ] Re-scan `docs/` to confirm no real content was removed
- [ ] Review the deletion set manually before moving on

---

## Phase 2 — Map old paths to new paths (1 hour)

### 2.1 Generate the full current path inventory

Substeps:
- [ ] Run `find docs -name "*.md" | sort > /tmp/old-paths.txt`
- [ ] Open `/tmp/old-paths.txt`
- [ ] Confirm every expected content area appears in the list
- [ ] Mark overview pages like `index.md`
- [ ] Mark folders with many deep-dive pages

### 2.2 Define the transformation rules in writing

Renaming rules:
1. Drop all numeric prefixes (`03-`, `01-`, `02-` -> gone)
2. Lowercase everything
3. Keep hyphens because they are already SEO-friendly
4. Flatten structural folders like `Case-Studies` and `Deep-Dives`
5. Drop tier folders like `Foundation` and `Expedition` if Strategy A is chosen

Substeps:
- [ ] Validate each rule against real examples from concepts, case studies, and estimation sections
- [ ] Confirm how `index.md` pages map under the new structure
- [ ] Confirm whether SDE grouping folders stay in navigation only or also appear in URLs
- [ ] Confirm whether shared topics need a parent folder to avoid ambiguity

Example transformations:
```text
docs/03-Case-Studies/03-Expedition/01-Rate-Limiter/index.md
  -> docs/rate-limiter/index.md

docs/03-Case-Studies/03-Expedition/01-Rate-Limiter/02-Deep-Dives/02-Distributed-Rate-Limiting/01-Atomicity-Problem.md
  -> docs/rate-limiter/atomicity-problem.md

docs/01-Concepts/02-Fundamentals/01-Performance-Metrics/04-Latency-vs-Throughput.md
  -> docs/performance-metrics/latency-vs-throughput.md
```

### 2.3 Create the master path map

Substeps:
- [ ] Create `/tmp/path-map.csv` with columns `old_path,new_path`
- [ ] Fill in one row for every markdown file
- [ ] Keep overview pages and content pages in the same map
- [ ] Keep temporary notes for edge cases beside the CSV if needed
- [ ] Review 20 random mappings manually for consistency

### 2.4 Check for collisions and weak slugs

Substeps:
- [ ] Identify any duplicate `new_path` values
- [ ] Identify any slugs that are too generic, like `introduction` or `overview`
- [ ] Resolve collisions by keeping one parent folder where needed
- [ ] Update the CSV after each resolution
- [ ] Review the final map once before touching any real files

---

## Phase 3 — Pilot migration (2 hours)

Migrate one case study end-to-end before touching the rest.

**Pilot:** `Rate-Limiter`

### 3.1 Prepare the pilot move plan

Substeps:
- [ ] List every file currently under `docs/03-Case-Studies/03-Expedition/01-Rate-Limiter/`
- [ ] Match each file to its destination in the path map
- [ ] Confirm whether any shared assets or includes are referenced from outside the folder
- [ ] Confirm the pilot has at least one overview page and multiple deep pages

### 3.2 Rename and relocate the pilot files

Substeps:
- [ ] Create `docs/rate-limiter/` if it does not already exist
- [ ] Move the overview page to `docs/rate-limiter/index.md`
- [ ] Move each deep-dive page into the new folder
- [ ] Strip numeric prefixes from every moved filename
- [ ] Lowercase every moved filename and folder name
- [ ] Remove empty source folders after confirming all files moved correctly

### 3.3 Update internal links for the pilot

Substeps:
- [ ] Search `docs/` for old Rate Limiter paths
- [ ] Update absolute and relative markdown links
- [ ] Update any inline references that mention old folder names
- [ ] Search for old slugs like `Atomicity-Problem` and verify they now point to the new path
- [ ] Re-scan the docs to confirm no old pilot path remains

### 3.4 Update `mkdocs.yml` for the pilot

Substeps:
- [ ] Find the Rate Limiter section in `nav:`
- [ ] Update each path to the new location
- [ ] Check for duplicate references after the path change
- [ ] Check `not_in_nav:` and any plugin config that may contain old paths
- [ ] Review indentation and YAML validity carefully

### 3.5 Verify the pilot locally

Substeps:
- [ ] Run `mkdocs serve`
- [ ] Confirm the build completes cleanly
- [ ] Open `http://localhost:8000/rate-limiter/`
- [ ] Open `http://localhost:8000/rate-limiter/atomicity-problem/`
- [ ] Click through every page in the Rate Limiter sidebar section
- [ ] Confirm there are no 404s, broken assets, or wrong breadcrumbs
- [ ] Compare sidebar order against the baseline screenshots

### 3.6 Manual review gate after pilot

Substeps:
- [ ] Review all moved pilot files manually
- [ ] Review all link updates manually
- [ ] Review the `mkdocs.yml` diff manually
- [ ] Decide whether the naming pattern is good enough to scale
- [ ] If anything feels inconsistent, fix the pattern now before batch migration

---

## Phase 4 — Migrate everything else (3-4 hours)

Now that the pattern is validated, migrate the rest in batches. Review each batch manually before moving to the next one.

### 4.1 Batch 1 — Concepts

Target:
- [ ] `01-Concepts/` -> topic-level folders like `/caching/`, `/messaging/`, `/performance-metrics/`

Substeps:
- [ ] Split the concepts section into logical topic folders
- [ ] Move overview pages first
- [ ] Move child pages next
- [ ] Update all internal links within concepts
- [ ] Update inbound links from case studies or other sections
- [ ] Update the concepts area in `mkdocs.yml`
- [ ] Run `mkdocs serve`
- [ ] Click through a representative sample of concept pages
- [ ] Review the changes manually

### 4.2 Batch 2 — Back-of-envelope estimation

Target:
- [ ] `02-Back-of-Envelope-Estimation/` -> `/back-of-envelope/`

Substeps:
- [ ] List all estimation pages
- [ ] Move them into the new folder structure
- [ ] Normalize filenames and slugs
- [ ] Update internal references
- [ ] Update nav paths in `mkdocs.yml`
- [ ] Run `mkdocs serve`
- [ ] Test the overview page and a few deep pages
- [ ] Review the changes manually

### 4.3 Batch 3 — Foundation case studies

Target:
- [ ] URL Shortener
- [ ] Unique ID Generator

Substeps:
- [ ] Migrate one case study at a time within the batch
- [ ] Move overview pages and deep pages
- [ ] Update all cross-links between case studies and concepts
- [ ] Update nav entries in `mkdocs.yml`
- [ ] Run local build checks after each case study
- [ ] Review the full batch manually before continuing

### 4.4 Batch 4 — Ascent case studies

Target:
- [ ] Notification System
- [ ] Pastebin

Substeps:
- [ ] Repeat the pilot pattern exactly
- [ ] Confirm path naming stays consistent with earlier batches
- [ ] Update all inbound and outbound links
- [ ] Update nav entries
- [ ] Run local checks
- [ ] Review manually

### 4.5 Batch 5 — Summit case studies

Target:
- [ ] KV Store
- [ ] Netflix

Substeps:
- [ ] Move the content based on the path map
- [ ] Verify deeper nested pages carefully because this batch may have more cross-links
- [ ] Update nav entries
- [ ] Run local checks
- [ ] Review manually

### 4.6 Batch 6 — Battleground case studies

Target:
- [ ] WhatsApp

Substeps:
- [ ] Migrate the overview page
- [ ] Migrate all child pages
- [ ] Update links and navigation
- [ ] Run local checks
- [ ] Review manually

### 4.7 Batch 7 — SDE groupings

Decision needed:
- [ ] Decide whether `00-SDE-1/`, `00-SDE-2/`, and `00-SDE-3/` are URL material or only navigation groupings

Substeps:
- [ ] Inspect how these folders are used today
- [ ] Check whether the grouping communicates useful search intent
- [ ] If not, keep them only in nav labels and remove them from URLs
- [ ] Update the path map accordingly
- [ ] Run local checks
- [ ] Review manually

### 4.8 Cross-batch process to repeat every time

For each batch:
1. Update the path map for that batch if anything changed during implementation
2. Move files and folders carefully
3. Update internal markdown links
4. Update `mkdocs.yml`
5. Run `mkdocs serve`
6. Click through representative pages
7. Review the batch manually before starting the next one

### 4.9 Stale folder cleanup

Substeps:
- [ ] After all batches, inspect `docs/01-Concepts/`, `docs/03-Case-Studies/`, and other old roots
- [ ] Confirm they are empty
- [ ] Delete the empty old folders
- [ ] Run `mkdocs build`
- [ ] Confirm the final local build has zero unexpected warnings

---

## Phase 5 — Verification before deploy (30 min)

### 5.1 Strict local verification

Substeps:
- [ ] Run `mkdocs build --strict`
- [ ] Fix every warning before moving on
- [ ] Open the built site locally
- [ ] Click through 10-20 random pages across all sections
- [ ] Check overview pages, deep-dive pages, and cross-links
- [ ] Confirm no page has a stale breadcrumb or stale URL reference

### 5.2 Automated link verification

Substeps:
- [ ] Run `linkchecker` or a similar crawler on the local build
- [ ] Record every 404 or broken anchor
- [ ] Fix each issue
- [ ] Re-run the crawl until the report is clean

### 5.3 Sitemap and production metadata check

Substeps:
- [ ] Open `mkdocs.yml`
- [ ] Confirm `site_url: https://leetdezine.com`
- [ ] Build the site
- [ ] Confirm `sitemap.xml` is generated
- [ ] Confirm the sitemap contains only the new URL structure

### 5.4 Final manual review gate

Substeps:
- [ ] Review the full file move set manually
- [ ] Review the `mkdocs.yml` changes manually
- [ ] Review a sample of updated markdown links manually
- [ ] Confirm the migration is ready for manual deployment steps

---

## Phase 6 — Deploy and monitor (15 min, then occasional checks)

### 6.1 Deploy

Substeps:
- [ ] Perform the manual deployment workflow used by the project
- [ ] Wait for Cloudflare Pages to finish deploying
- [ ] Open the production homepage
- [ ] Open at least 5 new production URLs
- [ ] Confirm they load correctly
- [ ] Confirm expected old URLs now 404

### 6.2 Tell Google about the new structure

Substeps:
- [ ] Open Google Search Console
- [ ] Open the Sitemaps section
- [ ] Resubmit `https://leetdezine.com/sitemap.xml`
- [ ] Open URL Inspection for the top pages currently getting impressions
- [ ] Request reindexing for each page at its new URL

Priority pages:
- [ ] The LWW page for KV Store leaderless replication
- [ ] The fixed window counter page
- [ ] The latency vs throughput page
- [ ] The SQS queue selection page
- [ ] The etcd / key-value store page

### 6.3 Monitor after deployment

Substeps:
- [ ] Week 1: watch Search Console for old URL 404s and confirm they are expected
- [ ] Week 1: verify the sitemap was accepted
- [ ] Week 2: check whether new URLs are being discovered
- [ ] Week 2-3: check whether impressions start shifting to the new URLs
- [ ] If indexing stalls by week 3, manually inspect `robots.txt`, sitemap contents, and canonical tags

---

## Recovery plan

If something breaks badly after deploy:

- [ ] Stop making further migration changes until the issue is understood
- [ ] Identify whether the breakage is in moved files, links, nav config, or deployment config
- [ ] Restore the last known-good project state using the team's normal manual git workflow
- [ ] Redeploy using the normal manual deployment workflow
- [ ] Re-test the affected URLs in production
- [ ] Resume migration only after the failure mode is documented

---

## Estimate

- Phase 0: 30 min
- Phase 1: 15 min
- Phase 2: 1 hour
- Phase 3: 2 hours
- Phase 4: 3-4 hours
- Phase 5: 30 min
- Phase 6: 15 min + light monitoring

Total focused work: ~7-8 hours.

---

## Open questions to resolve before starting

1. URL strategy A or B?
2. Should `00-SDE-1/`, `00-SDE-2/`, and `00-SDE-3/` appear in URLs, or only in navigation?
3. Are there any pages that intentionally need multiple valid URLs?
4. Are there any manually shared external links that should be updated after the migration is live?
