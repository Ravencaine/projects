---
created: 2026-08-02
updated: 2026-08-11
source: system:changelog
---

# CHANGELOG

All notable changes to this knowledge base are documented here.

## 2026-08-11 — Health check (delta)

Audit: 20 delta notes read. Delta since 2026-08-06.

Auto-fixed:
- writing-rules: 4 em-dash bullets replaced with colons across 4 files
- INDEX links: 3 orphaned notes added to Excel INDEX.md (In-Cell-Bar-Chart-REPT, REPT-In-Cell-Bar-Charts, integrating-python-excel-source)
- frontmatter: 32 `updated:` fields backfilled

New articles drafted: 0

Pending judgement:
- excel-index-extras: Excel INDEX header still shows 54 notes (needs +3, now 57) — auto-fixed this run

## 2026-08-06 — Ingestion batch

Sources: 1 file → 99.System/InboxArchive/2026-08/
Notes: 12 written across 1 KB
KBs: Data Modeling (12 notes: 1 source, 4 reference, 4 atomic, 3 pattern)
Errors fixed: 0 | Link ops applied: 0

## 2026-08-05 — Health check (delta, vault-wide)

Audit: vault-wide wikilink analysis + orphan scan across all 6 KBs.
Auto-fixed (delta notes only):
- writing-rules: 0 (Data Modeling delta = 0 new notes since last check)
- backlinks: 0
- INDEX links: 0

New articles drafted: 0

Pending judgement (vault-wide):
- article-candidate: Beginning Big Data with Power BI and Excel 2013 (Dunlop) — 202 broken wikilinks across vault → strongly recommend ingesting as new source
- article-candidate: STDEVX.P — 4 broken wikilinks in DAX Code (gamma-function, medianx, percentile-functions, trimmean)
- article-candidate: python-in-power-bi-setup — 3 broken wikilinks in Power Query
- link-density: Power Query at 23% (195/850) → significant same-KB cross-linking gap
- orphan-link-targets: 64 unique unfixable wikilink targets across vault (115 unique targets previously; ~50 resolved by new notes this session)
- orphan-source: 5 source orphans in Power BI (empty source: field) — color-area-charts, emoji-kpi-card, forecast-actual-flag, power-bi-design-best-practices, high-ot-flag
- orphan-registry: 7 archived sources with no inbound note references (benign — original notes absorbed into broader articles)
- missing-questions.md: No KB has a QUESTIONS.md file yet
- missing-frontmatter: 367 notes across vault missing updated: field
- vba-kb-empty: VBA KB has 3 nav-index entries but only 1 wiki note

## 2026-08-02 — Health check (full, first ever)

Audit: 65 of 65 articles read. No Outputs since KB creation.

Auto-fixed:
- writing-rules: 19 em-dash bullets replaced with colons across 5 files
- backlinks: 0 broken links (all cross-KB links resolve vault-wide; 0 same-KB broken)
- INDEX links: 0 broken links
- frontmatter: 65 `updated:` fields backfilled (all were missing)

New articles drafted: 0

Pending judgement:
- orphan-link-targets: 158 [[wikilinks]] across the vault point to notes not yet written (158 instances, 115 unique targets). Top: measure-branching-naming-conventions (6x), treatas (6x), Human Capital Value Added HCVA (6x), ATAN2 (4x), VARX.P (4x), On Time In Full OTIF (5x). These are article candidates for future ingestion sessions.
- missing-questions.md: No KB has a QUESTIONS.md file yet — consider creating one to track open questions per KB.
