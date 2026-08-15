---
created: 2026-08-13
source: "Top 10 Data Cleaning Tasks in Power BI (Power Query Editor)"
source_url: https://medium.com/write-your-world/top-10-data-cleaning-tasks-in-power-bi-power-query-editor-65c3e34c8563
note_type: gotcha
tags: [power-query, data-types, power-bi, silent-failure]
---

# Wrong Data Type Silently Breaks Visuals

Power Query does not warn you when a column's data type is wrong — visuals just render incorrectly or refuse to load.

## Expected Behaviour

A column of numbers should produce a numeric visual. A column of dates should sort chronologically. Power BI should auto-detect or at least warn when these expectations are violated.

## Actual Behaviour

Assigning the wrong type is silent:
- Numbers stored as **text** produce incorrect aggregations, missing totals, and broken charts
- Dates stored as **text** are not recognised as dates — sorting and time hierarchies do not work
- Decimals stored as **whole number** silently truncate values
- Power Query shows no warning on type assignment; the visual simply misbehaves

## Why It Happens

Power Query treats type conversion as a transform, not a validation. The type is changed without checking whether the column values are actually valid for that type. Invalid values may be preserved as errors or converted to null without notification.

## How to Handle It

1. Always set the correct type **immediately** after loading a column — before any other transforms
2. Check the type icon in the column header (ABC = text, 123 = whole number, calendar = date)
3. After setting type, use **Replace Errors** or **Remove Errors** to catch any conversion failures
4. Validate totals and aggregations in a matrix visual before assuming the type is correct

## Related Gotchas

- Fill Down / Up — direction matters
