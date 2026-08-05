---
created: 2026-08-01
updated: 2026-08-02
source: "The DAX concepts that actually save you time in Power BI.md"
note_type: atomic
tags: [dax, var, return, performance, readability, fundamentals, beginner]
---

# VAR: The Habit That Saves Hours

VAR lets you calculate something once, store it under a name, and reuse that name throughout a measure. Fixes both performance and readability simultaneously.

## The Pattern

```c
// Without VAR: same sub-calculation repeated 3 times
YoY Growth % =
DIVIDE(
    [Total Sales] - CALCULATE([Total Sales], SAMEPERIODLASTYEAR('Calendar'[Date])),
    CALCULATE([Total Sales], SAMEPERIODLASTYEAR('Calendar'[Date]))
)

// With VAR: calculate once, reuse cleanly
YoY Growth % =
VAR CurrentSales = [Total Sales]
VAR PriorSales = CALCULATE([Total Sales], SAMEPERIODLASTYEAR('Calendar'[Date]))
RETURN
    DIVIDE(CurrentSales - PriorSales, PriorSales)
```

## Why VAR Wins

**Readability:** Variables read like a sentence. Nested expressions read like a puzzle.

```c
// Self-documenting: the intent is clear
VAR TotalRevenue = [Total Sales]
VAR PriorYear = CALCULATE([Total Sales], SAMEPERIODLASTYEAR('Calendar'[Date]))
VAR Result = DIVIDE(TotalRevenue - PriorYear, PriorYear)
RETURN IF(NOT ISBLANK(Result), Result, BLANK())
```

**Performance:** Each expression inside a VAR is calculated **once**, not per reuse. Significant for repeated SUM, CALCULATE, SAMEPERIODLASTYEAR calls.

```c
// Without VAR: [Total Sales] evaluated 3 times
Bad Measure =
    IF([Total Sales] > 0, [Total Sales] * 1.1, [Total Sales] * 0.9)

// With VAR: [Total Sales] evaluated once
Good Measure =
VAR Sales = [Total Sales]
RETURN
    IF(Sales > 0, Sales * 1.1, Sales * 0.9)
```

## Multi-VAR Pattern

```c
Revenue YoY % =
VAR Current = [Total Revenue]
VAR Prior = CALCULATE([Total Revenue], SAMEPERIODLASTYEAR('Calendar'[Date]))
VAR Diff = Current - Prior
VAR Result = DIVIDE(Diff, Prior, 0)
RETURN
    IF(NOT ISBLANK(Prior), Result, BLANK())
```

## Scope

VAR variables are **measure-local**: they cannot be shared between measures. Each measure defines its own VARs.

For cross-measure sharing, use [[measure-branching-pattern]] — build a base measure and reference it.

## Related

- [[var-syntax-and-pattern]] — VAR/RETURN syntax (from Tejwani)
- [[var-performance-benefit]] — performance details (from Tejwani)
- [[dax-common-mistakes-beginners]] — forgetting VAR = repeated recalculation
