---
created: 2026-08-02
updated: 2026-08-05
source: Dynamic Bin Analysis Using Percentile Bucketing in Power BI (PBIX Included!) 🎢.md
note_type: pattern
tags: [powerbi, dax, switch, bucket, percentile]
---

# Quintile Bucket Min/Max Amount

Two DAX measures — `Bucket Min Amount` and `Bucket Max Amount` — that map a disconnected `Buckets[BucketIndex]` table row to the corresponding lower and upper percentile thresholds.

## Purpose

Each row in the `Buckets` table represents one percentile bin (index 1–5 for quintiles). These measures return the dollar value at that bin's lower and upper boundary by looking up the precomputed percentile threshold measures.

## Structure

```dax
Bucket Min Amount =
VAR idx = SELECTEDVALUE ( Buckets[BucketIndex] )
RETURN
    SWITCH (
        TRUE(),
        idx = 1, [p0 Amount],
        idx = 2, [p20 Amount],
        idx = 3, [p40 Amount],
        idx = 4, [p60 Amount],
        idx = 5, [p80 Amount]
    )

Bucket Max Amount =
VAR idx = SELECTEDVALUE ( Buckets[BucketIndex] )
RETURN
    SWITCH (
        TRUE(),
        idx = 1, [p20 Amount],
        idx = 2, [p40 Amount],
        idx = 3, [p60 Amount],
        idx = 4, [p80 Amount],
        idx = 5, [p100 Amount]
    )
```

## How It Works

- `SELECTEDVALUE(Buckets[BucketIndex])` reads the current bucket row from the disconnected table.
- `SWITCH` maps the index to the correct percentile threshold (p0–p80 for min, p20–p100 for max).
- Buckets are adjacent: bin N's max = bin N+1's min, with no overlap or gap.

## Bucket Label (readable display value)

```dax
Bucket Label =
VAR lo = FORMAT([Bucket Min Amount], "$#,0")
VAR hi = FORMAT([Bucket Max Amount], "$#,0")
RETURN
    lo & " – " & hi
```

## Variations

- **More bins:** Add idx = 6, 7, ..., 10 for deciles; extend SWITCH branches accordingly.
- **Different measures:** Rename for different metrics (Quantity, Days, etc.).

## Related

- [[dynamic-percentile-threshold-measures]]
- [[bucket-count-total-via-filter-allselected]]
- [[percentile-bucketing-concept]]
