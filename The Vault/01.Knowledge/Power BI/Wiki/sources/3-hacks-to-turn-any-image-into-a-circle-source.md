---
created: 2026-08-13
updated: 2026-08-14
source: "datatraining.io"
source_url: https://datatraining.io/blog/3-hacks-image-to-circle
video_file: 99.System/Attachments/Video/3 Hacks to Turn Any Image into a Circle in Power BI-exTSUPJPSqE.webm
transcript: 00.Inbox/3 Hacks to Turn Any Image into a Circle in Power BI - transcript.md
note_type: source
tags: [circular-image, powerpoint, python, mask, svg, base64, decision-guide, datatraining]
---

# 3 Hacks to Turn Any Image into a Circle in Power BI

> **Type:** article (web)
> **Author:** datatraining.io (How to Power BI blog)
> **Published:** not stated (sourced 2026-08-13)
> **URL:** https://datatraining.io/blog/3-hacks-image-to-circle
> **Routed to:** Power BI

A short blog post presenting three practical methods for rendering circular images in Power BI, organised as a decision guide based on what the reader has on hand (files vs URLs, count, position) and the SVG-measure-with-Base64 workaround for the URL-only case.

## Summary

datatraining.io lays out three increasingly flexible approaches to circular images in Power BI. The first is a manual PowerPoint Crop-to-Shape → Save-as-Picture flow for small batches of files. The second is a Python (Pillow) batch process for many local files. The third is a circular overlay mask built from a PowerPoint rectangle + circle merged with Combine Shapes, layered on top of the image in Power BI. The post also covers an SVG + Base64 alternative (a DAX measure embedding the image as a Base64 data URL inside an SVG with a circular clipPath) for URL-only scenarios where the image must appear inside a scrolling table.

## Key Claims

- The "lightest option that fits your scenario" principle — pick the simplest path that solves the immediate problem, not the most flexible one.
- Power BI's native Image visual renders square; Power BI has no built-in circular mask.
- Power BI blocks external image URLs referenced from inside SVGs — only Base64-embedded images survive.
- The PowerPoint "Combine Shapes" operation can punch a hole in a rectangle to produce a circular mask.
- SVG images inside a DAX measure are subject to the same column character limit (~32,767 characters) as Base64-encoded raster images — pre-resize/compress for larger sources.

## Notable Details

- The "Combine Shapes" → "Combine" operation in PowerPoint is the cleanest way to build a transparent-hole mask PNG — rectangle + circle selected, then Combine.
- The Python Pillow approach uses `Image.new("L", ...)` + `ImageDraw.ellipse(...)` to build the alpha mask, then `Image.paste(img, (0, 0), mask)` to apply it.
- The datatraining post explicitly suggests prompting an LLM (ChatGPT / Claude) to write the Python script — "you don't need to 'know Python' to run a simple script."
- The article links to a YouTube walkthrough (`https://www.youtube.com/watch?v=exTSUPJPSqE`) — the post itself is the textual counterpart.
- **Video transcript (2026-08-13) adds:** two Power Query M custom functions for Base64 encoding (basic + compressed via resize.now API); exact DAX SVG measure code with `clipPath` circle; explicit 32k character limit failure scenario for raw base64.
- The video shows that Power BI blocks external URLs inside SVG `<image href>` — the image must be embedded as a `data:` URI or Base64. A raw URL in `href` silently fails.
- The resize.now external API pattern (`Web.Contents("https://resize.now/?url=" & url & "&w=128&h=128")`) is the recommended compression path when Base64 exceeds 32k characters.

## Extracted Notes

- [[pre-circularize-images-in-powerpoint]] — `workflow` — manual Crop to Shape → Save as Picture flow
- [[batch-circularize-images-with-python]] — `workflow` — Pillow batch circularization
- [[circular-overlay-mask-powerpoint-power-bi]] — `workflow` — Combine Shapes mask layered on top
- [[circular-image-approaches-decision-guide]] — `comparison` — three-way decision framework
- [[new-card-visual-circular-image-binding]] — `atomic` — UI path for new Card visual image binding
- [[pre-resize-images-before-base64-encoding]] — `atomic` — why 32k limit requires compression before encoding
- [[URL-to-Base64-Power-Query]] — `function` — M custom function: image URL → Base64 data URL
- [[URL-to-Base64-Compressed-Power-Query]] — `function` — M custom function: image URL → resized + Base64 data URL (avoids 32k limit)
- [[DAX-SVG-Circular-Image-3-Hacks-Snippet]] — `snippet` — DAX measure for circular SVG profile image (3 Hacks version)

## Metadata

| Field | Value |
|-------|-------|
| Source file | `00.Inbox/3 Hacks to Turn Any Image into a Circle in Power BI.md` |
| Archived at | `99.System/InboxArchive/2026-08/` (pending) |
| Ingestion date | 2026-08-13 |
| Word count | ~700 |
