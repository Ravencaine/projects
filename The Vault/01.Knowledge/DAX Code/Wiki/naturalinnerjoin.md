---
created: 2026-07-26
updated: 2026-08-02
source: dax.pdf
note_type: function
tags: [dax, function, table]
---

# NATURALINNERJOIN

Applies to: Calculated column Calculated table Measure Visual calculation Performs an inner join of a table with another table.

## Syntax

```dax
NATURALINNERJOIN(<LeftTable>, <RightTable>)
```

## Remarks

Tables are joined on common columns (by name) in the two tables. If the two tables have no common column names, an error is returned. There is no sort order guarantee for the results. Columns being joined on must have the same data type in both tables.