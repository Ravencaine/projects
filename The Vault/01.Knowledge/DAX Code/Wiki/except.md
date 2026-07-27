---
created: 2026-07-26
source: dax.pdf
note_type: function
tags: [dax, function, table]
---

# EXCEPT

Applies to: Calculated column Calculated table Measure Visual calculation Returns the rows of the first table in the expression which do not appear in the second

## Syntax

```dax
EXCEPT(<table_expression1>, <table_expression2>)
```

## Remarks

If a row appears at all in both tables, it and its duplicates are not present in the result set. If a row appears in only table_expression1, it and its duplicates will appear in the result set. The column names will match the column names in table_expression1. The returned table has lineage based on the columns in table_expression1 , regardless of the lineage of the columns in the second table. For