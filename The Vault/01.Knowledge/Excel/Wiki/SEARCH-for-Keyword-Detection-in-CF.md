---
created: 2026-08-09
updated: 2026-08-09
source: "Advanced Conditional Formatting in Excel Using Formulas • My Online Training Hub"
note_type: atomic
tags: [excel, conditional-formatting, search, find, keyword, error-as-false, case-insensitive]
---

# SEARCH for Keyword Detection in CF

`=SEARCH("urgent",$H5)` detects keywords in a text column by exploiting SEARCH's return type: number on success, error on failure. Conditional formatting treats numbers as TRUE and errors as FALSE.

## Formula

```
=SEARCH("urgent",$H5)
```

## How It Works

| SEARCH result | CF evaluation |
|---------------|---------------|
| Number (position found) | TRUE → format applies |
| Error (not found) | FALSE → no format |

## Key Properties

- **Case-insensitive:** SEARCH("urgent",...) matches "Urgent", "URGENT", "urgent"
- **No need for ISNUMBER wrapper:** CF evaluates numeric result directly as TRUE; error becomes FALSE
- **Error as FALSE is the key mechanism:** unlike regular formulas where ISERROR catches errors, CF's TRUE/FALSE coercion handles this automatically

## Multiple Keywords

Create one rule per keyword:

```
=SEARCH("urgent",$H5)     → urgent → format A
=SEARCH("burned out",$H5) → burnout → format B
```

## Related

- [[Source-Advanced-Conditional-Formatting-Formulas-Mynda-Treacy]] — source
