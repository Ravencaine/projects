---
created: 2026-08-05
source: 5 Data Cleaning Mistakes That Ruin Your Dashboard (DigitalBYKewat)
note_type: workflow
tags: [data-cleaning, pipeline, etl, power-query, data-quality, workflow]
---

# Data Cleaning Pipeline Flow

An 8-step ordered pipeline for cleaning raw data before loading into Power BI. Each step is sequential and should be applied in order.

## The Pipeline

```
Raw Data
  ↓
① Duplicate Check      — Remove or flag duplicate records
  ↓
② Missing Value Check  — Investigate, replace, or drop blanks
  ↓
③ Standardize Formats  — Dates to ISO, numbers to consistent precision
  ↓
④ Validate Categories  — Normalise text: Trim, Clean, Case, Lookup maps
  ↓
⑤ Review Outliers     — Check min/max, investigate extreme values
  ↓
Clean Dataset
  ↓
⑥ Power BI Dashboard  — Load clean data into the semantic model
  ↓
⑦ Reliable Decisions  — Trustworthy insights for stakeholders
```

## Step Details

| Step | Action | Tool |
|------|--------|------|
| ① Duplicate Check | Remove exact duplicates on key ID columns | Power Query: Remove Duplicates |
| ② Missing Value Check | Replace or drop based on context | Power Query: Replace Nulls, Fill Down/Up |
| ③ Standardize Formats | ISO dates, consistent number formats, locale | Power Query: Change Type + Locale |
| ④ Validate Categories | Trim, clean, case-normalise, dimension map | Power Query: Text.Transform, Merge |
| ⑤ Review Outliers | Min/max QA, investigate extremes | Power BI Data view, DAX MEDIAN |
| ⑥ Clean Dataset | Load into the semantic model | Power Query: Close & Apply |
| ⑦ Dashboard | Build visuals on clean data | Power BI |

## Key Principle

**Order matters.** Remove duplicates before calculating aggregates. Standardise formats before building relationships. Validate categories before creating slicers.

## Related

- [[Duplicate-Records-Detection-Removal]]
- [[Inconsistent-Date-Formats-ISO]]
- [[Missing-Values-Handling-Strategy]]
- [[Inconsistent-Categories-Normalisation]]
- [[Ignoring-Outliers-Detection-Action]]
- [[Dashboard-Health-Checklist]]
