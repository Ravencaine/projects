---
title: "A SIMPLE Way AI is changing my POWER BI workflow"
created: 2026-08-08
updated: 2026-08-08
source: AI Changing Power BI Workflow
source_url: https://www.youtube.com/watch?v=rDuHokI3YBQ
author:
  - name: Edward Charles (Drop Materialized View)
url: https://www.linkedin.com/in/edward-charles-085025b1/
note_type: source
tags: [power-bi, ai, automation, powershell, pbi]
---

# AI Changing Power BI Workflow (Drop Materialized View)

AI agents (via PBIR + JSON + CLI) are changing the Power BI report-building workflow by enabling code-based visual editing and PowerShell automation.

> **Type:** video
> **Author:** Edward Charles (Drop Materialized View) — Microsoft MVP
> **Published:** 2026-07-04
> **URL:** https://www.youtube.com/watch?v=rDuHokI3YBQ
> **Routed to:** Power BI

## Summary

PBIR (Power BI enhanced report format) exposes report definitions as JSON files, giving AI agents a schema they can read and edit. Combined with the Power BI AI Agent CLI (`pbidesktop reload`), this enables a loop: AI edits JSON → reload → review in Power BI Desktop. PowerShell scripts written by AI agents automate repetitive design tasks (e.g., adding evenly-spaced shape borders to groups) that previously took 5-10 minutes in seconds.

## Key Claims

- PBIR format exposes report definitions as JSON — AI agents can read schemas and edit visuals via code
- `pbidesktop reload` CLI command refreshes the open Power BI Desktop report from the JSON files in real time
- AI-written PowerShell scripts automate repetitive design operations: pass in IDs and parameters, get consistent formatting instantly
- Example: shape border around a group — previously 5-10 min manual work, now 10 seconds via script
- AI agent writes the PowerShell script; human runs it and reloads in Power BI Desktop

## Notable Details

- PBIR is now the **default** Power BI report format
- Script requires: page ID (right-click page → Copy page ID) and group ID (right-click object → Copy object name)
- Script: `Add-GroupShapeBorder.ps1` — takes PageId, GroupId, PaddingPx parameters
- GitHub repo: https://github.com/edwardpcharles/Power-BI-Projects

## Extracted Notes

Links to notes derived from this source:

- [[PBIR-Power-BI-Report-Format-JSON]] — `atomic` — PBIR/PBI format exposes JSON report definitions
- [[Power-BI-AI-Agent-CLI-Reload]] — `atomic` — pbidesktop reload CLI for real-time report refresh
- [[AI-Written-PowerShell-Scripts-Design-Automation]] — `pattern` — AI-written PS scripts for Power BI design automation

## Metadata

| Field | Value |
|-------|-------|
| Script | 99.System/Attachments/AI-Power-BI-Workflow-Scripts/Add-GroupShapeBorder.ps1 |
| Archived at | 99.System/InboxArchive/2026-08/ |
| Ingestion date | 2026-08-08 |
| Word count | ~320 |
