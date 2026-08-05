---
created: 2026-07-27
updated: 2026-08-02
source: "Claude MCP + Power BI Semantic Models"
note_type: workflow
tags: [power-bi, mcp, claude, semantic-model, automation, model-audit, dax-review]
---

# MCP Power BI Semantic Model Workflow

Using Model Context Protocol (MCP) to connect an AI assistant to Power BI semantic models for automated model auditing and documentation.

## Prerequisites

- Power BI Pro or Premium workspace
- AI assistant with MCP client (Claude Desktop, Cursor, Windsurf, etc.)
- Read permissions on the semantic model
- MCP server for Power BI (e.g., powerbi-mcp, or custom via Power BI REST API)

## Step 1: Configure MCP Server for Power BI

1. Install the Power BI MCP server (via npm or Python package)
2. Configure authentication (Power BI Service principal or OAuth2)
3. Set the workspace and semantic model connection string

```bash
# Example: powerbi-mcp npm package
npm install -g powerbi-mcp
powerbi-mcp --workspace <workspace-id> --dataset <semantic-model-id>
```

## Step 2: Connect AI Assistant

1. Configure the AI assistant to use the Power BI MCP server
2. Test the connection: ask "List all tables in the semantic model"

## Step 3: Automated Model Audit

### Ask the AI to Inspect the Model

```
Prompt: "Review this semantic model and identify:
1. Missing date tables
2. Redundant or duplicate measures
3. Inconsistent naming conventions
4. Orphaned columns (columns not used by any visual or measure)
5. Relationships with potential issues"
```

### Example Findings from MCP

| Finding | Description | Severity |
|---------|------------|---------|
| Missing date table | No table marked as date table | High |
| Duplicate revenue measures | 3 measures all calculating the same thing | Medium |
| Orphaned column | Customer[FreeTextField] not used anywhere | Low |
| Bidirectional cross-filtering | Used on 4 relationships | Medium |

## Step 4: DAX Convention Review

```
Prompt: "Review all DAX measures against these conventions:
1. Base measures start with underscore (_) and are hidden
2. All division uses DIVIDE() with BLANK fallback
3. No measure is longer than 10 lines
4. Time intelligence uses CALCULATE with SAMEPERIODLASTYEAR
Report violations by measure name."
```

## Step 5: Generate Model Documentation

```
Prompt: "Generate a model overview document listing:
1. All tables and their purpose
2. All relationships (cardinality, cross-filter direction)
3. All measures with their formula
4. Business glossary: business term -> model object mapping"
```

## What MCP Gets Wrong (and How to Handle It)

| MCP Error | Why It Happens | How to Handle |
|---------|--------------|--------------|
| Misidentifies intentional cross-filtering as a problem | MCP sees bidirectional and flags it without context | Human review required |
| Hallucinates non-existent DAX functions | LLM inference without model context | Verify DAX against actual model |
| Over-flags "missing" date table | Treats any date column as a potential date table | Confirm manually |

## Limitations

- MCP is **read-only**: cannot modify the model, write DAX, or change relationships
- Cannot refresh the semantic model
- Best used for: auditing, documentation, convention enforcement — not for writing DAX

## Related

- [[power-bi-dashboard-checklist]] — pre-publish checklist
- [[ai-copilot-power-bi-workflow]] — Copilot for DAX generation
- [[reports-semantic-models-power-bi-service]] — MCP connects to the semantic model via the Power BI REST API
