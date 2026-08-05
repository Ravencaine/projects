---
created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
note_type: pattern
tags: [power-query, group-by, aggregate, transform]
---

# Power Query Group By: Single, Dual, and Triple Field Aggregation

Group By in Power Query aggregates data by one or more grouping columns, computing sum, count, average, etc. for each unique combination.

## Purpose

Group By is Power Query's equivalent of SQL's `GROUP BY` clause — it reduces a large table to summary rows by category.

## Components

- Grouping column(s): fields to group by
- Aggregation column: the numeric field to aggregate
- Aggregation operation: Count Rows, Sum, Average, Minimum, Maximum, Count Distinct Rows

## Structure

```
Power Query ribbon → Transform → Group By
```

### Single Field Group By

1. Select the grouping column in the table
2. Click Group By → choose the column as the Group By field
3. Operation: Count Rows (or Sum, Average, etc.)
4. Result: one row per unique value of the grouping column

### Dual Field Group By

1. Click the + button in the Group By dialog to add a second grouping field
2. Both fields must match for two rows to be in the same group
3. Result: one row per unique combination of Field1 + Field2

### Triple Field Group By (Adding a Detail Column)

1. Click + again to add a third grouping field
2. Optionally: add a "Count rows" aggregation
3. Optionally: click + to add a detail column — a non-grouping column to include in output (e.g., surname from a people table)

## Example

Nobel Prize JSON data (Ch8):
1. Import JSON from api.nobelprize.org/v1/laureate.json
2. Expand the nested data structure to one laureate per row
3. Group By: Category (1 field) → Count Rows → count of prizes per category
4. Group By: Category + Year (2 fields) → Count Rows → count of prizes per category per year
5. Group By: Category + Year + Surname (3 fields) → Count Rows → list of winners by category and year

## Notes

- Group By in the Query Editor ribbon (Transform tab) is applied to the currently selected column
- The gear icon next to "Group Rows" in the Applied Steps pane lets you edit the Group By settings after the fact
- Use Count Rows to count records without specifying a numeric column

## Related

- [[sql-aggregate-functions]] — SQL equivalent (COUNT, SUM, etc.)
- [[power-query-import-json-from-web-api]] — the data source for the Nobel Prize example
- [[sql-select-syntax-reference]] — GROUP BY clause in SQL queries
