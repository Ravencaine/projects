---
created: 2026-08-11
updated: 2026-08-11
source: "5-Power-BI-Slicer-Tricks-Goodly-Transcript.md"
note_type: pattern
tags: [power-bi, slicer, dax]
---

# Slicer Default Selection — Auto-Select Current Month

A slicer that automatically selects the current or most recent period after refresh — using a DAX column or Power Query column that marks the current period.

## DAX Approach

In the date dimension table, add a calculated column:

```dax
Current Month =
VAR RefreshDate = DATE(2025, 10, 1)  -- or TODAY(), MAX('ModelRefreshLog'[Date]), etc.
VAR FormattedRefresh = FORMAT(RefreshDate, "mmmm yyyy")
VAR FormattedCurrent = FORMAT('Date'[Date], "mmmm yyyy")
RETURN
    IF(FormattedCurrent = FormattedRefresh, FormattedRefresh, 'Date'[Month])
```

Use `Current Month` (not `Month`) in the slicer — it auto-selects the current period. Change the `RefreshDate` variable to use `TODAY()` or a model refresh date for live behavior.

## Power Query Approach

Same logic in M: create a column that compares the date against a refresh date and returns the matching formatted month.

## Key Rule

The logic is the same in DAX or M: format both dates to the same precision (month/year), compare, return matching period or the natural column value.

## Related

- [[slicer-apply-all-clear-all-buttons]] — Apply Slicers and Clear Slicers buttons
- [[disconnected-table-slicer-pattern]] — disconnected table for highlight-only behavior
