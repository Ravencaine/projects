---
created: 2026-07-30
updated: 2026-08-02
source: Dynamic Ranking in DAX How I Built a Top 5 Dashboard That Actually Worked.md
note_type: reference
tags: [dax, ranking, top-n, reference, rankx]
---

# Dynamic Ranking in DAX — Quick Reference

Core patterns for building Top N leaderboards that respond correctly to slicer interactions.

## Pattern Map

```
RANKX ( ALL ( column ), measure )
                    ↓
              Rank Measure
                    ↓
IF ( rank <= N, measure, BLANK() )
                    ↓
              Top N Display
```

## Key Formulas

### 1. Basic Global Rank

```dax
Rank = RANKX ( ALL ( Table[Column] ), [Measure], , DESC )
```

Ranks within ALL = ignores all external filters (static ranking universe).

### 2. Filter-Aware Rank (ALLSELECTED)

```dax
Rank Filtered = RANKX ( ALLSELECTED ( Table[Column] ), [Measure], , DESC )
```

Ranks within the current visual/page-level filter context only.

### 3. Dynamic Top N

```dax
Top N Measure =
IF (
    [Rank] <= 5,
    [Measure],
    BLANK ()
)
```

### 4. User-Driven N (Parameter Table)

```dax
-- Parameter table: single-column integer table, no model relationship
Selected TopN = SELECTEDVALUE ( TopN[TopN], 5 )

Top N Dynamic =
IF (
    [Rank] <= [Selected TopN],
    [Measure],
    BLANK ()
)
```

### 5. RANKX + VAR (Performance)

```dax
Rank Optimized =
VAR RankSet = ALL ( Table[Column] )
VAR M = [Measure]
RETURN
    RANKX ( RankSet, M, , DESC )
```

### 6. Top N + Others

```dax
TopNvsOthers =
VAR TopNSales = CALCULATE ( [Measure], FILTER ( ALL ( Table[Column] ), [Rank] <= [Selected TopN] ) )
VAR Others = [Measure] - TopNSales
RETURN
    UNION (
        ROW ( "Group", "Top " & [Selected TopN], "Value", TopNSales ),
        ROW ( "Group", "Others",           "Value", Others )
    )
```

## ALL vs ALLSELECTED

| Function | Ranking Universe | Use When |
|----------|-----------------|----------|
| `ALL( col )` | Full column, ignores all filters | Global leaderboard — ignore user slicers |
| `ALLSELECTED( col )` | Column within current visual/page context | Rankings that respond to slicers |
| `REMOVEFILTERS( col )` | Same as ALL | Modern DAX syntax; preferred in new models |

## Common Errors

| Symptom | Cause | Fix |
|---------|-------|-----|
| All rows show rank 1 | Rank measure used inside its own table | Rank must be a separate measure, not a calculated column referencing itself |
| Ranks shift when adding a slicer | ALL used instead of ALLSELECTED | Change `ALL( col )` → `ALLSELECTED( col )` |
| Slow visual refresh | Expensive measure in RANKX expression | Wrap in VAR to cache result |
| Ties at same rank, next rank skipped | RANKX default ties behavior | Add tie-breaker as third argument: `RANKX( ..., expression, BREAK_EVALUATION(...) )` |

## Related

- [[dynamic-top-n-ranking-pattern]] — full pattern documentation
- [[top-n-parameter-slicer-pattern]] — parameter table + SELECTEDVALUE
- [[rankx-var-performance-pattern]] — VAR caching for large datasets
- [[top-n-others-union-pattern]] — Top N + Others aggregate bar
