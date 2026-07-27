---
created: 2026-07-26
source: dax.pdf
note_type: pattern
tags: [dax, pattern, selectedvalue, values]
---

# Use SELECTEDVALUE Instead of VALUES

Test whether a column is filtered to exactly one value using SELECTEDVALUE, not HASONEVALUE + VALUES.

## Purpose

When a report slicer or filter selects exactly one value from a column, you often need to read that value in a measure. The classic pattern uses HASONEVALUE + VALUES; SELECTEDVALUE achieves the same result more cleanly.

## Components

- `SELECTEDVALUE` — returns the single value if exactly one is selected, otherwise returns BLANK or an alternate value
- `VALUES` — returns the set of values visible in the current filter context
- `HASONEVALUE` — returns TRUE if exactly one value is in context

## Structure

```dax
-- Classic pattern (verbose)
Australian Sales Tax =
IF(
    HASONEVALUE(Customer[Country-Region]),
    IF(
        VALUES(Customer[Country-Region]) = "Australia",
        [Sales] * 0.10
    )
)

-- SELECTEDVALUE pattern (clean)
Australian Sales Tax =
IF(
    SELECTEDVALUE(Customer[Country-Region]) = "Australia",
    [Sales] * 0.10
)
```

## Example

```dax
-- Read the selected product color and apply a premium multiplier
Colored Product Premium =
VAR SelectedColor = SELECTEDVALUE('Product'[Color], "No Selection")
RETURN
    SWITCH(
        SelectedColor,
        "Red", [Sales] * 1.10,
        "Blue", [Sales] * 1.05,
        [Sales]
    )
```

## Variations

```dax
-- With alternate result when multiple or no values are selected
SELECTEDVALUE(Column, "Multiple Values")

-- Use with DIVIDE for safe percentage calculations
SELECTEDVALUE(Parameter[Year], MAX('Date'[Year]))
```

## Related

- [[hasonevalue]] — function
- [[values]] — function
- [[if]] — function
- [[switch]] — function
- [[selectedvalue]] — function
