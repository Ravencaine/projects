---
created: 2026-08-02
updated: 2026-08-05
source: Power BI New User Defined Functions 10 Must-Have You'll Use in Every Report
note_type: function
tags: [dax, udf, top-n, ranking, group, power-bi]
---

# TopNWithinCurrentGroup — Top-N Items Table

Returns a table of the top N items ranked by a score measure, scoped to the current group context.

## Signature

```c
UDF TopNWithinCurrentGroup =
    ( items : TABLE,
      score : AnyRef expr,
      n : INT64,
      order : STRING   // "DESC" (highest) or "ASC" (lowest)
    ) => TOPN(n, withScore, [__Score], order)
```

## Related

- [[top-n-within-group-udf-pattern]]
- [[rankwithincurrentgroup-udf]]
