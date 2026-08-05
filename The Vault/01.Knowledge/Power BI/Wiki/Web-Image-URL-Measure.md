---
created: 2026-08-05
source: 5 Powerful Ways Import Images Power BI (Boniface Muchendu)
note_type: atomic
tags: [power-bi, image, web-image, measure, image-url, table]
---

# Web Image URL via Measure

Storing image URLs in a DAX measure, setting the Image URL data category, and displaying images in a table or matrix visual that renders them as actual images.

## Steps

### 1. Create the measure

```dax
Logo = "https://example.com/logo.png"
```

### 2. Set the data category

1. Select the measure in the Fields pane
2. In the **Modelling** ribbon → **Data category** → select **Image URL**

### 3. Add to a visual

Drag the measure into a **Table** or **Matrix** visual. Power BI renders the URL as an actual image.

## Prerequisites

- The URL must end in a recognised image extension: `.png`, `.jpg`, `.jpeg`, `.gif`, `.svg`, `.webp`
- The image host must allow direct linking (hotlinking)
- A stable internet connection is required — images are loaded from the web on each report view

## Best Use Cases

- Product catalogues: display product images alongside data in a table
- Employee directories: headshots in a matrix of employee attributes
- KPI tiles with small status icons

## When to Use

Use when images are available on the web and do not need to work offline. Fastest to implement for dynamic image sets where the URL comes from a data column.

## Limitations

- Requires internet connectivity
- If the image host blocks hotlinking, images won't render
- Images load at the resolution provided — no upscaling

## Related

- [[ImageBB-Hosting-Service]]
- [[Binary-Base64-Image-Model]]
- [[Image-URL-Data-Category]]
