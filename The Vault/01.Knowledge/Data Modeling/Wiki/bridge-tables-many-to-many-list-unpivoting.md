---
created: 2026-08-06
updated: 2026-08-06
source: Building a Data Warehouse from Scratch A Case Study in Kimball Modeling.md
note_type: pattern
tags: [data-warehouse, dimensional-modeling, bridge-table, many-to-many, fact-table, unnest]
---

# Bridge Tables — Many-to-Many and List Unpivoting

Standard fact table design assumes a many-to-one relationship between each fact row and its dimension keys. Many-to-many relationships require a bridge table. Also handles comma-separated list columns that need to be normalized.

## When a Bridge Table Is Needed

- One event affects multiple locations
- One order belongs to multiple categories
- One patient has multiple diagnoses
- Any fact where a single row's grain implies multiple values for the same attribute

## Rule

> Never assume two list columns in the same source row are index-parallel. Test this assumption — in real data, they often aren't.

Example: one event row contained `locations = "City A, City B, City C"` and `access_points = "AP1, AP2, AP3, AP4"` — four access points for three locations. The lists were independent, not parallel. Matching by index would have silently produced wrong results.

## Pattern: Unpivot Comma-Separated Lists

```sql
-- PostgreSQL: expand comma-separated list into rows
SELECT event_id,
       unnest(string_to_array(locations, ', ')) AS location
FROM source_events;

-- Build bridge table: one row per (fact, dimension) relationship
INSERT INTO event_location_bridge (event_sk, location_sk)
SELECT e.event_sk, l.location_sk
FROM events e
CROSS JOIN LATERAL (
    SELECT location
    FROM unnest(string_to_array(e.location_list, ', ')) AS loc(location)
) sub
JOIN dim_location l ON l.location = sub.location;
```

## Maintaining Fact Table Grain

The fact table grain remains "one event = one row." The bridge table does not change this — it adds the dimension relationship layer without duplicating the fact row.

## Related

- [[junk-dimension-combine-vs-separate]] — dimensional modeling decision pattern
- [[multi-source-merge-archive-priority-load-sequencing]] — load sequencing for fact tables with bridge relationships
- [[kimball-dimensional-modeling-case-study-baylas-2026]] — `source`
