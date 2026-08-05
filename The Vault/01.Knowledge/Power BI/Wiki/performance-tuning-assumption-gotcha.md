---
created: 2026-08-01
updated: 2026-08-02
source: "How I Reduced a Power BI Visual from 23 Seconds to 8 Seconds A Real Performance Tuning Case Study.md"
note_type: gotcha
tags: [power-bi, performance-tuning, dax, data-model, assumption, visual-settings, diagnosis]
---

# Performance Tuning: DAX Assumed First, Visual Settings Overlooked

When a Power BI report is slow, the first suspects are almost always DAX complexity, SQL queries, or the data model. The most impactful bottleneck in this case study was none of those — it was a single visual field well setting.

## The Pattern

Performance issues trigger predictable first-response assumptions:

| Rank | Assumed Cause | How Often True |
|------|--------------|----------------|
| 1 | Bad DAX measures | Sometimes |
| 2 | Inefficient SQL / data source | Sometimes |
| 3 | Large data model | Sometimes |
| 4 | Visual configuration settings | Rarely (until it's this) |

This ordering causes developers to spend hours optimizing DAX, tuning SQL, or redesigning the data model — when the real cause is a checkbox in the visual field well.

## Why This Gotcha Matters

In this case study:
- **23 seconds of the 23.6-second load** was in DAX Query time
- **88.7% Formula Engine**: looked like a DAX problem
- But: **1,033 Storage Engine queries for 17 rows**: a cross-join signature
- Root cause: "Show items with no data" on a grouping field

The symptoms pointed at DAX. The root cause was a visual setting.

## Lesson

**Measure before optimising. Let the data guide the investigation.**

The structured workflow — Performance Analyzer → DAX Studio → generated DAX query — revealed the culprit in minutes. Assumptions based on symptoms would have led to a day of DAX refactoring for zero gain.

## Related

- [[show-items-with-no-data-performance-impact]] — the specific setting that defeats the assumption
- [[ds0-primary-showallcompat-auto-generated-dax]] — the signature to look for
- [[power-bi-performance-diagnosis-workflow]] — structured workflow that avoids this gotcha
