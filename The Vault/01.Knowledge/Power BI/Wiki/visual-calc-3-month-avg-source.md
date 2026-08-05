---
created: 2026-08-02
updated: 2026-08-02
source: Using Visual Calculation To Easily Calculate Avg 3 Month Sales In Power BI(.pbix included).md
source_url: https://medium.com/microsoft-power-bi/using-visual-calculation-to-easily-calculate-avg-3-month-sales-in-power-bi-pbix-included-0a6d3b76f703
note_type: source
tags: [power-bi, medium, dax, visual-calculation, movingaverage, beginner, tutorial]
---

# Using Visual Calculation To Easily Calculate Avg 3 Month Sales In Power BI

A beginner-level tutorial demonstrating how to use Visual Calculations (a Power BI feature) to compute a 3-month rolling sales average directly within a table visual — without writing complex DAX measures at the model level.

> **Type:** tutorial / beginner
> **Level:** Beginner
> **Category:** DAX
> **Author:** Shashanka Shekhar (Microsoft Power BI contributor)
> **Published:** 2026-07-27
> **URL:** https://medium.com/microsoft-power-bi/using-visual-calculation-to-easily-calculate-avg-3-month-sales-in-power-bi-pbix-included-0a6d3b76f703
> **Routed to:** Power BI / DAX

## Summary

Tutorial: right-click a table visual → New visual calculation → write `MOVINGAVERAGE([Total Sales], 3)` wrapped in `IF(ISATLEVEL([Month]), ...)` to calculate a 3-month rolling average. `ISATLEVEL` acts as a guard — returns `TRUE` only at the Month row level, preventing misleading averages from appearing on Year rollup rows. `FORMAT()` applies number formatting but converts the result to text. Includes PBIX download link.

## Key Claims

- Visual Calculations are more intuitive than traditional DAX for rolling averages
- `MOVINGAVERAGE` is scoped to the visual's row ordering (not model context)
- `ISATLEVEL` prevents misleading values at rollup levels
- `FORMAT()` converts numeric output to text

## Notable Details

- Visual calculation: `IF(ISATLEVEL([Month]), FORMAT(MOVINGAVERAGE([Total Sales], 3), "#,#.0"))`
- `MOVINGAVERAGE([Total Sales], 3)` = current row + previous 2 rows
- `FORMAT(..., "#,#.0")` = thousands separator + 1 decimal place
- PBIX file available for download
- Beginner level, DAX category

## Extracted Notes

- [[movingaverage-visual-calc]] — `function` — MOVINGAVERAGE syntax, rolling window, visual vs model scope
- [[isatlevel-guard-pattern]] — `pattern` — ISATLEVEL as guard against rollup row misleading values; context table
- [[format-visual-calc-returns-text]] — `gotcha` — FORMAT converts to text, breaks sorting and numeric further calculations
- [[visual-calculations-what-they-are]] — `atomic` — What visual calculations are, how to create, when vs model measures

## Downloads

- **PBIX file:** [[99.System/Attachments/Using-Visual-Calculation-Avg-3-Month-Sales-In-Power-BI/Avg3_Months_Power_BI.pbix]]
- **Sample data (CSV):** [[99.System/Attachments/Using-Visual-Calculation-Avg-3-Month-Sales-In-Power-BI/Avg3Mnths.csv]]

## Metadata

| Field | Value |
|-------|-------|
| Source file | `Using Visual Calculation To Easily Calculate Avg 3 Month Sales In Power BI(.pbix included).md` |
| Archived at | 99.System/InboxArchive/2026-08/ |
| Ingestion date | 2026-08-02 |
| Word count | ~500 |
| Language | English |
