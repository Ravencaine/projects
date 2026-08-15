---
created: 2026-08-10
updated: 2026-08-10
source: 10 Power Automate Flows That Actually Save Hours — Not Just Demos
source_url: https://medium.com/@kaklotarrahul79/10-power-automate-flows-that-actually-save-hours-not-just-demos-78646527c0f3
note_type: pattern
tags: [power-automate, recurrence, adaptive-card, sharepoint, teams, reporting]
---

# Weekly Status Report Aggregator

Automatically collect weekly status updates from team members via an Adaptive Card form and compile them into a SharePoint List or draft an executive summary email.

## Purpose

Replaces the weekly ritual of chasing 10 team members for updates on Thursday afternoon and manually assembling them into a master document.

## Components

1. **Trigger:** Recurrence — every Thursday at 3:00 PM
2. **Action:** Send a Microsoft Form or Teams Chat with an Adaptive Card containing 3 brief questions (e.g., What did you complete? What are you working on? Any blockers?)
3. **Action:** Collect responses into a SharePoint List (one row per team member) OR automatically draft an executive summary email using the responses

## Structure

```
Trigger:   Recurrence — Weekly (Thursday 3:00 PM)
     ↓
Action:   Post adaptive card to Teams channel
          OR  Send a Microsoft Form link
          Questions: Completed / In Progress / Blockers
     ↓
Action:   Get response details
          (iterate over each response if multiple recipients)
     ↓
Action:   Create item in SharePoint List
          OR  Send email with compiled summary
```

## Hours Saved

~3 hours/week spent nagging colleagues and compiling reports.

## Related

- [[Multi-Level-Document-Approval-Engine]]
- [[Calendar-Deep-Work-Time-Blocker]]
