---
created: 2026-08-08
updated: 2026-08-08
source: "Analyzing the performance impact of visual calculations"
source_url: https://www.sqlbi.com/articles/analyzing-the-performance-impact-of-visual-calculations/
note_type: snippet
tags: [visual-calculations, performance, benchmark, dax, server-timings, distinctcount]
---

# VC vs Measure Benchmark Snippet (Contoso 23M-row model)

Specific benchmark numbers from the SQLBI article comparing visual calculation vs model measure performance on the Contoso model with 23 million rows in Sales. Use these numbers as reference points for estimating your own VC vs measure tradeoffs.

<!-- one-line description: benchmark — YoY% with DISTINCTCOUNT: VC 6s vs Measure 13s (small table); VC 62s vs Measure 15.6s (large table with 1.69M virtual rows) -->

## Scenario 1 — Small Virtual Table (~110 rows)

**Measure:** `# Customers` (DISTINCTCOUNT) + YoY% via SAMEPERIODLASTYEAR
**Visual Calculation:** Same base measure + YoY% via PREVIOUS(COLUMNS)
**Context:** 11 brands × 10 years

| Approach | Total time | SE CPU | FE CPU | SE% | FE% |
|---|---|---|---|---|---|
| Model Measure | 13,040 ms | 12,614 ms | 426 ms | 96.7% | 3.3% |
| Visual Calculation | 6,000 ms | 457 ms | ~5,543 ms | 0.7% | 99.3% |

**Winner: Visual Calculation:** 2× faster. PREVIOUS reads from the precomputed virtual table; no repeated SE scans per year.

## Scenario 2 — Large Virtual Table (1,686,390 rows)

**Measure:** `Sales Amount` + YoY% via SAMEPERIODLASTYEAR
**Visual Calculation:** Same base measure + YoY% via PREVIOUS(COLUMNS)
**Context:** 67 stores × 2,517 products × 10 years

| Approach | Total time | SE CPU | FE CPU | Key observation |
|---|---|---|---|---|
| Model Measure | 15,600 ms | 17,453 ms | ~5,800 ms | 37.2% FE; collapsed rows not computed |
| Visual Calculation | 62,000 ms | 1,953 ms | ~67,914 ms | 99.3% FE; full densified table materialised |

**Key FE row counts (measure-based, large table):**
- Main SE scan: 1,318,524 rows
- SAMEPERIODLASTYEAR FE step: 16,488,828 rows processed

**Key FE row counts (VC, large table):**
- Single SE scan: 1,318,524 rows
- All subsequent calculation: ~1.3M rows in FE

**Winner: Model Measure:** 4× faster. Densification overhead dominates at this scale.

## Rule of Thumb

```
Small table (< ~10,000 densified rows):   VC is faster
Large table (> ~10,000 densified rows):   Measure is faster
```

The 10K cutoff is approximate — test both approaches for virtual tables in the 5K–20K range.

## Related

- [[VC-vs-Measure-Performance-Decision]] — decision framework using these benchmarks
- [[VC-Densification-Performance-Overhead]] — why the large-table result is 4× slower for VCs
- [[SUMMARIZECOLUMNS-Blank-Elimination-VC-Densification]] — the blank elimination conflict driving the difference
- [[PREVIOUS-YoY-VC-Pattern]] — the VC pattern used in the small-table benchmark
- [[Source-Analyzing-Visual-Calculations-Performance]] — source article with server timing screenshots
