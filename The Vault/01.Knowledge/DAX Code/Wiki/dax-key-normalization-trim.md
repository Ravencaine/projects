---
created: 2026-08-01
updated: 2026-08-02
source: "When a Simple Variance Measure Breaks Power BI Lessons from Cross-Fact DAX.md"
note_type: atomic
tags: [dax, key-normalization, trim, ltrim, leading-space, cross-system, data-quality]
---

# Key Normalization — Leading Spaces Break Cross-System Joins

## The Bug

One system stores job numbers as:
```
"23540"
```
Other system stores as:
```
"23540"
```
Looks identical. DAX comparison: **NOT EQUAL.**

Root cause: a leading space in one system:
```
" 23540"  ← leading space
```

DAX comparisons are **exact**. Invisible characters silently break logic.

## The Fix

```c
-- Remove leading spaces
LTRIM(Job_Number)

-- Remove leading + trailing spaces
TRIM(Job_Number)

-- Apply in the model itself (preferred)
-- Power Query: Transform → Trim
-- SQL source: RTRIM(LTRIM(Job_Number))
```

## What to Check When Cross-System Joins Fail

| Issue | Example | Fix |
|-------|---------|-----|
| Leading space | `" 121-23540"` | `LTRIM()` |
| Trailing space | `"121-23540 "` | `RTRIM()` |
| Both | `" 121-23540 "` | `TRIM()` |
| Non-breaking space | `"121-23540"` (char 160) | `SUBSTITUTE(..., UNICHAR(160), "")` |
| Different data types | `INT` vs `STRING` | `FORMAT()` or `VALUE()` |
| Case sensitivity | `"ABC"` vs `"abc"` | `UPPER()` / `LOWER()` |

## Rule: Normalize Keys at the Source

Do NOT rely on DAX to fix dirty keys. Clean them in Power Query or SQL ETL:
1. **Power Query:** Add Column → Format → Trim
2. **SQL:** `RTRIM(LTRIM(Column))`
3. **DAX only if unavoidable:** `TRIM()` in the measure

Cross-system comparisons fail surprisingly often. Normalize keys as a standard practice when joining systems.
