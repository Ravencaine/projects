---
created: 2026-08-01
updated: 2026-08-02
source: "When a Simple Variance Measure Breaks Power BI Lessons from Cross-Fact DAX.md"
note_type: atomic
tags: [dax, selectedvalue, totals, iterator, sumx, blank, grand-total]
---

# SELECTEDVALUE in Totals — Why It Breaks and How to Fix

## Why SELECTEDVALUE Works at Row Level

At row level (one Vehicle + one Job):
```c
SELECTEDVALUE(Vehicle)     → "V1"
SELECTEDVALUE(Job_Number) → "J1"
```

Exactly one value exists → returns that value ✓

## Why SELECTEDVALUE Breaks at Grand Total

At Grand Total (multiple Vehicle + Job pairs):
```
V1  J1
V1  J2
V2  J1
V3  J4
```

```c
SELECTEDVALUE(Vehicle) = BLANK   ← multiple values exist
SELECTEDVALUE(Job)     = BLANK   ← multiple values exist
```

`BLANK` propagates through the calculation → wrong totals or BLANK results.

## Fix: Use Iterators to Stabilize Totals

```c
Vehicle Hours True-up =
SUMX(
    SUMMARIZE(
        fctPayrollVehicles,
        fctPayrollVehicles[Vehicle],
        fctPayrollVehicles[Job_Number]
    ),
    -- row-level calculation per Vehicle+Job pair
    VAR _Payroll = [Vehicle Labour Hours VJ]
    VAR _Equip   = [Vehicle Eq Hours]
    RETURN
        MAX(_Payroll - _Equip, 0)
)
```

SUMMARIZE creates a virtual table of distinct pairs:
```
(V1, J1)
(V1, J2)
(V2, J1)
(V3, J4)
```

SUMX iterates row-by-row, then sums — totals are always correct.

## The Pattern

```c
SUMX(
    DISTINCT business keys,
    row-level calculation
)
```

- `DISTINCT(...)` or `SUMMARIZE(...)` rebuilds the correct grain
- Iterator evaluates pair-by-pair (same grain at every step)
- SUMX sums the results

## SELECTEDVALUE Guard Pattern

```c
VAR _Vehicle = SELECTEDVALUE(fctPayrollVehicles[Vehicle])
RETURN
    IF(
        ISBLANK(_Vehicle),
        [Fallback at grand-total level],
        [Row-level calculation using _Vehicle]
    )
```

Use ISBLANK(_Vehicle) to detect totals vs row context and branch accordingly.

## When to Use Variables

```c
VAR _Vehicle = SELECTEDVALUE(fctPayrollVehicles[Vehicle])
VAR _Job     = SELECTEDVALUE(fctPayrollVehicles[Job_Number])
```

- Ensures both sides of a calculation use the same context
- Prevents expensive expressions from being recalculated repeatedly
- Improves readability and performance
