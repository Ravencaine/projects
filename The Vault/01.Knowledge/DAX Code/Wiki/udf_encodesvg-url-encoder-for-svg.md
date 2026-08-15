---
created: 2026-08-02
updated: 2026-08-05
source: One UDF to Build All Your SVG Pills in Power BI
note_type: function
tags: [dax, udf, svg, power-bi, url-encoding]
---

# UDF_EncodeSVG — URL Encoder for SVG

Encodes a raw SVG string so Power BI can render it as an image. Power BI visuals cannot display raw SVG markup — every special character must be percent-encoded before prepending the `data:image/svg+xml;utf8,` prefix.

## Signature

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

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `svg` | STRING | Raw SVG markup string (may contain `<`, `>`, `"`, `#`, spaces, etc.) |

## Returns

A `data:` URI string: `data:image/svg+xml;utf8,<encoded-svg>`. This is what Power BI renders when the measure's **Data Category** is set to **Image URL**.

## Why URL-Encode?

Power BI's image rendering layer expects a valid data URI. SVG characters like `<`, `>`, `"`, `#` are reserved in URI syntax and must be replaced:

| Char | Encoded |
|------|---------|
| space | `%20` |
| `#` | `%23` |
| `<` | `%3C` |
| `>` | `%3E` |
| `"` | `%22` |
| `'` | `%27` |
| `%` | `%25` |
| `:` | `%3A` |
| `/` | `%2F` |
| `?` | `%3F` |
| `=` | `%3D` |
| `&` | `%26` |

## Notes

- This is a **helper UDF:** it is called from *within* other UDFs, not used directly in measures
- **Do not URL-encode the final `data:image/svg+xml;utf8,` prefix:** only the SVG content inside it
- If building SVG strings manually (without a dedicated UDF), prepend the prefix *after* encoding all special characters in the SVG body
- Chaining `SUBSTITUTE` calls sequentially (s0 → s1 → s2...) is safe because each call replaces from the previous state

## Related

- [[udf_svgpillcanvas-generic-pill-renderer]] — `function` — calls this to encode its SVG output
- [[svg-pill-pattern-udf-based]] — `pattern` — the pattern that uses both UDFs
- [[svg-visualizations-in-power-bi]] — `pattern` — raw SVG without URL encoding (legacy approach)
