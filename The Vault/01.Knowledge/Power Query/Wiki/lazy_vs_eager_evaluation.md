---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: atomic
tags: ["m-language", "evaluation"]
---


# Lazy vs Eager Evaluation

M uses different evaluation strategies depending on the construct. Lists, records, and let expressions use **lazy evaluation**: they are only computed when accessed. All other expressions use **eager evaluation**: they are computed immediately.

## Key Points

- **Lazy evaluation**: lists, records, let expressions — computed only when needed
- **Eager evaluation**: primitive values, operators, function calls — computed immediately
- A list or record remembers how to compute its items, deferring until accessed
- The lookup operator `[]` (record) and index operator `{}` (list) trigger evaluation
- Understanding laziness is critical for performance in large datasets

## Examples

```m
// Record uses lazy evaluation — fields computed on access
[
    Sales = [ FirstHalf = 1000, SecondHalf = 1100 ],
    Total = Sales[FirstHalf] + Sales[SecondHalf]  // evaluated when accessed
]

// This record is equivalent after evaluation:
[
    Sales = [ FirstHalf = 1000, SecondHalf = 1100 ],
    Total = 2100
]
```

## Related

- [[m_evaluation_model]] — full evaluation model
- [[m_let_expressions]] — let also uses lazy evaluation
