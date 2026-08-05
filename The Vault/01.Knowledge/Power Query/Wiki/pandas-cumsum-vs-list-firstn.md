---
created: 2026-08-01
updated: 2026-08-02
source: "Unlocking Python Inside Power BI How I Solved the Cumulative Value Challenge (and What I Learned Along the Way).md"
note_type: atomic
tags: [power-query, python, pandas, cumsum, performance, intermediate]
---

# pandas cumsum() vs List.FirstN(): Cumulative Sums in Power Query

Power Query's M language has `List.FirstN()` for cumulative operations, but it degrades badly at scale. `pandas` `cumsum()` with `groupby()` is the O(n) alternative.

## The M Language Problem: List.FirstN() Is O(n²)

The M equivalent of a cumulative sum uses `List.FirstN()` inside a custom column:

```m
List.Sum(
    List.FirstN(
        #"Added Index"[Value],
        [Index]
    )
)
```

For each row, `List.FirstN` re-reads the entire list from the start. On n rows, this is O(n²) — every row resums all preceding rows. On 100K rows, that's ~10 billion operations. Refresh times go from seconds to minutes.

## The pandas Solution: cumsum() Is O(n)

```python
import pandas as pd

dataset = dataset.sort_values(["Version", "EU#", "MonthNum"])

dataset["Cumulative Value"] = (
    dataset.groupby(["Version", "EU#"])["Value"]
    .cumsum()
)
```

`groupby()` partitions the DataFrame — `cumsum()` is vectorised and runs in a single pass = O(n). The groupby ensures the cumulative sum **resets for each unique Version × EU# combination**.

## Why groupby() Is Essential

Without `groupby()`, `cumsum()` would accumulate across the entire dataset — not per version or business unit. The `groupby(["Version", "EU#"])` is what makes it work correctly for the multi-dimensional cumulative requirement.

```python
# Correct: resets per group
.groupby(["Version", "EU#"])["Value"].cumsum()

# Wrong: accumulates across all rows
dataset["Value"].cumsum()
```

## When to Use Each Approach

| Scenario | Approach |
|----------|----------|
| Simple cumulative sum, small dataset (< 10K rows) | `List.FirstN()` in M |
| Cumulative sum with grouping (version, category, region) | `pandas cumsum()` in Power Query |
| Large dataset, iterative calculation | `pandas cumsum()` — M is too slow |
| Production pipeline needing reproducibility | `pandas cumsum()` — M `List.FirstN()` is opaque |

## The Performance Gap

| Method | Complexity | 10K rows | 100K rows | 1M rows |
|--------|-----------|---------|---------|---------|
| `List.FirstN()` (M) | O(n²) | ~1s | ~100s | ~10,000s |
| `cumsum()` (pandas) | O(n) | <0.1s | <0.5s | ~5s |

## Related

- [[python-script-in-power-query]] — how to run this Python script inside Power Query
- [[python-in-power-bi-setup]] — getting Python working in Power BI
- [[power-query-workflow-process]] — where Python scripts fit in the broader PQ workflow
