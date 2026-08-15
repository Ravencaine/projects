---
created: 2026-08-05
updated: 2026-08-05
source: 10 Excel Data Cleaning Hacks That Save Hours Every Week (DigitalBYKewat)
note_type: atomic
tags: [excel, data-cleaning, checklist, workflow, routine, backup]
---

# 3-Minute Data Cleaning Checklist

A 7-step repeatable routine to clean any new file in 3 minutes — turning chaotic data cleaning into a consistent habit. Run before touching any formula, Pivot Table, or Power Query load.

## The 7 Steps

| Step | Action | Time |
|------|--------|------|
| **1. Backup** | Save an untouched copy of the original file | 10 sec |
| **2. TRIM spaces** | `=CLEAN(TRIM())` on all text columns | 30 sec |
| **3. Check duplicates** | Conditional Formatting → Duplicate Values | 30 sec |
| **4. Standardise** | `=PROPER()`/`UPPER()`/`LOWER()` on text; dates to ISO | 30 sec |
| **5. Highlight blanks** | Conditional Formatting → Blanks | 20 sec |
| **6. Convert to Table** | Ctrl+T on the cleaned range | 10 sec |
| **7. Verify totals** | Check row count, SUM, and a few pivot previews | 30 sec |

**Total: ~3 minutes**

## Why the Order Matters

1. **Backup first:** you need an untouched copy if something goes wrong
2. **TRIM before anything else:** spaces break VLOOKUP, merges, and duplicates
3. **Duplicates after TRIM:** TRIM may create new duplicates by normalising spaces
4. **Standardise after duplicates:** case/format fixes are cleaner once duplicates are resolved
5. **Highlight blanks after standardising:** blanks may appear or disappear after format changes
6. **Table after cleaning:** Table auto-expands the cleaned range, not the messy range
7. **Verify totals last:** confirm the cleaned data makes sense before publishing

## The Rule

> Never skip the backup. Everything else is fixable; the original file gone wrong is not.

## Related

- [[TRIM-CLEAN-Functions]] — step 2 detail
- [[Highlight-Duplicates-Conditional-Formatting]] — step 3 detail
- [[Excel-Table-Ctrl-T]] — step 6 detail
- [[Dashboard-Health-Checklist]] (Data Modeling) — equivalent 5-point pre-publish checklist for Power BI
