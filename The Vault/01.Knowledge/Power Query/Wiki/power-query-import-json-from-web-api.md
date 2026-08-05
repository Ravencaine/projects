---
created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
note_type: pattern
tags: [power-query, json, web-api, import, api]
---

# Power Query: Import JSON from Web API — Multi-Level Expand

Power Query can pull data from any JSON REST API, handling nested and repeating JSON structures through a sequence of expand operations.

## Purpose

Modern web APIs return data as JSON with nested objects and arrays. Power Query's expand mechanism lets you navigate multi-level JSON into flat tabular rows.

## Components

- Power Query → From Web (URL input)
- Query Editor → Convert to Table → expand button (⫋)
- Multiple expand levels for nested JSON arrays

## Structure

```
1. Power Query → From Web → enter URL → OK
2. Query Editor opens showing the JSON as a record/list structure
3. Click "Into Table" (first ribbon icon) to convert to a table
4. Click the expand button (⫋) on the column header → select fields to expand
5. Click expand again on the new column → nested arrays appear
6. Repeat expand steps until data is fully flattened
7. Rename columns → Close & Load
```

## Step-by-Step Example (Nobel Prize laureate.json)

URL: `http://api.nobelprize.org/v1/laureate.json`

1. `From Web` → enter URL → OK
2. Click **Into Table** (ribbon icon) → one row with a column called "Value"
3. Click expand (⫋) on Value → shows "laureates" (top-level array) → click OK → expands to multiple rows (one per laureate)
4. Scroll right → find another expand button → click → shows the per-laureate fields (id, firstname, surname, etc.) → accept all → one laureate per row
5. Scroll right → find another expand button (inside the prize sub-array) → click → expands to one row per prize per person → multiple prize winners get multiple rows
6. Scroll right → expand again → shows the "motivation" field
7. **Group By:** Category + Year → Count Rows → prizes per category per year
8. **Rename:** attribute column → "year", value column → "unemployment" (or whichever metric)
9. **Type conversion:** right-click year column → Change Type → Date; right-click value column → Change Type → Decimal Number

## Notes

- If the JSON is a top-level array, Into Table converts it directly. If it's a top-level object with an array inside a key, first expand the key then Into Table.
- "Skip nested files" errors in the Query Editor can be resolved by clicking the expand button on the specific nested field
- The Applied Steps pane (right side) shows every transformation — click the gear icon to edit any step

## Related

- [[power-query-group-by-single-dual-triple-field]] — Group By applied after JSON expansion
- [[sql-plus-plus-and-n1ql]] — N1QL's similar hierarchical JSON querying concept
- [[power-query-import-multiple-csv-files-from-folder]] — alternative structured data import
