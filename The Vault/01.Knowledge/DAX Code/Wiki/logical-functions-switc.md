---
created: 2026-08-01
updated: 2026-08-02
source: "Master Power BI Introduction to DAX - The Complete Guide.md"
note_type: atomic
tags: [dax, logical-functions, beginner, if, switch, and, or, isblank, iferror, divide]
---

# Logical Functions: IF, SWITCH, and Conditionals

Business logic is rarely binary. Logical functions let DAX make decisions based on conditions.

## IF — The Basic Conditional

```dax
IF(<logical_test>, <value_if_true>, <value_if_false>)
```

```dax
Target Status =
IF(
    [Total Revenue] >= 150000,
    "Target Met ✓",
    "Below Target"
)
```

## Nested IF — Multiple Conditions

```dax
Order Category =
IF(
    [Total Revenue] > 1000, "Large",
    IF(
        [Total Revenue] > 500, "Medium",
        "Small"
    )
)
```

Evaluated top-down. First true condition wins.

## SWITCH — Cleaner Than Nested IF

When you have three or more conditions, SWITCH is easier to read:

```dax
Discount Rate =
SWITCH(
    Customers[CustomerSegment],
    "Enterprise", 0.15,
    "SMB",        0.10,
    "Startup",    0.05,
    0              // Default: no discount
)
```

Much cleaner than nested IFs.

## SWITCH TRUE — Pattern Matching

Use SWITCH with TRUE() as the first argument to test multiple conditions (like nested IFs):

```dax
Priority =
SWITCH(
    TRUE(),
    [Total Revenue] > 10000, "Critical",
    [Total Revenue] > 5000,  "High",
    [Total Revenue] > 1000,   "Medium",
    "Low"
)
```

Each condition is evaluated in order. First TRUE wins.

## AND / OR — Combining Conditions

**AND — all conditions must be true:**

```dax
High Value Enterprise =
IF(
    AND(
        Customers[CustomerSegment] = "Enterprise",
        [Total Revenue] > 50000
    ),
    "Yes",
    "No"
)
```

Can also write as `&&`: `Customers[CustomerSegment] = "Enterprise" && [Total Revenue] > 50000`

**OR — at least one condition must be true:**

```dax
Coastal Customer =
IF(
    OR(
        Customers[CustomerCity] = "New York",
        Customers[CustomerCity] = "Los Angeles",
        Customers[CustomerCity] = "Miami"
    ),
    "Coastal",
    "Inland"
)
```

Can also write as `|`: `Customers[CustomerCity] IN {"New York", "Los Angeles", "Miami"}`

## ISBLANK — Handling Missing Data

```dax
Average Deal Size =
IF(
    ISBLANK([Total Orders]),
    BLANK(),
    DIVIDE([Total Revenue], [Total Orders])
)
```

Check if a value is BLANK before dividing.

## IFERROR — Catching Errors

```dax
Market Share % =
IFERROR(
    [Our Revenue] / [Total Market Revenue],
    0
)
```

If the division fails, return 0 instead of an error.

## DIVIDE's Third Parameter — The Shortcut

Instead of wrapping every division in IFERROR, use DIVIDE's third parameter:

```dax
// Equivalent to IFERROR above
Market Share % = DIVIDE([Our Revenue], [Total Market Revenue], 0)
```

DIVIDE handles BLANK and zero in the denominator automatically. Always prefer DIVIDE over the `/` operator.

## Traffic Light KPI

```dax
Performance Indicator =
VAR PercentOfTarget = DIVIDE([Total Revenue], 150000, 0)
RETURN
    SWITCH(
        TRUE(),
        PercentOfTarget >= 1,   "🟢 Above Target",
        PercentOfTarget >= 0.9, "🟡 Near Target",
        "🔴 Below Target"
    )
```

## Related

- [[time-intelligence-common-mistakes]] — IF + ISBLANK pattern for growth rate error handling
- [[calculate-pattern-library]] — SWITCH for segment-based CALCULATE filters
- [[advanced-patterns-ranking-abc-pareto]] — SWITCH TRUE pattern for ABC analysis
