---
created: 2026-08-09
updated: 2026-08-09
source: "Creating functions for the like-for-like DAX pattern.md"
note_type: atomic
tags: [dax, user-defined-function, model-independent, model-dependent, parameters, abstraction]
---

# Model-Dependent vs Model-Independent UDFs

The fundamental distinction in DAX user-defined function design: model-dependent functions know the structure of the semantic model; model-independent functions are completely agnostic to it.

## Model-Dependent UDF

A function that references tables, columns, or measures that exist in a specific model. The function body contains hard-coded model objects.

```dax
-- Model-dependent: references StoreStatus table, Store[StoreKey], 'Date'[Year]
DEFINE
FUNCTION Local.StoreStatus = () =>
    VAR AllStores = CROSSJOIN(
        SUMMARIZE(Sales, 'Date'[Year]),
        ALLNOBLANKROW(Store[StoreKey])
    )
    VAR OpenStores = SUMMARIZE(Sales, 'Date'[Year], Sales[StoreKey])
    RETURN
        UNION(
            ADDCOLUMNS(OpenStores, "Status", "Open"),
            ADDCOLUMNS(EXCEPT(AllStores, OpenStores), "Status", "Closed")
        )
```

Works only in the model where `StoreStatus`, `Store[StoreKey]`, and `'Date'[Year]` exist. Copying to another model would break unless those exact objects exist there.

## Model-Independent UDF

A function that receives every model object as a parameter. The function body contains no hard-coded table or column references.

```dax
-- Model-independent: all model objects are parameters
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

Works in any model — just pass the correct columns and tables at the call site.

## Naming Convention

| Prefix | Role | Example |
|--------|------|---------|
| `Local.` | Model-dependent wrapper | `Local.StoreStatus`, `Local.ProductStatus` |
| `DaxPatterns.<Domain>.` | Model-independent library | `DaxPatterns.LikeForLike.EntityStatus` |

The `Local.` prefix is a convention from SQLBI to mark the thin model-specific layer that sits between the library function and the model.

## Why Model-Independent Matters

1. **Centralization:** update the library function once, all models benefit
2. **Shareability:** publish to the community without model-specific assumptions
3. **Generalization:** the same function works for Store, Product, Customer, or any entity
4. **Clarity:** business logic (what to compute) is separated from model details (what to read)

## The Generalization Path

Domain-specific → Parameterized → Entity-generic:

```
StoreStatus (hard-coded)                    → StoreStatus (parameterized)          → EntityStatus (generic)
OpenStores ("Open"/"Closed")                → OpenStores (Active/Inactive)        → OpenEntities (any status)
[Store] columns                             → [Store] columns passed as params     → entityKeyColumn / entityStatusKeyColumn
```

## Relationship to VAL/EXPR

VAL and EXPR are about **parameter evaluation timing** (whether a parameter is evaluated before or after context transition). Model-dependent/independent is about **what the function knows about the model**. These are orthogonal axes.

## Related

- [[dax-udf-define-function-pattern]] — DEFINE FUNCTION syntax
- [[dax-udf-adoption-workflow]] — when to create each type
- [[val-vs-expr-parameter-evaluation]] — VAL vs EXPR (orthogonal dimension)
