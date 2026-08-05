---
created: 2026-08-05
updated: 2026-08-05
source: Automating PowerBI Deployments with GitHub Actions A Complete Guide.md
source_url: https://medium.com/@michael.hannecke/automating-powerbi-deployments-with-github-actions-a-complete-guide-ad11d116bd43
note_type: source
tags: [power-bi, github-actions, cicd, automation, deployment, azure-ad]
---

# Automating PowerBI Deployments with GitHub Actions (Hannecke)

> **Type:** article
> **Author:** Michael Hannecke
> **Published:** 2025-02-24
> **URL:** https://medium.com/@michael.hannecke/automating-powerbi-deployments-with-github-actions-a-complete-guide-ad11d116bd43
> **Routed to:** Power BI

## Summary

End-to-end guide for automating Power BI report deployment via GitHub Actions using Azure AD service principals, `MicrosoftPowerBIMgmt` PowerShell module, and the Power BI REST API. Covers Azure App Registration, workspace permissions, secrets/variables setup, and a full YAML workflow with error handling.

## Key Claims

- Azure AD App Registration (service principal) enables non-user-based authentication for CI/CD
- PowerShell `MicrosoftPowerBIMgmt` module provides `Connect-PowerBIServiceAccount`, `Get-PowerBIWorkspace`, and `New-PowerBIReport` cmdlets for automation
- `Get-PowerBIReport | Where-Object Name -eq $name` checks existence before deciding create vs update
- `-ConflictAction CreateOrOverwrite` on `New-PowerBIReport` handles idempotent updates
- `workflow_dispatch` for manual control during development; `pull_request` trigger for automation after testing
- `.pbix` format required (`.pbip` source-control format did not work in practice)

## Notable Details

- Uses `actions/setup-dotnet@v3` with `dotnet-version: '6.0.x'` as the .NET prerequisite for PowerShell
- `MicrosoftPowerBIMgmt` installed via `Install-Module -Force -Scope CurrentUser -AllowClobber` — no admin required
- The pipeline re-authenticates before the deploy step to ensure an active session
- GitHub Variables (`vars.WORKSPACE_NAME`) for non-sensitive config; Secrets for credentials
- Premium workspace required for scheduled data refresh; Contributor-level access is sufficient for deployment

## Extracted Notes

Links to notes derived from this source:

- [[power-bi-cicd-pipeline-github-actions]] — workflow — full end-to-end pipeline
- [[azure-ad-app-registration-power-bi-service-principal]] — pattern — Azure AD service principal setup
- [[connect-powerbi-serviceaccount-service-principal]] — snippet — PowerShell service principal auth
- [[pbix-deploy-create-or-overwrite]] — pattern — conditional create/update deployment logic
- [[workspace-not-found-pbix-deploy]] — error — workspace not found diagnosis

## Metadata

| Field | Value |
|-------|-------|
| Source file | Automating PowerBI Deployments with GitHub Actions A Complete Guide.md |
| Archived at | 99.System/InboxArchive/2026-08/ |
| Ingestion date | 2026-08-05 |
| Word count | ~247 |
