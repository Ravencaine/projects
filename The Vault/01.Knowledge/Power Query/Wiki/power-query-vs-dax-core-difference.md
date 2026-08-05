---
created: 2026-08-01
updated: 2026-08-02
source: "Power Query or DAX Make the Right Choice Every Time.md"
note_type: atomic
tags: [power-bi, power-query, dax, beginner, comparison, etl]
---

# Power Query vs DAX: Core Difference

Power Query and DAX both manipulate data, but they operate at completely different stages and in completely different ways.

## Power Query: The Kitchen Prep

Power Query is **ETL (Extract, Transform, Load)**. It runs once — at refresh time — before data enters the model.

What Power Query does:
- Cleans, filters, merges, and reshapes data
- Removes unnecessary columns
- Aggregates to reduce row count
- Pre-computes known values

After refresh, Power Query's work is done. The results are stored in the model.

**Analogy:** prepping ingredients before a dinner service. Everything is chopped, cleaned, and organised before the chef starts cooking.

## DAX: The On-the-Fly Chef

DAX is the **calculation engine**. It runs every time a visual renders — in response to slicers, filters, drill-downs, and user interactions.

What DAX does:
- Aggregates on the fly (SUM, COUNT, AVERAGE)
- Applies filter and row context
- Responds dynamically to user input
- Calculates what Power Query couldn't know in advance

**Analogy:** a chef cooking custom dishes to order, in front of the audience. Every dish is made fresh based on what the customer asked for.

## The Critical Distinction

| Aspect | Power Query | DAX |
|--------|------------|-----|
| Runs | Once per refresh | Every visual render |
| Stage | Before data loads | After data loads |
| Triggered by | Scheduled refresh | Slicer/filter/drill-down |
| Result stored | In the model | Computed on demand |
| Flexibility | Fixed once deployed | Dynamic per query |

## The Anti-Pattern

Using DAX to do Power Query's job — cleaning raw data, removing columns, or pre-aggregating known totals — is the equivalent of a chef chopping onions mid-service. It works, but it's slow, expensive, and wasteful.

**Rule:** Do in Power Query what you can. Reserve DAX for what you can't.

## Related

- [[storage-mode-import-vs-directquery]] — PQ only works in Import mode
- [[power-query-vs-dax-model-size-performance]] — performance consequences of the choice
- [[static-vs-dynamic-aggregations]] — known aggregations vs flexible user-driven calculation
