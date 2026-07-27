---
created: 2026-07-26
source: dax.pdf
note_type: function
tags: [dax, function, dax]
---

# FUNCTION

Introduces a function definition within a DEFINE statement in a DAX query. Creates a reusable named function as a model object.

## Syntax

```dax
FUNCTION <name>([param] : [type] [: subtype] [: mode], ...) => <body>
```

## Parameters

| Term | Definition |
|------|------------|
| `name` | The function name. Cannot be a reserved keyword such as MEASURE. |
| `param` | Parameter specification: name, type (anyval/scalar/table/anyref), optional subtype (boolean/datetime/decimal/double/int64/numeric/string/variant), optional passing mode (CONST/EAGER or VAR/expression-based). |
| `body` | A DAX expression defining the function body. |

## Return Value

The calculated result of the function body expression.

## Remarks

Status: Preview. Available in DEFINE FUNCTION ... END DEFINE blocks within DAX queries. Parameters can be scalar, table, or anyref types. Passing mode determines eager vs lazy evaluation.