---
created: 2026-07-26
updated: 2026-08-02
source: dax.pdf
note_type: function
tags: [dax, function, table]
---

# DATATABLE

Declare an inline table of static data values in a DAX expression.

## Signature

```dax
DATATABLE(
    ColumnName1, DataType1,
    ColumnName2, DataType2,
    ...,
    {
        { Value1, Value2, ... },
        { ValueN, ValueNN, ... }
    }
)
```

## Data Types

`BOOLEAN`, `CURRENCY`, `DATETIME`, `DOUBLE`, `INTEGER`, `STRING`

## Examples

```dax
-- Static parameter table
StatusTable = DATATABLE(
    "Status", STRING,
    "Value", INTEGER,
    {
        { "Active", 1 },
        { "Inactive", 0 },
        { "Pending", 2 }
    }
)

-- Date + value lookup
ParamTable = DATATABLE(
    "Month", DATETIME,
    "Rate", DOUBLE,
    {
        { DATE(2024, 1, 1), 0.05 },
        { DATE(2024, 7, 1), 0.06 }
    }
)
```

## Notes

- Values must be **constants**: cannot reference columns, tables, or relationships
- Can use `DATE()`, `TIME()`, `BLANK()`, and basic operators
- Nested arrays define rows: outer `{}` wraps all rows; inner `{}` wraps each row
- Missing values → BLANK
- Useful for small static lookup tables without a data source
- Related: [[generateseries-and-datatable]]

## Related

- [[generateseries-and-datatable]]
