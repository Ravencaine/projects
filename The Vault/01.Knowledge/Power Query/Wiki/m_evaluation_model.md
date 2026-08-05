---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: atomic
tags: ["m-language", "evaluation"]
---


# M Evaluation Model

M's evaluation model is similar to spreadsheet cell evaluation — expressions are evaluated in dependency order, determined by references between named values.

## Key Points

- Expressions reference other values by name
- The evaluator builds a dependency graph and computes in topological order
- Circular references are detected and produce an error
- Lazy constructs (records, lists, let) defer computation until accessed
- Eager constructs (primitives, operators, function calls) are computed immediately

## Examples

```m
// The evaluator determines A2 depends on A3, A1 depends on A2
[
    A1 = A2 * 2,
    A2 = A3 + 1,
    A3 = 1
]
// Evaluates to [A1 = 4, A2 = 2, A3 = 1]
```

## Related

- [[lazy_vs_eager_evaluation]] — lazy vs eager strategies
- [[m_let_expressions]] — let evaluation
