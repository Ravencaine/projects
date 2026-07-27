---
created: 2026-07-26
source: dax.pdf
note_type: function
tags: [dax, function, window]
---

# PARTITIONBY

Defines the columns that are used to partition a window function's relation parameter.

## Syntax

```dax
PARTITIONBY ( [<partitionBy_columnName>[, ...]] )
```

## Parameters

| Term | Definition |
|------|------------|
| `partitionBy_columnName` | (Optional) The name of an existing column to partition the window function's relation. RELATED() may be used to refer to a column in a related table. |

## Return Value

This function does not return a value — it is used as a clause within window functions.

## Remarks

Can only be used within a window function expression. See OFFSET for an example. Used alongside ORDERBY and optionally MATCHBY.