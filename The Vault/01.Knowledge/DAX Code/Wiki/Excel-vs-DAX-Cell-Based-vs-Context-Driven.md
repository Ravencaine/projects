---
created: 2026-08-09
updated: 2026-08-09
source: "DAX vs Excel Formulas What's the Real Difference.md"
note_type: comparison
tags: [dax, excel, comparison, cell-based, context-driven, filter-context, row-context]
---

# Excel vs DAX — Cell-Based vs Context-Driven

> **Type:** comparison
> **Routed to:** DAX Code
> **Primary source:** Elle Harrison, Select Distinct — 2026-07-08

## Summary

Excel uses cell-position references (A1, B2); DAX uses table/column references within a semantic model. Excel formulas break at scale (multiple sheets, new departments, growth). DAX measures are context-aware and automatically propagate across all visuals.

## Core Difference

| Dimension | Excel | DAX |
|-----------|-------|-----|
| Reference unit | Cell (A1, B2, range) | Table[Column] |
| Recalculation trigger | Manual or sheet change | User interaction / filter context |
| Propagation | Cell-to-cell chain | Single measure, all visuals |
| Growth | Formula chains break | Model scales (millions of rows) |

## Excel Formula Pain Points at Scale

- New departments → helper columns, new sheets, manual updates
- Multiple spreadsheets → fragile cross-sheet references
- Thousands of rows → slow recalculation
- Broken cell → chain of broken cells
- No distinction between stored values and calculations

## DAX Strengths at Scale

- One measure used everywhere: tables, charts, cards, tooltips
- Model relationships drive propagation automatically
- Filter context changes drive recalculation without formula edits
- Semantic model handles millions of rows efficiently (VertiPaq compression)

## Formula Translation Reference

```
Excel SUM          → DAX SUM(Table[Column])
Excel SUMIF        → DAX CALCULATE(SUM(...), FILTER(...))
Excel SUMPRODUCT   → DAX SUMX(Table, Table[A] * Table[B])
Excel XLOOKUP      → DAX RELATED() or LOOKUPVALUE()
```

## When to Use Each

| Use case | Tool |
|----------|------|
| Personal analysis, one-off modelling | Excel |
| Large-scale, automated, interactive reporting | DAX / Power BI |
| Static spreadsheet distribution | Excel |
| Model-driven dashboards with user filters | DAX |

## See Also

- [[Source-DAX-vs-Excel-Formulas]] — source article by Elle Harrison / Select Distinct
- [[DAX-Row-Context]] — row context in DAX vs Excel's row-by-row evaluation
- [[DAX-Filter-Context]] — filter context: the core DAX mental model
