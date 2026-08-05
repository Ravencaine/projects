---

created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
tags: ["dax", "pattern", "disconnected-tables", "slicer", "dynamic"]
note_type: pattern

---

# Disconnected Tables in DAX

Using tables with no active model relationships to drive dynamic calculations.

## Purpose

Power BI relationships only support exact matches on single columns. Disconnected tables paired with DAX can implement any comparison logic — ranges, complex conditions, multi-column lookups.

## Use Case: Parameter Table for Scenarios

```dax
Growth Rate = SELECTEDVALUE( 'Scenario'[GrowthRate], 0.05 )

Revenue Forecast :=
SUMX(
    'Sales',
    'Sales'[Revenue] * POWER( 1 + [Growth Rate], [Year] )
)
```

## Use Case: Dynamic Measure Selector

```dax
Selected Measure :=
SWITCH(
    TRUE(),
    'MeasureSelector'[Choice] = "Revenue",    [Revenue],
    'MeasureSelector'[Choice] = "Profit",     [Profit],
    'MeasureSelector'[Choice] = "Margin %",  [Margin %]
)
```

## Notes

- Disconnected tables pass values to measures via SELECTEDVALUE() or VALUES()
- DAX forms the "virtual relationship" that physical tables cannot provide
- Use with TREATAS() for multi-column virtual relationships

## Related

- [[cross-fact-treatas-virtual-relationships]]
- [[dynamic-measure-selection-in-dax]]
- [[table-constructor-pattern-in-dax]]
