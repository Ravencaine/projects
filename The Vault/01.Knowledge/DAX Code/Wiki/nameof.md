---
created: 2026-07-26
updated: 2026-08-02
source: dax.pdf
note_type: function
tags: [dax, function, information]
---

# NAMEOF

Summarize this article for me Applies to: Calculated column Calculated table Measure Visual calculation Returns the name of a table, column, measure, or calendar as a text string.

## Remarks

For tables, returns the name in the format 'TableName'. For columns, returns the name in the format 'TableName'[ColumnName]. For measures, returns the name in the format 'TableName'[MeasureName]. For calendars, returns the name in the format 'CalendarName'. For variation columns, returns the name in the format 'TableName'[ColumnName]. [VariationName]. Variables and dynamic expressions are not supported as arguments to NAMEOF. This function is not supported for use in DirectQuery mode when used in calculated columns or row-level security (RLS) rules.