---
created: 2026-08-09
updated: 2026-08-09
source: "DAX user-defined functions (UDF) vs. calculation groups.md"
source_url: https://www.sqlbi.com/articles/dax-user-defined-functions-udf-vs-calculation-groups/
note_type: source
tags: [dax, user-defined-function, calculation-groups, udf, comparison, performance, code-reuse, sqlbi, marco-russo, alberto-ferrari]
---

# DAX UDFs vs Calculation Groups

UDFs and calculation groups are complementary — not competing — tools. UDFs are invisible developer tools for organizing business logic. Calculation groups are user-facing selectors that apply common filters or transformations to all measures in a visual.

> **Type:** article
> **Author:** Marco Russo & Alberto Ferrari
> **Published:** 2026-03-25
> **URL:** https://www.sqlbi.com/articles/dax-user-defined-functions-udf-vs-calculation-groups/
> **Routed to:** DAX Code

## Summary

Three semantic model tools serve three distinct purposes: measures (user-facing calculations), calculation groups (user-facing filters/transformations), and user-defined functions (invisible developer tools for code reuse). UDFs are expanded at query-plan time like C macros; parameters are resolved before execution. Calculation groups pass parameters through filter context — cheaper for simple cases, more expensive for complex shared logic invoked multiple times. The design principle: decide user-facing exposure (measure vs calculation group) first; implement with UDFs for complex/shared logic.

## Key Claims

- Measures and calculation groups are visible to report users; UDFs are invisible
- Calculation groups: user-facing choice applied to all measures in a visual (period slicer, scale factor)
- UDFs: developer tool — organize business logic in one place, reuse across measures and calculation items
- UDFs are macro-expanded in the query plan — parameters resolved before execution
- Filter context parameter passing adds overhead at query time; scales poorly for complex shared logic
- UDF pattern: business logic in model-independent functions → model-dependent wrappers (Local.*) → called from measures and calculation items
- New/returning customers example: UDF defines the business rule once; both calculation item and standalone measure call the same function
- Side-by-side visuals: standalone measures using UDFs can coexist with calculation group items without interference
- Pragmatic rule: simple calculations (SUM, basic arithmetic) stay as measures; complex or shared logic goes in UDFs

## Extracted Notes

- [[UDF-vs-Calculation-Groups-Comparison]] — `comparison` — UDFs = developer code-reuse tool (invisible); Calculation Groups = user-facing selector (visible)
- [[UDF-vs-Calculation-Groups-When-Which]] — `reference` — decision matrix: user needs to choose? → calculation group. Developer needs to share complex logic? → UDF

## Metadata

| Field | Value |
|-------|-------|
| Source file | DAX user-defined functions (UDF) vs. calculation groups.md |
| Archived at | 99.System/InboxArchive/2026-08/ |
| Ingestion date | 2026-08-09 |
| Word count | ~3,200 |
