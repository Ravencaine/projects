---
created: 2026-08-02
updated: 2026-08-05
source: Dynamic Bin Analysis Using Percentile Bucketing in Power BI (PBIX Included!) 🎢.md
note_type: pattern
tags: [powerbi, dax, filter, allselected, bucket, percentile]
---

# Bucket Count and Total via FILTER + ALLSELECTED

Two DAX measures — `Bucket Count (Invoices)` and `Bucket Total Amount ($)` — that count and sum records falling within a given bucket's range, using FILTER over ALLSELECTED.

## Purpose

Feed the bar chart's Y-axis. Each measure computes its value for the current bucket row in the disconnected `Buckets` table by filtering `ALLSELECTED(Invoices)` to records whose amount falls between the bucket's min and max thresholds.

## Structure

```dax
Bucket Count (Invoices) :=
    VAR lo = [Bucket Min Amount]
    VAR hi = [Bucket Max Amount]
    RETURN
        COUNTROWS (
            FILTER (
                ALLSELECTED ( Invoices ),
                [Total Expense Amount] > lo && [Total Expense Amount] <= hi
            )
        )

Bucket Total Amount ($) :=
    VAR lo = [Bucket Min Amount]
    VAR hi = [Bucket Max Amount]
    RETURN
        SUMX (
            FILTER (
                ALLSELECTED ( Invoices ),
                [Total Expense Amount] > lo && [Total Expense Amount] <= hi
            ),
            Invoices[Amount]
        )
```

## How It Works

- `ALLSELECTED(Invoices)` preserves external filter context (slicers, page filters) while ignoring the bar chart's own axis.
- `FILTER(..., condition)` iterates over the filtered table and returns only rows where the amount falls within the bucket range.
- `COUNTROWS` / `SUMX` aggregate the filtered result.
- The bucket boundaries come from `Bucket Min Amount` / `Bucket Max Amount`, which are themselves driven by the current `Buckets[BucketIndex]` selection.

## Key Rules

- The `>` lo / `<= hi` pattern creates adjacent, non-overlapping bins (each record belongs to exactly one bucket).
- `ALLSELECTED` — not `ALL` — is critical: it keeps page-level slicer context active so the chart responds to user filters.

## Variations

- **Alternative metric:** Replace `SUMX(..., Invoices[Amount])` with any other numeric column to bucket by that measure.
- **Distinct count:** Replace `COUNTROWS` with `DISTINCTCOUNT(Invoices[InvoiceID])` if duplicates need to be deduplicated.

## Related

- [[quintile-bucket-min-max-amount]]
- [[dynamic-percentile-threshold-measures]]
- [[percentile-bucketing-concept]]
