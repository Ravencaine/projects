---
created: 2026-08-02
updated: 2026-08-02
source: AI in Excel for Project Management Smarter Gantt Charts and Trackers.md
note_type: function
tags: [excel, function, counting, project-management]
---

# COUNTIF — Count Cells Matching a Criterion

Counts the number of cells within a range that satisfy a single condition.

## Signature

```
=COUNTIF(range, criteria)
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `range` | Range | The range of cells to evaluate |
| `criteria` | String/Number | The condition to match (value, text, comparison, or wildcard) |

## Returns

A single integer — the count of cells in `range` that meet `criteria`.

## Examples

```excel
=COUNTIF(E2:E50, "Completed")        ' Count completed tasks
=COUNTIF(E2:E50, "In Progress")      ' Count active tasks
=COUNTIF(E2:E50, "Not Started")     ' Count backlog items
=COUNTIF(B2:B50, ">="&TODAY())      ' Count tasks due today or later
```

Typical project tracker use: `E2:E50` holds task status values. Use COUNTIF to populate summary KPIs on a dashboard tab.

## Notes

- `criteria` is not case-sensitive.
- Wildcard characters `?` (single char) and `*` (any chars) work in text criteria when used inside quotes.
- For multiple criteria across different ranges, use `COUNTIFS` instead.
- If no cells match, COUNTIF returns `0` — not an error.

## Related

- [[countifs-multi-criterion-project-tasks]] — `function`
- [[sumifs-conditional-project-sums]] — `function`
- [[dynamic-status-dashboard]] — `pattern`
- [[xlookup-modern-lookup]] — `function`
