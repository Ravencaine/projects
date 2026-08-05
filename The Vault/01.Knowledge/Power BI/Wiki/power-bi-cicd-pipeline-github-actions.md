---
created: 2026-08-05
updated: 2026-08-05
source: Automating PowerBI Deployments with GitHub Actions A Complete Guide.md
note_type: workflow
tags: [power-bi, github-actions, cicd, automation, deployment]
---

# Power BI CI/CD Pipeline via GitHub Actions

End-to-end workflow for automating Power BI report deployment to the Power BI Service using GitHub Actions, Azure AD service principals, and PowerShell's `MicrosoftPowerBIMgmt` module.

## Prerequisites

- GitHub repository
- Azure subscription with permission to create App Registrations
- Power BI workspace with admin/contributor access
- Basic familiarity with PowerShell and GitHub Actions

## Steps

### 1. Azure AD — Create App Registration

```powershell
az ad app create --display-name "GitHub-PowerBI-Deploy"
```

Save the **Application (client) ID**, **Directory (tenant) ID**, and create a **client secret**.

### 2. Power BI Service — Grant API Permissions

In the Azure Portal, under the App Registration's **API Permissions**, add:

- Power BI Service → `Workspace.Read.All`
- Power BI Service → `Workspace.ReadWrite.All`
- Power BI Service → `Report.Read.All`
- Power BI Service → `Report.ReadWrite.All`

Grant admin consent. Then assign the app registration **Contributor** access to the target Power BI workspace.

### 3. GitHub — Configure Secrets and Variables

Navigate to **Settings → Secrets and Variables → Actions** and add:

**Secrets:**
- `AZURE_CLIENT_ID` — App Registration client ID
- `AZURE_TENANT_ID` — Azure tenant ID
- `AZURE_CLIENT_SECRET` — Client secret value

**Variables:**
- `WORKSPACE_NAME` — Power BI workspace name
- `REPORT_NAME` — Report name (must match the `.pbix` filename)

### 4. Repository Structure

```
your-repo/
├── .github/
│   └── workflows/
│       └── powerbi-deploy.yml
└── reports/
    └── prd/
        └── your-report.pbix
```

### 5. GitHub Actions Workflow

```yaml
name: Deploy Power BI Report - Production

on:
  workflow_dispatch:

jobs:
  deploy-powerbi:
    runs-on: ubuntu-latest
    environment: ${{ github.ref_name }}

    env:
      WORKSPACE_NAME: ${{ vars.WORKSPACE_NAME }}
      REPORT_NAME: ${{ vars.REPORT_NAME }}

    steps:
      - name: Checkout repository
        uses: actions/checkout@v3

      - name: Set up .NET
        uses: actions/setup-dotnet@v3
        with:
          dotnet-version: '6.0.x'

      - name: Install PowerShell modules
        shell: pwsh
        run: |
          Install-Module -Name MicrosoftPowerBIMgmt -Force -Scope CurrentUser -AllowClobber

      - name: Authenticate and Get Workspace
        shell: pwsh
        id: auth-and-get-workspace
        run: |
          $clientId     = "${{ secrets.AZURE_CLIENT_ID }}"
          $clientSecret = "${{ secrets.AZURE_CLIENT_SECRET }}"
          $tenantId     = "${{ secrets.AZURE_TENANT_ID }}"

          $password    = ConvertTo-SecureString $clientSecret -AsPlainText -Force
          $credential  = New-Object System.Management.Automation.PSCredential($clientId, $password)

          Connect-PowerBIServiceAccount -ServicePrincipal -Credential $credential -TenantId $tenantId -ErrorAction Stop

          $workspace = Get-PowerBIWorkspace -Name $env:WORKSPACE_NAME -ErrorAction Stop
          Write-Host "Workspace ID: $($workspace.Id)"
          echo "WORKSPACE_ID=$($workspace.Id)" >> $env:GITHUB_ENV

      - name: Find PBIX File
        shell: pwsh
        run: |
          $pbixFiles = Get-ChildItem -Path "reports/prd" -Filter "*.pbix" |
                       Where-Object { $_.BaseName -eq $env:REPORT_NAME }

          if ($null -eq $pbixFiles) {
            Write-Host "::error::No PBIX file found: $env:REPORT_NAME"
            exit 1
          }
          echo "PBIX_FILE=$($pbixFiles[0].FullName)" >> $env:GITHUB_ENV

      - name: Deploy report
        shell: pwsh
        run: |
          $clientId     = "${{ secrets.AZURE_CLIENT_ID }}"
          $clientSecret = "${{ secrets.AZURE_CLIENT_SECRET }}"
          $tenantId     = "${{ secrets.AZURE_TENANT_ID }}"

          $password   = ConvertTo-SecureString $clientSecret -AsPlainText -Force
          $credential = New-Object System.Management.Automation.PSCredential($clientId, $password)
          Connect-PowerBIServiceAccount -ServicePrincipal -Credential $credential -TenantId $tenantId -ErrorAction Stop

          $existing = Get-PowerBIReport -WorkspaceId $env:WORKSPACE_ID |
                      Where-Object Name -eq $env:REPORT_NAME

          if ($null -ne $existing) {
            New-PowerBIReport -Path $env:PBIX_FILE -WorkspaceId $env:WORKSPACE_ID `
              -Name $env:REPORT_NAME -ConflictAction CreateOrOverwrite -ErrorAction Stop
          } else {
            New-PowerBIReport -Path $env:PBIX_FILE -WorkspaceId $env:WORKSPACE_ID `
              -Name $env:REPORT_NAME -ErrorAction Stop
          }
```

### 6. Trigger Modes

- **Manual only:** `workflow_dispatch` — safe during initial setup
- **On PR merge to main:**

```yaml
on:
  pull_request:
    types: [closed]
    branches: [main]
  workflow_dispatch:
```

## Common Errors

- [[workspace-not-found-pbix-deploy]] — `Workspace not found` when `WORKSPACE_NAME` is wrong or workspace access was not granted

## Related

- [[azure-ad-app-registration-power-bi-service-principal]] — Azure AD app setup pattern
- [[connect-powerbi-serviceaccount-service-principal]] — PowerShell service principal snippet
- [[pbix-deploy-create-or-overwrite]] — conditional create/update logic
