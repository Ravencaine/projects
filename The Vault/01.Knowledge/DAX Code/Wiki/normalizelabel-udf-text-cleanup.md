---
created: 2026-08-02
source: Power BI New User Defined Functions 10 Must-Have You'll Use in Every Report
note_type: function
tags: [dax, udf, text, normalization, trim, data-cleaning, power-bi]
---

# NormalizeLabel — Text Cleanup UDF

Trims whitespace and replaces common invisible characters. Use on text fields before joins, group-bys, or `LOOKUPVALUE` to prevent mismatches from tabs and non-breaking spaces.

## Signature

```c
UDF NormalizeLabel = ( s : STRING ) => TRIM(
    SUBSTITUTE(
        SUBSTITUTE(s, UNICHAR(160), " "),   // non-breaking space
        UNICHAR(9), " "                     // tab
    )
)
```

## Characters Handled

| Char | Source |
|------|--------|
| `UNICHAR(160)` | Non-breaking space — common in Excel/HTML copy-paste |
| `UNICHAR(9)` | Tab character |

## Usage

```c
// Clean category for grouping
Clean Category := NormalizeLabel(Sales[CategoryName])

// Safe lookup
Region Code := LOOKUPVALUE(
    Regions[Code],
    Regions[Name], NormalizeLabel(Sales[RegionName])
)
```

## Related

- [[function]]
- [[function]]
