---
created: 2026-08-05
source: Blank Values in Power BI Reports (Boniface Muchendu)
note_type: pattern
tags: [dax, pattern, blank, isblank, if, implicit]
---

# `IF([Measure], [Measure], "N/A")` — Implicit Blank Check

DAX `IF` evaluates the first argument in a boolean context. Passing a measure directly — without wrapping in `ISBLANK` — treats a blank return as `FALSE`, making this a compact one-argument blank check.

## Definition

```dax
Sales No Blank = IF([Sales], [Sales], "N/A")
```

When `[Sales]` returns `BLANK`, IF treats it as `FALSE` and returns `"N/A"`. When it returns a value, IF returns that value.

## Explicit Form (equivalent)

```dax
Sales No Blank = IF(ISBLANK([Sales]), "N/A", [Sales])
```

Both forms are functionally identical. The implicit form is shorter.

## When to Use

- Any visual (card, table, matrix) where you want custom text instead of blank
- Measures that return text (use quotes for the fallback) or numbers (use `0` or another numeric fallback)

## Variations

```dax
// Numeric fallback: blank becomes 0
Sales No Blank = IF([Sales], [Sales], 0)

// Custom text fallback
Status No Blank = IF([Status], [Status], "No Data")
```

## Why Not Always Use Implicit Form

- Explicit `ISBLANK` is clearer to readers unfamiliar with the implicit-blank behaviour
- The implicit form breaks if `[Sales]` could legitimately return `0` — `IF(0, ...)` treats `0` as `FALSE`, so `0` would be shown as `"N/A"`. Use `ISBLANK` explicitly when `0` is a valid measure result.

## Related

- [[Plus-Zero-Blanks-Atomic]]
- [[Choosing-Blank-Value-Strategy]]
- [[New-Card-Visual-Blank-Setting]]
