---
created: 2026-07-30
updated: 2026-08-02
source: "Power Query Trick Add Leading Zeros Only When You Should.md"
note_type: gotcha
tags: [text, type-safety, padstart]
---

# Text.PadStart Corrupts Mixed-Type Columns

Naive `Text.PadStart` on a column containing both numbers and text will prepend the pad character to text values — silently corrupting your data.

## Expected Behaviour

You expect `Text.PadStart` to pad only numeric-looking values, leaving text strings untouched.

```
100  → "0100"    (3-digit number padded)
ABC  → "ABC"     (text unchanged)
```

## Actual Behaviour

`Text.PadStart` coerces everything to text and pads from the start regardless of original type:

```
100    → "0100"    (looks correct)
ABC    → "0ABC"    (CORRUPTED — zero prepended to string)
T-900  → "0T-900"  (CORRUPTED — zero prepended to alphanumeric)
```

## Why It Happens

`Text.PadStart(text, count, character)` accepts any value and calls `Text.From()` internally. Numbers and text strings are all coerced to text, then padded. There is no built-in type guard — Power Query does not protect you from mixed-type assumptions.

## How to Handle It

Wrap `Text.PadStart` in a type check before applying it:

```m
= Table.TransformColumns(
    Source,
    {{"Column1",
        each if Value.Is(_, type number) and Text.Length(Text.From(_)) = 3
            then Text.PadStart(Text.From(_), 4, "0")
            else Text.From(_),
        type text}}
)
```

This pattern:
1. Checks `Value.Is(_, type number)` — skips pure text values
2. Checks `Text.Length(...) = 3` — targets only N-digit numbers (e.g., 3-digit)
3. Falls through to `Text.From(_)` for all other values — preserves text and longer numbers unchanged

## Related Gotchas

[[lazy_vs_eager_evaluation]] — related M evaluation model behaviour

## Related Notes

- [[text_padstart]] — the base function reference
- [[value_is]] — type checking in M
- [[conditional-text-padstart]] — the correct pattern
- [[pad-3-digit-numbers-workflow]] — step-by-step usage workflow
