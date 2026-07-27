---
created: 2026-07-26
source: dax.pdf
note_type: function
tags: [dax, function, table]
---

# GENERATE

Applies to: Calculated column Calculated table Measure Visual calculation Returns a table with the Cartesian product between each row in table1 and the table

## Syntax

```dax
GENERATE(<table1>, <table2>)
```

## Remarks

If the evaluation of table2 for the current row in table1 returns an empty table, then the result table will not contain the current row from table1. This is different than GENERATEALL() where the current row from table1 will be included in the results and columns corresponding to table2 will have null values for that row. All column names from table1 and table2 must be different or an error is returned.