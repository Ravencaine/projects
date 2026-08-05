---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: function
tags: ["expression", "m-function"]
---


# Expression.Evaluate

Returns the result of evaluating an M expression document, with the available identifiers that can be referenced defined by environment.

## Signature

```m
Expression.Evaluate(document as text, optional environment as nullable record) as
any
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| document | text | |
| optional environment | nullable record | |

## Returns

any

### Example 1

Evaluate a simple sum.

```m
Expression.Evaluate("1 + 1")
```

// Output
```
2
```

### Example 2

Evaluate a more complex sum.

```m
Expression.Evaluate("List.Sum({1, 2, 3})", [List.Sum = List.Sum])
```

// Output
```
6
```

### Example 3

Evaluate the concatenation of a text value with an identifier.

```m
Expression.Evaluate(Expression.Constant("""abc") & " & " &
Expression.Identifier("x"), [x = "def"""])
```

// Output
```
"""abcdef"""
```

