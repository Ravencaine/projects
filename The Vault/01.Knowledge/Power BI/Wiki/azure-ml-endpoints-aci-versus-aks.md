---
created: 2026-07-28
updated: 2026-08-02
source: Artificial Intelligence with Power BI (Diepeveen)
note_type: atomic
tags: [azure-ml, endpoints, aci, aks, deployment-targets]
---

# Azure ML Endpoints — ACI vs AKS

Two Azure compute targets for deploying ML models: Azure Container Instances (ACI) for dev/test, Azure Kubernetes Service (AKS) for production.

## Definition

| Target | Type | Use case | Scale |
|--------|------|---------|-------|
| **ACI** | Single container instance | Dev, test, demos | Low (1–3 replicas) |
| **AKS** | Managed Kubernetes cluster | Production | High (auto-scale to 100s) |

## ACI (Azure Container Instance)

- **Single container**: deploys one container with no orchestration
- **No auto-scale**: fixed replica count (max 3 by default)
- **Quick setup**: deploy directly from Designer or Python SDK
- **Cost**: pay per second while running
- **Best for**: development, demos, prototypes, batch inference

## AKS (Azure Kubernetes Service)

- **Kubernetes cluster**: full orchestration, auto-scaling, rolling updates
- **Auto-scale**: scale to hundreds of replicas based on traffic
- **High availability**: multiple zones, rolling deployments
- **Cost**: cluster management fee + VM cost per node
- **Best for**: production applications with high traffic, SLA requirements

## Decision Guide

| Requirement | Target |
|------------|--------|
| <1,000 predictions/day | ACI |
| Dev/test/demo | ACI |
| Production with SLA | AKS |
| >10,000 predictions/day | AKS |
| Auto-scaling needed | AKS |
| Managed service preferred | AKS |

## Related

- [[deploy-automl-model-aci-endpoint]]
- [[deploy-realtime-endpoint-designer]]
- [[batch-versus-realtime-inference]]
