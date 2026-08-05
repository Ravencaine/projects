---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: gotcha
tags: ["m-language", "evaluation", "performance"]
---


# List and Record Literals Use Lazy Evaluation — Not Computed Until Accessed

When you write a list or record literal, the inner expressions are **not evaluated immediately**. They are only computed when you access a field or list item.

## Expected Behaviour

The following should produce an error because the list contains an error expression:
```
let
    Source = {1, 2, error "boom"}
in
    Source
```

## Actual Behaviour

No error occurs — the list is created successfully. The `error "boom"` expression is never evaluated because no item is accessed.

## Why It Happens

Lists and records use **lazy evaluation**: items are computed only on demand. This is an optimization for large datasets.

## How to Handle It

- Access at least one item to trigger evaluation: `Source{0}` forces the error
- Use eager evaluation patterns (e.g., `List.Accumulate`) when immediate computation is needed
- Be aware that `List.Transform`, `Record.AddField` etc. force evaluation of their contents
