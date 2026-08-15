---
created: 2026-08-02
updated: 2026-08-02
source: One UDF, All Your KPI Colors 🎨: 3 Steps in Power BI
note_type: pattern
tags: [dax, pattern, udf, color, kpi, inverse, conditional-formatting]
---

# UDF Pattern: StatusColorPct — Three-Parameter Architecture

A reusable KPI color UDF that accepts: the metric value, an inverse flag, and the color mode.

**Parameters:**
- `_value` — the KPI metric (e.g. `% Variation`)
- `_inverse` — `FALSE` = higher is better (income); `TRUE` = lower is better (expenses, vacancy rate)
- `_mode` — `"Font"` returns dark shades; `"Background"` returns light shades

**Normalized value** is the core design element: `IF(_inverse, -_value, _value)` flips the sign so the same SWITCH branches work for both directions.

**Why three parameters:**
- `_value` makes the UDF metric-agnostic (call it for any KPI)
- `_inverse` handles the directionality of different metric types without duplicating the UDF
- `_mode` returns the right shade for font vs. background contexts

**Pattern:** define one UDF in the model; every metric gets a one-liner call passing its value and direction.
