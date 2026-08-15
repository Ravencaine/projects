---
created: 2026-08-06
updated: 2026-08-06
source: Conditional Formatting in Power BI Multi-Row Card Visuals
source_url: https://databear.com/power-bi-multi-row-card-visuals/
note_type: source
tags: [conditional-formatting, multi-row-card, power-bi, dax, unichar]
---

# Conditional Formatting in Power BI Multi-Row Card Visuals (Muchendu / Data Bear)

A Data Bear blog post by Boniface Muchendu explaining how to add conditional formatting icons to Multi-Row Card visuals using DAX UNICHAR measures — covering circles, arrows, and percentage formatting.

> **Type:** article
> **Author:** Boniface Muchendu (Data Bear)
> **Published:** 2024-03-17
> **URL:** https://databear.com/power-bi-multi-row-card-visuals/
> **Routed to:** Power BI

## Summary

The article identifies a gap in Power BI's Multi-Row Card visual — it lacks the conditional formatting option available in tables and matrices. The workaround uses a DAX measure with UNICHAR() to render conditional icons directly as text values within the card. Covers three stages: basic circle indicators (green/red), enhanced formula with FORMAT() for percentage display, and switching to arrow indicators (up/down triangles). ISBLANK() is used to handle missing data gracefully.

## Key Claims

- Multi-Row Card Format pane does not include a Conditional formatting section
- UNICHAR(11044) = 🟢 green circle, UNICHAR(128308) = 🔴 red circle, UNICHAR(9650) = ▲ up arrow, UNICHAR(9660) = ▼ down arrow
- FORMAT([Profit Growth], "0.0%") converts the number to percentage with one decimal place
- ISBLANK([Profit Growth]) guard prevents misleading icons for rows without data
- Icons work in Multi-Row Card, Card, and KPI visuals — any text-rendering visual
- The measure is portable: drop into any visual that displays text values

## Notable Details

- Images referenced in source (already in Attachments): _DAX_for_Conditional_Formatting_in_Power_BI.png, Incorporating_the_Measure_into_the_Visual.png, Enhancing_the_Measure_for_Clarity_Muticard.png, Expanding_the_Solution_Multi-Row_Card_Visuals.png
- [[Author-Boniface-Muchendu]] already extended with this as source #6
- [[UNICHAR]] and [[conditional-formatting-via-dax]] already in vault — the new notes link to these for the DAX function and general conditional formatting context

## Extracted Notes

Links to notes derived from this source:

- [[Conditional-Formatting-in-Multi-Row-Card-Visuals]] — `atomic` — concept overview
- [[UNICHAR-based-Conditional-Formatting-Pattern]] — `pattern` — DAX patterns for circles and arrows
- [[Add-Conditional-Formatting-to-Multi-Row-Card]] — `workflow` — step-by-step guide
- [[UNICHAR-Icon-Codes-Reference]] — `reference` — Unicode code point quick reference

## Metadata

| Field | Value |
|-------|-------|
| Source file | Conditional Formatting in Power BI Multi-Row Card Visuals.md |
| Archived at | 99.System/InboxArchive/2026-08/ |
| Ingestion date | 2026-08-06 |
| Word count | ~500 |
