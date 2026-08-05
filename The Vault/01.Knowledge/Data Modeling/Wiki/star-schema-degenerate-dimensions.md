---
created: 2026-08-02
updated: 2026-08-02
source: Why Star Schema FACT Tables Are More Powerful Than You Think (And How to Master Them).md
note_type: pattern
tags: [data-modeling, pattern, fact-table, degenerate-dimension, storage-optimization]
---

# Degenerate Dimensions

A degenerate dimension (DD) is a dimension attribute stored directly in the fact table — not in a separate dimension table — because it has no meaningful attributes beyond its identifier. Transaction IDs, invoice numbers, order numbers, and receipt IDs are classic DDs.

## When to Use

- The attribute has no attributes to describe it (only an ID)
- Creating a separate dimension table would add a pointless join
- The attribute is always filtered or grouped alongside the fact (never standalone)

## Examples

| Degenerate Dimension | In Fact Table | Why Not a Dimension Table |
|---|---|---|
| `transaction_id` | ✓ fact_sales | Only used with sales; has no descriptive attributes |
| `invoice_number` | ✓ fact_invoice | Only meaningful in context of fact |
| `loyalty_card_id` | ✓ fact_customer_activity | Card has no descriptive attributes beyond the number |

## Storage Benefit

Storing transaction IDs as DDs instead of creating a `dim_transaction` table:
- **Saves 40% storage:** no dimension table overhead, no foreign key, no join
- Enables fact-level traceability without a join

## When NOT to Use

If the attribute has meaningful descriptive attributes (e.g., a product has name, category, brand — so it belongs in `dim_product`), it should not be a DD.

## Related

- [[star-schema-fact-table-principles]] — `atomic`
- [[star-schema-grain-locking-constraint]] — `pattern`
