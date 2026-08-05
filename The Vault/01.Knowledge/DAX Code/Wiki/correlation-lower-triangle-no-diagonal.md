---
created: 2026-08-02
updated: 2026-08-05
source: How to Build a Correlation Matrix in Power BI Using Only DAX
note_type: function
tags: [dax, correlation, matrix, display, measure]
---

# Correlation (Lower Triangle, No Diagonal)

Wraps the core `Correlation` measure and hides the upper triangle and diagonal of the correlation matrix — leaving only the lower triangle visible.

## Signature

```dax
Correlation (Lower Triangle, No Diagonal) :=
VAR r     = [Correlation]
VAR XName = SELECTEDVALUE ( VariablesX[Variable] )
VAR YName = SELECTEDVALUE ( VariablesY[Variable] )
RETURN
    IF (
        ISBLANK ( r ) || ISBLANK ( XName ) || ISBLANK ( YName ),
        BLANK (),
        IF ( XName <= YName, BLANK (), r )
    )
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `[Correlation]` | measure | Core Pearson correlation measure |
| `VariablesX[Variable]` | column | Row variable name from the Matrix visual |
| `VariablesY[Variable]` | column | Column variable name from the Matrix visual |

## Returns

- The correlation value when `XName > YName` (lower triangle cells) — `BLANK()` otherwise (upper triangle and diagonal).

## Notes

- **Lexicographic ordering:** `XName <= YName` uses string comparison. For variables that might share a prefix, this is safe since the full variable names are unique in the `VariablesX`/`VariablesY` tables
- **Why hide the diagonal:** A variable always correlates perfectly with itself (r = 1), so the diagonal adds no information
- **Why hide the upper triangle:** Since correlation is symmetric (`r(X,Y) = r(Y,X)`), the upper triangle is redundant

## Related

- [[correlation-matrix-in-power-bi-dax-only]] — `pattern` — end-to-end matrix
- [[correlation-core-pearson-measure]] — `function` — the measure this wraps
