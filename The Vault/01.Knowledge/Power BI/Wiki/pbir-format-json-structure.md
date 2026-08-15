---
created: 2026-08-11
updated: 2026-08-11
source: "AI-Power-BI-Workflow-Transcript.md"
note_type: atomic
tags: [power-bi, pbir, json]
---

# PBIR Format — JSON-Based Report Structure

Power BI Enhanced Report format (.pbir) exposes the entire report definition as human-readable JSON files, enabling AI agents and code-based editing.

## Definition

When you save a Power BI report as .pbir instead of .pbix, the single-file archive is replaced by a folder containing separate JSON files — one per report object: pages, visuals, themes, filters, queries.

## Structure

```
MyReport.pbir/
  definition/
    report.json        # top-level report metadata
    page-1.json        # one file per page
    visual-1.json      # one file per visual
    filters.json
    queryBindings.json
    ...
  metadata/
    ...               # connection strings, model info
```

## Key Points

- The schema at the top of each JSON object is machine-readable — AI agents use it to understand visual structure
- Any text editor (VS Code) can edit the report; no Power BI Desktop required for modifications
- `powerbi desktop reload` picks up disk changes and refreshes the open report
- PBIR is now the default format in Power BI Desktop

## Related

- [[pbir-hot-reload-workflow]] — hot-reload after editing JSON
- [[powershell-design-automation-pbir]] — PowerShell scripts that automate formatting
