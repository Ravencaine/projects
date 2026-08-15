---
created: 2026-08-08
updated: 2026-08-08
source: "5 Power BI Slicer Tricks To Build Professional Dashboards"
source_url: https://www.youtube.com/watch?v=sdyxtL1250E
note_type: pattern
tags: [power-bi, slicers, date-table, dax]
related:
  - "[[Disconnected-Table-Slicer-Pattern]]"
---

# Slicer Default Selection (Current Month)

Auto-select the current or model-refresh month in a slicer after every data refresh.

## Purpose

After a monthly data refresh, a slicer set to a hard-coded month (e.g., March) will show stale data. This pattern makes the slicer dynamically select the current/refresh month — no manual intervention required.

## Components

1. **Calendar/Date table** with a `Current Month` calculated column
2. **DAX or Power Query** to compare each row's month to the refresh/current date
3. **Slicer** configured to display the `Current Month` column

## Structure

### Calculated Column (DAX)

```dax
Current Month =
VAR RefreshDate = DATE(2024, 10, 1)   -- replace with TODAY() or model refresh date
RETURN
    IF (
        FORMAT([Date], "mmmm yyyy")
            = FORMAT(RefreshDate, "mmmm yyyy"),
        "✓ " & FORMAT([Date], "mmmm yyyy"),   -- mark current month
        FORMAT([Date], "mmmm yyyy")             -- return normal month name
    )
```

### Calculated Column (Power Query M)

```m
"Current Month" = if Date.ToText([Date], "MMMM yyyy")
    = Date.ToText(Date.From(DateTime.LocalNow()), "MMMM yyyy")
then "✓ " & Date.ToText([Date], "MMMM yyyy")
else Date.ToText([Date], "MMMM yyyy")
```

## Example

1. Add `Current Month` column to the date table
2. In the slicer visual, remove the `Month` column and add `Current Month` instead
3. After a refresh, the slicer automatically highlights the current month

## Variations

- **Today's date:** Replace the manual date with `TODAY()` in DAX or `DateTime.LocalNow()` in Power Query
- **Fiscal year:** Use `EOMONTH(TODAY(), -1)` to mark the last completed fiscal month
- **Multiple hierarchies:** Create `Current Quarter`, `Current Year` columns alongside `Current Month`

## Related

- [[Disconnected-Table-Slicer-Pattern]] — uses the same column-swapping slicer technique
