---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["rowexpression", "m-function"]
---


# RowExpression.From

Returns the abstract syntax tree (AST) for the body of function, normalized into a row expression: The function must be a 1-argument lambda. All references to the function parameter are replaced with RowExpression.Row. All references to columns are replaced with RowExpression.Column(columnName). The AST will be simplified to contain only nodes of the kinds: Constant Invocation Unary Binary If FieldAccess An error is raised if a row expression AST cannot be returned for the body of function. This function is identical to ItemExpression.From. Example Returns the AST for the body of the function each [CustomerID] = "ALFKI". Usage Power Query M RowExpression.From(each [CustomerName] = "ALFKI") Output Power Query M --- PAGE 944 --- [ Kind = "Binary", Operator = "Equals", Left = RowExpression.Column("CustomerName"), Right = [ Kind = "Constant", Value = "ALFKI" ] ] Last updated on 03/24/2026 --- PAGE 945 ---

## Signature

```m
RowExpression.From(function as function) as record
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| function | function | |

## Returns

record

