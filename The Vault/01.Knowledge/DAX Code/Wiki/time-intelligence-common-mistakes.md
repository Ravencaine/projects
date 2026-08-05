---
created: 2026-08-01
updated: 2026-08-02
source: "Master Power BI Introduction to DAX - The Complete Guide.md"
note_type: atomic
tags: [dax, time-intelligence, gotcha, beginner, common-mistakes]
---

# Time Intelligence: Common Mistakes

Time intelligence is powerful but has three sharp edges that catch most beginners.

## Mistake 1: Using a Fact Table Date Column Instead of a Date Table

```dax
// ❌ This errors
Revenue YTD = TOTALYTD([Total Revenue], Orders[OrderDate])
```

TOTALYTD requires a dedicated Date dimension table marked as such. It won't work with a date column in the fact table.

**Fix:** Create a proper Date table with CALENDAR, mark it as a date table, create a relationship to Orders[OrderDate], then use Date[Date].

## Mistake 2: Multiple Active Relationships to the Date Table

When Orders has both OrderDate and ShipDate connected to Date[Date], only one can be active. Time intelligence functions use the active relationship.

```dax
// ❌ Uses the active relationship (OrderDate), ignores ShipDate
Revenue YTD = TOTALYTD([Total Revenue], Date[Date])

// ✅ Explicitly uses the ShipDate relationship
Revenue YTD Ship Date =
CALCULATE(
    TOTALYTD([Total Revenue], Date[Date]),
    USERELATIONSHIP(Orders[ShipDate], Date[Date])
)
```

USERELATIONSHIP activates an inactive relationship for a single calculation.

## Mistake 3: Showing -100% Growth for New Products

```dax
// ❌ If PY has no data, this shows -100% (not helpful)
Revenue Growth % =
    ([Total Revenue] - [Revenue PY]) / [Revenue PY]
```

If a product launched this year, PY is BLANK. The math gives -100%, which is misleading.

**Fix:** Use DIVIDE's third parameter or IF to suppress the error:

```dax
Revenue Growth % =
VAR CurrentRevenue = [Total Revenue]
VAR PreviousRevenue = [Revenue PY]
RETURN
    IF(
        ISBLANK(PreviousRevenue),
        BLANK(),    // Don't show anything if no PY data
        DIVIDE(CurrentRevenue - PreviousRevenue, PreviousRevenue, 0)
    )
```

Or more concisely:

```dax
Revenue Growth % =
DIVIDE(
    [Total Revenue] - [Revenue PY],
    [Revenue PY],
    BLANK()     // Return BLANK instead of error when PY is missing
)
```

## Related

- [[time-intelligence-functions]] — the functions this is built on
- [[calculate-context-modifier]] — CALCULATE underlies all time intelligence
- [[logical-functions-switc]] — SWITCH TRUE pattern for conditional growth rates
