---
created: 2026-07-26
updated: 2026-08-02
source: dax.pdf
note_type: gotcha
tags: [dax, gotcha, auto-exist, all, filter-context]
---

# Auto-Exist and ALL() Gotchas

Article - 09/20/2022

## Auto-Exist

Auto-exist is an optimization in DAX where only combinations of values that actually exist in the data are generated. This can produce unexpected results when ALL() is used incorrectly.

### The Problem

When you have multiple columns from the same table in a visual, auto-exist limits the combinations to those that actually exist in the data. This is usually desirable, but can cause issues with ALL().

### Example

```dax
-- This may not behave as expected because of auto-exist
CALCULATE(
    [Sales Amount],
    ALL('Product'[Color], 'Product'[Category])
)
```

When both Color and Category are in the visual, auto-exist means that ALL() only removes filters on combinations that exist — not on all individual values independently.

### Solution

Use REMOVEFILTERS() or be explicit:

```dax
-- Remove all filters on both columns independently
CALCULATE(
    [Sales Amount],
    REMOVEFILTERS('Product'[Color]),
    REMOVEFILTERS('Product'[Category])
)
```

## ALL() Unexpected Results

ALL() returns the full unfiltered column. But when used as a filter argument in CALCULATE, it removes filters. The gotcha: ALL() removes filters on the ENTIRE table, not just the column you specified.

### Example: ALL on one column vs. entire table

```dax
-- Removes filter on Product[Color] only
CALCULATE([Sales], ALL('Product'[Color]))

-- Removes ALL filters on the entire Product table
CALCULATE([Sales], ALL('Product'))
```

## ALLEXCEPT: When to Use It

ALLEXCEPT keeps filters on specified columns while removing all others:

```dax
-- Remove filters everywhere EXCEPT on the Year column
CALCULATE(
    [Sales Amount],
    ALLEXCEPT('Date', 'Date'[Year])
)
```

This is equivalent to:
```dax
CALCULATE(
    [Sales Amount],
    REMOVEFILTERS('Product'),
    REMOVEFILTERS('Customer'),
    REMOVEFILTERS('Product Category'),
    ... (all tables except Date)
)
```

## Cross-Filter Gotcha

Filters flow in one direction by default. If you need filters to flow in both directions, use CROSSFILTER:

```dax
CALCULATE(
    [Sales],
    CROSSFILTER('Sales'[ProductKey], 'Product'[ProductKey], BOTH)
)
```

## Related

- [[all]]
- [[allexcept]]
- [[calculate]]
- [[crossfilter]]
