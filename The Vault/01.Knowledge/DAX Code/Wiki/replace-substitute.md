---
created: 2026-07-26
source: dax.pdf
note_type: function
tags: [dax, function, text]
---

# REPLACE and SUBSTITUTE

Replace text by position or by content.

## REPLACE

```dax
REPLACE(<old_text>, <start_num>, <num_chars>, <new_text>)
```

Replaces characters starting at `start_num` for `num_chars` characters.

## SUBSTITUTE

```dax
SUBSTITUTE(<text>, <old_text>, <new_text>[, <instance_num>])
```

Replaces all occurrences (or a specific instance) of `old_text` with `new_text`.

| Term | Definition |
|------|------------|
| `text` | The source text |
| `old_text` | Text to find |
| `new_text` | Replacement text |
| `instance_num` | (Optional) Which occurrence to replace; omit to replace all |

## Examples

```dax
-- Replace first 3 characters with "X"
Masked Code = REPLACE('Account'[Code], 1, 3, "XXX")

-- Replace all spaces with underscores
No Spaces = SUBSTITUTE('Product'[Name], " ", "_")

-- Replace only the first occurrence
Replace First = SUBSTITUTE('Log'[Message], "ERROR", "WARNING", 1)
```

## Notes

- Use **SUBSTITUTE** when you know the text to replace but not its position
- Use **REPLACE** when you know the position but not the content
- REPLACE: if `num_chars` is BLANK, `new_text` is inserted without replacing anything
- SUBSTITUTE with `instance_num` targets a specific occurrence
- Not supported in DirectQuery mode for calculated columns or RLS rules

## Related

- [[left-right-mid]]
- [[exact]]
