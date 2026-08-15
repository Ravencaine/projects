---
created: 2026-08-10
updated: 2026-08-10
source: Excel IMPORTCSV and IMPORTTEXT Functions Explained
source_url: https://www.myonlinetraininghub.com/excel-importcsv-and-importtext-functions-explained
note_type: reference
tags: [excel, importcsv, importtext, dynamic-array, file-import, external-data]
---

# IMPORTCSV and IMPORTTEXT: Spill-Based File Import Functions

Two new Excel functions (Microsoft 365, Beta Channel) that import CSV and text files directly into the worksheet grid as dynamic arrays — no Power Query, no hidden steps, no configuration dialogs.

## IMPORTCSV — CSV Files

```
=IMPORTCSV(path, [skip_rows], [take_rows], [locale])
```

Minimal call — just the file path:
```
=IMPORTCSV("C:\Data\sales.csv")
```

Returns all rows, auto-detected comma delimiter.

| Arg | Description |
|-----|-------------|
| `path` | Full file path in quotes |
| `skip_rows` | Rows to skip from top (e.g., 1 to skip a header) |
| `take_rows` | Number of rows to import (default = all) |
| `locale` | Locale override for date/number formatting (e.g., "en-AU") |

## IMPORTTEXT — Text Files with Custom Delimiters or Fixed Width

```
=IMPORTTEXT(path, [delimiter], [skip_rows], [take_rows], [encoding], [locale])
```

### Custom Delimiter

```
=IMPORTTEXT("C:\Data\products.txt"," ")
```

### Fixed-Width Columns

Define column breakpoints as an ascending array of character positions:

```
=IMPORTTEXT("C:\Data\products.txt", {0, 10, 17}, 1)
```

`{0, 10, 17}` means: split at character 0 (start), 10, and 17. Works for consistent-width fields like dates or product codes.

| Arg | Description |
|-----|-------------|
| `delimiter` | Single character or fixed-width array `{pos1, pos2, ...}` |
| `encoding` | File encoding (UTF-8 is default; specify UTF-16 only when needed) |
| `locale` | Locale override for regional date/number interpretation |

## Refresh Behavior

Both functions are treated as external connections. Refresh via **Data tab → Refresh All**. No hidden query editor steps.

## Key Advantage: Full Transparency

Every import decision is visible in the formula bar. No background steps, no column mapping dialogs. Anyone opening the workbook immediately understands how data was imported.

## When to Use vs Power Query

| Use IMPORTCSV/IMPORTTEXT | Use Power Query |
|---------------------------|----------------|
| Single CSV or text file | Multiple files |
| Clean, structured data | Complex transformations |
| Need formula transparency | Need data cleaning |
| Simple repeatable import | APIs, databases, SharePoint |

## Related

- [[IMPORTCSV-CHOOSECOLS-GROUPBY-Summarization-Pattern]] — passing imported array into LET + CHOOSECOLS + GROUPBY for on-the-fly summarization
- [[Source-Treacy-IMPORTCSV-IMPORTTEXT]] — source note
