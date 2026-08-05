---
created: 2026-08-02
source: Dynamic Bin Analysis Using Percentile Bucketing in Power BI (PBIX Included!) 🎢.md
note_type: workflow
tags: [powerbi, dax, percentile, bucket, bar-chart, visualization]
---

# Dynamic Bin Bar Chart from Percentile Buckets

Build a bar chart that displays invoice counts or amounts across dynamically recalculated percentile buckets — adapting to user filter context in real time.

## Prerequisites

- A fact table with a numeric column to bucket (e.g. `Expenses[Amount]`).
- A disconnected `Buckets` table with `BucketIndex` and `BucketPct` columns (one row per bin).

## Steps

### 1. Create the bucket table

Create a calculated table (Modeling → New Table) with one row per percentile bin:

```
Buckets =
DATATABLE(
    "BucketIndex", INTEGER,
    "BucketPct", STRING,
    {
        { 1, "0–20%" },
        { 2, "20–40%" },
        { 3, "40–60%" },
        { 4, "60–80%" },
        { 5, "80–100%" }
    }
)
```

### 2. Create base and percentile threshold measures

- `[Total Expense Amount] = SUM(Expenses[Amount])`
- `p0/p20/p40/p60/p80/p100 Amount` using `PERCENTILEX.INC(ALLSELECTED(...), ..., k)`

### 3. Create bucket boundary measures

- `Bucket Min Amount` — SWITCH on `SELECTEDVALUE(Buckets[BucketIndex])` returning the lower bound.
- `Bucket Max Amount` — SWITCH returning the upper bound.
- `Bucket Label = FORMAT(Min) & " – " & FORMAT(Max)`

### 4. Create aggregation measures

- `Bucket Count (Invoices)` — `COUNTROWS(FILTER(ALLSELECTED(Invoices), amount > lo && amount <= hi))`
- `Bucket Total Amount ($)` — `SUMX(FILTER(ALLSELECTED(Invoices), ...), Invoices[Amount])`

### 5. Build the bar chart

- **X-axis (or legend):** `Buckets[BucketPct]`
- **Y-axis:** `Bucket Count (Invoices)` or `Bucket Total Amount ($)`
- Sort the visual by `Buckets[BucketIndex]` ascending.
- Turn off the Y-axis (values and title).

### 6. Configure labels and formatting

- Assign `Bucket Label` to data labels.
- Assign `Bucket Total Amount ($)` to the Detail field for data label context.
- Apply `Bucket Color` via conditional formatting → Field value on data colors.

### 7. Add slicers

Add slicers for Department, Category, Region, Period, or any relevant filter. Verify that bucket boundaries recalculate when slicers change.

## Variations

- **User-selectable bucket count:** Replace the static Buckets table with a field parameter (5 or 10 buckets), adjusting PERCENTILEX calls to 0.1 increments.
- **Rank-based tooltip:** Show "Top X% of spenders" in tooltips using `PERCENTILERANKX.INC`.
- **Outlier bucket:** Add an extra "No Amount / Outlier" bucket catching zero or null amounts.
- **Toggle between count and amount:** Use a field parameter on the Y-axis to switch between `Bucket Count` and `Bucket Total Amount`.

## Related

- [[percentile-bucketing-concept]]
- [[dynamic-percentile-threshold-measures]]
- [[quintile-bucket-min-max-amount]]
- [[bucket-count-total-via-filter-allselected]]
- [[bucket-color-by-index]]
