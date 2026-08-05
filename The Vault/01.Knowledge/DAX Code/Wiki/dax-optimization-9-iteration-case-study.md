---
created: 2026-07-30
updated: 2026-08-02
source: "dax4humans_ch15_optimize.txt"
note_type: pattern
tags: [optimization, performance, case-study, filter, switch]
---

# DAX Optimization — 9-Iteration Case Study

A step-by-step optimization of a slow measure, reducing query time from ~10 minutes to ~6 seconds — a 99% improvement.

## Starting Problem

A measure counting transactions that fall within hourly time buckets took over **581,894 ms (9m 42s)** to render.

## The Journey — 9 Iterations

### v1: Original (581,894 ms) — nested IF statements + dependent measures

```dax
No. of Orders =
  VAR __StartDate = VALUE(SELECTEDVALUE('Tracking_History'[Start Date]))
  VAR __EndDate   = VALUE(SELECTEDVALUE('Tracking_History'[End Date]))
  VAR __MinDate   = VALUE(MIN('DateTimeTable'[Date]))
  VAR __MaxDate   = VALUE(MAX('DateTimeTable'[Date]))
  VAR __Result    = IF(AND(__StartDate > __MinDate, __EndDate < __MaxDate), 1,
                   IF(AND(AND(__StartDate > __MinDate, __EndDate > __MaxDate),
                      __MaxDate > __StartDate), 1,
                   IF(AND(AND(__StartDate < __MinDate, __EndDate > __MinDate), 1,
                   IF(AND(__StartDate < __MaxDate, __EndDate > __MaxDate), 1, BLANK()))))
  RETURN __Result

Total Orders = SUMX('Tracking_History', [No. of Orders])
```

### v2: SWITCH(TRUE(), …) replaces nested IF — **58,175 ms** (90% faster)
```dax
No. of Orders 2 =
  VAR __Result = SWITCH(TRUE(),
    AND(__StartDate > __MinDate, __EndDate < __MaxDate), 1,
    AND(AND(__StartDate > __MinDate, __EndDate > __MaxDate), __MaxDate > __StartDate), 1,
    AND(AND(__StartDate < __MinDate, __EndDate > __MinDate), 1,
    AND(__StartDate < __MaxDate, __EndDate > __MaxDate), 1,
    BLANK())
  )
  RETURN __Result
```

### v3: Reorder conditions — most-eliminated-first — **27,424 ms** (52% faster)

Move the most-selective condition (rows outside the bucket entirely) first to eliminate the most rows early.

### v4: Consolidate into single measure — **25,000 ms** (7% faster)
Avoid dependent measures (measure branching). Put all logic in one measure.

### v5: FILTER early, before SWITCH — **16,000 ms** (36% faster)
```dax
VAR __Table = ADDCOLUMNS(
  FILTER('Tracking_History',
    OR('Tracking_History'[Start Date] <= __MaxDate,
       'Tracking_History'[End Date] > __MinDate)
  ),
  "__No", SWITCH(...)
)
```

### v6: Remove unnecessary VALUE() calls — **14,000 ms** (12% faster)
Direct date comparisons without VALUE() conversion.

### v7: Nested FILTER instead of SWITCH — **10,000 ms** (28% faster)
```dax
COUNTROWS(
  FILTER(FILTER(FILTER('Tracking_History',
    OR([Start Date] > __MinDate, [End Date] > __MaxDate)),
    __MaxDate > [Start Date]),
    OR([Start Date] <= __MinDate, [End Date] > __MaxDate)
  )
)
```

### v8: Simplify to bare minimum — **6,000 ms** (40% faster)
```dax
VAR __Date = MIN('DateTimeTable'[Date])
VAR __Result = COUNTROWS(
  FILTER('Tracking_History',
    'Tracking_History'[Start Date] <= __Date && 'Tracking_History'[End Date] > __Date
  )
)
```

**Total improvement: ~99% — from 9m 42s to 6s**

## Optimization Principles Summary

1. **Use SWITCH(TRUE(), …) instead of nested IF**: cleaner and faster
2. **Order conditions by selectivity**: eliminate the most rows first
3. **Consolidate into a single measure**: avoid measure branching overhead
4. **FILTER early and often**: the most powerful optimization function in DAX
5. **Remove unnecessary functions**: especially `VALUE()` and `VALUES()` in iterator contexts
6. **Nested FILTER outperforms SWITCH**: for row-by-row filtering tasks
7. **Simplify relentlessly**: the optimal version is usually the simplest version

## Related

- [[dax-optimization-tools-reference]] — tools for measuring performance
- [[storage-engine-vs-formula-engine-in-dax]] — understanding where time is spent
- [[SWITCH]] — SWITCH(TRUE()) pattern reference
