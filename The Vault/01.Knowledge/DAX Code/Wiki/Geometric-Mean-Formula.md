---
created: 2026-08-08
updated: 2026-08-08
source: Calculating Geometric Mean in Power BI
note_type: atomic
tags: [power-bi, power-query, geometric-mean, statistics, mean]
---

# Geometric Mean — Definition & Formula

The geometric mean of *n* values is the *n*th root of their product. It is always less than or equal to the arithmetic mean and is most useful when values have a multiplicative rather than additive relationship.

## Formula

$$\text{Geometric Mean} = \left( \prod_{i=1}^{n} x_i \right)^{\frac{1}{n}}$$

In words: multiply all values together, then take the *n*th root.

## Behaviour Across Spread

| Values | Arithmetic Mean | Geometric Mean | Harmonic Mean |
|--------|---------------|----------------|---------------|
| 50, 50 | 50.00 | 50.00 | 50.00 |
| 40, 60 | 50.00 | 48.99 | 48.00 |
| 30, 70 | 50.00 | 45.83 | 42.00 |
| 20, 80 | 50.00 | 40.00 | 32.00 |

As the spread between values increases, the geometric mean decreases — but less aggressively than the harmonic mean. The geometric mean is most sensitive to the **proportional relationship** between values, not their absolute differences.

## When to Use

- **Growth rates** (compound growth, returns over time)
- **Ratios and indices** (ratios with multiplicative relationships)
- **Multi-reviewer rankings** (reduces influence of extreme outlier scores)
- Any dataset where values are multiplicative rather than additive

## Related

- [[Geometric-Mean-Zero-Negative-Limitation]] — limitation: zero/negative values
- [[Geometric-Mean-Multi-Reviewer-Rankings]] — ranking use case
