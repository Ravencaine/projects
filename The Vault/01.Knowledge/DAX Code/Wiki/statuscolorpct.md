---
created: 2026-08-02
updated: 2026-08-02
source: One UDF, All Your KPI Colors 🎨: 3 Steps in Power BI
note_type: function
tags: [dax, udf, function, color, kpi, conditional-formatting, switch]
---

# StatusColorPct — Conditional Hex Color for KPI Indicators

Returns a hex color code based on whether a KPI value is positive, negative, or zero — with directionality and font/background mode.

```dax
DEFINE
    FUNCTION StatusColorPct =
        ( _value   : NUMERIC,
          _inverse : BOOLEAN,
          _mode    : STRING ) =>
        VAR _Normalized = IF(_inverse, -_value, _value)
        RETURN
            SWITCH(
                TRUE(),
                _Normalized > 0 && _mode = "Font",        [_Color Dark Green],
                _Normalized > 0 && _mode = "Background",  [_Color Light Green],
                _Normalized < 0 && _mode = "Font",        [_Color Dark Red],
                _Normalized < 0 && _mode = "Background",  [_Color Light Red],
                _Normalized = 0 && _mode = "Font",        [_Color Text Secondary],
                "#FFFFFF"   -- fallback
            )
```

**Logic:**
- `_inverse = FALSE` → normal polarity: increase = green
- `_inverse = TRUE` → inverted polarity: increase = red (for expenses, vacancy rate, etc.)
- `_mode = "Font"` → dark shades for readability on white
- `_mode = "Background"` → light shades for subtle cell fill

**Usage:** assign the measure to card/table visual font color `fx` or background color `fx`.

> Compare: `color-vacancy-rate-variation.md` uses the same SWITCH(TRUE()) logic but as a simple measure without `_inverse` or `_mode` — suited for single-metric use cases. `StatusColorPct` as a UDF scales to any number of KPIs.
