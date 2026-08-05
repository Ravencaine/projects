---

created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
tags: ["dax", "pattern", "dynamic", "measure-selection", "switch"]
note_type: pattern

---

# Dynamic Measure Selection in DAX

Allowing users to select which measure to display from a disconnected slicer.

## Purpose

Show only one of several measures at a time in a visual, controlled by a slicer.

## Data Model

Create a disconnected table:

```dax
Measure Selector =
SELECTCOLUMNS(
    { {"Revenue"}, {"Profit"}, {"Margin %"}, {"Orders"} },
    "Measure", [Value1]
)
```

## DAX Pattern

```dax
Selected KPI :=
SWITCH(
    TRUE(),
    'Measure Selector'[Measure] = "Revenue",   FORMAT( [Revenue], "$#,##0" ),
    'Measure Selector'[Measure] = "Profit",    FORMAT( [Profit], "$#,##0" ),
    'Measure Selector'[Measure] = "Margin %",  FORMAT( [Margin %], "0.0%" ),
    'Measure Selector'[Measure] = "Orders",    FORMAT( [Orders], "#,##0" )
)
```

## Notes

- Use SWITCH with TRUE() as the first argument for clean conditional logic
- FORMAT() ensures consistent number formatting regardless of which measure shows
- Works in Card, Table, and Matrix visuals

## Related

- [[disconnected-tables-in-dax]]
- [[SWITCH]]
