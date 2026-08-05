---
created: 2026-08-02
source: Power BI New User Defined Functions 10 Must-Have You'll Use in Every Report
note_type: function
tags: [dax, udf, percentile, distribution, power-bi]
---

# PercentileBoundsCustom — Dynamic Percentile Cutpoints

Computes Min / P1 / P2 / P3 / P4 / Max for any measure over a given table. Core of the [[percentile-buckets-udf-pattern]].

## Signature

```c
UDF PercentileBoundsCustom =
    ( measureExpr : AnyRef expr,
      wholeTable  : TABLE,
      q1 : NUMERIC, q2 : NUMERIC, q3 : NUMERIC, q4 : NUMERIC
    ) => ROW(
        "Min",  vMin,
        "P1",   p1,
        "P2",   p2,
        "P3",   p3,
        "P4",   p4,
        "Max",  vMax
      )
```

Returns a single-row table accessed via `B[Min]`, `B[P1]`, etc.

## Config

`// 🔧` — Change `wholeTable` to your data table. Use `ALL()` for absolute boundaries or `ALLSELECTED()` for filter-aware boundaries.

## Related

- [[percentile-buckets-udf-pattern]]
- [[bucketindexfrombounds-udf]]
