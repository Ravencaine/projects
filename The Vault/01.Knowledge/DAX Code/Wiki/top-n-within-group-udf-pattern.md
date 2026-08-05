---
created: 2026-08-02
source: Power BI New User Defined Functions 10 Must-Have You'll Use in Every Report
note_type: pattern
tags: [dax, udf, top-n, ranking, group, power-bi]
---

# Top-N Within Group UDF Pattern

Replace one-off "Top X per Y" measures with a reusable pattern. Ranks items inside the current group context and returns either a filtered table or a rank you can filter on.

## Two-Function Pair

```
TopNWithinCurrentGroup → returns a table of the top N items
RankWithinCurrentGroup → returns a rank number (1 = best)
```

Both take: `( items : TABLE, score : AnyRef expr, n/order : ... )`

## Usage

**Scenario:** "Top 3 Instructors per Category," ranked by Total Reviews.

```c
Total Reviews := SUM('Reviews'[ReviewCount])

// Visual filter: keep only Top 3
Is Top 3 Instructor :=
VAR t = TopNWithinCurrentGroup(
    VALUES('Instructor'[Instructor]),  // items
    [Total Reviews],                   // score
    3,                                // n
    "DESC"                            // order
)
RETURN IF(
    CONTAINS(t, 'Instructor'[Instructor], SELECTEDVALUE('Instructor'[Instructor])),
    1
)
```

Put **Category** on rows, **Instructor** in a table, add `Is Top 3 Instructor = 1` as a **visual filter**.

## Key Design Points

- `items : TABLE` — usually `VALUES('Table'[Item])` so filters propagate
- Group context determined by visual layout / slicers, not hard-coded in the UDF
- `RANKX` with `Dense` ties — no rank gaps

## Related

- [[topnwithincurrentgroup-udf]]
- [[rankwithincurrentgroup-udf]]
