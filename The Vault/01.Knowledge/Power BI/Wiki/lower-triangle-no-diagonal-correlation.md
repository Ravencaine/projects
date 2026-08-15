---
created: 2026-08-02
updated: 2026-08-05
source: How to Build a Correlation Matrix in Power BI Using Only DAX.md
note_type: pattern
tags: [powerbi, dax, correlation, matrix, conditional-display]
---

# Lower Triangle, No Diagonal Correlation

A DAX measure that wraps `Correlation` to display only the lower triangle of the matrix and hide the diagonal (where a variable is correlated with itself = 1).

## Formula

```c
Correlation (Lower Triangle, No Diagonal) =
VAR r     = [Correlation]
VAR XName = SELECTEDVALUE ( VariablesX[Variable] )
VAR YName = SELECTEDVALUE ( VariablesY[Variable] )
RETURN
    IF (
        ISBLANK ( r ) || ISBLANK ( XName ) || ISBLANK ( YName ),
        BLANK (),
        IF ( XName <= YName, BLANK (), r )   -- hides upper triangle AND diagonal
    )
```

## Logic

- Returns `BLANK()` when `XName <= YName`. This condition removes:
  - The **diagonal** (where X = Y, e.g., Performance Rating vs. Performance Rating = 1)
  - The **upper triangle** (where X > Y in alphabetical order)
- Returns `r` only for the **lower triangle:** where X precedes Y alphabetically.

## Effect on the Matrix Visual

| Cell | Condition | Result |
|------|-----------|--------|
| Diagonal (X = Y) | `XName <= YName` is TRUE | BLANK |
| Upper triangle | `XName <= YName` is TRUE | BLANK |
| Lower triangle | `XName <= YName` is FALSE | Correlation value |

## Notes

- The `ISBLANK` guard prevents errors when no variable is selected in rows or columns.
- This measure is the one to use as the **Values** field in the Matrix visual.
- Use this as the base measure for `Correlation Color (Buckets)` and `Correlation Font Color` as well.

## Related

- [[pearson-correlation-measure]]
- [[correlation-color-buckets]]
