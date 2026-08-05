---
created: 2026-07-28
updated: 2026-08-02
source: Artificial Intelligence with Power BI (Diepeveen)
note_type: atomic
tags: [supervised-learning, unsupervised-learning, labeled-data, clustering, regression, classification]
---

# Supervised vs Unsupervised Learning

The fundamental divide in ML: whether the training data includes labels (supervised) or not (unsupervised).

## Definition

- **Supervised Learning**: the training data includes the correct answer (label) for each observation. The model learns to map inputs to known outputs.
- **Unsupervised Learning**: no labels are provided. The model finds structure — groups, patterns, anomalies — purely from the data itself.

## Key Points

- Supervised = "learning with a teacher"; unsupervised = "finding structure without guidance"
- Supervised tasks: **regression** (predict a number) and **classification** (predict a category)
- Unsupervised tasks: **clustering** (group similar points), **anomaly detection** (find rare events)
- Azure Cognitive Services and Power BI's anomaly detection use unsupervised methods — no labelled examples needed
- Clustering algorithms (e.g., K-means) group data points by similarity; no "correct" answer is provided

## Examples

- Supervised (classification): predicting whether a bank customer will churn or stay — labels are historical churn outcomes
- Supervised (regression): predicting a house price from its features — the price is the known label
- Unsupervised (clustering): K-means clustering customer records to discover market segments without pre-defining the segments
- Unsupervised (anomaly detection): Power BI flags unexpected spikes in tourism data without labelled "anomaly" examples

## Related

- [[machine-learning-algorithm-plus-data-equals-model]]
- [[regression-classification-clustering]]
- [[anomaly-detection-supervised-versus-unsupervised]]
- supervised-versus-unsupervised-learning
