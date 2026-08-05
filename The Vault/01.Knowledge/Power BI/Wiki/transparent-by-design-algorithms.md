---
created: 2026-07-28
updated: 2026-08-02
source: Artificial Intelligence with Power BI (Diepeveen)
note_type: atomic
tags: [transparent-algorithms, linear-regression, decision-tree, interpretability, explainability]
---

# Transparent-by-Design Algorithms

Linear regression and decision trees are inherently interpretable — their predictions can be traced back to specific input features directly.

## Definition

Transparent-by-design algorithms are those where the model's reasoning is directly visible from its structure — no post-hoc explanation required.

## Examples

| Algorithm | Why it's transparent |
|-----------|---------------------|
| **Linear regression** | Prediction = weighted sum of features; coefficients show each feature's contribution |
| **Logistic regression** | Same as linear regression with a sigmoid transform |
| **Decision tree** | Prediction = follow the path from root to leaf; each split is an explicit rule |
| **K-nearest neighbours** | Prediction = average of K similar training examples |
| **Naive Bayes** | Prediction = Bayes rule applied to feature counts |

## Examples of Opaque Algorithms

| Algorithm | Why it's opaque |
|-----------|---------------|
| Random Forest | Average of hundreds of decision trees |
| Gradient Boosting | Sequentially fitted trees; complex interactions |
| Neural Networks | Millions of weighted connections; no human-readable rules |

## Trade-off

Transparent algorithms are interpretable but often less accurate. Opaque algorithms are more accurate but require post-hoc explanation techniques (SHAP, LIME).

## Related

- [[explain-black-box-models]]
- [[feature-importance-aggregate-versus-individual]]
