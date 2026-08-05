---
created: 2026-07-26
updated: 2026-08-02
source: dax.pdf
note_type: function
tags: [dax, function, table]
---

# CROSSJOIN, NATURALINNERJOIN, NATURALLEFTOUTERJOIN

Table joins and cross-products.

## CROSSJOIN

```dax
CROSSJOIN(<table1>, <table2>[, <table3>, ...])
```

Returns the **Cartesian product**: every combination of rows from all tables. Total rows = rows₁ × rows₂ × ...

```dax
-- All Color × Size combinations
ColorSizeCombo = CROSSJOIN(VALUES('Product'[Color]), VALUES('Product'[Size]))
```

## NATURALINNERJOIN

```dax
NATURALINNERJOIN(<LeftTable>, <RightTable>)
```

Inner join — returns only rows where **matching values exist in both tables**. Joins on columns with the **same name and data type**.

## NATURALLEFTOUTERJOIN

```dax
NATURALLEFTOUTERJOIN(<LeftTable>, <RightTable>)
```

Left outer join — returns all rows from the left table, with matching rows from the right (or BLANK if no match). Joins on columns with the **same name and data type**.

## Notes

- CROSSJOIN: all column names must be unique across tables, or an error is returned
- NATURAL joins: requires at least one common column name; common columns must have the same data type
- No sort order guarantee on NATURALINNERJOIN/NATURALLEFTOUTERJOIN
- Use [[cross-fact-treatas-virtual-relationships]] or [[summarizecolumns]] for more controlled joins
- Not supported in DirectQuery mode for calculated columns or RLS rules

## Related

- [[cross-fact-treatas-virtual-relationships]]
- [[summarizecolumns]]
