---
created: 2026-07-26
updated: 2026-08-02
source: dax.pdf
note_type: function
tags: [dax, function, text]
---

# LEFT, RIGHT, MID, LEN

Extract or measure text.

## LEFT / RIGHT

```dax
LEFT(<text>, <num_chars>)
RIGHT(<text>, <num_chars>)
```

Returns characters from the start or end of a string.

## MID

```dax
MID(<text>, <start_num>, <num_chars>)
```

Returns characters from any position. `start_num` is 1-indexed.

## LEN

```dax
LEN(<text>)
```

Returns the number of characters.

## Examples

```dax
-- First 3 characters (e.g., country code)
Country Code = LEFT('Geography'[PostalCode], 3)

-- Last 4 digits of an account number
Last4 = RIGHT('Account'[Number], 4)

-- Characters 4-8 (e.g., middle of a code)
Middle = MID('Product'[Code], 4, 5)

-- Check if exactly 10 characters
Is Valid Code = LEN('Product'[Code]) = 10
```

## Notes

- All are Unicode-aware — single and double-byte characters are treated equally
- num_chars defaults to 1 if omitted
- Not supported in DirectQuery mode for calculated columns or RLS rules
- Related: [[replace]], [[substitute]]

## Related

- [[replace]]
- [[substitute]]
