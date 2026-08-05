---
created: 2026-08-02
updated: 2026-08-05
source: How to Build Dynamic KPI Cards in Power BI Using Only Core Visuals
note_type: function
tags: [dax, measure, aggregation, overtime]
---

# OT Hours

The total sum of overtime hours from the Scheduling Data fact table.

## Signature

```dax
OT Hours = SUM('Scheduling Data'[OvertimeHours])
```

## Parameters

None — uses an implicit SUM over the `OvertimeHours` column.

## Returns

A scalar number — the total overtime hours across all rows in the current filter context.

## Examples

```dax
-- All overtime (no filter)
OT Hours

-- Overtime for a specific unit
CALCULATE(
    [OT Hours],
    Units[Unit] = "ICU"
)

-- Overtime in last 7 days
CALCULATE(
    [OT Hours],
    FILTER(
        'Scheduling Data',
        'Scheduling Data'[Date] > [Max Date - 7] &&
        'Scheduling Data'[Date] <= [Max Date]
    )
)
```

## Notes

This is a base measure. It should never be displayed directly — always divide or count it through other measures (e.g., `OT Hours per FTE`). Keeping aggregation as a separate base measure enables the branching pattern where dependent measures can reuse it with different CALCULATE contexts.

## Related

- [[Employee-Count]]
- [[OT-Hours-per-FTE]]
- [[OT-Hours-This-Week]]
