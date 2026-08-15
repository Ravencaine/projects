---
created: 2026-08-10
updated: 2026-08-10
source: 10 Power Automate Flows That Actually Save Hours — Not Just Demos
source_url: https://medium.com/@kaklotarrahul79/10-power-automate-flows-that-actually-save-hours-not-just-demos-78646527c0f3
note_type: pattern
tags: [power-automate, sharepoint, azure-blob, archival, compliance, recurrence, automation]
---

# Stale File Cleanup Bot

Monthly recurrence flow that checks SharePoint document libraries for files not modified in over 365 days and either moves them to cold storage or sends a "do you still need this?" email to the owner.

## Purpose

Cloud storage becomes a digital landfill of outdated drafts, temporary files, and abandoned project folders. This flow enforces storage hygiene proactively rather than reactively during compliance audits.

## Components

1. **Trigger:** Recurrence — Monthly (e.g., first day of month at 9:00 AM)
2. **Action:** Get file metadata from specified SharePoint document libraries (list all files in target libraries)
3. **Condition:** For each file, check if `Last Modified Date` is older than 365 days
4. **Actions (conditional):**
   - **Cold archive:** Move file to Azure Blob Storage (Cool or Cold tier) — cost-effective long-term storage
   - **Owner notification:** Send an email to the file owner asking if the file is still needed. If no response in 14 days, move to archive.

## Structure

```
Trigger:   Recurrence — Monthly (1st of month, 9 AM)
     ↓
Action:   List files (Get files (properties only))
          Site: <your SharePoint site>
          Library: <document library name>
     ↓
Apply to each file:
     ↓
Condition: DateDiff(utcNow(), file/modified) > 365 days
     ↓ (yes)
Action (Option A): Move file to Azure Blob Archive tier
         OR
Action (Option B): Send email to file author
          Subject: "Do you still need this file?"
          Body: "File [name] was last modified [date]. Click to keep or delete."
     ↓
Apply to each (for Option B response):
     ↓
If no response in 14 days → Move file to archive
```

## Key Parameters

| Parameter | Value |
|-----------|-------|
| Last Modified threshold | 365 days |
| Archive tier | Azure Blob Cool or Cold |
| Owner email wait | 14 days |

## Hours Saved

~2 hours/month in manual storage maintenance and compliance prep.

## Related

- [[Email-Attachment-Archiver-to-SharePoint]]
- [[Failed-Flow-Monitoring-Alerting]]
