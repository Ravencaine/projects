---

created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
tags: ["dax", "pattern", "aggregation", "multi-column", "tuple", "iteration"]
note_type: pattern

---

# Multi-column Aggregation in DAX

Aggregating across multiple columns simultaneously when a single-column SUM/COUNT is insufficient.

## Purpose

When data spans multiple columns (e.g., weekly columns Mon-Sun, quarterly columns Q1-Q4), aggregate across all columns.

## Sum Across Multiple Columns

```dax
Total Across Columns :=
SUMX(
    GENERATESERIES( 1, 7 ),
    VAR __Col = "Col" & [Value]
    RETURN
    SWITCH(
        __Col,
        "Col1", [Col1],
        "Col2", [Col2],
        "Col3", [Col3],
        "Col4", [Col4],
        "Col5", [Col5],
        "Col6", [Col6],
        "Col7", [Col7],
        0
    )
)
```

## ADDCOLUMNS Approach

```dax
Multi-Column Sum :=
VAR __Table =
    ADDCOLUMNS(
        'Data',
        "__Total", 'Data'[Mon] + 'Data'[Tue] + 'Data'[Wed] + 'Data'[Thu] + 'Data'[Fri]
    )
RETURN
SUMX( __Table, [__Total] )
```

## Notes

- Better to restructure the data in Power Query (unpivot) for most scenarios
- Use SWITCH with GENERATESERIES when the column structure is fixed

## Related

- [[table-constructor-pattern-in-dax]]
- [[GENERATESERIES]]
