---
created: 2026-08-02
source: How to Build Dynamic KPI Cards in Power BI Using Only Core Visuals
note_type: function
tags: [dax, measure, ratio, overtime, fte]
---

# OT Hours per FTE

Overtime hours divided by the count of distinct employees — a per-capita overtime metric.

## Signature

```dax
OT Hours per FTE = DIVIDE([OT Hours], [Employee Count])
```

## Parameters

None — references two other measures.

## Returns

A decimal number — overtime hours per full-time equivalent employee.

## Examples

```dax
-- Base ratio (all data in context)
[OT Hours per FTE]

-- For the last 7 days (rolling window)
VAR _MaxDate = [Max Date]
VAR _MinDate = [Max Date - 7]
RETURN
    CALCULATE(
        [OT Hours per FTE],
        FILTER(
            'Scheduling Data',
            'Scheduling Data'[Date] > _MinDate &&
            'Scheduling Data'[Date] <= _MaxDate
        )
    )
```

## Notes

`DIVIDE` is used instead of the `/` operator — it handles division by zero (BLANK if denominator is 0 or blank) safely without requiring explicit IFERROR wrapping. This is the base measure from which `This Week` and `Last Week` variants branch via CALCULATE.

## Related

- [[OT-Hours]]
- [[Employee-Count]]
- [[DIVIDE]]
- [[OT-Hours-per-FTE-This-Week]]
- [[OT-Hours-per-FTE-Last-Week]]
- [[OT-Hours-per-FTE-Variance]]
- [[OT-Hours-per-FTE-Variance-Pct]]
