---
created: 2026-08-01
updated: 2026-08-02
source: "When a Simple Variance Measure Breaks Power BI Lessons from Cross-Fact DAX.md"
note_type: atomic
tags: [dax, debugging, checklist, grain, selectedvalue, removefilters, sumx]
---

# DAX Debugging Checklist — Variance / Cross-Fact Measures

> "Most DAX problems are not syntax problems. They are grain problems."

## 1️⃣ Check the Grain First

Ask: **"What level of detail does this measure actually represent?"**

If two measures operate at different grains, variance calculations will break.

Grain questions to answer explicitly:
- Vehicle only?
- Vehicle + Job?
- Vehicle + Job + Employee?

## 2️⃣ Inspect the Filter Context

Check what filters are actually active:

```c
-- Use a test measure to see current context
_debug context =
CONCATENATEX(
    ALLSELECTED(),
    [ColumnName] & ": " & FORMAT([ColumnName], "General"),
    " | "
)
```

Sometimes unnecessary filters cause the problem:
```c
REMOVEFILTERS(dimEmpMaster[Type])
```

## 3️⃣ Verify Key Matching Between Tables

Cross-system comparisons fail because of subtle key mismatches:

```c
-- Always normalize before joining
TRIM(fctPayrollVehicles[Job_Number])
=
TRIM('LN Eq Rev'[Project])
```

Look for: leading/trailing spaces, different data types, hidden characters, inconsistent casing.

## 4️⃣ Understand When SELECTEDVALUE() Works

`SELECTEDVALUE()` returns BLANK when multiple values exist — common at totals.

Use ISBLANK to branch:
```c
IF(
    ISBLANK(SELECTEDVALUE(Column)),
    [Total-level fallback],
    [Row-level logic]
)
```

## 5️⃣ Use Iterators When Totals Break

When totals fail, rebuild at the correct grain:
```c
SUMX(
    SUMMARIZE(factTable, Col1, Col2),
    row-level calculation
)
```

## 6️⃣ Use Variables to Stabilize Complex Measures

```c
VAR _Vehicle = SELECTEDVALUE(fctPayrollVehicles[Vehicle])
VAR _Job     = SELECTEDVALUE(fctPayrollVehicles[Job_Number])
-- Both evaluated under the same context
-- Prevents repeated recalculation
```

## The Variance Measure Template

```c
Measure =
VAR _Grain =
    SUMMARIZE(
        factTable,
        factTable[Key1],
        factTable[Key2]
    )
RETURN
    SUMX(
        _Grain,
        VAR _Payroll = [Payroll Measure]
        VAR _Equip   = [Equipment Measure]
        RETURN
            MAX(_Payroll - _Equip, 0)
    )
```

## Symptoms → Root Causes

| Symptom | Likely Cause |
|---------|-------------|
| "Visual exceeded resources" | Grain mismatch (context reconciliation) |
| BLANK totals | SELECTEDVALUE at grand total |
| Wrong totals | Wrong grain or missing iterator |
| Slowly rendering | Over-complex CALCULATE with many context transitions |
| Mysteriously wrong numbers | Key mismatch (leading spaces, type mismatch) |
