---
created: 2026-08-01
updated: 2026-08-02
source: "Master Power BI Introduction to Data Modeling!.md"
note_type: atomic
tags: [power-bi, data-modeling, star-schema, snowflake-schema, beginner, performance]
---

# Star Schema vs Snowflake Schema

Two ways to arrange fact and dimension tables. One is recommended; one has a niche use case.

## Star Schema ⭐ (Recommended)

One fact table at the centre. All dimension tables connect directly to it, like points on a star.

```
                    ┌─────────────┐
                    │   Date      │
                    └──────┬──────┘
                           │
              ┌────────────┼────────────┐
              │            │            │
    ┌─────────┴───┐  ┌────┴────┐  ┌────┴────┐
    │  Customers  │  │ Products │  │  Stores  │
    └─────────────┘  └─────────┘  └─────────┘
                     ┌───────────┐
                     │   Sales   │  (fact)
                     │  (center) │
                     └───────────┘
```

**Characteristics:**
- All dimension tables connect directly to the fact table
- No intermediate tables between dimensions and fact
- Simple, fast, and easy to understand
- Power BI's storage engine loves this structure
- This is the standard. Default to this.

## Snowflake Schema

Dimension tables are normalised — split into sub-dimensions that connect to each other, not directly to the fact table.

```
           ┌─────────────┐
           │  Category   │
           └──────┬──────┘
                  │
        ┌─────────┴─────────┐
        │                   │
┌───────┴───────┐   ┌──────┴──────┐
│   Products    │   │   Subcat   │
└───────┬───────┘   └────────────┘
        │
        │
   ┌────┴────┐
   │  Sales  │  (fact)
   └─────────┘
```

**Characteristics:**
- Dimensions split into multiple related tables
- Categories → Subcategories → Products
- Reduces data redundancy within dimensions
- More normalised, theoretically cleaner
- Slower queries (more joins required)
- Power BI's VertiPaq engine compresses well anyway — star schema is usually faster

## When to Use Snowflake

Snowflake is appropriate when:
- Dimensions have meaningful sub-groupings that are reused across many entities
- You need to independently analyse the sub-dimension (e.g., analyse by subcategory separately)
- Source data is already normalised and merging would be complex

In most Power BI scenarios: flatten to star schema for better performance.

## The Performance Reality

Power BI's VertiPaq compression engine handles star schema extremely well. Even if your source data is normalised, consider denormalising (merging sub-dimension tables) in Power Query before loading to get the star schema benefits.

## Related

- [[fact-table-vs-dimension-table]] — the building blocks of both schemas
- [[relationship-types-one-to-many-many-to-many]] — cardinality in star schema
- [[data-model-5-testing-checks]] — verifying the schema structure works correctly
