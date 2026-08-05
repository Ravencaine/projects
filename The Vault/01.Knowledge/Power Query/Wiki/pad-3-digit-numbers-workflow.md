---
created: 2026-07-30
updated: 2026-08-02
source: "Power Query Trick Add Leading Zeros Only When You Should.md"
note_type: workflow
tags: [text, padstart, data-cleaning]
---

# Pad 3-Digit Numbers in Mixed-Type Column

Steps to pad only 3-digit numbers to 4 digits in a column that also contains text strings and other numeric values, without corrupting the non-target values.

## Prerequisites

- Power Query Editor open with your table loaded
- Column contains a mix of numeric codes (3-digit, 4-digit, etc.) and text strings

## Steps

### 1. Open Advanced Editor (optional)

If you prefer writing M directly, open **Advanced Editor** from the Home tab. Otherwise, use the custom column UI.

### 2. Add a Custom Column (or replace existing)

**Option A — Replace existing column:**
Open **Advanced Editor** and add a new step after your source. Paste the transformation:

```m
= Table.TransformColumns(
    #"PreviousStep",
    {{"Column1",
        each if Value.Is(_, type number) and Text.Length(Text.From(_)) = 3
            then Text.PadStart(Text.From(_), 4, "0")
            else Text.From(_),
        type text}}
)
```

**Option B — Add as new column (safer, non-destructive):**
Use **Add Column → Custom Column** with this formula:

```m
if Value.Is([Column1], type number) and Text.Length(Text.From([Column1])) = 3
    then Text.PadStart(Text.From([Column1]), 4, "0")
    else Text.From([Column1])
```

Name the new column (e.g., `Column1_Padded`) and set its type to `Text`.

### 3. Verify output

Check that:
- 3-digit numbers became 4-digit strings (`100` → `"0100"`)
- 4-digit and 5-digit numbers are unchanged (`1001` → `"1001"`)
- Text values are unchanged (`"ABC"` → `"ABC"`, `"T-900"` → `"T-900"`)
- All values are `Text` type

### 4. Rename / remove original column (if using Option B)

If you added a new column, rename it to replace the original or remove the original if no longer needed.

## Variations

| Target | Change `= 3` to | Change pad length to |
|--------|-----------------|----------------------|
| 2-digit numbers | `= 2` | `3` |
| 4-digit numbers | `= 4` | `5` |
| 5-digit numbers | `= 5` | `6` |

## Common Errors

- **`Text.PadStart` applied to text** → causes `ABC` → `"0ABC"`. Fix: always wrap with `Value.Is(_, type number)` guard.
- **All numbers padded** → the `Text.Length(...)` condition is missing or wrong. Adjust to match the exact digit count you want to target.

## Related

- [[conditional-text-padstart]] — the pattern with full example table
- [[text-padstart-corrupts-mixed-columns]] — the gotcha this workflow avoids
- [[text_padstart]] — base function reference
