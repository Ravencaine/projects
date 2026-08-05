---
created: 2026-08-02
updated: 2026-08-05
source: Dynamic Bin Analysis Using Percentile Bucketing in Power BI (PBIX Included!) 🎢.md
note_type: source
tags: [powerbi, dax, percentile, bucketing, tutorial]
---

# Source: Dynamic Bin Analysis Using Percentile Bucketing in Power BI (PBIX Included!)

> Author: Isabelle Bittar
> Published: 2025-10-19
> URL: https://medium.com/microsoft-power-bi/dynamic-bin-analysis-using-percentile-bucketing-in-power-bi-pbix-included-9109ec404b13

## Introduction

Fixed bins ("$0–10K", "$10K–25K") become meaningless when users drill into narrower slices. Percentile-based bins solve this: instead of hardcoded ranges, buckets are recalculated dynamically based on the actual distribution of the filtered data. Each bin represents an equal proportion of records — the dollar width adapts automatically.

## What is Percentile Bucketing?

Dividing a dataset into equally sized groups based on data distribution. Each bin holds the same *number* of records; the dollar range varies dynamically. The 20th percentile means 20% of records fall below that amount. The 50th percentile is the median.

Key advantage: when users filter data, percentiles are recomputed for that subset — bins always represent meaningful distribution ranges. Every bar represents the same proportion of the filtered dataset, enabling fair cross-segment comparison.

## Step 1: The Data

Single fact table `Expenses` with columns: `InvoiceID`, `InvoiceDate`, `Department`, `Category`, `Region`, `Vendor`, `CostCenter`, `Amount`.

Plus a disconnected `Buckets` calculated table with `BucketIndex` and `BucketPct` (one row per percentile bin).

## Step 2: Base and Percentile Threshold Measures

```c
[Total Expense Amount] = SUM ( Expenses[Amount] )

p20 Amount =
    PERCENTILEX.INC (
        ALLSELECTED ( Invoices ),
        [Total Expense Amount],
        0.20
    )

p40 Amount =
    PERCENTILEX.INC ( ALLSELECTED ( Invoices ), [Total Expense Amount], 0.40 )

p60 Amount =
    PERCENTILEX.INC ( ALLSELECTED ( Invoices ), [Total Expense Amount], 0.60 )

p80 Amount =
    PERCENTILEX.INC ( ALLSELECTED ( Invoices ), [Total Expense Amount], 0.80 )

p100 Amount =
    PERCENTILEX.INC ( ALLSELECTED ( Invoices ), [Total Expense Amount], 1.0 )

p0 Amount =
    PERCENTILEX.INC ( ALLSELECTED ( Invoices ), [Total Expense Amount], 0.0 )
```

### PERCENTILE.INC vs PERCENTILE.EXC

- `PERCENTILEX.INC`: Inclusive — 0th and 100th percentiles are defined (includes min and max values). Use when bins must span the full data range including extremes.
- `PERCENTILEX.EXC`: Exclusive — 0th and 100th percentiles are undefined; calculation is between extremes only.

## Bucket Boundary Measures

```c
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

Bucket Label =
    VAR lo = FORMAT([Bucket Min Amount], "$#,0")
    VAR hi = FORMAT([Bucket Max Amount], "$#,0")
    RETURN
        lo & " – " & hi
```

## Bucket Aggregation Measures

```c
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

## Step 3: Bar Chart Configuration

- **X-axis:** `Buckets[BucketPct]`
- **Y-axis:** `Bucket Total Amount ($)` or `Bucket Count (Invoices)`
- Sort by `Buckets[BucketIndex]` ascending.
- Turn off Y-axis.
- Assign `Bucket Label` to data labels.
- Assign `Bucket Total Amount ($)` to the Detail field for richer data labels.
- Apply `Bucket Color` via conditional formatting → Field value on data colors.

## Finishing Touches

- Sort bars by `Bucket Min Amount`.
- Apply accent colors using `Bucket Color` measure.
- Use a field parameter on X-axis to toggle between count vs. amount view.
- Add an informational tooltip explaining how the dynamic groupings work.
- Add a companion table visual to the left of the bar chart for bucket labels, with index column and headers hidden behind a shape.
- Integrate a periods selection (Last Week, Last Month, Last Year) using the Visual Explorer pattern.

## Bucket Color Measure

```c
_Color Primary  = "#3631F9"
_Color Accent 1 = "#7285FE"
_Color Accent 2 = "#E3E9F0"
_Color Accent 3 = "#E9EDF2"
_Color Accent 4 = "#BCC7D9"

Bucket Color =
    SWITCH ( [Bucket Index],
        5, [_Color Primary],
        4, [_Color Accent 1],
        3, [_Color Accent 3],
        2, [_Color Accent 2],
        1, [_Color Accent 4]
    )
```

## Ways to Extend

1. **User-selectable bucket count:** Field parameter toggling 5 vs 10 buckets (0.1 vs 0.2 increments).
2. **Rank-based tooltip:** Show "Top X% of spenders" via `PERCENTILERANKX.INC`.
3. **Outlier bucket:** Add "No Amount / Outlier" bucket for zero/null values or extreme transactions.
4. **Combine with anomaly detection:** Track outliers within percentile buckets using Python Isolation Forest in Power Query.

## PBIX Download

Available at: [[dynamic-percentile-threshold-measures]]
