---
created: 2026-07-26
source: dax.pdf
note_type: function
tags: [dax, function, dax]
---

# JSON

Converts a JSON string into a table. Used in DAX queries to deserialize JSON-formatted data as a DAX table expression.

## Syntax

```dax
JSON(<json_string>)
```

## Parameters

| Term | Definition |
|------|------------|
| `json_string` | A string containing valid JSON data in rowset format, typically produced by DAX query functions or exported from model data. |

## Return Value

A table with columns and rows matching the JSON structure.

## Remarks

Primarily used in DAX query language (EVALUATE, SUMMARIZECOLUMNS) to work with JSON data. Supported in Power BI, Analysis Services, and Azure Analysis Services.