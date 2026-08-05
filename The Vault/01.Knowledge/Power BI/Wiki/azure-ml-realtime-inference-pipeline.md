---
created: 2026-07-28
updated: 2026-08-02
source: Artificial Intelligence with Power BI (Diepeveen)
note_type: workflow
tags: [azure-ml-designer, realtime-inference, pipeline, deployment, inference]
---

# Azure ML Real-Time Inference Pipeline

Convert a training pipeline into a real-time inference pipeline for production scoring.

## Purpose

A training pipeline includes all preprocessing steps (clean, normalise, split). An inference pipeline wraps the trained model with the same preprocessing so new data gets the same treatment before scoring.

## Steps

### 1. Start from Training Pipeline

Complete and run the training pipeline in Azure ML Designer.

### 2. Create Inference Pipeline

Training pipeline → Create inference pipeline → Real-time inference pipeline

The Designer automatically:
- Removes the Split Data and Evaluate Model components
- Adds a **Web Service Input** (for new data)
- Adds a **Web Service Output** (for predictions)
- Wraps preprocessing steps around the trained model

### 3. Edit Inference Pipeline

1. Connect the Web Service Input to the preprocessing steps
2. Ensure the preprocessing parameters match the training run
3. Verify the model output is connected to Web Service Output
4. Submit the inference pipeline

### 4. Deploy

Inference pipeline → Deploy → Deploy to Azure Container Instance (ACI)

## Output

A REST endpoint accepting new data and returning predictions in real time.

## Related

- [[deploy-realtime-endpoint-designer]]
- [[integrate-azure-ml-endpoint-power-bi]]
- [[batch-versus-realtime-inference]]
