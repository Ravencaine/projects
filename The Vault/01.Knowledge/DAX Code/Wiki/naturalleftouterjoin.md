---
created: 2026-07-26
source: dax.pdf
note_type: function
tags: [dax, function, table]
---

# NATURALLEFTOUTERJOIN

Applies to: Calculated column Calculated table Measure Visual calculation Performs a join of the LeftTable with the RightTable by using the Left Outer Join

## Syntax

```dax
NATURALLEFTOUTERJOIN(<LeftTable>, <RightTable>)
```

## Remarks

Tables are joined on common columns (by name) in the two tables. If the two tables have no common column names, an error is returned. There is no sort order guarantee for the results. Columns being joined on must have the same data type in both tables.