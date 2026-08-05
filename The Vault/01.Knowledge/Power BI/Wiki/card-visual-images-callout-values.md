---
created: 2026-08-02
source: Next-Level Dashboard Design With Power BI's New Card Visual With Reference Labels
note_type: pattern
tags: [powerbi, pattern, card-visual, image, icon]
---

# Card Visual: Image per Callout Value

Each callout value in the new card visual can display an icon/image to its left or right.

**Two image sources:**
1. **Upload** — local image file stored in the PBIX
2. **Image URL** — remote URL fetched at render time

**Settings:**
- `Image Type` → select `Image` or `Image URL` per series
- `Size` → set px value (e.g. `38px`)
- `Position` → `Left to Text` or `Right to Text`
- `Space between image and callout` → px value (e.g. `8px`)

**Image URL approach** is dynamic — the image can change based on the data context. Covered in detail in the "Power BI's New Slicer: Market Watch Dashboard" tutorial (Bittar).
