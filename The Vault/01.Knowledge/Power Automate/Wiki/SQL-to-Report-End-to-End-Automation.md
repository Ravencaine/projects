---
created: 2026-08-10
updated: 2026-08-10
source: Build automatic process on Power Automate to reduce efforts of routine tasks
source_url: https://medium.com/@wedodo/build-automatic-process-on-power-automate-to-reduce-efforts-of-routine-tasks-e31a0306cf3c
note_type: pattern
tags: [power-automate, sql, excel, vb-script, pivot-table, outlook, automation, end-to-end]
---

# SQL-to-Report End-to-End Automation Pattern

Chain SQL query → Excel export → VBA pivot table → timestamped filename → Outlook delivery as a single automated flow.

## Flow Sequence

```
Variables (route, timestamp)
    → SQL: Run query → export result
    → Excel: Create headers, insert rows
    → VB Script: Build pivot table from data
    → File Rename: Append datetime to filename
    → Outlook: Send to stakeholder list
```

## Key Steps

### 1. Variables First

Define variables upfront (route paths, datetime formats) — same as declaring variables in code. Reference them throughout the flow instead of hardcoding.

### 2. SQL Connection

Use the **SQL Server** connector in Power Automate. Write and test the query in SSMS first; apply version control at the SQL layer.

### 3. Excel: Export + Header Insert

Export query results to an Excel file. Insert a header row via the Excel connector. The blue connectors represent objects (data, files) moving between steps — each carries a payload forward.

### 4. VB Script: Auto-Build Pivot Table

Invoke a VB script step to create a pivot table from the exported data automatically. This replaces manual pivot table construction for recurring reports.

### 5. Rename with DateTime

Use the datetime variables (set at the beginning) to stamp the filename automatically. Pattern: `{ReportName}_{YYYY-MM-DD}.xlsx`.

### 6. Outlook Send

Use the Outlook connector to compose and send: subject, body, CC/BCC, attachment. Optionally save as draft before sending.

## Design Principle

> Each step's output object carries the next step's required input. Variables set once at the start are referenced throughout — not hardcoded per step.

## Extending

Add conditional logic (flow control) to customise the report per stakeholder level (VP, district manager, sales rep) before sending.

## Related

- [[Power-Automate-Flow-Design-Principles]] — flow architecture guidance
- [[Email-Keyword-Conditional-Send]] — conditional email routing
