---
created: 2026-07-26
updated: 2026-08-02
source: dax.pdf
note_type: source
tags: [dax, reference, microsoft-learn]
---

# Microsoft Learn DAX Reference (dax.pdf)

**Document:** Data Analysis Expressions (DAX) Reference — Microsoft Learn
**Source file:** `C:\Users\krlsa\Documents\00 Projects\The Vault\00.Inbox\dax.pdf`
**Pages:** 1,425
**Ingested:** 2026-07-26
**Extraction method:** PyMuPDF (`fitz`)

## Document Structure

### Conceptual Articles (pages 1–70)
- DAX overview, context, data types, operators, syntax
- Measures vs. Calculated Columns
- Table Relationships in DAX
- Best practices: BLANK handling, FILTER, SELECTEDVALUE, COUNTROWS, variables, error functions, window functions, UDF preview

### Function Reference (pages 71–1414)
439 DAX functions across ~14 categories:

| Category | Functions | Notes |
|----------|----------|-------|
| Date and Time | 24 | DATE, DATEDIFF, DAY, MONTH, YEAR, WEEKDAY, WEEKNUM, FORMAT, etc. |
| Time Intelligence | ~20 | TOTALYTD, SAMEPERIODLASTYEAR, DATEADD, PARALLELPERIOD, CLOSINGBALANCEYEAR, etc. |
| Filter | ~12 | CALCULATE, CALCULATETABLE, FILTER, ALL, ALLEXCEPT, ALLSELECTED, REMOVEFILTERS, KEEPFILTERS, etc. |
| Information | ~15 | SELECTEDVALUE, VALUES, DISTINCT, HASONEVALUE, ISFILTERED, ISCROSSFILTERED, ISINSCOPE, LOOKUPVALUE, CONTAINS, etc. |
| Logical | ~15 | IF, IF.EAGER, SWITCH, COALESCE, AND, OR, NOT, TRUE, FALSE, IFERROR, ISERROR, etc. |
| Mathematical and Trigonometric | ~30 | SUM, SUMX, AVERAGE, AVERAGEX, MIN, MINX, MAX, MAXX, DIVIDE, MOD, ROUND, etc. |
| Statistical | ~35 | COUNT, COUNTA, COUNTROWS, DISTINCTCOUNT, COUNTBLANK, RANKX, etc. |
| Text | ~18 | FORMAT, CONCATENATEX, LEFT, RIGHT, MID, LEN, SUBSTITUTE, TRIM, UPPER, LOWER, etc. |
| Parent and Child | 7 | PATH, PATHITEM, PATHLENGTH, PATHCONTAINS, etc. |
| Table | ~20 | ADDCOLUMNS, SELECTCOLUMNS, SUMMARIZECOLUMNS, UNION, INTERSECT, EXCEPT, GENERATE, TREATAS, GENERATESERIES, DATATABLE, TOPN, etc. |
| Other / Miscellaneous | ~15 | BLANK, ERROR, EVALUATE, EVALUATEANDLOG, NAMEOF, TABLEOF, EXTERNALMEASURE, TOCSV, TOJSON, etc. |
| Window Functions | 9 | INDEX, OFFSET, WINDOW, RANKX, ROWNUMBER, ORDERBY, PARTITIONBY, MATCHBY, etc. |

### Additional Articles
- **DAX Queries**: EVALUATE syntax, DEFINE, ORDER BY, START AT
- **DAX Glossary**: Core terminology
- **User-Defined Functions (UDF)**: Preview feature documentation

## Ingestion Notes

- **Stage 1 (2026-07-26):** Conceptual atomics + gotchas + references (11 notes)
- **Stage 2 (2026-07-26):** Patterns + UDF function note (6 notes)
- **Stage 3 (2026-07-26):** Core functions batch 1 — filter/logical/aggregation (24 notes)
- **Stage 4 (2026-07-26):** Core functions batch 2 — time intel/table manip/window/info/scalar (21 notes)
- **Total notes written:** 62 function/concept/reference notes

## Key Notes for This Source

- The document uses 7-note articles for best practices (BLANK handling, FILTER, SELECTEDVALUE, COUNTROWS, variables, error handling, window functions) — these are the highest-value ingestion targets alongside the function reference
- The UDF feature is documented as **preview**: the API may change
- DAX queries (EVALUATE, DEFINE, etc.) are documented in the reference section
- ~380 functions remain as bulk references not individually written — target for future batch ingestion sessions

## Related Notes

- [[dax-overview]] — atomic
- [[dax-context]] — atomic
- [[calculate]] — function
- [[time-intelligence-functions-overview]] — function
- [[window-functions-overview]] — function
- [[dax-glossary]] — reference
