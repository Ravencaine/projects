---
created: 2026-08-08
updated: 2026-08-08
source: 11 Power BI Tips
note_type: pattern
tags: [dax, power-bi, switch, conditional-logic]
---

# SWITCH TRUE vs Nested IF

Replace deeply nested IF statements with `SWITCH(TRUE(), ...)` for better readability and maintainability.

## Purpose

When conditional logic grows beyond 2-3 levels, nested `IF` statements become hard to read and error-prone. `SWITCH(TRUE(), ...)` makes the intent explicit and is far easier to extend.

## Structure

```dax
MeasureName =
VAR PortfolioTotal = [Portfolio Total]
RETURN
    SWITCH(
        TRUE(),
        NOT ISINSCOPE(Product[Property]), PortfolioTotal,
        [Total Revenue] >= 35000000, "Exceptional",
        [Total Revenue] >= 25000000, "Strong",
        [Total Revenue] >= 15000000, "Moderate",
        "Low"
    )
```

## Example

Nested IF:
```dax
MeasureName = IF(NOT ISINSCOPE(Product[Property]), [Portfolio Total],
    IF([Total Revenue] >= 35000000, "Exceptional",
        IF([Total Revenue] >= 25000000, "Strong",
            IF([Total Revenue] >= 15000000, "Moderate", "Low")
        )
    )
)
```

SWITCH TRUE:
```dax
MeasureName =
VAR PortfolioTotal = [Portfolio Total]
RETURN
    SWITCH(
        TRUE(),
        NOT ISINSCOPE(Product[Property]), PortfolioTotal,
        [Total Revenue] >= 35000000, "Exceptional",
        [Total Revenue] >= 25000000, "Strong",
        [Total Revenue] >= 15000000, "Moderate",
        "Low"
    )
```

## Variations

- Order conditions from **highest to lowest** threshold — SWITCH stops at the first TRUE
- Can combine with `ISINSCOPE()`, `HASONEVALUE()`, or any boolean expression
- Fallback value (no conditions match) goes after the last comma

## Related

- [[calculate]] — DAX CALCULATE context
- [[Field-Parameters-Dynamic-Visuals]] — dynamic conditional logic via field parameters
