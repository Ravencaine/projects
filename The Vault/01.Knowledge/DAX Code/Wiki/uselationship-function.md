---
created: 2026-08-01
updated: 2026-08-02
source: "RELATIONSHIP in DAX - Unlocking Role - Playing Dimensions.md"
note_type: atomic
tags: [dax, uselationship, relationship, inactive, beginner]
---

# USERELATIONSHIP()

USERELATIONSHIP activates an existing **inactive** relationship between two tables — temporarily, within the expression that calls it.

## Syntax

```dax
CALCULATE (
    <expression>,
    USERELATIONSHIP ( <column1>, <column2> )
)
```

`column1` must be on the many side (fact table); `column2` must be on the one side (dimension table).

## What It Does and Doesn't Do

**What it does:**
- Temporarily overrides the active relationship and uses the specified inactive one instead
- Works only within the CALCULATE where it is placed
- Does not change the globally active relationship

**What it doesn't do:**
- It does not create a new relationship
- It does not modify the model
- It does not work if placed outside CALCULATE

## Common Use Case: Role-Playing Dates

A Sales fact table with both `InvoiceDate` and `ShipDate` needs two separate relationships to Date:

```
Sales[InvoiceDate] → Date[Date]   ← Active (default)
Sales[ShipDate]   → Date[Date]   ← Inactive (requires USERELATIONSHIP)
```

```dax
-- Uses the active relationship (InvoiceDate)
Sales by Invoice Date = SUM ( Sales[SalesAmount] )

-- Activates the inactive ShipDate relationship
Sales by Ship Date =
CALCULATE (
    SUM ( Sales[SalesAmount] ),
    USERELATIONSHIP ( Sales[ShipDate], 'Date'[Date] )
)
```

## Interaction with Other Filters

USERELATIONSHIP inside CALCULATE adds a relationship filter alongside any existing filters. It does not remove them — it overrides which relationship is active for that specific measure.

```dax
-- Still respects any existing filters on other tables;
-- only the Sales → Date relationship is overridden
Sales by Ship Date (Filtered) =
CALCULATE (
    SUM ( Sales[SalesAmount] ),
    USERELATIONSHIP ( Sales[ShipDate], 'Date'[Date] ),
    -- Additional filters still apply here
    KEEPFILTERS ( 'Product'[Category] = "Electronics" )
)
```

## Limitations

- Only works with inactive relationships (will error if applied to an already-active relationship)
- Requires single-column relationships (not multi-column)
- Both columns must be of the same data type
- Cross-filter direction must be appropriate for the filter direction needed

## Related

- [[role-playing-dimensions-pattern]] — single Date table vs duplicated date tables; when to use USERELATIONSHIP vs alternatives
- [[dynamic-date-switching-with-switch]] — combining USERELATIONSHIP with SWITCH for slicer-driven date type switching
- [[uselationship-common-mistakes]] — top errors when using USERELATIONSHIP
