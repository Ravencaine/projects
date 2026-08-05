---
created: 2026-07-28
updated: 2026-08-02
source: Artificial Intelligence with Power BI (Diepeveen)
note_type: workflow
tags: [azure-ml-designer, deploy, realtime-endpoint, aci, designer]
---

# Deploy Real-Time Endpoint from Azure ML Designer

Deploy a real-time inference pipeline from the Designer directly to ACI.

## Prerequisites

- Completed real-time inference pipeline in Azure ML Designer
- Azure ML workspace with sufficient quota for ACI

## Steps

### From the Designer

1. Open the real-time inference pipeline
2. Click **Submit** (bottom of canvas) to run the pipeline
3. After successful run → **Deploy**

### Deploy Configuration

| Setting | Value |
|---------|-------|
| Compute type | Azure Container Instance (ACI) |
| Endpoint name | descriptive (e.g., `housing-price-prediction`) |
| Enable Application Insights | Recommended (Yes) |
| Advanced settings | Leave default unless custom |

### Get Endpoint Details

After deployment (Endpoints → select endpoint):
- **REST endpoint URL**
- **Primary key** (Authentication)
- Application Insights connection string (for monitoring)

### Test the Endpoint

```bash
curl -X POST "<endpoint-url>" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <key>" \
  -d '{"data": [[val1, val2, ...]]}'
```

## Notes

- ACI is suitable for development and low-traffic production
- For production with high traffic, redeploy to AKS (Azure Kubernetes Service)

## Related

- [[azure-ml-realtime-inference-pipeline]]
- [[integrate-azure-ml-endpoint-power-bi]]
- [[azure-ml-endpoints-aci-versus-aks]]
