---

created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
tags: ["dax", "function", "math", "truncate", "integer"]
note_type: function

---

# TRUNC / INT — Truncation Functions

Removes the decimal portion of a number, returning the integer part.

## Signatures

```dax
TRUNC( <Number>, [<NumDigits>] )
INT( <Number> )
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| Number | Number | Number to truncate. |
| NumDigits | Number | Decimal places to keep. Optional. Default: 0. |

## Returns

The truncated number.

## Examples

```dax
TRUNC( 3.7 )     -- returns 3
TRUNC( -3.7 )    -- returns -3
INT( 3.7 )       -- returns 3
INT( -3.7 )      -- returns -4 (rounds toward negative infinity)

-- Truncate to 2 decimal places
Price Clean := TRUNC( [Price], 2 )
```

## Differences

| Function | 3.7 | -3.7 |
|----------|-----|------|
| TRUNC | 3 | -3 |
| INT | 3 | -4 |
| ROUND | 4 | -4 |

- `INT()` always rounds toward negative infinity (floor)
- `TRUNC()` simply removes the fractional part
- Use `TRUNC()` when you want consistent truncation regardless of sign

## Related

- [[round-trunc-int]] — full rounding guide
- [[mround]] — multiple rounding
