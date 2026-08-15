---
created: 2026-08-10
updated: 2026-08-10
source: A Practical Framework for Tagging and Classification in Power BI
source_url: https://medium.com/@jmwestendorp/a-practical-framework-for-tagging-and-classification-in-power-bi-da82114a8a49
note_type: reference
tags: [powerbi, data-modeling, tagging, bridge-table, reference]
---

# Tagging Model Data Model Reference

Four-table data model for flexible, multi-category entity classification via tagging. Each table has a single, distinct role.

## Schema

```
┌─────────────────┐     ┌─────────────────────┐
│  service_tags   │     │   tagged_services   │
│─────────────────│     │─────────────────────│
│ TagKey (PK)    │←──┐ │ KeyFieldID          │
│ TagName         │   │ │ TagKey              │───┐
│ TagStatus       │   │ │ Notes (optional)    │   │
└─────────────────┘   │ └─────────────────────┘   │
                       └──────────────┬────────────┘
                                      │
                         many-to-one (bi-directional)
                                      │
                       ┌──────────────▼────────────┐
                       │   dim_service_bridge       │
                       │────────────────────────────│
                       │ KeyFieldID (PK, from fact) │
                       └──────────────┬────────────┘
                                      │
                            one-to-many
                                      │
                       ┌──────────────▼────────────┐
                       │         Data               │
                       │────────────────────────────│
                       │ KeyFieldID (FK)            │
                       │ Measure columns...         │
                       │ Other attributes...        │
                       └─────────────────────────────┘
```

## Table Roles

| Table | Role | Connects To |
|-------|------|-------------|
| `service_tags` | Tag vocabulary definition | → `tagged_services` (one-to-many) |
| `tagged_services` | Entity-to-tag assignments | ← `service_tags`; → `dim_service_bridge` (many-to-one, bi-dir) |
| `dim_service_bridge` | Filter control layer | ← `tagged_services`; → `Data` (one-to-many) |
| `Data` | Fact table | ← `dim_service_bridge` |

## Filter Flow

```
service_tags → tagged_services → dim_service_bridge → Data
```

## Bridge Table Construction (Power Query M)

```m
= Table.Distinct(
    Table.SelectColumns(Data, {"KeyFieldID"})
)
```

Or in DAX as a calculated table:

```dax
dim_service_bridge =
DISTINCT(SELECTCOLUMNS(Data, "KeyFieldID", Data[KeyFieldID]))
```

## Relationship Types

| From | To | Type | Direction |
|------|----|------|-----------|
| `service_tags` | `tagged_services` | One-to-many | Single |
| `tagged_services` | `dim_service_bridge` | Many-to-one | **Bi-directional** |
| `dim_service_bridge` | `Data` | One-to-many | Single |

The bi-directional relationship on the bridge is **intentional and isolated:** it is not applied across the model.

## Key Design Rules

1. Never connect `service_tags` or `tagged_services` directly to `Data`
2. The bridge must always be the sole filter-control intermediary
3. All tag filtering flows through `dim_service_bridge`
4. `service_tags` and `Data` are never directly related

## Related

- [[Tagging-Bridge-Table-Pattern]]
- [[Tag-Assignment-Table-Pattern]]
