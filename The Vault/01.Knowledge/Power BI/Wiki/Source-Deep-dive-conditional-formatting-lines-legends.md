---
created: 2026-08-09
updated: 2026-08-09
source: "Deep dive into conditional formatting for lines and legends.md"
source_url: https://community.fabric.microsoft.com/t5/Power-BI-Updates-Blog/Deep-dive-into-conditional-formatting-for-lines-and-legends/ba-p/5331078
note_type: source
tags: [power-bi, conditional-formatting, line-chart, legend, gradient, field-value, fabric]
---

# Deep dive into conditional formatting for lines and legends (Microsoft Fabric)

> **Type:** article
> **Author:** Microsoft Fabric / DataZoe
> **Published:** 2026-08-04
> **URL:** https://community.fabric.microsoft.com/t5/Power-BI-Updates-Blog/Deep-dive-into-conditional-formatting-for-lines-and-legends/ba-p/5331078
> **Routed to:** Power BI

## Summary

Conditional formatting for lines and legends extended across many Power BI visuals. Formats: rules, gradients, field values. Applies to: line/area/stacked area/100% stacked area charts (whole lines, shading, segments, markers, series labels); bar/column/combo/ribbon/pie/donut/funnel (legend categories).

## Key Scenarios

- **Latest year highlight:** gradient from light gray → dark gray → blue based on measure; latest year stays coloured, earlier years fade
- **Spike/dip segments:** gradient dark red (min) → gray (zero) → dark blue (max)
- **Min/max markers:** DAX measure returns theme positive/negative/transparent colour; applied via Markers > Color > Field value
- **Consistent legends:** model column with colour values; every chart picks up same source; card as central legend
- **Field parameters + colours:** colour column in parameter table; colour follows measure selection
- **Gradient across legend:** legend shows categories; plotted colours reflect underlying value

## Mechanics

- Fx button → Format style: Gradient / Rules / Field value
- Gradient: min/max colours + optional midpoint
- Field value: colour from measure or column (most flexible, reusable across visuals)
- Segments: left/center/right position; gradient blending; Shade area option
- Visual calculations can supply field values (DAX logic in visual, no model measure needed)

## Metadata

| Field | Value |
|-------|-------|
| Source file | Deep dive into conditional formatting for lines and legends.md |
| Archived at | 99.System/InboxArchive/2026-08/ |
| Ingestion date | 2026-08-09 |
