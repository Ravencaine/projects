---
created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
note_type: function
tags: [dax, function, text, string]
---

# LEFT() — Extract Prefix Characters from DAX Text

`LEFT()` returns the specified number of characters from the start of a text string.

## Signature

```dax
LEFT( <text>, <num_chars> )
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `<text>` | string | The text string to extract from — can be a column reference or string literal |
| `<num_chars>` | integer | The number of characters to extract from the left side |

## Returns

A text string — the leftmost N characters of the input string.

## Examples

```dax
-- Extract year (first 4 characters) from a DateKey stored as text
Year := LEFT(dbo_DimDate[Datekey], 4)

-- Combined with CALCULATE to filter by year
StoreSales2009 := CALCULATE(
    [StoreSales],
    LEFT(dbo_DimDate[Datekey], 4) = "2009"
)
```

## Notes

- `LEFT()` works on string (text) columns — if DateKey is stored as a numeric type, first convert with `FORMAT()` or `CAST()`
- `RIGHT()` is the complementary function for extracting from the end
- `MID()` extracts from a specific starting position
- Dunlop uses `LEFT` in the year-over-year example because the DimDate table's `Datekey` field stores dates as a text string (e.g., "20090101")

## Related

- [[dax-year-over-year]] — the pattern where LEFT is used for year extraction
- [[dax-calculate-function]] — CALCULATE with LEFT filter for year-based calculations
