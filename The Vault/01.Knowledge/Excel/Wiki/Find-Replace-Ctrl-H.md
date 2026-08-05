---
created: 2026-08-05
updated: 2026-08-05
source: 10 Excel Data Cleaning Hacks That Save Hours Every Week (DigitalBYKewat)
note_type: atomic
tags: [excel, find-replace, ctrl+h, null, n-a, placeholder, data-cleaning]
---

# Find & Replace: Ctrl+H

Ctrl+H (Find & Replace) replaces all instances of a string across a selected range or sheet — the fastest way to standardise placeholder values like `NULL`, `N/A`, `-`, and `Unknown` that CRM and ERP systems export as text strings.

## The Standard Workflow

1. Select the range (or entire sheet)
2. Press **Ctrl + H**
3. **Find what:** `NULL` (or `N/A`, `-`, `Unknown`, etc.)
4. **Replace with:** `Pending` (or `0`, or leave blank to delete)
5. Click **Replace All**

## Common Placeholder Values to Replace

| Find what | Replace with | Why |
|-----------|-------------|-----|
| `NULL` | *(blank)* or `0` | NULL as text breaks calculations |
| `N/A` | *(blank)* | N/A as text creates false entries |
| `-` | *(blank)* | Dash often means "no data" |
| `Unknown` | `Unknown` (leave) | Sometimes worth keeping as a category |
| `Aproved` | `Approved` | Typos in dropdown columns |

## What "Replace All" Does

- Replaces every matching cell in the selected range
- Does NOT affect formulas — only values
- Use **Replace** (not Replace All) to preview each replacement first for risky changes

## When NOT to Use

- When `NULL` is a legitimate value (not a placeholder)
- When the column contains numeric data imported as text — use `=VALUE()` or Text to Columns instead of Find & Replace for numeric conversion
- When the placeholder appears in formulas — Find & Replace also searches within formulas if "Within: Workbook" is selected

## Related

- [[TRIM-CLEAN-Functions]] — cleaning spaces before running Find & Replace
- [[Data-Validation-Dropdown]] — prevent future placeholder entries with a dropdown list
