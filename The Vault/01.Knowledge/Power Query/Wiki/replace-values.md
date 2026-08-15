---
created: 2026-08-12
source: Top 10 Data Cleaning Tasks in Power BI (Power Query Editor)
source_url: https://medium.com/write-your-world/top-10-data-cleaning-tasks-in-power-bi-power-query-editor-65c3e34c8563
note_type: pattern
tags: [data-cleaning, power-query, replace-values]
---

# Replace Values

Fix spelling errors or standardize inconsistent entries in a column.

## Purpose

Correct data entry errors and normalise categorical values. Common use: replace sentinel values like `"N/A"` or `""` with `null`.

## Components

- `Table.ReplaceValue`

## Structure

```m
Table.ReplaceValue(
    Source,
    oldValue,     // value to find
    newValue,    // replacement
    replacer,    // replacer function: Replacer.ReplaceValue or Replacer.ReplaceText
    columns      // list of column names
)
```

## Example

```m
// Replace "N/A" strings with null
Table.ReplaceValue(
    Source,
    "N/A",
    null,
    Replacer.ReplaceValue,
    {"StatusColumn"}
)

// Replace text (case-insensitive)
Table.ReplaceValue(
    Source,
    "inactive",
    "Inactive",
    Replacer.ReplaceText,
    {"StatusColumn"}
)
```

## Variations

| Replacer | Use case |
|----------|----------|
| `Replacer.ReplaceValue` | Exact match, including `null` |
| `Replacer.ReplaceText` | Regex-style text replacement |
| UI: Transform → Replace Values | Calls `Replacer.ReplaceValue` under the hood |

## Related

- [[Trim-and-Clean-Text]] — fix whitespace/corrupt characters
- [[Change-Data-Types]] — convert to correct type after cleaning
