---
created: 2026-07-26
updated: 2026-08-02
source: dax.pdf
note_type: function
tags: [dax, function, dax]
---

# RETURN

Returns the result of a table expression from a DAX query or a DEFINE FUNCTION body.

## Syntax

```dax
RETURN <result_expression>
```

## Parameters

| Term | Definition |
|------|------------|
| `result_expression` | A table expression (for DAX query RETURN) or scalar value (for DEFINE FUNCTION RETURN) to return. |

## Return Value

The evaluated result of the expression.

## Remarks

In DAX query language: RETURN terminates the query expression and outputs the result. In DEFINE FUNCTION: RETURN specifies what the user-defined function evaluates to.