---
created: 2026-07-26
updated: 2026-08-02
source: dax.pdf
note_type: function
tags: [dax, function, window]
---

# MATCHBY

In window functions, defines the columns that are used to determine how to match data and identify the current row.

## Syntax

```dax
MATCHBY ( [<matchBy_columnName>[, ...]] )
```

## Parameters

| Term | Definition |
|------|------------|
| `matchBy_columnName` | (Optional) The name of an existing column to identify the current row in the window function's relation. RELATED() may also be used to refer to a column in a related table. |

## Return Value

This function does not return a value — it is used as a clause within window functions.

## Remarks

Can only be used within a window function expression. See OFFSET for an example. Used alongside ORDERBY and PARTITIONBY to fully define window function behavior.