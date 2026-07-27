---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["itemexpression", "m-function"]
---


# ItemExpression.From

Returns the abstract syntax tree (AST) for the body of function, normalized into an item expression: The function must be a 1-argument lambda. All references to the function parameter are replaced with ItemExpression.Item. The AST will be simplified to contain only nodes of the kinds: Constant Invocation Unary Binary If FieldAccess An error is raised if an item expression AST cannot be returned for the body of function. This function is identical to RowExpression.From.

## Signature

```m
ItemExpression.From(function as function) as record
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| function | function | |

## Returns

record

### Example 1

Returns the AST for the body of the function each _ <> null.

```m
ItemExpression.From(each _ <> null)
```

// Output
```
[
Kind = "Binary",
Operator = "NotEquals",
Left = ItemExpression.Item,
Right =
[
Kind = "Constant",
Value = null
]
]
```

