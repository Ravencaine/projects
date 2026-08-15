---
title: "My Claude Code Workflow And Personal Tips"
source: "https://substack.com/home/post/p-167419041"
author: "substack.com"
date: "2026-08-11"
tags: [imported, power-bi]
created: "2026-08-11"
---

> How I use roadmap + task files to manage Claude Code, and my personal tips for effective Claude Code usage.

My Claude Code Workflow And Personal Tips - by Zhu Liang The Ground Truth Subscribe Sign in My Claude Code Workflow And Personal Tips How I use roadmap + task files to manage Claude Code, and my personal tips for effective Claude Code usage. Zhu Liang Jul 03, 2025 34 5 2 Share I have shared bits and pieces of my current coding workflow with Claude Code (and Cursor). Many people wanted to know more details and the exact setup I use, so here it is, along my personal tips on how to use Claude Code effectively. My Current Workflow Setup ROADMAP.md Have a ROADMAP.md file inside reference folder:  . The ROADMAP.md describes two things: The overall development process The high level overview of each task in a few bullet points The ROADMAP.md file acts as the single entry point to planning out new features, adjusting priorities and working on new tasks. Make sure to include the ROADMAP.md file explicitly inside CLAUDE.md (via the CLAUDE.md import syntax ) or Cursor rules (via reference ). Explicit reference via @ syntax You can verify that the import is working by using the  command inside Claude Code, it should print out full the memory import structure: By explicitly including the file as part of memory / rules, the agent has access to the full high-level context of the project for each task, effectively grounding the agent and guiding it to the correct path. Here’s an excerpt of my current ROADMAP.md for my new app 16x Writer , which describes the development workflow and high-level tasks / features: I have published the full ROADMAP.md on GitHub for your reference. Individual Task Plans While ROADMAP.md gives the high-level overview of each task, the detailed planning of each task is carried out separately as individual files inside  folder:     … Screenshot of sample task planning files for 16x Writer You can think of these files are a combination of PRD (product requirement document) and system design (architecture) for each feature. Each file includes the following components: Prerequisites Background and requirements Current state and desired states Implementation steps Files that needs to modified and created Acceptance criteria Here is an excerpt of a sample task planning file: I have published the full task plan sample file on GitHub for your reference. Note that with the non-deterministic nature of AI agents, the plan is merely a guide for the agent, not a rule that the agent will follow 100%. I have observed that agents tend to overlook certain instructions or requirements inside the document, especially when the task is complex, or when the initial planning was not very clear on specific parts of the task. So it is best to treat it as a draft plan that the agent can reference during the implementation, instead of expecting it be followed religiously. Claude Code now has a planning mode which performs a similar function as the task planning files. However, the task planning files are still useful. They can serve a persistent reference for future features, as it is part of the repo, and can be accessed easily by humans and agents alike. Claude Code plans are not persistent and are gone after you start a new session. Update on Feb 2026: You can now save the plan files from Claude Code plan mode into current project via plansDirectory option in Claude Code. Ad Hoc Tasks and Refactoring I also have a dedicated file for tracking ad hoc tasks that are too small for ROADMAP.md, but also significant enough to warrant recording-keeping. They reside inside  and  . Sample REFACTORS.md I mainly use them for small enhancement features and refactoring that are worth keeping track of. While you can just prompt the coding agent to work on them directly, tracking them inside a file have some benefits: For example, when working on a big feature, you notice a small refactoring is needed. You can record it inside  first and then prompt agent to work on it later. With the advancement of background async agents, you could also have agents that periodically analyse the codebase, record down refactoring and enhancement opportunities inside the file. Then you can spawn another set of agents to work on them autonomously. Folder Structure Setup Here’s an tree overview of the folder structure of my current setup: My Claude Code Workflow Since most of the workflow is already described in the ROADMAP.md file, the exact workflow I use is quite simple to describe. For big features: Describe my requirement (in a few sentences) to the agent, which would update  to add a new task with high-level summary Review the summary captured by the agent and adjust them if necessary (remove unnecessary features, or take care of special interactions) Example high-level summary for tasks, some requires manual editing Ask agent to write more detailed plan in individual task files inside  folder Note that inside ROADMAP.md, I have instructions for the agent to study the existing codebase and understand the current state before writing the plan, as part of the development workflow. This guides the agent to retrieve relevant context before planning. Review the plan generated to see if it is on the right track Prompt the agent to make amendments to the plan if necessary Once you are happy with the plan, exit the current session or clear the agent’s context and start a new session with fresh context , so that you get maximum context window for the actual implementation. Ask agent to implement one step at a time (pause after each step and await for human review), or complete the whole task (don’t pause after each step, just proceed to next step automatically until the whole task is completed) For small enhancements or refactoring: Record tasks inside  or  Ask Claude Code to implement one-by-one Do one task per session (Use  command or restart Claude Code) to avoid wasting tokens (sending context from previous task to the next task) One-Shotting Multi-Step Tasks Lately I have been asking the agent to just work on the task from start to f

## Code / Examples

```
reference/ROADMAP.md
```
```
/status
```
```
tasks
```
```
001-db.md
```
```
002-source-library.md
```
```
003-e2e-testing.md
```
```
004-source-refactor-context.md
```
```
reference/AD_HOC_TASKS.md
```


---
*Source: [substack.com](https://substack.com/home/post/p-167419041)*
