---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: atomic
tags: ["m-language", "control-flow"]
---


# If Expressions (Conditionals)

The if expression selects between two expressions based on a logical condition. It follows the form: `if <condition> then <true_expr> else <false_expr>`.

## Key Points

- The condition must evaluate to a logical (true/false) value
- Both the true and false branches are expressions — they produce values
- Only the selected branch is evaluated (lazy in practice)
- `if` expressions can be nested
- No `elsif` — use nested if expressions or logical operators

## Examples

```m
if 2 > 1 then
    2 + 2
else
    1 + 1  // evaluates to 4

// Nested if
if Units = 0 then
    error "No Units"
else
    Revenue / Units

// Using logical operators for multiple conditions
if Status = "Active" and Score > 50 then
    "Approved"
else
    "Rejected"
```

## Related

- [[m_let_expressions]] — conditionals often used inside let
- [[m_error_handling_with_try]] — combining if with error handling
