---
created: 2026-08-11
updated: 2026-08-11
source: "ABC-Analysis-HowToPowerBI-Transcript.md"
note_type: source
tags: [power-bi, abc-analysis, visual-calculations, pareto, video]
---

# ABC Analysis — HowToPowerBI — Source

HowToPowerBI demonstrates an ABC/Pareto analysis in Power BI using visual calculations to build a shaded A/B/C chart with labeled bucket boundaries.

> **Type:** video
> **Author:** HowToPowerBI
> **Published:** 2025 (approx.)
> **URL:** https://www.youtube.com/watch?v=lvUELVwxdMI
> **Routed to:** Power BI

## Summary

Builds an ABC/Pareto chart using only native Power BI visual calculations (no external tools). Items are classified into A (top ~40% cumulative), B (40-80%), C (rest) by revenue. RUNNINGSUM creates the Pareto line; shading comes from stacking three bar series at 0.4, 0.8, and 1.0 with overlap formatting. Bucket labels are placed using the NEXT function to find the last item in each bucket.

## Key Claims

- Visual calculations are still underused — ABC chart is a practical showcase
- Do NOT hardcode product fields — use `ROWS` keyword for dimension flexibility
- Hide from visual ≠ delete: hidden measures are still referenced by other visual calculations
- The technique scales to any dimension (swap product ID for customer, region, etc.)

## Extracted Notes

Links to notes derived from this source:

- [[abc-classification-visual-calculations]] — pattern — full ABC Pareto chart walkthrough
- [[abc-analysis-dax-pattern]] — pattern — DAX-only ABC approach
- [[visual-calculations-functions-reference]] — reference — COLLAPSEDEALL, RUNNINGSUM, ORDER BY, NEXT

## Metadata

| Field | Value |
|-------|-------|
| Source file | ABC-Analysis-HowToPowerBI-Transcript.md |
| Ingestion date | 2026-08-11 |
| Duration | 14:09 |
