---
created: 2026-08-02
source: How to Design Attractive Power BI Reports
note_type: atomic
tags: [powerbi, design, typography, font, limitation]
---

# Custom Fonts in Power BI

Power BI supports custom fonts, but users must have the font installed on their device to render it correctly.

## Limitation

If a report uses a font not installed on the viewer's machine, Power BI falls back to the default font — the custom typography is silently lost.

## Mitigation

- Stick to fonts with near-universal installation (Segoe UI, Calibri, Arial)
- If using custom fonts, document the requirement and provide the font file for distribution
- For web-based distribution (Power BI Service), verify font availability in the browser environment

## See Also

Bittar's dedicated article: "Beyond Defaults: Using Custom Fonts in Power BI"

## Source

Isabelle Bittar — FP20 Analytics Challenge series, 2024-01-28
