---
created: 2026-08-08
updated: 2026-08-08
source: AI Changing Power BI Workflow
note_type: atomic
tags: [power-bi, pbir, json, report-format, ai, workflow]
---

# PBIR (Power BI Report Format) + JSON

PBIR (Power BI enhanced report format) stores the complete report definition as structured JSON files, making reports readable and editable by AI agents and code.

## Definition

When saving a Power BI report as a PBIR file, the report definition is split into multiple JSON files inside a `definition/` folder. Each visual, page, filter, and theme is represented as a JSON object with a schema at the top. This structure enables AI agents to parse the schema, understand the visual structure, and make targeted edits programmatically.

## Key Points

- PBIR is now the **default** save format in Power BI Desktop
- Files stored in `definition/` subfolder — one JSON file per visual/page/filter/theme
- Each JSON object starts with a **schema declaration:** the AI agent can reference this to understand the exact structure
- AI agents read the schema, understand the current visual configuration, and generate edits
- Changes are written directly to the JSON files — Power BI Desktop reloads them in real time
- Compatible with VS Code and any text/code editor

## Examples

**VS Code view of a PBIR report:**
```
MyReport.pbir/
  definition/
    pages/
      page-1.json
      page-2.json
    visuals/
      visual-abc123.json
      visual-def456.json
    themes/
      theme.json
```

**Visual JSON schema (abbreviated):**
```json
{
  "$schema": "https://powerbi.com/product/schema#visual",
  "visual": {
    "name": "clusteredBarChart1",
    "type": "clusteredBarChart",
    "filters": [],
    "display": {}
  }
}
```

## Related

- [[Power-BI-AI-Agent-CLI-Reload]] — CLI for reloading PBIR JSON edits into Power BI Desktop
- [[AI-Written-PowerShell-Scripts-Design-Automation]] — PowerShell scripts that edit PBIR JSON files
