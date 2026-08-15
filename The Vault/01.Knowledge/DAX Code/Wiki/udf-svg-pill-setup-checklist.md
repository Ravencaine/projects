---
created: 2026-08-02
updated: 2026-08-05
source: One UDF to Build All Your SVG Pills in Power BI
note_type: snippet
tags: [dax, udf, svg, power-bi, setup, checklist]
---

# UDF SVG Pill Setup Checklist

Step-by-step checklist to add SVG pills to a Power BI report.

## Prerequisites

- [ ] Power BI Desktop — UDFs are a **preview feature** as of late 2025
- [ ] Enable in **Options → Preview features → User-Defined Functions**
- [ ] Use the new **DAX Query View** (not Legacy DAX Query View)

## Step 1 — Define the UDFs

In **DAX Query View**, paste:

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

  FUNCTION UDF_SVGPillCanvas =
    ( label : STRING, bgColor : STRING, borderColor : STRING,
      textColor : STRING, showBorder : DECIMAL, dotColor : STRING, showDot : DECIMAL ) =>
    VAR fontSize = 11; VAR canvasWidth = 200; VAR canvasHeight = 28; VAR leftPad = 8
    VAR _pillH = 24; VAR _corner = 12; VAR _charW = 6; VAR _hPad = 9
    VAR _textLen = LEN(label); VAR _baseTextPad = 8; VAR _gapAfterDot = 6
    VAR _dotR = fontSize * 0.55 / 2; VAR _dotOffsetX = leftPad + _baseTextPad; VAR _dotOffsetY = canvasHeight / 2
    VAR _extraLeft = IF(showDot = 1, _baseTextPad + (_dotR * 2) + _gapAfterDot, _baseTextPad)
    VAR _pillW = _textLen * _charW + _hPad + _extraLeft
    VAR _rectY = (canvasHeight - _pillH) / 2; VAR _textX = leftPad + _extraLeft; VAR _textY = canvasHeight / 2
    VAR _strokeColor = IF(showBorder = 1, borderColor, "none"); VAR _strokeWidth = IF(showBorder = 1, "1", "0")
    VAR _rect = "<rect x=""" & leftPad & """ y=""" & _rectY & """ width=""" & (_pillW - 1) & """ height=""" & (_pillH - 1) & """ rx=""" & _corner & """ fill=""" & bgColor & """ stroke=""" & _strokeColor & """ stroke-width=""" & _strokeWidth & """ />"
    VAR _svgDot = IF(showDot = 1, "<circle cx=""" & _dotOffsetX & """ cy=""" & _dotOffsetY & """ r=""" & _dotR & """ fill=""" & dotColor & """ />", "")
    VAR _svgText = "<text x=""" & _textX & """ y=""" & _textY & """ dominant-baseline=""middle"" text-anchor=""start"" fill=""" & textColor & """ font-family=""Segoe UI"" font-size=""" & fontSize & """px"" font-weight=""400"">" & label & "</text>"
    VAR _svg = "<svg xmlns=""http://www.w3.org/2000/svg"" width=""" & canvasWidth & """ height=""" & canvasHeight & """ viewBox=""0 0 " & canvasWidth & " " & canvasHeight & """>" & _rect & _svgDot & _svgText & "</svg>"
    RETURN UDF_EncodeSVG(_svg)
```

**Click "Update model with changes":** this is required for the UDFs to be callable from measures.

## Step 2 — Color Palette Measures

Define accent color measures (or adapt existing ones):

```dax
_ColorWhite = "#FFFFFF"
_ColorTextDark = "#4B4B4B"
_StatusBackgroundColor = SWITCH(SELECTEDVALUE(Tasks[Status]),
    "Completed", "#00C48C", "In Progress", "#007AFF", "At Risk", "#FF3B30", "Not Started", "#8E8E93", "#FFFFFF")
```

## Step 3 — Pill Measures

Create one measure per pill type (see `task-status-pill-measure` and `task-priority-pill-measure-with-dot`).

## Step 4 — Visual Setup

On each pill measure:
- **Data category** → **Image URL**

In the table visual:
- **Values → Grid → Image size**: Height = **28 px**, Width = **200 px** (match UDF canvas constants)

## Related

- [[svg-pill-pattern-udf-based]] — `pattern` — full architecture
- [[udf_encodesvg-url-encoder-for-svg]] — `function` — the encoder UDF
- [[udf_svgpillcanvas-generic-pill-renderer]] — `function` — the renderer UDF
