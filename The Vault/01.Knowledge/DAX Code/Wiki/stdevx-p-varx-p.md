---

created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
tags: [dax, function, statistics, standard-deviation, variance]
note_type: function

---

# STDEVX.P / VARX.P — Population Std Dev & Variance

Iterator functions that return the population standard deviation and variance.

## Signatures

```dax
STDEVX.P( <Table>, <Expression> )
VARX.P( <Table>, <Expression> )
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| Table | Table | Table or table expression to iterate. |
| Expression | Number | Numeric expression evaluated per row. |

## Returns

- `STDEVX.P` → Population standard deviation (sigma, not sample)
- `VARX.P` → Population variance (sigma²)

## Examples

```dax
Pop StdDev := STDEVX.P( 'Table', 'Table'[Value] )
Pop Variance := VARX.P( 'Table', 'Table'[Value] )
```

## Notes

- **P** suffix = population (divide by N). **S** suffix = sample (divide by N-1).
- Use `STDEVX.S` / `VARX.S` for sample data
- Use `STDEV()` / `VAR()` for column-level aggregation (non-iterator)
- Both are iterator functions — use inside measures, not as column formulas

## Related

- [[medianx]] — iterator-based median
- [[weighted-average-in-dax]]
