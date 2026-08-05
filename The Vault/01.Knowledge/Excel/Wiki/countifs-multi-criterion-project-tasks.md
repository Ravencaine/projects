---
created: 2026-08-02
updated: 2026-08-02
source: AI in Excel for Project Management Smarter Gantt Charts and Trackers.md
note_type: function
tags: [excel, function, counting, multi-criteria, project-management]
---

# COUNTIFS — Multi-Criterion Count

Counts cells that satisfy multiple conditions across different ranges. AND logic: all criteria must be true.

## Signature

```
=COUNTIFS(criteria_range1, criteria1, [criteria_range2, criteria2], ...)
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `criteria_range1` | Range | First range to evaluate |
| `criteria1` | String/Number | Condition for `criteria_range1` |
| `criteria_range2` | Range | Optional — second range to evaluate |
| `criteria2` | String/Number | Optional — condition for `criteria_range2` |

## Returns

An integer — the count of rows where all criteria are satisfied simultaneously.

## Examples

```excel
=COUNTIFS(E2:E50, "Completed", D2:D50, ">=1-Jan-2026")    ' Tasks done on time
=COUNTIFS(E2:E50, "In Progress", D2:D50, "<"&TODAY())    ' Overdue active tasks
=COUNTIFS(E2:E50, "In Progress", F2:F50, "High")         ' High-priority active tasks
=COUNTIFS(E2:E50, "<>Completed", D2:D50, "<"&TODAY())    ' All overdue tasks
```

Use on a project dashboard to show segmented task counts: by status and priority, by status and owner, or by status and deadline.

## Notes

- All ranges must have the same row dimensions; COUNTIFS does not broadcast mismatched ranges.
- Criteria are applied with AND logic — unlike SUMPRODUCT which supports OR with addition.
- Use `<>"Completed"` to count non-matching cells, including blanks.
- Works with date comparisons, number comparisons, and text wildcards.

## Related

- [[countif-project-progress]] — `function`
- [[sumifs-conditional-project-sums]] — `function`
- [[dynamic-status-dashboard]] — `pattern`
