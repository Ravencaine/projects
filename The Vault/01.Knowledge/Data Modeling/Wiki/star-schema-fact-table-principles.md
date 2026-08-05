---
created: 2026-08-02
updated: 2026-08-02
source: Why Star Schema FACT Tables Are More Powerful Than You Think (And How to Master Them).md
note_type: atomic
tags: [data-modeling, atomic, star-schema, fact-table, grain, dimension, additive-measures]
---

# Star Schema FACT Table Design Principles

Star schema separates facts (numerical measurements at a specific grain) from dimensions (descriptive attributes for filtering and grouping). FACT tables store quantitative business events. DIMENSION tables store the context.

## The Core Insight

Real-world fact tables handle late returns, multi-currency chaos, and promotional rules — not the clean "sales_fact" textbook examples. Star schema solves these problems structurally, not analytically.

## Essential Grain Principles

**Lock the grain first. No compromises.**

The grain is the atomic level of one row in the fact table. Every fact table must have exactly one grain — one transaction, one line item, one event. Common grains:
- Point-of-sale: one product per transaction per day
- E-commerce: one product per order line item
- Inventory: one product per store per day

If grain is not locked, every aggregation silently double-counts.

## Fact Table Types

| Type | Description | Examples |
|---|---|---|
| **Transaction** | One row per business event | Sales, orders, invoices |
| **Periodic Snapshot** | One row per dimension per period | Daily inventory balances |
| **Accumulating Snapshot** | One row per pipeline milestone | Order fulfillment stages |

## Design Rules

1. **Only store facts at one grain:** mixing grains in one table causes silent double-counting
2. **Degenerate dimensions** (transaction IDs, invoice numbers) live in the fact table — do not create separate dimension tables for them
3. **Denormalize slowly changing metrics** (exchange rates, discount flags) into the fact table — do not join at query time
4. **PK-FK relationships are non-negotiable:** every foreign key must reference a valid primary key
5. **Pre-aggregate obvious totals:** daily sales, weekly orders, monthly summaries as separate pre-aggregated tables for dashboard performance

## Common Mistakes

| Mistake | Symptom | Fix |
|---|---|---|
| Mixed grain | Revenue doubles when filtering by two dimensions | Re-declare grain, split into separate fact tables |
| Normalized fact table | Slow queries (BI tool joining too many tables) | Denormalize exchange rates and promo flags into the fact |
| No primary key | Duplicate rows | Add UNIQUE constraint on grain columns |
| Non-additive fields | 10–100x slower queries | Replace discount_rate with total_discounts; calculate ratio at semantic layer |

## Related

- [[star-schema-double-timestamp-pattern]] — `pattern`
- [[star-schema-degenerate-dimensions]] — `pattern`
- [[star-schema-late-arrival-handling]] — `pattern`
- [[star-schema-multi-key-partitioning]] — `pattern`
- [[star-schema-zstd-encoding-clustering]] — `pattern`
- [[star-schema-rollup-flags-pattern]] — `pattern`
- [[star-schema-referential-integrity-rely]] — `pattern`
- [[star-schema-grain-locking-constraint]] — `pattern`
- [[non-additive-measures-audit]] — `pattern`
