---
created: 2026-07-27
updated: 2026-08-02
source: "Star Schema vs Snowflake Schema in Power BI"
source_url: "https://medium.com/learning-data/star-schema-vs-snowflake-schema-in-power-bi-5711f294e584"
note_type: comparison
tags: [star-schema, snowflake-schema, data-modeling, power-bi, performance]
---

# Star Schema vs Snowflake Schema

## Summary

Star Schema is simpler and faster — single-hop joins from fact to dimension. Snowflake Schema is more normalised but adds multi-hop joins that degrade Power BI refresh and query performance. Default to Star Schema 90% of the time.

## Star Schema

### Pros
- Single join from fact to each dimension — fastest query path
- Simple data model — analysts understand it in minutes
- Works well with Power BI's auto-generated relationships
- Handles flat hierarchies (no nesting) directly in the dimension table

### Cons
- Flattened hierarchies can lead to wide dimension tables with redundant data
- If hierarchies are deep and normalised, flattening produces large rows

## Snowflake Schema

### Pros
- Normalised dimensions reduce data redundancy
- Hierarchies (Region → Manager → Director) stored cleanly in separate tables
- Easier to maintain consistent category definitions across products

### Cons
- Multi-hop joins: 4 queries to traverse Region → Manager → Director
- Each join adds latency; 4 hops is ~4x slower than 1 hop for the same row count
- Power BI's auto relationships may not handle snowflaked chains correctly

## Comparison Table

| Criteria | Star Schema | Snowflake Schema |
|----------|-------------|-----------------|
| Join depth | 1 hop (fact → dim) | Multi-hop (fact → dim → subdim → subdim) |
| Query speed | Fast | Slower |
| Data redundancy | Higher | Lower |
| Model simplicity | High | Lower |
| Hierarchy handling | Flattened in dim | Separate normalised tables |
| Refresh performance | Better | Worse |
| 1.5M row refresh | ~2 min | ~8 min |

## When to Use

**Use Star Schema when:**
- Data is "flat" — no deep organisational or geographic hierarchies
- Performance is a priority (always in Power BI)
- Default choice for almost all Power BI projects

**Use Snowflake Schema when:**
- Data has genuine deep hierarchies (geography: Country → Region → District → Store)
- You have a MDM (Master Data Management) system that already normalises categories
- Power BI is connected to a pre-existing data warehouse with snowflaked dimensions

## Related

- [[medallion-architecture]] — layered architecture where Gold layer typically uses Star Schema
- [[degenerate-dimension-barcode-in-fact]] — dimension modelling technique compatible with Star Schema
