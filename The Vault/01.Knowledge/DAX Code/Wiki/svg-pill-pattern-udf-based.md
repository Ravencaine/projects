---
created: 2026-08-02
source: One UDF to Build All Your SVG Pills in Power BI
note_type: pattern
tags: [dax, power-bi, svg, udf, visualization, pills]
---

# SVG Pill Pattern (UDF-based)

Generate dynamic, color-coded SVG pills (status tags, priority indicators, department labels) in Power BI table visuals using two reusable DAX User-Defined Functions.

## Purpose

Render pill-shaped visual badges inside a table or matrix visual without external assets. The same two UDFs handle all pill variants — filled, outline, dot, no dot — by varying the calling measure's arguments.

## Architecture

```
[Color measure] → UDF_SVGPillCanvas(label, bgColor, borderColor, textColor, showBorder, dotColor, showDot) → UDF_EncodeSVG → data:image/svg+xml;utf8,...
```

**Two UDFs, one model:**

1. **`UDF_EncodeSVG`** — URL-encodes any raw SVG string so Power BI can render it
2. **`UDF_SVGPillCanvas`** — draws the pill (rect + optional dot + text), then calls `UDF_EncodeSVG`

**Separation of concerns:**
- UDFs handle only *drawing* (geometry, padding, rounded corners)
- Measures handle *semantics* (which color maps to which label, when the dot appears)

## UDF #1 — SVG Encoder

```dax
DEFINE
  FUNCTION UDF_EncodeSVG =
    ( svg : STRING ) =>
    VAR s0 = SUBSTITUTE(svg, "%",   "%25")
    VAR s1 = SUBSTITUTE(s0,  "#",   "%23")
    VAR s2 = SUBSTITUTE(s1,  "<",   "%3C")
    VAR s3 = SUBSTITUTE(s2,  ">",   "%3E")
    VAR s4 = SUBSTITUTE(s3,  """",  "%22")
    VAR s5 = SUBSTITUTE(s4,  "'",   "%27")
    VAR s6 = SUBSTITUTE(s5,  " ",   "%20")
    VAR s7 = SUBSTITUTE(s6,  ":",   "%3A")
    VAR s8 = SUBSTITUTE(s7,  "/",   "%2F")
    VAR s9 = SUBSTITUTE(s8,  "?",   "%3F")
    VAR sA = SUBSTITUTE(s9,  "=",   "%3D")
    VAR sB = SUBSTITUTE(sA,  "&",   "%26")
    RETURN "data:image/svg+xml;utf8," & sB
```

## UDF #2 — Pill Renderer

```dax
DEFINE
  FUNCTION UDF_SVGPillCanvas =
    ( label       : STRING,
      bgColor     : STRING,
      borderColor : STRING,
      textColor   : STRING,
      showBorder  : DECIMAL,   -- 1 = border, 0 = no border
      dotColor    : STRING,
      showDot     : DECIMAL    -- 1 = dot, 0 = no dot
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
    VAR _baseTextPad = 8
    VAR _gapAfterDot = 6
    VAR _dotR       = fontSize * 0.55 / 2
    VAR _dotOffsetX = leftPad + _baseTextPad
    VAR _dotOffsetY = canvasHeight / 2
    VAR _extraLeft  =
        IF(showDot = 1,
            _baseTextPad + (_dotR * 2) + _gapAfterDot,
            _baseTextPad)
    VAR _pillW = _textLen * _charW + _hPad + _extraLeft
    VAR _rectY  = (canvasHeight - _pillH) / 2
    VAR _textX  = leftPad + _extraLeft
    VAR _textY  = canvasHeight / 2
    VAR _strokeColor = IF(showBorder = 1, borderColor, "none")
    VAR _strokeWidth = IF(showBorder = 1, "1", "0")
    VAR _rect =
        "<rect x=""" & leftPad & """ y=""" & _rectY &
        """ width=""" & (_pillW - 1) & """ height=""" & (_pillH - 1) &
        """ rx=""" & _corner &
        """ fill=""" & bgColor &
        """ stroke=""" & _strokeColor &
        """ stroke-width=""" & _strokeWidth & """ />"
    VAR _svgDot =
        IF(showDot = 1,
            "<circle cx=""" & _dotOffsetX & """ cy=""" & _dotOffsetY &
            """ r=""" & _dotR & """ fill=""" & dotColor & """ />",
            "")
    VAR _svgText =
        "<text x=""" & _textX & """ y=""" & _textY &
        """ dominant-baseline=""middle"" text-anchor=""start"" fill=""" & textColor &
        """ font-family=""Segoe UI"" font-size=""" & fontSize &
        """px"" font-weight=""400"">" & label & "</text>"
    VAR _svg =
        "<svg xmlns=""http://www.w3.org/2000/svg"" width=""" & canvasWidth &
        """ height=""" & canvasHeight &
        """ viewBox=""0 0 " & canvasWidth & " " & canvasHeight & """>" &
            _rect & _svgDot & _svgText &
        "</svg>"
    RETURN UDF_EncodeSVG(_svg)
```

## Example: Task Status Pill (outline, no dot)

```dax
Task Status Pill :=
VAR _label     = SELECTEDVALUE(Tasks[Status])
VAR _bgColor   = [Status Background Color]
VAR _borderCol = [Status Border Color]
VAR _textColor = [_ColorTextDark]
VAR _dotColor  = [Status Border Color]
RETURN
    IF(ISBLANK(_label), BLANK(),
        UDF_SVGPillCanvas(
            _label, _bgColor, _borderCol, _textColor,
            1, _dotColor, 0   -- no dot
        )
    )
```

## Example: Task Priority Pill (outline, with dot)

```dax
Task Priority Pill :=
VAR _label     = SELECTEDVALUE(Tasks[Priority])
VAR _bgColor   = [_ColorWhite]
VAR _borderCol = [_ColorAccent9Dark]
VAR _textColor = [_ColorTextDark]
VAR _dotColor  =
    SWITCH(SELECTEDVALUE(Tasks[Priority]),
        "High",   [_ColorAccent5Dark],
        "Medium", [_ColorAccent4Dark],
        "Low",    [_ColorAccent1Dark],
        [_ColorAccent9Dark])
RETURN
    IF(ISBLANK(_label), BLANK(),
        UDF_SVGPillCanvas(
            _label, _bgColor, _borderCol, _textColor,
            1, _dotColor, 1   -- dot visible
        )
    )
```

## Setup Checklist

1. **Enable UDFs:** Options → Preview features → enable UDFs; use the new DAX Query View
2. **Paste both DEFINE FUNCTION blocks** and click **Update model with changes**
3. **Set Data Category** on each pill measure to **Image URL**
4. **Image size** in table visual: Grid → Image size → Height = 28 px, Width = 200 px

## Variations

| Use case | showBorder | showDot | Notes |
|---|---|---|---|
| Status (filled) | 1 | 0 | bgColor carries the signal |
| Status (outline) | 1 | 0 | white bg, colored border |
| Priority with dot | 1 | 1 | neutral pill, dot carries signal |
| Tag / category | 0 | 0 | minimal clean pill |

## Related

- [[udf_encodesvg-url-encoder-for-svg]] — `function` — URL encoder UDF
- [[udf_svgpillcanvas-generic-pill-renderer]] — `function` — pill renderer UDF
- [[svg-pill-geometry-dynamic-sizing]] — `atomic` — dynamic width/height calculations
- [[udf-separation-principle-drawing-vs-semantics]] — `atomic` — design principle
- [[svg-visualizations-in-power-bi]] — `pattern` — related SVG pattern
- [[svg-star-rating-dax]] — `pattern` — another SVG pattern
