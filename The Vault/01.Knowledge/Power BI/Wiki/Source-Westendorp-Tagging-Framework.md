---
created: 2026-08-10
updated: 2026-08-10
source: A Practical Framework for Tagging and Classification in Power BI
source_url: https://medium.com/@jmwestendorp/a-practical-framework-for-tagging-and-classification-in-power-bi-da82114a8a49
note_type: source
tags: [powerbi, data-modeling, tagging, classification, bridge-table, many-to-many]
---

# Source: Westendorp — Tagging Framework

> **Type:** article
> **Author:** Jacob Westendorp
> **Published:** 2026-08-02
> **URL:** https://medium.com/@jmwestendorp/a-practical-framework-for-tagging-and-classification-in-power-bi-da82114a8a49
> **Routed to:** Power BI

## Summary

Replaces rigid hierarchical dimensions with a tagging-based classification model in Power BI. Entities can belong to multiple tags simultaneously via a bridge table that controls filter propagation and prevents ambiguous many-to-many aggregations. Covers data model design, filter flow mechanics, user interpretation caveats (non-additive totals), and governance principles.

## Key Claims

1. Hierarchical models force mutually-exclusive categorization — real-world entities often span multiple categories
2. Tagging allows multi-dimensional classification but requires a bridge table to avoid ambiguous filter propagation
3. The four-table model: `service_tags` (vocabulary) → `tagged_services` (assignments) → `dim_service_bridge` (filter control) → `Data` (fact)
4. The bridge is a distinct list of `KeyFieldID` values from the fact table — built via `Table.Distinct()`
5. Bi-directional filtering on the bridge is intentional and isolated to that layer only
6. Tag totals are NOT additive across categories — same entity may appear in multiple tag views
7. Tags = lenses, not partitions; each tag answers "what data relates to this?" not "what share belongs exclusively here?"
8. Governance shifts from structural enforcement (hierarchies) to process discipline (tagging)
9. Tag lifecycle: retire tags via `TagStatus = Inactive`, never delete
10. Assignment table maintained outside Power BI initially (Excel → SharePoint as governance matures)

## Notable Details

- `service_tags.TagKey` is the unique identifier; `TagName` is business-facing label
- `TagStatus` (Active/Inactive) enables lifecycle management without deleting rows
- Bridge table construction: `Table.Distinct(Table.SelectColumns(Data, {"KeyFieldID"}))`
- The `Notes` column in `tagged_services` is internal context, not user-facing
- Governance owner: typically a data steward or domain owner, not ad hoc contributors
- Over-tagging = tagging everything with everything = reduces analytical value
- Governance failures: duplicate tags, meaning drift, incomplete tagging, over-tagging

## Extracted Notes

Links to notes derived from this source:

- [[Tagging-Bridge-Table-Pattern]] — `pattern` — four-table model with bridge; filter flow mechanics
- [[Tag-Assignment-Table-Pattern]] — `pattern` — `tagged_services` structure and design decisions
- [[Tags-Equal-Lens-Not-Partition]] — `atomic` — tags as perspectives, not exclusive subsets
- [[Tag-Totals-Are-Not-Additive]] — `gotcha` — combined totals ≠ sum of individual tag totals
- [[Governance-Shifts-from-Structure-to-Process]] — `atomic` — tagging replaces structural discipline with process discipline
- [[Tag-Governance-Workflow]] — `workflow` — tag lifecycle, assignment standards, review cadence
- [[Tagging-Model-Data-Model-Reference]] — `reference` — schema diagram, table roles, relationship types

## Metadata

| Field | Value |
|-------|-------|
| Source file | A Practical Framework for Tagging and Classification in Power BI.md |
| Archived at | 99.System/InboxArchive/2026-08/ |
| Ingestion date | 2026-08-10 |
| Word count | ~456 |
