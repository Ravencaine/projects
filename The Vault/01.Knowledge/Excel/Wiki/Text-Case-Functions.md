---
created: 2026-08-05
updated: 2026-08-05
source: 10 Excel Data Cleaning Hacks That Save Hours Every Week (DigitalBYKewat)
note_type: atomic
tags: [excel, formula, proper, upper, lower, text-case, pivot-table, normalisation]
---

# Text Case Functions: PROPER/UPPER/LOWER

`PROPER()`, `UPPER()`, and `LOWER()` standardise the case of text entries, preventing case-splitting in Pivot Tables and duplicate entries in case-sensitive systems.

## The Three Functions

| Function | What it does | Example |
|----------|-------------|---------|
| `=PROPER(A2)` | Capitalises the first letter of each word | `new york` → `New York` |
| `=UPPER(A2)` | Converts all letters to uppercase | `New York` → `NEW YORK` |
| `=LOWER(A2)` | Converts all letters to lowercase | `NEW YORK` → `new york` |

## Why Standardising Case Matters

The same entity entered in different cases creates separate groups in Pivot Tables:

| Raw | Pivot Table result (broken) |
|-----|--------------------------|
| `new york` | Bar: "new york" |
| `NEW YORK` | Separate bar: "NEW YORK" |
| `New york` | Separate bar: "New york" |

All three should be one bar. Case normalisation collapses them.

## Use Cases

| Case function | Best for |
|--------------|---------|
| `PROPER()` | Names, addresses, city names — proper nouns |
| `UPPER()` | Codes, IDs, status values — technical identifiers |
| `LOWER()` | Emails, URLs — case-sensitive identifiers |

## Combining with TRIM

```excel
=PROPER(TRIM(A2))   -- clean spaces first, then capitalise
```

## Pivot Table Behaviour

Excel Pivot Tables are **not** case-sensitive by default — `NEW YORK` and `New York` are grouped together. However:
- Some data sources (Power Query joins, Power BI) are case-sensitive
- Filtering by case in Excel can behave inconsistently
- Cleaning case upfront prevents downstream errors in ETL pipelines

## Related

- [[TRIM-CLEAN-Functions]] — `CLEAN(TRIM())` to apply before case functions
- [[Inconsistent-Categories-Normalisation]] (Data Modeling) — Text.Trim and dimension lookup tables for persistent category normalisation
- [[Text-Transform-M-Power-Query]] — `Text.Proper`, `Text.Upper`, `Text.Lower` in Power Query
