---
created: 2026-08-10
updated: 2026-08-10
source: A Practical Framework for Tagging and Classification in Power BI
source_url: https://medium.com/@jmwestendorp/a-practical-framework-for-tagging-and-classification-in-power-bi-da82114a8a49
note_type: workflow
tags: [powerbi, data-modeling, tagging, governance, workflow]
---

# Tag Governance Workflow

Process for establishing and maintaining a tagging model over time — covering tag lifecycle, assignment standards, and maintenance cadence.

## Prerequisites

- Tagging + Bridge Table pattern implemented in the data model
- `service_tags` table deployed with `TagStatus` column (Active/Inactive)
- Business stakeholders identified for tag governance decisions

## Steps

### 1 — Assign Ownership

1. Identify a **data steward** or **domain owner** responsible for the tag vocabulary
2. Document the owner in the tag governance policy
3. Avoid ad hoc updates from multiple independent contributors — all changes go through the owner

### 2 — Establish a Controlled Vocabulary

1. Create tags in `service_tags` only when they clearly add analytical value
2. Define each tag with a **business-friendly label** and a **documented meaning**
3. Store the definition alongside the tag (in the tag description field or a companion lookup table)
4. Review proposed new tags against existing tags to prevent duplication

### 3 — Set Assignment Standards

1. Define what constitutes a valid tag application for each entity type
2. Document assignment guidelines (e.g., "a service is tagged Logistics if >50% of its activity relates to logistics")
3. Avoid over-tagging — not every applicable tag should be applied to every entity
4. Assign responsibility for making assignment decisions to a specific role, not individuals

### 4 — Manage the Assignment Layer

1. Maintain `tagged_services` outside of Power BI initially (Excel → SharePoint List as governance matures)
2. Periodically audit assignments for:
   - Missing tags on entities that clearly qualify
   - Incorrect tags applied to entities
   - Duplicate or near-duplicate tag patterns
3. Use the `Notes` column for audit trails on edge cases

### 5 — Lifecycle Management (Retire, Don't Delete)

1. When a tag becomes obsolete, set `TagStatus = Inactive` — **do not delete rows**
2. Ensure the reporting behaviour for inactive tags is documented and communicated
3. Notify report consumers before retiring a tag

### 6 — Review Cadence

| Frequency | Scope |
|-----------|-------|
| Weekly | New assignment requests |
| Monthly | Tag vocabulary consistency check |
| Quarterly | Full assignment audit + governance review |
| Annually | Tag relevance review — are all active tags still adding value? |

## Common Errors

- [[Tag-Totals-Are-Not-Additive]] — users summing across tags instead of viewing in isolation
- Creating tags without documented definitions (causes inconsistent application)
- Deleting old tags instead of retiring them (breaks historical report comparisons)

## Related

- [[Governance-Shifts-from-Structure-to-Process]]
- [[Tagging-Bridge-Table-Pattern]]
- [[Tags-Equal-Lens-Not-Partition]]
