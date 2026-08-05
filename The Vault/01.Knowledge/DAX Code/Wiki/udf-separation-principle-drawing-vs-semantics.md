---
created: 2026-08-02
updated: 2026-08-05
source: One UDF to Build All Your SVG Pills in Power BI
note_type: atomic
tags: [dax, udf, design-principle, architecture, svg]
---

# UDF Separation Principle (Drawing vs. Semantics)

Design principle for DAX User-Defined Functions: UDFs should only handle drawing; measures should handle business logic.

## The Rule

| Layer | Responsibility | Examples |
|-------|---------------|----------|
| **UDF** | Drawing: geometry, padding, SVG shapes, colors | Pill width, rounded corners, dot position |
| **Measure** | Semantics: which label, which color, when to show | `SELECTEDVALUE`, `SWITCH` on status, dot-on/off logic |

## Why This Matters

Without separation, each new pill use case requires a new UDF — geometry code gets duplicated and becomes brittle. With separation:

- **One pill UDF** handles any label, any color scheme, any combination of border/dot
- **Each new pill type** is a 10–15 line measure: pick label, map colors, decide dot/border flags
- **Design system stays consistent**: colors live in dedicated `_Color*` measures, not buried in SVG strings

## Correct (Separated)

```dax
-- UDF: only draws
FUNCTION UDF_SVGPillCanvas(label, bgColor, borderColor, ...) =>
    -- geometry, SVG shapes, UDF_EncodeSVG call
    RETURN ...

-- Measure: decides what to draw
Task Priority Pill :=
    VAR _label = SELECTEDVALUE(Tasks[Priority])
    VAR _dotColor = SWITCH(SELECTEDVALUE(Tasks[Priority]),
        "High", [_ColorAccent5Dark],
        "Medium", [_ColorAccent4Dark],
        ...
    )
    RETURN UDF_SVGPillCanvas(_label, ..., _dotColor, 1)
```

## Anti-pattern (Not Separated)

Embedding status/color logic inside the UDF body — requires modifying the UDF for every new label variant.

## Related

- [[svg-pill-pattern-udf-based]] — `pattern` — the pattern that embodies this principle
- [[udf_svgpillcanvas-generic-pill-renderer]] — `function` — the drawing-only UDF
- [[dax-udf-define-function-pattern]] — `function` — how to define UDFs in DAX
