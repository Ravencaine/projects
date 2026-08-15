---
created: 2026-08-10
updated: 2026-08-10
source: DAX Time Intelligence: Year-to-Date, Rolling Averages, and Comparisons
source_url: https://medium.com/@saketsis/dax-time-intelligence-year-to-date-rolling-averages-and-comparisons-6a120ccef282
note_type: source
tags: [dax, time-intelligence, ytd, rolling-average, growth-rate, mom, qoq, yoy, cumulative-total]
---

# Source: Sisodia — DAX Time Intelligence: YTD, Rolling Averages, and Comparisons

> **Type:** tutorial / pattern reference
> **Author:** Saket Sisodia
> **Published:** 2026-07-29
> **URL:** https://medium.com/@saketsis/dax-time-intelligence-year-to-date-rolling-averages-and-comparisons-6a120ccef282
> **Routed to:** DAX Code
> **Category:** DAX, Time Intelligence, YTD, Rolling Averages, Period Comparisons

## Summary

Three core DAX time intelligence patterns: YTD calculations via TOTALYTD + SAMEPERIODLASTYEAR; rolling averages via AVERAGEX + DATESINPERIOD; prior-period comparisons (MoM/QoQ/YoY) via DIVIDE + CALCULATE + time shift functions. Finance and sales dashboard use cases. Best practices and common pitfalls.

## Key Claims / Components

1. **YTD:** `TOTALYTD(SUM(Sales[Amount]), 'Date'[Date])` — aggregates from year start to selected date; resets each year
2. **LYTD:** `CALCULATE([Revenue YTD], SAMEPERIODLASTYEAR('Date'[Date]))` — last year YTD for variance
3. **Rolling average:** `AVERAGEX(DATESINPERIOD(...), [Total Sales])` — smooths seasonal fluctuations; rolling average vs rolling total distinction
4. **MoM growth:** `DIVIDE([Sales] - CALCULATE([Sales], DATEADD(..., -1, MONTH)), CALCULATE([Sales], DATEADD(..., -1, MONTH)))`
5. **QoQ growth:** same pattern with `DATEADD(..., -1, QUARTER)`
6. **YoY growth:** same pattern with `SAMEPERIODLASTYEAR`
7. **YTD vs cumulative total:** YTD resets at year boundary; cumulative total does not; critical for multi-year dashboards
8. **Best practices:** always use Date table; build base measures first; test with slicers; document formulas

## Extracted Notes

- [[Rolling-Average-AVERAGEX-DATESINPERIOD-Pattern]] — `pattern` — AVERAGEX + DATESINPERIOD rolling average; rolling avg vs rolling total; common window sizes
- [[Growth-Rate-Pattern-DIVIDE-Prior-Period]] — `pattern` — universal DIVIDE(Current−Prior, Prior) template; MoM/QoQ/YoY variants; base measure first
- [[YTD-vs-Cumulative-Total-Reset-Behaviour]] — `gotcha` — YTD resets at year start; cumulative total does not; rule for multi-year dashboards
- [[Source-Sisodia-DAX-Time-Intelligence-YTD-Rolling-Averages]] — `source` — this note

## Metadata

| Field | Value |
|-------|-------|
| Source file | DAX Time Intelligence Year-to-Date, Rolling Averages, and Comparisons.md |
| Archived at | 99.System/InboxArchive/2026-08/ |
| Ingestion date | 2026-08-10 |
| Notes count | 3 (pattern ×2, gotcha ×1) |
