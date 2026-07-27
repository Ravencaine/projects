---
created: 2026-07-26
source: dax.pdf
note_type: function
tags: [dax, function, information]
---

# ISINSCOPE, ISCROSSFILTERED, ISFILTERED, HASONEFILTER, HASONEVALUE

Detect filter context state — which columns are active, scoped, or have single values.

## ISINSCOPE

```dax
ISINSCOPE(<columnName>)
```

Returns TRUE when `columnName` is currently being iterated in a hierarchy or grouped in a visual.

```dax
-- % of parent in a Category > Subcategory hierarchy
% of Parent = SWITCH(TRUE(),
    ISINSCOPE(DimProduct[Subcategory]),
        DIVIDE(SUM(Sales[Amount]), CALCULATE(SUM(Sales[Amount]), ALLSELECTED(DimProduct[Subcategory]))),
    ISINSCOPE(DimProduct[Category]),
        DIVIDE(SUM(Sales[Amount]), CALCULATE(SUM(Sales[Amount]), ALLSELECTED(DimProduct[Category]))),
    SUM(Sales[Amount])
)
```

## ISFILTERED / ISCROSSFILTERED

```dax
ISFILTERED(<columnName>)
ISCROSSFILTERED(<columnName>)
```

| Function | Tests |
|----------|-------|
| `ISFILTERED` | Direct filter on the column (from slicer, visual, or filter pane) |
| `ISCROSSFILTERED` | Any filter affecting this column, including cross-filters from related columns |

## HASONEFILTER / HASONEVALUE

```dax
HASONEFILTER(<columnName>)
HASONEVALUE(<columnName>)
```

| Function | Tests |
|----------|-------|
| `HASONEFILTER` | Exactly one distinct value from **direct** filter |
| `HASONEVALUE` | Exactly one distinct value from **direct + cross** filters |

> HASONEVALUE checks cross-filters; HASONEFILTER checks direct filters only.

## Examples

```dax
-- Safe to use SELECTEDVALUE when exactly one value
Safe Value = IF(HASONEVALUE('Date'[Year]), SELECTEDVALUE('Date'[Year]), 2020)

-- Detect if a column is grouped in a visual
Is Scoped = ISINSCOPE(Product[Subcategory])

-- Is column being filtered?
Has Filter = IF(ISFILTERED(Date[Month]), "Filtered", "All")
```

## Notes

- ISFILTERED/ISCROSSFILTERED: not supported in DirectQuery mode for calculated columns or RLS
- HASONEVALUE: equivalent to `COUNTROWS(VALUES(col)) = 1` but with cross-filter awareness
- HASONEFILTER: equivalent to `COUNTROWS(VALUES(col)) = 1` but direct filters only
- Use [[selectedvalue]] instead of the HASONEVALUE + VALUES pattern in modern DAX
- Related: [[selectedvalue]]

## Related

- [[selectedvalue]]
