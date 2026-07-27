---
created: 2026-07-26
note_type: index
tags: [dax, index]
---

# DAX Code — Knowledge Base Index

This is the index for the DAX Code knowledge base. Notes are grouped by type.

## Conceptual Atomics

| Note | Description |
|------|-------------|
| [[dax-overview]] | DAX language overview |
| [[dax-data-types]] | Data types in DAX |
| [[dax-context]] | Row context, filter context, and query context |
| [[measures-vs-calculated-columns]] | Differences between measures and calculated columns |
| [[table-relationships-in-dax]] | Relationships and how DAX uses them |

## Gotchas

| Note | Description |
|------|-------------|
| [[avoid-converting-blanks-to-values]] | Don't convert BLANK to zero |
| [[avoid-using-filter-as-filter-argument]] | FILTER in CALCULATE is often slow |
| [[divide-function-vs-divide-operator]] | DIVIDE() vs / operator |

## Reference Notes

| Note | Description |
|------|-------------|
| [[dax-operators]] | All DAX operators |
| [[dax-syntax]] | Formula syntax rules |
| [[dax-queries]] | EVALUATE, DEFINE, ORDER BY |
| [[dax-glossary]] | Key terminology |
| [[information-functions-overview]] | ISFILTERED, HASONEVALUE, ISINSCOPE, etc. |
| [[table-manipulation-functions-overview]] | ADDCOLUMNS, SUMMARIZECOLUMNS, etc. |
| [[time-intelligence-functions-overview]] | TOTALYTD, DATEADD, SAMEPERIODLASTYEAR, etc. |
| [[window-functions-overview]] | INDEX, OFFSET, WINDOW, RANKX, etc. |

## Patterns

| Note | Description |
|------|-------------|
| [[use-selectedvalue-instead-of-values]] | SELECTEDVALUE over HASONEVALUE+VALUES |
| [[use-countrows-instead-of-count]] | COUNTROWS over COUNT |
| [[use-variables-in-dax-formulas]] | VAR pattern |
| [[window-functions-orderby-partitionby-matchby]] | ORDERBY/PARTITIONBY/MATCHBY guide |
| [[appropriate-use-of-error-functions]] | IFERROR best practices |
| [[sales-to-budget-variance-percent]] | Retail variance pattern: DIVIDE(Actual, Budget) − 1 |
| [[conditional-variance-display-percent-hide]] | Hide −100% variance for missing budgets |
| [[inventory-aging-buckets-0-1-1-2-5-weeks]] | Inventory age bucket measures with 0-return guard |
| [[dax-coding-challenge-sales-analytics-library]] | 5-measure sales analytics library |

## Atomic Conceptual Notes

| Note | Description |
|------|-------------|
| [[filter-context-vs-row-context]] | Core DAX evaluation contexts |
| [[context-transition-with-calculate]] | CALCULATE inside iterators and calculated columns |

## Gotchas

| Note | Description |
|------|-------------|
| [[avoid-converting-blanks-to-values]] | Don't convert BLANK to zero |
| [[avoid-using-filter-as-filter-argument]] | FILTER in CALCULATE is often slow |
| [[divide-function-vs-divide-operator]] | DIVIDE() vs / operator |
| [[blank-vs-zero-in-averages]] | BLANK excluded from averages; 0 included |

## Source Notes

| Note | Description |
|------|-------------|
| [[advanced-power-bi-dax-measures-retail-analytics-source]] | Jesse Ruiz — DAX Pt 1 & 2 source |
| [[the-dax-concepts-that-actually-save-you-time-source]] | Daniel Olatunji — fundamentals source |
| [[ALL, ALLEXCEPT, ALLSELECTED, and REMOVEFILTERS in Power BI What’s the Difference]] | Gulab Chand Tejwani — ALL/ALLEXCEPT/ALLSELECTED/REMOVEFILTERS guide |
| [[CALCULATE in Power BI The Most Important Function in DAX Explained with Examples]] | Gulab Chand Tejwani — CALCULATE fundamentals |
| [[Calculated objects in Power BI]] | LearnBI — columns, tables, measures, calculation groups |
| [[Iterators in DAX SUMX, AVERAGEX, RANKX and How They Use Row & Filter Context]] | Gulab Chand Tejwani — iterators and context |
| [[Mastering Power BI Accurate Aggregation with DAX]] | Mark Chen — AVERAGEX aggregation patterns |
| [[Power BI Demystified Row Context vs. Context Transition Explained with Examples]] | Gulab Chand Tejwani — row context and context transition |
| [[Simplify Your DAX Expressions with Direct Filters in Power BI]] | Mark Chen — direct filter arguments in CALCULATE |
| [[The FILTER Function in DAX Friend or Foe]] | Gulab Chand Tejwani — FILTER function deep dive |
| [[Using Visual Calculation To Easily Calculate Avg 3 Month Sales In Power BI(.pbix included)]] | Shashanka Shekhar — MOVINGAVERAGE visual calculation |
| [[What is Filter Context in Power BI A Complete Guide with Examples and Visuals]] | Gulab Chand Tejwani — filter context fundamentals |
| [[Why Totals Look Wrong in DAX (and How to Fix Them)]] | Gulab Chand Tejwani — wrong totals, SUMX, HASONEVALUE fixes |

## Reference Notes

| Note | Description |
|------|-------------|
| [[dax-operators]] | All DAX operators |
| [[dax-syntax]] | Formula syntax rules |
| [[dax-queries]] | EVALUATE, DEFINE, ORDER BY |
| [[dax-glossary]] | Key terminology |
| [[information-functions-overview]] | ISFILTERED, HASONEVALUE, ISINSCOPE, etc. |
| [[table-manipulation-functions-overview]] | ADDCOLUMNS, SUMMARIZECOLUMNS, etc. |
| [[time-intelligence-functions-overview]] | TOTALYTD, DATEADD, SAMEPERIODLASTYEAR, etc. |
| [[time-intelligence-quick-reference-retail-analytics]] | Retail analytics time intel cheat sheet |
| [[window-functions-overview]] | INDEX, OFFSET, WINDOW, RANKX, etc. |

## Functions

### Filter & Context

| Note | Description |
|------|-------------|
| [[calculate]] | CALCULATE |
| [[calculate-table]] | CALCULATETABLE |
| [[filter]] | FILTER |
| [[all]] | ALL |
| [[allexcept]] | ALLEXCEPT |
| [[allselected]] | ALLSELECTED |
| [[removefilters]] | REMOVEFILTERS |
| [[keepfilters]] | KEEPFILTERS |

### Table

| Note | Description |
|------|-------------|
| [[values]] | VALUES |
| [[distinct]] | DISTINCT |
| [[selectedvalue]] | SELECTEDVALUE |
| [[coalesce]] | COALESCE |
| [[summarizecolumns]] | SUMMARIZECOLUMNS |
| [[addcolumns]] | ADDCOLUMNS |
| [[selectcolumns]] | SELECTCOLUMNS |
| [[union-intersect-except]] | UNION, INTERSECT, EXCEPT |
| [[generate-and-generateall]] | GENERATE, GENERATEALL |
| [[treatas]] | TREATAS |
| [[generateseries-and-datatable]] | GENERATESERIES, DATATABLE |

### Logical

| Note | Description |
|------|-------------|
| [[if]] | IF, IF.EAGER |
| [[switch]] | SWITCH |
| [[iferror]] | IFERROR |
| [[coalesce]] | COALESCE |

### Aggregation

| Note | Description |
|------|-------------|
| [[sum]] | SUM |
| [[sumx]] | SUMX |
| [[countrows]] | COUNTROWS |
| [[distinctcount]] | DISTINCTCOUNT |
| [[divide]] | DIVIDE |
| [[average]] | AVERAGE, AVERAGEX |
| [[min]] | MIN, MINX |
| [[max]] | MAX, MAXX |

### Context & Relationships

| Note | Description |
|------|-------------|
| [[earlier]] | EARLIER |
| [[related]] | RELATED |
| [[userexplicitrelationship]] | USERELATIONSHIP |
| [[crossfilter]] | CROSSFILTER |

### Time Intelligence

| Note | Description |
|------|-------------|
| [[datesytd]] | DATESYTD |
| [[sameperiodlastyear]] | SAMEPERIODLASTYEAR |
| [[dateadd]] | DATEADD |
| [[datesbetween]] | DATESBETWEEN |

### Window

| Note | Description |
|------|-------------|
| [[the-dax-concepts-that-actually-save-you-time-source]] | Source note — Daniel Olatunji fundamentals |
| [[offset]] | OFFSET |
| [[window]] | WINDOW |
| [[rankx]] | RANKX |
| [[rownumber]] | ROWNUMBER |

### Information & Lookup

| Note | Description |
|------|-------------|
| [[lookupvalue]] | LOOKUPVALUE |

### Text

| Note | Description |
|------|-------------|
| [[format]] | FORMAT |
| [[concatenatex]] | CONCATENATEX |

### Other

| Note | Description |
|------|-------------|
| [[blank]] | BLANK |
| [[error]] | ERROR |
| [[evaluate]] | EVALUATE |
| [[var-variable]] | VAR |
| [[parent-child-functions]] | PATH, PATHITEM, PATHLENGTH |
| [[dax-user-defined-functions-udf]] | UDF (preview) |
