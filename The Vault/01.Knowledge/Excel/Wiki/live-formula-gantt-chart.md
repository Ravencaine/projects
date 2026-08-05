---
created: 2026-08-02
updated: 2026-08-02
source: AI in Excel for Project Management Smarter Gantt Charts and Trackers.md
note_type: pattern
tags: [excel, gantt, timeline, pattern, dynamic]
---

# Live Formula Gantt Chart

A Gantt chart built on Excel Tables and formula-driven conditional formatting that updates automatically when task dates or status changes — replacing static chart objects that require manual surgery.

## Purpose

Keeps the timeline view synchronized with the task tracker without rebuilding the chart. Traditional Excel Gantt charts become stale the moment a task date shifts; this pattern maintains a live view through formulas and conditional formatting rules.

## Components

- Excel Table as the task data source
- Date-based formula columns (start offset, duration, days remaining)
- Stacked bar chart OR conditional formatting on a date-grid layout
- Conditional formatting rules for overdue highlighting

## Structure

### Variant A — Stacked Bar Chart

```excel
' Helper columns in the task table:
StartOffset = [Start Date] - MIN([Start Date])    ' Days from earliest task start
Duration    = [Due Date] - [Start Date] + 1        ' Calendar days inclusive

' Chart:
' - Series 1: StartOffset (invisible, no fill) — shifts the bar right
' - Series 2: Duration (visible fill) — the visible bar
```

### Variant B — Conditional Formatting on Date Grid

```excel
' For each task row, place a formula in each date column of the grid:
=IF(AND(col_date >= [Start Date], col_date <= [Due Date]), "█", "")

' Apply conditional formatting: colour the cell based on status
' Green  = Completed  (fill based on Status column)
' Blue   = In Progress
' Grey   = Not Started
' Red    = Overdue   (Due Date < TODAY() AND Status <> "Completed")
```

## Example

AI-assisted workflow (from Excelmatic):
1. Build a basic task list with Task Name, Start Date, Due Date, Status
2. Ask Copilot or a general AI tool to generate the Gantt formula structure
3. Apply conditional formatting rules to colour bars by status
4. Result: a timeline that reflects task updates immediately

## Variations

- **Milestone markers**: add a column flagging tasks where `Due Date = Start Date`, render as diamonds
- **Critical path highlight**: use a formula to flag tasks on the critical path and apply a distinct border
- **Resource loading view**: transpose the grid and group by Owner instead of task sequence

## Notes

AI-based charting tools (Excelmatic, built-in AI chart suggestions) can accelerate the initial build but are not required. The pattern works with plain formulas and conditional formatting — available in all Excel versions that support Tables.

## Related

- [[four-layer-project-workbook]] — `pattern`
- [[dynamic-status-dashboard]] — `pattern`
- [[ai-assisted-project-estimation]] — `pattern`
