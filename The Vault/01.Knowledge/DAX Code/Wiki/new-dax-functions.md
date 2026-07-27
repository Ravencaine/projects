---
created: 2026-07-26
source: dax.pdf
note_type: concept
tags: [dax, new-functions, recent-additions, preview]
---

# New DAX Functions

DAX is continuously updated with new functions. New functions are documented here as they are added to the reference.

## Recent Additions

### Window Functions (GA)
- INDEX: Returns a row at a specific position within a partition
- OFFSET: Returns a row at a specified offset from the current row
- WINDOW: Returns a range of rows relative to the current row
- RANK: Ranks values within a partition
- ROWNUMBER: Assigns sequential numbers to rows

These work with ORDERBY, PARTITIONBY, and MATCHBY.

### DAX User-Defined Functions (Preview)
DAX UDFs allow you to package DAX logic into reusable named functions. See: [[dax-user-defined-functions-udf]]

### Visual Calculations (Preview)
Visual calculations allow DAX formulas to be written directly in a report visual, without a model-level measure.

### Copilot Integration (2024)
DAX query support in Power BI Copilot allows natural language to DAX query generation.

## Checking for New Functions

When a function is new, the documentation page notes "Article - [date]" and may indicate preview status.

Preview functions:
- May change before general availability
- May require enabling in Power BI Desktop options
- May not be supported in all environments

## Related

- [[window]]
- [[offset]]
- [[dax-user-defined-functions-udf]]
