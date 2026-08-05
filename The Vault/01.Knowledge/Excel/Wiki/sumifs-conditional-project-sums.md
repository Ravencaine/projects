---
created: 2026-08-02
updated: 2026-08-02
source: AI in Excel for Project Management Smarter Gantt Charts and Trackers.md
note_type: function
tags: [excel, function, summing, conditional, project-management]
---

# SUMIFS — Conditional Sum Across Multiple Criteria

Sums values from a range that satisfy multiple conditions applied to separate ranges.

## Signature

```
=SUMIFS(sum_range, criteria_range1, criteria1, [criteria_range2, criteria2], ...)
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `sum_range` | Range | The range of numeric values to sum |
| `criteria_range1` | Range | The first range to evaluate |
| `criteria1` | String/Number | Condition for `criteria_range1` |
| `criteria_range2` | Range | Optional — second range to evaluate |
| `criteria2` | String/Number | Optional — condition for `criteria_range2` |

## Returns

A single numeric value — the sum of `sum_range` cells that satisfy all criteria.

## Examples

```excel
=SUMIFS(C2:C50, E2:E50, "Completed")              ' Sum budget of completed tasks
=SUMIFS(C2:C50, E2:E50, "In Progress", D2:D50, "High")  ' Sum budget of high-priority active tasks
=SUMIFS(C2:C50, D2:D50, ">"&TODAY()-30)          ' Sum spending in last 30 days
```

Use case: budget tracking on a project dashboard. `C` column = budgeted cost, `D` column = due date, `E` column = status.

## Notes

- All `criteria_range` arguments must have the same dimensions as `sum_range`.
- Criteria are applied with AND logic — a cell is summed only if all conditions are met.
- Use double quotes around text criteria; use `"<"&DATE(...)` syntax for date comparisons.
- COUNTIFS has the same signature structure but counts instead of sums.

## Related

- [[countif-project-progress]] — `function`
- [[countifs-multi-criterion-project-tasks]] — `function`
- [[dynamic-status-dashboard]] — `pattern`
- [[xlookup-modern-lookup]] — `function`
