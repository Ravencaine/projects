---
created: 2026-07-27
updated: 2026-08-02
source: "Time Intelligence in DAX: The Secret Behind YTD, QTD, and SamePeriodLastYear"
source_url: "https://medium.com/write-your-world/time-intelligence-in-dax-the-secret-behind-ytd-qtd-and-sameperiodlastyear-4e4b16c3e6b2"
note_type: source
tags: [dax, time-intelligence, ytd, qtd, sameperiodlastyear, date-table]
---

# Time Intelligence in DAX: The Secret Behind YTD, QTD, and SamePeriodLastYear

> **Type:** article
> **Author:** Gulab Chand Tejwani
> **Published:** 2025-10-27
> **URL:** https://medium.com/write-your-world/time-intelligence-in-dax-the-secret-behind-ytd-qtd-and-sameperiodlastyear-4e4b16c3e6b2
> **Routed to:** DAX Code

## Summary

DAX time intelligence functions (YTD, QTD, SAMEPERIODLASTYEAR) depend on a properly configured date table. The key insight: using ALLSELECTED() inside time intelligence functions produces more robust results than hardcoded YEAR() filters, because it respects user-selected date ranges while maintaining correct period-over-period comparisons.

## Key Claims

- YTD, QTD, MTD require a contiguous date table — gaps cause incorrect or blank results
- SAMEPERIODLASTYEAR requires continuous date series; PARALLELPERIOD handles gaps by shifting month/quarter/year boundaries
- BEST PRACTICE: Use DATESYTD(..., "06/30") for fiscal year calendars (non-calendar year end)
- When the date slicer selects a non-contiguous range, SAMEPERIODLASTYEAR fails — use PREVIOUSMONTH/PREVIOUSQUARTER instead

## Extracted Notes

- [[time-intelligence-ytd-pattern]] — pattern
- [[sameperiodlastyear-vs-parallelperiod]] — comparison

## Metadata

| Field | Value |
|-------|-------|
| Source file | Time Intelligence in DAX The Secret Behind YTD, QTD, and SamePeriodLastYear.md |
| Archived at | 99.System/InboxArchive/2026-07/ |
| Ingestion date | 2026-07-27 |
| Word count | ~1,042 |
