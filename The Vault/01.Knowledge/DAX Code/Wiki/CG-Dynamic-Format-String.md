---
created: 2026-08-08
updated: 2026-08-08
source: "Create calculation groups in Power BI"
source_url: https://learn.microsoft.com/en-us/power-bi/transform-model/calculation-groups
note_type: pattern
tags: [calculation-groups, dynamic-format-string, dax, power-bi]
---

# CG Dynamic Format String Pattern

Calculation items can override the format of the underlying measure using a dynamic format string — enabling percentage, currency, or custom formatting that applies only when a specific calculation item is active.

## Purpose

When a calculation item performs a transformation that changes the unit or scale of the measure (e.g., converting a raw sales figure to a YOY% change), the measure's built-in format string no longer matches. A dynamic format string keeps the visual clean without requiring separate measures for each format variant.

## Pattern

### Via Power BI Properties Pane

1. Select the calculation item in Model View
2. In the **Properties** pane, enable **Dynamic format string**
3. Enter the format string expression — can be a literal or a DAX expression

```
#,##0.00%
```

### Via TMDL

```tmdl
calculationItem 'YOY%'
    expression = SELECTEDMEASURE()
    formatStringExpression = "#,##0.00%"
```

## Example

A `YOY%` calculation item:

```dax
CALCULATE(
    SELECTEDMEASURE(),
    SAMEPERIODLASTYEAR('Date'[Date])
) / CALCULATE(
    SELECTEDMEASURE(),
    SAMEPERIODLASTYEAR('Date'[Date]),
    REMOVEFILTERS('Date')
)
```

With dynamic format string `#,##0.00%`, the result displays as `12.50%` instead of `0.125`.

## Dynamic Format String with DAX Expression

The format string itself can be a DAX expression for conditional formatting:

```dax
IF(
    SELECTEDMEASUREFORMATSTRING() = "$#,##0",
    "$#,##0.00",
    SELECTEDMEASUREFORMATSTRING()
)
```

## Gotcha — Variant Data Type

When a calculation group is added to a model, all measures become **variant** data type. This can break dynamic format string reuse patterns where one measure's format string references another measure. See [[CG-Variant-Data-Type-Gotcha]].

## Related

- [[CG-Variant-Data-Type-Gotcha]] — variant data type side effect
- [[ISNUMERIC-Guard-Pattern-for-CG]] — companion guard for non-numeric measures
- [[Currency-Conversion-Format-String-Pattern]] — format string in currency conversion CGs
- [[Format-String-Expression-in-Calculation-Groups]] — formatStringExpression DAX syntax
