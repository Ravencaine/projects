---
created: 2026-08-13
source: "3 Hacks to Turn Any Image into a Circle in Power BI"
source_url: https://datatraining.io/blog/3-hacks-image-to-circle
note_type: workflow
tags: [powerpoint, image-crop, oval, save-as-picture, png, circular-image]
---

# Pre-Circularize Images in PowerPoint

Convert a small set of local image files into circular PNGs by cropping them to an oval inside PowerPoint, then save them as new picture files for use in Power BI.

## When to Use

- You have direct access to the image files (local drive, shared folder) — not just URLs.
- The set is small (under ~20 images) and the list rarely changes.
- You want zero code, no extra tools, and no model changes.

## Prerequisites

- PowerPoint (any modern version — 2016+)
- The original image files

## Steps

### 1 — Insert the Image

Open PowerPoint → **Insert → Pictures** → select the image. It lands as a rectangle on the slide.

### 2 — Crop to an Oval

With the image selected → **Picture Format → Crop → Crop to Shape → Oval**.

Resize the oval as needed. Hold **Shift** while resizing to keep it perfectly round.

### 3 — Save as PNG

Right-click the cropped image → **Save as Picture…** → save as PNG (best transparency behaviour for circular crops).

Repeat for every image you need.

### 4 — Host the New PNGs

Upload the circular PNGs somewhere Power BI can reach:
- OneDrive for Business (best for Power BI Service)
- SharePoint document library
- A public folder accessible via URL

### 5 — Wire Up in Power BI

In Power BI Desktop:
1. **Modelling ribbon → Data category** for the URL column → set to **Image URL**.
2. Add the column to a Card visual (or any image-aware visual).
3. **Images = On → Image type = Image URL**.
4. Click `fx` → **Field value** → pick the column with the circular PNG URL.

The visual now renders the circular assets.

## Pros

- Quick, no code, no model changes.
- Works with any image-aware visual (Card, Table, Multi-row Card).
- Final output is a normal raster image — readable by every Power BI visual.

## Cons

- Manual — does not scale to hundreds of images.
- One PowerPoint action per image — slow for bulk.
- No dynamic switching back to the square version (the original URL is now orphaned).

## Related

- [[batch-circularize-images-with-python]] — when the set is large
- [[circular-overlay-mask-powerpoint-power-bi]] — alternative that keeps the original image URL
- [[circular-image-approaches-decision-guide]] — when to use which approach
