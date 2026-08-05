---
created: 2026-08-05
updated: 2026-08-05
source: Circular Images in Power BI (Isabelle Bittar)
source_url: https://medium.com/microsoft-power-bi/how-to-create-circular-images-in-power-bi-that-actually-render-properly-6d51849415d6
note_type: source
tags: [power-bi, svg, base64, image, visualization, power-query, dax]
---

# Circular Images in Power BI (Isabelle Bittar)

How to render circular profile images in Power BI table visuals using Power Query Base64 conversion and DAX SVG generation — a pattern that separates image data from presentation.

> **Type:** article
> **Author:** Isabelle Bittar (KI Data Science)
> **Published:** 2025-12-11
> **URL:** https://medium.com/microsoft-power-bi/how-to-create-circular-images-in-power-bi-that-actually-render-properly-6d51849415d6
> **Routed to:** Power BI (primary), Power Query

## Summary

Isabelle Bittar solves Power BI's inability to crop images into circles by separating image data (converted to Base64 in Power Query) from presentation (SVG circular clipPath in DAX). The key insight: Power BI blocks external image URLs inside SVGs, so the image must be embedded as a Base64 data URL. The pattern works for employee avatars, product images, building photos, and asset previews — any rectangular image that needs circular display in table visuals.

## Key Claims

- Power BI has no native image masking or cropping — SVG clipPath is the workaround but fails with external image URLs
- Circular images require Base64 embedding: download → convert → store as text in Power Query
- SVG handles only shape and layout; Base64 carries the image data as a `data:image/svg+xml;utf8,` string
- Set the table visual column format to "Image URL" for the DAX SVG measure to render
- The pattern is reusable: same logic, different image source = different use case
- Optional enhancements: colored status borders, category rings, initials fallback, SVG profile cards

## Notable Details

- PBIX available for download (Google Drive link in source)
- `fxImageToBase64` Power Query function uses `Web.Contents()` + `Binary.ToText(Source, BinaryEncoding.Base64)`
- The SVG uses `clipPath` for circular crop and `preserveAspectRatio="xMidYMid slice"` for smart centering
- An optional grey background circle gives contrast during image load
- `SUBSTITUTE` is used in DAX to escape `&` as `&amp;` in XML attributes
- CSS `<style>` block inside the SVG DAX string controls font-family, size, and fill for text elements
- Image URL format must be set on the table visual column (not just the measure) for rendering to work
- Large image libraries in Base64 bloat the model size — best for demo datasets and controlled internal assets

## Extracted Notes

Links to notes derived from this source:

- [[fxImageToBase64-Power-Query]] — `function` — Power Query M function to convert image URLs to Base64 data URLs
- [[Circular-Image-Power-BI-Table-Pattern]] — `pattern` — the complete 2-step pattern: Power Query Base64 + DAX SVG circular clip
- [[DAX-SVG-Circular-Image-Snippet]] — `snippet` — copy-paste DAX measure for a circular profile image
- [[DAX-SVG-Profile-Card-Snippet]] — `snippet` — copy-paste DAX measure for a circular avatar + name + email SVG card
- [[SVG-in-Power-BI-Key-Concepts]] — `reference` — clipPath, viewBox, preserveAspectRatio, data URI at a glance
- [[Power-Query-Base64-Conversion-Reference]] — `reference` — Web.Contents, Binary.ToText, BinaryEncoding.Base64 key facts
- [[Circular-Image-Parameters-Reference]] — `reference` — circle cx/cy/r, viewBox dimensions, image width/height at a glance
- [[Image-Masking-Limitation-Power-BI]] — `atomic` — why Power BI blocks external URLs inside SVGs and the Base64 workaround
- [[Author-Isabelle-Bittar]] — `author` — Isabelle Bittar, independent BI and data science consultant, KI Data Science

## Metadata

| Field | Value |
|-------|-------|
| Source file | Circular Images in Power BI (Isabelle Bittar).md |
| Archived at | 99.System/InboxArchive/2026-08/ |
| Ingestion date | 2026-08-05 |
| Word count | ~900 |
| PBIX attachment | [Circular_Images_Power_BI.pbix](file:///C:/Users/krlsa/Documents/00%20Projects/The%20Vault/99.System/Attachments/Circular_Images_Power_BI.pbix) |
