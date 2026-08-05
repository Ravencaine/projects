---
created: 2026-08-02
source: Power BI New User Defined Functions 10 Must-Have You'll Use in Every Report
note_type: function
tags: [dax, udf, variance, target, comparison, power-bi]
---

# VarAbs — Variance from Reference

Computes the absolute variance between an actual value and a reference (target or prior-period measure). Reference can be a budget/target column/measure or the output of `CompareOverPeriodRange`.

## Signature

```c
UDF VarAbs = ( actual : NUMERIC, reference : NUMERIC ) => actual - reference
```

## Usage

```c
// Variance vs. budget target
Sales Variance := VarAbs([Total Sales], [Sales Target])

// Variance vs. prior period
Sales Variance (MoM) :=
    VarAbs(
        [Total Sales],
        CompareOverPeriodRange([Total Sales], "MoM", "VALUE")
    )
```

## Pairs With

- [[statuscolor-udf-variance-based-status-color]] — color the variance output (red/gray/green)
- [[compareoverperiodrange-udf-whole-period-time-comparisons]] — reference prior-period values
