

## 2026-08-03 — Health check (delta, automated)

Audit: 10 articles read (all modified today 2026-08-03) + 5 random.
Auto-fixed:
- frontmatter: 8 files backfilled with updated: 2026-08-03

Pending judgement:
- external URLs: skipped (Cloudflare timeouts on URL validation)

---
created: 2026-07-26
---

# CHANGELOG

## 2026-08-02 — INDEX Rebuild

**Trigger:** Complete vault health check.
**Action:** Full INDEX.md rebuild — 872 notes categorized into 14 sections. Previous INDEX had ~7 entries (corrupted during prior patch attempt).
**Categories:** Conceptual Atomics (429), Context & CALCULATE (51), Date & Time (73), Math & Trig (54), Statistical (63), Text (25), Table Manipulation (39), Financial (54), Bitwise (5), Information (56), Relationships & Data Modeling (1), Debugging & Evaluation (8), Governance & Metadata (5), AI & Advanced Analytics (9).
**Also fixed:** || patch artifacts, em-dash bullet violations, 5 missing INDEX.md files (Power BI, Power Query, Excel, Data Modeling, VBA).

## 2026-07-29 — DAX for Humans (Greg Deckler, Packt 2025)

**Source:** DAX for Humans.epub — Greg Deckler, Packt Publishing, September 2025
**KB:** DAX Code
**Notes:** 64 written (1 source + 63 extracted); 21 chapters; 806K source chars; 146 DAX formulas extracted across 62 sections
**Novel content:** CALCUHATE philosophy (Banana Pattern, No CALCULATE first), 15 novel KPI patterns not in Microsoft Learn (ETR, NPS, LTV, Churn, Bradford, Kaplan-Meier, Gini, HCVA, Burndown, EVM, OTIF, OEE, MTTR/MTBF, DOS, FIFO), spatial trigonometry suite (ATAN2, Haversine, Bearing, Nearest Point, Transitive Closure), SVG star ratings, Levenshtein fuzzy matching, multi-column aggregation

**New to KB:** absenteeism, reverse-ytd, modified-dietz-return, compound-interest, market-basket-analysis, delivery-date-accuracy, fifo, order-fulfillment, cartesian-to-polar, box-size-optimization

## 2026-07-29 — Forensic Health Check

**Trigger:** User requested forensic health check — suspected prior ingestion left phantom archives.

**Finding:** dax.pdf (2026-07-26) and m-code.pdf (2026-07-27) showed as "archived" in _INGESTED.md but files were still in inbox. Registry was updated; shutil.move never ran. Also: 1,278 notes (503 dax.pdf + 775 m-code.pdf) not registered in NewNotesTracker.md; dax-source-note missing from INDEX.

**Remediated:**
- Moved dax.pdf, m-code.pdf, DAX for Humans.epub → InboxArchive/2026-07/
- Registered 503 dax.pdf notes + 775 m-code.pdf notes in NewNotesTracker.md
- Added dax-source-note + DAX Reference Functions section to DAX Code INDEX
- Frontmatter quality verified: clean across both KBs

## 2026-07-27 — Ingestion batch (25 files)

Sources: 25 files archived → 99.System/InboxArchive/2026-07/
Notes: 57 written
Highlights: TREATAS (function + comparison + dynamic segmentation), EARLIER (function + gotcha), VAR, Measure Branching, Time Intelligence (YTD + SAMEPERIODLASTYEAR vs PARALLELPERIOD), Measure Library Architecture + Naming Conventions, DAX UDF/Lambda syntax, Performance anti-patterns (5,000-measure analysis), 5 Senior Analyst Patterns (Measure Branching, Defensive DAX, Context Isolation, SSOT, Validation Loop), Dynamic Top N Ranking, Iterator Fundamentals

## 2026-07-26 — PDF extraction (dax.pdf)

Sources: 1 file archived → 99.System/InboxArchive/2026-07/
Notes: 71 written (62 extracted + 1 source + 8 subagent-written)
Notes: dax.pdf extracted via pdfplumber. 299+ DAX functions across 71 notes. Covers: aggregators, iterators, time intelligence, filters, relationships, CALCULATE, context functions, table functions, and more.

## 2026-07-26 — Ingestion batch (batch 2)

Sources: 25 files archived → 99.System/InboxArchive/2026-07/ (second session of the day)
Notes: ~30 written across multiple KBs
Notes: Mixed article ingestion — DAX, Data Modeling, Power BI, Power Query articles. Key additions include: ALL/ALLEXCEPT/ALLSELECTED/REMOVEFILTERS comparison, CALCULATE deep dive, FILTER function, Row Context vs Context Transition, Data Warehouse Architectures (Inmon/Kimball/Data Vault 2.0), Fabric Pipelines, TMDL governance, Storage Modes, Perspectives & Personalization

*(No entries yet.)*
Pending judgement:
- external URLs (3 genuinely broken): microsoft-fabric-missing-piece.md — 2× malformed MS Learn URLs (fixed); world-happiness-dataset-workflow.md — GitHub raw 404 (fixed)
- external URLs (144 kanerika.com SEO scrapers): 503 from any bot — links work in browser, not from server
- external URLs (4 logo.clearbit.com): DNS fail — fictional company examples, expected broken
- external URLs (4 LinkedIn): bot-blocked (405/999) — links work in browser
- external URLs (2 packtpub.com): bot-blocked (403)
- external URLs (14 misc): ColorOracle, Ko-Fi, AppSource, Azure blog timeout, etc.