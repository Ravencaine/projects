---
created: 2026-08-11
updated: 2026-08-11
source: "AI-Power-BI-Workflow-Transcript.md"
note_type: pattern
tags: [power-bi, pbir, powershell, automation]
---

# PowerShell Design Automation with PBIR

AI agents can generate PowerShell scripts that manipulate PBIR JSON files to automate report design tasks — spacing, formatting, layout — then trigger hot-reload.

## Purpose

Report formatting tasks like "add evenly-spaced shapes around this group with 30px padding" are tedious by hand. An AI-generated PowerShell script does it in seconds and is reusable.

## Example (from Ned — 5min → 10sec)

```powershell
# Prompt the AI: "write a script that takes a page ID and group ID,
# and adds an evenly-spaced rectangle around that group with configurable padding"

param(
    [string]$PageId,
    [string]$GroupId,
    [int]$PaddingPx = 30
)

# Script reads the PBIR page JSON
# Calculates group bounds + padding
# Injects shape objects into the JSON
# Saves the file

# Run from VS Code terminal:
# ./autofill-shapes.ps1 -PageId "abc123" -GroupId "def456" -PaddingPx 30
# powerbi desktop reload
```

## Workflow

1. AI agent writes the PowerShell script once
2. Human runs it: `.\script.ps1 -PageId <id> -GroupId <id> -PaddingPx N`
3. Get IDs from Power BI Desktop: right-click → Copy Page ID / Copy Object Name
4. `powerbi desktop reload` → Power BI Desktop reflects the changes instantly

## Why It Works

PBIR exposes JSON. PowerShell reads/writes JSON natively. The AI agent writes the PowerShell. Human applies and approves.

## Related

- [[pbir-hot-reload-workflow]] — the reload step that completes this workflow
- [[power-bi-ai-agent-overview-ned]] — AI + PBIR overview from Ned
