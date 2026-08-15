---
created: 2026-08-09
updated: 2026-08-09
source: "Fix Incorrect Totals in Power BI Tables.md"
note_type: pattern
tags: [dax, power-bi, totals, sumx, summarize, context-transition, calculate, pattern]
---

# Fix Incorrect Totals — SUMX + SUMMARIZE Pattern

Corrects the total row in table/matrix visuals when using non-additive aggregations (MAX, MIN, AVERAGE) by ensuring each row-level group contributes its aggregate to the total.

## Purpose

`MAX`, `MIN`, and `AVERAGE` applied directly to a column return a single value for the entire filter context — not the sum of per-group aggregates. The total row therefore shows the wrong number. This pattern forces the total to iterate over groups and sum each group's aggregate.

## Structure

```dax
Corrected Measure :=
SUMX(
    SUMMARIZE(
        <GroupTable>,
        <GroupTable>[GroupColumn],
        "AggPerGroup", CALCULATE( <Aggregation>( <Table>[Column] ) )
    ),
    [AggPerGroup]
)
```

## Components

- `SUMMARIZE` — builds a table of distinct groups (categories, months, etc.)
- `CALCULATE` inside SUMMARIZE — triggers **context transition**: each row's filter context is applied to the aggregation, producing the per-group result
- `SUMX` — iterates over the group table and sums each per-group aggregate into the total

## Example 1: Max Unit Price Per Category

**Naive (wrong):**
```dax
Max Unit Price = MAX(OrderDetails[UnitPrice])
```
Total shows the single maximum across all categories — not the sum of per-category maxima.

**Corrected:**
```dax
Max Unit Price Corrected :=
SUMX(
    SUMMARIZE(
        Categories,
        Categories[CategoryName],
        "MaxPerCategory", CALCULATE( MAX( OrderDetails[UnitPrice] ) )
    ),
    [MaxPerCategory]
)
```
Total now correctly sums the max unit price for each category.

## Example 2: Average Quantity Per Month

**Naive (wrong):**
```dax
Avg Quantity = AVERAGE( OrderDetails[Quantity] )
```
Total shows the average across all months — not the sum of per-month averages.

**Corrected:**
```dax
Avg Quantity Corrected :=
SUMX(
    SUMMARIZE(
        Calendar,
        Calendar[Year],
        Calendar[Month],
        "AvgPerMonth", CALCULATE( AVERAGE( OrderDetails[Quantity] ) )
    ),
    [AvgPerMonth]
)
```
Total sums the monthly averages. Subtotals per year are also correct.

## Why CALCULATE Is Required Inside SUMMARIZE

Without `CALCULATE`, `MAX(OrderDetails[UnitPrice])` inside `SUMMARIZE` runs in the **row context** of the SUMMARIZE iteration but not the **filter context** of the visual. `CALCULATE` converts the row context into filter context via **context transition**, so the aggregation sees the correct per-group filter.

## When to Use This Pattern

- MAX, MIN, AVERAGE measures showing wrong totals
- Matrix visuals with subtotals and grand totals
- Any situation where "sum of groups" ≠ "grouped sum of aggregates"

## Variations

| Situation | Change |
|----------|--------|
| Multiple grouping columns | Add columns to SUMMARIZE: `SUMMARIZE(Table, Table[Col1], Table[Col2])` |
| DISTINCTCOUNT | Replace MAX with DISTINCTCOUNT; still needs CALCULATE for context transition |
| MEDIAN | MEDIAN does not support CALCULATE context transition — use `MEDIANX(SUMMARIZE(...), CALCULATE(MEDIAN(...)))` |

## Common Errors

- **Missing CALCULATE** → context transition doesn't fire; MAX returns the wrong aggregate per group
- **SUM instead of SUMX** → works but `SUMX(...,[AggPerGroup])` is the idiomatic iterator form
- **Forgetting to add all group columns** → subtotal rows collapse incorrectly

## Related

- [[Why Totals Look Wrong in DAX (and How to Fix Them)]] — `source` — general explanation of why totals differ from row sums
- [[measure-totals-problem-dax]] — `reference` — HASONEVALUE, ISINSCOPE guards for semi-additive measures
- [[context-transition-with-calculate]] — context transition mechanics
- [[sumx]] — SUMX iterator reference
- [[summarize]] — SUMMARIZE function reference
- [[Fix-Incorrect-Totals-Workflow]] — `workflow` — Power BI visual application steps
