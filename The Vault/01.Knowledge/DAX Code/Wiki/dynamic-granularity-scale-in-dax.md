---

created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
tags: ["dax", "pattern", "dynamic", "granularity", "scale", "report"]
note_type: pattern

---

# Dynamic Granularity Scale in DAX

Displaying measures at different granularities based on the selected time period.

## Purpose

When a user selects Day, show daily values. When they select Month, show monthly aggregates — without changing the visual.

## Pattern

```dax
Adaptive KPI :=
SWITCH(
    TRUE(),
    SELECTEDVALUE( 'Granularity'[Level] ) = "Day",
        FORMAT( [DailySales], "$#,##0" ),
    SELECTEDVALUE( 'Granularity'[Level] ) = "Month",
        FORMAT( [MonthlySales], "$#,##0" ),
    FORMAT( [AnnualSales], "$#,##0" )
)
```

## Notes

- A granularity selector table drives which measure is displayed
- Use SELECTEDVALUE() with a default for consistent handling

## Related

- [[dynamic-measure-selection-in-dax]]
- [[dynamic-text-titles-in-power-bi]]
