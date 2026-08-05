---
created: 2026-07-27
updated: 2026-08-02
source: "Using Visual Calculation To Easily Calculate Avg 3 Month Sales In Power BI(.pbix included).md"
note_type: atomic
tags: [power-bi, visual-calculations, new-feature, measure-alternative, model-fragmentation]
---

# Visual Calculations: When to Use vs. When to Use Measures

Visual Calculations allow DAX-like expressions directly inside a visual — fast to write, but scoped to that visual only. This creates a critical decision point: visual calculation or model measure?

## What Visual Calculations Are

Expressions written directly in the visual using a simplified DAX-like syntax with relative references:

```dax
-- Visual Calculation (inside a specific visual):
Running Total = CALCULATE(SUM(Sales[Amount]), RUNNINGTOTAL)
Percent of Total = [Amount] / CALCULATE(SUM(Sales[Amount]), ALLSELECTED())
```

## The Decision Framework

| Scenario | Use Visual Calculation | Use Model Measure |
|---------|----------------------|------------------|
| One-off calculation used only in this visual | Yes | No |
| Calculation should appear on multiple visuals | No | Yes |
| Calculation is a business KPI | No | Yes |
| Rapid prototyping / what-if analysis | Yes | No |
| Calculation requires RLS (row-level security) | No | Yes |
| Calculation is complex and needs testing | No | Yes |
| Calculation needs to be shared with other analysts | No | Yes |

## The Model Fragmentation Risk

**Anti-pattern: Visual Calculation everywhere**

- Visual A: running total in visual calculation
- Visual B: same running total, duplicated in another visual calculation
- Problem: business changes the running total definition — update both visuals manually

**Better: Centralized measure**

```dax
-- In the model:
Running Total = CALCULATE(SUM(Sales[Amount]), RUNNINGTOTAL)
```
Now both visuals reference [[runningsum]] — one change propagates everywhere.

## Quick Decision Rule

> If another visual in the report might need this calculation, it belongs in the model as a measure — not in the visual as a Visual Calculation.

## Syntax Note

Visual Calculations use simplified relative syntax. RUNNINGTOTAL, PERCENTTOTAL, and other relative operators work within the visual's context but are **not available in model measures**.

## Related

- [[measure-branching-pattern]] — organizing centralized model measures
- [[power-bi-dashboard-checklist]] — pre-publish review for calculation governance
