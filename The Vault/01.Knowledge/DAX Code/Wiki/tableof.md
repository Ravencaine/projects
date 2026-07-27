---
created: 2026-07-26
source: dax.pdf
note_type: function
tags: [dax, function, dax]
---

# TABLEOF

Summarize this article for me Applies to: Calculated column Calculated table Measure Visual calculation Returns a reference to the table associated with a specified column, measure, or calendar.

## Remarks

The TABLEOF function returns a table reference, not the table data itself. When passed a column name, it returns the table that contains that column. When passed a measure name, it returns the table where that measure is defined. When passed a calendar reference, it returns the table associated with that calendar. This function is useful in scenarios where you need to dynamically determine which table a column or measure belongs to. TABLEOF does not resolve columns from row context; it only resolves columns from the current filter context (base table). This function is not supported for use in