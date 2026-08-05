---
created: 2026-07-28
updated: 2026-08-02
source: Artificial Intelligence with Power BI (Diepeveen)
note_type: atomic
tags: [deep-learning, neural-network, artificial-neural-network, gpu, unstructured-data]
---

# Deep Learning — Artificial Neural Networks

Deep learning uses layered artificial neural networks to learn hierarchical features from data, especially unstructured data.

## Definition

Deep Learning (DL) is a specialised subset of ML using artificial neural networks (ANNs) with multiple hidden layers. These layers progressively extract higher-level features from raw input — images, audio, text — without manual feature engineering.

## Key Points

- **ANNs mimic the brain**: layers of interconnected nodes (neurons) with weighted connections
- **Depth matters**: more layers let the model learn hierarchical representations (edges → shapes → objects in images)
- **GPU advantage**: matrix multiplication at scale makes DL practical; cloud computing democratises access
- **No manual feature engineering**: unlike traditional ML, DL derives its own features from raw data
- Trade-off: more accurate but less transparent (black-box models)

## Examples

- Azure Computer Vision: image description, object detection
- Azure Cognitive Services speech and language APIs
- Azure Custom Vision: custom image classifiers trained with labelled photos
- SR-CNN (Spectral Residual-Convolutional Neural Network) used by Power BI's anomaly detection

## Related

- [[ai-as-umbrella-term]]
- [[machine-learning-algorithm-plus-data-equals-model]]
- [[explain-black-box-models]]
- [[pytorch-deep-learning-framework]]
