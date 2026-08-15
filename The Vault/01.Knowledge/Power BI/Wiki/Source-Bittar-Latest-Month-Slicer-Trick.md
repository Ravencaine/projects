---
created: 2026-08-10
updated: 2026-08-10
source: A Simple Trick to Always Display the Latest Month in Power BI (Even After Refresh)
source_url: https://medium.com/microsoft-power-bi/a-simple-trick-to-always-display-the-latest-month-in-power-bi-even-after-refresh-0630fef5e2f3
note_type: source
tags: [powerbi, slicer, user-experience, date-table, power-query]
---

# Source: Bittar — Latest Month Slicer Trick

> **Type:** article
> **Author:** Isabelle Bittar (KI Data Science)
> **Published:** 2026-02-12
> **URL:** https://medium.com/microsoft-power-bi/a-simple-trick-to-always-display-the-latest-month-in-power-bi-even-after-refresh-0630fef5e2f3
> **Routed to:** Power BI
> **Level:** Beginner
> **Category:** Data Visualization, DAX
> **Tags:** Tips & Tricks, Tutorial, Data Visualization, DAX

## Summary

Sticky slicer UX pattern: add a "This Month" column to the date table that labels the current calendar month as `"This Month"` and all others with `"MMM yyyy"`. Use the "This Month" column in the slicer with `"This Month"` pre-selected. On refresh, `DateTime.LocalNow()` updates the label — the slicer selection moves forward automatically. Includes full Power Query M code for the dynamic date table.

## Key Claims

1. After refresh, slicers retain their text selection — not their underlying value
2. A `"This Month"` label that dynamically changes means the slicer selection moves with the data
3. Power Query M approach: `if Date.StartOfMonth([Date]) = Date.StartOfMonth(Date.From(DateTime.LocalNow())) then "This Month" else [Month]`
4. Date table is fully dynamic — min/max dates pull from the fact table, so calendar always covers available data
5. Advantages: no republish, users retain control, report always opens in right context, easy to maintain
6. When `DateTime.LocalNow()` labels a month with no fact data, the visual shows blank — verify freshness separately
7. Alternative: DAX-based current period measures work better when you control all measures and don't need slicer-driven period logic

## Notable Details

- PBIX demo available for download
- The "This Month" column is text — the slicer remembers `"This Month"` as a text value, not a specific month
- Works only for the current calendar month, not rolling periods
- Isabelle Bittar is a known author in the KB (KI Data Science)

## Extracted Notes

- [[Sticky-Slicer-This-Month-Auto-Select]] — `pattern` — overview, problem, solution, when to use vs DAX approach
- [[This-Month-Slicer-Date-Table-M-Code]] — `reference` — full Power Query M code for the dynamic date table

## Metadata

| Field | Value |
|-------|-------|
| Source file | A Simple Trick to Always Display the Latest Month in Power BI (Even After Refresh).md |
| Archived at | 99.System/InboxArchive/2026-08/ |
| Ingestion date | 2026-08-10 |
| Word count | ~287 |
