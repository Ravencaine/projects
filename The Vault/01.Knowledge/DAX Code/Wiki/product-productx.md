---
created: 2026-07-26
updated: 2026-08-02
source: dax.pdf
note_type: function
tags: [dax, function, math]
---

# PRODUCT and PRODUCTX

Multiply all values in a column or expression to return the product.

## PRODUCT

```dax
PRODUCT(<column>)
```

Multiplies all values in a column. Ignores blanks, logical values, and text.

`PRODUCT(Table[Column])` is equivalent to `PRODUCTX(Table, Table[Column])`.

## PRODUCTX

```dax
PRODUCTX(<table>, <expression>)
```

Iterator — evaluates `expression` per row, then returns the product of all results.

## Examples

```dax
-- Product of a column
Total Growth Factor = PRODUCT('Returns'[GrowthRate])

-- Product of per-row growth rates
Compound Growth = PRODUCTX('Returns', 1 + 'Returns'[Rate])
```

## Notes

- Useful for compound growth, chain reaction, and factorial-type calculations
- Ignores BLANK, logical values, and text
- Not supported in DirectQuery mode for calculated columns or RLS rules

## Related

- [[sumx]]
