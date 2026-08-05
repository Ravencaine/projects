---
created: 2026-08-05
updated: 2026-08-05
source: Automating PowerBI Deployments with GitHub Actions A Complete Guide.md
note_type: pattern
tags: [power-bi, deployment, powershell, microsoftpowerbimgmt, automation]
---

# PBIX Deployment Logic: Create or Overwrite

Check whether a report already exists in a Power BI workspace, then deploy with the correct cmdlet and conflict action.

## Purpose

Automate the two deployment scenarios: creating a new report and updating an existing one. Use `-ConflictAction CreateOrOverwrite` on the update path to avoid errors when the report already exists.

## Structure

```powershell
# After authentication and workspace lookup
$workspaceId = $env:WORKSPACE_ID
$reportName  = $env:REPORT_NAME
$pbixFile   = $env:PBIX_FILE

# Check if report exists in the workspace
$existingReport = Get-PowerBIReport -WorkspaceId $workspaceId -ErrorAction Stop |
                  Where-Object Name -eq $reportName

if ($null -ne $existingReport) {
    # Update existing report
    New-PowerBIReport -Path $pbixFile `
        -WorkspaceId $workspaceId `
        -Name $reportName `
        -ConflictAction CreateOrOverwrite `
        -ErrorAction Stop
    Write-Host "Report updated successfully"
} else {
    # Create new report
    New-PowerBIReport -Path $pbixFile `
        -WorkspaceId $workspaceId `
        -Name $reportName `
        -ErrorAction Stop
    Write-Host "Report created successfully"
}
```

## Key Points

- `Get-PowerBIReport -WorkspaceId` returns all reports in the workspace — filter by name client-side
- `New-PowerBIReport` is used for **both** create and update; the `-ConflictAction CreateOrOverwrite` flag controls update behaviour
- Without `-ConflictAction CreateOrOverwrite`, attempting to create a report that already exists throws an error
- `-ErrorAction Stop` ensures the step fails immediately on errors rather than silently continuing

## Related

- [[power-bi-cicd-pipeline-github-actions]] — full pipeline integrating this logic
- [[connect-powerbi-serviceaccount-service-principal]] — authentication before deployment
