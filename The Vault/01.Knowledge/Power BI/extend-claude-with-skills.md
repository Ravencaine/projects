---
title: "Extend Claude with skills"
source: "https://code.claude.com/docs/en/skills"
author: "code.claude.com"
date: "2026-08-11"
tags: [imported, power-bi]
created: "2026-08-11"
---

> Create, manage, and share skills to extend Claude's capabilities in Claude Code. Includes custom commands and bundled skills.

Extend Claude with skills - Claude Code Docs Documentation Index Fetch the complete documentation index at: /docs/llms.txt Use this file to discover all available pages before exploring further. Skip to main content Skills extend what Claude can do. Create a  file with instructions, and Claude adds it to its toolkit. Claude uses skills when relevant, or you can invoke one directly with  . Create a skill when you keep pasting the same instructions, checklist, or multi-step procedure into chat, or when a section of CLAUDE.md has grown into a procedure rather than a fact. Unlike CLAUDE.md content, a skill’s body loads only when it’s used, so long reference material costs almost nothing until you need it. For built-in commands like  and  , and bundled skills like  and  , see the commands reference . Custom commands have been merged into skills. A file at  and a skill at  both create  and work the same way. Your existing  files keep working. Skills add optional features: a directory for supporting files, frontmatter to control whether you or Claude invokes them , and the ability for Claude to load them automatically when relevant. Claude Code skills follow the Agent Skills open standard, which works across multiple AI tools. Claude Code extends the standard with additional features like invocation control , subagent execution , and dynamic context injection . See Using skill frontmatter outside Claude Code for which frontmatter fields are part of the standard and which are Claude Code extensions. ​ Bundled skills Claude Code includes a set of bundled skills, such as  ,  ,  ,  ,  , and  . Bundled skills are prompt-based: they give Claude detailed instructions and let it orchestrate the work using its tools. Most built-in commands instead execute fixed logic directly. You invoke a bundled skill the same way as any other skill, by typing  followed by the skill name. Claude invokes some bundled skills automatically when relevant; others, including  and  , run only when you invoke them, which keeps you in control of when these longer-running checks spend time and tokens. Before v2.1.215, Claude could also run  and  on its own. Bundled skills are available in every session. To turn them off, use the  setting, which disables every bundled skill except  . The  setup checkup stays typable when  is on, in Claude Code v2.1.205 and later. To hide it, set the  environment variable or a  entry of  . Before v2.1.205,  was a built-in command rather than a bundled skill. Bundled skills are listed alongside built-in commands in the commands reference , marked Skill in the Purpose column. ​ Run and verify your app Three bundled skills work together to launch your app and confirm changes against the running app instead of just tests: Skill Purpose  Launch and drive your app to see a change working  Build and run your app to confirm a code change does what it should, without falling back to tests or type checks  Teach  and  how to build and launch your project All three skills require Claude Code v2.1.145 or later. Check your version with  or the  command.  and  work without setup. They infer the launch from your project type (CLI, server, TUI, browser-driven) and from what’s in your README,  , or  . That inference gets unreliable for projects that need anything beyond a standard launch: a database, an env file, a graphical session, a multi-step build.  records the recipe instead. It gets your app running from a clean environment, captures what worked (the install commands, the env vars, the launch script), and commits it as a per-project skill at  . After that,  ,  , and any other agent in the repo follow the recorded recipe instead of rediscovering it. Run  once per project, and again if the build or launch process changes.  can also record its own recipe. When it has to build and drive your app without a recorded recipe, it writes what worked to  at the repo root, or in the touched package directory in a monorepo, so later runs and other agents follow the same steps. At the repo root, the recorded skill replaces the bundled  . This requires Claude Code v2.1.200 or later. Claude edits the recorded file only when it steered a run wrong, such as a command that failed or a missing step, so you can commit the file without per-session diffs. Before v2.1.205, the bundled skill told Claude to fold in anything a run learned, which caused frequent merge conflicts. ​ Getting started ​ Create your first skill This example creates a skill that summarizes the uncommitted changes in your git repository and flags anything risky. It pulls the live diff into the prompt before Claude reads it, so the response is grounded in your actual working tree rather than what Claude can guess from open files. Claude loads the skill automatically when you ask about your changes, or you can invoke it directly with  . 1 Create the skill directory Create a directory for the skill in your personal skills folder. Personal skills are available across all your projects. 2 Write SKILL.md Every skill needs a  file with two parts: YAML frontmatter between  markers that tells Claude when to use the skill, and markdown content with the instructions Claude follows when the skill runs. The directory name becomes the command you type, and the  helps Claude decide when to load the skill automatically. Save this to  : The  line uses dynamic context injection : Claude Code runs the command and replaces the line with its output before Claude sees the skill content, so the instructions arrive with the current diff already inlined. 3 Test the skill Open a git project, make a small edit to any file, and start Claude Code by running  . You can test the skill two ways. Let Claude invoke it automatically by asking something that matches the description: Or invoke it directly with the skill name: Either way, Claude should respond with a short summary of your edit and a list of risks. ​ Where skills live Where you store a skill determines who can use it: Location Pat

## Code / Examples

```
SKILL.md
```
```
/skill-name
```
```
/help
```
```
/compact
```
```
/debug
```
```
/code-review
```
```
.claude/commands/deploy.md
```
```
.claude/skills/deploy/SKILL.md
```


---
*Source: [code.claude.com](https://code.claude.com/docs/en/skills)*
