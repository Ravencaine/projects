---
created: 2026-08-13
source: "Top 10 Data Cleaning Tasks in Power BI (Power Query Editor)"
source_url: https://medium.com/write-your-world/top-10-data-cleaning-tasks-in-power-bi-power-query-editor-65c3e34c8563
note_type: reference
tags: [power-query, data-cleaning, power-bi]
---

# Top 10 Power Query Data Cleaning Tasks

Quick-reference cheatsheet for the 10 most common data cleaning operations in Power Query Editor.

## Quick Reference

| # | Task | Menu Path | Use Case |
|---|------|----------|----------|
| 1 | Remove Duplicates | Home → Remove Rows → Remove Duplicates | Delete duplicate rows based on one or more columns |
| 2 | Replace Values | Transform → Replace Values | Fix spelling errors; replace "N/A" with null |
| 3 | Trim and Clean Text | Transform → Format → Trim / Clean | Trim removes extra spaces; Clean removes non-printable characters |
| 4 | Fill Down / Up | Transform → Fill → Down / Up | Fill missing values using the row above or below |
| 5 | Remove Empty / Error Rows | Home → Remove Rows → Remove Blank Rows / Remove Errors | Delete rows that are null or contain errors |
| 6 | Change Data Types | Transform → Data Type | Convert columns to text, number, date; critical for correct visuals |
| 7 | Split Column by Delimiter | Transform → Split Column → By Delimiter | Separate embedded data (e.g. "FirstName LastName") |
| 8 | Unpivot Columns | Transform → Unpivot Columns | Convert wide data to tall format for time-series or repeated metrics |
| 9 | Merge Queries (Joins) | Home → Merge Queries | Combine data from different sources based on key columns |
| 10 | Group By | Transform → Group By | Summarize data (e.g. total sales per region) |

## Notes

- **Fill Down / Up**: Direction matters — Down uses the value above to fill blanks; Up uses the value below. Common in Excel-style tables where nulls represent carry-forward values.
- **Change Data Types**: Assigning the wrong data type is a silent visual killer — numbers stored as text produce incorrect charts, dates stored as text are not recognized as dates.
- **Unpivot**: Essential for converting attributes-as-columns layouts into a clean normalised tall format suitable for Power BI visuals.

## Related

<!-- links -->
