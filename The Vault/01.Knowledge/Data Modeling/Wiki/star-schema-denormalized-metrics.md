---
created: 2026-08-02
updated: 2026-08-02
source: Why Star Schema FACT Tables Are More Powerful Than You Think (And How to Master Them).md
note_type: pattern
tags: [data-modeling, pattern, fact-table, denormalization, currency, multi-currency, performance]
---

# Denormalized Metrics — Pre-Computed Exchange Rates

Pre-denormalize slowly changing or frequently joined metric components directly into the fact table. Do not join at query time for attributes that change per transaction.

## The Problem

Multi-currency reporting that joins a `dim_currency` table at query time to apply `exchange_rate` to `sales_amount` causes the BI tool to perform the calculation on every query — and creates a many-to-many relationship if exchange rates change over time.

## The Pattern

```sql
sales_amount                  DECIMAL(18,4),
exchange_rate_at_transaction DECIMAL(10,6),
normalized_usd_revenue       DECIMAL(18,4)
```

Three columns instead of one — but all computation happens at load time, not query time:
- `sales_amount` — original transaction currency amount
- `exchange_rate_at_transaction` — rate locked at transaction date
- `normalized_usd_revenue` — pre-computed USD value

## Why This Is a Fact Table, Not a Dimension

Currency rate is not a descriptive attribute of the product or customer — it is a transaction-level numeric component that changes per transaction and per day. It belongs in the fact table.

## General Rule

Denormalize into the fact any metric component that:
- Changes per transaction (not per product/customer)
- Would require a join at query time
- Is used in >80% of queries

## Related

- [[star-schema-fact-table-principles]] — `atomic`
- [[star-schema-grain-locking-constraint]] — `pattern`
