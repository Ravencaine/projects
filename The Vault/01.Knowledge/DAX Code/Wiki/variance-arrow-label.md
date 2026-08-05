---
created: 2026-08-02
updated: 2026-08-05
source: How to Conditionally Format Chart Label Backgrounds in Power BI
note_type: pattern
tags: [dax, pattern, label, arrow, formatting]
---

# Variance Arrow Label

A DAX measure that formats a variance as a signed percentage with a directional arrow prefix (↑ for positive, ↓ for negative).

## Purpose

When displaying variance on a chart label, users benefit from both the direction and the magnitude. This pattern uses `IF` to pick the correct arrow character and `FORMAT` to render the absolute value as a percentage. The result is a string like `"↑ 2.34%"` or `"↓ 1.05%"`.

## Components

1. `IF` — picks between positive and negative branch
2. `FORMAT(ABS(), "0.00%")` — formats the absolute value as a percentage
3. String concatenation with arrow prefix

## Structure

```dax
Label Variance =
VAR _Var = [Turnover Rate Variance]
RETURN
    IF(
        _Var > 0,
        "↑ " & FORMAT(_Var, "0.00%"),
        "↓ " & FORMAT(ABS(_Var), "0.00%")
    )
```

## Example Output

```
↑ 2.34%   (turnover increased — bad)
↓ 1.05%   (turnover decreased — good)
```

## Variations

- Swap arrows for `▲`/`▼` (Unicode triangles) for a more compact display
- For a more inclusive display that handles exactly zero: `IF(_Var > 0, "↑ ", IF(_Var < 0, "↓ ", "— "))`
- Use with `Label Font Color` to color-code the arrow text in addition to the label background

## Related

- [[dummy-measures-for-label-background]]
- [[Label-Font-Color-SWITCH]]
