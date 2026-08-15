---
created: 2026-08-11
updated: 2026-08-11
source: "Handling Multiple Fact Tables in Power BI.md"
note_type: gotcha
tags: [data-modeling, anti-pattern, multi-fact]
---

# Pitfall: Consolidated (Appended) Fact Tables

Stacking multiple fact tables into one via append (union) creates a single large fact table with null keys wherever fact-specific dimensions don't apply.

## Expected Behaviour

Consolidating into one table seems simpler — one fact, one place to filter.

## Actual Behaviour

- Columns that don't exist in all source facts produce `BLANK` values in every row where that column has no data
- Report consumers see unexpected blanks in visuals when filtering on fact-specific dimensions
- The consolidated table grows large and slow to refresh
- Measure logic becomes complex: must handle nulls and fact-type branching in every aggregation
- Grain becomes ambiguous — the table now holds rows at multiple granularities

## Why It Happens

An append/union in Power Query or a `UNION ALL` in SQL loads rows from each source fact into one table. Fact-specific columns (e.g., EmployeeKey for Reseller Sales) have no matching values for Internet Sales rows — they become NULL or a sentinel value.

## How to Handle It

Keep fact tables separate and connect them to shared dimensions. If consolidation is required for a specific downstream tool, apply it only in that layer — not in the analytical model.

## Related Gotchas

- [[pitfall-duplicating-dimensions]] — the other extreme of the same misdesign
- [[shared-dimensions-multi-fact]] — correct approach
