---
created: 2026-07-26
source: dax.pdf
note_type: concept
tags: [dax, reference, parameter-naming, syntax]
---

# DAX Parameter Naming Conventions

Article - 10/20/2023

Parameter names are standardized in DAX reference documentation to make functions easier to learn and understand.

## Standard Parameter Names

| Parameter | Meaning |
|-----------|---------|
| `expression` | Any DAX expression that returns a scalar value, evaluated multiple times |
| `column` | A column reference — unqualified within the current table context |
| `table` | A table expression — can be a table, a function returning a table, etc. |
| `value` | A scalar value — can be a constant, column reference, or expression |
| `number` | A numeric value |
| `dates` or `date` | A column of dates |
| `filter` | A table expression that defines a filter |
| `order` | ASC (default) or DESC |

## Optional Parameters

Parameter names may be omitted from syntax documentation when the prefix is self-explanatory:

```dax
-- Documentation shows:
DATE(Year, Month, Day)

-- Instead of the full form:
DATE(Year_Value, Month_Value, Day_Value)
```

## Parameter Type Indicators

Some functions show type indicators:

| Indicator | Meaning |
|-----------|---------|
| `<columnName>` | A column name in standard DAX syntax |
| `<tableName>` | A table name in standard DAX syntax |
| `<expression>` | Any expression returning a scalar or table |
| `<order>` | ASC or DESC |
| `<variant>` | Optional third argument in iterator functions |

## Related

- [[dax-syntax]]
