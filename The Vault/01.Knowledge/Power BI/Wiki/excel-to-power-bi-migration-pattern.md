---
created: 2026-07-27
updated: 2026-08-02
source: "We Replaced 47 Excel Files With One Power BI Model"
note_type: pattern
tags: [power-bi, excel-migration, change-management, governance, enterprise-migration]
---

# Excel to Power BI Migration Pattern

A structured approach to replacing a multi-Excel-file reporting ecosystem with a single Power BI semantic model, including the organizational and change management dimensions.

## Purpose

Migrate from a fragmented Excel-based reporting system (where each analyst maintains their own file) to a unified Power BI model — without breaking existing workflows or losing institutional knowledge.

## When to Use

- Multiple Excel files exist with overlapping data
- Each Excel file has its own copy of "master data" with formulas
- Monthly report publishing is manual and error-prone
- Business users spend more time maintaining Excel than analyzing data

## Phase 1: Assessment

1. Inventory all Excel files: purpose, data sources, formulas, users
2. Identify the single source of truth: which file has the rawest data?
3. Identify overlapping data: where are the same numbers calculated differently?
4. Identify analyst-maintained macros and formulas: which are replaceable, which are not?
5. Build a dependency map: which Excel file depends on which other file?

## Phase 2: Data Layer (Technical)

1. Consolidate raw data sources into Power Query (or a data warehouse)
2. Build the semantic model: relationships, date table, hierarchies
3. Create master measures using [[measure-branching-pattern]]
4. Validate against the original Excel totals
5. Create TEST measures for every base calculation

## Phase 3: Transition (User Adoption)

1. **Do not remove Excel files immediately**: run Power BI in parallel for 1 month
2. Compare Power BI outputs against Excel outputs daily
3. Identify which Excel formulas have no Power BI equivalent yet
4. Build a "bridge" for analyst-maintained macros: Power Query parameters, manual entry tables

## Phase 4: Cutover

1. Train analysts on Power BI (2-hour workshop recommended)
2. Set up a support channel (Teams channel, 1-month intensive support)
3. Archive Excel files (do not delete — keep for audit trail)
4. Document the new workflow in a shared wiki

## Common Pitfalls

| Pitfall | Prevention |
|---------|-----------|
| Resistance from Excel power users | Pilot with a receptive team first, not the most resistant |
| Replacing Excel formulas that can't be replicated | Keep a "manual entry" Excel for edge cases; don't over-engineer |
| Not validating Power BI against Excel totals | Run parallel for 1 month with daily reconciliation |
| No governance for new reports | Establish a semantic model governance policy before cutover |
| Shadow IT returns | Define who can create new datasets/measures; restrict workspace permissions |

## Change Management (Often the Hardest Part)

- Communicate the benefit to analysts: less time maintaining Excel, more time analyzing
- Do NOT frame it as "we're taking away your Excel" — frame as "we're automating the boring parts"
- Provide a 1-month support channel after cutover
- Celebrate early wins publicly

## Related

- [[measure-branching-pattern]]
- [[power-bi-dashboard-checklist]] — pre-publish checklist for the migrated model
- [[data-warehousing-bi]] — the single source of truth concept for the migrated model is grounded in data warehousing principles
