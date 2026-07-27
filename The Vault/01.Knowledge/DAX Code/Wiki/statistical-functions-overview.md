---
created: 2026-07-26
source: dax.pdf
note_type: concept
tags: [dax, statistical-functions, aggregation, standard-deviation, variance]
---

# Statistical Functions in DAX

DAX includes aggregation, standard deviation, variance, and distribution functions.

## Aggregation Functions

### Simple Aggregations
SUM, AVERAGE, MIN, MAX, COUNT, COUNTA, COUNTBLANK, COUNTROWS

### Iterator Aggregations (X-suffix)
SUMX, AVERAGEX, MINX, MAXX, COUNTX, COUNTAX

### Counting
- **DISTINCTCOUNT**: Count unique values (most common statistical function)
- **DISTINCTCOUNTNOBLANK**: Distinct count excluding BLANK
- **APPROXIMATEDISTINCTCOUNT**: Memory-efficient distinct count for large datasets

### Geometric Mean
- **GEOMEAN**: Geometric mean of a column
- **GEOMEANX**: Geometric mean of an expression

```dax
Avg Growth Rate = GEOMEAN('Returns'[GrowthRate])
```

## Standard Deviation

| Function | Population/ Sample | Iterator |
|----------|-------------------|---------|
| STDEV.P | Population | STDEVX.P |
| STDEV.S | Sample | STDEVX.S |

- **STDEV.P** (population): Divide by N
- **STDEV.S** (sample): Divide by N-1

```dax
Pop StdDev = STDEV.P('Sales'[Amount])
Sample StdDev = STDEV.S('Sales'[Amount])
```

## Variance

| Function | Population/ Sample | Iterator |
|----------|-------------------|---------|
| VAR.P | Population | VARX.P |
| VAR.S | Sample | VARX.S |

```dax
Pop Variance = VAR.P('Sales'[Amount])
Sample Variance = VAR.S('Sales'[Amount])
```

## Distribution Functions

### Normal Distribution
- NORM.DIST, NORM.INV, NORM.S.DIST, NORM.S.INV

### Other Distributions
- BETA.DIST, BETA.INV
- CHISQ.DIST, CHISQ.INV, CHISQ.DIST.RT, CHISQ.INV.RT
- EXPON.DIST
- POISSON.DIST
- T.DIST, T.DIST.2T, T.DIST.RT, T.INV, T.INV.2T

### Confidence Intervals
- CONFIDENCE.NORM, CONFIDENCE.T

## LINEST (Linear Regression)

LINEST and LINESTX return statistics for a best-fit straight line:

```dax
LINEST('Sales'[Amount], 'Sales'[AdvertisingCost])
```

## SAMPLE

```dax
SAMPLE(<n>, <table>, <orderBy_expression>[, <order>])
```

Returns N random rows from a table.

## Key Formulas

```dax
-- Coefficient of Variation
CV = DIVIDE(STDEV.P('Sales'[Amount]), AVERAGE('Sales'[Amount]))

-- Z-Score
ZScore = DIVIDE([Amount] - AVERAGE('Sales'[Amount]), STDEV.P('Sales'[Amount]))
```

## Related

- [[sumx]]
- [[distinctcount]]
