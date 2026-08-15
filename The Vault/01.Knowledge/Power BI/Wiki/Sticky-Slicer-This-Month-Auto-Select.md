---
created: 2026-08-10
updated: 2026-08-10
source: A Simple Trick to Always Display the Latest Month in Power BI (Even After Refresh)
source_url: https://medium.com/microsoft-power-bi/a-simple-trick-to-always-display-the-latest-month-in-power-bi-even-after-refresh-0630fef5e2f3
note_type: pattern
tags: [powerbi, slicer, user-experience, date-table, power-query]
---

# Sticky Slicer — "This Month" Auto-Select Pattern

A slicer UX pattern that automatically opens the report on the latest available month after dataset refresh — without republishing. Uses a dynamic "This Month" label column in the date table that moves forward automatically.

## Problem

After dataset refresh, Power BI slicers retain their last selection. A slicer set to *March 2024* stays on *March 2024* even after *April 2024* data is added — unless manually changed and republished.

## Solution

1. Create a `This Month` column in the date table that labels the current calendar month as `"This Month"` and all other months with their regular `"MMM yyyy"` label
2. Use this column in the slicer
3. Select `"This Month"` once in the slicer
4. On every refresh, the underlying data shifts — the current calendar month becomes the new "This Month", and the slicer selection moves with it automatically

The slicer remembers the **text value** "This Month", not a specific month. Because the label itself changes dynamically, the slicer appears to move forward automatically.

## Advantages

- ✅ No republish after every refresh
- ✅ Users retain full control over historical periods
- ✅ Report always opens in the right context
- ✅ Easy to explain and maintain
- ✅ Makes the report feel thoughtful instead of annoying

## Limitations

- Works only for the **current calendar month:** not a rolling last-N-months selection
- Requires the report to rely on slicer-based period selection
- If `DateTime.LocalNow()` runs on a day with no data, "This Month" labels a month with no facts — verify data freshness separately

## When to Use vs. DAX-Based "Current Period" Measures

| Approach | When to Use |
|---------|-------------|
| DAX-based current period (`MAX(Dates[Date])`) | You control all measures; report doesn't rely on slicers for period logic |
| Sticky slicer ("This Month") | Report already uses slicers extensively; users expect to control the time period themselves; rewriting all KPIs would be too disruptive |

## Related

- [[This-Month-Slicer-Date-Table-M-Code]] — Power Query M code for the full date table including the "This Month" column
