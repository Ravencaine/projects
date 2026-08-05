---
created: 2026-07-28
updated: 2026-08-02
source: Artificial Intelligence with Power BI (Diepeveen)
note_type: workflow
tags: [automl, deploy, aci, azure-container-instance, endpoint, power-bi]
---

# Deploy AutoML Model to ACI Endpoint

After AutoML training completes, deploy the best model to an Azure Container Instance (ACI) for real-time scoring.

## Prerequisites

- Completed AutoML run with a registered model
- Model selected from the AutoML run's Models tab
- Registered model in Azure ML workspace

## Steps

### 1. Select the Best Model

AutoML run → Models tab → select the best model (sorted by primary metric) → Deploy → Deploy to web service

### 2. Configure Deployment

| Setting | Value |
|---------|-------|
| Compute type | Azure Container Instance (ACI) |
| Name | descriptive (e.g., `tourism-forecast-v1`) |
| Authentication | Token-based (recommended) |
| Application Insights | Enable (for monitoring) |

### 3. Wait for Deployment

Deployment typically takes 5–15 minutes. Status shown in the Endpoints tab.

### 4. Get Endpoint Details

After deployment, note from the endpoint details:
- **REST endpoint URL**
- **Primary key** (for authentication)

These go into Power BI's Azure ML integration.

## Notes

- **ACI is for development/testing**: production should use Azure Kubernetes Service (AKS)
- **ACI auto-scales to 3 replicas max**: for higher throughput, redeploy to AKS
- Deployment status can be monitored via Application Insights

## Related

- [[azure-ml-model-integration-power-bi]]
- [[azure-ml-endpoints-aci-versus-aks]]
