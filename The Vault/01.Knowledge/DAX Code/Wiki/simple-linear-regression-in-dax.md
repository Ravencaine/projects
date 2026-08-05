---

created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
tags: ["dax", "pattern", "statistics", "regression", "trend"]
note_type: pattern

---

# Simple Linear Regression in DAX

Calculating trend lines and predictions using linear regression formulas.

## Purpose

Given paired data (x, y), find the relationship y = mx + b. This enables forecasting and trend analysis within Power BI.

## DAX Formulas

```dax
Slope (m) :=
VAR __n = COUNTROWS( 'Data' )
VAR __SumX = SUMX( 'Data', 'Data'[X] )
VAR __SumY = SUMX( 'Data', 'Data'[Y] )
VAR __SumXY = SUMX( 'Data', 'Data'[X] * 'Data'[Y] )
VAR __SumX2 = SUMX( 'Data', 'Data'[X] ^ 2 )
RETURN
DIVIDE( __n * __SumXY - __SumX * __SumY, __n * __SumX2 - __SumX ^ 2 )

Intercept (b) :=
VAR __n = COUNTROWS( 'Data' )
VAR __SumX = SUMX( 'Data', 'Data'[X] )
VAR __SumY = SUMX( 'Data', 'Data'[Y] )
RETURN
DIVIDE( __SumY - [Slope] * __SumX, __n )

Prediction :=
VAR __x = [InputX]
RETURN
[Intercept] + [Slope] * __x
```

## Notes

- Requires paired observations of independent (x) and dependent (y) variables
- The R-squared value indicates how well the line fits the data
- For time series, x is typically the time period number

## Related

- [[regression-analysis-in-dax]]
- [[linear-interpolation-in-dax]]
