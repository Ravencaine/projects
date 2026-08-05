---
created: 2026-08-02
updated: 2026-08-02
source: AI in Excel for Project Management Smarter Gantt Charts and Trackers.md
note_type: pattern
tags: [excel, dashboard, pattern, dynamic, reporting]
---

# Dynamic Status Dashboard

A formula-driven summary layer that automatically updates when task data changes — eliminating manual report updates and stale charts.

## Purpose

Provides a real-time executive view of project health by pulling live metrics from the task tracker via COUNTIF, COUNTIFS, SUMIFS, and XLOOKUP. The dashboard reads from Excel Tables so it reflects changes immediately without any manual refresh.

## Components

- **Data tab** containing an Excel Table with task records
- **Dashboard tab** with KPI tiles fed by summary formulas
- **Conditional formatting** on the dashboard to flag overdue or at-risk metrics
- **XLOOKUP** for dynamic label resolution (e.g., task owner name from an ID)

## Structure

```excel
' Dashboard KPIs (each references the [Data] Excel Table)
=COUNTIF(TableTasks[Status], "Completed")       ' Total completed
=COUNTIF(TableTasks[Status], "In Progress")      ' Total active
=COUNTIFS(TableTasks[Status], "In Progress",
          TableTasks[Due Date], "<"&TODAY())     ' Overdue active
=SUMIFS(TableTasks[Budget], TableTasks[Status], "Completed")  ' Spent
=SUMIFS(TableTasks[Budget], TableTasks[Status], "<>Completed") ' Remaining

' Dynamic owner lookup
=XLOOKUP(A2, TableRACI[TaskID], TableRACI[Owner], "Unassigned")
```

## Example

A project dashboard with four tiles:
- **% Complete:** `=COUNTIF(TableTasks[Status],"Completed") / ROWS(TableTasks)`
- **Overdue Tasks:** `=COUNTIFS(TableTasks[Status],"In Progress", TableTasks[Due Date],"<"&TODAY())`
- **Budget Spent:** `=SUMIFS(TableTasks[Cost], TableTasks[Status],"Completed")`
- **Open Risks:** `=COUNTIF(TableRisks[Status],"Open")`

Each tile updates the moment a task status or cost cell is edited.

## Variations

- **Traffic-light dashboard**: use conditional formatting on KPI cells — green/yellow/red based on thresholds
- **Owner breakdown**: use COUNTIFS grouped by Owner to show task load per team member
- **Weekly burndown**: track completed vs remaining task counts over time (requires a historical log or manual weekly snapshot)

## Notes

The critical enabler is **Excel Tables** (Insert → Table). Charts and formulas that reference a Table range automatically expand as new rows are added. Non-Table ranges require manual range updates and are prone to stale references.

## Related

- [[four-layer-project-workbook]] — `pattern`
- [[live-formula-gantt-chart]] — `pattern`
- [[countif-project-progress]] — `function`
- [[sumifs-conditional-project-sums]] — `function`
- [[countifs-multi-criterion-project-tasks]] — `function`
- [[xlookup-modern-lookup]] — `function`
