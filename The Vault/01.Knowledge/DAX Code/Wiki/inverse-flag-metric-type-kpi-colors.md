---
created: 2026-08-02
source: One UDF, All Your KPI Colors 🎨: 3 Steps in Power BI
note_type: pattern
tags: [dax, pattern, udf, color, kpi, inverse, expenses]
---

# Metric-Specific Inverse Flag in KPI Color UDFs

The `_inverse` parameter maps metric type to color logic:

| Metric type | `_inverse` | Color logic |
|------------|------------|-------------|
| Income, revenue, profit | `FALSE` | Increase = green |
| Expenses, costs, vacancy rate | `TRUE` | Increase = red |

`_inverse = TRUE` flips the sign before the SWITCH so the same branches return red for increases even when the underlying value is positive.

**Why it matters:** without this flag, each metric type would need its own color UDF. The flag makes the UDF universal across any KPI that follows a "good/bad" direction.

**Example calls:**
```dax
Font Color Income Variation   = StatusColorPct([Income % Variation],  FALSE, "Font")
Font Color Expense Variation  = StatusColorPct([Expense % Variation], TRUE, "Font")
```
