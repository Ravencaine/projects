---
created: 2026-08-09
updated: 2026-08-09
source: "10 Excel Custom Number Formatting Tricks • My Online Training Hub"
note_type: atomic
tags: [excel, formatting, number-format, phone, leading-zero, international, data-entry]
---

# Phone Number Format Preserving Leading Zero

Format phone numbers consistently and preserve leading zeros — no apostrophes, no text conversion. The `0` placeholder in a custom format holds a digit or produces a leading zero.

## Format

```
"+1 "(000) 000 0000
```

- `"+1 "` — literal text prefix (preserved as-is)
- `(000)` — area code in parentheses, 3 digits minimum (leading zero preserved)
- `000 0000` — local number, space-separated

## Why This Works

In custom number formats, `0` is a **required digit placeholder:** unlike `#`, it forces a digit to display even if it's a leading zero. This is critical for phone numbers where the area code may start with 0.

## Benefits

- **Leading zeros preserved:** `020 7946 0958` displays correctly, not `20 7946 958`
- **Consistent formatting:** no manual spaces or apostrophes
- **Data entry speed:** type the digits, format applies automatically
- **No text conversion:** values remain numeric (sortable, usable in formulas)

## Related

- [[Source-10-Custom-Number-Formatting-Tricks-Mynda-Treacy]] — source
