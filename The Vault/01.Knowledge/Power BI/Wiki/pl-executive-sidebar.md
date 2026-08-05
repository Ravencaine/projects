---
created: 2026-08-02
updated: 2026-08-02
source: How to Build a Clean P&L in Power BI — Select Distinct.md
note_type: pattern
tags: [power-bi, pattern, kpi-card, trend-chart, executive-dashboard, ytd]
---

# P&L Executive Sidebar

A sidebar of KPI cards and a trend chart placed beside the P&L Matrix gives stakeholders an immediate high-level overview before they explore the line-by-line statement.

## KPI Cards to Include

| Card | Metric | Format |
|---|---|---|
| **Total YTD Revenue** | Top-line revenue | Currency |
| **Total YTD Gross Profit** | Revenue minus direct costs | Currency |
| **YTD Operating Profit** | Value + percentage | Currency + % |
| **Net Profit** | Final bottom-line | Currency |

## Monthly Performance Trend

A **combined column and line chart** overlaid on the same canvas:
- **Columns**: Monthly Revenue
- **Line**: Monthly Operating Profit

This visual maps financial momentum month-over-month, making it immediately visible whether profitability is tracking with or diverging from revenue trends.

## Placement

Position the sidebar above or beside the P&L Matrix — do not let it crowd the main statement. The sidebar is context; the Matrix is the report.

## Measures Used

See [[ytd-kpi-measures-pl]] for the underlying DAX measures.

## Related

- [[ytd-kpi-measures-pl]] — `function`
- [[executive-pl-statement-structure]] — `atomic`
- [[pl-styling]] — `pattern`
