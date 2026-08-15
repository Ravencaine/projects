---
created: 2026-08-10
updated: 2026-08-10
source: Advanced Power BI DAX Measures for Retail Analytics Pt 1
source_url: https://medium.com/@jjr8888/advanced-power-bi-dax-measures-for-retail-analytics-pt-1-297936931171
note_type: function
tags: [dax, divide, division, safe-division, zero]
---

# DIVIDE() — Safe Division with BLANK on Zero or Blank

`DIVIDE(<numerator>, <denominator>[, <alternateresult>])` performs safe division in DAX. It returns `BLANK()` when the denominator is 0 or BLANK, avoiding the `# arithmetic operation overflow or underflow` error that the `/` operator throws.

## Syntax

```
DIVIDE(<numerator>, <denominator>[, <alternateresult>])
```

| Argument | Description |
|----------|-------------|
| `numerator` | The dividend — the value being divided |
| `denominator` | The divisor — what to divide by |
| `alternateresult` | Optional. Value to return instead of BLANK when denominator is 0 or BLANK. If omitted, returns BLANK(). |

## Behaviour

| Numerator | Denominator | `/` operator | `DIVIDE(numerator, denominator)` | `DIVIDE(..., 0)` |
|-----------|------------|--------------|-------------------------------|------------------|
| 100 | 50 | 2 | 2 | 2 |
| 100 | 0 | Error | BLANK() | 0 |
| 100 | BLANK() | Error | BLANK() | 0 |
| BLANK() | 50 | BLANK() | BLANK() | BLANK() |
| 0 | 50 | 0 | 0 | 0 |

## Common Uses

### Ratio or percentage

```dax
-- Safe percentage: if budget = 0 or blank, show nothing
MEASURE [% of Budget] =
DIVIDE([Total Sales], [Budget])
```

### Variance

```dax
-- Variance: if budget is blank, show nothing
MEASURE [% Variance] =
IF(
    ISBLANK([Budget]),
    BLANK(),
    DIVIDE([Total Sales], [Budget]) - 1
)
```

## DIVIDE vs /

| Situation | Use |
|-----------|-----|
| Denominator is known to never be 0 or BLANK | Either is fine |
| Denominator might be 0 or BLANK | **Always use DIVIDE** |
| You want a fallback value (e.g., 0) instead of BLANK | `DIVIDE(a, b, 0)` |
| In a CALCULATE filter or IF condition | `DIVIDE` handles blanks cleanly |

## Performance

`DIVIDE` is implemented natively and is typically faster than wrapping `/` in `IFERROR` or `IF`. Microsoft recommends it as the standard division function in DAX.

## Related

- [[Conditional-Variance-Display-Hide-Minus-100]] — variance pattern using DIVIDE
- [[BLANK-vs-Zero]] — BLANK() behaviour in calculations
