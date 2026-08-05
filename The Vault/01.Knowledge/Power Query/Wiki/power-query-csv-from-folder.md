---


title: "Power Query CSV from Folder"
created: 2026-07-28
updated: 2026-08-02
tags: [power-query, pattern, reference]
note_type: reference
description: "Loading multiple CSV files from a folder as a single table in Power Query — NYSE stock price example. From Dunlop."


source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"

---

# Power Query: Import CSV Files from a Folder

Loads all CSV files in a folder into a single query, enabling analysis across many files at once.

## Workflow

```
Power Query → From File → From Folder → Browse to folder
```

Power Query returns a list of all files in the folder, showing columns:
- `Attribute` (filename)
- `Content` (binary)

## Opening Individual Files

Click **Binary** in the `Content` column to open a specific file in the Query Editor.

## Key Point

The Query Editor loads a **subset** of the total records — enough to show the structure. Use Close & Load to import all rows.

## Use Case

Hadoop log data stored as CSV files — load into Power Query → PowerPivot → Pivot Tables without needing Hortonworks or HDFS access.

## Source Reference

Chapter 8, NYSE stock price CSV example, *Beginning Big Data with Power BI and Excel 2013* (Dunlop, Apress 2015).
