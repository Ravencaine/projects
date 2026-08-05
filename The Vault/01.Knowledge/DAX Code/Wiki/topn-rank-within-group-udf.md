---
created: 2026-08-02
source: Power BI's New User Defined Functions: 10 Must-Have You'll Use in Every Report
note_type: function
tags: [dax, udf, function, top-n, ranking, filter-context]
---

# TopNWithinCurrentGroup + RankWithinCurrentGroup — Dynamic Top-N Within Filter Context

Ranks or filters items within the current group context (e.g., Top 3 per category).

```dax
DEFINE
    FUNCTION TopNWithinCurrentGroup =
        ( items : TABLE, score : AnyRef expr, n : INT64, order : STRING ) =>
        VAR _ord = UPPER(order)
        VAR _withScore = ADDCOLUMNS(items,"__Score",CALCULATE(score))
        RETURN IF(_ord="ASC",
            TOPN(n,_withScore,[__Score],ASC),
            TOPN(n,_withScore,[__Score],DESC));

    FUNCTION RankWithinCurrentGroup =
        ( items : TABLE, score : AnyRef expr, order : STRING ) =>
        VAR _ord = UPPER(order)
        VAR _withScore = ADDCOLUMNS(items,"__Score",CALCULATE(score))
        RETURN IF(_ord="ASC",
            RANKX(_withScore,[__Score],,ASC,Dense),
            RANKX(_withScore,[__Score],,DESC,Dense))
```

**`TopNWithinCurrentGroup`:** returns a table of the top `n` items — use as a visual filter with `CONTAINS`.

**`RankWithinCurrentGroup`:** returns 1-based dense rank of the current item — filter on `<= N` to show top-N in visuals.

**Usage — Top 3 per Category:**
```dax
Is Top 3 Instructor =
VAR t = TopNWithinCurrentGroup(
    VALUES('Instructor'[Instructor]),
    [Total Reviews],
    3,
    "DESC"
)
RETURN IF(CONTAINS(t,'Instructor'[Instructor],SELECTEDVALUE('Instructor'[Instructor])),1)
```
Put `Is Top 3 Instructor = 1` as a visual filter.
