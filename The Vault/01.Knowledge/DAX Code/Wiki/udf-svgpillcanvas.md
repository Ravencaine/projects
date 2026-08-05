---
created: 2026-08-02
source: One UDF to Build All Your SVG Pills in Power BI
note_type: function
tags: [dax, udf, function, svg, pill, canvas]
---

# UDF_SVGPillCanvas — Draw SVG Pill (Rect + Dot + Text)

Draws a rounded pill (background + optional border + optional dot + text) and returns it as a URL-encoded SVG data URI.

```dax
DEFINE
  FUNCTION UDF_SVGPillCanvas =
    ( label       : STRING,
      bgColor     : STRING,
      borderColor : STRING,
      textColor   : STRING,
      showBorder  : DECIMAL,  -- 1 = border on, 0 = no border
      dotColor    : STRING,
      showDot     : DECIMAL   -- 1 = dot on, 0 = no dot
    ) =>
    VAR fontSize     = 11
    VAR canvasWidth  = 200
    VAR canvasHeight = 28
    VAR leftPad      = 8
    VAR _pillH       = 24
    VAR _corner      = 12
    VAR _charW       = 6
    VAR _hPad        = 9
    VAR _textLen     = LEN(label)
    -- ... geometry calculations ...
    VAR _rect   = "<rect x=\""" & leftPad & ...
    VAR _svgDot = IF(showDot = 1, "<circle ...>", "")
    VAR _svg    = "<svg ...>" & _rect & _svgDot & _svgText & "</svg>"
    RETURN UDF_EncodeSVG(_svg)
```

**Geometry constants** (must match table visual image size):
- `canvasWidth = 200`, `canvasHeight = 28`
- Pill height `24px`, corner radius `12px` (fully rounded)

**Parameters:**
- `showBorder` — `1` renders a border stroke; `0` renders `stroke="none"`
- `showDot` — `1` renders a circle before the text; `0` omits it
- `dotColor`, `bgColor`, `borderColor`, `textColor` — pass accent color measures from logic measures, not hardcoded strings

**Design principle:** UDF owns geometry; measures own color/semantic decisions.
