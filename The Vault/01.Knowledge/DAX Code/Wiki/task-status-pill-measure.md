---
created: 2026-08-02
source: One UDF to Build All Your SVG Pills in Power BI
note_type: pattern
tags: [dax, power-bi, svg, pill, status, visualization]
---

# Task Status Pill Measure

Renders an outline-style SVG pill for a task status column in a Power BI table visual. Background carries the color signal (filled pill); the dot is hidden.

## Purpose

Display task statuses (Not Started / In Progress / Completed / At Risk) as colored pills inside a table. A `SWITCH`-based color measure maps each status value to a background and border color; the pill measure assembles them.

## Pattern

```dax
Task Status Pill :=
VAR _label     = SELECTEDVALUE(Tasks[Status])
VAR _bgColor   = [Status Background Color]
VAR _borderCol = [Status Border Color]
VAR _textColor = [_ColorTextDark]
VAR _dotColor  = [Status Border Color]
RETURN
    IF(
        ISBLANK(_label),
        BLANK(),
        UDF_SVGPillCanvas(
            _label,             -- label text
            _bgColor,           -- background color
            _borderCol,         -- border color
            _textColor,         -- text color
            1,                  -- showBorder = 1
            _dotColor,          -- dot color (not shown here)
            0                   -- showDot = 0 (no dot)
        )
    )
```

## Supporting Color Measures (not shown, called by reference)

```dax
Status Background Color :=
SWITCH(SELECTEDVALUE(Tasks[Status]),
    "Completed",   [_ColorMint],    -- mint green
    "In Progress", [_ColorBlue],    -- blue
    "At Risk",     [_ColorRed],     -- red
    "Not Started", [_ColorGrey],    -- grey
    BLANK()
)

Status Border Color :=
SWITCH(SELECTEDVALUE(Tasks[Status]),
    "Completed",   [_ColorMintDark],
    "In Progress", [_ColorBlueDark],
    "At Risk",     [_ColorRedDark],
    "Not Started", [_ColorGreyDark],
    BLANK()
)
```

## Setup

1. Set **Data Category = Image URL** on `Task Status Pill`
2. In the table visual, set **Grid → Image size**: Height = 28 px, Width = 200 px
3. Place `Task Status Pill` in the desired column

## Variations

| Style | showBorder | showDot | Signal source |
|---|---|---|---|
| Filled | 1 | 0 | bgColor |
| Outline (clean) | 1 | 0 | borderColor |
| Outline + dot | 1 | 1 | dotColor |

## Related

- [[svg-pill-pattern-udf-based]] — `pattern` — the UDF architecture this measure uses
- [[udf_svgpillcanvas-generic-pill-renderer]] — `function` — the UDF this measure calls
- [[task-priority-pill-measure-with-dot]] — `pattern` — same pill, with dot signal
