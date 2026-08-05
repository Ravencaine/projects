---
created: 2026-08-02
source: One UDF, All Your KPI Colors 🎨: 3 Steps in Power BI
note_type: pattern
tags: [dax, pattern, udf, color, kpi, font, background, visual-formatting]
---

# One-Liner UDF Call per Color Property (Font + Background)

Each color indicator needs two calls to `StatusColorPct` — one for font color, one for background — assigned to separate visual formatting properties.

```dax
Font Color Cash Flow Variation =
    StatusColorPct([Cash Flow % Variation], FALSE, "Font")

Background Color Cash Flow Variation =
    StatusColorPct([Cash Flow % Variation], FALSE, "Background")
```

Assign `Font Color ...` to the visual's font color `fx` field, `Background Color ...` to the background color `fx` field.

**One-liner pattern:** the call is always three arguments — value, inverse flag, mode — making every metric's color measures follow the same shape and trivially auditable.
