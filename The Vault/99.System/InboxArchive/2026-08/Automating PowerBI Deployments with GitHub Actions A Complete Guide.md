---
title: "Automating PowerBI Deployments with GitHub Actions: A Complete Guide"
source: "https://medium.com/@michael.hannecke/automating-powerbi-deployments-with-github-actions-a-complete-guide-ad11d116bd43"
author:
  - "[[Michael Hannecke]]"
published: 2025-02-24
created: 2026-08-03
description: "More"
Processed: "Unprocessed"
---
![](99.System/Attachments/1!U0_aog9pL_44Lpg3vw0JzA.jpeg.webp)

Business Reporting as Dall-E sees it

In our modern, data-driven world, PowerBI is one of the most used tools for business intelligence and reporting. However, manually deploying PowerBI reports can be time-consuming and error-prone. This guide will show you how to automate PowerBI deployments using GitHub Actions, complete with Azure configuration and troubleshooting tips.

### Prerequisites

- A GitHub repository
- An Azure subscription
- PowerBI workspace with admin access
- Basic familiarity with PowerShell and GitHub Actions

### Setting Up Azure Configuration

**Create an App Registration**  
First, you’ll need to create an App Registration in Azure AD. This can be done through the Azure Portal or using Azure CLI. We will name our App Registration “GitHub-PowerBI-Deploy”

```c
# Install Azure CLI if you haven't already
winget install -e - id Microsoft.AzureCLI

# Create the App Registration

az ad app create - display-name "GitHub-PowerBI-Deploy"
```

**Configure PowerBI API Permissions**  
In the Azure Portal, in your App Registration:

- Save the Application client ID
- Navigate to “API Permissions”
- Add the following PowerBI Service permissions:  
	— ***Workspace.Read.All  
	— Workspace.ReadWrite.All  
	— Report.Read.All  
	— Report.ReadWrite.All  
	— Workspace.Read.All  
	— Workspace.ReadWrite.All***
- Grant admin consent for these permissions
- In the app registration in **Certification & secrets** create a new client secret and save the value

### PowerBI Service Configuration

- Login to [app.powerbi.com](http://app.powerbi.com/)
- On the left navigation pane, select workspaces and the button **New Workspace**
- Give the workspace a name and description (optional)
- If you want to enable scheduled data refresh for the reports deployed on the workspace you must select Premium under advanced settings.
- Once the workspace is deployed, select **Manage Access** in the upper right
- Select **add people or groups** and search for the name of your app registration
- Select **Contributor** as access level.
- Save the Workspace name -it will be needed as environment variable for the github action

### GitHub Configuration

- **Repository Structure**  
	Set up your repository with this structure:
```c
your-repo/
├── .github/
│ └── workflows/
│   └── deploy-powerbi.yml
└── reports/
 └── prd/
   └── your-report.pbip
```
- **Configure Secrets and Variables**  
	Navigate to your repository’s Settings > Secrets and variables > Actions and add:  
	**Secrets:  
	**\- AZURE\_CLIENT\_ID (your App Registration client ID)  
	\- AZURE\_TENANT\_ID (your Azure tenant ID)  
	\- AZURE\_CLIENT\_SECRET (your app secret from above)
- **Variables:**  
	\- WORKSPACE\_NAME (your PowerBI workspace name)  
	\- REPORT\_NAME (your report name)

### Power BI Report

- Create a new Power Bi Report and save it as \*.pbix file (this should be the default)
- For the Github action it is expected to save the report in reports/prod. If you want to use a diffeent path, you need to adopt the path in the yaml file accordingly.
- Use the same name you provided in REPORT\_NAME

> Microsoft recommends to use the **\*.pbip** format for storing the Power BI report, which would provide detailed source code versioning and control. But that did not work for me, I had to convert back to **\*.pbix** prior to deployment, so I skipped this and went without detailed source control in the report itself.

### GitHub Actions Workflow

Copy and save the attached script as powerbi-deploy.yml un the workflow folder:

```c
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
      DEBUG_MODE: ${{ github.event.inputs.debug_mode }}
    
    steps:
      - name: Checkout repository
        uses: actions/checkout@v3
        
      - name: Set up PowerShell Core
        uses: actions/setup-dotnet@v3
        with:
          dotnet-version: '6.0.x'
      
      - name: Install PowerShell modules
        shell: pwsh
        run: |
          Write-Host "Installing PowerShell modules..."
          Install-Module -Name MicrosoftPowerBIMgmt -Force -Scope CurrentUser -AllowClobber
      
      - name: Authenticate and Get Power BI Workspace
        shell: pwsh
        id: auth-and-get-workspace
        run: |
          Write-Host "Authenticating to Power BI Service..."
          
          $clientId = "${{ secrets.AZURE_CLIENT_ID }}"
          $clientSecret = "${{ secrets.AZURE_CLIENT_SECRET }}"
          $tenantId = "${{ secrets.AZURE_TENANT_ID }}"
          
          try {
            $password = ConvertTo-SecureString $clientSecret -AsPlainText -Force
            $credential = New-Object System.Management.Automation.PSCredential($clientId, $password)
            
            Connect-PowerBIServiceAccount -ServicePrincipal -Credential $credential -TenantId $tenantId -ErrorAction Stop
            
            # Get workspace
            Write-Host "Getting Power BI workspace: $env:WORKSPACE_NAME"
            $workspace = Get-PowerBIWorkspace -Name $env:WORKSPACE_NAME -ErrorAction Stop
            
            if ($null -eq $workspace) {
              Write-Host "::error::Workspace '$env:WORKSPACE_NAME' not found"
              exit 1
            }
            
            Write-Host "Workspace found with ID: $($workspace.Id)"
            echo "WORKSPACE_ID=$($workspace.Id)" >> $env:GITHUB_ENV
          }
          catch {
            Write-Host "::error::Power BI operation failed: $_"
            exit 1
          }
      
      - name: Find PBIX File
        shell: pwsh
        id: find-pbix
        run: |
          Write-Host "Searching for PBIX file for report: $env:REPORT_NAME"
          
          $pbixFiles = Get-ChildItem -Path "reports/prd" -Filter "*.pbix" -ErrorAction SilentlyContinue | Where-Object { $_.BaseName -eq $env:REPORT_NAME }
          
          if ($null -eq $pbixFiles -or $pbixFiles.Count -eq 0) {
            Write-Host "::error::No PBIX file found for report: $env:REPORT_NAME in path reports/prd"
            exit 1
          }
          
          $pbixFile = $pbixFiles[0].FullName
          Write-Host "Found PBIX file: $pbixFile"
          echo "PBIX_FILE=$pbixFile" >> $env:GITHUB_ENV
      
      - name: Deploy report to Power BI
        shell: pwsh
        run: |
          try {
            # Re-authenticate to ensure active session
            $clientId = "${{ secrets.AZURE_CLIENT_ID }}"
            $clientSecret = "${{ secrets.AZURE_CLIENT_SECRET }}"
            $tenantId = "${{ secrets.AZURE_TENANT_ID }}"
            
            $password = ConvertTo-SecureString $clientSecret -AsPlainText -Force
            $credential = New-Object System.Management.Automation.PSCredential($clientId, $password)
            
            Connect-PowerBIServiceAccount -ServicePrincipal -Credential $credential -TenantId $tenantId -ErrorAction Stop
            
            Write-Host "Checking if report already exists in workspace..."
            
            $workspaceId = $env:WORKSPACE_ID
            $reportName = $env:REPORT_NAME
            
            $existingReport = Get-PowerBIReport -WorkspaceId $workspaceId -ErrorAction Stop | Where-Object Name -eq $reportName
            
            $pbixFile = $env:PBIX_FILE
            
            if ($null -ne $existingReport) {
              Write-Host "Updating existing report '$reportName'..."
              $result = New-PowerBIReport -Path $pbixFile -WorkspaceId $workspaceId -Name $reportName -ConflictAction CreateOrOverwrite -ErrorAction Stop
              Write-Host "Report updated successfully"
            } else {
              Write-Host "Creating new report '$reportName'..."
              $result = New-PowerBIReport -Path $pbixFile -WorkspaceId $workspaceId -Name $reportName -ErrorAction Stop
              Write-Host "Report created successfully"
            }
            
            Write-Host "Deployment completed successfully"
          }
          catch {
            Write-Host "::error::Deployment failed: $_"
            exit 1
          }
```

The Github action is configured to be started manually — use this until the action fits to your needs and executes without any errors. You can set it to be executed on pull-request if you want:

```c
on:
  pull_request:
    types:
      - closed
    branches:
      - main
  workflow_dispatch:
```

Change the ‘on’ section to your needs

Once the Github action executes — depending on your Action settings — the report will be deployed and published on your Power BI Service.

### Conclusion

Automating PowerBI deployments with GitHub Actions not only saves time but also reduces human error and provides a consistent deployment process. While the initial setup requires careful attention to detail, the long-term benefits of automation are well worth the effort.

Remember to keep your configurations up to date and regularly review security settings. As both GitHub Actions and PowerBI continue to evolve, stay informed about new features and best practices that could enhance your deployment pipeline.

### Additional Resources

- \[PowerBI REST API Documentation\]([https://learn.microsoft.com/en-us/rest/api/power-bi/](https://learn.microsoft.com/en-us/rest/api/power-bi/))
- \[GitHub Actions Documentation\]([https://docs.github.com/en/actions](https://docs.github.com/en/actions))
- \[Azure AD App Registration Guide\]([https://learn.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app](https://learn.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app))