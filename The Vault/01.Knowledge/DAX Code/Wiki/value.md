---
created: 2026-07-26
source: dax.pdf
note_type: function
tags: [dax, function, text]
---

# VALUE

Converts a text string representing a number into a numeric value.

## Signature

```dax
VALUE(<text>)
```

## Examples

```dax
-- Convert text column to number
NumValue = VALUE('Sales'[AmountText])

-- Use with RIGHT to extract numeric suffix
Order Num = VALUE(RIGHT('Order'[Code], 4))
```

## Notes

- Implicit conversion handles most cases — VALUE is rarely needed explicitly
- Input must be in a recognized number, date, or time format
- Returns error if the text is not a valid number format
- Use TRIM/CLEAN first if the text may have extra spaces or non-printable characters
- VALUE returns a decimal number
- Not supported in DirectQuery mode for calculated columns or RLS rules

## Related

- [[format]]
- [[left-right-mid]]
