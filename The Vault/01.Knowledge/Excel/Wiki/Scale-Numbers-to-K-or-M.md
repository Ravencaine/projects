---
created: 2026-08-09
updated: 2026-08-09
source: "10 Excel Custom Number Formatting Tricks • My Online Training Hub"
note_type: atomic
tags: [excel, formatting, number-format, scale, thousands, millions, k, m]
---

# Scale Numbers to K or M

Use commas inside a custom number format to remove thousands separators and add a display unit. The underlying value stays full-precision — formulas and charts are unaffected.

## Formats

| Unit | Format |
|------|--------|
| Millions | `#,##0.00,,"M"` |
| Thousands | `#,##0.00,"K"` |
| Millions (no decimals) | `#,##0,,"M"` |

Each comma removes 3 zeros from the display. Two commas = millions.

## Best Practice

Keep the scale consistent across the entire report. Put the unit in the column header rather than formatting every individual cell — reduces visual clutter in large tables.

## Example

`1,250,000` with `#,##0.00,,"M"` → displays as `1.25M`
`1,250,000` with `#,##0.00,"K"` → displays as `1,250.00K`

## Related

- [[Source-10-Custom-Number-Formatting-Tricks-Mynda-Treacy]] — source
- [[Four-Section-Number-Format-Structure]] — combine with colour sections for sign-aware display
