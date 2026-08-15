---
created: 2026-08-10
updated: 2026-08-10
source: A Practical Framework for Tagging and Classification in Power BI
source_url: https://medium.com/@jmwestendorp/a-practical-framework-for-tagging-and-classification-in-power-bi-da82114a8a49
note_type: pattern
tags: [powerbi, data-modeling, tagging, bridge-table, many-to-many, classification]
---

# Tagging + Bridge Table Pattern

Use a controlled tagging model with a bridge table to allow data entities to belong to multiple categories simultaneously — replacing rigid hierarchies with flexible, many-to-many classification without ambiguous filter propagation.

## Purpose

Hierarchical dimensions force each entity into a single path. Real-world entities (services, products, documents) often span multiple categories. This pattern allows multi-dimensional classification without the filter ambiguity that direct many-to-many relationships introduce.

## Components

Four tables, each with a distinct role:

1. **service_tags:** Tag definition layer: `TagKey`, `TagName`, `TagStatus` (Active/Inactive)
2. **tagged_services:** Assignment layer: `KeyFieldID`, `TagKey`, optional `Notes`; maps entities to tags
3. **dim_service_bridge:** Filter control layer: `KeyFieldID` (distinct values from fact table)
4. **Data:** Fact table: measures + `KeyFieldID`; does NOT connect directly to tags

## Filter Path

```
User selects tag (service_tags)
    ↓ one-to-many
Filtered tagged_services (only rows matching tag)
    ↓ many-to-one (bi-directional)
dim_service_bridge (controlled intersection)
    ↓ one-to-many
Data fact table
```

## Bridge Table Construction

```dax
-- Power Query M for the bridge:
= Table.Distinct(
    Table.SelectColumns(Data, {"KeyFieldID"})
)
```

The bridge is simply a distinct list of `KeyFieldID` values pulled from the fact table. No additional columns.

## Why the Bridge Is Required

Direct tag → fact many-to-many causes:
- Ambiguous filter propagation
- Incorrect aggregations
- Non-deterministic totals

The bridge reduces every relationship to a series of standard one-to-many paths, keeping filter behavior deterministic.

## Bi-Directional Filtering

The relationship between `tagged_services` and `dim_service_bridge` is **bi-directional:** this is intentional and isolated to this table only. It allows:
- Forward propagation: tag selection → bridge → fact
- Backward consistency: bridge interactions with other dimensions stay consistent

This is NOT a blanket bi-directional approach across the model — it is confined to the bridge layer.

## Mental Model

| Layer | Role |
|-------|------|
| `service_tags` | defines what you **select** |
| `tagged_services` | defines what **matches** the selection |
| `bridge` | defines what is **allowed** to filter the fact |
| `Data` | contains what you **measure** |

Each step narrows the dataset in a controlled way.

## Related

- [[Tag-Assignment-Table-Pattern]]
- [[Tags-Equal-Lens-Not-Partition]]
- [[Tag-Totals-Are-Not-Additive]]
- [[Tag-Governance-Workflow]]
