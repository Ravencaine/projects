---
created: 2026-08-02
updated: 2026-08-02
source: Why Star Schema FACT Tables Are More Powerful Than You Think (And How to Master Them).md
note_type: reference
tags: [data-modeling, reference, star-schema, fact-table, framework, performance, checklist]
---

# Star Schema Performance Framework (5-Step Summary)

A 5-step framework for designing star schema fact tables that maximize analytical performance and reporting accuracy.

## The 5 Steps

1. **Lock the grain first:** No compromises. Define one grain per fact table. One row = one transaction/line item/event. No mixed grains.
2. **PK-FK enforcement:** Every foreign key must reference a valid primary key. Add explicit constraints. Use `RELY` in cloud warehouses.
3. **Pre-aggregate the obvious:** Daily sales totals, weekly orders, monthly summaries — store pre-aggregated summaries as separate tables or rollup flags for dashboard queries.
4. **Test with real users:** Benchmark against flat-table baselines. If star schema is not faster, the design is wrong.
5. **Document and monitor:** Document the grain in DDL comments. Add UNIQUE constraint. Run non-additive measure audit quarterly.

## Performance Results (Real-World)

| Scenario | Before | After |
|---|---|---|
| Complex promotional rules query | 4 hours (flat file) | 36 minutes (star schema) |
| Regional sales report | 12 seconds (flat table) | 0.8 seconds (star schema + RELY) |
| Monthly average order value | 14 seconds | 1.2 seconds (semantic layer fix) |
| Dashboard load | 2 minutes | 3 seconds (rollup flags) |

## Related

- [[star-schema-fact-table-principles]] — `atomic`
- [[non-additive-measures-audit]] — `pattern`
- [[star-schema-referential-integrity-rely]] — `pattern`
- [[star-schema-grain-locking-constraint]] — `pattern`
