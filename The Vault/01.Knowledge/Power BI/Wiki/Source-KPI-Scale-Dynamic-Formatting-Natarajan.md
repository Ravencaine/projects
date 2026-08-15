---
created: 2026-08-10
updated: 2026-08-10
source: "Give Users Full Control Over KPI Scale with Dynamic Formatting"
source_url: "https://community.fabric.microsoft.com/t5/Power-BI-Community-Blog/Give-Users-Full-Control-Over-KPI-Scale-with-Dynamic-Formatting/ba-p/5297206"
note_type: source
tags: [power-bi, source, dynamic-format, disconnected-table, community-blog]
---

# KPI Scale Dynamic Formatting — Natarajan M

Source: Microsoft Fabric Community Blog. Published 2026-07-17. Author: Natarajan M.

> **Type:** community blog
> **Author:** Natarajan M
> **Published:** 2026-07-17
> **URL:** https://community.fabric.microsoft.com/t5/Power-BI-Community-Blog/Give-Users-Full-Control-Over-KPI-Scale-with-Dynamic-Formatting/ba-p/5297206
> **Routed to:** Power BI

## Summary

Uses Dynamic Format Strings with a disconnected dimension table to let report users switch KPI measures between Actuals, Thousands, Millions, and Billions via a slicer — all with a single base measure. The format string handles display scaling; DAX stays whole. Also demonstrates extending the pattern to multi-currency symbol switching.

## Key Claims

- Display Units (visual settings) are limited: Auto is unpredictable, Fixed units show $0.0M for small values, duplicate measures create technical debt
- Dynamic Format String + disconnected Scale table solves all three
- Step 1: Create Scale dimension table via DATATABLE (Actuals/Thousands/Millions/Billions)
- Step 2: `Selected Scale = SELECTEDVALUE('Scale'[Scale Name])`
- Step 3: Write base KPI measure as SUM — do NOT divide in DAX
- Step 4: Measure Tools → Format → Dynamic → SWITCH format string with comma placement
- Comma placement: `,.00` = /1000, `,,.00` = /1M, `,,,.00` = /1B
- Bonus: same pattern works for multi-currency (SWITCH on currency symbol)
- Benefits: self-service UX, cleaner semantic model, consistent calculations

## Notable Details

- Scale table must be sorted by an integer ID to appear in logical (not alphabetical) order
- SWITCH default fallback prevents blanks when no slicer selection is active
- No PBIX attached — technique description only

## Extracted Notes

Links to notes derived from this source:

- [[Dynamic-KPI-Scale-Disconnected-Table-SWITCH]] — `pattern` — full pattern with components and structure
- [[Dynamic-Format-String-Implementation]] — `workflow` — step-by-step implementation guide
- [[Dynamic-Format-vs-Fixed-Display-Units]] — `comparison` — when to use each approach
- [[Multi-Currency-Dynamic-Format-SWITCH]] — `pattern` — extending to currency symbol switching
- [[Keep-Base-Measure-Whole]] — `atomic` — key principle: scale in format string, not DAX

## Metadata

| Field | Value |
|-------|-------|
| Source file | Inbox |
| Archived at | pending |
| Ingestion date | 2026-08-10 |
| Word count | ~350 |
