---
created: 2026-08-11
updated: 2026-08-11
source: "AI-Power-BI-Workflow-Transcript.md"
note_type: pattern
tags: [power-bi, pbir, ai-agent, workflow]
---

# PBIR Hot-Reload Workflow with AI Agents

Edit a Power BI report via code (JSON in VS Code), then hot-reload the open report in Power BI Desktop without touching the UI.

## Purpose

PBIR (Power BI enhanced report format / project format) exposes the entire report definition as JSON files. AI agents can read the schema and edit visuals directly in code. The `powerbi desktop reload` CLI command tells Power BI Desktop to pick up the changes instantly.

## Components

- **PBIR format:** save a .pbix as .pbir to get JSON files in a `definition/` folder
- **VS Code:** edit the JSON — AI agent or manual
- **Power BI AI agent CLI:** `powerbi desktop reload` — reloads the open report from disk

## Structure

```
Power BI Desktop → Save As → .pbir
↓
Open .pbir folder in VS Code
↓
AI agent edits JSON (e.g., visual properties, shape positions)
↓
$ powerbi desktop reload
↓
Power BI Desktop refreshes the report in the background
```

## Key Insight

The AI agent points to the schema at the top of each JSON object — it knows exactly how every visual is structured, so edits are precise, not guesswork.

## Related

- [[pbir-json-structure]] — the JSON file structure inside a PBIR
- [[power-bi-ai-agent-workflow-ned]] — AI + PBIR for PowerShell design automation
