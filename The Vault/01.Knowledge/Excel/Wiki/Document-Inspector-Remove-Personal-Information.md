---
created: 2026-08-09
updated: 2026-08-09
source: "Excel File Protection Tricks • My Online Training Hub"
note_type: workflow
tags: [excel, document-inspector, metadata, privacy, personal-information, inspector, remove, author, comments]
---

# Document Inspector: Remove Personal Information

Run Document Inspector before sharing an Excel file to identify and remove hidden personal information and metadata that Excel stores in the workbook — author name, last modified by, company, comment metadata, custom XML, and other hidden file properties.

## When to Use

Before sharing a file externally: to clients, recruiters, suppliers, external partners, or anyone outside your organisation.

## Critical Warning

**Make a backup copy first.** Some Document Inspector changes cannot be undone.

## Step-by-Step

1. File → Info
2. Check for Issues → **Inspect Document**
3. Check **Document Properties and Personal Information** (and other relevant options)
4. Click **Inspect**
5. Review results
6. Click **Remove All** beside each item to remove

## What Document Inspector Removes

| Item | Details |
|------|---------|
| Author name | Set in file properties |
| Last modified by | Windows account name |
| Company | Organisation field |
| Comment metadata | Author names attached to comments |
| Hidden worksheets | Sheets not visible in the UI |
| Custom XML data | Embedded structured data |
| Document properties | Custom and standard properties |
| Other hidden file info | Headers, footers, metadata streams |

## Treat It Like Spell Check

Run Document Inspector as a final check before sending any important file. It only takes a moment and can prevent accidental disclosure of information you did not realise was stored in the workbook.

## Related

- [[Source-Excel-File-Protection-Tricks-Mynda-Treacy]] — source
- [[Encrypt-Workbook-with-Password]] — encryption is the security layer; Document Inspector is the privacy layer
