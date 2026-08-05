---
created: 2026-08-02
updated: 2026-08-02
source: Why Star Schema FACT Tables Are More Powerful Than You Think (And How to Master Them).md
note_type: pattern
tags: [data-modeling, pattern, fact-table, encoding, compression, zstd, storage, performance]
---

# ZSTD Encoding + Column Clustering (500GB → 70GB)

Column-level ZSTD encoding on a fact table compresses storage dramatically while maintaining query performance. Pre-sorting (clustering) by high-cardinality columns used in WHERE clauses accelerates BI query patterns.

## ZSTD Encoding

ZSTD (Zstandard) is a lossless compression algorithm that balances compression ratio with fast decompression — ideal for data warehouse workloads.

```sql
transaction_id VARCHAR(50) ENCODE ZSTD NOT NULL,
customer_id    INT        ENCODE ZSTD NOT NULL,
product_id     INT        ENCODE ZSTD NOT NULL,
gross_revenue  DECIMAL(18,4) ENCODE ZSTD,
net_profit     DECIMAL(18,4) ENCODE ZSTD
```

Apply to: high-cardinality string columns, numeric columns that are not used in range predicates.

**Result: 500GB table compressed to 70GB (86% reduction).**

## Column Clustering (Pre-Sort Order)

```sql
ORDER BY (customer_id, transaction_id);
```

Clustering stores rows physically sorted by the specified columns. Queries filtering on `customer_id` read contiguous disk blocks — reducing I/O by ~40%.

## When to Use

| Technique | Best For |
|---|---|
| ZSTD encoding | High-cardinality strings, decimal numerics not used in range scans |
| Column clustering | Columns frequently filtered in WHERE clauses (customer_id, product_id) |

## Related

- [[star-schema-multi-key-partitioning]] — `pattern`
- [[star-schema-rollup-flags-pattern]] — `pattern`
