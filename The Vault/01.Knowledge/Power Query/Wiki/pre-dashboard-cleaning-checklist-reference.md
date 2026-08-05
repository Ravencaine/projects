---
created: 2026-08-02
updated: 2026-08-02
source: Power BI Data Cleaning Checklist Before Creating Dashboards 12 Essential Steps That Save Hours of Rework.md
note_type: reference
tags: [power-query, reference, checklist, data-quality, pre-dashboard, power-bi]
---

# Pre-Dashboard Cleaning Checklist (12 Steps)

A condensed, actionable checklist for running before dragging any visual onto the Power BI canvas. Compiled from the 12-step Power Query data cleaning workflow.

## The 12-Step Checklist

- \[ \] 1 — Duplicate records removed (inspect before removing)
- \[ \] 2 — Data types explicitly set (never trust auto-detection)
- \[ \] 3 — Missing/blank values handled deliberately
- \[ \] 4 — Extra spaces trimmed (Trim + Clean on all text columns)
- \[ \] 5 — Dates and categories standardized to one format
- \[ \] 6 — Relationships validated (primary keys unique, cross-filter correct)
- \[ \] 7 — Unused columns removed
- \[ \] 8 — Numeric outliers checked (min/max via Column Distribution)
- \[ \] 9 — Totals verified against source system
- \[ \] 10 — Refresh indicator added (DateTime.LocalNow())
- \[ \] 11 — Aggregations tested in Matrix before building visuals
- \[ \] 12 — Data quality page created and hidden

## Why 20–30 Minutes Upfront Saves Hours Later

- Duplicate orders double revenue with zero warning
- Blank `Product Category` silently creates a "Blank" chart segment
- Auto-detected number-as-text sorts alphabetically ($10 before $2)
- A relationship that "almost works" produces numbers that "almost look right"

## Metadata

| Field | Value |
|-------|-------|
| Source | [[power-query-data-cleaning-checklist]] |
| Type | reference / checklist |

## Related

- [[power-query-data-cleaning-checklist]] — `pattern` — Full detail on each step
- [[data-quality-page-pattern]] — `pattern` — Hidden monitoring tab
