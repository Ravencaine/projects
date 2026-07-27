---
created: 2026-07-26
source: dax.pdf
note_type: function
tags: [dax, function, table]
---

# CROSSJOIN

Applies to: Calculated column Calculated table Measure Visual calculation Returns a table that contains the Cartesian product of all rows from all tables in the

## Syntax

```dax
CROSSJOIN(<table>, <table>[, <table>]…)
```

## Remarks

Column names from table arguments must all be different in all tables or an error is returned. The total number of rows returned by CROSSJOIN() is equal to the product of the number of rows from all tables in the arguments; also, the total number of columns in the result table is the sum of the number of columns in all tables. For