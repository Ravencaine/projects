---
created: 2026-08-06
updated: 2026-08-06
source: Claude Power BI MCP Integration
note_type: atomic
tags: [mcp, claude, power-bi, ai, automation, desktop]
---

# Claude Power BI MCP Integration

Using the Model Context Protocol (MCP) to connect Anthropic's Claude AI directly to Power BI Desktop, enabling AI-assisted model building tasks — DAX generation, hierarchy creation, metadata population — without writing code manually.

<!-- one-line description: AI-powered Power BI model automation via Claude connected to Power BI Desktop through Microsoft's Model Context Protocol -->

## Definition

The Claude Power BI MCP integration connects Claude (via VS Code) to an open Power BI Desktop file using Microsoft's Model Context Protocol. Unlike the Power BI Service MCP (which reads semantic models via XMLA), the Desktop MCP integration operates on the live `.pbix` model. Claude can read metadata, write DAX, create hierarchies, and populate descriptions — all within Power BI Desktop.

## Key Points

- Uses **VS Code + Power BI MCP extension** to connect Claude to Power BI Desktop
- MCP is the API framework Microsoft provides for external AI tools to interact with Power BI
- Capabilities: DAX measure generation, field renaming, display folder organisation, hierarchy creation, description/synonym population, data type optimisation, data dictionary auto-generation
- Achieved **up to 15% model size reduction** and **3x query speed improvement** in demo benchmarks
- Setup: VS Code → Power BI MCP extension → Claude Desktop config → prompt to connect
- Contrast with [[mcp-power-bi-semantic-model-workflow]] — this approach targets Desktop, the existing workflow targets Power BI Service semantic models
- Contrast with [[mcp-power-bi-modeling-preview-caveats]] — the existing caveats apply to the Power BI Service MCP server; the Desktop MCP extension may have different support status

## Examples

- "Create a Net Sales measure and a YTD calculation table"
- "Add display folders to organize all my measures"
- "Build a Product → Subcategory → Item hierarchy"
- "Add descriptions and synonyms to every field"
- "Optimize all column data types for compression"

## Related

- [[Connect-Claude-to-Power-BI-via-MCP]] — step-by-step setup workflow
- [[7-AI-Prompts-for-Power-BI-MCP]] — reference card of 7 prompts
- [[mcp-power-bi-semantic-model-workflow]] — Power BI Service MCP workflow (read-only, XMLA)
- [[mcp-power-bi-modeling-preview-caveats]] — governance and trust requirements for MCP
- [[Organizing-Measures-Display-Folders]] — the display folder pattern Claude automates
