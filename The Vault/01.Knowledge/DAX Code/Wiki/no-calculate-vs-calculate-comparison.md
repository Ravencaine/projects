---

created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
tags: [dax, calculate, comparison, no-calculate]
note_type: comparison

---

# No CALCULATE vs CALCULATE Comparison

Side-by-side comparison of the same calculation written both ways.

## Comparison

### No CALCULATE

```dax
Sum Total Cost No Pickle =
VAR __ExcludeItem = "Pickle"
VAR __Table = FILTER( 'Table', 'Table'[Item] <> __ExcludeItem )
VAR __Result = SUMX( __Table, [Total Cost] )
RETURN
__Result
```

### CALCULATE

```dax
Sum Total Cost No Pickle C =
CALCULATE(
    SUM( 'Table'[Total Cost] ),
    'Table'[Item] <> "Pickle"
)
```

Both return the same result (38.89). The key differences:

| Aspect | No CALCULATE | CALCULATE |
|--------|-------------|-----------|
| Explicit table | Yes — `FILTER()` | No — implicit |
| Step visible | Yes — each VAR | No — hidden inside |
| Multiple filters | Chain `FILTER()` calls | Comma-separated arguments |
| Debugging | Print `__Table` to inspect | Harder to inspect intermediate state |
| Readability | Longer but transparent | Shorter but dense |

## When to Use Each

- **No CALCULATE:** default for new DAX learners; any calculation where transparency matters
- **CALCULATE:** experienced developers writing short, idiomatic DAX; KEEPFILTERS combinations; complex filter argument expressions

## Related

- [[CALCUHATE]]
- [[no-calculate-dax-pattern]]
- [[calculate]]
