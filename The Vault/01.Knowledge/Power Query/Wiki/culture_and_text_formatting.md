---
created: 2026-07-27
updated: 2026-08-02
source: "m-code.pdf"
note_type: atomic
tags: ["m-language", "culture", "text"]
---


# Culture and Text Formatting in M

M's text formatting is culture-aware. Number and date formatting (via `Number.ToText`, `Date.ToText`) uses culture settings that affect decimal separators, thousand separators, month names, and date order.

## Key Points

- Culture affects number formatting (decimal/thousand separators)
- Culture affects date/time formatting (month names, order of day/month/year)
- The `Culture` parameter accepts culture codes (e.g., `"en-US"`, `"de-DE"`, `"pt-BR"`)
- Default culture is determined by system locale
- `Comparer.FromCulture` respects culture for text comparisons

## Examples

```m
// US format: 1,234.56
Number.ToText(1234.56, "N2", "en-US")

// German format: 1.234,56
Number.ToText(1234.56, "N2", "de-DE")

// Date in Brazilian Portuguese
Date.ToText(#date(2025, 1, 15), "d", "pt-BR")  // "15/01/2025"
```

## Related

- [[standard_numeric_format_strings]] — format specifiers
- [[custom_numeric_format_strings]] — custom format patterns
- [[comparer_functions]] — Comparer.FromCulture
