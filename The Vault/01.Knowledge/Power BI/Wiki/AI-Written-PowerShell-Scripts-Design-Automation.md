---
created: 2026-08-08
updated: 2026-08-08
source: AI Changing Power BI Workflow
note_type: pattern
tags: [power-bi, powershell, ai, automation, design, pbi-desktop]
---

# AI-Written PowerShell Scripts for Power BI Design Automation

AI agents write PowerShell scripts that programmatically edit PBIR JSON files to automate repetitive Power BI report design tasks — from shape borders to bulk visual configuration.

## Purpose

Repetitive design tasks (adding consistent padding to shapes, applying themes across visuals, resizing groups) are tedious to do manually in Power BI Desktop but can be codified into PowerShell scripts. Rather than writing the scripts by hand, an AI agent generates them from a natural-language description of the desired operation. The human supplies IDs (page ID, object ID) and runs the script, then reloads Power BI Desktop.

## Components

- **Power BI AI Agent:** writes the PowerShell script from a description of the desired automation
- **PBIR format:** the underlying JSON files that the script edits
- **`pbidesktop reload`:** refreshes Power BI Desktop after the script runs
- **IDs from Power BI Desktop:** page ID (right-click page → Copy page ID) and object/group ID (right-click object → Copy object name)
- **Parameters:** passed to the script at runtime (padding, IDs, etc.)

## Structure

**PowerShell script signature:**
```powershell
param(
    [string]$PageId,
    [string]$GroupId,
    [double]$PaddingPx,
    [string]$ProjectRoot = (Get-Location).Path,
    [string]$ShapeId,
    [switch]$Reload
)
```

**Workflow:**
1. Open Power BI Desktop → right-click page → Copy page ID
2. Select a visual group → right-click → Copy object name (Group ID)
3. Run script: `.\Add-GroupShapeBorder.ps1` → paste Page ID → paste Group ID → enter padding in px
4. Type `pbidesktop reload` → Power BI Desktop updates with the new shape border

## Example

**Add evenly-spaced shape border to a visual group:**
```powershell
.\Add-GroupShapeBorder.ps1
Enter PageId: <paste from Power BI Desktop>
Enter GroupId: <paste from Power BI Desktop>
Enter PaddingPx: 30
pbidesktop reload
```
Result: evenly spaced 30px border around the group — previously 5-10 minutes, now 10 seconds.

**Other automatable tasks:**
- Bulk color theme application across visuals
- Consistent font sizing across a page
- Standardized spacing between visual groups
- Renaming visual objects in bulk

## Related

- [[PBIR-Power-BI-Report-Format-JSON]] — PBIR format the scripts operate on
- [[Power-BI-AI-Agent-CLI-Reload]] — reload CLI for applying script changes
