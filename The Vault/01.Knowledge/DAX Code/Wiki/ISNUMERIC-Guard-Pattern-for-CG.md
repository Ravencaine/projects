---
created: 2026-08-08
updated: 2026-08-08
source: "Create calculation groups in Power BI"
source_url: https://learn.microsoft.com/en-us/power-bi/transform-model/calculation-groups
note_type: pattern
tags: [calculation-groups, isnumeric, guard, dax, power-bi]
---

# ISNUMERIC Guard Pattern for Calculation Groups

Use `ISNUMERIC()` inside a calculation item expression to check whether the active measure is numeric before applying a math operation — preventing **Cannot convert value... of type Text to type Numeric** errors on non-numeric measures.

## Purpose

Calculation items are reusable across any measure placed in a visual. Non-numeric measures — commonly used for dynamic titles and dynamic format strings — will error if a math operation (e.g., multiplication, division) is applied to them. The `ISNUMERIC` guard short-circuits the calculation item for non-numeric measures.

## Pattern

```dax
Calculation item safe =
    IF(
        // Check the measure is numeric before applying math
        ISNUMERIC(SELECTEDMEASURE()),
        // Apply the calculation only to numeric measures
        SELECTEDMEASURE() * 1.1,
        // Pass through non-numeric measures unchanged
        SELECTEDMEASURE()
    )
```

## Common Use Cases

| Scenario | Non-numeric measure affected |
|----------|------------------------------|
| Multiplication (e.g., 10% uplift) | Percentage format strings, margin ratios |
| Division (e.g., YOY change) | Dynamic format string measures |
| Running total | Measures used for dynamic titles |

## Why Not ISERROR or HASONEVALUE?

`ISERROR` catches the error after it fires but leaves the visual in an error state briefly. `ISNUMERIC` is a proactive guard — it prevents the error from occurring by checking the measure type before the math operation runs.

`HASONEVALUE` checks whether a single value is selected on a column — it is not a measure type check and does not prevent the type conversion error.

## Related

- [[CG-Variant-Data-Type-Gotcha]] — variant data type side effect (companion gotcha)
- [[Calculation-Groups]] — where this pattern fits in CG usage
- [[ISNUMERIC]] — the underlying DAX function
