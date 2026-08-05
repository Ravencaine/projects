---
created: 2026-08-02
updated: 2026-08-05
source: Power BI New User Defined Functions 10 Must-Have You'll Use in Every Report
note_type: function
tags: [dax, udf, ranking, top-n, group, power-bi]
---

# RankWithinCurrentGroup — Item Rank

Returns the rank of the current item within the current group context.

## Signature

```c
UDF RankWithinCurrentGroup =
    ( items : TABLE,
      score : AnyRef expr,
      order : STRING   // "DESC" or "ASC"
    ) => RANKX(withScore, [__Score], , order, Dense)
```

Dense ties: no rank gaps.

## Related

- [[top-n-within-group-udf-pattern]]
- [[topnwithincurrentgroup-udf]]
