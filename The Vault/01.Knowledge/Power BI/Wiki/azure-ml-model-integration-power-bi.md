---
created: 2026-07-28
updated: 2026-08-02
source: Artificial Intelligence with Power BI (Diepeveen)
note_type: workflow
tags: [azure-ml, model-integration, power-bi, realtime-endpoint, score]
---

# Azure ML Model Integration in Power BI

Call a deployed Azure ML model from Power BI to add scored predictions to your reports.

## Prerequisites

- Azure ML model deployed to ACI or AKS
- REST endpoint URL and authentication key
- Power BI Desktop or Power BI Premium per-capacity license

## Steps

### 1. Enable Azure ML Integration in Power BI

Power BI Desktop → File → Options → Preview Features → Enable Azure ML model parameters

### 2. Get the Endpoint Details

From Azure ML Studio → Endpoints → select endpoint:
- REST endpoint URL
- Primary key

### 3. Enter Credentials in Power BI

Power Query Editor → Home → Get Data → Azure → Azure Machine Learning:
- Sign in with Azure credentials
- Select the workspace → the endpoint
- Power BI auto-discovers the input columns

### 4. Map Columns

Power BI shows the expected input columns:
- Map each input column from your dataset to the model's expected input
- Click Invoke to run the model

### 5. Expand Output

Power BI creates a new column with the model's output. Expand the record/list to extract individual predictions.

## Notes

- **Premium license required** for cloud refresh of Azure ML model calls
- Works natively in Power BI Desktop without Premium
- Input column types must match what the model expects (check schema in Azure ML)

## Related

- [[azure-ml-realtime-inference-pipeline]]
- [[deploy-automl-model-aci-endpoint]]
