---
created: 2026-07-30
updated: 2026-08-02
source: "Power Query Trick Add Leading Zeros Only When You Should.md"
note_type: snippet
tags: [text, padstart, type-guard]
---

# Conditional PadStart M Snippet

Copy-paste boilerplate for padding only N-digit numbers in a mixed-type column, leaving text and other numbers untouched.

## Code

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

**Replace in use:**
- `"Column1"` → your actual column name
- `= 3` → target number of digits
- `4` → target length after padding (one more than digit count)
- `"0"` → pad character

## When to Use

- Column has mixed numeric and text values (e.g., product codes, IDs)
- Only a specific digit-count needs padding
- Text strings and other numbers must be preserved as-is
- Output column must be `type text` for consistency

## Variations

**Add as a new column instead of replacing:**
```m
Table.AddColumn(
    Source,
    "ColumnName_Padded",
    each if Value.Is(_, type number) and Text.Length(Text.From(_)) = 3
        then Text.PadStart(Text.From(_), 4, "0")
        else Text.From(_),
    type text
)
```

**Pad to 5 digits (2-digit numbers):**
```m
= Table.TransformColumns(
    Source,
    {{"Column1",
        each if Value.Is(_, type number) and Text.Length(Text.From(_)) = 2
            then Text.PadStart(Text.From(_), 3, "0")
            else Text.From(_),
        type text}}
)
```

## Related

- [[conditional-text-padstart]] — full pattern with example table
- [[text_padstart]] — base function reference
- [[text-padstart-corrupts-mixed-columns]] — why the naive approach fails
