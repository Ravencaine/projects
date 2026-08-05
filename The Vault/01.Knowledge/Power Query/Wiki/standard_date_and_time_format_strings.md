---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: reference
tags: ["m-language", "formatting", "dates"]
---


# Standard Date and Time Format Strings

Standard format specifiers for date/time values include: `d` (short date), `D` (long date), `f` (full), `F` (full datetime), `g` (general), `G` (general long), `M`/`m` (month day), `O`/`o` (ISO 8601 round-trip), `R`/`r` (RFC 1123), `s` (sortable), `t` (short time), `T` (long time), `u` (universal sortable), `U` (universal full), `Y`/`y` (year month).

## Quick Reference

| Specifier | Name | Example Output |
|-----------|------|---------------|
| `d` | Short date | `3/15/2024` |
| `D` | Long date | `Friday, March 15, 2024` |
| `f` | Full date/short time | `Friday, March 15, 2024 4:00 PM` |
| `F` | Full date/long time | `Friday, March 15, 2024 4:00:00 PM` |
| `g` | General/short time | `3/15/2024 4:00 PM` |
| `G` | General/long time | `3/15/2024 4:00:00 PM` |
| `M` or `m` | Month/day | `March 15` |
| `O` or `o` | ISO 8601 | `2024-03-15T16:00:00.0000000Z` |
| `R` or `r` | RFC 1123 | `Fri, 15 Mar 2024 16:00:00 GMT` |
| `s` | Sortable | `2024-03-15T16:00:00` |
| `t` | Short time | `4:00 PM` |
| `T` | Long time | `4:00:00 PM` |
| `U` | Universal full | `Friday, March 15, 2024 11:00:00 PM` |
| `Y` or `y` | Year month | `March 2024` |

## Examples

```m
Date.ToText(#date(2024, 3, 15), "d")      // "3/15/2024"
Date.ToText(#date(2024, 3, 15), "D")      // "Friday, March 15, 2024"
Date.ToText(#date(2024, 3, 15), "Y")     // "March 2024"
DateTime.ToText(#datetime(2024,3,15,14,30,0), "O")  // ISO 8601
```

## Related

- [[custom_date_and_time_format_strings]] — custom patterns
- [[culture_and_text_formatting]] — culture affects output
