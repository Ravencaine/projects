---
created: 2026-08-09
updated: 2026-08-09
source: "5 Boring Excel Functions That Are Secretly Brilliant • My Online Training Hub"
source_url: "https://www.myonlinetraininghub.com/5-boring-excel-functions-that-are-secretly-brilliant"
published: 2026-07-21
note_type: source
tags: [excel, functions, beginner, advanced, formulas]
---

# 5 Boring Excel Functions — My Online Training Hub / Mynda Treacy

Source: My Online Training Hub. Published 2026-07-21. Author: Mynda Treacy — new author not previously in vault.

## Summary

Five underrated Excel functions available in virtually every version (no Microsoft 365 required). Each solves a specific, common business problem. Core message: small, composable techniques beat one giant formula.

## The Five Functions

| # | Function | Core Problem Solved |
|----|----------|---------------------|
| 1 | `ABS` | Misleading % change when prior year is negative |
| 2 | `SIGN` | Double-counting in SUMPRODUCT OR logic |
| 3 | `REPT` | In-cell bar charts without chart objects |
| 4 | `TRUNC` | Whole quantities from division (vs INT for negatives) |
| 5 | `CELL` | Dynamic worksheet name from file path |

## Key Insights Extracted

- [[ABS-Absolute-Value]] — `atomic` — removes sign; fixes % change with negative denominators; invoice tolerance checks
- [[SIGN-Function-OR-Logic-SUMPRODUCT]] — `atomic` — SIGN((A)+(B)) prevents double-counting in SUMPRODUCT OR conditions
- [[REPT-In-Cell-Bar-Charts]] — `atomic` — in-cell visual bar charts; dashboards, KPI reports, heat maps
- [[TRUNC-vs-INT-Negative-Numbers]] — `atomic` — TRUNC moves toward zero; INT always rounds down; critical for negative numbers
- [[CELL-Function-Dynamic-Worksheet-Name]] — `atomic` — MID(CELL("filename",A1), FIND("]",CELL("filename",A1))+1, 31) extracts sheet name from path

## Author

- [[Author-Mynda-Treacy]] — created alongside this source
