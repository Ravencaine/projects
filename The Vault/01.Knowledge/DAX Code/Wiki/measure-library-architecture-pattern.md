---
created: 2026-07-27
updated: 2026-08-02
source: "DAX Measure Library Architecture: From Messy to Maintainable"
note_type: pattern
tags: [dax, measure-library, architecture, organization, folders, dependency-registry]
---

# Measure Library Architecture Pattern

A comprehensive organizational pattern for structuring all DAX measures in a PBIX file around business domains rather than technical categories, with clear naming conventions and a dependency registry.

## Purpose

Transform a chaotic PBIX model (where measures are dumped in a flat list with cryptic names) into a maintainable, self-documenting library that scales to 100+ measures and survives multiple authors over years.

## Folder Structure (Business Domain Organization)

```
Measures/
├── 00. Infrastructure/          -- Base calculations: SUM, COUNT, MIN, MAX
│   ├── _RowCount/
│   ├── _TotalAmount/
│   └── _DateRange/
│
├── 01. Revenue/
│   ├── Revenue                  -- Base revenue (simple SUM)
│   ├── Revenue LY              -- Revenue same period last year
│   ├── Revenue vs LY %         -- YoY comparison
│   ├── Revenue vs Budget
│   └── Revenue vs Budget %
│
├── 02. Profit/
│   ├── _GrossProfit             -- Internal: row-level calc (SUMX)
│   ├── _NetProfit               -- Internal: gross - costs
│   ├── Gross Margin %           -- Business KPI
│   └── Net Margin %
│
├── 03. Customer/
│   ├── Active Customers
│   ├── New Customers
│   ├── Customer LTV
│   └── Customer Rank
│
├── 04. Inventory/
│   ├── Stock On Hand
│   ├── Stock Turnover
│   └── Days of Supply
│
├── 05. Tests/                   -- Never deleted; used for validation
│   ├── TEST Revenue = SUM(Sales[Revenue])
│   ├── TEST GrossProfit = Revenue - Cost
│   └── TEST CustomerCount = DISTINCTCOUNT(Customers[CustID])
│
└── Z. Archive/                  -- Deprecated measures; kept for audit trail
    ├── [Old] Revenue Old Formula
    └── [Old] Budget v1
```

## Naming Conventions

| Prefix | Meaning | Example |
|--------|---------|---------|
| `_` (underscore) | Internal/base measure — not shown to business users | `_GrossProfit`, `_RowCount` |
| (no prefix) | Business-facing KPI — safe for end users | `Revenue`, `Gross Margin %` |
| `TEST` | Validation measure — verify base calculations | `TEST Revenue` |
| `[Old]` | Deprecated — kept for history, not used | `[Old] Revenue v1` |

## Measure Name Suffixes

| Suffix | Meaning |
|--------|---------|
| ` LY` | Same period last year |
| `vs Budget` | Variance to budget |
| `vs Budget %` | Percentage variance to budget |
| ` MTD` | Month to date |
| ` QTD` | Quarter to date |
| ` YTD` | Year to date |
| ` vs LY %` | Year-over-year percentage |

## Dependency Registry

A living document (Excel, separate tab in PBIX, or Obsidian note) tracking which KPI measures reference which base measures. Critical for safe deletion and refactoring.

| KPI Measure | Depends On | Last Validated |
|------------|-----------|----------------|
| `Gross Margin %` | `_GrossProfit`, `Revenue` | 2026-07-27 |
| `Net Margin %` | `_NetProfit`, `Revenue` | 2026-07-27 |
| `Revenue vs LY %` | `Revenue`, `Revenue LY` | 2026-07-27 |

## Performance Budgets

| Measure Type | Target |
|------------|--------|
| Base aggregation (SUM, COUNT) | <100ms |
| Intermediate measure (1-2 CALCULATEs) | <200ms |
| Complex branching KPI | <500ms |
| Time intelligence (YTD, LY) | <300ms |

## Anti-Patterns (What to Avoid)

- **Flat folder**: all measures in one folder named "Measures"
- **Technical folders**: "Aggregations", "Filters", "Calculations" (not business-readable)
- **No underscore convention**: base measures mixed with KPI measures
- **No dependency registry**: deleting a base measure silently breaks 40 KPIs
- **Descriptive suffixes on internal measures**: `_GrossProfitCalculation` instead of `_GrossProfit`

## Related

- [[measure-branching-pattern]]
- [[measure-naming-conventions]]
- [[var-in-dax]]
