---
created: 2026-08-09
updated: 2026-08-09
source: "Error Handling in Power BI A Guide to Power Query and DAX.md"
source_url: https://databear.com/handling-errors-in-power-bi/
note_type: source
tags: [power-bi, power-query, dax, error-handling, try, otherwise, iferror, databear, boniface-muchendu]
---

# Error Handling in Power BI: A Guide to Power Query and DAX (Data Bear)

> **Type:** article
> **Author:** Boniface Muchendu
> **Published:** 2023-07-16
> **URL:** https://databear.com/handling-errors-in-power-bi/
> **Routed to:** Power BI

## Summary

Error handling prevents a single error from breaking a report (failed refresh, blank calculations). Power Query: `try ... otherwise` — returns alternative value on error; without `otherwise` returns a record with error details per row. DAX: `IFERROR` wraps an expression with an alternative return value; use `CONVERT` to type-cast columns before arithmetic to avoid type-mismatch errors.

## Key Claims

### Power Query — Try and Otherwise
- `try [expression] otherwise <fallback>` — returns fallback on error
- Without `otherwise`: returns a record (table-like structure per row) with error details — useful for troubleshooting multiple error types
- Example: `try [Unit Price] * [Quantity] otherwise null` — catches type-mismatch when Quantity contains text
- `otherwise` value can be null, zero, or any custom value

### DAX — IFERROR
- `IFERROR(<expression>, <fallback>)` — two parameters: expression + fallback
- Example: `IFERROR(CONVERT([Quantity], INTEGER), 0)` — converts text to integer before arithmetic, returns 0 on error
- Full sales formula: `[Unit Price] * IFERROR(CONVERT([Quantity], INTEGER), 0)`
- Prevents blank values in calculated columns when data contains invalid entries

### General
- Single error in one line can cause dashboard refresh failures or blank calculations
- DIVIDE has a built-in third parameter for the error fallback value
- Error handling = catch and fix without breaking the report

## Metadata

| Field | Value |
|-------|-------|
| Source file | Error Handling in Power BI: A Guide to Power Query and DAX.md |
| Archived at | 99.System/InboxArchive/2026-08/ |
| Ingestion date | 2026-08-09 |
