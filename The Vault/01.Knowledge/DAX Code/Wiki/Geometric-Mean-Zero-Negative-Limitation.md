---
created: 2026-08-08
updated: 2026-08-08
source: Calculating Geometric Mean in Power BI
note_type: atomic
tags: [power-bi, power-query, geometric-mean, zero, negative, limitation]
---

# Geometric Mean — Zero and Negative Values Limitation

The geometric mean **breaks when any value in the dataset is zero or negative**. This is a mathematical constraint, not a Power BI limitation.

## Why Zero Breaks It

The geometric mean formula requires taking the *n*th root of a product:

$$\text{GM} = \left(\prod x_i\right)^{1/n}$$

If any single value = 0, the entire product = 0, regardless of the other values → meaningless geometric mean.

## Why Negative Values Break It

Taking the root of a negative product produces a complex number (e.g., the cube root of -8 = -2, but the square root of -8 has no real solution). This makes the result undefined for most analytical purposes.

## Practical Implication

Before applying the geometric mean technique, **filter or validate the data** to ensure all values are strictly positive (> 0).

## Related

- [[Geometric-Mean-Formula]] — formula and use cases
- [[Geometric-Mean-Power-Query]] — implementation (with this prerequisite)
