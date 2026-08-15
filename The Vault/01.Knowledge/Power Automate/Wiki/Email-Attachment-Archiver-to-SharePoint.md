---
created: 2026-08-10
updated: 2026-08-10
source: 10 Power Automate Flows That Actually Save Hours — Not Just Demos
source_url: https://medium.com/@kaklotarrahul79/10-power-automate-flows-that-actually-save-hours-not-just-demos-78646527c0f3
note_type: pattern
tags: [power-automate, email, sharepoint, attachment, file-management, automation]
---

# Email Attachment Archiver to SharePoint

Automatically save email attachments to a structured SharePoint folder hierarchy (e.g., `/invoices/2026/VendorName/`) while filtering out signature images.

## Purpose

Replaces manually saving email attachments to local folders or forgetting they existed. All attachments are automatically filed and searchable in SharePoint.

## Components

1. **Trigger:** When a new email with attachments arrives (Outlook V2)
2. **Filter:** Exclude small files (< 10KB) — these are usually signature images (`.png`, `.jpg`)
3. **Action:** Create file in a SharePoint folder structured by date and/or sender
   - Example path: `/invoices/2026/VendorName/`
   - Date from email: `/2026/07/` folder structure
4. **Action:** Optionally notify the user or add a row to a tracking log

## Structure

```
Trigger:   When a new email arrives (with attachments)
     ↓
Condition: Attachment size > 10KB
     ↓ (yes — filter out signature images)
Action:   Create file in SharePoint
          Site: https://contoso.sharepoint.com/sites/Finance
          Folder: /attachments/2026/07/
          File name: @{triggerOutputs()?['body/from']}/@{triggerOutputs()?['body/subject']}
     ↓
Action:   Send confirmation email (optional)
```

## Key Filter

Always filter out files < 10KB to avoid saving Outlook signature images. Check `size` property of each attachment in the trigger output.

## Hours Saved

~1.5 hours/week searching for lost attachments.

## Related

- [[PDF-Form-Processing-to-SharePoint-Excel]]
- [[Multi-Level-Document-Approval-Engine]]
- [[Stale-File-Cleanup-Bot]]
