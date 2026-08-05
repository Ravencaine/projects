---
created: 2026-07-30
updated: 2026-08-02
source: I Analyzed 5,000 DAX Measures. Here Are The 5 Patterns That Kill Performance.md
source_url: https://medium.com/towards-artificial-intelligence/i-analyzed-5-000-dax-measures-here-are-the-5-patterns-that-kill-performance-ea259894ba0f
note_type: source
tags: [dax, performance, benchmarking, audit]
---

# Tejwani — 5,000 DAX Measures Performance Analysis

Empirical study of 5,247 DAX measures across 89 production reports. Found 78% of slow measures share 5 patterns; average 14x speedup after fixing.

> **Type:** article
> **Author:** Gulab Chand Tejwani
> **Published:** 2026-02-16
> **URL:** https://medium.com/towards-artificial-intelligence/i-analyzed-5-000-dax-measures-here-are-the-5-patterns-that-kill-performance-ea259894ba0f
> **Routed to:** DAX Code

## Summary

Tejwani analyzed 5,247 DAX measures across 89 production Power BI reports over 4 weeks. Out of 892 slow measures (>2s), 697 (78%) shared 5 patterns. The study used DAX Studio (XMLA endpoint), Performance Analyzer, and Server Timings. Average slow measure time: 8.4s → 0.6s after fix (14x improvement). One measure dropped from 18.3s to 0.3s using DATESYTD instead of FILTER(ALL()).

## Key Claims

- 78% of slow measures share just 5 patterns
- Pattern 1 (unnecessary iterators): 41% of slow measures, avg 19.5x speedup
- Pattern 2 (calculated columns): 28%, reduces refresh time by 67%
- Pattern 3 (RELATED in iterators): 19%, avg 14.9x speedup
- Pattern 4 (nested CALCULATE): 23%, avg 12.1x speedup; with SAMEPERIODLASTYEAR: 56.5x
- Pattern 5 (ALL vs REMOVEFILTERS): 31%, avg 11.6x speedup
- "Slow" defined as >2s in Performance Analyzer or >1s in DAX Studio

## Notable Details

- Study model: 8.2M rows in Sales table
- REMOVEFILTERS() does not materialize the table; ALL() materializes AND returns the table
- The 5-measure audit: 10min identify + 5min per measure check + 10min per measure fix = ~1hr for 5 measures
- Cancelled $180K Premium capacity upgrade after optimizing existing measures

## Extracted Notes

Links to notes derived from this source:

- [[5-dax-performance-patterns-reference]] — `reference` — The 5 patterns overview with benchmarks
- [[unnecessary-iterator-pattern]] — `pattern` — SUMX/AVERAGEX/COUNTX on single columns
- [[calculated-columns-vs-measures-performance]] — `pattern` — when to use each, tradeoffs
- [[related-in-iterators-performance]] — `pattern` — RELATED() inside iterators causes cross-joins
- [[nested-calculate-direct-filters-pattern]] — `pattern` — nested CALCULATE + ALL(FILTER)) → direct filters
- [[all-vs-removefilters-performance]] — `pattern` — ALL() materializes; REMOVEFILTERS() only removes
- [[dax-measure-audit-workflow]] — `workflow` — 3-step audit framework
- [[iterator-cost-principle]] — `atomic` — iterators are powerful but expensive; use only when computing something not in the table
- [[Author-Gulab-Chand-Tejwani]] — author note

## Metadata

| Field | Value |
|-------|-------|
| Source file | I Analyzed 5,000 DAX Measures. Here Are The 5 Patterns That Kill Performance.md |
| Ingestion date | 2026-07-30 |
| Word count | ~1,500 |
