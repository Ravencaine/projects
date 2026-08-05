---
created: 2026-08-05
updated: 2026-08-05
source: Automating PowerBI Deployments with GitHub Actions A Complete Guide.md
note_type: pattern
tags: [power-bi, azure-ad, service-principal, authentication, security]
---

# Azure AD App Registration for Power BI Service Principal

Create an Azure AD App Registration (service principal) to authenticate GitHub Actions against the Power BI Service API.

## Purpose

A service principal allows GitHub Actions to authenticate to Power BI without a human user account. The principal is granted API permissions and workspace access, then used in CI/CD pipelines.

## Components

- Azure AD App Registration — the identity
- Client secret — a credential for the identity
- Power BI Service API permissions — what the identity can do
- Workspace access assignment — which workspaces the identity can deploy to

## Structure

### Step 1 — Create App Registration

```powershell
az ad app create --display-name "GitHub-PowerBI-Deploy"
```

Or via Azure Portal: **Azure Active Directory → App registrations → New registration**.

Save:
- **Application (client) ID**
- **Directory (tenant) ID**
- Client secret value (created in the app registration under **Certificates & secrets**)

### Step 2 — Grant Power BI API Permissions

In the Azure Portal, under **API Permissions** for the app registration:

Add Power BI Service permissions:

| Permission | Type | Purpose |
|-----------|------|---------|
| `Workspace.Read.All` | Application | Read workspace metadata |
| `Workspace.ReadWrite.All` | Application | Create/update workspaces |
| `Report.Read.All` | Application | Read report definitions |
| `Report.ReadWrite.All` | Application | Publish/replace reports |

Select **Grant admin consent for [tenant]** after adding permissions.

### Step 3 — Assign Workspace Access

In Power BI Service:

1. Go to the target workspace → **Manage Access**
2. Search for the app registration name (the display name from Step 1)
3. Set access level to **Contributor**
4. Save

> If using Premium capacity for scheduled refresh, ensure the workspace is on a Premium node and the service principal has capacity-level permissions.

## Variations

**Premium Per-Workspace:** Assign the service principal directly to the workspace with Contributor role.

**Premium Capacity:** Assign the service principal to the capacity with Member or Admin role.

## Related

- [[power-bi-cicd-pipeline-github-actions]] — full pipeline using this principal
- [[connect-powerbi-serviceaccount-service-principal]] — PowerShell authentication snippet
- [[pbix-deploy-create-or-overwrite]] — deployment logic after auth
