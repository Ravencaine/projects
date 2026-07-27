---
created: 2026-07-26
source: dax.pdf
note_type: function
tags: [dax, function, table]
---

# UNION

Applies to: Calculated column Calculated table Measure Visual calculation Creates a union (join) table from a pair of tables.

## Syntax

```dax
UNION(<table_expression1>, <table_expression2> [,<table_expression>]…)
```

## Remarks

The two tables must have the same number of columns. Columns are combined by position in their respective tables. The column names in the return table will match the column names in table_expression1. Duplicate rows are retained. The returned table has lineage where possible. For