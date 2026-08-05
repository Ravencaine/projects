---
created: 2026-08-02
updated: 2026-08-05
source: One UDF to Build All Your SVG Pills in Power BI
note_type: pattern
tags: [dax, pattern, svg, pill, priority, dot-color, switch]
---

# Task Priority Pill — Neutral Pill + Dot Color Carries the Signal

A priority pill with neutral background/border where the **dot color carries the signal** — High→dark red, Medium→amber, Low→green.

```dax
Task Priority Pill :=
VAR _label     = SELECTEDVALUE(Tasks[Priority])
VAR _bgColor  = [_ColorWhite]
VAR _borderC  = [_ColorAccent9Dark]
VAR _textC    = [_ColorTextDark]

VAR _dotColor =
    SWITCH(
        SELECTEDVALUE(Tasks[Priority]),
        "High",   [_ColorAccent5Dark],
        "Medium", [_ColorAccent4Dark],
        "Low",    [_ColorAccent1Dark],
        [_ColorAccent9Dark]
    )

RETURN
    IF(
        ISBLANK(_label),
        BLANK(),
        UDF_SVGPillCanvas(
            _label,
            _bgColor,
            _borderC,
            _textC,
            1,           -- showBorder = on
            _dotColor,   -- dot carries the priority signal
            1            -- showDot = on
        )
    )
```

**Design pattern:** neutral pill (white bg, dark border) keeps the text readable; SWITCH on dot color lets you signal intensity without visual noise. Contrast with `task-status-pill-svg.md` where background color carries the status signal.
