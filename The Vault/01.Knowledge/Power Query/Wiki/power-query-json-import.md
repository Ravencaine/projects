---


title: "Power Query JSON Import (Nobel Prize)"
created: 2026-07-28
updated: 2026-08-02
tags: [power-query, pattern, reference]
note_type: reference
description: "Step-by-step import of nested JSON from a URL into Power Query — expanding records, arrays, and the prize motivation field. From Dunlop."


source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"

---

# Power Query: Import JSON from URL

Imports nested JSON data from a web URL, expanding arrays and records into tabular format.

## Step-by-Step: Nobel Prize JSON

### 1. Import
```
Power Query → From Web → enter URL
http://api.nobelprize.org/v1/laureate.json
```

### 2. Convert to Table
```
Click "Into Table" icon (upper-left ribbon)
```

### 3. Expand Top-Level Record
```
Click expand button (↔) beside the Value column
```

### 4. Expand Inner Arrays
Each subsequent expand generates more rows:
- First expand: one row per laureate
- Second expand: multiple rows for laureates with multiple prizes
- Third expand: additional fields (e.g., motivation)

### 5. Group by Category and Year
```
Select category column → Group By → add year as second field
```

### 6. Count Prizes
```
Aggregation: surname → Count Rows
```

## JSON Expansion Rules

| JSON Structure | Power Query Behavior |
|---------------|---------------------|
| Array of records | One row per record after first expand |
| Nested array | Each element = one new row |
| Repeated nested | Leads to row multiplication |

## Source Reference

Chapter 8, Nobel Prize JSON import, *Beginning Big Data with Power BI and Excel 2013* (Dunlop, Apress 2015).
