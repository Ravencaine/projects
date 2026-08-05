---
created: 2026-07-28
updated: 2026-08-02
source: Artificial Intelligence with Power BI (Diepeveen)
note_type: atomic
tags: [azure-ml-designer, drag-and-drop, ml-pipeline, visual-interface]
---

# Azure ML Designer — Drag-and-Drop ML Pipeline

A visual interface for building ML pipelines without writing code — components are dragged onto a canvas and connected.

## Definition

Azure ML Designer is a GUI-based ML workbench. Pipelines are built by dragging components (data ingestion, transforms, algorithms, training, scoring) onto a canvas and connecting them. It generates Python code under the hood but abstracts it completely.

## Key Points

- **No code required**: every component is a visual block
- **Under-the-hood Python**: the Designer generates runnable Python scripts from your pipeline
- **Full ML lifecycle**: data ingestion, feature engineering, model training, evaluation, deployment
- **Compared to AutoML**: Designer gives you manual control over each step; AutoML automates the entire pipeline

## When to Use Designer vs AutoML

| Scenario | Use |
|---------|-----|
| Quick model with minimal config | AutoML |
| Need specific algorithm or feature engineering | Designer |
| Want to understand pipeline steps | Designer |
| Experimenting with multiple preprocessing options | Designer |

## Related

- [[azure-ml-designer-pipeline-components]]
- [[azure-ml-realtime-inference-pipeline]]
- [[train-evaluate-regression-model-designer]]
