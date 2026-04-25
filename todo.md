# URL Flattening — Migration Plan

## Goal

Remove the intermediate sub-folder level from every concept URL on leetdezine.com.

Current (3 levels deep):
```
/event-driven-patterns/cdc/what-is-cdc/
/event-driven-patterns/inbox-outbox-together/what-is-inbox-pattern/
/caching/cache-invalidation/ttl-based/
/caching/distributed-caching/consistent-hashing/
/storage-and-databases/acid/atomicity/
```

Target (2 levels deep):
```
/event-driven-patterns/what-is-cdc/
/event-driven-patterns/what-is-inbox-pattern/
/caching/ttl-based/
/caching/consistent-hashing/
/storage-and-databases/atomicity/
```

Why: The sub-folder (`cdc/`, `inbox-outbox-together/`, `cache-invalidation/`) is purely organizational — it exists to group files on disk, not to convey meaning to Google. It adds a URL level that dilutes keyword proximity to the domain root without giving any topical authority signal that the top-level folder doesn't already provide. The top-level folder (`event-driven-patterns/`, `caching/`) is enough for topical clustering. Site is 3 days old — zero indexed equity to lose.

---

## Affected Sections

These sections have the extra sub-folder level that needs to be removed:

| Section folder | Sub-folders to flatten |
|---|---|
| `caching/` | `cache-invalidation/`, `cache-problems/`, `distributed-caching/`, `eviction-policies/`, `population-strategies/`, `redis/`, `writing-strategies/`, `interview-questions/` |
| `event-driven-patterns/` | `cdc/`, `cqrs/`, `inbox-outbox-together/`, `outbox-pattern/`, `what-is-event-sourcing/` |
| `storage-and-databases/` | `acid/`, `cdc/`, `connection-pooling/`, `fundamentals/`, `indexing/`, `pagination/`, `read-write-splitting/`, `sql/` |
| `database-types/` | `blob-storage/`, `choosing-the-right-db/`, `column-family/`, `data-modeling/`, `document-stores/`, `graph-databases/`, `key-value-stores/`, `newsql/`, `oltp-vs-olap/`, `search-engines/` |
| `distributed-systems/` | `cap-theorem/`, `consensus/`, `consistency-models/`, `coordination-services/`, `crdts/`, `distributed-clocks/`, `failure-detection/`, `merkle-trees/`, `network-partitions/`, `pacelc/`, `problems/`, `replication/`, `sharding/` |
| `event-broker/` | `advanced/`, `architecture/`, `backpressure/`, `consumer/`, `kafka-vs-sqs-vs-rabbitmq/`, `producer/` |
| `messaging/` | `fundamentals/`, `rabbitmq/`, `sqs/` |
| `data-processing/` | `batch-processing/`, `lambda-kappa/`, `schema-evolution/`, `stream-processing/` |
| `scalability/` | `auto-scaling/`, `load-balancing/` |
| `availability/` | `interview-questions/` |
| `performance-metrics/` | `interview-questions/` |
| `reliability/` | `interview-questions/` |
| `service-levels/` | `interview-questions/` |

Sections that are already flat (no change needed):
- `concurrency-locking/` — all files are directly in root
- `back-of-envelope/` — all files are directly in root
- `fundamentals/` — all files are directly in root
- `nfrs/`, `durability/`, `fault-tolerance/`, `security/`, `state-machines/` — flat already
- Case studies: `rate-limiter/`, `url-shortener/`, `unique-id-generator/`, `notification-system/`, `pastebin/`, `kv-store/`, `netflix/`, `whatsapp/` — these have `deep-dives/` sub-folder which is intentional and meaningful, leave untouched

---

## Collision Risk

When flattening sub-folders, filenames from different sub-folders may clash.

Example:
- `caching/cache-invalidation/interview-cheatsheet.md`
- `caching/eviction-policies/interview-cheatsheet.md`
- `caching/distributed-caching/interview-cheatsheet.md`

These would all become `caching/interview-cheatsheet.md` — collision.

Resolution rule: prefix the filename with the sub-folder name when collision exists.
- `caching/cache-invalidation-interview-cheatsheet.md`
- `caching/eviction-policies-interview-cheatsheet.md`
- `caching/distributed-caching-interview-cheatsheet.md`

Step 2.3 below is specifically for detecting these before touching files.

---

## Phase 0 — Baseline (15 min)

### 0.1 Confirm current build is clean

- [ ] `cd /Users/home/Desktop/github && source .venv/bin/activate && mkdocs build --strict`
- [ ] Record any existing warnings so they are not confused with migration regressions
- [ ] Confirm `site/` was generated successfully

### 0.2 Save a copy of the current mkdocs.yml

- [ ] `cp mkdocs.yml mkdocs.yml.bak`
- [ ] This is the rollback reference — do not delete until migration is verified live

---

## Phase 1 — Detect collisions (30 min)

### 1.1 Generate filename inventory per section

For each affected section folder, list all filenames across all sub-folders:

- [ ] `find docs/caching -name "*.md" | xargs -I{} basename {} | sort | uniq -d`
- [ ] Repeat for `docs/event-driven-patterns/`, `docs/storage-and-databases/`, `docs/database-types/`, `docs/distributed-systems/`, `docs/event-broker/`, `docs/messaging/`, `docs/data-processing/`

### 1.2 Document every collision

- [ ] Create `/tmp/collisions.txt`
- [ ] For each colliding filename, write: `section | filename | sub-folders it appears in | resolved new name`
- [ ] Apply the resolution rule: prefix with sub-folder name, e.g. `cache-invalidation-interview-cheatsheet.md`

### 1.3 Verify resolved names are unique

- [ ] Re-check each resolved name does not itself clash with another file in the section
- [ ] Sign off on the full collision list before moving any files

---

## Phase 2 — Build the path map (30 min)

### 2.1 Generate full old→new path mapping

- [ ] `find docs -name "*.md" | grep -v "whatsapp\|rate-limiter\|url-shortener\|unique-id-generator\|notification-system\|pastebin\|kv-store\|netflix" | sort > /tmp/old-paths.txt`
- [ ] For each path in the affected sections, write the new path:
  - Rule: `docs/[section]/[sub-folder]/[file].md` → `docs/[section]/[file].md`
  - Exception: collision-resolved files use prefixed names from Phase 1
  - Exception: `index.md` inside sub-folders maps to `[sub-folder-name].md` in parent, or is dropped if redundant

### 2.2 Clarify what happens to sub-folder index.md files

- [ ] For each sub-folder that has its own `index.md`: decide whether it becomes a standalone page or gets merged into the parent section index
- [ ] Write the decision for each one in `/tmp/index-decisions.txt`
- [ ] Default rule: if the sub-folder index just lists child pages, drop it; if it has real content, rename it to `[sub-folder].md` in the parent

### 2.3 Review the full path map

- [ ] Open `/tmp/old-paths.txt` alongside proposed new paths
- [ ] Spot-check 20 random entries for correctness
- [ ] Confirm no two new paths are identical
- [ ] Sign off before touching any files

---

## Phase 3 — Pilot: event-driven-patterns (1 hour)

Smallest section with multiple sub-folders. Migrate this first.

### 3.1 Move files

- [ ] `mv docs/event-driven-patterns/cdc/what-is-cdc.md docs/event-driven-patterns/what-is-cdc.md`
- [ ] `mv docs/event-driven-patterns/cdc/debezium.md docs/event-driven-patterns/debezium.md`
- [ ] `mv docs/event-driven-patterns/cdc/outbox-pattern.md docs/event-driven-patterns/outbox-pattern.md` (check for name clash with `outbox-pattern/` folder first)
- [ ] Repeat for all files in `cqrs/`, `inbox-outbox-together/`, `outbox-pattern/`, `what-is-event-sourcing/`
- [ ] Apply collision-resolved names where flagged in Phase 1
- [ ] `rmdir` each emptied sub-folder after confirming it is empty

### 3.2 Update internal links

- [ ] `grep -r "event-driven-patterns/cdc/" docs/ --include="*.md" -l`
- [ ] `grep -r "event-driven-patterns/cqrs/" docs/ --include="*.md" -l`
- [ ] `grep -r "event-driven-patterns/inbox-outbox-together/" docs/ --include="*.md" -l`
- [ ] `grep -r "event-driven-patterns/outbox-pattern/" docs/ --include="*.md" -l`
- [ ] Update every reference found to the new flat paths
- [ ] Re-grep to confirm zero old sub-folder paths remain for this section

### 3.3 Update mkdocs.yml

- [ ] Find the `event-driven-patterns` section in `nav:`
- [ ] Remove the sub-folder grouping level — items that were indented under `- CDC:` now live directly under `- Event-Driven Patterns:`
- [ ] Update every file path to the new flat path
- [ ] Validate YAML is syntactically correct after edits

### 3.4 Verify pilot locally

- [ ] `mkdocs serve`
- [ ] Open `http://localhost:8000/event-driven-patterns/what-is-cdc/`
- [ ] Open `http://localhost:8000/event-driven-patterns/what-is-inbox-pattern/`
- [ ] Click through every page in the Event-Driven Patterns sidebar
- [ ] Confirm breadcrumbs are correct
- [ ] Confirm zero 404s
- [ ] Fix any issues before proceeding to Phase 4

---

## Phase 4 — Migrate remaining sections (3-4 hours)

Work one section at a time. For each section: move files → update links → update mkdocs.yml → local build check → manual review → next section.

### 4.1 caching/

- [ ] Move all files from 8 sub-folders into `docs/caching/` with collision-resolved names
- [ ] Update internal links across all of `docs/`
- [ ] Update `nav:` in mkdocs.yml for the caching section
- [ ] `mkdocs serve` + spot-check 5 caching pages
- [ ] Manual review of moved files and nav diff

### 4.2 storage-and-databases/

- [ ] Move all files from 8 sub-folders into `docs/storage-and-databases/`
- [ ] Update internal links
- [ ] Update nav
- [ ] `mkdocs serve` + spot-check
- [ ] Manual review

### 4.3 database-types/

- [ ] Move all files from 10 sub-folders into `docs/database-types/`
- [ ] Update internal links
- [ ] Update nav
- [ ] `mkdocs serve` + spot-check
- [ ] Manual review

### 4.4 distributed-systems/

- [ ] Move all files from 13 sub-folders into `docs/distributed-systems/`
- [ ] Update internal links — this section likely has many cross-links to other sections, check carefully
- [ ] Update nav
- [ ] `mkdocs serve` + spot-check
- [ ] Manual review

### 4.5 event-broker/

- [ ] Move all files from 6 sub-folders into `docs/event-broker/`
- [ ] Update internal links
- [ ] Update nav
- [ ] `mkdocs serve` + spot-check
- [ ] Manual review

### 4.6 messaging/

- [ ] Move all files from 3 sub-folders into `docs/messaging/`
- [ ] Update internal links
- [ ] Update nav
- [ ] `mkdocs serve` + spot-check
- [ ] Manual review

### 4.7 data-processing/

- [ ] Move all files from 4 sub-folders into `docs/data-processing/`
- [ ] Note: `batch-processing/mapreduce/` and `batch-processing/spark/` are 3 levels deep — flatten to `data-processing/mapreduce-*.md` and `data-processing/spark-*.md`
- [ ] Update internal links
- [ ] Update nav
- [ ] `mkdocs serve` + spot-check
- [ ] Manual review

### 4.8 scalability/, availability/, performance-metrics/, reliability/, service-levels/

- [ ] These have only `interview-questions/` sub-folders — small lift
- [ ] Move interview question files up one level, applying collision names if needed
- [ ] Update nav
- [ ] `mkdocs serve` check

---

## Phase 5 — Final verification (30 min)

### 5.1 Strict build

- [ ] `mkdocs build --strict`
- [ ] Zero warnings allowed before deploy
- [ ] Fix any remaining broken links or missing files

### 5.2 Link crawl

- [ ] `pip install linkchecker` (inside .venv)
- [ ] `mkdocs serve &` then `linkchecker http://localhost:8000`
- [ ] Record every 404 or broken anchor
- [ ] Fix all issues
- [ ] Re-run until clean

### 5.3 Sitemap check

- [ ] Open `site/sitemap.xml`
- [ ] Confirm zero old 3-level URLs appear
- [ ] Confirm all URLs are 2-level (section/page)
- [ ] Confirm total URL count is reasonable (should be close to file count)

### 5.4 Manual review gate

- [ ] Diff `mkdocs.yml` against `mkdocs.yml.bak` and read through fully
- [ ] Open 10 random pages in the local build and verify content, breadcrumbs, and sidebar
- [ ] Confirm the site looks and functions correctly before signaling ready for deploy

---

## Phase 6 — Deploy (15 min + monitoring)

### 6.1 Deploy

- [ ] `git add` and commit (user performs this manually per project workflow)
- [ ] Push to `master` — Cloudflare Pages auto-deploys
- [ ] Wait for Cloudflare build to complete
- [ ] Open production and verify 5 new-format URLs load correctly

### 6.2 Search Console

- [ ] Open Google Search Console
- [ ] Sitemaps → resubmit `https://leetdezine.com/sitemap.xml`
- [ ] URL Inspection → request reindexing for top pages at their new URLs

### 6.3 Monitor

- [ ] Week 1: check for unexpected 404s in Search Console coverage report
- [ ] Week 2: confirm new URLs start appearing in impressions
- [ ] If anything stalls by week 3, check `robots.txt` and canonical tags

---

## Rollback

If something breaks after deploy:
- [ ] `cp mkdocs.yml.bak mkdocs.yml`
- [ ] Restore moved files from git history: `git checkout HEAD~1 -- docs/`
- [ ] Push the revert
- [ ] Redeploy and verify

---

## Time Estimate

| Phase | Time |
|---|---|
| Phase 0 — Baseline | 15 min |
| Phase 1 — Collision detection | 30 min |
| Phase 2 — Path map | 30 min |
| Phase 3 — Pilot | 1 hour |
| Phase 4 — All sections | 3-4 hours |
| Phase 5 — Verification | 30 min |
| Phase 6 — Deploy | 15 min |
| **Total** | **~6-7 hours** |
