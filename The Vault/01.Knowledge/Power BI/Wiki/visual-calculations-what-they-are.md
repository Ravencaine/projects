---
created: 2026-08-02
updated: 2026-08-02
source: Using Visual Calculation To Easily Calculate Avg 3 Month Sales In Power BI(.pbix included).md
note_type: atomic
tags: [power-bi, atomic, visual-calculation, dax, beginner]
---

# Visual Calculations — What They Are

Visual Calculations is a Power BI feature that allows analysts to write DAX expressions directly within a specific visual, rather than creating measures in the model. Calculations are scoped to that visual only and respect the visual's row ordering.

## Core Concept

Traditional DAX measures live in the data model and are evaluated in filter context. Visual calculations live inside a specific visual and are evaluated in the visual's row context, which includes the physical row order displayed in the visual.

## When to Use Visual Calculations

| Use When | Use Model Measures Instead |
|---|---|
| Calculation is unique to one visual | Calculation is reused across multiple visuals |
| Calculation depends on visual row order | Calculation is independent of row ordering |
| Non-technical users need a quick formula | Complex logic requiring model-level context |
| Rapid prototyping | Production-grade reusable logic |

## How to Create One

1. Right-click on a visual
2. Select **New visual calculation**
3. Write the DAX expression
4. Press Enter

The expression is scoped to that visual and does not appear in the model field list.

## New Visual Calculation Functions

Visual calculations introduce functions not available in model-level DAX:

- `MOVINGAVERAGE` — rolling window average across rows
- `RUNNINGSUM` — cumulative sum across rows
- `OFFSET` — reference a row N positions away
- `ISATLEVEL` — check if the current row is at a specific hierarchy level
- `ISMEtLEVEL` — check if current context is at or above a hierarchy level

## Related

- [[movingaverage-visual-calc]] — `function`
- [[isatlevel-guard-pattern]] — `pattern`
