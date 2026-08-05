---


title: "Pivot Table Timeline Slicer"
created: 2026-07-28
updated: 2026-08-02
tags: [power-bi, excel, pivot-table, pattern]
note_type: pattern
description: "Timeline slicer in Excel Pivot Tables — filter by year/quarter/month/day interactively. Different from standard date slicer."


source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"

---

# Pivot Table Timeline Slicer

A specialized slicer for date fields that allows filtering by **time intervals** (years, quarters, months, days) with a visual calendar-style interface.

## Insert

```
Pivot Table Tools → Analyze → Insert Timeline
Select date field → OK
```

## Time Period Selector

Click the dropdown arrow at the upper-right of the Timeline:
- **Years**: highest level, one click filters to entire year
- **Quarters**: drill into Q1/Q2/Q3/Q4
- **Months**: drill into individual months
- **Days**: finest granularity

## Combining with Other Slicers

The Timeline works alongside **standard slicers**. Select a salesperson (slicer) and a date range (Timeline) simultaneously — both filters apply to the Pivot Table.

## Use Cases

- Quarterly reports that need quick year-over-year comparisons
- Month-level drill-down without changing the Pivot Table structure
- Replacing multiple manual date filters with one visual control

## Difference from Standard Date Slicer

| Feature | Standard Date Slicer | Timeline Slicer |
|---------|---------------------|----------------|
| Granularity | Individual dates | Years/Quarters/Months/Days |
| Visual | List of dates | Calendar-style UI |
| Period selection | Single or range | Period level dropdown |

## Source Reference

Chapter 3, *Beginning Big Data with Power BI and Excel 2013* (Dunlop, Apress 2015).
