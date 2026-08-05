---
created: 2026-08-02
updated: 2026-08-05
source: One UDF to Build All Your SVG Pills in Power BI
note_type: function
tags: [dax, udf, svg, power-bi, pill, visualization]
---

# UDF_SVGPillCanvas — Generic Pill Renderer UDF

Draws a rounded pill shape (rectangle with border, optional status dot, and label text) and returns it as a URL-encoded data URI. All geometry is computed dynamically from the label string length.

## Signature

```dax
DEFINE
  FUNCTION UDF_SVGPillCanvas =
    ( label       : STRING,
      bgColor     : STRING,
      borderColor : STRING,
      textColor   : STRING,
      showBorder  : DECIMAL,   -- 1 = border on, 0 = border off
      dotColor    : STRING,
      showDot     : DECIMAL    -- 1 = dot on, 0 = dot off
    ) =>
    -- canvas
    VAR fontSize     = 11
    VAR canvasWidth  = 200
    VAR canvasHeight = 28
    VAR leftPad      = 8
    -- pill geometry
    VAR _pillH   = 24
    VAR _corner  = 12
    VAR _charW   = 6
    VAR _hPad    = 9
    VAR _textLen = LEN(label)
    -- dot geometry
    VAR _dotR       = fontSize * 0.55 / 2
    VAR _dotOffsetX = leftPad + 8 + (_dotR * 2) + 6   -- (conditional on showDot)
    VAR _dotOffsetY = canvasHeight / 2
    -- text offset (conditional on showDot)
    VAR _extraLeft =
        IF(showDot = 1, 8 + (_dotR * 2) + 6, 8)
    -- pill width
    VAR _pillW = _textLen * _charW + _hPad + _extraLeft
    -- rect
    VAR _rectY  = (canvasHeight - _pillH) / 2
    VAR _rect   = "<rect x=""" & leftPad & """ y=""" & _rectY & """ width=""" & (_pillW - 1) &
                  """ height=""" & (_pillH - 1) & """ rx=""" & _corner &
                  """ fill=""" & bgColor & """ stroke=""" & IF(showBorder = 1, borderColor, "none") &
                  """ stroke-width=""" & IF(showBorder = 1, "1", "0") & """ />"
    -- dot
    VAR _svgDot = IF(showDot = 1,
        "<circle cx=""" & (leftPad + 8 + _dotR) & """ cy=""" & _dotOffsetY &
        """ r=""" & _dotR & """ fill=""" & dotColor & """ />", "")
    -- text
    VAR _textX  = leftPad + _extraLeft
    VAR _svgText = "<text x=""" & _textX & """ y=""" & canvasHeight / 2 &
                   """ dominant-baseline=""middle"" text-anchor=""start"" fill=""" & textColor &
                   """ font-family=""Segoe UI"" font-size=""" & fontSize &
                   """px"" font-weight=""400"">" & label & "</text>"
    -- full SVG
    VAR _svg = "<svg xmlns=""http://www.w3.org/2000/svg"" width=""" & canvasWidth &
               """ height=""" & canvasHeight &
               """ viewBox=""0 0 " & canvasWidth & " " & canvasHeight & """>" &
               _rect & _svgDot & _svgText & "</svg>"
    RETURN UDF_EncodeSVG(_svg)
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `label` | STRING | Text displayed inside the pill |
| `bgColor` | STRING | Hex fill color for the pill background |
| `borderColor` | STRING | Hex color for the pill border |
| `textColor` | STRING | Hex color for the label text |
| `showBorder` | DECIMAL | 1 = show border, 0 = hide border |
| `dotColor` | STRING | Hex color for the optional status dot |
| `showDot` | DECIMAL | 1 = show dot, 0 = hide dot |

## Returns

A `data:image/svg+xml;utf8,...` URI string. Assign to a measure with **Data Category = Image URL**.

## Key Geometry Values

| Constant | Value | Purpose |
|----------|-------|---------|
| `fontSize` | 11 | Text size in px |
| `canvasWidth` | 200 | SVG canvas width (px) — match table visual image width |
| `canvasHeight` | 28 | SVG canvas height (px) — match table visual image height |
| `_pillH` | 24 | Pill height within canvas |
| `_corner` | 12 | Corner radius = half of pill height (fully rounded) |
| `_charW` | 6 | Approximate px width per character |
| `_hPad` | 9 | Horizontal padding around text |
| `_dotR` | 3.025 | Dot radius = `fontSize * 0.55 / 2` |

## Notes

- **Dynamic width:** Pill width = `LEN(label) * _charW + _hPad + _extraLeft` — longer text automatically widens the pill
- **Dot-aware offset:** `_extraLeft` increases by `(dotR * 2 + 6)` when `showDot = 1`, keeping text and dot visually balanced
- **Corner radius:** `_corner = 12 = _pillH / 2` — creates fully rounded pill ends
- **Conditional stroke:** When `showBorder = 0`, stroke is set to `"none"` and width to `"0"` (not omitted) to keep valid XML
- Call `UDF_EncodeSVG` on the result — do not call this UDF directly from a measure without encoding

## Related

- [[udf_encodesvg-url-encoder-for-svg]] — `function` — called internally to encode the SVG
- [[svg-pill-pattern-udf-based]] — `pattern` — shows calling measures
- [[svg-pill-geometry-dynamic-sizing]] — `atomic` — geometry derivation details
- [[task-status-pill-measure]] — `pattern` — example measure
- [[task-priority-pill-measure-with-dot]] — `pattern` — example measure with dot
