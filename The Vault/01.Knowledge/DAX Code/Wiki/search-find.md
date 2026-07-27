---
created: 2026-07-26
source: dax.pdf
note_type: function
tags: [dax, function, text]
---

# SEARCH and FIND

Find the position of one text string inside another.

## SEARCH

```dax
SEARCH(<find_text>, <within_text>[, <start_num>[, <NotFoundValue>]])
```

| Term | Definition |
|------|------------|
| `find_text` | Text to find (case-insensitive). Supports `?` and `*` wildcards; use `~` to escape |
| `within_text` | Text to search in |
| `start_num` | (Optional) Character position to start from; default 1 |
| `NotFoundValue` | (Optional, recommended) Value to return if not found; defaults to error |

## FIND

```dax
FIND(<find_text>, <within_text>[, <start_num>[, <NotFoundValue>]])
```

Same as SEARCH but **case-sensitive** and **accent-sensitive**.

## Returns

Position number (1-indexed) of the first match, or `NotFoundValue` / error if not found.

## Examples

```dax
-- Find position of "cycle" (case-insensitive)
Pos = SEARCH("cycle", 'Reseller'[Name], 1, BLANK())

-- Extract text after finding a pattern
IFERROR(MID('Code'[Value], SEARCH("-", 'Code'[Value]) + 1, 10), "")

-- Case-sensitive version
Pos = FIND("Sales", 'Category'[Name], 1, 0)

-- Use wildcard to find anything starting with "X"
Pos = SEARCH("X*", 'Product'[Name], 1, 0)
```

## Notes

- SEARCH is **case-insensitive**; FIND is **case-sensitive**
- Both are accent-sensitive
- Always use the `NotFoundValue` parameter (e.g., `BLANK()` or `0`) to prevent errors when text is not found
- Combine with MID to extract text around a found position
- Not supported in DirectQuery mode for calculated columns or RLS rules
- Related: [[left-right-mid]], [[replace]]

## Related

- [[left-right-mid]]
- [[replace]]
