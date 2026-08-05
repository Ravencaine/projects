---

created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
tags: ["dax", "pattern", "index", "row-number", "ranking", "iteration"]
note_type: pattern

---

# DAX Index Pattern (Row Number)

Generating a sequential row number within a table or filtered context.

## Purpose

Unlike Excel's ROW() or SQL's ROWNUMBER(), DAX has no native row number. This pattern creates one.

## Basic Index

```dax
Row Number :=
COUNTROWS(
    FILTER(
        ALL( 'Table' ),
        'Table'[SortColumn] <= EARLIER( 'Table'[SortColumn] )
    )
)
```

## With ORDERBY

```dax
Row Number :=
RANKX(
    ALL( 'Table' ),
    'Table'[SortColumn],
    ,
    ASC,
    DENSE
)
```

## Index with GROUPBY

```dax
Row Within Group :=
VAR __GroupKey = 'Table'[Group]
RETURN
COUNTROWS(
    FILTER(
        ALL( 'Table' ),
        'Table'[Group] = __GroupKey
        && 'Table'[SortCol] <= EARLIER( 'Table'[SortCol] )
    )
)
```

## Notes

- FILTER + EARLIER is the classic approach — slow on large tables
- RANKX with DENSE ranking is faster for simple sequential numbering
- For best performance, add a sort column index in Power Query instead

## Related

- [[streak-detection-in-dax]]
- [[RANKX]]
