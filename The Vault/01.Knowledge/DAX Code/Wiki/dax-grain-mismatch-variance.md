---
created: 2026-08-01
updated: 2026-08-02
source: "When a Simple Variance Measure Breaks Power BI Lessons from Cross-Fact DAX.md"
note_type: atomic
tags: [dax, grain, variance, cross-fact, removefilters, context]
---

# DAX Grain Mismatch — Variance Measure Breakdown

## The Problem

Two measures evaluated at different grains:

```
Payroll Context:  Vehicle + Job + Employee + Type
Equipment Context: Vehicle + Job
```

Power BI must reconcile these contexts repeatedly → "visual has exceeded available resources" error.

## The Fix: Equalize Grain with REMOVEFILTERS

```c
Vehicle Labour Hours VJ =
CALCULATE(
    SUM(fctPayrollVehicles[TotalHours]),
    REMOVEFILTERS(dimEmpMaster[Type]),
    REMOVEFILTERS(fctPayrollVehicles[Employee_Name])
)
```

Result: Both measures now operate at **Vehicle + Job** grain.

## Variance Measure

```c
Vehicle Hours True-up =
IF(
    [Vehicle Labour Hours VJ] > [Vehicle Eq Hours],
    [Vehicle Labour Hours VJ] - [Vehicle Eq Hours],
    0
)
```

## Rule: Variance Measures Must Compare Same Grain

If two measures operate at different levels of detail, Power BI has to reconcile contexts repeatedly — causing incorrect results or resource errors.

Always ask: **"What level of detail does this measure actually represent?"**

## Grain Identification Checklist

| Scenario | Grain |
|----------|-------|
| Payroll hours per vehicle | Vehicle |
| Payroll hours per job | Vehicle + Job |
| Payroll hours per employee | Vehicle + Job + Employee |
| Equipment hours per asset | Equipment Serial Code |

## REMOVEFILTERS Alternatives

```c
-- REMOVEFILTERS (DAX 2020+)
REMOVEFILTERS(dimEmpMaster[Type])

-- ALL (legacy equivalent)
ALL(dimEmpMaster[Type])

-- KEEPFILTERS variant (preserves outer filter context)
CALCULATE([Measure], REMOVEFILTERS(...))
```
