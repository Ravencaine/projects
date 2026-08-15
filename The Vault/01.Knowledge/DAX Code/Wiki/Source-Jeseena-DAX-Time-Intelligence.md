---
created: 2026-08-10
updated: 2026-08-10
source: DAX Time Intelligence: Where Everything You've Learned About Context Finally Pays Off
source_url: https://medium.com/@jeseenaparveenk/dax-time-intelligence-where-everything-youve-learned-about-context-finally-pays-off-8de1bb67adcb
note_type: source
tags: [dax, time-intelligence, dateadd, sameperiodlastyear, parallelperiod, totalmtd, totalytd, datesinperiod, datesbetween, calculate, filter-context]
---

# Source: Jeseena — DAX Time Intelligence: Where Context Pays Off

> **Type:** tutorial / reference
> **Author:** Jeseena (Jeseena Parveen K)
> **Published:** 2026-07-08
> **URL:** https://medium.com/@jeseenaparveenk/dax-time-intelligence-where-everything-youve-learned-about-context-finally-pays-off-8de1bb67adcb
> **Routed to:** DAX Code
> **Category:** DAX, Time Intelligence, CALCULATE, Filter Context

## Summary

Part 3 of a DAX series (following CALCULATE/Context and Filter Modifiers). Time intelligence is framed as the practical application of everything learned: every function is CALCULATE with a specially constructed date table passed as a filter modifier. Covers: Date table prerequisite; time shift functions (DATEADD, SAMEPERIODLASTYEAR, PARALLELPERIOD) with their key differences; running totals (TOTALMTD/QTD/YTD vs DATESMTD/QTD/YTD); rolling windows via DATESINPERIOD + LASTDATE; custom date ranges via DATESBETWEEN + DATE. Includes a mind map linking all functions.

## Key Claims / Components

1. **Date table must be marked:** auto date/time not sufficient; right-click → Mark as date table; no gaps; covers full data range
2. **DATEADD:** literal shift of whatever window is selected; intervals: DAY/MONTH/QUARTER/YEAR; most flexible
3. **SAMEPERIODLASTYEAR:** exactly same dates from one year prior; self-documenting YoY intent; equivalent to DATEADD(-1, YEAR) in most cases
4. **PARALLELPERIOD:** always returns complete periods snapped to boundaries — vs DATEADD which returns partial periods for mid-period selections
5. **TOTALMTD/QTD/YTD:** shortcut wrapping CALCULATE + DATES*; TOTALYTD accepts optional fiscal year end string parameter
6. **DATESMTD/QTD/YTD:** raw date table for combining with other CALCULATE filters (e.g., region-specific YTD)
7. **DATESINPERIOD + LASTDATE:** sliding rolling window; negative number for trailing, positive for forward; most common: rolling 3-month, trailing 12-month
8. **DATESBETWEEN + DATE:** fixed precise date range; ignores user date filter context when hardcoded; useful for fiscal periods with custom boundaries
9. **The key insight:** every time intelligence function = CALCULATE + specially constructed date table filter; stop memorizing, start reasoning from the pattern
10. **FIRSTDATE/LASTDATE:** return first/last date in current filter context; perform context transition; used as anchors inside other functions

## Extracted Notes

- [[Date-Table-Must-Be-Marked-Requirement]] — `atomic` — prerequisite: marked Date table, no gaps, covers full data range
- [[Time-Shift-Functions-DATEADD-SAMEPERIODLASTYEAR-PARALLELPERIOD]] — `reference` — comparison table for all three shift functions
- [[Running-Total-Functions-TOTALMTD-TOTALQTD-TOTALYTD]] — `reference` — TOTAL* shortcuts vs DATES* explicit; fiscal year parameter
- [[Rolling-Window-Functions-DATESINPERIOD]] — `reference` — DATESINPERIOD + LASTDATE; rolling trailing windows; anchor behavior
- [[Custom-Date-Range-DATESBETWEEN]] — `reference` — DATESBETWEEN + DATE; hardcoded fixed range; ignores user date filter
- [[Time-Intelligence-Is-CALCULATE-With-Date-Table]] — `concept` — the unifying insight: all time intelligence = CALCULATE with date table filter modifier
- [[Source-Jeseena-DAX-Time-Intelligence]] — `source` — this note

## Metadata

| Field | Value |
|-------|-------|
| Source file | DAX Time Intelligence Where Everything You've Learned About Context Finally Pays Off.md |
| Archived at | 99.System/InboxArchive/2026-08/ |
| Ingestion date | 2026-08-10 |
| Notes count | 6 (atomic ×1, reference ×4, concept ×1) |
