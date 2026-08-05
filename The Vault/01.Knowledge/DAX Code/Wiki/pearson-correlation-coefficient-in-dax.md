---
created: 2026-08-02
updated: 2026-08-05
source: How to Build a Correlation Matrix in Power BI Using Only DAX
note_type: pattern
tags: [dax, statistics, correlation, pearson, measure]
---

# Pearson Correlation Coefficient in DAX

Implements the Pearson correlation coefficient using only DAX iteration functions — no external libraries required.

## Purpose

Quantify the linear relationship between two numeric variables as a single value in [-1, +1]. The DAX implementation follows the covariance-over-product-of-standard-deviations formula.

## Components

- **`SUMMARIZE`** — builds per-employee row context
- **`ADDCOLUMNS`** — adds X and Y numeric columns
- **`SWITCH (TRUE())`** — maps variable name strings to their numeric values
- **`FILTER`** — removes rows with blank X or Y
- **`AVERAGEX`** — computes mean of X and mean of Y
- **`SUMX`** — computes numerator (covariance sum) and denominator (sqrt of product of variance sums)
- **`SQRT`** — denominator correction

## Structure

```
Pearson r = Σ[(Xi - μX)(Yi - μY)] / √[ Σ(Xi - μX)² × Σ(Yi - μY)² ]
```

DAX equivalent:

```dax
VAR AvgX = AVERAGEX ( Clean, [X] )
VAR AvgY = AVERAGEX ( Clean, [Y] )
VAR Num  = SUMX ( Clean, ( [X] - AvgX ) * ( [Y] - AvgY ) )
VAR Den  = SQRT ( SUMX ( Clean, ( [X] - AvgX ) ^ 2 ) * SUMX ( Clean, ( [Y] - AvgY ) ^ 2 ) )
RETURN IF ( 0 = COUNTROWS ( Clean ), BLANK(), Num / Den )
```

## Key Behaviour

- Returns `BLANK()` when either variable has no data (division guard: `IF ( 0 = N, ... )`)
- Handles `BLANK()` rows via `FILTER ( WithXY, NOT ISBLANK ( [X] ) && NOT ISBLANK ( [Y] ) )`
- Fully dynamic: X and Y are determined at query time via `SELECTEDVALUE` on disconnected selector tables

## Related

- [[correlation-matrix-in-power-bi-dax-only]] — `pattern` — end-to-end matrix using this formula
- [[pearson-correlation-coefficient]] — `atomic` — the statistical concept
- [[dax-sumx-function]] — `function` — row-by-row iteration with expression
- [[average]] — `function` — iterator for averages
