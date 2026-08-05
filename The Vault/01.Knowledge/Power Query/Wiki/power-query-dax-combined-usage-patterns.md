---
created: 2026-08-01
updated: 2026-08-02
source: "Power Query or DAX Make the Right Choice Every Time.md"
note_type: atomic
tags: [power-bi, power-query, dax, best-practices, workflow, beginner]
---

# Six Rules for Using Power Query and DAX Together

Power Query and DAX are teammates, not rivals. These six rules define how to combine them effectively.

## Rule 1: Clean and Filter Early

Don't import every column "just in case." Use Power Query to trim the dataset to only what the report needs.

The smaller the model, the faster every DAX measure runs.

## Rule 2: Pre-Aggregate When You Know the Answer

If you know you'll always need monthly totals, quarterly revenue, or yearly customer counts — compute those in Power Query during refresh.

No point making DAX recalculate the same totals on every visual render.

## Rule 3: Centralise Business Logic Once

Rules like "a customer is active if they purchased in the last 90 days" belong in Power Query — computed once, reused everywhere — not copied into 10 different measures across 5 reports.

Build it once in Power Query. DAX references it everywhere.

## Rule 4: Build Helper Tables in Power Query

Calendar tables, category mappings, and reference tables are easier to manage and maintain in Power Query than to work around in DAX.

**Example:** A date dimension with Year, Quarter, Month, WeekDay columns — built in Power Query using `CALENDAR()` or `CALENDARAUTO()` — is simpler and faster than building it with DAX calculated columns.

## Rule 5: Flatten When It Makes Sense

For non-technical audiences who just need slicers and a table to explore, consider denormalising with Power Query into a single "mega table."

Trade-off: faster for simple users, less flexible for analysts. Use judgement.

## Rule 6: Reserve DAX for Dynamic Exploration

DAX is the on-demand calculation engine. Its strength is reacting to user input — slicers, filters, drill-downs, custom hierarchies.

If a calculation doesn't need to be dynamic, do it in Power Query instead.

## The Summary Principle

> **Do in Power Query what you can. Reserve DAX for what you can't.**

Power Query: heavy lifting, done once, at refresh.
DAX: dynamic calculation, done on demand, per visual.

## Related

- [[power-query-vs-dax-core-difference]] — the foundational distinction
- [[static-vs-dynamic-aggregations]] — applying Rule 2 and Rule 6
- [[power-query-vs-dax-model-size-performance]] — why Rule 1 and Rule 2 matter for speed
