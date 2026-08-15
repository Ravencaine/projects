---

created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
tags: [dax, function, math, rounding, multiple]
note_type: function

---

# MRound — Multiple Rounding

Rounds a number to the nearest specified multiple.

## Signature

```dax
MROUND( <Number>, <Multiple> )
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| Number | Number | Value to round. |
| Multiple | Number | Multiple to round to. |

## Examples

```dax
MROUND( 27, 5 )   -- returns 25 (nearest 5)
MROUND( 28, 5 )   -- returns 30
MROUND( 0.333, 0.25 )  -- returns 0.25
MROUND( 1.99, 0.1 )    -- returns 2.0
```

## Notes

- Rounds away from zero when the number is exactly halfway
- Returns BLANK if either argument is BLANK
- Useful for pricing (round to nearest $0.99), scheduling (round to nearest 15 min), etc.

## Related

- [[round-trunc-int]]
- [[round-trunc-int]]
