---
created: 2026-07-26
source: dax.pdf
note_type: function
tags: [dax, function, user-defined-functions, udf, preview]
---

# DAX User-Defined Functions (UDF)

User-Defined Functions (UDFs) let you package DAX logic into reusable, named functions. UDFs are first-class model objects — callable from measures, calculated columns, visual calculations, and other UDFs.

> **Status:** Preview — not all limitations resolved (see Notes section)

## Signature

```dax
FUNCTION FunctionName = (
    [param1] : [TYPE] [: SUBTYPE] [: PARAMETER_MODE],
    [param2] : [TYPE] [: SUBTYPE] [: PARAMETER_MODE],
    ...
) =>
    <expression>
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `TYPE` | scalar, table, any | What type the parameter accepts |
| `SUBTYPE` | int64, decimal, double, string, datetime, boolean, numeric | For scalar types: specific subtype |
| `PARAMETER_MODE` | val, expr | When argument is evaluated: val = eager, expr = lazy |

### Available Types

| Type | Description |
|------|-------------|
| `AnyVal` | Any scalar value |
| `Scalar` | Any scalar value (same as AnyVal) |
| `Table` | A table |
| `AnyRef` | Any reference (column, table, measure, calendar) |
| `CalendarRef` | Reference to a calendar |
| `ColumnRef` | Reference to a column |
| `MeasureRef` | Reference to a measure |
| `TableRef` | Reference to a table |

### Parameter Modes

- `val` — argument is evaluated once before entering the function (eager)
- `expr` — argument is passed as an unevaluated expression; evaluated lazily inside the function

## Returns

Whatever the `<expression>` in the function body returns.

## Examples

### Basic UDF

```dax
-- Define in DAX query view
DEFINE
    FUNCTION AddTax = (amount : NUMERIC) => amount * 1.1
EVALUATE { AddTax(100) }
-- Returns: 110

-- Use in a measure
Total Sales with Tax := AddTax([Total Sales])
```

### UDF with Table Parameter

```dax
FUNCTION SalesAbove = (t : TABLE, threshold : NUMERIC val) =>
    FILTER(t, [Sales] > threshold)

-- Use: filter Sales table to rows above $10,000
VAR HighSales = SalesAbove('Sales', 10000)
RETURN
    COUNTROWS(HighSales)
```

### Type Checking in UDFs

```dax
FUNCTION GetCurrencyName = (currency : ANY) =>
    IF(
        ISINT64(currency),
        -- lookup by key
        LOOKUPVALUE('Currency'[Name], 'Currency'[Key], currency),
        -- lookup by code
        LOOKUPVALUE('Currency'[Name], 'Currency'[Code], currency)
    )
```

### Nested UDFs

```dax
FUNCTION AddTax = (amount : NUMERIC val) => amount * 1.1
FUNCTION AddTaxAndDiscount = (amount : NUMERIC val) =>
    AddTax(amount) * 0.9  -- 10% tax then 10% discount
```

## Notes

- UDFs are created in DAX query view or TMDL view (Power BI Desktop)
- UDFs cannot be authored or modelled in the Power BI Service
- Limitations (preview):
  - Cannot combine UDFs with translations
  - Object-Level Security (OLS) does not transfer to UDFs
  - Formula fix-up for unqualified column names is limited
  - Parser inconsistencies in advanced scenarios with expr parameters

## Related

- [[var-variable]] — function (related syntax)
- [[tableof]] — function (new function for UDFs)
- [[var-variable]] — function (new function for UDFs)
