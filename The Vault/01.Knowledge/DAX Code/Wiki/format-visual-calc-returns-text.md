---
created: 2026-08-02
updated: 2026-08-02
source: Using Visual Calculation To Easily Calculate Avg 3 Month Sales In Power BI(.pbix included).md
note_type: gotcha
tags: [dax, gotcha, format, text, visual-calculation, number-vs-text]
---

# FORMAT in Visual Calculations — Returns Text

When `FORMAT()` is applied to a numeric value inside a visual calculation, it converts the result to a text string. This has downstream consequences for sorting, further calculations, and visual behavior that are not always obvious.

## The Pattern

```dax
Avg Past 3 Months =
IF(
    ISATLEVEL([Month]),
    FORMAT(MOVINGAVERAGE([Total Sales], 3), "#,#.0")
)
```

`MOVINGAVERAGE` returns a numeric value. `FORMAT(...)` wraps it as text with thousands separators and one decimal place (e.g., `583.3`).

## The Problem

Once `FORMAT()` converts the number to text:
- The visual column becomes a **text field**, not a number
- Text sorting applies (alphabetical, not numeric)
- The value cannot be used in subsequent numeric calculations within the same visual
- Conditional formatting expecting numeric input will not apply

## Workaround

If numeric behavior is needed alongside formatting:
1. Keep the raw numeric visual calculation for sorting and further math
2. Use `FORMAT()` only on a separate display column
3. Or apply number formatting in the visual's property pane instead of via DAX `FORMAT()`

## Rule of Thumb

Use `FORMAT()` in visual calculations only when text output is intentional — display labels, concatenated strings, or formatted currencies. For numeric values that will be sorted or used in subsequent calculations, format in the visual properties pane.

## Related

- [[movingaverage-visual-calc]] — `function`
- [[isatlevel-guard-pattern]] — `pattern`
