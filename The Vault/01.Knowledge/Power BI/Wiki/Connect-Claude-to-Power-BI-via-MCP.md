---
created: 2026-08-06
updated: 2026-08-06
source: Claude Power BI MCP Integration
note_type: workflow
tags: [mcp, claude, power-bi, ai, setup, desktop]
---

# Connect Claude to Power BI via MCP

Set up the Claude Power BI MCP integration to control Power BI Desktop from Claude AI via VS Code — enabling AI-assisted DAX generation, metadata population, and model organisation.

## Prerequisites

- **Visual Studio Code:** code editor
- **Power BI Desktop:** latest version, with a `.pbix` file open
- **Claude Desktop for Windows:** desktop app from Anthropic
- **Power BI MCP extension** for VS Code — the MCP server that bridges Claude to Power BI

## Steps

1. **Install Visual Studio Code**  
   Download from https://code.visualstudio.com/ and install.

2. **Install the Power BI MCP extension in VS Code**  
   Open VS Code → Extensions → search "Power BI MCP" → install.

3. **Install Claude Desktop for Windows**  
   Download and install from https://claude.ai/download.

4. **Configure the MCP server in Claude Desktop**  
   Open the Claude Desktop config file and add the Power BI MCP server connection:

   ```
   // claude_desktop_config.json
   "mcpServers": {
     "powerbi": {
       "command": "code",
       "args": ["--extension", "powerbi-mcp"]
     }
   }
   ```

   (Or use the specific command/path for the installed extension — check the extension documentation for the exact config.)

5. **Restart Claude Desktop and VS Code**  
   Close both applications completely and relaunch.

6. **Open a Power BI Desktop model**  
   Open the `.pbix` file you want to work with.

7. **Connect Claude**  
   In Claude Desktop, prompt: *"Connect to the open Power BI Desktop file"*

## Verify the Connection

Ask Claude to list all tables in the model:

```
Prompt: "List all tables in the semantic model and show their column names"
```

If tables are returned, the connection is active.

## Common Errors

- **Extension not appearing:** ensure VS Code is restarted after installing the Power BI MCP extension
- **Claude cannot connect:** verify the MCP server config in `claude_desktop_config.json` is correct
- **No tables returned:** ensure Power BI Desktop is open with a model loaded

## Related

- [[Claude-Power-BI-MCP-Integration]] — concept overview
- [[7-AI-Prompts-for-Power-BI-MCP]] — reference card of 7 prompts
- [[mcp-power-bi-semantic-model-workflow]] — Power BI Service MCP workflow (read-only)
- [[mcp-power-bi-modeling-preview-caveats]] — governance and trust requirements
