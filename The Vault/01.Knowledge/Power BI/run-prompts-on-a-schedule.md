---
title: "Run prompts on a schedule"
source: "https://code.claude.com/docs/en/scheduled-tasks"
author: "code.claude.com"
date: "2026-08-11"
tags: [imported, power-bi]
created: "2026-08-11"
---

> Use /loop and the cron scheduling tools to run prompts repeatedly, poll for status, or set one-time reminders within a Claude Code session.

Run prompts on a schedule - Claude Code Docs Documentation Index Fetch the complete documentation index at: /docs/llms.txt Use this file to discover all available pages before exploring further. Skip to main content Scheduled tasks let Claude re-run a prompt automatically on an interval. Use them to poll a deployment, babysit a PR, check back on a long-running build, or remind yourself to do something later in the session. To react to events as they happen instead of polling, see Channels : your CI can push the failure into the session directly. To keep the session working turn after turn until a condition is met rather than on an interval, see  . Tasks are session-scoped: they live in the current conversation and stop when you start a new one. Resuming with  or  brings back any task that hasn’t expired : a recurring task created within the last 7 days, or a one-shot whose scheduled time hasn’t passed yet. For scheduling that survives independently of any session, use Routines to create a routine on the cloud, set up a Desktop scheduled task , or use GitHub Actions . ​ Compare scheduling options Claude Code offers three ways to schedule recurring or one-off work: Cloud Desktop  Runs on Cloud, Anthropic-managed by default Your machine Your machine Requires machine on No Yes Yes Requires open session No No Yes Persistent across restarts Yes Yes Restored on  if unexpired Access to local files No (fresh clone) Yes Yes MCP servers Connectors configured per task Config files and connectors Inherits from session Permission prompts No (runs autonomously) Configurable per task Inherits from session Customizable schedule Via  in the CLI Yes Yes Minimum interval 1 hour 1 minute 1 minute Use cloud tasks for work that should run reliably without your machine. Use Desktop tasks when you need access to local files and tools. Use  for quick polling during a session. ​ Run a prompt repeatedly with /loop The  bundled skill is the quickest way to run a prompt on repeat while the session stays open. Both the interval and the prompt are optional, and what you provide determines how the loop behaves. What you provide Example What happens Interval and prompt  Your prompt runs on a fixed schedule Prompt only  Your prompt runs at an interval Claude chooses each iteration Interval only, or nothing  The built-in maintenance prompt runs, or your  if one exists You can also pass a skill as the prompt, for example  , to re-run that skill each iteration. As of v2.1.196, a scheduled fire only runs skills that Claude is allowed to invoke on its own . The following reach Claude as plain text instead of executing: Built-in commands such as  ,  , or  Skills marked  , including the bundled  and  skills. Skills withheld from Claude by a  setting or a  deny rule MCP prompts such as  ​ Run on a fixed interval When you supply an interval, Claude converts it to a cron expression, schedules the job, and confirms the cadence and job ID. The interval can lead the prompt as a bare token like  , or trail it as a clause like  . Supported units are  for seconds,  for minutes,  for hours, and  for days. Seconds are rounded up to the nearest minute since cron has one-minute granularity. Intervals that don’t map to a clean cron step, such as  or  , are rounded to the nearest interval that does and Claude tells you what it picked. ​ Let Claude choose the interval When you omit the interval, Claude chooses one dynamically instead of running on a fixed cron schedule. After each iteration it picks a delay between one minute and one hour based on what it observed: short waits while a build is finishing or a PR is active, longer waits when nothing is pending. The chosen delay and the reason for it are printed at the end of each iteration. The example below checks CI and review comments, with Claude waiting longer between iterations once the PR goes quiet: When you ask for a dynamic  schedule, Claude may use the Monitor tool directly. Monitor runs a background script and streams each output line back, which avoids polling altogether and is often more token-efficient and responsive than re-running a prompt on an interval. A dynamically scheduled loop appears in your scheduled task list like any other task, so you can list or cancel it the same way. The jitter rules don’t apply to it, but the seven-day expiry does: the loop ends automatically seven days after you start it. On Amazon Bedrock, Claude Platform on AWS, Google Cloud’s Agent Platform, and Microsoft Foundry, a prompt with no interval runs on a fixed 10-minute schedule instead. ​ Run the built-in maintenance prompt When you omit the prompt, Claude uses a built-in maintenance prompt instead of one you supply. On each iteration it works through the following, in order: continue any unfinished work from the conversation tend to the current branch’s pull request: review comments, failed CI runs, merge conflicts run cleanup passes such as bug hunts or simplification when nothing else is pending Claude does not start new initiatives outside that scope, and irreversible actions such as pushing or deleting only proceed when they continue something the transcript already authorized. A bare  runs this prompt at a dynamically chosen interval . Add an interval, for example  , to run it on a fixed schedule instead. To replace the built-in prompt with your own default, see Customize the default prompt with loop.md . On Amazon Bedrock, Claude Platform on AWS, Google Cloud’s Agent Platform, and Microsoft Foundry,  with no prompt prints the usage message instead of running the maintenance prompt. ​ Customize the default prompt with loop.md A  file replaces the built-in maintenance prompt with your own instructions. It defines a single default prompt for bare  , not a list of separate scheduled tasks, and is ignored whenever you supply a prompt on the command line. To schedule additional prompts alongside it, use  or ask Claude directly . Claude looks for the file in two locations and uses the first one it

## Code / Examples

```
/goal
```
```
--resume
```
```
--continue
```
```
/loop
```
```
--resume
```
```
/schedule
```
```
/loop
```
```
/loop
```


---
*Source: [code.claude.com](https://code.claude.com/docs/en/scheduled-tasks)*
