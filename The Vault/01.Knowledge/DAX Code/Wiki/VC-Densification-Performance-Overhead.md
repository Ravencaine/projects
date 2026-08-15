---
created: 2026-08-08
updated: 2026-08-08
source: "Analyzing the performance impact of visual calculations"
source_url: https://www.sqlbi.com/articles/analyzing-the-performance-impact-of-visual-calculations/
note_type: atomic
tags: [visual-calculations, densification, performance, dax, summarizecolumns]
---

# VC Densification Performance Overhead

Visual calculations require the DAX engine to **densify** the virtual table — adding rows for all combinations of row/column values, including cells where SUMMARIZECOLUMNS originally returned BLANK. This densification overhead grows with the size of the virtual table and is the primary cause of degraded performance in large reports.

<!-- one-line description: densification rebuilds the full cross-product of row/column values, including BLANK rows eliminated by SUMMARIZECOLUMNS — overhead is O(brands × years) or O(stores × products × years) -->

## Mechanism

### SUMMARIZECOLUMNS blank elimination

`SUMMARIZECOLUMNS` applies an optimisation: it does **not** return rows where all measures evaluate to BLANK. In a matrix with 11 brands and 10 years, the maximum possible cells is 110. If 10 of those cells are blank, SUMMARIZECOLUMNS returns only 100 rows.

### VC densification step

When a visual calculation is present, the engine must recreate those 10 blank rows so that `PREVIOUS`, `NEXT`, and other visual calculation functions can correctly navigate the full cross-product of rows and columns. This is because visual calculations can produce non-blank results in cells that would have been blank for the base measures.

> **Example:** A YoY% calculation returns `-10%` in a cell where the base measure was BLANK (no sales that year). SUMMARIZECOLUMNS would skip that row, but the VC needs it to know there was a prior column to compare against.

### Densification formula

```
Densified rows = (distinct values in ROWS axis) × (distinct values in COLUMNS axis)
```

In the Contoso large-table scenario:

```
67 stores × 2,517 products × 10 years = 1,686,390 densified rows
```

## Performance Numbers (Contoso, 23M Sales rows)

| Report type | Virtual table | Densified rows | Total time | SE time | FE time |
|---|---|---|---|---|---|
| Measure-based (small) | ~110 cells | 0 (no VC) | 13s | 12,614 ms | 426 ms |
| VC (small) | ~110 cells | ~110 | 6s | 457 ms | 67,914 ms |
| Measure-based (large) | 1,686,390 | 0 (no VC) | 15.6s | 17,453 ms | 37.2% FE |
| VC (large) | 1,686,390 | 1,686,390 | 62s | 1,953 ms | 67,914 ms |

**Key insight:** The FE CPU time is roughly the same in all VC scenarios (~67s) — the densified row count barely affects it. The overhead is in the **materialization** of the densified table, which consumes both time and memory.

## Why Densification Is Unavoidable

Measure-based reports compute only what is visible. If a matrix row is collapsed, its children are not computed. Visual calculations **must materialize the full densified table at the leaf level** regardless of the visual's expansion state, because the VC expression must be able to reference any cell.

## When Densification Is Negligible

Densification overhead is negligible when the virtual table has fewer than ~10,000 rows. In this range the FE can process the densified table quickly enough that the PREVIOUS() benefit (no repeated SE queries) outweighs the densification cost.

## Related

- [[VC-vs-Measure-Performance-Decision]] — decision framework using virtual table size as the key metric
- [[SUMMARIZECOLUMNS-Blank-Elimination-VC-Densification]] — the interaction between blank elimination and densification
- [[PREVIOUS-YoY-VC-Pattern]] — pattern that benefits from VCs on small tables
- [[Source-Analyzing-Visual-Calculations-Performance]] — source article with screenshots and server timings
