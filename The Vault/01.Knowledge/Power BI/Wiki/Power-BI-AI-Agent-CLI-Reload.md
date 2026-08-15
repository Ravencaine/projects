---
created: 2026-08-08
updated: 2026-08-08
source: AI Changing Power BI Workflow
note_type: atomic
tags: [power-bi, ai-agent, cli, automation, pbi-desktop]
---

# Power BI AI Agent CLI: `pbidesktop reload`

The Power BI AI Agent CLI exposes a `reload` command that refreshes an open Power BI Desktop report directly from the JSON files in the PBIR definition folder — enabling a real-time AI-edit loop.

## Definition

After an AI agent edits the JSON files in a PBIR report's `definition/` folder, running `pbidesktop reload` from the command line sends a signal to the open Power BI Desktop instance, which re-reads and re-renders the report from the updated JSON files. The report refreshes in the background without the user needing to manually reopen the file.

## Key Points

- Command: `pbidesktop reload` (part of Power BI AI Agent skills/CLI)
- Requires Power BI Desktop to be open with the corresponding PBIR file loaded
- The AI agent edits JSON → user types `pbidesktop reload` → report updates in seconds
- Workflow: edit in VS Code → reload → inspect in Power BI Desktop → iterate
- Available as part of the Power BI AI Agent **skills** feature (not a standalone CLI install)
- No manual save or re-open required — refresh is near-instant

## Example

**Loop:**
1. AI agent reads PBIR JSON, identifies a visual needing a color change
2. Agent edits `visuals/visual-abc.json` → changes fill color
3. User runs `pbidesktop reload`
4. Power BI Desktop refreshes — new color visible immediately

**Prerequisite:** Power BI Desktop must be running with the `.pbir` file open.

## Related

- [[PBIR-Power-BI-Report-Format-JSON]] — what the reload command works on
- [[AI-Written-PowerShell-Scripts-Design-Automation]] — PowerShell scripts that automate design tasks on top of PBIR
