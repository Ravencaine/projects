---
created: 2026-08-09
updated: 2026-08-09
source: "Build an Automated Excel Database • My Online Training Hub"
note_type: atomic
tags: [excel, xmatch, duplicate-detection, validation, form, iserror, existing-data, match]
---

# XMATCH for Form-Level Duplicate Detection

`=ISNUMBER(XMATCH(D5, ClientData[Full Name], 0))` checks if a value entered in a form field already exists in the database table. If XMATCH finds a match it returns a position (number); ISNUMBER converts that to TRUE → display a warning.

## Formula

```
=IF(ISNUMBER(XMATCH(D5, ClientData[Full Name], 0)),
  "⚠️ This customer is already in the database.",
  "")
```

## How It Works

| Step | Expression | Result |
|------|-----------|--------|
| 1 | `XMATCH(D5, ClientData[Full Name], 0)` | Position number (found) or error (not found) |
| 2 | `ISNUMBER(...)` | TRUE (found) or FALSE (not found) |
| 3 | `IF(TRUE, warning, "")` | Shows warning if customer exists |

## XMATCH vs MATCH

| | XMATCH | MATCH |
|--|--------|-------|
| Default match mode | Exact | Exact |
| Match type arg | 0 = exact | 0 = exact |
| No match result | Error | Error |
| Available | Excel 365 | All versions |
| Direction | Searches from top by default | Searches from top by default |

XMATCH is used here for its Excel 365 availability and cleaner exact-match semantics.

## Key Point

Validation happens at the **form level** before the record is saved — the user sees the warning before the duplicate enters the database.

## Related

- [[Source-Automated-Excel-Database-Mynda-Treacy]] — source
- [[COUNTIF-Expanding-Range-for-Duplicates]] — CF-level duplicate detection; XMATCH handles form-level pre-entry validation
- [[Office-Scripts-Form-Database-Automation]] — the automation step that saves data after the form passes validation
