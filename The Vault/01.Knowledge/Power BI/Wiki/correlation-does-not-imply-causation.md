---
created: 2026-07-28
updated: 2026-08-02
source: Artificial Intelligence with Power BI (Diepeveen)
note_type: gotcha
tags: [correlation, causation, scatter-plot, statistics, misleading]
---

# Correlation ≠ Causation

A scatter plot shows that two variables move together — it does not prove that one causes the other.

## Expected Behaviour

A strong positive correlation between Life Ladder and Healthy Life Expectancy means: "countries with higher life expectancy tend to have higher Life Ladder scores."

## Actual Behaviour

The scatter plot cannot tell you *why*. It could be that higher life expectancy causes greater happiness. Or a third variable (e.g., national wealth) drives both. Or it's coincidence.

## Why It Happens

Correlation measures association, not mechanism. The relationship could be:
- A causes B
- B causes A
- A and B are both caused by C (confounding variable)
- Random coincidence (especially in small datasets)

## How to Handle It

- Always use **domain knowledge** to interpret correlations
- Check for confounding variables before drawing causal conclusions
- Design controlled experiments or use causal inference techniques when causation matters
- Power BI scatter plots show the association — the analyst provides the explanation

## Related

- [[scatter-plot-trend-line-correlation]]
- [[fair-models-identify-mitigate-unfairness]]
