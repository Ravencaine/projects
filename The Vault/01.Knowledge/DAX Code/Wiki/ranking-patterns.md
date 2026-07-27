---
created: 2026-07-26
source: dax.pdf
note_type: pattern
tags: [dax, pattern, ranking, rankx, rank]
---

# Ranking Patterns in DAX

DAX provides multiple ways to rank data: RANKX, RANK, and ROWNUMBER.

## RANKX

```dax
RANKX(<table>, <expression>[, <value>[, <order>[, <ties>]]])
```

Ranks each row in a table based on the expression value.

| Parameter | Description |
|-----------|-------------|
| `table` | The table to rank over |
| `expression` | The value to rank |
| `value` | (Optional) The specific value to rank; defaults to current row's expression |
| `order` | 0/DESC = highest first, 1/ASC = lowest first |
| `ties` | Skip = how many positions to skip (default), Dense = no skip |

```dax
-- Rank products by sales (highest sales = rank 1)
Product Rank = RANKX(ALL('Product'), [Sales Amount])

-- Rank within category
Category Rank = RANKX(
    FILTER(ALL('Product'), 'Product'[Category] = EARLIER('Product'[Category])),
    [Sales Amount]
)
```

## RANK

```dax
RANK(<order>[, <ties>])
```

Ranks the current row within a window context.

```dax
-- Rank in window function context
RANK(ORDERBY('Sales'[Amount], DESC))
```

## ROWNUMBER

```dax
ROWNUMBER(<orderBy>[, <partitionby>])
```

Assigns sequential row numbers within a partition, with no ties.

```dax
-- Row number within category
ROW_NUMBER = ROWNUMBER(
    ORDERBY('Sales'[Amount], DESC),
    PARTITIONBY('Product'[Category])
)
```

## Common Ranking Patterns

### Top N Per Category
```dax
Top 5 Per Category =
TOPN(
    5,
    SUMMARIZECOLUMNS(
        'Product'[Category],
        'Product'[Product Name],
        "Sales", [Sales Amount]
    ),
    [Sales Amount],
    DESC
)
```

### Percent Rank
```dax
Percent Rank =
DIVIDE(
    RANKX(ALL('Product'[Product Name]), [Sales Amount],,ASC,Dense) - 1,
    COUNTROWS(ALL('Product'[Product Name])) - 1
)
```

## Related

- [[rankx]]
- [[rownumber]]
