---
created: 2026-07-26
source: dax.pdf
note_type: function
tags: [dax, function, table-manipulation]
---

# UNION, INTERSECT, EXCEPT

Set operations on tables.

## UNION

Stacks rows from two or more tables. Duplicate rows are retained.

```dax
UNION(<table1>, <table2>[, <table3> …])
```

- Tables are combined by **position** (same number of columns required)
- Column names from the **first** table are preserved
- Duplicate rows are **retained**
- Supports lineage preservation when first columns share lineage

## INTERSECT

Returns rows that appear in **both** tables.

```dax
INTERSECT(<table1>, <table2>)
```

- Only rows with matching values in all columns are returned
- Column names from the **first** table are preserved
- Duplicate rows are retained only if they appear multiple times in both tables
- Column order must match between tables

## EXCEPT

Returns rows in the **first** table that are **not** in the second table.

```dax
EXCEPT(<table1>, <table2>)
```

- Rows from table1 that have a match in table2 are excluded
- Column names from the **first** table are preserved
- Use `EXCEPT(table2, table1)` for the reverse (rows in table2 not in table1)

## Examples

```dax
-- Stack two product lists
UNION(
    SUMMARIZECOLUMNS('Product'[Color]),
    DATATABLE("Color", STRING, { {"Red"}, {"Blue"} })
)

-- Products that appear in both categories
INTERSECT(
    VALUES('Product'[ProductKey]),
    FILTER(VALUES('Product'[Category]), 'Product'[Category] = "Bikes")
)

-- Products that were sold this year but not last year
EXCEPT(
    VALUES('Sales'[ProductKey]),
    CALCULATETABLE(VALUES('Sales'[ProductKey]), SAMEPERIODLASTYEAR('Date'[Date]))
)
```

## Notes

- All three require tables with the **same number of columns**
- Column data types must be compatible
- INTERSECT and EXCEPT remove duplicate rows

## Related

- [[table-manipulation-functions-overview]]
- [[generate]]
- [[crossjoin]]
