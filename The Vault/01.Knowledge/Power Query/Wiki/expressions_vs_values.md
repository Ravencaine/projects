---
created: 2026-07-27
source: "m-code.pdf"
note_type: atomic
tags: ["m-language", "fundamentals"]
---


# Expressions vs Values

An expression is a recipe for computation; a value is the result. `1` is an expression that evaluates to the value `1`. `1 + 1` is an expression that evaluates to the value `2`. A value is not itself an expression.

## Key Points

- An **expression** is the recipe — a formula you write
- A **value** is the result — what you get after evaluation
- Expressions are **recipes**: `1 + 1` and `2` are different expressions that yield the same value
- A value cannot be evaluated further — it is final
- Understanding the distinction matters for let expressions and scoping

## Examples

```m
// These are two different expressions yielding the same value:
1 + 1        // expression → value 2
2           // expression → value 2

// Records can contain deferred computations
[
    A1 = A2 * 2,
    A2 = A3 + 1,
    A3 = 1
]
// This evaluates to [A1 = 4, A2 = 2, A3 = 1]
```

## Related

- [[m_evaluation_model]] — when and how expressions are evaluated
- [[m_let_expressions]] — naming intermediate values
