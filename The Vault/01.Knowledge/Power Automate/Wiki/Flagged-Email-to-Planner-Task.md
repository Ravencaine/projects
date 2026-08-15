---
created: 2026-08-10
updated: 2026-08-10
source: 10 Power Automate Flows That Actually Save Hours — Not Just Demos
source_url: https://medium.com/@kaklotarrahul79/10-power-automate-flows-that-actually-save-hours-not-just-demos-78646527c0f3
note_type: pattern
tags: [power-automate, email, planner, microsoft-to-do, task-management, automation]
---

# Flagged Email to Planner Task

Convert a flagged Outlook email into a Microsoft Planner or To-Do task, with the email subject as the task title and body as the description. Unflags the email to keep the inbox clean.

## Purpose

Actionable emails often represent work that needs to be tracked separately. Instead of leaving emails flagged (creating inbox clutter) or copying information manually into task tools, the flow bridges the two.

## Components

1. **Trigger:** When an email is flagged (Outlook V2 — "When an email is flagged")
2. **Action:** Create a task in Microsoft Planner (or Microsoft To-Do)
   - Task title: email subject line
   - Description: email body content
   - Assigned to: (flow creator or specified user)
   - Due date: (optional — extract from email if present)
3. **Action:** Unflag the email so the inbox stays clean

## Structure

```
Trigger:   When an email is flagged (Outlook V2)
     ↓
Action:   Create a task (Planner)
          - Plan ID: <your plan>
          - Title: @{triggerOutputs()?['body/subject']}
          - Notes: @{triggerOutputs()?['body/body']}
          - Bucket: "Inbox" or similar
     ↓
Action:   Mark as complete (Outlook V2)
          OR  Remove flag from email
```

## Variations

- **With due date extraction:** Use a **Text/Compose** step with a regex or `match()` expression to extract a date from the email body and set it as the task due date
- **With priority:** Map email importance flag to Planner priority (1–10)
- **To-Do instead of Planner:** Use the "Create a To-Do" action (part of the Tasks connector) for personal task management

## Hours Saved

~2 hours/week in task management overhead.

## Related

- [[Calendar-Deep-Work-Time-Blocker]]
- [[VIP-Email-to-Teams-Alert-Flow]]
