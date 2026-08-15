---
created: 2026-08-09
updated: 2026-08-09
source: "Creating functions for the like-for-like DAX pattern.md"
note_type: pattern
tags: [dax, user-defined-function, like-for-like, pattern, daxpatterns, library, entity, active, inactive]
---

# Like-for-Like UDF Library (DaxPatterns.LikeForLike)

A three-function model-independent library for like-for-like comparison across any entity (Store, Product, Customer, etc.). From SQLBI's "Creating Functions for the Like-for-Like DAX Pattern."

## Purpose

Like-for-like comparison filters a measure to only include entities that were active throughout the entire selected time period. For stores: only stores open in every year are included in year-over-year comparisons. This pattern applies to any entity that can be active or inactive across time.

## EntityStatus Table Function

Creates a calculated-table function returning entity status (Active/Inactive) per period.

```dax
/// Returns a table with EntityKey and Status ("Active" or "Inactive") for each
/// year, based on whether the entity had transactions in all selected years.
DEFINE
FUNCTION DaxPatterns.LikeForLike.EntityStatus = (
    dateYearNumberColumn : ANYREF,
    entityColumn : ANYREF,
    transactionTable : ANYREF
) =>
    VAR AllEntities = CROSSJOIN(
        SUMMARIZE(transactionTable, dateYearNumberColumn),
        ALLNOBLANKROW(entityColumn)
    )
    VAR OpenEntities = SUMMARIZE(
        transactionTable,
        dateYearNumberColumn,
        entityColumn
    )
    RETURN
        UNION(
            ADDCOLUMNS(OpenEntities, "Status", "Active"),
            ADDCOLUMNS(EXCEPT(AllEntities, OpenEntities), "Status", "Inactive")
        )
```

## ComputeForSameEntity Measure Function

Filters a measure to only active entities (those active throughout the selected period).

```dax
/// Filters formulaExpr to only entities active across all selected periods.
/// entityStatusKeyColumn: key column in the status table (e.g., ProductStatus[ProductKey])
/// entityStatusStatusColumn: status column in the status table (e.g., ProductStatus[Status])
/// entityKeyColumn: key column in the dimension table (e.g., Product[ProductKey])
/// dateTable: the date table reference (e.g., 'Date')
/// formulaExpr: the measure expression to filter (EXPR type — evaluated at call site)
DEFINE
FUNCTION DaxPatterns.LikeForLike.ComputeForSameEntity = (
    entityStatusKeyColumn : ANYREF,
    entityStatusStatusColumn : ANYREF,
    entityKeyColumn : ANYREF,
    dateTable : ANYREF,
    formulaExpr : EXPR
) =>
    VAR OpenEntities = CALCULATETABLE(
        FILTER(
            ALLSELECTED(entityStatusKeyColumn),
            CALCULATE(
                SELECTEDVALUE(entityStatusStatusColumn)
            ) = "Active"
        ),
        ALLSELECTED(dateTable)
    )
    VAR FilterOpenEntities = TREATAS(
        OpenEntities,
        entityKeyColumn
    )
    VAR Result = CALCULATE(
        formulaExpr,
        KEEPFILTERS(FilterOpenEntities)
    )
    RETURN
        Result
```

## StoreStatus Calculated Table (Model-Specific Instance)

```dax
StoreStatus = DaxPatterns.LikeForLike.EntityStatus(
    'Date'[Year],
    Store[StoreKey],
    Sales
)
```

## ComputeForSameStore Measure (Model-Specific Instance)

```dax
Same Store Sales = DaxPatterns.LikeForLike.ComputeForSameEntity(
    StoreStatus[StoreKey],
    StoreStatus[Status],
    Store[StoreKey],
    'Date',
    [Sales Amount]
)
```

## Extending to Product

```dax
-- Calculated table
ProductStatus = DaxPatterns.LikeForLike.EntityStatus(
    'Date'[Year],
    Product[ProductKey],
    Sales
)

-- Measure
Same Product Sales = DaxPatterns.LikeForLike.ComputeForSameEntity(
    ProductStatus[ProductKey],
    ProductStatus[Status],
    Product[ProductKey],
    'Date',
    [Sales Amount]
)
```

The entire business logic is handled by the library functions — only the column/table mapping changes.

## Anatomy of the Pattern

| Component | Role |
|-----------|------|
| `SUMMARIZE(transactionTable, dateYearNumberColumn)` | Find all entity-period combinations with transactions |
| `ALLNOBLANKROW(entityColumn)` | Include entities with at least one transaction |
| `EXCEPT(AllEntities, OpenEntities)` | Find entities missing from at least one period |
| `CALCULATETABLE(FILTER(ALLSELECTED(...), CALCULATE(SELECTEDVALUE(...))="Active"))` | Keep entities with Status=Active in every selected period |
| `TREATAS(OpenEntities, entityKeyColumn)` | Re-target the filter context to the dimension table |

## Generalization from Store to Entity

The key insight is replacing domain-specific terms:

- StoreKey → entityKeyColumn
- OpenStores → OpenEntities
- "Open"/"Closed" → "Active"/"Inactive"
- Store[StoreKey] → entityColumn

This allows a single library function to work for any comparable entity dimension.

## Related

- [[Model-Dependent-vs-Model-Independent-UDFs]] — the distinction that makes this work
- [[Local-Wrapper-UDF-Pattern]] — the Local.* wrapper pattern
- [[dax-udf-define-function-pattern]] — DEFINE FUNCTION syntax
- [[TREATAS]] — virtual relationship for re-targeting filter context
- [[KEEPFILTERS]] — preserves outer filter context within CALCULATE
