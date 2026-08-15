---
title: "Connect Claude Code to tools via MCP"
source: "https://code.claude.com/docs/en/mcp"
author: "code.claude.com"
date: "2026-08-11"
tags: [imported, power-bi]
created: "2026-08-11"
---

> Learn how to connect Claude Code to your tools with the Model Context Protocol.

Connect Claude Code to tools via MCP - Claude Code Docs Documentation Index Fetch the complete documentation index at: /docs/llms.txt Use this file to discover all available pages before exploring further. Skip to main content Claude Code can connect to hundreds of external tools and data sources through the Model Context Protocol (MCP) , an open source standard for AI-tool integrations. MCP servers give Claude Code access to your tools, databases, and APIs. Connect a server when you find yourself copying data into chat from another tool, like an issue tracker or a monitoring dashboard. Once connected, Claude can read and act on that system directly instead of working from what you paste. If you’re connecting your first server, start with the MCP quickstart for a step-by-step walkthrough. This page is the full reference. ​ What you can do with MCP With MCP servers connected, you can ask Claude Code to: Implement features from issue trackers : “Add the feature described in JIRA issue ENG-4521 and create a PR on GitHub.” Analyze monitoring data : “Check Sentry and Statsig to check the usage of the feature described in ENG-4521.” Query databases : “Find emails of 10 random users who used feature ENG-4521, based on our PostgreSQL database.” Integrate designs : “Update our standard email template based on the new Figma designs that were posted in Slack” Automate workflows : “Create Gmail drafts inviting these 10 users to a feedback session about the new feature.” React to external events : an MCP server can also act as a channel that pushes messages into your session, so Claude reacts to Telegram messages, Discord chats, or webhook events while you’re away. ​ Find and build MCP servers Browse reviewed connectors in the Anthropic Directory . Directory connectors use the same MCP infrastructure as Claude Code, so you can add any remote server listed there with  . Verify you trust each server before connecting it. Servers that fetch external content can expose you to prompt injection risk . To build your own server, see the MCP server guide for protocol fundamentals and the Claude connector building docs for authentication, testing, and Directory submission. You can also have Claude scaffold a server for you with the official  plugin . 1 Install the plugin In a Claude Code session, run: If the install fails, match the message Claude Code reports:  : add the marketplace with  , then retry the install. The plugin is not found in the marketplace: check the plugin name. Claude Code refreshes a stale marketplace catalog and retries before reporting this, so if you turned off marketplace auto-update , refresh manually with  and retry the install. Check the install summary: if it reports  , run that command. 2 Run the build skill Claude asks about your use case and scaffolds a remote HTTP or local stdio server. ​ Installing MCP servers MCP servers can be configured in several ways depending on your needs: ​ Option 1: Add a remote HTTP server HTTP servers are the recommended option for connecting to remote MCP servers. This is the most widely supported transport for cloud-based services. When configuring MCP servers via JSON in  ,  , or  , the  field accepts  as an alias for  . The MCP specification uses the name  for this transport, so configurations copied from server documentation work without modification. A JSON entry that has a  but no  is a configuration error, because Claude Code reads an entry with no  as a stdio server. Claude Code skips that server and reports  . Before v2.1.202, Claude Code reported this misconfiguration as  . In  runs, Claude Code also reports a skipped  entry in the  event’s  field , so scripts can detect that the server never loaded. This requires Claude Code v2.1.219 or later. ​ Option 2: Add a remote SSE server The SSE (Server-Sent Events) transport is deprecated. Use HTTP servers instead, where available. Some services still expose only an SSE endpoint. Use the same command as the HTTP transport, with  : ​ Option 3: Add a local stdio server Stdio servers run as local processes on your machine. They’re ideal for tools that need direct system access or custom scripts. Claude Code sets  in the spawned server’s environment to the project root, so your server can resolve project-relative paths without depending on the working directory. This is the same directory hooks receive in their  variable. Read it from inside your server process, for example  in Node or  in Python.  is the stable project root and doesn’t change when you add or remove working directories mid-session. A server that limits its own filesystem access to a set of allowed directories should implement the MCP  request instead. Claude Code answers  with the session’s launch directory plus every additional working directory you’ve granted with  ,  , or the  setting. Claude Code sends  when that set changes. Before v2.1.203,  returned only the launch directory and Claude Code didn’t send  . This variable is set in the server’s environment, not in Claude Code’s own environment, so referencing it via  expansion in the  or  of a project-scoped  entry or a local- or user-scoped server entry in  requires a default such as  . Plugin-provided MCP configurations substitute  directly and don’t need the default. Important: Separate server arguments with  For stdio servers, the  (double dash) separates Claude’s own options, such as  ,  , and  , from the command and arguments that run the server. Everything after  is passed to the server untouched. For example:  → runs   → runs  with  in environment Without  , Claude Code would try to parse the server’s flags, like  above, as its own options.  accepts multiple  pairs. If the server name comes directly after  , the CLI reads the name as another pair and rejects it, so place at least one other option between  and the server name, as in the examples above. ​ Option 4: Add a remote WebSocket server WebSocket servers hold a persistent bidirectional connection, which suits remot

## Code / Examples

```
claude mcp add
```
```
mcp-server-dev
```
```
Marketplace "claude-plugins-official" not found
```
```
/plugin marketplace add anthropics/claude-plugins-official
```
```
/plugin marketplace update claude-plugins-official
```
```
Run /reload-plugins to activate.
```
```
.mcp.json
```
```
~/.claude.json
```


---
*Source: [code.claude.com](https://code.claude.com/docs/en/mcp)*
