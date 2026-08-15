---
created: 2026-08-02
updated: 2026-08-11
source: system:changelog
---

# CHANGELOG

All notable changes to this knowledge base are documented here.

## 2026-08-11 — Health check (delta)

Audit: full scan of 903 wiki files. Delta since 2026-08-08.

Auto-fixed:
- writing-rules: 107 em-dash bullets replaced with colons across 107 files
- frontmatter: 290 `updated:` fields backfilled

New articles drafted: 0

Pending judgement:
- orphan-source: resolved — Power BI notes no longer have empty source: fields

## 2026-08-08 — Ingestion batch

Sources: 1 file (Crafting Compelling and Impactful Power BI Reports) — pending archive
Notes: 6 written (3 new + 3 extended) across 1 KB
KBs: Power BI

New notes:
- [[Source-Crafting-Compelling-Impactful-Power-BI-Reports]] — source note
- [[Report-Structural-Integrity]] — atomic — structural integrity as a design principle
- [[Data-Accuracy-and-Reliability]] — atomic — data accuracy as foundation of report trust
- [[Power-BI-Interactive-Features]] — pattern — drill-down, filters, slicers as a unified exploration pattern

Extended notes:
- [[data-storytelling]] — added Van Zyl's annotation and narrative framework
- [[Data-Narratives-Report-Design]] — added Step 0 structural integrity check
- [[tooltip-design-concise-and-relevant]] — added presentation-layer framing
- [[Power-BI-UX-7-Features]] — added section 3b: interactive features as holistic pattern

Errors fixed: 0 | Link ops applied: 0

## 2026-08-06 — Second-pass extractions (Esther 2026)

Source: "Building an Interactive Flip Card KPI Dashboard with Dash, Plotly & CSS" (Esther, Medium 2026-04-11) — re-scanned against all 9 templates after Pass 1 had been archived pending.
Added: 5 residual notes discovered in Pass 2 (1 function + 1 pattern + 3 gotchas).
KBs: Power BI

- [[hex-to-rgba-python]] — function — `hex_to_rgba()` color utility (small, reusable, independent of the chart_base family).
- [[generic-dash-callback-splat]] — pattern — splat-operator N-of-N callback (`*[Output(...)]` / `*[Input(...)]`), the data-driven-UI pattern's natural callback companion.
- [[plotly-layout-mutation-gotcha]] — gotcha — promoted from a `Notes` line in [[chart-base-plotly]]; explains why the helper must return a fresh dict.
- [[autorange-reversed-horizontal-bar-top]] — gotcha — Plotly `orientation="h"` bar-chart default direction.
- [[hoverinfo-skip-on-base-trace]] — gotcha — duplicate-hover suppression on hidden fill traces (companion to [[Two-Layer-Area-Line-Micro-Chart]]).

INDEX updated: extended "Patterns — CSS Interaction & Data-Driven UI (Esther, 2026)" with [[generic-dash-callback-splat]], [[chart-base-plotly]], [[hex-to-rgba-python]]; added new section "Gotchas — Plotly & Dash Mechanics (Esther, 2026)" with the 3 gotchas; back-fills missing description for [[Data-Driven-UI-Card-Tuples]]; source-note backref updated to all 11 derived notes.
Errors fixed: 0 | Link ops applied: 0

Source remains in Inbox pending archive; registry note updated.

## 2026-08-06 — Ingestion batch

Sources: 1 file → 99.System/InboxArchive/2026-08/
Notes: 1 written across 1 KB
KBs: Power BI (1 note)
Errors fixed: 0 | Link ops applied: 0

## 2026-08-06 — Ingestion batch

Sources: 1 file → 99.System/InboxArchive/2026-08/
Notes: 1 written across 1 KB
KBs: Power BI (1 note)
Errors fixed: 0 | Link ops applied: 0

## 2026-08-05 — Health check (delta)

Audit: 6 new notes read (delta since 2026-08-02).
Auto-fixed:
- writing-rules: 0 (6 new notes all clean)
- backlinks: 0 broken (new notes clean)
- INDEX links: 0 broken
- frontmatter: 6 updated: backfilled

New articles drafted: 0

Pending judgement:
- orphan-source: 5 Power BI notes have empty source: field (color-area-charts, emoji-kpi-card, forecast-actual-flag, power-bi-design-best-practices, high-ot-flag) → add source: to frontmatter
- link-density: Power Query at 23% — note same-KB cross-linking gap in Power Query applies vault-wide
- orphan-link-targets: see Data Modeling CHANGELOG (shared pool)
- missing-questions.md: No KB has a QUESTIONS.md file yet
- missing-frontmatter: 367 notes across vault missing updated: field

## 2026-08-02 — Health check (full, first ever)

Sources: 1 file (Automating PowerBI Deployments with GitHub Actions A Complete Guide.md)
Notes: 6 written across 1 KB
KBs: Power BI (6 notes)
Errors fixed: 0 | Link ops applied: 0

## 2026-08-02 — Health check (full, first ever)

Audit: 410 of 410 articles read. No Outputs since KB creation.

Auto-fixed:
- writing-rules: 18 em-dash bullets replaced with colons across 7 files
- backlinks: 0 broken links
- INDEX links: 0 broken links (412 INDEX entries match 411 wiki files + 1 nav file)
- frontmatter: 410 `updated:` fields backfilled (all were missing)
- downloads: 2 PBIX + 1 CSV downloaded to 99.System/Attachments; 3 GitHub repos cloned; wikilinks inserted in source notes

New articles drafted: 0

Pending judgement:
- orphan-link-targets: see Data Modeling CHANGELOG
- missing-questions.md: No KB has a QUESTIONS.md file yet.
