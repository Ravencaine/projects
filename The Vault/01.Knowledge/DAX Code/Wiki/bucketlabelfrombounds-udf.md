---
created: 2026-08-02
source: Power BI New User Defined Functions 10 Must-Have You'll Use in Every Report
note_type: function
tags: [dax, udf, bucket, percentile, distribution, label, text, power-bi]
---

# BucketLabelFromBounds — Bucket Label Generator

Builds a human-readable `"a – b"` range label from percentile bounds. Prefixes zero-width spaces so the text sorts correctly in visual axes.

## Signature

```c
UDF BucketLabelFromBounds =
    ( value : NUMERIC,
      minV : NUMERIC, p1 : NUMERIC, p2 : NUMERIC, p3 : NUMERIC, p4 : NUMERIC, maxV : NUMERIC,
      includeZeroBlank : BOOL
    ) => REPT(UNICHAR(8203), band + 1) & label
```

Band → label mapping:

| Index | Label |
|-------|-------|
| 0 | "No Value" |
| 1 | `minV – p1` |
| 2 | `p1 – p2` |
| 3 | `p2 – p3` |
| 4 | `p3 – p4` |
| 5 | `p4 – maxV` |

Zero-width space prefix (`UNICHAR(8203)`) ensures alphabetical sort puts bands in the correct order without a separate sort column.

## Related

- [[bucketindexfrombounds-udf]]
- [[percentile-buckets-udf-pattern]]
