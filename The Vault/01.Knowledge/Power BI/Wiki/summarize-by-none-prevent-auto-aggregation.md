---
created: 2026-08-09
updated: 2026-08-09
source: "Enhance Data Modelling in Power BI.md"
note_type: atomic
tags: [power-bi, data-modeling, summarize-by, aggregation, default-behavior, atomic]
---

# Summarize by None Prevent Auto-Aggregation Atomic

**Type:** Atomic · **KB:** Power BI · **Source:** [[source-enhance-data-modelling-power-bi]]

Power BI defaults to summarizing numeric fields (sum, average, count). For fields like Calendar Year that should not be summed, set `Summarize by = None` in model view to prevent incorrect auto-aggregation.

## Problem

When a `CalendarYear` or `MonthName` column is added to a visual, Power BI tries to aggregate it (sum or count by default). This produces meaningless numbers for categorical/text date fields.

## Fix

1. In **Model View**, select the field
2. In the **Properties pane**, find **Summarize by**
3. Set to **None**

The field no longer auto-summarizes. It behaves as a categorical grouping field.

## Other Summarize by options

| Setting | Effect |
|---------|--------|
| Sum | Default — sums numeric values |
| Average | Averages numeric values |
| Count | Counts rows |
| Min / Max | Minimum / maximum value |
| Distinct count | Unique value count |
| None | No aggregation — treated as text/category |

## Common use cases for None

- Calendar Year, Month Name, Quarter Name
- Product Category, Region, Status codes
- Any text field that happens to have numeric-looking content

## Related

- [[measures-repository-setup-workflow]] — broader model organization
- [[display-folder-organization-workflow]] — measure organization
