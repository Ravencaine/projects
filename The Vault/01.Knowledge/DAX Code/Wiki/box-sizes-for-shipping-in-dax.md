---

created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
tags: [dax, pattern, operations, shipping, logistics, optimization]
note_type: pattern

---

# Box Sizes for Shipping in DAX

Determining the optimal box size from a set of standard sizes based on item dimensions.

## Purpose

Given item dimensions (L x W x H) and a list of box sizes, find the smallest box that fits all items.

## DAX Pattern

```dax
Optimal Box :=
VAR __Items =
    SUMMARIZECOLUMNS(
        'OrderLines',
        "MaxL", MAX( 'OrderLines'[Length] ),
        "MaxW", MAX( 'OrderLines'[Width] ),
        "MaxH", MAX( 'OrderLines'[Height] ),
        "TotalVol", SUMX( 'OrderLines', 'OrderLines'[L] * 'OrderLines'[W] * 'OrderLines'[H] )
    )
VAR __Box =
    FILTER(
        'BoxSizes',
        'BoxSizes'[Length] >= [MaxL]
        && 'BoxSizes'[Width] >= [MaxW]
        && 'BoxSizes'[Height] >= [MaxH]
    )
VAR __Smallest =
    TOPN( 1, __Box, 'BoxSizes'[Volume], ASC )
RETURN
MAXX( __Smallest, 'BoxSizes'[Name] )
```

## Notes

- Replace SUMMARIZECOLUMNS with actual item dimensions from the data
- Box sizes should be a separate dimension table

## Related

- [[inventory-turnover-in-dax]]
- [[on-time-in-full-otif-dax]]
