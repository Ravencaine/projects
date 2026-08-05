---
created: 2026-08-05
source: 5 Powerful Ways Import Images Power BI (Boniface Muchendu)
note_type: atomic
tags: [power-bi, data-category, image-url, model, measure, modelling]
---

# Image URL Data Category

The data category setting that tells Power BI a text column or measure contains a URL that should be rendered as an image rather than displayed as plain text.

## Where to Set It

1. Select the column or measure in the **Fields** pane
2. Go to the **Modelling** ribbon
3. Find **Data category** dropdown
4. Select **Image URL**

Power BI will now render any value in that field as an image in visuals that support it (Table, Matrix, Card, KPI).

## What It Expects

| Format | Example |
|--------|---------|
| Web URL | `https://example.com/image.png` |
| Data URI (Base64) | `data:image/png;base64,iVBORw0KGgo...` |
| Data URI (SVG) | `data:image/svg+xml;utf8,<svg...` |

The field must be a text type (string). Numeric URLs stored as numbers will not render.

## Common Mistake

Setting the data category but leaving the column as a number type. Power BI will not render the image. Solution: change the column type to **Text** first, then set the data category.

## Related

- [[Web-Image-URL-Measure]]
- [[Binary-Base64-Image-Model]]
- [[SVG-Images-Power-BI]]
