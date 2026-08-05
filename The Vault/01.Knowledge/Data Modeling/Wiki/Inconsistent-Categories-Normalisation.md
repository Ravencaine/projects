---
created: 2026-08-05
source: 5 Data Cleaning Mistakes That Ruin Your Dashboard (DigitalBYKewat)
note_type: atomic
tags: [data-cleaning, text-cleaning, trim, case-normalisation, dimension-table, data-quality]
---

# Inconsistent Categories: Normalisation

The same entity entered four different ways (`Mumbai`, `MUMBAI`, `Mumbai City`, `Bombay`) becomes four separate bars on a bar chart — splitting a single market into four phantom segments.

## The Problem

Text inconsistencies silently split aggregation groups. A bar chart that should show one large bar for Mumbai shows four small bars instead.

## Causes

- Manual data entry with no standard
- Legacy naming conventions (Bombay → Mumbai)
- Different case conventions across source systems
- Ghost characters (leading/trailing spaces, non-breaking spaces) invisible to the eye

## Power Query Fixes

### Remove invisible characters

```m
Text.Clean(Text.Trim([City]))
```

`Text.Trim` removes leading/trailing spaces. `Text.Clean` removes non-printable characters (newlines, carriage returns, BOM characters).

### Normalise case

| Transform | Use when |
|-----------|----------|
| **UPPERCASE** (`Text.Upper`) | All values should be uppercase |
| **Proper Case** (`Text.Proper`) | Each word capitalised |
| **Trim + Lower** | Normalise everything to lowercase, then re-case as needed |

### Map legacy names with a dimension table

Create a lookup table:

| Legacy Name | Canonical Name |
|-------------|---------------|
| Mumbai | Mumbai |
| MUMBAI | Mumbai |
| Mumbai City | Mumbai |
| Bombay | Mumbai |

Then merge the dimension table with the fact table on the legacy column.

## Prevention

- Enforce dropdown lists at data entry — no free-text entry for standard categories
- Document canonical category values in a data dictionary
- Run a `DISTINCTCOUNT` vs `COUNTROWS` check on category columns — a large gap indicates inconsistent naming

## Related

- [[Duplicate-Records-Detection-Removal]]
- [[Dashboard-Health-Checklist]]
