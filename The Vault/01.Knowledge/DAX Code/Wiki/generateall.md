---
created: 2026-07-26
updated: 2026-08-02
source: dax.pdf
note_type: function
tags: [dax, function, table]
---

# GENERATEALL

Returns a table with the Cartesian product between each row in table1 and the table that results from evaluating table2 in the context of the current row from table1.

## Syntax

```dax
GENERATEALL(<table1>, <table2>)
```

## Remarks

If the evaluation of table2 for the current row in table1 returns an empty table, then the current row from table1 will be included in the results and columns corresponding to table2 will have null values for that row. This is different than GENERATE() where the current row from table1 will not be included in the results. All column names from table1 and table2 must be different or an error is returned. This function is not supported for use in DirectQuery mode when used in calculated columns or row-level security (RLS) rules.