---
created: 2026-08-10
updated: 2026-08-10
source: A Practical Framework for Tagging and Classification in Power BI
source_url: https://medium.com/@jmwestendorp/a-practical-framework-for-tagging-and-classification-in-power-bi-da82114a8a49
note_type: pattern
tags: [powerbi, data-modeling, tagging, assignment-table, many-to-many]
---

# Tag Assignment Table Pattern

The `tagged_services` (assignment) table maps entities to tags, creating the many-to-many relationship that enables flexible multi-category classification.

## Purpose

Separates the act of tagging from tag definition. A tag can be renamed or retired in `service_tags` without touching the assignment table. Assignments can be updated by business stakeholders without changing the model structure.

## Structure

**Columns:**
| Column | Source | Notes |
|--------|--------|-------|
| `KeyFieldID` | From fact table | The entity being tagged |
| `TagKey` | From `service_tags` | The classification tag applied |
| `Notes` | Optional | Internal context for auditors |

**Cardinality:**
- One entity can appear multiple times (once per tag)
- One tag can map to many entities
- This is the many-to-many layer

## Design Decisions

**Keep it flat.** Avoid adding columns unless they serve a clear analytical purpose. Each extra column in the assignment table increases maintenance burden and risks inconsistency.

**Separate from tag definition.** The assignment table should never embed tag metadata. Tag names, descriptions, and status belong in `service_tags` — not duplicated in assignments.

**Maintain outside Power BI initially.** Start in Excel for sandboxing. As tagging matures, move to a shared list or collaborative tool (SharePoint List). Power BI simply consumes the curated table.

## Governance Implication

This table is the most operationally intensive to maintain — it requires ongoing input from business stakeholders. Governance must cover:
- Who can add/remove assignments
- What constitutes a valid tag application
- Review cadence for consistency
- How to handle untagged entities

## Related

- [[Tagging-Bridge-Table-Pattern]]
- [[Tag-Governance-Workflow]]
- [[Tag-Totals-Are-Not-Additive]]
