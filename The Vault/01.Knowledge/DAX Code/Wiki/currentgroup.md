---
created: 2026-07-26
updated: 2026-08-09
source: dax.pdf
note_type: function
tags: [dax, function, table, groupby, iterator, count]
---

# CURRENTGROUP

Applies to: Calculated column Calculated table Measure Visual This function is discouraged for use in visual calculations as it likely returns Returns a set of rows from the table argument of a GROUPBY expression that belong to

## Return Value

meaningless results. Returns a set of rows from the table argument of a GROUPBY expression that belong to the current row of the GROUPBY result. Syntax DAX CURRENTGROUP ( ) Parameters None Return value The rows in the table argument of the GROUPBY function corresponding to one group of values of the

## Remarks

This function can only be used within a GROUPBY expression. This function takes no arguments and is only supported as the first argument to one of the following aggregation functions: AVERAGEX, COUNTAX, COUNTX, GEOMEANX, MAXX, MINX, PRODUCTX, STDEVX.S, STDEVX.P, SUMX, VARX.S, VARX.P.

## Counting rows per group: SUMX(CURRENTGROUP(), 1)

`COUNTROWS` is **not** in the supported-aggregator list above, so it cannot be used directly as a `GROUPBY` aggregation. The standard idiom to count rows per group is `SUMX(CURRENTGROUP(), 1)` — iterate over the current group and sum a constant `1` per row.

```dax
ProdsAndCount =
GROUPBY (
    YearsAndTop10,
    'Product'[ProductKey],
    "NumOfYears", SUMX ( CURRENTGROUP (), 1 )    -- counts rows per product
)
```

For each product, `NumOfYears` equals the number of years that product appeared in the source table. This is the canonical workaround for "count rows in a GROUPBY" and is essential when the source is a `VAR` (a virtual table) where you cannot add a calculated column.

### Variations

| Need                          | Expression                                          |
| ----------------------------- | --------------------------------------------------- |
| Count rows                    | `SUMX ( CURRENTGROUP (), 1 )`                       |
| Count rows where condition    | `SUMX ( CURRENTGROUP (), IF ( <cond>, 1, 0 ) )`     |
| Sum a column                  | `SUMX ( CURRENTGROUP (), SourceTable[Amount] )`     |
| Average                       | `AVERAGEX ( CURRENTGROUP (), SourceTable[Amount] )` |

## Related

- [[groupby]] — function that produces groups for CURRENTGROUP
- [[sumx]] — the iterator that wraps CURRENTGROUP
- [[groupby-sumx-currentgroup-constant-count-pattern]] — full pattern
- [[evergreen-top-n-products-pattern]] — uses this idiom for "appearances per product"
- [[Source-Find-Top-10-Products-Every-Year-DAX]] — source
