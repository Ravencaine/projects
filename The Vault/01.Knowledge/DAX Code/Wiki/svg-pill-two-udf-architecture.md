---
created: 2026-08-02
updated: 2026-08-05
source: One UDF to Build All Your SVG Pills in Power BI
note_type: pattern
tags: [dax, pattern, svg, udf, pill, design-system]
---

# UDF Pattern: SVG Pill — Two-UDF Architecture

A reusable SVG pill pattern in Power BI requires **two separate UDFs**:

1. **`UDF_EncodeSVG`:** URL-encodes a raw SVG string so Power BI can render it as an image
2. **`UDF_SVGPillCanvas`:** draws the pill (background, border, optional dot, text)

The architecture follows a clear separation of concerns:

- **UDFs own the drawing:** geometry, padding, rounded corners, dot position, URL encoding. Never change these once defined.
- **Measures own the semantics:** label text, color choices, when to show border/dot. One new measure per pill type (status, priority, tag, etc.).

**Design once, reuse everywhere:** after both UDFs are in the model, every new pill variant is 10–15 lines of measure logic. No SVG changes required.

> Related: `UDF_EncodeSVG.md` and `UDF_SVGPillCanvas.md` (function notes).
