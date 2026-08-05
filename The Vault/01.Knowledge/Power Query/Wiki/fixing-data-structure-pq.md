---
created: 2026-07-28
updated: 2026-08-02
source: Artificial Intelligence with Power BI (Diepeveen)
note_type: pattern
tags: [data-structure, power-query, headers, delimiters, json, expand]
---

# Fixing Data Structure in Power Query

Common structural problems when importing data into Power BI: wrong headers, wrong delimiter, nested JSON documents.

## Purpose

Raw imported data often has structural issues that must be resolved before analysis.

## Components

| Problem | Fix | Power Query step |
|---------|-----|-----------------|
| Headers on data row | Promote first row to headers | Use First Row as Headers |
| Wrong delimiter | Re-detect delimiter | Detect Delimiter button |
| JSON nested docs | Expand record/list columns | Click expand icon on column header |
| Duplicate column names | Rename after expand | Rename Column |
| Key-value pairs in JSON | Extract to columns | Expand or Transform |

## Steps

### Fixing CSV Headers

1. Get Data → CSV
2. If headers appear as data rows:
   - Home → Use First Row as Headers
3. Check column names and data types

### Fixing JSON Documents

1. Get Data → JSON → navigate to file
2. In Power Query Editor, find the column with record/list values
3. Click the expand icon (two arrows) in the column header
4. Select which fields to extract
5. Handle missing keys: Power Query returns null for absent keys

## Notes

- Semi-structured data from Azure Cosmos DB may have varying keys per document
- Use Column Quality after expanding to check for nulls introduced by missing keys
- Rename expanded columns to human-readable names immediately

## Related

- [[power-query-expand-versus-extract]]
- [[power-query-unpivot-columns]]
- [[structured-versus-semi-structured-data]]
