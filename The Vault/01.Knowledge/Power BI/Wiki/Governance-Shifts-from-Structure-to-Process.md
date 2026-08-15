---
created: 2026-08-10
updated: 2026-08-10
source: A Practical Framework for Tagging and Classification in Power BI
source_url: https://medium.com/@jmwestendorp/a-practical-framework-for-tagging-and-classification-in-power-bi-da82114a8a49
note_type: atomic
tags: [powerbi, data-modeling, tagging, governance, maintenance]
---

# Governance Shifts from Structure to Process

In hierarchical models, structure enforces discipline — a rigid parent-child path prevents inconsistency by design. In a tagging model, the structure is flexible, so consistency depends entirely on governance: defined processes, clear ownership, and ongoing review.

## Definition

A tagging model replaces structural simplicity with organizational discipline. Without governance, tagging degrades into duplicate tags, inconsistent application, and over-tagging — eroding trust and analytical value.

## Key Points

**Hierarchical models:** structure = discipline
- Every entity has exactly one path
- Mistakes are architecturally bounded
- Maintenance is purely structural

**Tagging models:** process = discipline
- Entities can span multiple categories
- Mistakes require process correction, not just model edits
- Maintenance is behavioural and organizational

## Governance Failure Modes

| Failure Mode | Example |
|-------------|---------|
| Duplicate tags | "Biofuel" and "Renewable Energy" both exist |
| Meaning drift | "Compliance" changes scope without notice |
| Inconsistent tagging | Some services tagged, others not |
| Over-tagging | Every entity tagged with every applicable tag |
| Silent gaps | Business changes but tagging is never updated |

## What Governance Must Cover

1. **Ownership:** who controls the tag vocabulary and assignment decisions
2. **Vocabulary control:** how tags are created, renamed, or retired
3. **Assignment standards:** how entities get tagged; who approves
4. **Lifecycle management:** how inactive tags are handled (retire, don't delete)
5. **Review cadence:** periodic consistency checks on the assignment table

## The Cost of Skipping Governance

A well-maintained tagging model scales cleanly. A poorly governed one becomes:
- Harder to understand
- Harder to trust
- Harder to fix later

The structural integrity of the bridge table is worthless if the tag vocabulary and assignments drift out of sync with business reality.

## Related

- [[Tag-Governance-Workflow]]
- [[Tagging-Bridge-Table-Pattern]]
