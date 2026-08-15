---

created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
tags: [power-bi, pattern, dynamic-title, text, report]
note_type: pattern

---

# Dynamic Text Titles in Power BI

Using DAX to create report titles that update based on the current filter context.

## Purpose

Static titles don't reflect what the user is looking at. Dynamic titles show the selected filters.

## Basic Dynamic Title

```dax
Report Title :=
"Sales for " & SELECTEDVALUE( 'Dates'[Year], "All Years" )
& " — " & SELECTEDVALUE( 'Geography'[Region], "All Regions" )
```

## Measure-driven Dynamic Title

```dax
KPI Title :=
"Current: " & [Total Sales]
& " | Target: " & [Sales Target]
& " | Variance: " & FORMAT( [Sales Variance], "0.0%" )
```

## Notes

- Use SELECTEDVALUE() with a default to handle multi-selection states
- Can include KPIs, dates, and any slicer value in the title

## Related

- [[svg-visualizations-in-power-bi]]
- [[UNICHAR]]
