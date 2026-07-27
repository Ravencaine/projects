---
created: 2026-07-26
source: dax.pdf
note_type: function
tags: [dax, function, filter-context]
---

# CALCULATE

> **Extended 2026-07-27** — context transition teaching from Advanced Power BI DAX Measures (Jesse Ruiz) and The DAX Concepts... (Daniel Olatunji)

## Signature
```
CALCULATE(<expression>[, <filter1> [, <filter2> [, …]]])
```

## Parameters

| # | Parameter | Type | Description |
|---|-----------|------|-------------|
| 1 | `expression` | scalar | The measure or scalar expression to evaluate |
| 2+ | `filter1`, `filter2`, … | filter | Boolean or table filter expressions |

## Returns

**scalar value**

## Examples

```dax
-- Total Red Sales
Total Red Sales := CALCULATE(SUM(Sales[Amount]), 'Product'[Color] = "Red")

-- Same Period Last Year
Same Period Last Year := CALCULATE([Sales], SAMEPERIODLASTYEAR('Date'[Date]))
```

## Notes

- The first argument is always a **scalar expression** (not a table). It is evaluated in the context modified by the filter arguments — essentially as if it were a measure.
- Multiple filter arguments are **ANDed** together.
- Filters can be:
  - **Boolean**: `Column = value`
  - **Table**: `FILTER(...)`, `CALCULATETABLE(...)`
  - **Modifier functions**: `ALL(...)`, `KEEPFILTERS(...)`, `REMOVEFILTERS(...)`, `ALLEXCEPT(...)`
- `CALCULATETABLE` is the table-returning equivalent of `CALCULATE`.

## Related

- [[calculate-table]] — table-returning counterpart
- [[filter]] — iterator filter function
- [[all]] — clear filters
- [[removefilters]] — clear filters (modern alias)
- [[keepfilters]] — AND filters instead of replacing
- [[dax-context]] — filter vs. row context
