---
created: 2026-07-26
source: dax.pdf
note_type: function
tags: [dax, function, text]
---

# FORMAT

Converts a value to text according to a specified format string.

## Signature

```dax
FORMAT(<value>, <format_string>[, <locale_name>])
```

## Common Format Strings

### Numbers

| Format | Result for 1234.5 |
|--------|-------------------|
| `"General Number"` | 1234.5 |
| `"0.00"` | 1234.50 |
| `"#,##0"` | 1,235 |
| `"$#,##0.00"` | $1,234.50 |
| `"Percent"` | 123450% |
| `"Scientific"` | 1.23E+03 |
| `"Yes/No"` | Yes |

### Dates

| Format | Result for 2024-03-15 |
|--------|-----------------------|
| `"YYYY-MM-DD"` | 2024-03-15 |
| `"MMM YYYY"` | Mar 2024 |
| `"MMMM D, YYYY"` | March 15, 2024 |
| `"Q"` | 1 (quarter) |

### Sections (positive; negative; zero)

```dax
"$#,##0;($#,##0);Zero"   --  1234 | (1234) | Zero
```

## Examples

```dax
-- Date formatting
Month Year = FORMAT('Date'[Date], "MMM YYYY")
Quarter = "Q" & FORMAT('Date'[Date], "Q")

-- Number formatting
Currency = FORMAT([Sales], "$#,##0.00")
Pct = FORMAT([Margin], "Percent")

-- Conditional text
Signed Amount = FORMAT([Amount], "$#,##0;($#,##0)")
```

## Notes

- BLANK → empty string
- `format_string` = BLANK → auto-format based on data type
- `locale_name` allows locale-specific formatting (e.g., European vs US date order)
- FORMAT returns text — not usable in numeric calculations
- Not supported in DirectQuery mode for calculated columns or RLS rules
- Related: [[date-datevalue]]

## Related

- [[date-datevalue]]
