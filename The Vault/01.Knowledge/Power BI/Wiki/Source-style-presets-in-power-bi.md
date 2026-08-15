---
created: 2026-08-04
source: Style Presets in Power BI
source_url: https://databear.com/power-bi-style-presets/
note_type: source
tags: [power-bi, style-presets, json, theming, formatting]
---

# Style Presets in Power BI — Source

Reusable visual-level formatting templates in Power BI, defined in JSON theme files. Introduced March 2025. Apply consistent formatting to individual visuals across reports with one click.

> **Type:** article
> **Author:** Boniface Muchendu (DataBear)
> **Published:** 2025-05-04
> **URL:** https://databear.com/power-bi-style-presets/
> **Routed to:** Power BI

## Summary

Style presets live under `visualStyles` in the theme JSON. Each preset targets a visual type (card, columnChart, etc.) and defines formatting properties. Use the `*` key for the default preset. Presets appear in the format pane once a matching visual is selected. Not visible unless defined in the JSON — no UI editor yet.

## Key Techniques

- `visualStyles` > visual type > `*` (default) > `stylePresets` structure
- `*` key determines which preset loads by default
- Requires Power BI Desktop March 2025 or newer
- Export existing theme JSON, add `stylePresets` block, re-import
- VS Code with JSON folding (`Ctrl+K Ctrl+0`) recommended for editing

## Extracted Notes

- [[style-presets-in-power-bi]] — pattern — JSON structure and workflow
- [[style-presets-json]] — snippet — `visualStyles` JSON template
- [[boniface-muchendu]] — author

## Metadata

| Field | Value |
|-------|-------|
| Source file | Style Presets in Power BI |
| Ingestion date | 2026-08-11 |
| Video attachment | [[Attachments/Video/New Power BI Style Presets Demo.mp4]] |
