---
created: 2026-08-01
updated: 2026-08-02
source: "Understanding EARLIER in DAX The Time Machine You Didn't Know You Had.md"
note_type: atomic
tags: [dax, earlier, real-world, ranking, running-total, calculated-columns]
---

# EARLIER Real-World Patterns

## Pattern 1: Running Total by Group

Classic use case — cumulative sum partitioned by a category.

```c
Running Total :=
VAR CurrentCustomer = Sales[Customer]
VAR CurrentMonth    = Sales[Month]
RETURN
    CALCULATE(
        SUM(Sales[Sales]),
        FILTER(
            ALL(Sales),
            Sales[Customer] = CurrentCustomer &&
            Sales[Month]    <= CurrentMonth
        )
    )
// Note: CALCULATE above works as a measure or column
// Using EARLIER in a calculated column instead:
Running Total Col =
CALCULATE(
    SUM(Sales[Sales]),
    FILTER(
        Sales,
        Sales[Customer] = EARLIER(Sales[Customer]) &&
        Sales[Month]    <= EARLIER(Sales[Month])
    )
)
```

## Pattern 2: Customer Purchase Ranking

Rank each customer's purchases within their own context.

```c
Rank by Customer :=
RANKX(
    FILTER(Sales, Sales[Customer] = EARLIER(Sales[Customer])),
    Sales[Sales],
    ,
    DESC
)
```

- `FILTER` creates inner context
- `EARLIER(Sales[Customer])` captures outer context value
- `RANKX` ranks by `Sales` within each customer's filtered set

**Limitation:** This pattern only works in calculated columns. Moving to a measure requires refactoring with VAR + a base measure.

## Pattern 3: Count of Rows Up To Current

Count how many rows existed up to and including the current row.

```c
Row Count :=
CALCULATE(
    COUNTROWS(Sales),
    FILTER(
        Sales,
        Sales[Customer] = EARLIER(Sales[Customer]) &&
        Sales[Date]    <= EARLIER(Sales[Date])
    )
)
```

## Pattern 4: Flagging First/Last Occurrence

```c
Is First Purchase :=
VAR CurrCustomer = Sales[Customer]
VAR CurrDate     = Sales[Date]
RETURN
    CALCULATE(
        COUNTROWS(Sales),
        FILTER(
            ALL(Sales),
            Sales[Customer] = CurrCustomer &&
            Sales[Date]     < CurrDate
        )
    ) = 0
// Result: TRUE for the earliest purchase per customer
```

## When NOT to Use EARLIER

| Situation | Use Instead |
|-----------|------------|
| Measure-level logic | VAR + base measure |
| Need to reference outside current row | `MAX()`, `LOOKUPVALUE()`, `RELATED()` |
| Cross-table context | `CALCULATE` with `FILTER(ALL(...))` |
| Complex nested iterations | Refactor into separate base measures |

EARLIER is a calculated-column tool. Once logic needs to live in measures or respond to visual filter contexts, VAR is the modern replacement.
