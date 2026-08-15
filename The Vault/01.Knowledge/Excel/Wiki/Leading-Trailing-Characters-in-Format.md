---
created: 2026-08-09
updated: 2026-08-09
source: "10 Excel Custom Number Formatting Tricks • My Online Training Hub"
note_type: atomic
tags: [excel, formatting, number-format, leading-characters, trailing-characters, fill, signature, table-of-contents]
---

# Leading/Trailing Characters in Number Format

Use `@` (text placeholder) with `*` (repeat character) to fill a cell with a repeating character — useful for signature lines, dotted leaders, and visual layout effects.

## Key Placeholders

| Placeholder | Meaning |
|-------------|---------|
| `@` | Text character position (like `*` for numbers) |
| `*` | Repeat the next character to fill the remaining cell width |
| `0` | Required digit placeholder |
| `#` | Optional digit placeholder |

## Signature Line Pattern

```
@*_
```

`@` holds the text (e.g. a name). `*_` repeats underscores to the right edge of the cell — creates a fill line after any name.

## Dot Leader (Table of Contents)

```
*.@
```

`*` repeats dots before `@` — dots fill from left to the text, creating a table-of-contents dot leader effect.

## Use Cases

- Signature lines on forms
- Table of contents with dot leaders
- Dotted underlines for fill-in forms
- Visual separation between label and value in report layouts

## Related

- [[Source-10-Custom-Number-Formatting-Tricks-Mynda-Treacy]] — source
