---
created: 2026-08-09
updated: 2026-08-09
source: "Filters in Power BI Everything You Need to Know.md"
note_type: atomic
tags: [power-bi, filters, basic-filter, advanced-filter, top-n, relative-date, slicer, atomic]
---

# Filter Types Overview Atomic

**Type:** Atomic · **KB:** Power BI · **Source:** [[source-filters-in-power-bi-everything-you-need-to-know]]

Five filter types in Power BI, each suited for different scenarios.

## Types

| Type | Use case | How it works |
|------|----------|--------------|
| **Basic** | Known values to include/exclude | Select or type specific values |
| **Advanced** | Multiple conditions | AND/OR/NOT logic on one or more fields |
| **Top N** | Rank by measure | Show top or bottom N items (e.g., top 10 products) |
| **Relative Date** | Time-series dynamic filtering | Last N days/weeks/months/quarters/years |
| **Slicer** | User-interactive on canvas | Visual on the report canvas; filters page on selection |

## Basic vs Advanced

- **Basic:** choose values directly. Good when you know the specific items.
- **Advanced:** write conditions. Good for multi-value ranges, OR conditions, or blank/non-blank checks.

## Top N filter

Sorts by the specified measure and keeps only the top (or bottom) N rows. Requires a measure in the "By value" field.

## Relative Date filter

Dynamic — recalculates based on the current date. Options include: last N periods, next N periods, or a fixed period. Common for "YTD", "last 30 days", "MTD".

## Slicer

Not technically a filter type — it is a visual. But it functions as an interactive page-level filter. The report viewer controls it directly, unlike static filters set by the author.

## Related

- [[filter-levels-in-power-bi]] — visual/page/report/drillthrough scope
- [[apply-filters-to-visuals-workflow]] — setting up filters
- [[filter-best-practices]] — when to use which
