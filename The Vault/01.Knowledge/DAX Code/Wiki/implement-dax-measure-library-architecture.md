---
created: 2026-07-29
updated: 2026-08-02
source: DAX Measure Library Architecture — From Messy to Maintainable (Tejwani, 2026-01-19)
note_type: workflow
tags: [dax, measure-library, architecture, organization, folder-structure, governance, implementation]
---

# Implement a DAX Measure Library Architecture

A 4-week implementation plan to transform a chaotic measures table into a maintainable, team-usable DAX measure library. Based on Tejwani's 4-layer framework: folder structure, naming conventions, documentation, and governance.

## Purpose

Most Power BI models with 50+ measures are unusable by anyone other than their author. A measure library architecture makes DAX findable, understandable, and reusable — the organizational equivalent of the UDF pattern applied to the measure surface.

## The 4-Layer Framework

| Layer | What It Provides |
|-------|-----------------|
| 1 — Folder Structure | Visual organization by business function |
| 2 — Naming Conventions | Findability through search |
| 3 — Documentation Standards | Understanding of purpose and logic |
| 4 — Governance Process | Long-term sustainability |

## When to Use

**Essential when:**
- Team of 2+ analysts
- 50+ measures in any shared model
- Models shared across departments
- High turnover or onboarding frequency

**Not necessary when:**
- Solo analyst
- 20 or fewer measures
- Simple, stable calculations

## 4-Week Implementation Roadmap

### Week 1: Foundation

1. **Audit current state**: count measures, screenshot the chaos, identify top 10 most-used measures
2. **Define folder structure**: start with 3–5 business domains, expand as needed
3. **Agree on naming conventions**: one pattern, written down, with examples
4. **Create documentation template**: PURPOSE / USAGE / DEPENDENCIES / BUSINESS RULES / OWNER

### Week 2: Reorganization

1. Move top 20 most-used measures into the new folder structure
2. Rename measure violations
3. Add basic documentation to all 20
4. Update all visuals — they will break when measures are renamed

### Week 3: Process

1. Document the governance process (see [[measure-governance-process]])
2. Schedule recurring reviews
3. Assign first Library Champion role
4. Train the team on conventions

### Week 4: Refinement

1. Run the first weekly review
2. Catch early violations
3. Adjust conventions based on feedback
4. Celebrate wins

## After Week 4

Sustainability comes from consistency: weekly cadence continues until conventions become habit. The architecture becomes invisible — it just works.

## Starting Folder Structure Template

```
📁 _Base Measures
   📁 [Business Domain]
   📁 Date
📁 Time Intelligence
   📁 [Business Domain]
📁 Comparisons & Variance
   📁 [Business Domain]
📁 KPIs & Metrics
   📁 [Business Domain]
📁 Utilities
📁 Formatting
📁 _Exploration
   📁 [AnalystName]_[Project]
```

Replace `[Business Domain]` with actual domains: Sales, Customer, Product, Finance, Operations.

## Rule: Maximum 3 Folder Levels

```
✅ Good: KPIs & Metrics → Customer → Customer LTV
❌ Too deep: KPIs → Financial → Customer → Acquisition → Cost per Customer
```

More than 3 levels signals categories are too granular. Refactor instead of nesting.

## Rule: Folders Use Business Language

```
✅ Good: Sales, Customer, Product
❌ Bad: Fact_Sales, Dim_Customer, Aggregations
```

Business users should understand the organization without a data dictionary.

## Related

- [[measure-governance-process]] — governance workflow
- [[dax-measure-naming-convention-framework]] — naming conventions
- [[dax-measure-folder-structure-template]] — folder structure reference
- [[dax-measure-documentation-template]] — documentation template
- [[when-measure-library-architecture-is-essential]] — scope decision
- [[hidden-cost-of-messy-measures]] — the problem this solves
- [[measure-library-architecture-roi]] — before/after comparison
