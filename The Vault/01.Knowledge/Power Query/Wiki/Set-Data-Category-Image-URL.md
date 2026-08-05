---
created: 2026-07-29
updated: 2026-08-02
source: "[[Author-Isabelle-Bittar|Isabelle Bittar]]"
note_type: workflow
tags: [power-query, image-url, data-category, slicer, new-slicer]
related: [SELECTEDVALUE]
---

# Set Data Category to Image URL (Power Query)

When a column contains public web URLs pointing to images (PNG, JPG, SVG), set the data category to `Image URL` so Power BI's new slicer renders the images inline.

## Step 1 — Prepare the URL Column

In Power Query or Excel, ensure the column contains valid public image URLs:

| Key | Full Name | Description | Image |
|-----|-----------|-------------|-------|
| AAPL | Apple Inc. | Technology stock | `https://logo.clearbit.com/apple.com` |
| MSFT | Microsoft Corp. | Software stock | `https://logo.clearbit.com/microsoft.com` |

## Step 2 — Set Data Category in Power BI

1. Load the table to Power BI.
2. Go to **Model view** → select the `Image` column.
3. In the **Properties** pane, go to **Advanced** → **Data category** → select **Image URL**.

```
Model view → [Image column] → Properties → Advanced → Data category → Image URL
```

## Step 3 — Use in the New Slicer

1. Create a new **Slicer** visual.
2. Add the `Key` column to the slicer.
3. Add the `Image` column to the slicer's **Image** field well.
4. Format: set `Image fit` → `Normal`, `Position` → `Left`, `Image area size` → `10%`.

## Notes

- The URLs must be publicly accessible — Power BI downloads and caches images from these URLs.
- Internal/intranet URLs will not work without a gateway or published PBIX.
- `Image URL` data category works with the **new slicer** (released November 2023) and the **HTML Content** custom visual.
- Bittar's Market Watch article uses this technique to show company logos next to stock ticker symbols in a slicer.
- Alternative: use a binary image column imported from a folder — but `Image URL` is simpler for publicly available logos/icons.

## Related

- [[SELECTEDVALUE]] — combine with the Key column to build descriptive labels
- [[table_transformcolumntypes]] — ensure Key column is text type
- [[Build-Period-Table]] — similar Power Query table-building pattern
