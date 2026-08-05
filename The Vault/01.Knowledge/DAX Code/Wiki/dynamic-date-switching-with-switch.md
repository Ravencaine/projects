---
created: 2026-08-01
updated: 2026-08-02
source: "RELATIONSHIP in DAX - Unlocking Role - Playing Dimensions.md"
note_type: atomic
tags: [dax, switch, selectedvalue, uselationship, dynamic-filtering, beginner, intermediate]
---

# Dynamic Date Switching with SWITCH + SELECTEDVALUE

Combine USERELATIONSHIP with SWITCH and SELECTEDVALUE to let users choose which date perspective to view via a slicer — without needing separate visuals or measures.

## The Pattern

### Step 1: Create a Parameter Table

Create an unconnected table with the date types as values:

```
DateType Table:
| Date Type     |
|--------------|
| Invoice Date |
| Ship Date    |
```

This table is **not related** to any other table in the model.

### Step 2: Write the Dynamic Measure

```dax
Dynamic Sales =
SWITCH (
    SELECTEDVALUE ( DateType[Date Type] ),
    "Invoice Date", [Sales by Invoice Date],
    "Ship Date",    [Sales by Ship Date]
)
```

`SELECTEDVALUE` reads the user's slicer selection from the DateType parameter table. `SWITCH` routes to the appropriate pre-built measure.

### Step 3: Build the Pre-Built Measures

```dax
Sales by Invoice Date =
    SUM ( Sales[SalesAmount] )

Sales by Ship Date =
CALCULATE (
    SUM ( Sales[SalesAmount] ),
    USERELATIONSHIP ( Sales[ShipDate], 'Date'[Date] )
)
```

## Why This Pattern Works

- The parameter table (DateType) drives which measure is active — no relationships needed
- `SELECTEDVALUE` returns the single selected value; if nothing is selected or multiple values are selected, it returns blank (or a default)
- SWITCH evaluates in order and returns the first matching branch

## Handling "No Selection" and "Multiple Selections"

```dax
Dynamic Sales =
VAR SelectedType = SELECTEDVALUE ( DateType[Date Type] )
RETURN
    SWITCH (
        TRUE (),
        ISBLANK ( SelectedType ), [Sales by Invoice Date],  -- default when nothing selected
        SelectedType = "Invoice Date", [Sales by Invoice Date],
        SelectedType = "Ship Date",    [Sales by Ship Date]
    )
```

Using `SWITCH ( TRUE(), ... )` pattern allows Boolean conditions rather than equality checks against specific values.

## Use Cases

- Single chart that switches between Order Date, Ship Date, Delivery Date
- Toggle between Invoice Amount vs Budget Amount
- Revenue vs Cost comparison on the same visual

## Limitations

- Only one date type visible at a time (for side-by-side comparison, use separate measures instead)
- Requires a dedicated parameter table
- `SELECTEDVALUE` may need `ALLNOGROUPING()` or `HASONEVALUE()` guard depending on the visual context

## Related

- [[uselationship-function]] — the underlying mechanism for activating inactive relationships
- [[role-playing-dimensions-pattern]] — when to use USERELATIONSHIP vs other approaches
- [[logical-functions-switc]] — SWITCH syntax and patterns beyond this use case
