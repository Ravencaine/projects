---
created: 2026-08-05
updated: 2026-08-05
source: 5 Data Cleaning Mistakes That Ruin Your Dashboard (DigitalBYKewat)
note_type: atomic
tags: [data-cleaning, duplicate, primary-key, power-query, sql, data-quality]
---

# Duplicate Records: Detection and Removal

Duplicate records inflate count metrics and distort revenue, profit, customer count, and inventory — often silently, until a stakeholder notices a massive discrepancy post-publication.

## Why Duplicates Happen

- Manual data entry: double-click on Submit button, double-pasting rows
- Multiple system imports merged without deduplication
- Incorrect JOIN conditions in SQL or Power Query (Cartesian product)
- API synchronisation lag causing re-insert of the same record

## Impact

A single duplicated large transaction can:
- Overstate revenue and profit
- Skew customer count and average order value
- Distort inventory quantities

## Detection

### QA measure: COUNTROWS vs DISTINCTCOUNT

```dax
Row Count        = COUNTROWS('Table')            // all rows including duplicates
Distinct Count   = DISTINCTCOUNT('Table'[ID])    // unique IDs only
Duplicate Count  = [Row Count] - [Distinct Count] // non-zero = duplicates exist
```

If `[Row Count] > [Distinct Count]`, duplicates are present.

### Power Query: Group By count

1. Group by the suspected key column (e.g., Order ID)
2. Add an "All Rows" aggregation
3. Filter rows where count > 1

## Removal

### Power Query

**Home → Remove Rows → Remove Duplicates** — removes rows that are identical across all columns.

**Important:** Apply this early in the pipeline, before any aggregations or joins.

### SQL

```sql
SELECT DISTINCT * INTO CleanTable FROM DirtyTable
```

Or use `ROW_NUMBER() OVER (PARTITION BY key ORDER BY ...) WHERE rn = 1`.

## Prevention

- Enforce primary keys at the source database level
- Audit JOIN conditions before running merge queries
- Set unique constraints on transaction ID columns in the data warehouse

## Related

- [[Dashboard-Health-Checklist]]
- [[Data-Cleaning-Pipeline-Flow]]
