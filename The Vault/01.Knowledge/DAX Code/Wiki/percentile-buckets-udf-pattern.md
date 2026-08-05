---
created: 2026-08-02
source: Power BI New User Defined Functions 10 Must-Have You'll Use in Every Report
note_type: pattern
tags: [dax, udf, percentile, bucketing, binning, distribution, power-bi]
---

# Percentile Buckets UDF Pattern

Dynamic binning by percentile cutpoints. Bands and counts rebuild on every filter context change — ideal for risk amounts, response times, order values that shift over time.

## Architecture

Three-function chain:

```
PercentileBoundsCustom → computes Min / P1 / P2 / P3 / P4 / Max
BucketIndexFromBounds  → maps value → 0..5 band index
BucketLabelFromBounds  → maps value → human-readable "a – b" label
```

Wrapper binds the table once; measures call the wrapper.

## Usage

```c
Amount := SUM(aggregate_risk[amount])

// Quintile labels + sort index
Amount Bucket      := QuantileBucketLabel([Amount], TRUE, 0.2, 0.4, 0.6, 0.8)
Amount Bucket Index := QuantileBucketIndex([Amount], TRUE, 0.2, 0.4, 0.6, 0.8)

// Visual: Amount Bucket on rows, COUNTROWS on values
Risk Count := COUNTROWS(aggregate_risk)
```

Sort axis by `Amount Bucket Index` for correct ordering.

## Key Design Points

- `PERCENTILEX.INC` — inclusive percentile
- Zero-width space prefix (`UNICHAR(8203)`) forces text sort in bucket order without a separate sort column
- `includeZeroBlank: TRUE` → blanks/zeroes → "No Value" bucket (index 0)
- `ALL(aggregate_risk)` vs. `ALLSELECTED` — choose based on whether bucket boundaries should respect user filters

## Config

`// 🔧` — Change `aggregate_risk` to your table name. Adjust `q1..q4` cutpoints (e.g., `0.2, 0.4, 0.6, 0.8` for quintiles, `0.25, 0.5, 0.75` for quartiles).

## Related

- [[percentileboundscustom-udf]]
- [[bucketindexfrombounds-udf]]
- [[bucketlabelfrombounds-udf]]
