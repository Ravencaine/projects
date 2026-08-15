---
created: 2026-08-11
updated: 2026-08-11
source: "Handling Multiple Fact Tables in Power BI.md"
note_type: gotcha
tags: [data-modeling, anti-pattern, multi-fact]
---

# Pitfall: Duplicating Dimensions Per Fact Table

Creating separate dimension tables for each fact table (e.g., one Date table per fact, one Product table per fact) bloats the model, slows refresh, and breaks cross-fact reporting.

## Expected Behaviour

Each dimension should filter its related fact table. Having a dedicated dimension per fact might seem like clean separation.

## Actual Behaviour

- Model size grows with every duplicated dimension copy
- Refresh time increases as Power BI processes N identical Date tables instead of one
- Report authors see multiple Date tables and multiple Product tables, with no clarity on which to use
- Cross-fact reports (e.g., combining Internet and Reseller Sales) produce ambiguous or incorrect results because there is no single shared dimension to slice by

## Why It Happens

Default data warehouse extracts often copy dimension tables per fact. BI developers replicate this pattern without recognising it as an anti-pattern in an in-memory model like Power BI.

## How to Handle It

Replace all duplicate dimensions with a single shared dimension table. In Power BI:

1. Import only one Date table, one Product table, one Location table
2. Create relationships from the shared dimension to each fact table
3. Add table descriptions in Power BI so authors know which dimensions are shared vs fact-specific

## Related Gotchas

- [[pitfall-consolidated-fact-tables]] — the opposite extreme: stacking fact tables instead of sharing dimensions
- [[shared-dimensions-multi-fact]] — correct approach
