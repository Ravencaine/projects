---
created: 2026-08-06
updated: 2026-08-06
source: Conditionally Color-Coding Line Charts in Power BI 📈
source_url: https://medium.com/the-bi-corner/conditionally-color-coding-line-charts-in-power-bi-3978fd93a2cc
note_type: source
tags: [line-chart, conditional-color, power-bi, visualization, overlay-series, dax]
---

# Conditionally Color-Coding Line Charts in Power BI (Bittar / KI Data Science)

A Medium article by Isabelle Bittar (KI Data Science) explaining how to conditionally color-code a line chart in Power BI — using two overlay DAX measure series and static Format pane colors.

> **Type:** article
> **Author:** Isabelle Bittar (KI Data Science)
> **Published:** 2025-04-26
> **URL:** https://medium.com/the-bi-corner/conditionally-color-coding-line-charts-in-power-bi-3978fd93a2cc
> **Routed to:** Power BI

## Summary

Power BI line charts have no built-in conditional formatting (unlike bar/column charts). The article presents the overlay series technique: create two measures that each return the same price data but only when their condition is met (positive/negative price variation), place both on the Y-axis, color them green and red via the Format pane, then adjust the IF() conditions to return BLANK() when not met. Key insight: set colors BEFORE adjusting the conditions to hide the inactive series. Uses Bitcoin price data as the example. PBIX available for download (Google Drive link — not downloaded).

## Key Claims

- Line charts do not expose conditional formatting in the Format pane — the workaround is two overlapping series
- IF() must return BLANK() (not 0) when the condition is not met — returning 0 creates a flat zero line
- Colors must be set before making the IF() conditions hide the inactive series
- A disconnected Calendar table (not linked to the model) drives the X-axis continuity without interfering with slicer filtering
- Price Variation = Current Price − Last Price (where both are calculated from DateSelection-driven min/max dates)
- The technique works for Area charts too

## Notable Details

- PBIX download: Google Drive folder (scan_for_downloads.py: GDrive → skipped)
- Isabelle Bittar article cross-referenced: "Using Time Periods as Slicers to Enhance Power BI Line or Area Charts' Range" — already in vault (archived)
- [[Author-Isabelle-Bittar]] already extended with sources; this is source #7
- Technique is Technique 4 in [[Color-Coding-4-Techniques]] — existing note already references `[[Dynamic-Line-Area-Chart-Color]]` as the follow-on

## Extracted Notes

Links to notes derived from this source:

- [[Conditional-Color-Coding-Line-Charts-in-Power-BI]] — `atomic` — concept overview
- [[Line-Chart-Overlay-Pattern-for-Conditional-Color]] — `pattern` — full DAX pattern reference
- [[Build-a-Conditionally-Color-Coded-Line-Chart]] — `workflow` — step-by-step

## Metadata

| Field | Value |
|-------|-------|
| Source file | Conditionally Color-Coding Line Charts in Power BI 📈.md |
| Archived at | 99.System/InboxArchive/2026-08/ |
| Ingestion date | 2026-08-06 |
| Word count | ~1,600 |
