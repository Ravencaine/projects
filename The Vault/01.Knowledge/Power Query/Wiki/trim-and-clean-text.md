---
created: 2026-08-12
source: Top 10 Data Cleaning Tasks in Power BI (Power Query Editor)
source_url: https://medium.com/write-your-world/top-10-data-cleaning-tasks-in-power-bi-power-query-editor-65c3e34c8563
note_type: pattern
tags: [data-cleaning, power-query, text-cleaning, trim, clean]
---

# Trim and Clean Text

Remove excess whitespace and non-printable characters from text columns.

## Purpose

Data imported from databases, CSVs, or legacy systems often contains:
- **Leading/trailing spaces** — breaks joins and lookups
- **Internal multiple spaces** — causes duplicate categories
- **Non-printable characters** — characters 0–31 and 127 from legacy systems

## Components

- `Text.Trim`
- `Text.Clean`
- `Replacer.ReplaceText`

## Structure

```m
Table.TransformColumns(
    Source,
    {{"ColumnName", each Text.Clean(Text.Trim(_)), type text}}
)
```

## Example

```m
// Trim leading/trailing spaces, then remove non-printable characters
Table.TransformColumns(
    Source,
    {
        {"Name", each Text.Clean(Text.Trim(_)), type text},
        {"Address", each Text.Clean(Text.Trim(_)), type text}
    }
)
```

Order matters: `Trim` first, then `Clean` to handle spaces introduced by cleaning.

## Variations

| Function | Removes |
|---------|---------|
| `Text.Trim` | Leading, trailing, and internal multiple spaces |
| `Text.Clean` | Non-printable characters (ASCII 0–31, 127) |
| UI: Transform → Format → Trim | `Text.Trim` |
| UI: Transform → Format → Clean | `Text.Clean` |

## Related

- [[Replace-Values]] — fix sentinel values before/after trimming
- [[Change-Data-Types]] — ensure column type is `text` after cleaning
