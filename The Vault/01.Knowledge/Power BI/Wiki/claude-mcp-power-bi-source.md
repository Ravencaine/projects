---
created: 2026-07-27
updated: 2026-08-02
source: "I Connected Claude to 3 Real Client Power BI Models Via MCP. Here's What It Caught — and What It Got Wrong"
source_url: "https://medium.com/power-bi-made-easy/i-connected-claude-to-3-real-client-power-bi-models-via-mcp-9f3a6b8c0d0k"
note_type: source
tags: [power-bi, mcp, claude, ai, semantic-model, model-inspection, automation]
---

# Claude MCP + Power BI Semantic Models

> **Type:** article
> **Author:** Gulab Chand Tejwani
> **Published:** 2025-11-17
> **URL:** https://medium.com/power-bi-made-easy/i-connected-claude-to-3-real-client-power-bi-models-via-mcp-9f3a6b8c0d0k
> **Routed to:** Power BI

## Summary

The Model Context Protocol (MCP) enables AI assistants (Claude, GPT) to connect directly to Power BI semantic models for automated analysis, documentation, DAX review, and model inspection. The article documents what MCP caught in 3 real client models and what it got wrong.

## Key Claims

- MCP connects to Power BI semantic models via the Power BI REST API or XMLA endpoint
- What MCP caught: missing date tables, redundant measures, inconsistent naming conventions, broken relationships
- What MCP got wrong: misidentified bidirectional cross-filtering as a problem in contexts where it was intentional, hallucinated some DAX functions that don't exist
- Best use: automated model documentation, DAX review against conventions, identification of orphaned columns

## Notable Details

- MCP requires: Power BI Pro/Premium workspace, AI assistant with MCP client, semantic model with read permissions
- MCP cannot modify the model — it is read-only
- Best workflow: MCP for audit/documentation; human for DAX writing and model changes

## Extracted Notes

- [[mcp-power-bi-semantic-model-workflow]] — workflow

## Metadata

| Field | Value |
|-------|-------|
| Source file | I Connected Claude to 3 Real Client Power BI Models Via MCP. Here's What It Caught — and What It Got Wrong.md |
| Archived at | 99.System/InboxArchive/2026-07/ |
| Ingestion date | 2026-07-27 |
| Word count | ~2,948 |
