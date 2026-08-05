---
created: 2026-08-02
source: One UDF to Build All Your SVG Pills in Power BI
note_type: pattern
tags: [dax, pattern, svg, pill, status, switch, selectedvalue]
---

# Task Status Pill — SELECTEDVALUE + Color Maps → UDF Call

A pill measure that maps a `Status` column value to color measures, then calls `UDF_SVGPillCanvas`.

```dax
Task Status Pill :=
VAR _label     = SELECTEDVALUE(Tasks[Status])
VAR _bgColor  = [Status Background Color]   -- SWITCH: Completed→mint, In Progress→blue, At Risk→red
VAR _borderC  = [Status Border Color]        -- same SWITCH or distinct mapping
VAR _textC    = [_ColorTextDark]
VAR _dotC     = [Status Border Color]

RETURN
    IF(
        ISBLANK(_label),
        BLANK(),
        UDF_SVGPillCanvas(
            _label,
            _bgColor,
            _borderC,
            _textC,
            1,      -- showBorder = on
            _dotC,
            0       -- showDot = off (clean outline pill)
        )
    )
```

**Architecture:** `SELECTEDVALUE` extracts the current row's column value. Dedicated color measures (`[Status Background Color]`, etc.) hold the SWITCH mappings — keeping color logic separate from UDF call makes the pill reusable across reports without touching the UDF itself.

**Variants:** change only the `showDot` and `showBorder` parameters for filled vs. outline pills.
