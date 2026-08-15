---
created: 2026-08-06
updated: 2026-08-06
source: Claude Power BI MCP Integration
note_type: reference
tags: [mcp, claude, power-bi, ai, prompts, automation]
---

# 7 AI Prompts for Power BI MCP

Quick reference for the seven Claude prompts that automate Power BI model-building tasks via the Claude Power BI MCP integration.

## Quick Reference

### Prompt 1 — Create a Calculations Table and Build Measures

```
"Create a calculations table with Net Sales and YTD, MoM, and Previous Month measures"
```

Claude creates:
- A dedicated calculation table
- Net Sales DAX measure
- Time intelligence measures: YTD, Month-over-Month, Previous Month

---

### Prompt 2 — Rename Fields for Consistency

```
"Analyze all field names across tables and rename them for consistency in casing, prefixes, and patterns. Update all DAX measures with the new table references."
```

Claude:
- Scans all table names, column names, and measure names
- Identifies naming inconsistencies
- Applies consistent casing, prefixes, and patterns
- Updates all DAX measure references automatically

---

### Prompt 3 — Add Display Folders

```
"Add display folders to organize fields by category"
```

Claude:
- Groups measures into logical display folders
- Creates nested folder structures for clean model navigation
- Structures the model for easier analyst use

---

### Prompt 4 — Hide Foreign Keys

```
"Hide all ID columns that are not used by report consumers"
```

Claude hides unused foreign key columns, decluttering the field list.

---

### Prompt 5 — Add Descriptions and Synonyms

```
"Add descriptions to all measures, columns, and tables, and add synonyms for Q&A support"
```

Claude generates:
- Clear metadata for every field
- Synonyms for natural language Q&A accuracy
- Plain-English DAX explanations

---

### Prompt 6 — Create Hierarchies

```
"Create hierarchies for drill-down navigation"
```

Claude builds hierarchies such as:
- `Product Category → Subcategory → Item`
- `Year → Quarter → Month → Day`
- `Region → Store`

Also provides usage documentation.

---

### Prompt 7 — Optimize Data Types

```
"Analyze all column data types and optimize them for compression and performance"
```

Claude reviews every column and adjusts data types for best compression.

> Demo results: **up to 15% model size reduction** and **up to 3x query speed improvement**.

---

### Bonus — Auto-Generate a Data Dictionary

```
"Create a complete data dictionary with executive summary, Mermaid model diagram, table definitions, and DAX explanations"
```

Output:
- Executive summary
- Mermaid ER diagram of the model
- Table and column definitions
- DAX logic in plain English

Exportable as markdown, PDF, or searchable document.

## Notes

- All seven prompts are demonstrated live in the Data Bear demo video
- Prompt 2 (rename) updates DAX measure references automatically — no broken links
- Prompt 7 (data type optimisation) requires verification — Claude may suggest changes that affect downstream calculations

## Related

- [[Claude-Power-BI-MCP-Integration]] — concept overview
- [[Connect-Claude-to-Power-BI-via-MCP]] — setup workflow
- [[mcp-power-bi-modeling-preview-caveats]] — governance and trust requirements
- [[Organizing-Measures-Display-Folders]] — the display folder pattern Prompt 3 automates
