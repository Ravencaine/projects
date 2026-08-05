---
created: 2026-08-02
source: What Scatter Plots Tell You That Summary Statistics Hide
note_type: pattern
tags: [powerbi, pattern, data-visualization, scatter-plot, loess, regression, confidence-band, trend]
---

# Reading Scatter Plots: LOESS, Linear/Logistic Regression, Confidence Bands, Trend/Groups/Outliers

Three things to scan for in every scatter plot: **trend** (shape of relationship), **groups** (hidden populations), **outliers** (errors or the most interesting cases).

**Adding a guide for the eye:**

| Fit type | When to use |
|----------|-------------|
| **LOESS** (locally estimated scatterplot smoothing) | Default for exploratory work — flexible wire threads through data, reveals bends without imposing a formula |
| **Linear regression** | Only when the underlying relationship is genuinely linear — forces a straight line |
| **Logistic regression** | Binary outcome (Success/Fail, Yes/No) — produces S-curve modeling probability |

**Confidence bands:** The grey ribbon around a fitted line shows uncertainty in the estimate. Narrow band = enough data to be confident. Wide, flaring band = "not enough observations here to know where the trend really goes" — a warning, not decoration.

**Pattern reading checklist:**
- Trend: linear, curved, saturating, or flat?
- Groups: one population or several mixed together? (Often a hidden categorical variable)
- Outliers: data error or the most interesting observation in the whole dataset?

**Prefer LOESS over linear** unless you have prior reason to believe the relationship is linear — linear forces a shape that may not exist.
