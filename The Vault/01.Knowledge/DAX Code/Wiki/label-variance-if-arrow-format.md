---
created: 2026-08-02
source: How to Conditionally Format Chart Label Backgrounds in Power BI
note_type: function
tags: [dax, formatting, text, label, arrow, switch, if]
---

# Label Variance — Arrow + % Text Formatting

Formats a variance as a display label with direction arrow and percentage.

## Pattern

```c
Label Variance =
VAR _Var = [Variance Measure]
RETURN
    IF(
        _Var > 0,
        "↑ " & FORMAT(_Var, "0.00%"),
        "↓ " & FORMAT(ABS(_Var), "0.00%")
    )
```

## Output Examples

| Variance | Label |
|----------|-------|
| +0.0523 | `↑ 5.23%` |
| -0.0310 | `↓ 3.10%` |
| 0 | `↓ 0.00%` |

## Usage

- Assign to **Data label → Value** for all chart series
- Pair with [[label-font-color-variance-based]] for color-coded labels
- Works across all bar, column, and line chart data labels

## Related

- [[FORMAT]] — FORMAT function reference
- [[label-font-color-variance-based]]
- [[dual-measure-label-background-trick]]
