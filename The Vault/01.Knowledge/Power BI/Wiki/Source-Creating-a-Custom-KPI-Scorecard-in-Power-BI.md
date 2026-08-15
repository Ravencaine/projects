---
created: 2026-08-09
updated: 2026-08-09
source: "Creating a Custom KPI Scorecard in Power BI.md"
source_url: https://databear.com/creating-a-custom-kpi-scorecard-in-power-bi/
note_type: source
tags: [power-bi, kpi, dax, scorecard, conditional-formatting, databear, boniface-muchendu]
---

# Creating a Custom KPI Scorecard in Power BI

Custom KPI scorecard using DAX measures for values, thresholds, indicators, and colors — replacing the built-in KPI visual with a Matrix + conditional formatting approach.

> **Type:** article
> **Author:** Boniface Muchendu
> **Published:** 2026-03-23
> **URL:** https://databear.com/creating-a-custom-kpi-scorecard-in-power-bi/
> **Routed to:** Power BI

## Summary

Builds a custom KPI scorecard in Power BI using a three-measure chain: a status measure driven by threshold logic, a UNICHAR-based indicator for trend arrows, and a color measure for conditional font formatting — applied to a Matrix visual instead of the built-in KPI visual.

## Key Claims

- Custom scorecards give full control over threshold values and symbols, avoiding the built-in KPI visual's limitations
- Thresholds should live in DAX measures so they are defined once and propagate everywhere
- UNICHAR renders symbols (arrows) directly inside text values without external assets
- A three-measure chain (status → indicator → color) keeps each measure single-purpose
- Conditional formatting is applied per-field in the formatting pane, not inside the measure itself

## Notable Details

- `Report Tooltip` measure uses `SELECTEDVALUE(Sales[Amount])` — returns blank when context is ambiguous
- Image attachments (KPI matrix screenshot, conditional formatting screenshot) are in `99.System/Attachments/`
- The article uses Year-over-Year sales as the example KPI value
- Thresholds used: ±5% band = neutral; below −5% = negative; above +5% = positive

## Extracted Notes

Links to notes derived from this source:

- [[KPI-Scorecard-UNICHAR-SWITCH-Workflow]] — `workflow` — end-to-end implementation of the scorecard pattern
- [[UNICHAR-KPI-Indicator-SWITCH-Pattern]] — `pattern` — the three-measure chain (status + indicator + color)
- [[Author-Boniface-Muchendu]] — `author` — author profile updated

## Related

- [[conditional-formatting-in-power-bi]] — Power BI conditional formatting reference
- [[power-graphing]] — Matrix visual usage
- [[enhancing-data-narratives-power-bi-tooltips]] — tooltip design for KPI detail
- [[UNICHAR]] — Unicode character rendering in DAX
- [[SWITCH]] — SWITCH(TRUE(), ...) for threshold logic

## Metadata

| Field | Value |
|-------|-------|
| Source file | Creating a Custom KPI Scorecard in Power BI.md |
| Archived at | 99.System/InboxArchive/2026-08/ |
| Ingestion date | 2026-08-09 |
| Word count | ~350 |
