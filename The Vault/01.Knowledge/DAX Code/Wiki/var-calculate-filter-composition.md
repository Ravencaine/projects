---
created: 2026-08-01
updated: 2026-08-02
source: "Stop Repeating Yourself in DAX - The Power of Variables (VAR).md"
note_type: atomic
tags: [dax, var, calculate, filter, composition, beginner, intermediate]
---

# VAR with CALCULATE and FILTER

VAR composes naturally with `CALCULATE` and `FILTER` — variables store intermediate results that feed into context-modifying functions cleanly.

## VAR + CALCULATE: The Core Composition

CALCULATE modifies filter context. VAR stores intermediate values that CALCULATE can then use as filters or in the expression:

```dax
YoY Profit % =
VAR Revenue = SUM ( Sales[Revenue] )
VAR LY = CALCULATE ( SUM ( Sales[Revenue] ), SAMEPERIODLASTYEAR ( 'Date'[Date] ) )
RETURN
DIVIDE ( Revenue - LY, LY )
```

`CALCULATE` here is inside a VAR — not wrapping the final RETURN. This is a scalar use of CALCULATE within VAR.

## CALCULATE Wrapping RETURN: Adding a Filter

Use `CALCULATE` in the RETURN to add filter context on top of the VAR-defined measures:

```dax
Revenue This Year =
VAR Revenue = [Total Revenue]
RETURN
CALCULATE (
    Revenue,
    'Date'[Year] = YEAR ( TODAY() )
)
```

The variable `Revenue` holds the measure result; `CALCULATE` applies the year filter without needing to rewrite the measure logic.

## FILTER with Table Variables

Combine a table variable with `FILTER` to apply a pre-computed table as a filter:

```dax
High-Value Revenue =
VAR HighValueCustomers =
    FILTER (
        SUMMARIZE (
            Sales,
            Sales[Customer],
            "TotalSales", SUM ( Sales[Revenue] )
        ),
        [TotalSales] > 100000
    )
RETURN
CALCULATE (
    [Total Revenue],
    HighValueCustomers
)
```

The pre-computed `HighValueCustomers` table is evaluated once and applied as a filter by CALCULATE.

## CALCULATETABLE with Table Variables

For measures that return tables (not scalars), use `CALCULATETABLE` in the RETURN:

```dax
Top Products Table =
VAR TopProds =
    TOPN (
        10,
        SUMMARIZE ( Sales, Sales[Product], "Revenue", SUM ( Sales[Revenue] ) ),
        [Revenue],
        DESC
    )
RETURN
CALCULATETABLE (
    'Product',
    TopProds
)
```

## Scalar Variables Inside CALCULATE Filters

Variables holding scalar values can be passed directly into CALCULATE filter arguments:

```dax
Performance vs Target =
VAR Actual = [Total Revenue]
VAR Target = [Total Target]
VAR Gap = Actual - Target
RETURN
DIVIDE ( Gap, Target )
```

To add filter context to this measure:

```dax
Performance vs Target (Electronics) =
VAR Actual = [Total Revenue]
VAR Target = [Total Target]
VAR Gap = Actual - Target
RETURN
CALCULATE (
    DIVIDE ( Gap, Target ),
    'Product'[Category] = "Electronics"
)
```

## Self-Documenting Intermediate Results

The real benefit is clarity — every intermediate calculation has a name:

```dax
Revenue Achievement % =
VAR Actual     = [Total Revenue]
VAR Target     = [Total Target]
VAR LY         = [LY Revenue]
VAR Growth     = DIVIDE ( Actual - LY, LY )
VAR Ach        = DIVIDE ( Actual, Target )
RETURN
FORMAT ( Ach, "0%" ) & " | " & FORMAT ( Growth, "+0%;-0%;0%" )
```

Each line is immediately understandable. To change the LY calculation, change it in one place.

## Related

- [[var-syntax-and-pattern]] — basic VAR / RETURN syntax
- [[var-performance-benefit]] — why storing CALCULATE in VAR helps performance
- [[var-table-variables]] — table expressions as VAR
- [[calculate-context-modifier]] — deep dive on CALCULATE mechanics
