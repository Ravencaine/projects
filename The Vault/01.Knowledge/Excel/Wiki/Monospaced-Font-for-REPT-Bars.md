---
created: 2026-08-10
updated: 2026-08-10
source: "Excel REPT Function In Cell Charts • My Online Training Hub"
source_url: "https://www.myonlinetraininghub.com/excel-rept-function-in-cell-charts"
note_type: atomic
tags: [excel, atomic, font, formatting, visualisation]
---

# Monospaced Font Required for REPT Bar Alignment

REPT bar charts only align correctly when displayed in a monospaced (fixed-width) font.

## Definition

Characters in a monospaced font all occupy the same horizontal width. This ensures each repeated character contributes equally to the bar length — producing evenly-spaced, visually correct bars.

## Key Points

- Non-monospaced fonts (Calibri, Arial, etc.) assign different widths to different characters
- `█` and `|` may visually look the same width in proportional fonts but are not
- The bar will appear uneven even when the REPT formula is mathematically correct
- **Required fonts:** Consolas, Courier New, Lucida Console, or similar monospaced fonts

## Examples

| Font | Result |
|------|--------|
| Consolas | `████████████████████` — even alignment |
| Calibri | `████████████████████` — may appear uneven |

## Related

- [[In-Cell-Bar-Chart-REPT]] — pattern
- [[Progress-Bar-REPT-LET]] — pattern
- [[REPT-Function]] — function
