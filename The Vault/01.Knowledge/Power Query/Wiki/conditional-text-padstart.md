---
created: 2026-07-30
updated: 2026-08-02
source: "Power Query Trick Add Leading Zeros Only When You Should.md"
note_type: pattern
tags: [text, type-safety, conditional, padstart]
---

# Conditional Text.PadStart

Applies `Text.PadStart` only to numeric values of a specific length, leaving all other values (text, longer/shorter numbers) untouched and coercing the entire column to text type.

## Purpose

Used when a column contains mixed data types — some numeric codes of a fixed length that need zero-padding, alongside text strings or numbers of other lengths that must be left as-is. Naive `Text.PadStart` would corrupt the text values.

## Components

- `Value.Is(_, type number)` — guards against non-numeric values
- `Text.Length(Text.From(_)) = N` — targets only N-digit numbers
- `Text.PadStart(Text.From(_), N+1, "0")` — applies the padding
- `else Text.From(_)` — preserves everything else unchanged
- `Table.TransformColumns` — applies the transformation in-place

## Structure

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

## Example

Given column `Column1` with mixed values:

| Column1 (input) | Column1 (output) |
|-----------------|------------------|
| 100             | "0100"           |
| 1001            | "1001"           |
| "ABC"           | "ABC"            |
| "T-900"         | "T-900"          |
| 10010           | "10010"          |

The formula targets only 3-digit numbers and pads them to 4 digits. All other values are preserved as text.

## Variations

**Different target length:** Change `Text.Length(...) = 3` and `Text.PadStart(..., 4, "0")` together:
- For 2-digit numbers → `= 2` and pad to `3`
- For 5-digit numbers → `= 5` and pad to `6`

**Different pad character:** Replace `"0"` with any character:
```m
Text.PadStart(Text.From(_), 6, " ")
```

**Using Table.AddColumn (adds new column instead of replacing):**
```m
= Table.AddColumn(
    Source,
    "Column1_Padded",
    each if Value.Is(_, type number) and Text.Length(Text.From(_)) = 3
        then Text.PadStart(Text.From(_), 4, "0")
        else Text.From(_),
    type text
)
```

## Related

- [[text_padstart]] — base function reference
- [[text-padstart-corrupts-mixed-columns]] — the gotcha this pattern solves
- [[pad-3-digit-numbers-workflow]] — step-by-step workflow
