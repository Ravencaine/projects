---
created: 2026-07-26
updated: 2026-08-02
source: dax.pdf
note_type: function
tags: [dax, function, table]
---

# CONTAINSROW

Returns TRUE if a row exists in a table.

## Signature

```dax
CONTAINSROW(<table>, <expr>[, <expr>...])
```

## Parameters

| Term | Definition |
|------|------------|
| `table` | A table expression |
| `expr` | Any DAX expression evaluated for each row of the table |

Returns TRUE if the set of values matches any row in the table.

## Examples

```dax
CONTAINSROW({"Red", "Blue"}, [Color])
```

## Notes

- CONTAINSROW is used to test whether a row exists in a table
- Often used as a filter condition
- Related to CONTAINS but operates on rows instead of column/value pairs

## Related

- [[contains]]
- 
