---
created: 2026-07-26
source: dax.pdf
note_type: function
tags: [dax, function, table]
---

# INTERSECT

Applies to: Calculated column Calculated table Measure Visual calculation Returns the row intersection of two tables, retaining duplicates.

## Syntax

```dax
INTERSECT(<table_expression1>, <table_expression2>)
```

## Remarks

Intersect is not commutative. In general, Intersect(T1, T2) will have a different result set than Intersect(T2, T1). Duplicate rows are retained. If a row appears in table_expression1 and table_expression2, it and all duplicates in table_expression_1 are included in the result set. The column names will match the column names in table_expression1.