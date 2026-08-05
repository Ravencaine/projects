---
created: 2026-08-02
updated: 2026-08-05
source: Power BI New User Defined Functions 10 Must-Have You'll Use in Every Report
note_type: function
tags: [dax, udf, bucket, percentile, distribution, power-bi]
---

# BucketIndexFromBounds — Bucket Band Index

Maps a numeric value to a band index (0–5) based on pre-computed percentile bounds. Used in the [[percentile-buckets-udf-pattern]].

## Signature

```c
UDF BucketIndexFromBounds =
    ( value : NUMERIC,
      minV : NUMERIC, p1 : NUMERIC, p2 : NUMERIC, p3 : NUMERIC, p4 : NUMERIC, maxV : NUMERIC,
      includeZeroBlank : BOOL
    ) => SWITCH(TRUE(),
        includeZeroBlank && (ISBLANK(value) || value = 0), 0,   // "No Value"
        value <= p1, 1,
        value <= p2, 2,
        value <= p3, 3,
        value <= p4, 4,
        5
      )
```

## Related

- [[bucketlabelfrombounds-udf]]
- [[percentile-buckets-udf-pattern]]
