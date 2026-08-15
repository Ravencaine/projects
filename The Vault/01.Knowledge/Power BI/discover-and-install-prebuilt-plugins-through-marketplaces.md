---
title: "Discover and install prebuilt plugins through marketplaces"
source: "https://code.claude.com/docs/en/discover-plugins"
author: "code.claude.com"
date: "2026-08-11"
tags: [imported, power-bi]
created: "2026-08-11"
---

> Find and install plugins from marketplaces to extend Claude Code with new skills, agents, and capabilities.

Discover and install prebuilt plugins through marketplaces - Claude Code Docs Documentation Index Fetch the complete documentation index at: /docs/llms.txt Use this file to discover all available pages before exploring further. Skip to main content Plugins extend Claude Code with skills, agents, hooks, and MCP servers. Plugin marketplaces are catalogs that help you discover and install these extensions without building them yourself. Looking to create and distribute your own marketplace? See Create and distribute a plugin marketplace . ​ How marketplaces work A marketplace is a catalog of plugins that someone else has created and shared. Using a marketplace is a two-step process: 1 Add the marketplace This registers the catalog with Claude Code so you can browse what’s available. No plugins are installed yet. 2 Install individual plugins Browse the catalog and install the plugins you want. ​ Official Anthropic marketplace Claude Code adds the official Anthropic marketplace (  ) automatically the first time you start it interactively. If Claude Code can’t add it, for example because your network blocks the download or a marketplace policy blocked an earlier attempt, add it yourself with  . To browse what’s available, run  and go to the Discover tab, or view the catalog at claude.com/plugins . To install a plugin from the official marketplace, use  . For example, to install the GitHub integration:  opens an interactive panel in the terminal CLI. If Claude replies that  isn’t available in this environment, use the plugin browser in the Claude desktop app, or declare the plugin under  in  for cloud sessions. If the install fails, match the message Claude Code reports:  : add the marketplace with  , then retry the install. The plugin is not found in the marketplace: check the plugin name. Claude Code refreshes a stale marketplace catalog and retries before reporting this, so if you turned off marketplace auto-update , refresh manually with  and retry the install. The official marketplace is curated by Anthropic, and inclusion is at Anthropic’s discretion. The in-app submission forms add plugins to the community marketplace , not the official one. To distribute plugins independently, create your own marketplace and share it with users. The official marketplace includes several categories of plugins: ​ Code intelligence Code intelligence plugins enable Claude Code’s built-in LSP tool, giving Claude the ability to jump to definitions, find references, and see type errors immediately after edits. These plugins configure Language Server Protocol connections, the same technology that powers VS Code’s code intelligence. Install the language server binary from the table below before using these plugins; the plugin doesn’t install it for you. If you already have a language server installed, Claude may prompt you to install the corresponding plugin when you open a project. Language Plugin Binary required C/C++   C#   Go   Java   Kotlin   Lua   PHP   Python   Rust   Swift   TypeScript   You can also create your own LSP plugin for other languages. If you see  in the  Errors tab after installing a plugin, install the required binary from the table above. ​ What Claude gains from code intelligence plugins Once a code intelligence plugin is installed and its language server binary is available, Claude gains two capabilities: Automatic diagnostics : after every file edit Claude makes, the language server reports errors and warnings back, so Claude sees type errors, missing imports, and syntax issues without running a compiler or linter. If Claude introduces an error, it notices and fixes it in the same turn. Code navigation : Claude can use the language server to jump to definitions, find references, get type info on hover, list symbols, find implementations, and trace call hierarchies. These operations give Claude more precise navigation than grep-based search, though availability may vary by language and environment. You don’t need to configure diagnostics beyond installing the plugin. To read them yourself, press Ctrl+O when Claude Code shows an indicator such as Found 3 new diagnostic issues in 2 files . If you run into issues, see Code intelligence troubleshooting . ​ External integrations These plugins bundle pre-configured MCP servers so you can connect Claude to external services without manual setup: Source control :  ,  Project management :  (Jira/Confluence),  ,  ,  Design :  Infrastructure :  ,  ,  Communication :  Monitoring :  ​ Automatic security review The  plugin reviews each change Claude makes for common vulnerabilities and instructs Claude to fix what it finds in the same session. See Catch security issues as Claude writes code for what it checks and how to add project-specific rules. ​ Development workflows Plugins that add skills and agents for common development tasks: commit-commands : Git commit workflows including commit, push, and PR creation pr-review-toolkit : specialized agents for reviewing pull requests agent-sdk-dev : tools for building with the Claude Agent SDK plugin-dev : toolkit for creating your own plugins ​ Output styles Customize how Claude responds: explanatory-output-style : educational insights about implementation choices learning-output-style : interactive learning mode for skill building ​ Community marketplace The community marketplace at  hosts third-party plugins that have passed Anthropic’s automated validation and safety screening. Each plugin is pinned to a specific commit SHA in the catalog. Unlike the official marketplace, you add it manually: Then install plugins from it using the  marketplace name: To submit your own plugin to the community marketplace, see Submit your plugin to the community marketplace in the create-plugins guide. ​ Try it: add the demo marketplace Anthropic also maintains a demo plugins marketplace (  ) with example plugins that show what’s possible with the plugin system. Unlike the official marketplace, you need to add this one ma

## Code / Examples

```
claude-plugins-official
```
```
/plugin marketplace add anthropics/claude-plugins-official
```
```
/plugin
```
```
/plugin install <name>@claude-plugins-official
```
```
/plugin
```
```
/plugin
```
```
enabledPlugins
```
```
.claude/settings.json
```


---
*Source: [code.claude.com](https://code.claude.com/docs/en/discover-plugins)*
