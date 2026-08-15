---
created: 2026-08-09
updated: 2026-08-09
source: "Dynamic formatting by hierarchy level with ISINSCOPE and ISATLEVEL.md"
note_type: pattern
tags: [dax, collapse, collapseall, visual-calculation, hierarchy-navigation, level-detection, pattern]
---

# COLLAPSE / COLLAPSEALL Hierarchy Navigation Pattern

**Type:** Pattern · **KB:** DAX Code · **Source:** [[Source-Dynamic-formatting-ISINSCOPE-ISATLEVEL]]

Navigate up a visual hierarchy from within a visual calculation using COLLAPSE and COLLAPSEALL. These replace CALCULATE + REMOVEFILTERS when working at the report layer instead of the semantic model layer.

## COLLAPSE — one level up

```dax
YearTotal = COLLAPSE([Sales Amount], [Year-Quarter-Month Quarter])
```

Collapses the visual by one level from the current cell to the specified parent level. Returns the measure value aggregated at that parent level.

## COLLAPSEALL — all the way to grand total

```dax
GrandTotal = COLLAPSEALL([Sales Amount], ROWS)
```

Collapses the entire visual to the grand total (top of the visual hierarchy). Analogous to `CALCULATE(measure, REMOVEFILTERS('Date'))` in a measure.

## Side-by-side comparison

| Semantic model layer | Visual calculation layer |
|---------------------|------------------------|
| `CALCULATE(m, REMOVEFILTERS('Date'), VALUES('Date'[Year]))` | `COLLAPSE([m], [Hierarchy Year])` |
| `CALCULATE(m, REMOVEFILTERS('Date'))` | `COLLAPSEALL([m], ROWS)` |
| `AVERAGEX(VALUES('Date'[Quarter]), m)` | `CALCULATE(AVERAGEX(ROWS, [m]))` |
| Uses model column paths | Uses visual reference syntax |

## ROWS axis

`ROWS` is the visual axis that corresponds to row hierarchy levels in a matrix. For column hierarchies, use `COLUMNS`.

## Inverse function

EXPANDALL is the inverse of COLLAPSEALL — expands from a collapsed level back down. COLLAPSE is the inverse of EXPAND.

## Related

- [[ISATLEVEL-Visual-Calculation]] — practical use of COLLAPSE/COLLAPSEALL
- [[ISINSCOPE-Per-Level-Conditional-Formatting]] — measure-layer equivalent using CALCULATE
