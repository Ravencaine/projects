---
created: 2026-07-27
source: "m-code.pdf"
note_type: function
tags: ["rowexpression", "m-function"]
---


# RowExpression.Column

Returns an abstract syntax tree (AST) that represents access to column columnName of the row within a row expression.

## Signature

```m
RowExpression.Column(columnName as text) as record
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| columnName | text | |

## Returns

record

### Example 1

Creates an AST representing access of column "CustomerName".

```m
RowExpression.Column("CustomerName")
```

// Output
```
[
Kind = "FieldAccess",
Expression = RowExpression.Row,
MemberName = "CustomerName"
]
```

