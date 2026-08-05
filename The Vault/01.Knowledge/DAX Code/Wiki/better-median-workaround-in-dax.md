---

created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
tags: ["dax", "pattern", "statistics", "median", "quirk"]
note_type: pattern

---

# Better MEDIAN Workaround in DAX

DAX's MEDIAN function has issues with BLANK values and integer vs. decimal handling.

## Purpose

`MEDIAN()` skips BLANKs but can return unexpected data types. The MEDIANX iterator approach provides more control.

## Iterator-based MEDIAN

```dax
Better MEDIAN :=
MEDIANX(
    FILTER( 'Table', NOT( ISBLANK( 'Table'[Value] ) ),
    'Table'[Value]
)
```

## Complete Pattern with Odd/Even Handling

```dax
Custom MEDIAN :=
VAR __Values =
    ADDCOLUMNS(
        FILTER( 'Table', NOT( ISBLANK( 'Table'[Value] ) ),
        "__Val", 'Table'[Value]
    )
VAR __Count = COUNTROWS( __Values )
VAR __Sorted =
    TOPN(
        __Count,
        __Values,
        [__Val],
        ASC
    )
RETURN
IF(
    MOD( __Count, 2 ) = 1,
    -- Odd: middle value
    MAXX(
        TOPN( ( __Count + 1 ) / 2, __Sorted, [__Val], ASC ),
        [__Val]
    ),
    -- Even: average of two middle values
    DIVIDE(
        MAXX( TOPN( __Count / 2,     __Sorted, [__Val], ASC ), [__Val] ) +
        MAXX( TOPN( __Count / 2 + 1, __Sorted, [__Val], ASC ), [__Val] ),
        2
    )
)
```

## Notes

- MEDIANX() is the iterator version — more flexible than MEDIAN()
- Explicitly filter BLANKs for accurate results
- The complete pattern handles even-count lists correctly (average of two middle values)

## Related

- [[medianx]]
- [[no-calculate-dax-pattern]]
