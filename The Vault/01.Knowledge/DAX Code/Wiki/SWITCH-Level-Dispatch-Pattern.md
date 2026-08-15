---
created: 2026-08-09
updated: 2026-08-09
source: "Dynamic formatting by hierarchy level with ISINSCOPE and ISATLEVEL.md"
note_type: pattern
tags: [dax, isinscope, isatlevel, switch, level-detection, conditional-formatting, dynamic-formatting, pattern]
---

# SWITCH-Level-Dispatch Pattern

**Type:** Pattern · **KB:** DAX Code · **Source:** [[Source-Dynamic-formatting-ISINSCOPE-ISATLEVEL]]

Apply different logic depending on which level of a hierarchy a cell currently belongs to. One SWITCH TRUE dispatch, one branch per level.

## Template

```dax
MeasureName =
SWITCH(
    TRUE,
    -- Most specific level first
    ISINSCOPE(Table[MostSpecificColumn]),
        <calculation for most specific level>,
    ISINSCOPE(Table[MidColumn]),
        <calculation for mid level>,
    ISINSCOPE(Table[LeastSpecificColumn]),
        <calculation for least specific level>
)
```

## Why most-specific-first ordering matters

When at the month level, ISINSCOPE returns TRUE for all parent levels too (Year Month Short = TRUE, Year Quarter = TRUE, Year = TRUE). Testing from most specific to least specific ensures the first match is the *actual* current level, not a parent.

## Per-level arithmetic is self-contained

Each branch is independent. Common per-level patterns:

| Level | Typical calculation | Example |
|-------|-------------------|---------|
| Leaf | Share of parent total | DIVIDE(value, CALCULATE(...REMOVEFILTERS(parent))) |
| Mid | Comparison to average | IF(value >= AVERAGEX(VALUES(...), measure), "green", "pink") |
| Root | Share of grand total | DIVIDE(value, CALCULATE(measure, REMOVEFILTERS(all))) |

## Works with both ISINSCOPE and ISATLEVEL

The dispatch pattern is identical — only the detection function changes:

| | ISINSCOPE (measure) | ISATLEVEL (visual calc) |
|--|--|--|
| Detection target | Model column path | Visual reference syntax |
| Navigation up hierarchy | CALCULATE + REMOVEFILTERS | COLLAPSE / COLLAPSEALL |
| Arithmetic location | Semantic model | Visual calculation |
| Reusability | Across all reports | Confined to one visual |

## Related

- [[ISINSCOPE-Per-Level-Conditional-Formatting]] — measure-based implementation
- [[ISATLEVEL-Visual-Calculation]] — visual calculation implementation
- [[SWITCH-Specificity-Ordering]] — why order matters
