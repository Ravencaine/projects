---
title: "Troubleshooting"
source: "https://code.claude.com/docs/en/troubleshooting"
author: "code.claude.com"
date: "2026-08-11"
tags: [imported, power-bi]
created: "2026-08-11"
---

> Fix high CPU or memory usage, hangs, auto-compact thrashing, and search problems in Claude Code, and find the right page for other issues.

Troubleshooting - Claude Code Docs Documentation Index Fetch the complete documentation index at: /docs/llms.txt Use this file to discover all available pages before exploring further. Skip to main content This page covers performance, stability, and search problems once Claude Code is running. For other issues, start with the page that matches where you’re stuck: Symptom Go to  , install fails, PATH issues,  , TLS errors Troubleshoot installation and login Update or install download fails with  or  Error reference Login loops, OAuth errors,  , “organization disabled”, Amazon Bedrock, Google Cloud’s Agent Platform, or Microsoft Foundry credentials Troubleshoot installation and login Settings not applying, hooks not firing, MCP servers not loading Debug your configuration  ,  ,  , request validation errors Error reference  or  Error reference VS Code extension not connecting or detecting Claude VS Code integration  in VS Code or an SDK app Error reference JetBrains plugin or IDE not detected JetBrains integration High CPU or memory, slow responses, hangs, search not finding files Performance and stability below If you’re not sure which applies, run  inside Claude Code for an automated check of your installation, settings, extensions, and context usage; it proposes fixes it can apply after you confirm. If  won’t start at all, run  from your shell instead. Run  to check MCP server status. ​ Performance and stability These sections cover issues related to resource usage, responsiveness, and search behavior. ​ High CPU or memory usage Claude Code is designed to work with most development environments, but may consume significant resources when processing large codebases. If you’re experiencing performance issues: Use  regularly to reduce context size. If it returns  , the conversation has too few turns to summarize; that can happen even with a full context when a single large paste filled it Close and restart Claude Code between major tasks Consider adding large build directories to your  file Restart with  to check whether a plugin, MCP server, or hook is the source. It disables all customizations for the session; if usage drops, see Debug your configuration to find which one If memory usage stays high after these steps, run  to write two files to  : a JavaScript heap snapshot named  and a memory breakdown named  . The command doesn’t appear in the command menu; type it in full. On Linux without a Desktop folder, the files are written to your home directory. The  file contains every string in the process, including your full conversation and credentials. Don’t attach it to a public issue or share it. The command also prints a summary in the conversation, showing resident set size, JS heap, array buffers, and unaccounted native memory, plus any leak indicators it detected, such as a high memory growth rate or an unusually high number of open handles. The summary says whether most memory is in the JS heap, which the snapshot captures, or in native memory, which it doesn’t. Do one of two things with the output: Report it : open a GitHub issue and attach only the  file, which carries the statistics behind the printed summary and no conversation content or credentials Investigate it yourself : if the summary says most memory is JS heap, open the  file in Chrome DevTools under Memory → Load and sort by retained size to see what’s holding the memory If the summary says most memory is native, the snapshot can’t show it; include the summary’s leak indicators in your report instead. ​ Large tables are cut off in the terminal A Markdown table with more than 200 rows renders its first 200 rows followed by a  line. Only the display is capped: the full table stays in the conversation, and  copies every row. For a table too large to read in the terminal, ask Claude to write it to a file instead. Before v2.1.208, Claude Code rendered every row, so resuming a session that contained a very large table could stall while it re-rendered. ​ Auto-compaction stops with a thrashing error If you see  , automatic compaction succeeded but a file or tool output immediately refilled the context window several times in a row. Claude Code stops retrying to avoid wasting API calls on a loop that isn’t making progress. To recover: Ask Claude to read the oversized file in smaller chunks, such as a specific line range or function, instead of the whole file Run  with a focus that drops the large output, for example  Move the large-file work to a subagent so it runs in a separate context window Run  if the earlier conversation is no longer needed ​ Command hangs or freezes If Claude Code seems unresponsive: Press Ctrl+C to attempt to cancel the current operation If unresponsive, you may need to close the terminal and restart Restarting doesn’t lose your conversation. Run  in the same directory to pick the session back up. ​ Garbled or corrupted text in an editor’s integrated terminal If characters render as boxes, smears, or the wrong glyphs when running Claude Code in the VS Code, Cursor, or Devin Desktop integrated terminal, the terminal’s GPU renderer is likely the cause. Run  inside Claude Code to set  to  , or set it manually in your editor settings and reload the window. See Terminal configuration for the other settings  writes. ​ Search and discovery issues If the Search tool,  mentions, custom agents, or custom skills aren’t finding files, the bundled  binary may not run on your system. Install your platform’s  package and tell Claude Code to use it instead: macOS Ubuntu/Debian Alpine Arch Windows  is in Alpine’s community repository. If  reports that the package is missing, see Alpine Linux setup . Then set  to  , either in your shell environment or in the  block of your  : To confirm the switch took effect, run  in your terminal and check that the Search line shows the path of your system ripgrep instead of  . ​ Slow or incomplete search results on WSL Disk read performance penalties when working across file systems on

## Code / Examples

```
command not found
```
```
EACCES
```
```
The connection dropped while downloading the update
```
```
aborted
```
```
403 Forbidden
```
```
API Error: 5xx
```
```
529 Overloaded
```
```
429
```


---
*Source: [code.claude.com](https://code.claude.com/docs/en/troubleshooting)*
