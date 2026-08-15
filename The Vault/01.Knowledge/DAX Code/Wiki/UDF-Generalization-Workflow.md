---
created: 2026-08-09
updated: 2026-08-09
source: "Creating functions for the like-for-like DAX pattern.md"
note_type: workflow
tags: [dax, user-defined-function, generalization, refactoring, pattern, library, model-independent]
---

# UDF Generalization: From Pattern to Reusable Library

Refactor a working DAX pattern into a model-independent user-defined function library in three stages. Based on the SQLBI like-for-like pattern article.

## Prerequisites

- Working DAX pattern in a semantic model
- Power BI Desktop (June 2026+), compatibility level 1702+
- DAX query view or TMDL view for Model Explorer

## When to Generalize

Apply this workflow when:
- A pattern has been implemented in two or more models with minor variations
- The pattern's business logic is stable and unlikely to change
- You want to share the pattern across a team

Do not generalize:
- One-off measures unlikely to be reused
- Patterns with model-grain assumptions that cannot be parameterized
- Patterns under active development — stabilize first, generalize later

## Stages

### Stage 1 — Encapsulate in Local.* Functions

Wrap the existing pattern code in model-dependent functions using the `Local.` prefix. Do not change the code — only wrap it.

```dax
-- Before: inline pattern measure
Same Store Sales =
    CALCULATETABLE(
        FILTER(
            ALLSELECTED(StoreStatus[StoreKey]),
            CALCULATE(SELECTEDVALUE(StoreStatus[Status])) = "Open"
        ),
        ALLSELECTED('Date')
    )
    ... more DAX

-- After: Local.* wrapper with no parameters
DEFINE
FUNCTION Local.SameStoreSales = () =>
    -- paste original measure code here, unchanged
    CALCULATETABLE(...)
    ...
```

**Goal:** The measure becomes `Same Store Sales = Local.SameStoreSales()`. The logic is identical, only the location changes.

### Stage 2 — Extract Model Objects as Parameters

Replace every hard-coded table or column name with a typed parameter. Name the function with a library namespace (e.g., `DaxPatterns.<Domain>.`).

```dax
DEFINE
-- Before: model-dependent
FUNCTION Local.StoreStatus = () =>
    CROSSJOIN(
        SUMMARIZE(Sales, 'Date'[Year]),
        ALLNOBLANKROW(Store[StoreKey])
    )
    ...

-- After: model-independent with ANYREF parameters
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

**ANYREF for columns/tables, EXPR for measures/expressions.**

Update the Local.* wrapper to call the new model-independent function:

```dax
FUNCTION Local.StoreStatus = () =>
    DaxPatterns.LikeForLike.EntityStatus(
        'Date'[Year],
        Store[StoreKey],
        Sales
    )
```

**Goal:** The business logic is now in a parameterizable function. Update the Local.* call to test.

### Stage 3 — Generalize Domain-Specific Terms

Rename domain-specific terminology to entity-generic terms. This is the step that makes the function reusable beyond its original use case.

| Domain-Specific | Entity-Generic |
|-----------------|---------------|
| StoreStatus | EntityStatus |
| StoreKey | entityKeyColumn |
| "Open" / "Closed" | "Active" / "Inactive" |
| Sales table | transactionTable |

The function now works for Product, Customer, or any comparable entity — no change to the business logic.

## Validation Checklist

Before finalizing:

- [ ] The model-dependent Local.* function produces the same numbers as the original inline pattern
- [ ] The model-independent library function works with the Local.* wrapper
- [ ] Measure reads as `= Local.<EntityName>([MeasureExpression])` — one parameter
- [ ] A second entity type (e.g., Product) has been implemented with the same library functions
- [ ] No hard-coded table or column names remain in the library function body

## Common Pitfalls

- **Forgetting EXPR for measure expressions:** if the measure expression uses CALCULATE inside the function, it must be passed as EXPR, not VAL
- **Keeping domain-specific terms:** "Open/Closed" limits the function to stores; "Active/Inactive" works for any entity
- **Parameter order confusion:** use descriptive parameter names inside the function; the Local.* wrapper provides the clarity

## Related

- [[Model-Dependent-vs-Model-Independent-UDFs]] — conceptual foundation
- [[Local-Wrapper-UDF-Pattern]] — the Local.* pattern
- [[DaxPatterns-LikeForLike-Library]] — full example of all three stages
- [[dax-udf-define-function-pattern]] — DEFINE FUNCTION syntax
- [[dax-udf-adoption-workflow]] — broader UDF adoption process
