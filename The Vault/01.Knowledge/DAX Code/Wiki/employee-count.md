---
created: 2026-08-02
source: How to Build Dynamic KPI Cards in Power BI Using Only Core Visuals
note_type: function
tags: [dax, measure, count, distinct, employee]
---

# Employee Count

The count of distinct employee IDs in the current filter context.

## Signature

```dax
Employee Count = DISTINCTCOUNT('Scheduling Data'[EmployeeID])
```

## Parameters

None — uses an implicit DISTINCTCOUNT over the `EmployeeID` column.

## Returns

An integer — the number of unique employees. Returns BLANK if no data.

## Examples

```dax
-- Total employee count
[Employee Count]

-- Employee count for Night shift only
CALCULATE(
    [Employee Count],
    'Scheduling Data'[Shift] = "Night"
)
```

## Notes

`DISTINCTCOUNT` counts each unique EmployeeID once regardless of how many rows that employee has. This makes it suitable as the denominator for per-capita metrics like OT Hours per FTE. For a per-employee aggregation (e.g., "count employees over threshold"), use `COUNTROWS(FILTER(...))` on the grouped employee set instead — DISTINCTCOUNT inside that pattern would double-count.

## Related

- [[OT-Hours]]
- [[OT-Hours-per-FTE]]
