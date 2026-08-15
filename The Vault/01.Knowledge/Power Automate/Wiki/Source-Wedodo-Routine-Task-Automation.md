---
created: 2026-08-10
updated: 2026-08-10
source: Build automatic process on Power Automate to reduce efforts of routine tasks
source_url: https://medium.com/@wedodo/build-automatic-process-on-power-automate-to-reduce-efforts-of-routine-tasks-e31a0306cf3c
note_type: source
tags: [power-automate, sql, excel, vb-script, pivot-table, outlook, automation, routine-tasks]
---

# Source: Wedodo — Routine Task Automation with Power Automate

> **Type:** end-to-end pattern walkthrough
> **Author:** Wedodo (Medium handle)
> **Published:** 2024-09-13
> **URL:** https://medium.com/@wedodo/build-automatic-process-on-power-automate-to-reduce-efforts-of-routine-tasks-e31a0306cf3c
> **Routed to:** Power Automate
> **Category:** Power Automate, SQL, Excel, VBA, Outlook, Automation, End-to-End

## Summary

Builds an end-to-end automated reporting pipeline: SQL query → Excel export → VBA-generated pivot table → datetime-stamped filename → Outlook delivery to stakeholders. Emphasises treating Power Automate steps like object-oriented code: variables defined upfront carry values through each step, and each connector's output (the "blue objects") is the input to the next step.

## Key Claims / Components

1. **Variables first:** Define route paths and datetime format upfront; reference throughout (no hardcoding per step)
2. **SQL connector:** Write query in SSMS, version-control at SQL layer; test before using in flow
3. **Excel connector:** Export SQL result → create headers; "blue connectors" carry data objects between steps
4. **VB Script step:** Invoke VBA to auto-build a pivot table from exported data
5. **Datetime rename:** Append timestamp to filename using variables set at the start
6. **Outlook connector:** Send with subject, body, CC/BCC, attachment; optional draft save
7. **Stakeholder customisation:** Add conditional logic per recipient level before sending
8. **Power Automate action area:** Available components include Excel functions, flow control, Python script, VB script, HTML

## Limitations

- No actual SQL, VBA, or M code shown — descriptive walkthrough only
- No error handling or retry logic documented
- VB Script step requires desktop flow or attended automation (not cloud-only)
- "Python script" component mentioned but not shown

## Value: Power Automate KB

Core contribution: the complete SQL → Excel → VB pivot → datetime rename → Outlook pattern (6-step chain). Also the variable-as-object mental model. No existing notes cover a multi-technology end-to-end flow with VBA pivot table generation.

## Extracted Notes

- [[SQL-to-Report-End-to-End-Automation]] — `pattern` — SQL query → Excel export → VBA pivot → datetime filename → Outlook delivery; treat variables as objects carrying data between steps
- [[Source-Wedodo-Routine-Task-Automation]] — `source` — this note

## Metadata

| Field | Value |
|-------|-------|
| Source file | Build automatic process on Power Automate to reduce efforts of routine tasks.md |
| Archived at | 99.System/InboxArchive/2026-08/ |
| Ingestion date | 2026-08-10 |
| Word count | ~64 |
