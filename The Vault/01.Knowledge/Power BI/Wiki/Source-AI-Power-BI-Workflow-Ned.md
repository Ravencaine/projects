---
created: 2026-08-11
updated: 2026-08-11
source: "AI-Power-BI-Workflow-Transcript.md"
note_type: source
tags: [power-bi, pbir, ai-agent, powershell, video]
---

# AI Power BI Workflow — Drop Materialized View — Source

Ned (Microsoft MVP, Power BI focus) demonstrates how AI agents combined with PBIR format change the day-to-day Power BI report-building workflow.

> **Type:** video
> **Author:** Ned (Microsoft MVP)
> **Published:** 2025 (approx.)
> **URL:** https://www.youtube.com/watch?v=rDuHokI3YBQ
> **Routed to:** Power BI

## Summary

PBIR (Power BI enhanced report format) exposes report definitions as JSON, enabling AI agents to edit visuals directly in code. A CLI reload command (`powerbi desktop reload`) hot-reloads changes into the open Power BI Desktop report instantly. AI-generated PowerShell scripts automate design tasks (spacing, padding) by manipulating the same JSON files.

## Key Claims

- PBIR is the catalyst for AI-driven report editing — the JSON schema gives AI agents precise structure knowledge
- `powerbi desktop reload` hot-reloads from disk without closing/reopening Power BI Desktop
- PowerShell + AI agent = reusable design automation (shapes, spacing, formatting)
- The 5-minute manual task (evenly-spaced shapes) becomes a 10-second script execution

## Extracted Notes

Links to notes derived from this source:

- [[pbir-format-json-structure]] — atomic — JSON structure inside a PBIR
- [[pbir-hot-reload-workflow]] — pattern — hot-reload with `powerbi desktop reload`
- [[powershell-design-automation-pbir]] — pattern — AI-generated PowerShell for design tasks

## Metadata

| Field | Value |
|-------|-------|
| Source file | AI-Power-BI-Workflow-Transcript.md |
| Ingestion date | 2026-08-11 |
| Duration | 4:41 |
