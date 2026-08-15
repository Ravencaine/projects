---
created: 2026-08-10
updated: 2026-08-10
source: 10 Power Automate Flows That Actually Save Hours — Not Just Demos
source_url: https://medium.com/@kaklotarrahul79/10-power-automate-flows-that-actually-save-hours-not-just-demos-78646527c0f3
note_type: pattern
tags: [power-automate, sharepoint, approval, document-management, automation]
---

# Multi-Level Document Approval Engine

Route documents submitted to SharePoint through a structured approval process — approved files are moved to an "Approved" folder; rejected files are returned with comments.

## Purpose

Replaces approval email chains that get lost, delayed, or forgotten. The flow enforces a structured approval path so managers always respond and submitters always get feedback.

## Components

1. **Trigger:** When an item or file is created in a SharePoint document library (e.g., `/Approvals/`)
2. **Action:** Start and wait for an approval (Approvals App / Approvals connector)
3. **Condition:** Approval outcome
   - **Approved:** Move file to "Approved" folder → update SharePoint column status → notify submitter
   - **Rejected:** Request rejection comments → send back to submitter with feedback

## Structure

```
Trigger:   When a file is created in SharePoint (e.g., /Approvals/)
     ↓
Action:   Start and wait for an approval
          - Assigned to: approver(s)
          - Title: file name
          - Link: file URL
     ↓
Condition: Outputs of 'Start and wait for an approval'
     ├─ Approved
     │    → Move file to /Approved/ folder
     │    → Update column: Status = "Approved"
     │    → Send email to submitter: approved
     │
     └─ Rejected / Cancelled
          → Send email to submitter with comments
          → Optionally move to /Rejected/ folder
```

## Hours Saved

~2 hours/week lost in email ping-pong on approvals.

## Related

- [[Email-Attachment-Archiver-to-SharePoint]]
- [[PDF-Form-Processing-to-SharePoint-Excel]]
