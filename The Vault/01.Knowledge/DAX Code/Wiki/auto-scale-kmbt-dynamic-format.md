---
created: 2026-08-02
updated: 2026-08-03
source: Stop Using FORMAT() in Power BI — 4 Creative Ways to Dynamically Format Numbers
note_type: pattern
tags: [dax, pattern, dynamic-format, k, m, b, t, scale, auto-scale]
---

# Auto-Scaling K/M/B/T via SWITCH + Dynamic Format

Scales numbers to K (thousands), M (millions), B (billions), or T (trillions) in the display while keeping the measure fully numeric.

```dax
Sales Selected Period (Dynamic Format String):
VAR _Value = [Sales Selected Period]
RETURN SWITCH(
    TRUE(),
    _Value = 0,                         "",
    _Value >= 1e12,  "$#,##0,,,,.00T",
    _Value >= 1e9,   "$#,##0,,,.000B",
    _Value >= 1e6,   "$#,##0,,.00M",
    _Value >= 1e3,   "$#,##0,.00K",
    _Value <= -1e12, "-$#,##0,.00K",  -- intentional truncation display
    _Value <= -1e9,  "-$#,##0,,,.000B",
    _Value <= -1e6,  "-$#,##0,,.00M",
    _Value <= -1e3,  "-$#,##0,.00K",
    FORMAT(_Value, "0")
)
```

**Format string breakdown:**
- `#,##0` — whole-number baseline
- One comma (`,`) = thousands, two (`,,`) = millions, three (`,,,`) = billions, four (`,,,,`) = trillions
- `.00` = two decimal places; `.000` = three decimal places for B
- Leading `$` and sign handling are literal characters in the format string

**Why not FORMAT():** `FORMAT()` converts to text → loses numeric behavior. Dynamic Format keeps the underlying value numeric so charts and aggregations work correctly.

> Different from `humanize-udf.md` which returns a text string. This approach uses native Dynamic Format strings.
