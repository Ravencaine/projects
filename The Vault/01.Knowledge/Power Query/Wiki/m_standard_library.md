---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: atomic
tags: ["m-language", "library"]
---


# M Standard Library

M includes a standard library — a set of named values and functions available in every expression without explicit definition. Examples include `Number.E`, `Text.PositionOf`, and all `List.*`, `Table.*`, `Text.*` functions.

## Key Points

- The **standard library** is always in scope
- Library names include value constants (e.g., `Number.E`, `Number.PI`)
- Library names include all built-in functions (Table, List, Text, Date, etc.)
- Library definitions are pre-computed and optimised
- You can extend the library using let expressions and sections

## Examples

```m
Number.E           // Euler's number: 2.7182...
Number.PI          // Pi: 3.1415...
Text.PositionOf("Hello", "ll")  // 2
List.Count({1, 2, 3})          // 3
```

## Related

- [[m_functions_as_values]] — all library functions are values
- [[m_evaluation_model]] — library values are pre-computed
