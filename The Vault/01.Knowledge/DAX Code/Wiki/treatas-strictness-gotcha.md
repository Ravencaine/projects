---
created: 2026-07-31
updated: 2026-08-02
source: "🧠 \"Which Date Is It, Anyway\" — Making Peace with TREATAS in a Multi-Date World.md"
note_type: gotcha
tags: [dax, treatas, gotcha, data-type-mismatch, blanks, strictness]
---

# TREATAS Strictness — Data Type Alignment and Blank Handling

TREATAS silently fails or produces unexpected results when the projected column and target column have mismatched data types, or when the target column contains blank values.

## Symptom

TREATAS returns unexpected rows or blanks, or the measure produces no results despite the slicer having valid values.

## Causes

**1. Data type mismatch**

TREATAS requires the data types of the source expression and the target column to match exactly. Common mismatches:

- `Date` vs `DateTime` — the Date table column is `Date`, the fact column is `DateTime`
- `Integer` vs `Text` — surrogate keys of different types
- `Decimal` vs `Integer` — numeric key mismatches

The engine does not coerce types. If the types don't match, TREATAS produces an empty result set silently.

**2. Blank values in the target column**

If the fact table date column (e.g., `ShipDate`) has blank/null rows, TREATAS may propagate blanks into the result or drop those rows entirely. Unlike a physical relationship, TREATAS does not have configurable blank-row handling.

**3. Granularity mismatch**

If the Date table has one row per day and the fact column has multiple entries per day, TREATAS works correctly (many-to-one filtering). However, if the Date table is coarser (e.g., monthly) and the fact column is daily, the mapping may not behave as expected.

## Fixes

**For data type mismatch — use a calculated column:**

```dax
-- Add to the fact table:
ShipDateKey = TRUNC(CustomerTransactions[ShipDate])   -- removes time component

-- Then TREATAS against the key column:
CALCULATE(
    SUM(CustomerTransactions[Quantity]),
    TREATAS(VALUES('Date'[Date]), CustomerTransactions[ShipDateKey])
)
```

Or align the Date table to match:
```dax
-- Add to the Date dimension:
DateKey = TRUNC('Date'[Date])
```

**For blank handling — filter blanks before TREATAS:**

```dax
Shipped Qty by Date =
CALCULATE(
    SUM(CustomerTransactions[Quantity]),
    TREATAS(
        VALUES('Date'[Date]),
        CALCULATETABLE(
            CustomerTransactions,
            KEEPFILTERS(NOT ISBLANK(CustomerTransactions[ShipDate]))
        )
    )
)
```

Or add a WHERE clause at the data source level.

## Related

- [[cross-fact-treatas-virtual-relationships]] — `function` — the function this gotcha applies to
- [[treatas-multi-date-metrics]] — `pattern` — real-world usage where this gotcha surfaces
