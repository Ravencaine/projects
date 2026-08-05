---
created: 2026-07-26
updated: 2026-08-02
source: dax.pdf
note_type: function
tags: [dax, function, text]
---

# LOWER, UPPER, TRIM

Transform text casing or remove whitespace.

## LOWER / UPPER

```dax
LOWER(<text>)
UPPER(<text>)
```

Converts all letters to lowercase or uppercase.

## TRIM

```dax
TRIM(<text>)
```

Removes leading, trailing, and repeated interior spaces from text (but not interior tabs).

## Examples

```dax
-- Normalize to lowercase for matching
Email Match = LOWER('User'[Email]) = LOWER('Input'[Email])

-- Standardize to uppercase
Region Code = UPPER('Location'[Region])

-- Clean imported text
Clean Name = TRIM('Import'[RawName])
```

## Notes

- LOWER/UPPER affect only letters — numbers and symbols are unchanged
- TRIM is especially useful for cleaning data imported from external systems
- TRIM in DAX removes all extra spaces (like Excel's TRIM), not just leading/trailing
- Not supported in DirectQuery mode for calculated columns or RLS rules
- Related: [[exact]]

## Related

- [[exact]]
