---

created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
tags: ["dax", "pattern", "statistics", "regression", "slope", "intercept"]
note_type: pattern

---

# Regression Analysis in DAX

Implementing simple and multiple linear regression using DAX iterators.

## Purpose

Linear regression finds the best-fit line through data points, providing slope (rate of change) and intercept (starting value). Useful for trend analysis and forecasting.

## Simple Linear Regression

```dax
Slope :=
VAR __MeanX = AVERAGEX( 'Data', 'Data'[X] )
VAR __MeanY = AVERAGEX( 'Data', 'Data'[Y] )
RETURN
DIVIDE(
    SUMX( 'Data', ( 'Data'[X] - __MeanX ) * ( 'Data'[Y] - __MeanY ) ),
    SUMX( 'Data', POWER( 'Data'[X] - __MeanX, 2 ) )
)

Intercept :=
VAR __MeanX = AVERAGEX( 'Data', 'Data'[X] )
VAR __MeanY = AVERAGEX( 'Data', 'Data'[Y] )
RETURN
__MeanY - [Slope] * __MeanX

Predicted Y :=
VAR __x = [X]
RETURN
[Intercept] + [Slope] * __x
```

## Notes

- Uses the least-squares method to minimize squared errors
- `POWER(x, 2)` replaces x^2 in DAX
- `DIVIDE()` handles the zero-denominator edge case

## Related

- [[linear-interpolation-in-dax]]
- [[simple-linear-regression-in-dax]]

---

## Deckler Extension — LINEST and LINESTX (ch5)

DAX also provides native regression functions that return a **single-row table** with Slope, Intercept, and Coefficient of Determination:

```dax
Regression =
LINEST(
    'Advertising'[Sales ($ thousands)],
    'Advertising'[Advertising Spend ($ thousands)]
)
```

Returns a 10-column table. Key columns:

| Column | Description |
|--------|-------------|
| Slope1 | Gradient of the best-fit line |
| Intercept | y-intercept (value when x = 0) |
| CoefficientOfDetermination | R² — how well the line fits; 1 = perfect, 0 = none |

**Formula:** `y = mx + b` where `m = Slope1` and `b = Intercept`.

```dax
Regression Line =
    VAR __Slope     = MAX( 'Regression'[Slope1] )
    VAR __Intercept = MAX( 'Regression'[Intercept] )
    VAR __x         = MAX( 'Advertising'[Advertising Spend ($ thousands)] )
    VAR __Result    = __Slope * __x + __Intercept
    RETURN __Result
```

**Note:** LINEST / LINESTX take `y` (dependent) as first param, `x` (independent) as second — opposite of the covariance-based manual approach.

**Visualization:** Scatter chart — dots = actual data points; line = `Regression Line` measure plotted against the x-axis range.

**Source:** DAX for Humans (Greg Deckler, ch5) — dax4humans_ch5_regression.txt
