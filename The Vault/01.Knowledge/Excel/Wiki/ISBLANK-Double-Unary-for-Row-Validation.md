---
created: 2026-08-09
updated: 2026-08-09
source: "Advanced Conditional Formatting in Excel Using Formulas • My Online Training Hub"
note_type: atomic
tags: [excel, conditional-formatting, isblank, double-unary, array, row-validation, missing-data]
---

# ISBLANK + Double Unary for Row Validation

`=SUM(--ISBLANK($C5:$H5))` flags any row where one or more cells are blank. ISBLANK returns a TRUE/FALSE array; double unary converts to 1/0; SUM reduces it to a single number for the conditional format.

## Formula

```
=SUM(--ISBLANK($C5:$H5))
```

## How It Breaks Down

| Step | Expression | Result |
|------|-----------|--------|
| 1 | `ISBLANK($C5:$H5)` | `{FALSE, TRUE, FALSE, FALSE, FALSE, TRUE}` |
| 2 | `--{FALSE, TRUE, ...}` | `{0, 1, 0, 0, 0, 1}` |
| 3 | `SUM({0,1,0,0,0,1})` | `2` |

`SUM(--ISBLANK(...))` returns a number. CF treats anything > 0 as TRUE → row gets formatted.

## Why Double Unary

Conditional formatting formulas must return a single scalar value. Without `--`, the TRUE/FALSE array from ISBLANK can't be coerced directly. Double unary converts to numeric 1/0, then SUM collapses the array to one number.

## Use Cases

- Contact lists: flag rows with missing email, phone, or manager
- Orders: flag incomplete rows before processing
- Any data entry sheet: quality control highlighting

## Related

- [[Source-Advanced-Conditional-Formatting-Formulas-Mynda-Treacy]] — source
