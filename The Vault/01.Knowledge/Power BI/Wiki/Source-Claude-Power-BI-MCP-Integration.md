---
created: 2026-08-06
updated: 2026-08-06
source: Claude Power BI MCP Integration
source_url: https://databear.com/claude-power-bi-mcp-integration/
note_type: source
tags: [mcp, claude, power-bi, ai, automation, desktop]
---

# Claude Power BI MCP Integration (Boniface Muchendu / Data Bear)

A Data Bear blog post by Boniface Muchendu explaining how to connect Claude AI to Power BI Desktop via the Model Context Protocol (MCP) — covering 7 AI prompts for automating model building tasks.

> **Type:** article
> **Author:** Boniface Muchendu (Data Bear)
> **Published:** 2026-01-03
> **URL:** https://databear.com/claude-power-bi-mcp-integration/
> **Routed to:** Power BI

## Summary

The article introduces the Claude Power BI MCP integration — using Microsoft's Model Context Protocol to connect Anthropic's Claude AI to Power BI Desktop via VS Code. Seven prompts automate model-building tasks: DAX generation, field renaming, display folder organisation, hierarchy creation, metadata/synonym population, data type optimisation, and data dictionary auto-generation. Demo benchmarks showed 15% model size reduction and 3x query speed improvement.

## Key Claims

- MCP connects Claude to Power BI Desktop (not Service) via VS Code
- Seven prompts cover the full model-building lifecycle: measures, renaming, folders, hierarchies, descriptions, optimisation, documentation
- Prompt 2 (rename) updates DAX measure references automatically — no broken links
- Prompt 7 (data type optimisation) achieved 15% model size reduction and 3x query speed improvement in demo
- Bonus prompt generates a complete data dictionary with Mermaid ER diagram
- Setup requires: VS Code, Power BI MCP extension, Claude Desktop for Windows

## Notable Details

- The Desktop MCP differs from the Power BI Service MCP — Desktop MCP can write to the model; Service MCP is read-only via XMLA
- [[Author-Boniface-Muchendu]] already in vault — extend the author note with this 5th source
- Data Bear training: https://databear.com/power-bi-training/

## Extracted Notes

Links to notes derived from this source:

- [[Claude-Power-BI-MCP-Integration]] — `atomic` — concept overview of the Desktop MCP integration
- [[Connect-Claude-to-Power-BI-via-MCP]] — `workflow` — step-by-step setup
- [[7-AI-Prompts-for-Power-BI-MCP]] — `reference` — 7 prompts quick reference

## Metadata

| Field | Value |
|-------|-------|
| Source file | Claude Power BI MCP Integration.md |
| Archived at | 99.System/InboxArchive/2026-08/ |
| Ingestion date | 2026-08-06 |
| Word count | ~720 |
