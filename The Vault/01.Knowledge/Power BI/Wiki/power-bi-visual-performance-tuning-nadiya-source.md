---
created: 2026-08-01
updated: 2026-08-02
source: "How I Reduced a Power BI Visual from 23 Seconds to 8 Seconds A Real Performance Tuning Case Study.md"
source_url: "https://medium.com/@AIAnalyticsWithNadiya/how-i-reduced-a-power-bi-visual-from-23-seconds-to-8-seconds-a-real-performance-tuning-case-study-21538321ca7f"
note_type: source
tags: [power-bi, performance-tuning, visual-settings, dax-optimization, case-study]
---

# Power BI Visual Performance Tuning: 23s → 8s

> **Type:** article / case study
> **Author:** Nadiya Modi
> **Published:** 2026-07-27
> **URL:** https://medium.com/@AIAnalyticsWithNadiya/how-i-reduced-a-power-bi-visual-from-23-seconds-to-8-seconds-a-real-performance-tuning-case-study-21538321ca7f
> **Routed to:** Power BI

## Summary

A real production case study where an Account Table visual loaded in 23.6 seconds. The investigation used Performance Analyzer and DAX Studio to isolate the bottleneck: **"Show items with no data"** was enabled on a grouping field, forcing Power BI to generate thousands of cross-join queries. Disabling the setting reduced load time to 8.7 seconds — a ~63% improvement — with no DAX or data model changes.

## The Problem

- One visual (Account Table) took **23.6 seconds** to load
- The rest of the dashboard was responsive
- The visual had a grouping field with **"Show items with no data"** enabled

## Performance Breakdown (Before Fix)

| Metric | Value |
|--------|-------|
| Total Visual Load | 23,599 ms |
| DAX Query | 23,300 ms |
| Visual Rendering | Negligible |

## DAX Studio Findings (Before Fix)

| Metric | Value |
|--------|-------|
| Formula Engine share | 88.7% of execution time |
| Storage Engine queries | 1,033 |
| Rows returned | 17 |

1,033 Storage Engine queries for 17 rows is a clear signal of unnecessary cross-joins and repeated evaluation.

## The Root Cause

Power BI's **"Show items with no data"** setting (displayed as `__DS0PrimaryShowAllCompat` in the generated DAX) causes the engine to:
- Generate every possible category combination
- Perform unnecessary cross-joins across all grouping fields
- Evaluate every measure for blank values across all combinations
- Repeat those calculations thousands of times

## The Fix

Disabled **"Show items with no data"** on the affected grouping field in the visual field well.

## Results (After Fix)

| Metric | Before | After |
|--------|--------|-------|
| Total Visual Load | 23,599 ms | 8,741 ms |
| Performance Improvement | — | ~63% faster |

No DAX rewrites. No data model changes. One visual setting.

## The 5-Step Diagnostic Workflow

1. **Measure** the problem — Performance Analyzer in Power BI Desktop
2. **Isolate** the bottleneck — narrow to DAX vs rendering vs data model
3. **Analyze** the evidence — DAX Studio Server Timings + Query Plan
4. **Identify** the root cause — examine the generated DAX query
5. **Validate** the improvement — repeat diagnostics after the fix

## Key Takeaways

- ✅ Measure before optimising — never guess
- ✅ Let data guide the investigation — not assumptions
- ✅ Don't assume DAX is always the problem
- ✅ Read the generated DAX query — it reveals hidden auto-generated behaviour
- ✅ Small configuration changes can produce significant performance improvements

## Extracted Notes

- [[show-items-with-no-data-performance-impact]] — `atomic` — how the setting causes cross-joins and 1000+ SE queries
- [[ds0-primary-showallcompat-auto-generated-dax]] — `atomic` — what the generated DAX signature reveals
- [[power-bi-performance-diagnosis-workflow]] — `pattern` — 5-step structured diagnostic workflow
- [[performance-tuning-assumption-gotcha]] — `gotcha` — DAX/SQL/data model assumed first; visual settings rarely suspected

## Metadata

| Field | Value |
|-------|-------|
| Source file | How I Reduced a Power BI Visual from 23 Seconds to 8 Seconds A Real Performance Tuning Case Study.md |
| Ingestion date | 2026-08-01 |
| Word count | ~215 |
