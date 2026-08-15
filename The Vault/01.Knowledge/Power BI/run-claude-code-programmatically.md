---
title: "Run Claude Code programmatically"
source: "https://code.claude.com/docs/en/headless"
author: "code.claude.com"
date: "2026-08-11"
tags: [imported, power-bi]
created: "2026-08-11"
---

> Use the Agent SDK to run Claude Code programmatically from the CLI, Python, or TypeScript.

Run Claude Code programmatically - Claude Code Docs Documentation Index Fetch the complete documentation index at: /docs/llms.txt Use this file to discover all available pages before exploring further. Skip to main content The Agent SDK gives you the same tools, agent loop, and context management that power Claude Code. It’s available as a CLI for scripts and CI/CD, or as Python and TypeScript packages for full programmatic control. To run Claude Code in non-interactive mode, pass  with your prompt and the CLI options you need: This page covers using the Agent SDK via the CLI (  ). For the Python and TypeScript SDK packages with structured outputs, tool approval callbacks, and native message objects, see the full Agent SDK documentation . ​ Basic usage Add the  (or  ) flag to any  command to run it non-interactively. Not every CLI option combines with  . Claude Code rejects  , and rejects  with a task description, with an error naming the conflict;  with a session ID and  instead queues a message into that cloud session and exits. Options you’ll combine with  often include:  for continuing conversations  for auto-approving tools  for structured output This example asks Claude a question about your codebase and prints the response: Claude Code exits with code 0 on success and a non-zero code when the run fails, so your scripts can branch on the exit status. If you pass an invalid flag, Claude Code reports the error to stderr before the run starts. When a failure happens inside the run, such as missing authentication, Claude Code prints the failure as the result on stdout. ​ Start faster with bare mode Add  to reduce startup time by skipping auto-discovery of hooks, skills, plugins, MCP servers, auto memory, and CLAUDE.md. Without it,  loads the same context an interactive session would, including anything configured in the working directory or  . Bare mode is useful for CI and scripts where you need the same result on every machine. A hook in a teammate’s  or an MCP server in the project’s  won’t run, because bare mode never reads them. This example runs a one-off summarize task in bare mode and pre-approves the Read tool so the call completes without a permission prompt. Set  before running it, because bare mode doesn’t use your subscription login: In bare mode, Claude Code never reads OAuth credentials or the system keychain. For the Anthropic API, set  in the environment, with a key created in the Claude Console , or supply an  in the  JSON. Amazon Bedrock, Google Cloud’s Agent Platform, and Microsoft Foundry continue to read their own provider credentials as usual. In bare mode Claude has access to the Bash, file read, and file edit tools. Pass any context you need with a flag: To load Use System prompt additions  ,  Settings  MCP servers  Custom agents  A plugin  ,   is the recommended mode for scripted and SDK calls, and will become the default for  in a future release. ​ Background tasks at exit If Claude starts a background Bash task during a  run, for example a dev server or a watch build, that shell is terminated about five seconds after Claude has returned its final result and stdin has closed. The grace period lets a task that finishes right after the result still deliver its output. Before v2.1.163, a never-exiting background process would hold the  invocation open indefinitely. Background subagents and workflows are exempt from the five-second grace because their result is part of the final output, so  waits for them to complete. From v2.1.182, that wait is capped at ten minutes by default so a stuck background agent cannot hold the process open indefinitely. Adjust the cap with  , or set it to  to wait without a limit. If you stop a  run with SIGTERM, for example from  , a process supervisor, or an SDK host closing the session, Claude Code aborts the in-progress turn, terminates the process tree of any running Bash command, runs  hooks , and exits with code 143. ​ Examples These examples highlight common CLI patterns. Where a command names a file such as  or  , substitute a file from your own project. In CI or other scripted environments, add  so Claude Code starts without loading the host’s hooks, plugins, auto memory, or  . ​ Pipe data through Claude Non-interactive mode reads stdin, so you can pipe data in and redirect the response out like any other command-line tool. This example pipes a build log into Claude and writes the explanation to a file: With  , the response payload includes  and a per-model cost breakdown, so scripted callers can track spend per invocation without consulting the usage dashboard . Both figures are client-side estimates and can differ from your actual bill. Piped stdin is capped at 10MB. If you exceed the cap, Claude Code exits with a clear error and a non-zero status. To work with larger inputs, write the content to a file and reference the file path in your prompt instead of piping it. If Claude Code can’t read stdin, for example because the process that started it disconnected its end, Claude Code prints a warning to stderr and continues with the prompt from the command line. Before v2.1.211, an unreadable stdin on Windows crashed the session or made it exit silently with no output. ​ Add Claude to a build script You can wrap a non-interactive call in a script to use Claude as a project-specific linter or reviewer. This  script pipes the diff against  into Claude and asks it to report typos. Piping the diff means Claude doesn’t need Bash permission to read it, and the escaped double quotes keep the script portable to Windows: Run it with  . ​ Get structured output Use  to control how responses are returned:  (default): plain text output  : structured JSON with result, session ID, and metadata  : newline-delimited JSON for real-time streaming This example returns a project summary as JSON with session metadata, with the text result in the  field: To get output conforming to a specific schema, use  with  and a JSON Schema definition. The respo

## Code / Examples

```
-p
```
```
claude -p
```
```
-p
```
```
--print
```
```
claude
```
```
-p
```
```
--bg
```
```
--cloud
```


---
*Source: [code.claude.com](https://code.claude.com/docs/en/headless)*
