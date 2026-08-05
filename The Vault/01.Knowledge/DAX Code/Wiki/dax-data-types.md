---
created: 2026-07-26
updated: 2026-08-02
source: dax.pdf
note_type: atomic
tags: [dax, fundamentals, data-types]
---

# DAX Data Types

DAX supports a defined set of data types that control how values are stored and evaluated.

## Definition

Every column and expression in a DAX data model has an explicit data type. DAX performs implicit conversions between compatible types but will error on incompatible operations.

## Key Points

### Scalar Types

| Model type | DAX type | Description |
|-----------|----------|-------------|
| Whole Number | Integer | 64-bit integer: -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807 |
| Decimal | Double | 64-bit floating point, 17 significant digits |
| Boolean | Boolean | TRUE or FALSE |
| Text | String | Unicode character string |
| Date | DateTime | Dates after March 1, 1900 |
| Currency | Currency | Fixed decimal, 4 decimal places |

### Table Type

DAX functions can input or output a **Table** data type (e.g., FILTER, ALL, SUMMARIZECOLUMNS). Tables are not displayed directly but are used as inputs to aggregation and other functions.

### Type Coercion Rules

- Mixing Integer and Double: result is Double
- String + Integer: DAX may implicitly convert
- `&` (concatenate) always produces a String result
- `+` with a text string: may return unexpected results (e.g., `"1" + "2"` returns 3 as Integer, but `"A" + "B"` errors)

### Important Gotchas

- **DAX uses datetime, not serial numbers** for dates — unlike Excel which stores dates as serial numbers
- BLANK is not 0 — it is an empty cell that behaves differently in aggregations
- Dividing `1 & 2` (text) returns `"12"`; dividing `"1" + "2"` returns `3`
- DAX functions return a table type often cannot be saved directly — they must be consumed by another function

## Related

- [[dax-overview]] — atomic
- [[dax-context]] — atomic
- [[blank]] — function
- [[convert]] — function
