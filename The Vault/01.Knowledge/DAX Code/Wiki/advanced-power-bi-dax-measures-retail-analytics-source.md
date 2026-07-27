---
created: 2026-07-27
source: "Advanced Power BI DAX Measures for Retail Analytics Pt 1"
source_url: "https://medium.com/@jjr8888/advanced-power-bi-dax-measures-for-retail-analytics-pt-1-297936931171"
note_type: source
tags: [dax, power-bi, retail, time-intelligence, variance, budget]
---

# Advanced Power BI DAX Measures for Retail Analytics (Parts 1–2)

Two-part Medium series by Jesse Ruiz covering foundational DAX fundamentals and advanced retail analytics patterns: sales-to-budget variance, inventory aging, time intelligence, and the variable pattern.

> **Type:** article
> **Author:** Jesse Ruiz (she/they)
> **Published:** Part 1: 2026-07-06, Part 2: 2026-07-20
> **URL:** https://medium.com/@jjr8888/advanced-power-bi-dax-measures-for-retail-analytics-pt-1-297936931171
> **Routed to:** DAX Code

## Summary

Part 1 covers DAX fundamentals (measures vs calculated columns, filter context vs row context), the sales-to-budget variance pattern with conditional display, and teaching points on VAR, BLANK vs 0, and DIVIDE. Part 2 covers time intelligence (MTD, YTD, SAMEPERIODLASTYEAR, DATESBETWEEN), inventory aging analysis with age buckets, and context transition with CALCULATE inside AVERAGEX.

## Key Claims

- Measures respond to filter context; calculated columns compute once at refresh and don't respond
- BLANK() propagates correctly in charts and averages; 0 implies a measured value
- DIVIDE handles zero denominator safely, returning BLANK
- VAR makes DAX readable, debuggable, and performant
- Inventory aging buckets must return 0 not BLANK for percentage sums
- MAXX + ALLSELECTED finds the latest date in a slicer selection for budget retrieval
- ALLSELECTED preserves slicer selections; ALL ignores all filters

## Notable Details

- Part 2 mentions: "AVERAGEX iterates over each store, CALCULATE converts row context to filter context so [Sales] evaluates correctly per store"
- The -100% variance hide pattern: stores without budget show blank, not alarming red

## Extracted Notes

Links to notes derived from this source:

- [[sales-to-budget-variance-percent]] — `pattern` — basic variance formula
- [[conditional-variance-display-percent-hide]] — `pattern` — hiding -100% variance
- [[inventory-aging-buckets-0-1-1-2-5-weeks]] — `pattern` — age bucket measures
- [[filter-context-vs-row-context]] — `atomic` — core DAX contexts
- [[context-transition-with-calculate]] — `atomic` — CALCULATE inside iterators
- [[blank-vs-zero-in-averages]] — `gotcha` — BLANK() vs 0
- [[time-intelligence-quick-reference-retail-analytics]] — `reference` — function reference
- [[calculate]] — extended with context transition teaching point

## Metadata

| Field | Value |
|-------|-------|
| Source file | Advanced Power BI DAX Measures for Retail Analytics Pt 1.md (+ Pt 2) |
| Archived at | 99.System/InboxArchive/2026-07/ |
| Ingestion date | 2026-07-27 |
| Word count | ~1,600 (parts combined) |
