---
created: 2026-07-29
updated: 2026-08-02
source: "[[Author-Isabelle-Bittar|Isabelle Bittar]]"
note_type: function
tags: [text-formatting, number-format, date-format, concatenation]
related: [UNICHAR, CONCATENATEX, SUBSTITUTE]
---

# FORMAT

Converts a value to text in a specified format. Essential for dynamic labels, KPI card text, and any text concatenation that includes numbers or dates.

## Signature

```dax
FORMAT(<value>, <formatText>)
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `value` | Any | The value to format (number, date, currency) |
| `formatText` | String | A format string (named or custom) |

## Common Format Strings

### Number Formats

| Format | Input | Output |
|-------|-------|--------|
| `"0"` | `1234.5` | `1235` |
| `"0.00"` | `1234.5` | `1234.50` |
| `"#,##0"` | `1234567` | `1,234,567` |
| `"$#,##0.00"` | `1234.5` | `$1,234.50` |
| `"0%"` | `0.235` | `24%` |
| `"0.0%"` | `0.2345` | `23.5%` |
| `"0.0##x"` | `1.234` | `1.234x` |

### Date Formats

| Format | Result |
|--------|--------|
| `"yyyy-mm-dd"` | `2024-03-15` |
| `"mmm yyyy"` | `Mar 2024` |
| `"dddd"` | `Friday` |
| `"dd/mmm"` | `15/Mar` |

### Color-Value Labels

Format a metric with its color as a text label for display in a visual:
```dax
KPI Label =
    [KPI Name] & ": " &
    FORMAT([KPI Value], "$#,##0") & " " &
    "（" & FORMAT([Variance], "+0.0%;-0.0%;0.0%") & "）"
```

## Examples

**Dynamic axis label with date range:**
```dax
Date Range Label =
    FORMAT([Min Date], "mmm dd") & " - " & FORMAT([Max Date], "mmm dd, yyyy")
```

**Performance score as a grade:**
```dax
Performance Grade =
    VAR _Score = [Metric Value]
    RETURN
        SWITCH(
            TRUE(),
            _Score >= 0.9, "A",
            _Score >= 0.8, "B",
            _Score >= 0.7, "C",
            "D"
        )
```

**Combine with UNICHAR for KPI cards:**
```dax
KPI Card Text =
    [KPI Title] & " | " &
    FORMAT([KPI Value], "$#,##0") & " " &
    UNICHAR(9650) & " " &
    FORMAT([Variance], "+0.0%;-0.0%")
```

## Notes

- `FORMAT` returns text — the result cannot be used in further numeric calculations.
- Named formats (`"General Number"`, `"Currency"`, `"Short Date"`) are locale-dependent — prefer explicit custom strings like `"$#,##0.00"` for consistent cross-environment output.
- In Bittar's KPI card techniques, `FORMAT` is used to construct the card's main value label and the variance indicator text.
- Use `FORMAT` inside `CONCATENATEX` when building text lists with formatted numbers (e.g., `"$1.2M, $890K, $450K"`).
- `FORMAT` for dates uses DAX/M code page formatting, which differs from Excel's format strings in some edge cases.

## Related

- [[UNICHAR]] — combine with FORMAT for labelled values
- [[CONCATENATEX]] — format each item in a table iteration
- [[SUBSTITUTE]] — inject FORMAT results into HTML strings
