---
created: 2026-08-05
updated: 2026-08-05
source: Automating PowerBI Deployments with GitHub Actions A Complete Guide.md
note_type: error
tags: [power-bi, github-actions, error, deployment, workspace]
---

# Workspace Not Found — GitHub Actions PBIX Deployment

## Error Message

```
Write-Host "::error::Workspace '$env:WORKSPACE_NAME' not found"
exit 1
```

Triggered when `Get-PowerBIWorkspace -Name $env:WORKSPACE_NAME` returns `$null`.

## Cause

- `WORKSPACE_NAME` GitHub variable does not match the actual workspace name exactly
- Service principal does not have access to the workspace
- Workspace was deleted or renamed
- Wrong tenant / Power BI tenant context

## How to Handle It

1. **Verify the workspace name** in Power BI Service (app.powerbi.com) matches `WORKSPACE_NAME` exactly — case-sensitive
2. **Grant workspace access** to the service principal: Power BI Service → Workspace → Manage Access → add the app registration with **Contributor** role
3. **Check tenant context**: if the service principal belongs to a different Azure AD tenant, `Connect-PowerBIServiceAccount` will succeed but workspace queries return nothing
4. **Print debug output**: add `Write-Host "Workspace: $($workspace | ConvertTo-Json)"` before the null check to inspect what was returned

## Related

- [[power-bi-cicd-pipeline-github-actions]] — pipeline where this error occurs
- [[azure-ad-app-registration-power-bi-service-principal]] — service principal setup and workspace access
