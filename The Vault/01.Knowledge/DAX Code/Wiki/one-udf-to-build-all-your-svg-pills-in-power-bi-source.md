---
created: 2026-08-02
updated: 2026-08-05
source: One UDF to Build All Your SVG Pills in Power BI
source_url: https://medium.com/microsoft-power-bi/one-udf-to-build-all-your-svg-pills-in-power-bi-43da8ca9058e
note_type: source
tags: [dax, power-bi, svg, udf, pill, visualization]
---

# One UDF to Build All Your SVG Pills in Power BI

Generate reusable, color-coded SVG pill badges for table visuals using two DAX User-Defined Functions — no external assets needed.

> **Type:** article
> **Author:** Isabelle Bittar (KI Data Science)
> **Published:** 2025-11-27
> **URL:** https://medium.com/microsoft-power-bi/one-udf-to-build-all-your-svg-pills-in-power-bi-43da8ca9058e
> **Routed to:** DAX Code

## Summary

Two DAX UDFs — `UDF_EncodeSVG` (URL-encodes raw SVG) and `UDF_SVGPillCanvas` (draws the pill) — provide a reusable foundation for any SVG pill in Power BI. The UDFs handle all geometry and encoding; each pill measure handles only its label selection and color mapping. This separation of concerns means a new pill variant is a 10–15 line measure, not a new UDF. The article demonstrates status pills (filled background) and priority pills (dot-only signal) in a table visual.

## Key Claims

- DAX UDFs enable a reusable SVG pill architecture across reports — define once, call from many measures
- `UDF_EncodeSVG` is a generic utility: any SVG-drawing UDF or measure calls it to encode its output
- Pill geometry is fully dynamic: width scales with `LEN(label)`, dot/text positions adjust automatically
- Keeping colors in dedicated measures (not in UDF bodies) creates a maintainable design system
- The pattern works for statuses, priorities, departments, tags, and any categorical label
- UDFs must be enabled in Preview features and require "Update model with changes" to activate

## Notable Details

- **Preview feature:** UDFs in Power BI are still in preview as of late 2025 — must be enabled in Options
- **UDF encode order matters:** SUBSTITUTE chains from s0→sB sequentially; encoding `%` first prevents double-encoding of `%25` in later passes
- **Data category required:** Pill measures must have Data Category = Image URL to render as images
- **Image size must match UDF canvas:** Table visual Grid → Image size Height = 28px, Width = 200px
- The `_pillW - 1` and `_pillH - 1` in the rect dimensions create a 1px aesthetic margin inside the rounded pill edge
- `dominant-baseline="middle"` in the SVG `<text>` element handles vertical centering without manual `y` offset
- PBIX available for download

## Extracted Notes

Links to notes derived from this source:

- [[svg-pill-pattern-udf-based]] — `pattern` — end-to-end SVG pill architecture
- [[udf_encodesvg-url-encoder-for-svg]] — `function` — URL encoder UDF
- [[udf_svgpillcanvas-generic-pill-renderer]] — `function` — generic pill renderer UDF
- [[task-status-pill-measure]] — `pattern` — filled status pill example
- [[task-priority-pill-measure-with-dot]] — `pattern` — priority pill with dot signal
- [[svg-pill-geometry-dynamic-sizing]] — `atomic` — geometry derivation
- [[udf-separation-principle-drawing-vs-semantics]] — `atomic` — design principle
- [[udf-svg-pill-setup-checklist]] — `snippet` — setup checklist
- [[Author-Isabelle-Bittar]] — `author` — author note (already exists, extend if needed)

## Metadata

| Field | Value |
|-------|-------|
| Source file | One UDF to Build All Your SVG Pills in Power BI.md |
| Archived at | pending — source remains in Inbox |
| Ingestion date | 2026-08-02 |
| Word count | ~1,100 |
