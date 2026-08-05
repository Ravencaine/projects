---

created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
tags: ["dax", "pattern", "table", "constructor"]
note_type: pattern

---

# Table Constructor Pattern in DAX

Using row constructors to create inline tables for slicers, parameters, and small lookups.

## Purpose

Row constructors create small tables inline without Power Query or external data sources.

## Basic Syntax

```dax
-- Single-column table
Colors = { {"Red"}, {"Blue"}, {"Green"} }
```

## With SELECTCOLUMNS for Named Columns

```dax
Parameters =
SELECTCOLUMNS(
    { {"Low", 0.05}, {"Medium", 0.10}, {"High", 0.20} },
    "Tier", [Value1],
    "Rate", [Value2]
)
```

## For Disconnected Slicer Values

```dax
Budget Options =
SELECTCOLUMNS(
    { {"Base", 100000}, {"Mid", 250000}, {"Aggressive", 500000} },
    "Label", [Value1],
    "Amount", [Value2]
)
```

## Notes

- Row constructors do not specify column names — use SELECTCOLUMNS() to name them
- Small tables (under ~10 rows) are suitable for inline construction
- For larger tables, use Power Query or a calculated table

## Related

- [[SELECTCOLUMNS]]
- [[disconnected-tables-in-dax]]
- [[GENERATESERIES]]
