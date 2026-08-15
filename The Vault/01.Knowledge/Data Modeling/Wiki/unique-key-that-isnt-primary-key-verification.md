---
created: 2026-08-06
updated: 2026-08-06
source: Building a Data Warehouse from Scratch A Case Study in Kimball Modeling.md
note_type: atomic
tags: [data-warehouse, primary-key, data-quality, sql, verification]
---

# "Unique" Key That Isn't — Primary Key Verification

Always test every column assumed to be a primary key before using it. Source systems frequently claim uniqueness that doesn't hold under real data volume.

## Definition

A column (or column set) is a reliable primary key only when `COUNT(*) = COUNT(DISTINCT column)`. Any gap between these two values means the column is not unique and cannot safely serve as a primary key or join target.

## Key Points

- Never accept "this `id` column is unique" without running `COUNT(*) vs COUNT(DISTINCT id)` against the actual table
- An `id` column may act as a category/type code rather than a record identifier — e.g., a detail table where `id` takes only ten distinct values across millions of rows
- If a single column isn't unique, test for a **composite key** — a combination of columns that together establish uniqueness
- If no natural key candidate is unique, generate a surrogate key yourself

## Examples

```sql
-- Step 1: Test a single column
SELECT COUNT(*), COUNT(DISTINCT id)
FROM source_table;

-- If counts differ, try a composite key:
SELECT COUNT(*), COUNT(DISTINCT CONCAT(id, '-', sub_id))
FROM source_table;
```

A gap means blind upsert logic (using that column as a key) will silently overwrite the wrong rows.

## Related

- [[same-code-different-meanings-code-column-reliability]] — another dimension of source column unreliability
- [[multi-source-merge-archive-priority-load-sequencing]] — upsert logic that depends on reliable keys
- [[kimball-dimensional-modeling-case-study-baylas-2026]] — `source`
