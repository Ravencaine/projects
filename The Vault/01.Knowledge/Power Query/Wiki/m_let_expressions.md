---
created: 2026-07-27
source: "m-code.pdf"
note_type: atomic
tags: ["m-language", "syntax"]
---


# Let Expressions

A let expression assigns names to values and expressions, which are then used in a final expression after the `in` keyword. Let expressions allow you to build up complex transformations step by step.

## Key Points

- `let` introduces named values; `in` declares the output
- Variables can reference earlier variables in the same let block
- Variable names can contain spaces using `#"Variable name"` syntax
- Let expressions use **lazy evaluation**: inner expressions are only computed when referenced
- Each variable definition ends with a comma except the last before `in`

## Structure

```m
let
    VariableName = expression,
    #"Variable with spaces" = expression2,
    AnotherVar = VariableName + 1
in
    AnotherVar
```

## Examples

```m
let
    Sales2007 = [Year = 2007, FirstHalf = 1000, SecondHalf = 1100,
                 Total = FirstHalf + SecondHalf],
    Sales2008 = [Year = 2008, FirstHalf = 1200, SecondHalf = 1300,
                 Total = FirstHalf + SecondHalf],
    TotalSales = Sales2007[Total] + Sales2008[Total]
in
    TotalSales  // 4600
```

## Related

- [[m_evaluation_model]] — let uses lazy evaluation
- [[expressions_vs_values]] — let creates named values
