---
created: 2026-08-02
updated: 2026-08-05
source: One UDF to Build All Your SVG Pills in Power BI
note_type: function
tags: [dax, udf, function, svg, url-encode]
---

# UDF_EncodeSVG — URL-Encode Raw SVG String

Converts a raw SVG markup string into a URL-encoded `data:` URI that Power BI visuals can render as an image.

```dax
DEFINE
  FUNCTION UDF_EncodeSVG =
    ( svg : STRING ) =>
    VAR s0 = SUBSTITUTE(svg, "%",   "%25")
    VAR s1 = SUBSTITUTE(s0,  "#",   "%23")
    VAR s2 = SUBSTITUTE(s1,  "<",   "%3C")
    VAR s3 = SUBSTITUTE(s2,  ">",   "%3E")
    VAR s4 = SUBSTITUTE(s3,  "\"",  "%22")
    VAR s5 = SUBSTITUTE(s4,  "'",   "%27")
    VAR s6 = SUBSTITUTE(s5,  " ",   "%20")
    VAR s7 = SUBSTITUTE(s6,  ":",   "%3A")
    VAR s8 = SUBSTITUTE(s7,  "/",   "%2F")
    VAR s9 = SUBSTITUTE(s8,  "?",   "%3F")
    VAR sA = SUBSTITUTE(s9,  "=",   "%3D")
    VAR sB = SUBSTITUTE(sA,  "&",   "%26")
    RETURN "data:image/svg+xml;utf8," & sB
```

Power BI visuals (table, matrix, etc.) cannot render raw SVG markup — the SVG must be wrapped in a `data:image/svg+xml;utf8,` URI after URL-encoding. Call `UDF_EncodeSVG` inside every SVG-drawing UDF as the final step before returning.

**Prerequisite:** enable UDFs in **Options → Preview features** and use **DAX Query View**. Click **Update model with changes** after defining.
