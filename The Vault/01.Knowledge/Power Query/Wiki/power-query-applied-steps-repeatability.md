---
created: 2026-08-01
updated: 2026-08-02
source: "Master Power BI Transforming Data with Power Query Editor.md"
note_type: atomic
tags: [power-bi, power-query, beginner, applied-steps, m-language, automation, repeatability]
---

# Power Query: Applied Steps and Repeatability

Applied Steps is what makes Power Query transformative — not just a cleaning tool, but an automated, repeatable data pipeline.

## The Core Benefit

Every transformation is recorded as a named step. These steps replay automatically when you refresh the data.

**Traditional approach (Excel):**
1. Receive new monthly sales file
2. Delete last month's columns
3. Paste new columns
4. Re-apply VLOOKUPs
5. Fix broken references
6. Recalculate totals
7. Update charts

**Power Query approach:**
1. Refresh data source
2. Done. Everything replays automatically.

The steps you applied last month apply to this month's data.

## What This Means for Monthly Reports

**Scenario:** Your monthly sales report receives a new file on the first of each month. The file format is slightly different each time (different number of header rows, a new column added).

With Applied Steps:
1. Build the transformation once
2. Each month: replace the source file
3. All steps replay
4. If a step fails (new column name changed), fix it once and the whole pipeline updates

## The Applied Steps Pane

```
Applied Steps:
1. Source                          ← connect to Excel file
2. Navigation                      ← select the sheet/table
3. Remove Top Rows                 ← skip header clutter
4. Use First Row as Headers
5. Changed Type                    ← set data types
6. Replace Errors                  ← handle N/A values
7. Added Custom Column             ← calculated field
8. Removed Columns                 ← drop unused columns
```

Each step can be:
- **Clicked**: preview the data at that stage
- **Renamed**: give descriptive names for clarity
- **Deleted**: remove a transformation (data reverts to that stage)
- **Reordered**: drag to change the sequence
- **Edited**: click the gear icon to change settings

## The M Formula Bar

Each step has M code behind it. View → Formula Bar to see it:

```m
= Table.ReplaceErrorValues(Source, {{"Amount", null}})
```

You can edit M directly for precise control. Most users never touch it — the UI covers 95% of cases.

## What Power Query Can't Do

It's NOT for:
- Complex statistical analysis (use DAX measures instead)
- Real-time data streaming (Power BI Service scheduled refresh handles scheduled updates)
- Creating visualisations (that's the main Power BI interface)
- Advanced machine learning (simple predictive functions available via AI Insights)

It IS for:
- Data preparation and shaping
- Connecting to virtually any data source
- Automating repetitive cleaning tasks
- Creating reusable transformation pipelines

## Related

- [[power-query-workflow-process]] — the workflow that generates these steps
- [[power-query-5-core-components]] — where Applied Steps live in the UI
