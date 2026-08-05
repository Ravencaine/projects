---
created: 2026-07-28
updated: 2026-08-02
source: Artificial Intelligence with Power BI (Diepeveen)
note_type: workflow
tags: [azure-ml, workspace, compute-cluster, dataset, setup, automl]
---

# Azure ML Workspace — Create Workspace, Compute Cluster, and Dataset

Prerequisites for running AutoML in Azure Machine Learning.

## Prerequisites

- Azure subscription
- Contributor access to the Azure subscription

## Steps

### 1. Create Workspace

Azure Portal → Create a Resource → AI + Machine Learning → Machine Learning:
- Workspace name: e.g., `diepeveen-ai-powerbi`
- Subscription, Resource Group, Region
- Storage account: auto-created or select existing
- Key Vault: auto-created
- Application Insights: auto-created
- Container Registry: auto-created (or None for basic tier)
- Review + Create

### 2. Create Compute Cluster

Azure ML Studio (ml.azure.com) → Manage → Compute → Compute clusters → New:
- Compute name: e.g., `cpu-cluster`
- Virtual machine type: CPU (Standard_DS3_v2) or GPU
- Minimum nodes: 0 (scale to zero when idle)
- Maximum nodes: 2 (keep costs low)
- Enable SSH access: No (not needed for AutoML)

### 3. Create Dataset

Azure ML Studio → Assets → Datasets → Create:
- **Tabular**: connect to data source (Blob Storage, SQL DB, Web URL)
- **File**: point to files in Blob Storage
- Set column types and schema
- Register the dataset in the workspace

## Notes

- Compute clusters scale to 0 when idle — no cost when not running
- Datasets are versioned in Azure ML — always use the registered dataset name in AutoML runs
- Workspace settings persist — compute and datasets are reusable across experiments

## Related

- [[automl-run-configuration]]
- [[automl-overview]]
