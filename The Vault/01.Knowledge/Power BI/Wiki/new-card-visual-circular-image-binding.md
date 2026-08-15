---
created: 2026-08-14
source: 3 Hacks to Turn Any Image into a Circle in Power BI (datatraining.io + video)
source_url: https://datatraining.io/blog/3-hacks-image-to-circle
note_type: atomic
tags: [power-bi, new-card-visual, image-url, image-type, circular-image, workflow]
---

# New Card Visual — Circular Image Binding

Concrete UI path for showing a circular image inside a **new Card visual** (the "new card" introduced in 2022+) — uses the visual's image settings, not a measure.

## Steps

1. Insert the **new Card visual**.
2. Open **Format visual** pane → **Images** section → turn **Image** on.
3. Set **Image type** to **Image URL**.
4. Use the **fx (field value)** button to bind it to the column/measure that holds the circular image link (or the SVG-with-clipPath measure).
5. Confirm the bound column/measure has its **Data category** set to **Image URL** in the Modelling ribbon (otherwise the image does not render).

## Why This Matters

- Older Card visuals may not render SVG strings or Base64 cleanly — the **new Card visual** is the reliable host.
- Avoids the need to overlay a mask visual on top of the image visual — the image is a *property of* the Card itself, so the card and its image move together (no scroll misalignment like Approach B).

## Pitfall

If the field is bound but the image does not appear, the Data category is almost always wrong — it must be set to **Image URL** on the *target column or measure*, not just on the source. Numeric columns also fail; convert to Text first.

## Related

- [[circular-image-approaches-decision-guide]] — when to use the new Card visual vs. tables
- [[Circular-Image-Power-BI-Table-Pattern]] — Table/Matrix version of this pattern
- [[DAX-SVG-Circular-Image-Snippet]] — the SVG-with-clipPath measure to bind
- [[Image-URL-Data-Category]] — why Data category must be Image URL
- [[Image-Masking-Limitation-Power-BI]] — overlay-mask limitation the new Card visual avoids
