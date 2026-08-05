---
created: 2026-07-28
updated: 2026-08-02
source: Artificial Intelligence with Power BI (Diepeveen)
note_type: pattern
tags: [image-reel, matrix-visual, image-url, power-bi, image-gallery]
---

# Image Reel Visualisation — Matrix Visual

Use Power BI's Matrix visual to create an image reel: a grid of image thumbnails pulled from URLs in your data model.

## Purpose

Power BI has no native image reel visual. The Matrix visual can be used as a workaround: one cell per row, with the cell displaying an image URL as a picture.

## Configuration

1. Build a table in your data model with:
   - Image URL column (text, must be full URL)
   - Category or filter column (e.g., product name)
2. Insert → **Matrix** visual
3. Add a **slicer** for the category to filter images
4. In the Matrix visual format pane:
   - Turn off row/column headers
   - Set values per row = 1
   - Image URL column → Values field
5. In visual format options:
   - Image fit: **Fit**
   - Turn on **Image** display

## Notes

- The Matrix must have exactly 1 value per row for clean image display
- Images must be publicly accessible URLs (or use [[anonymous-image-access-power-bi]])
- Works best with a horizontal layout and a single column
- For a true carousel/reel, use a custom marketplace visual instead

## Related

- [[anonymous-image-access-power-bi]]
- [[azure-blob-storage-sas-image-urls]]
- [[ai-insights-vision-power-bi]]
