---
created: 2026-08-01
updated: 2026-08-02
source: "My Power BI Report Took 14 Seconds to Load. Here's Everything I Did to Get It Under 2.md"
note_type: atomic
tags: [power-bi, performance, vertipaq, cardinality, compression, intermediate]
---

# VertiPaq Column Cardinalinality

VertiPaq compresses data column by column using dictionary encoding. **Column cardinality — the number of unique values — drives model size more than row count.**

## The Cardinality Rule

| Column Type | Unique Values | Compression |
|-------------|-------------|-------------|
| Region | 5 | Excellent — stored almost for free |
| Order Date | 365/year | Good |
| TransactionID | 12M (= row count) | Terrible — huge dictionary |

A single high-cardinality column can cost more memory than a dozen low-cardinality ones.

## Columns to Remove

Ask of every column: does a visual, measure, or relationship actually use this?

Common offenders to remove:
- **Raw transaction IDs**: used as grouping keys? No → remove
- **Millisecond-accurate timestamps**: report by day only? → split to Date only
- **Free-text notes**: rarely/never opened → remove
- **Duplicate data**: same info already in another table → remove

## Practical Impact

Removing TransactionID, a DateTime column (kept date only), and three unused notes fields: **38% smaller model file** (210MB → 129MB). Smaller model → less to scan → faster every query.

## The Fix Order

1. Remove unused columns entirely
2. Reduce precision on high-cardinality date columns (DateTime → Date)
3. Check relationships — remove bidirectional ones that aren't needed
4. Denormalize repeated text into dimension tables

## Related

- [[star-schema-performance-impact]] — why splitting to dimensions helps compression
- [[auto-date-time-disable]] — DateTime split as a specific case
- [[direct-lake-vs-import]] — model size also affects refresh duration in Import mode
