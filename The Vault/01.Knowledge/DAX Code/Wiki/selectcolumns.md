---
created: 2026-07-26
source: dax.pdf
note_type: function
tags: [dax, function, table]
---

# SELECTCOLUMNS

Applies to: Calculated column Calculated table Measure Visual Returns a table with selected columns from the table and new columns specified by the

## Syntax

```dax
SELECTCOLUMNS(<Table>, [<Name>], <Expression>, [<Name>], …)
```

## Remarks

SELECTCOLUMNS has the same signature as ADDCOLUMNS, and has the same behavior except that instead of starting with the Table specified, SELECTCOLUMNS starts with an empty table before adding columns.