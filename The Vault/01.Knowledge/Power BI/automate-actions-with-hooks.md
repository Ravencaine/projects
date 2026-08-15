---
title: "Automate actions with hooks"
source: "https://code.claude.com/docs/en/hooks-guide"
author: "code.claude.com"
date: "2026-08-11"
tags: [imported, power-bi]
created: "2026-08-11"
---

> Run shell commands automatically when Claude Code edits files, finishes tasks, or needs input. Format code, send notifications, validate commands, and enforce project rules.

Automate actions with hooks - Claude Code Docs Documentation Index Fetch the complete documentation index at: /docs/llms.txt Use this file to discover all available pages before exploring further. Skip to main content Hooks are user-defined shell commands. Claude Code runs them at specific points in its lifecycle, which gives you deterministic control: certain actions always happen rather than relying on the LLM to choose to run them. Use hooks to enforce project rules, automate repetitive tasks, and integrate Claude Code with your existing tools. For decisions that require judgment rather than deterministic rules, you can also use prompt-based hooks or agent-based hooks that use a Claude model to evaluate conditions. For other ways to extend Claude Code, see skills for giving Claude additional instructions and executable commands, subagents for running tasks in isolated contexts, and plugins for packaging extensions to share across projects. This guide covers common use cases and how to get started. For full event schemas, JSON input/output formats, and advanced features like async hooks and MCP tool hooks, see the Hooks reference . ​ Set up your first hook To create a hook, add a  block to a settings file . This walkthrough creates a desktop notification hook, so you get alerted whenever Claude is waiting for your input instead of watching the terminal. 1 Add the hook to your settings Open  and add a  hook. If the file doesn’t exist, create it. The example below uses  for macOS; see Get notified when Claude needs input for Linux and Windows commands. If your settings file already has a  key, add  as a sibling of the existing event keys rather than replacing the whole object. Each event name is a key inside the single  object: You can also ask Claude to write the hook for you by describing what you want in the CLI. 2 Verify the configuration Type  to open the hooks browser. You’ll see a list of all available hook events, with a count next to each event that has hooks configured. Select  to confirm your new hook appears in the list. Selecting the hook shows its details: the event, matcher, type, source file, and command. 3 Test the hook Press  to return to the CLI. Ask Claude to do something that requires permission, then switch away from the terminal. You should receive a desktop notification. The  menu is read-only. To add, modify, or remove hooks, edit your settings JSON directly or ask Claude to make the change. ​ What you can automate Hooks let you run code at key points in Claude Code’s lifecycle: format files after edits, block commands before they execute, send notifications when Claude needs input, inject context at session start, and more. For the full list of hook events, see the Hooks reference . Each example includes a ready-to-use configuration block that you add to a settings file . For a production example of hooks that run a separate model review and feed findings back into the session, see how the  plugin integrates with Claude Code . ​ Get notified when Claude needs input Get a desktop notification whenever Claude finishes working and needs your input, so you can switch to other tasks without checking the terminal. This hook uses the  event, which Claude Code fires when Claude is waiting for input or permission. See when each notification type fires for the exact timing. Each tab below uses the platform’s native notification command. Add this to  : macOS Linux Windows (PowerShell) If no notification appears  routes notifications through the built-in Script Editor app. If Script Editor doesn’t have notification permission, the command fails silently, and macOS won’t prompt you to grant it. Run this in Terminal once to make Script Editor appear in your notification settings: Nothing will appear yet. Open System Settings > Notifications , find Script Editor in the list, and turn on Allow Notifications . Run the command again to confirm the test notification appears. If no notification appears  needs a desktop notification daemon, which headless servers, SSH sessions, and most containers don’t have. Test the command directly first: If the command isn’t found, install the  package on Debian and Ubuntu, or your distribution’s equivalent. If no dialog appears This command opens a dialog box rather than a notification in the corner of your screen, so the dialog can open behind your terminal window. Test the command directly in PowerShell first. If you run Claude Code inside WSL,  must be available on your  through Windows interop. The empty  fires on all notification types. To fire only on specific events, set it to one of these values: Matcher Fires when  Claude needs you to approve a tool use and you haven’t typed for about 6 seconds  Claude finished responding about 60 seconds ago and you haven’t typed since  Authentication completes  An MCP server opens an elicitation form and you haven’t typed for about 6 seconds  An MCP server asks you to open a browser URL and you haven’t typed for about 6 seconds  An MCP elicitation form is submitted or dismissed  An MCP elicitation response is sent back to the server  A background session starts waiting on your input. Fires only while agent view is open  A background session finishes or fails. Fires only while agent view is open The  and  matchers require Claude Code v2.1.198 or later. Type  and select  to confirm the hook is registered. For the full event schema, see the Notification reference . ​ Auto-format code after edits Automatically run Prettier on every file Claude edits, so formatting stays consistent without manual intervention. This hook uses the  event with an  matcher, so it runs only after file-editing tools. The command extracts the edited file path with  and passes it to Prettier. Add this to  in your project root: To test the hook, ask Claude to add a line with single-quoted strings to a JavaScript file, then open the file: with Prettier’s default settings, the hook rewrites them to double quotes. When the hook succe

## Code / Examples

```
hooks
```
```
~/.claude/settings.json
```
```
Notification
```
```
osascript
```
```
hooks
```
```
Notification
```
```
hooks
```
```
/hooks
```


---
*Source: [code.claude.com](https://code.claude.com/docs/en/hooks-guide)*
