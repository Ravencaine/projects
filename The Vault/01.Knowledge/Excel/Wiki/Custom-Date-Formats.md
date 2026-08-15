---
created: 2026-08-09
updated: 2026-08-09
source: "10 Excel Custom Number Formatting Tricks • My Online Training Hub"
note_type: atomic
tags: [excel, formatting, number-format, date, custom-date, regional, presentation]
---

# Custom Date Formats

Default date formats are limited. Custom date formats give full control over how dates display while keeping the underlying value as a real Excel date — grouping in PivotTables and date calculations remain intact.

## Common Date Format Codes

| Code | Meaning | Example |
|------|---------|---------|
| `d` | Day (no leading zero) | `9` |
| `dd` | Day (two digits) | `09` |
| `ddd` | Day name (short) | `Mon` |
| `dddd` | Day name (full) | `Monday` |
| `m` | Month (no leading zero) | `6` |
| `mm` | Month (two digits) | `06` |
| `mmm` | Month name (short) | `Jun` |
| `mmmm` | Month name (full) | `June` |
| `yy` | Year (2 digits) | `26` |
| `yyyy` | Year (4 digits) | `2026` |

## Examples

| Format | Display |
|--------|---------|
| `dd-mmm-yy` | `09-Aug-26` |
| `mmmm d, yyyy` | `August 9, 2026` |
| `mmm-yy` | `Aug-26` |
| `dd/mm/yyyy` | `09/08/2026` |

## Key Principle

The cell holds a real Excel date serial number. Change the format, the display changes — but grouping, sorting, YEAR()/MONTH(), and PivotTable grouping all continue to work.

## Use Cases

- Regional format preferences (US vs UK date order)
- Dashboard titles that include the date
- Reports with consistent date formatting regardless of system locale

## Related

- [[Source-10-Custom-Number-Formatting-Tricks-Mynda-Treacy]] — source
