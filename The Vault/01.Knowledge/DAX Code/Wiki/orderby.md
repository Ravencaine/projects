---
created: 2026-07-26
source: dax.pdf
note_type: function
tags: [dax, function, window]
---

# ORDERBY

Defines the expressions that determine the sort order within each partition of a window function.

## Syntax

```dax
ORDERBY ( [<orderBy_expression>[, <order>[, <blanks>]][, ...]] )
```

## Parameters

| Term | Definition |
|------|------------|
| `orderBy_expression` | (Optional) Any scalar expression that will be used to sort the data within each partition. |
| `order` | (Optional) ASC (ascending, default) or DESC (descending). Alternatives: 1/TRUE for ASC, 0/FALSE for DESC. |
| `blanks` | (Optional) BLANKS DEFAULT (default — blanks ordered between zero and negatives for numbers, before strings for text) or BLANKS FIRST (blanks always first regardless of direction). |

## Return Value

This function does not return a value — it is used as a clause within window functions.

## Remarks

Defaults to ordering by every column in relation not already specified in PARTITIONBY when omitted. See OFFSET for usage examples.