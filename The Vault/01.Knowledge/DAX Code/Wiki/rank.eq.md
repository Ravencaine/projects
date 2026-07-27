---
created: 2026-07-26
source: dax.pdf
note_type: function
tags: [dax, function, statistical]
---

# RANK.EQ

Returns the ranking of a number in a list of numbers. Returns the rank of the specified value in the given column. If two or more values are tied, all receive the same rank and the next rank value is skipped.

## Syntax

```dax
RANK.EQ(<value>, <columnName>[, <order>])
```

## Parameters

| Term | Definition |
|------|------------|
| `value` | Any DAX expression returning a single scalar value whose rank is to be found. Evaluated once before the function is evaluated. |
| `columnName` | The name of an existing column against which ranks will be determined. Cannot be an expression or a column created using ADDCOLUMNS, ROW, or SUMMARIZE. |
| `order` | (Optional) 0/FALSE = descending (default — highest number gets rank 1), 1/TRUE = ascending (lowest number gets rank 1). |

## Return Value

A number representing the rank of the specified value.