---
created: 2026-08-05
updated: 2026-08-05
source: 10 Excel Data Cleaning Hacks That Save Hours Every Week (DigitalBYKewat)
note_type: atomic
tags: [excel, flash-fill, pattern, ctrl+e, text-extraction, automation]
---

# Flash Fill: Ctrl+E Pattern

Flash Fill (Ctrl+E) detects a pattern from one manually typed example and automatically fills the rest of the column — no formula needed.

## How It Works

1. Type the desired output in the first cell of an adjacent column
2. Press **Ctrl+E**
3. Excel analyses the input column, applies the pattern, and fills the rest

## Examples

### Last Name, First Name → Surname, Given Name

| Input | Output (type one manually, then Ctrl+E) |
|-------|----------------------------------------|
| John Smith | Smith, John |
| Emma Wilson | Wilson, Emma |
| Michael Brown | Brown, Michael |

### Extract Email Username

| Input | Output |
|-------|--------|
| john.smith@company.com | john.smith |
| emma.wilson@company.com | emma.wilson |

### Phone Formatting

| Input | Output |
|-------|--------|
| 9876543210 | (987) 654-3210 |

### Date Standardisation

| Input | Output |
|-------|--------|
| 01/04/2026 | 2026-04-01 |

## Limitations

| Limitation | Detail |
|-----------|--------|
| No formula | Flash Fill values don't update if input changes — they are static |
| Pattern ambiguity | Flash Fill fails if the pattern is unclear or inconsistent |
| Large datasets | Flash Fill works best with 100–10,000 rows; very large ranges may misfire |
| Must type the first example | Excel needs one manual entry to infer the pattern |

## When to Use

Use Flash Fill for one-off transformations where building a formula would take longer. For repeatable or formula-driven work, prefer `=LEFT()`, `=MID()`, `=TEXTSPLIT()` or Power Query instead.

## Related

- [[Text-to-Columns]] — Power Query / Excel alternative for splitting columns
- [[TRIM-CLEAN-Functions]] — often used before Flash Fill to clean the input first
