---
created: 2026-08-01
updated: 2026-08-02
source: "The 5 DAX Patterns Senior Analysts Use (and How to Validate Them in Your Model).md"
note_type: atomic
tags: [dax, defensive, error-handling, divide, blank, var, data-quality, intermediate]
---

# Defensive DAX: Explicit Error Handling

Never trust your data, your users, or your future self. Every division, iterator, and calculated result needs explicit handling.

## Rule 1: Always Use DIVIDE, Never "/"

```c
-- Never this
Margin = [Profit] / [Revenue]

-- Always this
Margin = DIVIDE([Profit], [Revenue], BLANK())
```

`DIVIDE` handles zero denominator gracefully. `/` produces infinity or error.

## Rule 2: BLANK() vs Zero — Know the Difference

```c
-- Zero: something happened and result is zero
-- BLANK(): no data exists

-- This is why BLANK() matters in visuals
VAR Visits = SUM(Sales[Visits])
VAR Conversions = SUM(Sales[Conversions])
VAR Result =
    IF(
        Visits > 0,
        DIVIDE(Conversions, Visits, 0),
        BLANK()  -- no visits = no data = BLANK
    )
RETURN Result
```

## Rule 3: Capture Inputs as Variables

```c
-- WRONG: calculates [Base Metric] three times
Result =
IF([Base Metric] > 0,
    [Base Metric] * 1.1,
    [Base Metric]
)

-- RIGHT: calculates once, validates once
Result =
VAR Base = [Base Metric]
RETURN
    IF(Base > 0, Base * 1.1, Base)
```

## Rule 4: Full Defensive Pattern

```c
Safe Conversion Rate =
-- Step 1: Capture inputs as variables
VAR Visits = SUM(Sales[Visits])
VAR Conversions = SUM(Sales[Conversions])

-- Step 2: Validate data quality assumptions
VAR HasData = NOT ISBLANK(Visits) && NOT ISBLANK(Conversions)
VAR IsValidData = Visits >= Conversions  -- sanity check

-- Step 3: Calculate with explicit error handling
VAR Result =
    SWITCH(
        TRUE(),
        NOT HasData, BLANK(),
        NOT IsValidData, ERROR("Data quality issue: Conversions > Visits"),
        Visits = 0, BLANK(),
        DIVIDE(Conversions, Visits, 0)
    )

RETURN Result
```

## Rule 5: Data Quality Checks with SWITCH

```c
Inventory Turnover =
VAR COGS = [Cost of Goods Sold]
VAR AvgInventory = [Average Inventory Value]
VAR DataQualityFlag =
    SWITCH(
        TRUE(),
        ISBLANK(COGS), "Missing COGS data",
        ISBLANK(AvgInventory), "Missing inventory data",
        AvgInventory <= 0, "Invalid inventory value",
        "OK"
    )
RETURN
    IF(
        DataQualityFlag = "OK",
        DIVIDE(COGS, AvgInventory, 0),
        ERROR("Inventory Turnover calculation failed: " & DataQualityFlag)
    )
```

`ERROR()` with a message won't break the visual — it shows your custom error text.

## Validation Test: The Four Edge Cases

For every measure with division, test with these filters one at a time:

1. Filter returns zero rows
2. Denominator = 0, numerator ≠ 0
3. Numerator = 0, denominator ≠ 0
4. Both numerator and denominator = 0

Handle all four gracefully: BLANK(), 0, or a readable error message.

## Validation Test: The NULL Cascade Test

```c
Test Measure =
VAR BaseValue = [Your Base Measure]
VAR Derived = BaseValue * 1.1
RETURN Derived
```

If `[Base Measure]` returns BLANK, does `Derived` propagate BLANK or show 0?

Senior pattern: explicit BLANK handling at every level:
```c
Derived Measure =
VAR Base = [Base Measure]
RETURN
    IF(NOT ISBLANK(Base), Base * 1.1, BLANK())
```

## Related

- [[measure-branching-naming-conventions]] — defensive patterns within branching hierarchy
- [[context-transition-architecture]] — BLANK() handling when context yields no data
- [[performance-first-measure-design]] — VAR for performance alongside defensive coding
