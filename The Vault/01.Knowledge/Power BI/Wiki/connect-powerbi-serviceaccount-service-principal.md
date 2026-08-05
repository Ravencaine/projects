---
created: 2026-08-05
updated: 2026-08-05
source: Automating PowerBI Deployments with GitHub Actions A Complete Guide.md
note_type: snippet
tags: [power-bi, powershell, service-principal, authentication, microsoftpowerbimgmt]
---

# PowerShell: Connect-PowerBIServiceAccount (Service Principal)

Authenticate to the Power BI Service from PowerShell using a service principal (Azure AD App Registration) — used in automated deployment pipelines.

## Snippet

```powershell
# Prerequisites
$clientId     = "<AZURE_CLIENT_ID>"
$clientSecret = "<AZURE_CLIENT_SECRET>"   # from Azure AD App Registration
$tenantId     = "<AZURE_TENANT_ID>"

# Build credential
$password   = ConvertTo-SecureString $clientSecret -AsPlainText -Force
$credential = New-Object System.Management.Automation.PSCredential($clientId, $password)

# Authenticate as service principal
Connect-PowerBIServiceAccount -ServicePrincipal `
    -Credential $credential `
    -TenantId $tenantId `
    -ErrorAction Stop
```

## Module Requirements

```powershell
Install-Module -Name MicrosoftPowerBIMgmt -Force -Scope CurrentUser -AllowClobber
```

Requires PowerShell Core (pwsh) — used with `shell: pwsh` in GitHub Actions.

## Parameters

| Parameter | Source | Notes |
|-----------|--------|-------|
| `-ServicePrincipal` | Flag | Use app registration, not user account |
| `-Credential` | `$PSCredential` | Built from client ID + secret |
| `-TenantId` | Azure AD | Directory (tenant) ID from the app registration |

## Related

- [[azure-ad-app-registration-power-bi-service-principal]] — how to create the service principal
- [[power-bi-cicd-pipeline-github-actions]] — full workflow using this authentication
