---
created: 2026-07-27
updated: 2026-08-02
source: "Visual Calculations Just Went GA. They'll Save You Hours — and Quietly Fragment Your Model If You Let Them"
source_url: "https://medium.com/power-bi-made-easy/visual-calculations-just-went-ga-9f5a6b8c0d2m"
note_type: source
tags: [power-bi, visual-calculations, new-feature, ga, model-fragmentation]
---

# Visual Calculations (GA)

> **Type:** article
> **Author:** Gulab Chand Tejwani
> **Published:** 2025-11-03
> **URL:** https://medium.com/power-bi-made-easy/visual-calculations-just-went-ga-9f5a6b8c0d2m
> **Routed to:** Power BI

## Summary

Visual Calculations (now Generally Available) allow DAX-like expressions to be written directly inside Power BI visuals — without creating measures in the model. This accelerates report development but creates a model fragmentation risk: calculations stored only in visuals are invisible to other visuals, untested, and impossible to reuse.

## Key Claims

- Visual Calculations are scoped to a single visual — not reusable across the report
- The model fragmentation risk: every analyst adds calculations to their visual; the logic is never centralized
- Best use: quick prototyping, one-off calculations, calculations that genuinely belong to one visual
- Dangerous use: replacing measures that should be centralized in the model

## Notable Details

- Visual Calculations use a simplified DAX syntax with relative referencing (e.g., RunningTotal instead of CALCULATE + FILTER)
- Syntax: `CALCULATE(SUM(Sales), RUNNINGTOTAL)` — relative references work within the visual context
- Available in: Power BI Desktop (latest), Power BI Service

## Extracted Notes

- [[visual-calculations-usage-guide]] — atomic — when to use vs. when to use measures

## Metadata

| Field | Value |
|-------|-------|
| Source file | Visual Calculations Just Went GA. They'll Save You Hours — and Quietly Fragment Your Model If You Let Them.md |
| Archived at | 99.System/InboxArchive/2026-07/ |
| Ingestion date | 2026-07-27 |
| Word count | ~1,937 |
