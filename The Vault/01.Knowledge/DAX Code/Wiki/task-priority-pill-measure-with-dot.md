---
created: 2026-08-02
updated: 2026-08-05
source: One UDF to Build All Your SVG Pills in Power BI
note_type: pattern
tags: [dax, power-bi, svg, pill, priority, visualization, dot]
---

# Task Priority Pill Measure (with dot)

Renders a neutral-outline SVG pill for task priority, with a colored dot carrying the intensity signal. The pill background is white; the border is dark; the dot color changes per priority level.

## Purpose

Show task priorities (High / Medium / Low) as outline pills where the dot color — not the background — signals urgency. The neutral pill design avoids visual clutter while keeping priority immediately readable.

## Pattern

```dax
Task Priority Pill :=
VAR _label     = SELECTEDVALUE(Tasks[Priority])
VAR _bgColor   = [_ColorWhite]
VAR _borderCol = [_ColorAccent9Dark]
VAR _textColor = [_ColorTextDark]
VAR _dotColor  =
    SWITCH(SELECTEDVALUE(Tasks[Priority]),
        "High",   [_ColorAccent5Dark],   -- red/orange
        "Medium", [_ColorAccent4Dark],   -- yellow/amber
        "Low",    [_ColorAccent1Dark],   -- green
        [_ColorAccent9Dark]
    )
RETURN
    IF(
        ISBLANK(_label),
        BLANK(),
        UDF_SVGPillCanvas(
            _label,
            _bgColor,
            _borderCol,
            _textColor,
            1,              -- showBorder = 1
            _dotColor,      -- dot color carries the signal
            1               -- showDot = 1
        )
    )
```

## Setup

1. Set **Data Category = Image URL** on `Task Priority Pill`
2. In the table visual, set **Grid → Image size**: Height = 28 px, Width = 200 px
3. Place `Task Priority Pill` in the Priority column

## Dot Color Mapping

| Priority | Dot Color | Effect |
|---|---|---|
| High | Dark accent 5 | Red/orange — urgent |
| Medium | Dark accent 4 | Yellow/amber — moderate |
| Low | Dark accent 1 | Green — low |
| Default | Dark accent 9 | Neutral fallback |

## Related

- [[svg-pill-pattern-udf-based]] — `pattern` — the UDF architecture this measure uses
- [[udf_svgpillcanvas-generic-pill-renderer]] — `function` — the UDF this measure calls
- [[task-status-pill-measure]] — `pattern` — filled status pill (signal via background color)
