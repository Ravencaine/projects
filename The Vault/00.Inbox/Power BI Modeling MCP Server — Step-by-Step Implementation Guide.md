---
title: "Power BI Modeling MCP Server — Step-by-Step Implementation Guide"
source: "https://medium.com/microsoft-power-bi/power-bi-modeling-mcp-server-step-by-step-implementation-guide-b7209d6d2506"
author:
  - "[[Michael Hannecke]]"
published: 2025-12-19
created: 2026-08-03
description: "More"
Processed: "Unprocessed"
---
![](99.System/Attachments/1!WIJoglMtZR-uOgFoA9Of5g.jpeg.webp)

*Local and Remote Server Setup for VS Code, Claude Desktop, and GitHub Copilot*

> ***TL;DR:*** *This tutorial walks you through setting up Microsoft’s* ***Power BI Modeling MCP Server*** *to use* ***natural language*** *for building and managing Power BI semantic models. You’ll learn three setup paths (VS Code, Claude Desktop, Remote Server), how to connect to models in Desktop/Fabric/PBIP, and practical prompts for bulk operations, DAX validation, and model documentation.* ***Recommended path:*** *VS Code + GitHub Copilot for easiest setup*

**🎁** [**Get friend links for all of our 1500> Power BI learning articles here**](https://powerbi-masterclass.short.gy/learning-database?utm_source=medium&utm_medium=medium-post&utm_campaign=database-medium-post-start) **🎁**

## Table of Contents

1. Overview
2. Prerequisites
3. Setup: VS Code + GitHub Copilot (Local Server)
4. Setup: Claude Desktop (Local Server)
5. Setup: Remote MCP Server (Preview)
6. Connecting to Semantic Models
7. Example Use Cases and Prompts
8. Available MCP Tools Reference
9. Security Considerations
10. Troubleshooting
11. Additional Resources

## 1\. Overview

The **Power BI Modeling MCP Server** is Microsoft’s official implementation of the Model Context Protocol (MCP) that enables AI agents to interact with Power BI semantic models. This local MCP server allows you to use natural language to build, modify, and manage semantic models across Power BI Desktop, Fabric workspaces, and Power BI Project (PBIP) files.

### Key Capabilities

- **Natural Language Model Editing:** Create, update, and manage tables, columns, measures, and relationships using conversational commands
- **Bulk Operations at Scale:** Execute batch operations on hundreds of objects simultaneously with transaction support
- **Best Practice Application:** Evaluate and implement modeling best practices against your model
- **Agentic Development Workflows:** Work with TMDL and Power BI Project files for autonomous AI development
- **DAX Query Validation:** Execute and validate DAX queries to test measures and troubleshoot calculations

### ⚠️ Important Warnings — CAUTION

> *\- The underlying LLM may produce unexpected or inaccurate results that could lead to unintended changes.* ***Always create a backup of your model before performing any operations.***
> 
> *\- LLMs might unintentionally expose sensitive information from the semantic model in logs or responses.* ***Exercise caution when sharing chat sessions.***
> 
> *\- This MCP server can only execute modeling operations. It cannot modify report pages or diagram layouts.*

## 2\. Prerequisites

### General Requirements

- **Windows 10/11** (the MCP server is Windows-only)
- **Power BI Desktop** installed (latest version recommended)
- **A semantic model** to connect to (in Desktop, Fabric, or PBIP format)
- **Node.js** (for Claude Desktop configuration with npx)

### For VS Code + GitHub Copilot

- Visual Studio Code installed
- GitHub Copilot subscription (Individual, Business, or Enterprise)
- GitHub Copilot and GitHub Copilot Chat extensions installed

### For Claude Desktop

- Claude Desktop application installed
- Anthropic account (free tier works)

### Recommended AI Models

For best results with semantic model operations, Microsoft recommends using deep-reasoning models such as **GPT-5** or **Claude Sonnet 4.5**. The AI model you select directly influences the quality and relevance of the responses.

### Context Window & Cost Considerations

Be aware of token limits when working with large models:

- A medium-sized `model.bim` (~26k lines JSON) requires ~210k tokens — exceeding standard context windows
- Loading a full model schema into Claude Sonnet 4.5 costs approximately $0.60+ per session
- Large models may experience “context rot” where the LLM loses track of earlier schema details
- **Recommendation:** For large models, work with specific tables/measures rather than loading the entire schema

> *💡* ***Cost Management Tip:*** *For production use with large models, scope your prompts to specific tables or measure groups rather than loading the entire schema. This reduces token costs by 70–90% and improves response quality.*

## 3\. Setup: VS Code + GitHub Copilot (Local Server)

This is the **recommended and easiest** installation method using Microsoft’s official VS Code extension for the local MCP server.

### Installation Steps

1. **Install Visual Studio Code** from [https://code.visualstudio.com/download](https://code.visualstudio.com/download)
2. **Install GitHub Copilot Extensions:** Open VS Code, go to Extensions (`Ctrl+Shift+X`), and install both:

\- “GitHub Copilot” — “GitHub Copilot Chat”

1. **Install Power BI Modeling MCP Extension:** Search for “Power BI Modeling MCP” in the Extensions marketplace or visit [https://aka.ms/powerbi-modeling-mcp-vscode](https://aka.ms/powerbi-modeling-mcp-vscode)
2. **Verify Installation:** Open GitHub Copilot Chat and confirm “powerbi-modeling-mcp” appears in the available MCP tools

### Verification

After installation, open the GitHub Copilot Chat panel in VS Code. Click on the MCP tools icon (hammer icon) in the chat input area. You should see “powerbi-modeling-mcp” listed and selected as an available tool.

> *✅* ***Best Practice:*** *Start with* `*--readonly*` *mode when exploring a new semantic model. This prevents accidental modifications while you learn the available operations and build confidence with natural language prompts.*

### Configuration Options

To configure command-line options, open VS Code User Settings (`Ctrl+,`) and search for `@ext:Microsoft.powerbi-modeling-mcp`.

![](99.System/Attachments/1!7VWlPqtX4Io57xlT_Sz4QQ.png.webp)

## 4\. Setup: Claude Desktop (Local Server)

Claude Desktop requires manual configuration since the Power BI Modeling MCP Server is a local stdio-based server.

### Step 1: Download the MCP Server

1. Download the latest VSIX package from:
```c
https://marketplace.visualstudio.com/_apis/public/gallery/publishers/analysis-services/vsextensions/powerbi-modeling-mcp/0.2.2/vspackage?targetPlatform=win32-x64
```
1. Rename the downloaded `.vsix` file to `.zip`
2. Extract the contents to a folder, e.g.:
```c
C:\MCPServers\PowerBIModelingMCP
```

### Step 2: Locate the Claude Desktop Configuration File

The configuration file location:

- **Windows:**`%APPDATA%\Claude\claude_desktop_config.json`

You can also access this by opening Claude Desktop → Settings → Developer → Edit Config

### Step 3: Add MCP Server Configuration

Add or modify your `claude_desktop_config.json` with the following configuration:

```c
{
  "mcpServers": {
    "powerbi-modeling-mcp": {
      "type": "stdio",
      "command": "C:\\MCPServers\\PowerBIModelingMCP\\extension\\server\\powerbi-modeling-mcp.exe",
      "args": ["--start"],
      "env": {}
    }
  }
}
```

> ***Important:*** *Replace the path with the actual location where you extracted the MCP server. Use double backslashes (*`*\\*`*) in JSON paths on Windows.*

### Step 4: Restart Claude Desktop

Completely quit Claude Desktop (not just close the window) and restart it. After restart, you should see a small hammer icon in the chat input area indicating MCP servers are available.

### Optional: Additional Arguments

You can add additional arguments to the `args` array:

```c
// Read-only mode (safe exploration)
"args": ["--start", "--readonly"]
 
// Skip confirmation prompts (use with caution)
"args": ["--start", "--skipconfirmation"]
```

## 5\. Setup: Remote MCP Server (Preview)

Since November 2025, Microsoft offers a **Remote Power BI MCP Server** that enables AI agents to securely connect to semantic models in the cloud without running a local server.

### Key Differences from Local Server

![](99.System/Attachments/1!_SPLWsg5Qq2xuis6yaq1Zg.png.webp)

### Prerequisites

- Power BI admin must enable: **“Users can use the Power BI Model Context Protocol server endpoint (preview)”**
- Build permissions on at least one Power BI semantic model
- VS Code with GitHub Copilot (recommended)

### Quick Setup (VS Code)

1. Use the one-click installer or manually add to your MCP configuration:
```c
{
  "servers": {
    "powerbi-remote": {
      "type": "http",
      "url": "https://api.fabric.microsoft.com/v1/mcp/powerbi"
    }
  }
}
```
1. Start the MCP server in VS Code
2. Provide the semantic model ID when prompted
3. Authenticate with your Microsoft account

### Available Tools (Remote Server)

The remote server provides three focused tools:

![](99.System/Attachments/1!53vTk5zuOj3NmnyRGi8Yng.png.webp)

> ***Note:*** *Row-level security (RLS) is currently not enforced when using Service Principal authentication. The remote server is in preview — tool definitions may change.*

For full documentation: [Remote Power BI MCP Server](https://learn.microsoft.com/en-us/power-bi/developer/mcp/remote-mcp-server-get-started)

## 6\. Connecting to Semantic Models

Before you can perform any modeling operations, you must connect to a Power BI semantic model. There are three connection scenarios supported (for the local server).

### Option A: Power BI Desktop

Connect to a model currently open in Power BI Desktop:

1. Open your `.pbix` file in Power BI Desktop
2. In the AI chat, use the following prompt:
```c
Connect to 'Sales Report' in Power BI Desktop
```

Replace `'Sales Report'` with your actual PBIX file name (without the `.pbix` extension).

### Option B: Fabric Workspace

Connect to a semantic model published in a Microsoft Fabric workspace:

```c
Connect to semantic model 'Sales Analytics' in Fabric Workspace 'Production'
```

> ***Note:*** *Connecting to Fabric workspaces requires proper authentication. You’ll be prompted to sign in with your Microsoft account. The connection may not work in all tenants due to ongoing rollout of authentication features.*

### Option C: Power BI Project (PBIP) Files

Connect to a local PBIP project folder containing TMDL files:

```c
Open semantic model from PBIP folder 'C:\Projects\SalesReport\SalesReport.SemanticModel\definition'
```

Point to the `definition` folder within your `.SemanticModel` folder that contains the TMDL files.

## 7\. Example Use Cases and Prompts

Once connected, you can use natural language prompts to perform various modeling operations. Here are practical examples organized by scenario.

### Naming Conventions & Bulk Rename

```c
Analyze my model's naming conventions and suggest renames to ensure consistency.
```
```c
Analyze the naming convention of the 'Sales' table and apply the same pattern across the entire model.
```

### Documentation & Descriptions

```c
Add descriptions to all measures, columns, and tables to clearly explain their purpose and explain the logic behind the DAX code in simple, understandable terms.
```

### Translations

```c
Generate a German translation for my model including tables, columns and measures.
```

### Calculation Groups & Refactoring

```c
Refactor measures 'Sales Amount 12M Avg' and 'Sales Amount 6M Avg' into a calculation group and include new variants: 24M and 3M.
```

### Power Query Parameters

```c
Analyze the Power Query code for all tables, identify the data source configuration, and create semantic model parameters to enable easy switching of the data source location.
```

### DAX Query Benchmarking

```c
Connect to semantic model 'V1' and 'V2'. And benchmark the following DAX query against both models: [Your DAX Query]
```

### Model Documentation Generation

```c
Generate a Markdown document (.md) that provides complete, professional documentation for my Power BI Semantic Model. Use a simple mermaid diagram to illustrate the table relationships; Document each measure including the DAX code and a description of the business logic; Document row level filters; Document the data sources by analyzing the Power Query code.
```

> *“Use natural language to perform bulk operations on hundreds of model objects simultaneously — tasks that would take hours manually can now be executed in seconds with proper AI assistance.”*

## 8\. Available MCP Tools Reference

The MCP server exposes numerous tools that AI agents can invoke. Here are the key tools organized by category.

![](99.System/Attachments/1!D3IVDDJT2eYdwKWEl2y16A.png.webp)

## 9\. Security Considerations

MCP is a novel technology standard. **Every MCP integration requires a dedicated security review** before deployment in production environments.

> *⚠️* ***Critical Security Warning:*** *LLMs can generate syntactically valid but semantically incorrect DAX code (wrong filter propagation, context transitions). Always validate generated DAX against known test cases before deploying to production models.*

### Specific Risks to Address

![](99.System/Attachments/1!VXso-yJVeGlyROG3Q4dPnA.png.webp)

### Authentication & Credentials

- Credentials are handled through the official **Azure Identity SDK** — tokens are never stored or managed directly by the MCP server
- For Fabric workspace connections, authentication uses your Microsoft Entra ID credentials
- Follow Microsoft security guidance: enable Entra ID authentication, secure token management, and network isolation

### Permissions & RBAC

- MCP clients invoke operations based on the user’s Fabric RBAC permissions
- Apply **least-privilege RBAC roles** before deployment
- Autonomous or misconfigured clients may perform destructive actions — implement safeguards

### Version History as Safety Net

Power BI now automatically captures **up to five versions** for semantic models edited on the web or via Direct Lake in Desktop:

- Versions saved automatically when publishing `.pbix` files or restoring previous versions
- Rollback available for versions less than 14 days old
- Requires large semantic model storage format (enabled automatically on first web edit)
- **Limitation:** Not available for free-tier users or models in My Workspace

For robust version control, combine with **Git integration** for your semantic models.

### Best Practices

![](99.System/Attachments/1!Py3sGlBhylvTVbucCSzWRA.png.webp)

## 10\. Troubleshooting

### MCP server not appearing in Claude Desktop

- Verify the path in your configuration uses double backslashes (`\\`)
- Ensure the `.exe` file exists at the specified location
- Completely quit and restart Claude Desktop (not just close the window)
- Check that the JSON syntax is valid (no trailing commas, proper quotes)

### Cannot connect to Power BI Desktop

- Ensure Power BI Desktop is running with a PBIX file open
- Use the exact file name (without `.pbix` extension)
- Only one Analysis Services instance per PBIX file is supported
- Try restarting Power BI Desktop

### Fabric workspace connection fails

- This feature is in preview — may not work in all tenants
- Verify you have proper permissions on the semantic model
- Check that authentication completed successfully
- Ensure your tenant allows the required API access

### Operations timing out

- Large models may take longer to process
- Try breaking bulk operations into smaller batches
- Check your network connection for Fabric operations

### DAX queries returning errors

- Validate DAX syntax before executing
- Ensure referenced tables and columns exist
- Check for circular dependencies in measures

## 11\. Additional Resources

### Official Links

- **GitHub Repository:**[https://github.com/microsoft/powerbi-modeling-mcp](https://github.com/microsoft/powerbi-modeling-mcp)
- **VS Code Extension:**[https://aka.ms/powerbi-modeling-mcp-vscode](https://aka.ms/powerbi-modeling-mcp-vscode)
- **Remote MCP Server Docs:**[https://learn.microsoft.com/power-bi/developer/mcp/remote-mcp-server-get-started](https://learn.microsoft.com/power-bi/developer/mcp/remote-mcp-server-get-started)
- **Demo Video:**[https://aka.ms/power-modeling-mcp-demo](https://aka.ms/power-modeling-mcp-demo)
- **Troubleshooting Guide:**[https://github.com/microsoft/powerbi-modeling-mcp/blob/main/TROUBLESHOOTING.md](https://github.com/microsoft/powerbi-modeling-mcp/blob/main/TROUBLESHOOTING.md)

### Community Alternatives

Microsoft’s MCP server isn’t the only option. Community-developed alternatives may suit specific needs:

**pbi-desktop-mcp** (Maxim Anatsko)

- 26 tools, includes read-only variant for safe exploration
- Independent community project ([GitHub](https://github.com/maxanatsko/PowerBI-Desktop-MCP) )

> ***Note:*** *Community tools are not affiliated with or endorsed by Microsoft. Evaluate security and licensing before use.*

### Related Documentation

- **MCP Protocol Specification:**[https://modelcontextprotocol.io/specification/latest](https://modelcontextprotocol.io/specification/latest)
- **Microsoft Security Guidance for MCP:**[https://learn.microsoft.com/azure/api-management/secure-mcp-servers](https://learn.microsoft.com/azure/api-management/secure-mcp-servers)
- **Power BI Version History:**[https://learn.microsoft.com/power-bi/transform-model/service-semantic-model-version-history](https://learn.microsoft.com/power-bi/transform-model/service-semantic-model-version-history)
- **Power BI Project (PBIP) Documentation:**[https://learn.microsoft.com/power-bi/developer/projects/projects-dataset](https://learn.microsoft.com/power-bi/developer/projects/projects-dataset)
- **TMDL Format:**[https://learn.microsoft.com/power-bi/developer/projects/projects-dataset#tmdl-format](https://learn.microsoft.com/power-bi/developer/projects/projects-dataset#tmdl-format)

### Claude Desktop MCP Configuration

- **Claude Desktop MCP Docs:**[https://modelcontextprotocol.io/docs/develop/connect-local-servers](https://modelcontextprotocol.io/docs/develop/connect-local-servers)
- **Config File Location (Windows):**`%APPDATA%\Claude\claude_desktop_config.json`
- **Config File Location (macOS):**`~/Library/Application Support/Claude/claude_desktop_config.json` *(Note: The Power BI Modeling MCP Server is Windows-only. This path is provided for general Claude Desktop MCP configuration reference.)*

## Quick Reference: Claude Desktop Config

```c
{
  "mcpServers": {
    "powerbi-modeling-mcp": {
      "type": "stdio",
      "command": "C:\\MCPServers\\PowerBIModelingMCP\\extension\\server\\powerbi-modeling-mcp.exe",
      "args": ["--start"],
      "env": {}
    }
  }
}
```

## Quick Reference: Connection Prompts

![](99.System/Attachments/1!w0dd4_Albo_2cmxoRmxFzA.png.webp)

*Power BI Modeling MCP Server v0.2.2 (Public Preview)*

*This tutorial reflects my professional experience and perspective. Drafting was assisted by Claude, but the insights and final curation are entirely my own.*

[Sovereign AI Strategist](https://www.linkedin.com/in/michaelhannecke/) @ [bluetuple.ai](https://www.bluetuple.ai/) | Exploring autonomous AI systems, agentic architectures, and secure AI independence. Writing about what it takes to build AI that stays under your control.

**💡** [**MUST TRY — Power BI GPT — Personal Power BI Learning Coach**](https://powerbi-masterclass.short.gy/pbi-gpt?utm_source=medium&utm_campaign=pbi-gpt-medium-post-end) **💡**

> Don’t forget to subscribe to
> 
> 👉 [Power BI Publication](https://powerbi-masterclass.short.gy/publication?utm_source=medium&utm_medium=medium-post&utm_campaign=publication-medium-post-end)
> 
> 👉 [Power BI Newsletter](https://powerbi-masterclass.short.gy/newsletter-medium?utm_source=medium&utm_medium=medium-post&utm_campaign=newsletter-medium-medium-post-end)
> 
> and join our Power BI community:

## [Microsoft Power BI Masterclass | Linktree](https://linktr.ee/powerbi.masterclass?utm_source=medium&utm_medium=medium-post&utm_campaign=linktree-medium-post-end&source=post_page-----b7209d6d2506---------------------------------------)

### Let’s share our Microsoft Power BI experience. Learn together. Grow together.

linktr.ee

**Power BI Masterclass Article Classification**

**Level:** Beginner

**Category:** AI

**Tags:** Tutorial, AI