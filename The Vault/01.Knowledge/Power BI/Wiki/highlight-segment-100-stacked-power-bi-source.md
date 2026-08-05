---
created: 2026-08-02
updated: 2026-08-02
source: How to Highlight a Segment in a 100% Stacked Chart and Move It to the Baseline in Power BI.md
source_url: https://medium.com/microsoft-power-bi/how-to-highlight-a-segment-in-a-100-stacked-chart-and-move-it-to-the-baseline-in-power-bi-fbb68f3dade6
note_type: source
tags: [power-bi, medium, 100-stacked-chart, dax, disconnected-table, position-measure, baseline, tooltip]
---

# Highlight Segment 100% Stacked Power BI

A technique for making a user-selected category always sit on the chart baseline in a 100% stacked bar or column chart — the selected segment appears in a highlight color, all others stack above in grey. Uses N separate position measures instead of one measure + category field, with a disconnected Selector table and optional custom tooltip page.

> **Type:** tutorial / advanced visualization
> **Author:** Iwa Sanjaya (Power BI Masterclass / PowerLib)
> **Published:** 2026-07-27
> **URL:** https://medium.com/microsoft-power-bi/how-to-highlight-a-segment-in-a-100-stacked-chart-and-move-it-to-the-baseline-in-power-bi-fbb68f3dade6
> **Routed to:** Power BI

## Summary

The article explains why only baseline segments in 100% stacked charts are reliably comparable (floating segments distort apparent length), then provides a complete implementation: disconnected `Selector` DATATABLE for the slicer, Position 1–N measures using rank arithmetic (`TargetRank = IF(k < SelRank, k, k+1)`) to always put the selected category at Position 1, per-measure color formatting (highlight on Position 1, grey gradient on rest), legend off, optional sort-by-Position-1, optional custom tooltip page using a `Tooltip Position` table and `Ord Category/Value` measures with rank-inverted SWITCH logic. Gotchas covered: circular dependency from separate Sort Order calculated column (fix: same DATATABLE literal), Power Query vs DAX sort column (M for real dimension tables, DATATABLE literals for disconnected tables).

## Key Claims

- One measure + category field in Legend cannot control stacking order — DAX cannot reach the chart engine
- N separate position measures solve this: which measure is plotted first determines which category touches the baseline
- Disconnected `Selector` table: no relationship, feeds `SELECTEDVALUE()` only
- Sort column in separate DAX calculated column → circular dependency error
- Sort column in Power Query (M) → no dependency cycle for real imported dimension tables
- Native tooltip shows "Position 1/2/3…" — custom tooltip page required

## Notable Details

- Position arithmetic: `TargetRank = IF(k < SelRank, k, k+1)` — k stays at k if before selected rank, shifts to k+1 if after
- For exactly 3 categories: direct SWITCH branches simpler than rank formula
- Tooltip page: Matrix visual required (not Table), rows from `Tooltip Position[Pos]`, Ord measures compute category name per row position
- `Ord Font Color` measure returns color for Pos=1, blank for others — conditional font color hides it on non-highlighted rows
- `SELECTEDVALUE(Selector[Category], "Value A")` sets a default when nothing is selected

## Extracted Notes

- [[stacked-chart-baseline-order-matters]] — `atomic` — Only baseline segments are reliably comparable; position order is chart-engine-controlled
- [[stacked-chart-baseline-highlight-pattern]] — `pattern` — Full pattern: Selector + Position N + color formatting + slicer + optional tooltip
- [[selector-datatable-disconnected-table]] — `function` — DATATABLE with literal Category + Sort Order in same call
- [[position-measures-stacked-chart]] — `function` — Position 1 (selected) + Position k (rank arithmetic); simple SWITCH for N=3
- [[color-by-position-visual-formatting]] — `pattern` — Per-measure colors; highlight on P1, grey gradient on P2…N; legend off
- [[stacked-chart-custom-tooltip]] — `pattern` — Tooltip Position DATATABLE + Ord Category/Value/AbsoluteValue/FontColor measures
- [[sort-column-pq-vs-dax]] — `pattern` — M for real imported dimensions; DATATABLE literals for disconnected tables
- [[circular-dependency-datatable-gotcha]] — `gotcha` — Separate Sort Order calculated column creates cycle; fix: same DATATABLE
- [[stacked-highlight-test-checklist]] — `reference` — 8-point verification checklist

## Metadata

| Field | Value |
|-------|-------|
| Source file | `How to Highlight a Segment in a 100% Stacked Chart and Move It to the Baseline in Power BI.md` |
| Archived at | 99.System/InboxArchive/2026-08/ |
| Ingestion date | 2026-08-02 |
| Word count | ~2,300 |
| Language | English |
