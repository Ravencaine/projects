---
created: 2026-08-02
updated: 2026-08-05
source: How to Build a Correlation Matrix in Power BI Using Only DAX
note_type: atomic
tags: [statistics, correlation, pearson, concept]
---

# Pearson Correlation Coefficient

A measure of linear relationship between two numeric variables, ranging from -1 to +1.

## Definition

The Pearson correlation coefficient (r) standardises the covariance of two variables by their standard deviations:

```
r = Σ[(Xi - μX)(Yi - μY)] / √[ Σ(Xi - μX)² × Σ(Yi - μY)² ]
```

## Key Points

- **+1** — perfect positive correlation: variables increase together
- **0** — no linear relationship
- **-1** — perfect negative correlation: one increases as the other decreases
- The value is symmetric: `r(X, Y) = r(Y, X)`
- The diagonal of a correlation matrix is always 1 (a variable correlates perfectly with itself)
- Sensitive to outliers: extreme values can pull r toward ±1 even with few data points

## Interpretation Buckets

| |r| range | Strength |
|---|---|---|
| 0.00 – 0.10 | negligible / none |
| 0.10 – 0.30 | low / weak |
| 0.30 – 0.50 | medium / moderate |
| 0.50 – 0.70 | medium-high |
| 0.70 – 1.00 | high / strong |

## Related

- [[pearson-correlation-coefficient-in-dax]] — `pattern` — DAX implementation
- [[correlation-matrix-in-power-bi-dax-only]] — `pattern` — full matrix using this measure
- [[correlation-does-not-imply-causation]] — `atomic` — related Power BI KB note on interpreting correlations
