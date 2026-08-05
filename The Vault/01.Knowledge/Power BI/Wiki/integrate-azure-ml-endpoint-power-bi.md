---
created: 2026-07-28
updated: 2026-08-02
source: Artificial Intelligence with Power BI (Diepeveen)
note_type: workflow
tags: [azure-ml, real-time, endpoint, power-bi, azure-ml-integration]
---

# Integrate Azure ML Real-Time Endpoint in Power BI

Call a deployed real-time inference endpoint from Power BI to score new data.

## Prerequisites

- Azure ML real-time endpoint deployed (ACI or AKS)
- REST endpoint URL + authentication key
- Power BI Desktop or Premium per-capacity license

## Steps

### 1. Enable Azure ML Integration

Power BI Desktop → File → Options → Preview → Enable Azure ML model parameters

### 2. Connect via Azure ML Integration

Power Query Editor → Home → Get Data → Azure → Azure Machine Learning:
1. Sign in with Azure credentials
2. Select Subscription → Resource Group → Workspace → Endpoint
3. Power BI auto-discovers input parameters

### 3. Map Columns

Power BI shows the expected input schema:
- Map each required input column from your dataset
- All inputs must be provided for the model to score

### 4. Invoke

Click Invoke → Power BI adds a custom column with the model's scored output

### 5. Expand Output

The output is a record. Expand to extract:
- Predicted value (for regression)
- Probability scores (for classification)
- Class label (for classification)

## Notes

- Works in Power BI Desktop without Premium
- Cloud refresh requires **Premium per-capacity** (not per-user)
- Input types must match — check the model's expected schema in Azure ML Studio

## Related

- [[azure-ml-realtime-inference-pipeline]]
- [[deploy-realtime-endpoint-designer]]
- [[batch-versus-realtime-inference]]
