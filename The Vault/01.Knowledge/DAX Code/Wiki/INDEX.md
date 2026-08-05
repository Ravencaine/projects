---
created: 2026-07-26
updated: 2026-08-02
note_type: index
tags: [dax, index]
---

# DAX Code - Knowledge Base Index

This is the index for the DAX Code knowledge base. 879 notes grouped by type.

## Conceptual Atomics  (429 notes)

| Note | Description |
|------|-------------|
| [[5-dax-performance-patterns-reference.md]] | The 5 DAX Performance Patterns — Quick Reference

Five anti-patterns responsible for 78% of slow DAX measures, found in  |
| [[5-senior-dax-patterns-source.md]] | The 5 DAX Patterns Senior Analysts Use

> Type: article
> Author: Gulab Chand Tejwani
> Published: 2025-07-14
> URL: htt |
| [[Author-Gulab-Chand-Tejwani]] | Gulab Chand Tejwani

Power BI practitioner and author of the empirical DAX performance study: I Analyzed 5,000 DAX Measu |
| [[Author-Md-Mizanur-Rahman-Nayan]] | Md Mizanur Rahman Nayan — DAX Author

PL-300 Certified Power BI practitioner. |
| [[DIVIDE.md]] | DIVIDE

Performs division and returns an alternate result if the denominator is zero or blank. |
| [[FORMAT.md]] | FORMAT

Converts a value to text in a specified format. |
| [[Mastering Power BI Accurate Aggregation with DAX.md]] | Introduction: Creating accurate and dynamic reports in Power BI can be an art. |
| [[QUESTIONS.md]] | Open Questions

(None yet — questions surface here after ingestion, health checks, or during note-writing.) |
| [[SWITCH.md]] | SWITCH

Evaluates a list of expressions and returns one of multiple possible results. |
| [[Simplify Your DAX Expressions with Direct Filters in Power BI.md]] | When working with Power BI, optimizing and simplifying your DAX (Data Analysis Expressions) code can make a significant  |
| [[The FILTER Function in DAX Friend or Foe.md]] | The FILTER function is one of the most powerful and misunderstood tools in DAX. |
| [[UNICHAR.md]] | UNICHAR

Returns the Unicode character corresponding to a code point. |
| [[Why Totals Look Wrong in DAX (and How to Fix Them).md]] | If you’ve ever seen a Power BI total that made no sense, you’re not alone. |
| [[abs-sign-sqrt.md]] | ABS, SIGN, SQRT

Basic numeric operations: absolute value, sign, and square root. |
| [[abs.md]] | ABS

Applies to: Calculated column Calculated table Measure Visual calculation Returns the absolute value of a number. |
| [[accrint.md]] | ACCRINT

Returns the accrued interest for a security that pays periodic interest. |
| [[accrintm.md]] | ACCRINTM

Applies to: Calculated column Calculated table Measure Visual calculation Returns the accrued interest for a s |
| [[acos.md]] | ACOS

Applies to: Calculated column Calculated table Measure Visual calculation Returns the arccosine, or inverse cosine |
| [[acosh.md]] | ACOSH

Applies to: Calculated column Calculated table Measure Visual calculation Returns the inverse hyperbolic cosine o |
| [[acot.md]] | ACOT

Applies to: Calculated column Calculated table Measure Visual calculation Returns the principal value of the arcco |
| [[acoth.md]] | ACOTH

Applies to: Calculated column Calculated table Measure Visual calculation Returns the inverse hyperbolic cotangen |
| [[addcolumns.md]] | ADDCOLUMNS

Applies to: Calculated column Calculated table Measure Visual calculation Adds calculated columns to the giv |
| [[addmissingitems.md]] | ADDMISSINGITEMS

Applies to: Calculated column Calculated table Measure Visual calculation Adds rows with empty values t |
| [[all.md]] | ALL

Signature
```
ALL([<table> | <column>[, <column>[, …])
```

Parameters

| | Parameter | Type | Description |
|---|- |
| [[and-slicer-multi-select-dax.md]] | AND Slicer / Multi-Select Pattern in DAX

Default Power BI slicers use OR logic — selecting more values returns more row |
| [[and.md]] | AND

Syntax

```dax
AND(<logical1>,<logical2>)
```

Remarks

The AND function in DAX accepts only two (2) arguments. |
| [[appropriate-use-of-error-functions.md]] | Appropriate Use of Error Functions

ISERROR and IFERROR help handle evaluation-time errors, but misuse degrades performa |
| [[asin.md]] | ASIN

Applies to: Calculated column Calculated table Measure Visual calculation Returns the arcsine, or inverse sine, of |
| [[asinh.md]] | ASINH

Applies to: Calculated column Calculated table Measure Visual calculation Returns the inverse hyperbolic sine of  |
| [[atan.md]] | ATAN

Applies to: Calculated column Calculated table Measure Visual calculation Returns the arctangent, or inverse tange |
| [[atanh.md]] | ATANH

Applies to: Calculated column Calculated table Measure Visual calculation Returns the inverse hyperbolic tangent  |
| [[auto-exist-and-all-gotchas.md]] | Auto-Exist and ALL() Gotchas

Article - 09/20/2022

Auto-Exist

Auto-exist is an optimization in DAX where only combinat |
| [[avoid-converting-blanks-to-values.md]] | Avoid Converting BLANKs to Values

It is tempting to convert BLANK results to zero (or another default value) in measure |
| [[avoid-using-filter-as-filter-argument.md]] | Avoid Using FILTER as Filter Argument

Using FILTER as a CALCULATE filter argument is a common mistake that hurts perfor |
| [[base-measure-design.md]] | Base Measure Design

The quality of a measure branching model depends on the base measures. |
| [[basic-aggregation-measures.md]] | Basic Aggregation Measures

DAX measures start with aggregations — SUM, COUNTROWS, AVERAGE, DISTINCTCOUNT. |
| [[better-mod-workaround-dax.md]] | Better MOD Workaround

A corrected implementation of the modulo operation in DAX that handles floating-point/decimal div |
| [[better-mod-workaround-in-dax.md]] | Better MOD Workaround in DAX

DAX's MOD function has a known quirk when handling large negative numbers. |
| [[better-together-market-basket-dax.md]] | Better Together — Market Basket Analysis

Identifies pairs of items that are purchased together in the same order, enabl |
| [[blank.md]] | BLANK

Returns a blank value. |
| [[box-size-optimization-dax.md]] | Box Size Optimization in DAX

Selecting the optimal shipping box based on item dimensions using DAX spatial calculations |
| [[box-sizes-for-shipping-in-dax.md]] | Box Sizes for Shipping in DAX

Determining the optimal box size from a set of standard sizes based on item dimensions. |
| [[bradford-factor-dax.md]] | Bradford Factor in DAX

The Bradford Factor weights employee absenteeism by frequency of absences. |
| [[ceiling.md]] | CEILING

Applies to: Calculated column Calculated table Measure Visual calculation Rounds a number up, to the nearest in |
| [[coalesce.md]] | COALESCE

Signature

```dax
COALESCE(<expr1>, <expr2>, ...)
```

Parameters

| Parameter | Description |
|-----------|-- |
| [[column-and-measure-references.md]] | Column and Measure References

Article - 09/20/2022

Column References

Fully Qualified

`Table[Column]` — includes the  |
| [[combin.md]] | COMBIN

Applies to: Calculated column Calculated table Measure Visual Returns the number of combinations for a given num |
| [[combina.md]] | COMBINA

Applies to: Calculated column Calculated table Measure Visual Returns the number of combinations (with repetiti |
| [[combinevalues.md]] | COMBINEVALUES

Applies to: Calculated column Calculated table Measure Visual calculation Joins two or more text strings  |
| [[complex-selector-pattern-in-dax.md]] | Complex Selector Pattern in DAX

Using disconnected tables with multi-column logic to implement complex selection criter |
| [[compound-interest-future-value-dax.md]] | Compound Interest and Future Value in DAX

Financial calculations for compound interest and future value. |
| [[convert.md]] | CONVERT — Data Type Conversion

Converts a value from one data type to another. |
| [[cos.md]] | COS

Applies to: Calculated column Calculated table Measure Visual Returns the cosine of the given angle. |
| [[cosh.md]] | COSH

Applies to: Calculated column Calculated table Measure Visual Returns the hyperbolic cosine of a number. |
| [[cot.md]] | COT

Applies to: Calculated column Calculated table Measure Visual calculation Returns the cotangent of an angle specifi |
| [[coth.md]] | COTH

Applies to: Calculated column Calculated table Measure Visual calculation Returns the hyperbolic cotangent of a hy |
| [[crossfilter.md]] | CROSSFILTER

Signature

```dax
CROSSFILTER(<columnName1>, <columnName2>, <crossFilterType>)
```

Parameters

| Parameter |
| [[crossjoin-naturaljoin.md]] | CROSSJOIN, NATURALINNERJOIN, NATURALLEFTOUTERJOIN

Table joins and cross-products. |
| [[crossjoin.md]] | CROSSJOIN

Applies to: Calculated column Calculated table Measure Visual calculation Returns a table that contains the C |
| [[currency.md]] | CURRENCY

Applies to: Calculated column Calculated table Measure Visual calculation Evaluates the argument and returns t |
| [[currentgroup.md]] | CURRENTGROUP

Applies to: Calculated column Calculated table Measure Visual This function is discouraged for use in visu |
| [[dax-coding-challenge-sales-analytics-library.md]] | DAX Coding Challenge — Sales Analytics Library

A solved take-home coding challenge covering the five foundational measu |
| [[dax-common-mistakes-beginners.md]] | DAX Common Mistakes: The Ones That Still Show Up

The mistakes Daniel Olatunji sees most often — and how to avoid them. |
| [[dax-complete-guide-janvi-source.md]] | DAX — The Complete Guide — Janvi Gupta

> Type: tutorial / beginner guide
> Author: Janvi Gupta
> Published: 2026-01-05
 |
| [[dax-data-types.md]] | DAX Data Types

DAX supports a defined set of data types that control how values are stored and evaluated. |
| [[dax-documentation-philosophy.md]] | DAX Documentation Philosophy: Pattern + Condition

DAX pattern documentation should always include the conditions under  |
| [[dax-finally-got-user-defined-functions-source.md]] | DAX Finally Got User-Defined Functions (source note)

> Type: article
> Author: Gulab Chand Tejwani
> Published: 2026-07 |
| [[dax-for-humans-deckler-source.md]] | DAX for Humans (Greg Deckler, Packt 2025)

Greg Deckler's contrarian guide to DAX — teaching the language without CALCUL |
| [[dax-function-naming-convention-a-x.md]] | DAX Function Naming Convention — "A" and "X" Suffixes

The Core Rule

DAX uses two suffixes to signal behavior:

| Suffi |
| [[dax-functions-shortlist.md]] | DAX Functions: The 8 That Cover 80% of Real Work

A curated shortlist from Daniel Olatunji's experience — the functions  |
| [[dax-gaps-and-islands-pattern.md]] | DAX Gaps and Islands Pattern

Detect the longest consecutive run of a condition per entity — e.g., longest streak of act |
| [[dax-glossary.md]] | DAX Glossary

A quick reference for DAX terminology. |
| [[dax-index-pattern-deckler.md]] | DAX Index Pattern (Row Number)

Purpose

DAX has no native row-number function. |
| [[dax-index-pattern-row-number-in-dax.md]] | DAX Index Pattern (Row Number)

Generating a sequential row number within a table or filtered context. |
| [[dax-is-column-oriented.md]] | DAX Is Column-Oriented — Unlike Excel Cell Formulas

DAX formulas operate on entire columns at once, not individual cell |
| [[dax-left-function.md]] | LEFT() — Extract Prefix Characters from DAX Text

`LEFT()` returns the specified number of characters from the start of  |
| [[dax-logical-operators.md]] | DAX Logical Operators

Operators

| Operator | Name | Description |
|----------|------|-------------|
| `&&` | AND | Bot |
| [[dax-measure-audit-workflow.md]] | DAX Measure Audit Workflow

A 3-step workflow to identify, diagnose, and fix slow DAX measures using Performance Analyze |
| [[dax-measure-library-architecture-source.md]] | DAX Measure Library Architecture — From Messy to Maintainable (source note)

> Type: article
> Author: Gulab Chand Tejwa |
| [[dax-measure-naming-convention-framework.md]] | DAX Measure Naming Convention Framework

The naming convention formula and rules that make DAX measures findable through |
| [[dax-measure-use-cases.md]] | DAX Measure Use Cases

Measures are for numbers that change based on report context — anything that aggregates, compares |
| [[dax-operators.md]] | DAX Operators: Arithmetic, Comparison, Logical, and Text

Complete reference for all operator types available in DAX for |
| [[dax-optimization-9-iteration-case-study.md]] | DAX Optimization — 9-Iteration Case Study

A step-by-step optimization of a slow measure, reducing query time from ~10 m |
| [[dax-optimization-best-practices.md]] | DAX Optimisation: Best Practices Checklist

DAX that works and DAX that works fast are different. |
| [[dax-optimization-tools-reference.md]] | DAX Optimization Tools — Quick Reference

Overview of the three primary tools for analyzing and improving DAX query perf |
| [[dax-overview.md]] | DAX Overview

Data Analysis Expressions (DAX) is a formula expression language for Power BI, Analysis Services, and Powe |
| [[dax-parameter-naming.md]] | DAX Parameter Naming Conventions

Article - 10/20/2023

Parameter names are standardized in DAX reference documentation  |
| [[dax-performance-5000-measures-source.md]] | I Analyzed 5,000 DAX Measures: The 5 Patterns That Kill Performance

> Type: article
> Author: Gulab Chand Tejwani
> Pub |
| [[dax-performance-optimization-techniques.md]] | DAX Performance Optimization Techniques

Practical methods for improving DAX query speed in large semantic models. |
| [[dax-performance-optimization-tools.md]] | DAX Performance Optimization Tools

Tools for profiling and optimizing DAX performance, covered in Ch15 of DAX for Human |
| [[dax-performance-patterns.md]] | DAX Performance Best Practices

Measure vs Calculated Column

- Use measures for aggregations that respond to filters
-  |
| [[dax-queries.md]] | DAX Queries

DAX queries are statements run in DAX query view (Power BI Desktop), DAX Studio, or SQL Server Management S |
| [[dax-query-language-reference.md]] | DAX Query Language Reference

Article - 12/13/2024

A DAX query is used to retrieve data from a data model. |
| [[dax-source-note.md]] | Microsoft Learn DAX Reference (dax.pdf)

Document: Data Analysis Expressions (DAX) Reference — Microsoft Learn
Source fi |
| [[dax-studio-performance-validation.md]] | DAX Studio Performance Validation

DAX Studio is the primary tool for validating measure performance. |
| [[dax-sum-vs-sumx-when-each.md]] | SUM vs SUMX — When Each Applies

The Misleading "Best Practice"

"Always use SUM instead of SUMX — SUMX is slower becaus |
| [[dax-sumx-function.md]] | SUMX() — Row-By-Row Iteration with Expression

`SUMX()` iterates through each row of a table, evaluates an expression fo |
| [[dax-syntax.md]] | DAX Syntax

DAX syntax rules govern how formulas, references, and expressions are written. |
| [[dax-tools.md]] | DAX Tools

Built-in Tools

Power BI Desktop
- Formula bar with AutoComplete for writing DAX formulas
- DAX Editor for ca |
| [[dax-udf-adoption-workflow.md]] | Adopt DAX UDFs in a Production Model

A four-move workflow for safely introducing DAX user-defined functions into an exi |
| [[dax-udf-define-function-pattern.md]] | DEFINE FUNCTION Syntax Pattern

The canonical pattern for defining a DAX user-defined function with a doc comment, typed |
| [[dax-udf-source.md]] | DAX Finally Got User-Defined Functions

> Type: article
> Author: Gulab Chand Tejwani
> Published: 2025-06-09
> URL: htt |
| [[dax-user-defined-functions-udf.md]] | DAX User-Defined Functions (UDF)

User-Defined Functions (UDFs) let you package DAX logic into reusable, named functions |
| [[dax-user-defined-functions-udfs.md]] | DAX User-Defined Functions (UDFs)

DAX UDFs are named, parameterized, first-class function objects defined in the semant |
| [[dax-vs-excel-mindset-difference.md]] | DAX vs Excel: The Mindset Shift

DAX looks like Excel formulas but works completely differently. |
| [[dax-year-over-year.md]] | DAX Year-over-Year: CALCULATE + LEFT + Calculated Field Composition

A three-step pattern for building year-over-year gr |
| [[dax-year.md]] | YEAR

Extracts the four-digit year from a date value. |
| [[daxlib-sqlbi-open-source-dax-library.md]] | daxlib: SQLBI Open-Source DAX Function Library

daxlib is an open-source repository of model-independent DAX user-define |
| [[day.md]] | DAY

Applies to: Calculated column Calculated table Measure Visual calculation Returns the day of the month, a number fr |
| [[days-of-supply-dos-dax.md]] | Days of Supply (DOS) in DAX

Inventory KPI measuring how many days of inventory remain at the current consumption rate. |
| [[db.md]] | DB

Applies to: Calculated column Calculated table Measure Visual calculation Returns the depreciation of an asset for a |
| [[ddb.md]] | DDB

Applies to: Calculated column Calculated table Measure Visual calculation Returns the depreciation of an asset for  |
| [[defensive-dax-error-handling.md]] | Defensive DAX: Explicit Error Handling

Never trust your data, your users, or your future self. |
| [[degrees.md]] | DEGREES

Applies to: Calculated column Calculated table Measure Visual calculation Converts radians into degrees. |
| [[direct-filter-pattern.md]] | Direct Filter Pattern in CALCULATE

Replace verbose `FILTER()` table iterators inside `CALCULATE` with concise direct fi |
| [[disc.md]] | DISC

Returns the discount rate for a security. |
| [[distinct.md]] | DISTINCT

Signature

```dax
DISTINCT(<column>)
DISTINCT(<table>)
```

Parameters

| Parameter | Description |
|--------- |
| [[divide-function-vs-divide-operator.md]] | DIVIDE Function vs Divide Operator

`DIVIDE()` and the `/` operator both perform division, but they handle division by z |
| [[duration.md]] | DURATION

Applies to: Calculated column Calculated table Measure Visual calculation Returns the Macauley duration for an |
| [[dynamic-granularity-scale-in-dax.md]] | Dynamic Granularity Scale in DAX

Displaying measures at different granularities based on the selected time period. |
| [[dynamic-measure-selection-in-dax.md]] | Dynamic Measure Selection in DAX

Allowing users to select which measure to display from a disconnected slicer. |
| [[dynamic-ranking-in-dax-quick-reference.md]] | Dynamic Ranking in DAX — Quick Reference

Core patterns for building Top N leaderboards that respond correctly to slicer |
| [[dynamic-ranking-source.md]] | Dynamic Ranking in DAX: How I Built a Top 5 Dashboard That Actually Worked

> Type: article
> Author: Gulab Chand Tejwan |
| [[dynamic-top-n-ranking-pattern.md]] | Dynamic Top N Ranking Pattern

Control what the ranking universe is by choosing exactly which filters ALL() removes. |
| [[dynamic-top-n-vs-others-pattern.md]] | Dynamic Top N vs Others Pattern

Uses DAX UNION() + ROW() to combine "Top N" and "Others" into a single two-row virtual  |
| [[effect.md]] | EFFECT

Applies to: Calculated column Calculated table Measure Visual calculation Returns the effective annual interest  |
| [[elapsed-time-between-timestamps.md]] | Elapsed Time Between Timestamps

Calculating the exact elapsed time between two datetime values in DAX. |
| [[endofmonth.md]] | ENDOFMONTH

Applies to: Calculated column Calculated table Measure Visual calculation ７ Note This function is discourage |
| [[endofquarter.md]] | ENDOFQUARTER

Applies to: Calculated column Calculated table Measure Visual calculation ７ Note This function is discoura |
| [[endofweek.md]] | ENDOFWEEK

Applies to: Calculated column Calculated table Measure Visual calculation ７ Note This function is discouraged |
| [[endofyear.md]] | ENDOFYEAR

Applies to: Calculated column Calculated table Measure Visual calculation ７ Note This function is discouraged |
| [[error.md]] | ERROR

Applies to: Calculated column Calculated table Measure Visual Raises an error with an error message. |
| [[even.md]] | EVEN

Applies to: Calculated column Calculated table Measure Visual calculation Returns number rounded up to the nearest |
| [[exact.md]] | EXACT

Applies to: Calculated column Calculated table Measure Visual calculation Compares two text strings and returns T |
| [[except.md]] | EXCEPT — Set Difference

Returns rows from the left table that do not exist in the right table. |
| [[exp.md]] | EXP

Applies to: Calculated column Calculated table Measure Visual calculation Returns e raised to the power of a given  |
| [[expon.dist.md]] | EXPON.DIST

Applies to: Calculated column Calculated table Measure Visual calculation Returns the exponential distributi |
| [[fact.md]] | FACT

Syntax

```dax
FACT(<number>)
```

Remarks

If the number is not an integer, it is truncated and an error is retur |
| [[false.md]] | FALSE

Applies to: Calculated column Calculated table Measure Visual calculation Returns the logical value FALSE. |
| [[filter.md]] | FILTER

Signature
```
FILTER(<table>, <filter>)
```

Parameters

| | Parameter | Type | Description |
|---|-----------|- |
| [[filters-topn.md]] | FILTERS and TOPN

Return the active filters on a column, or the top N rows of a table. |
| [[filters.md]] | FILTERS

Syntax

```dax
FILTERS(<columnName>)
```

Remarks

This function is not supported for use in DirectQuery mode w |
| [[find.md]] | FIND — Case-sensitive Text Search

Returns the starting position of a substring within a text string. |
| [[fixed.md]] | FIXED

Applies to: Calculated column Calculated table Measure Visual calculation Rounds a number to the specified number |
| [[floor.md]] | FLOOR

Applies to: Calculated column Calculated table Measure Visual calculation Rounds a number down, toward zero, to t |
| [[function.md]] | FUNCTION

Introduces a function definition within a DEFINE statement in a DAX query. |
| [[fuzzy-matching-in-dax.md]] | Fuzzy Matching in DAX

Finding approximate string matches when exact matching fails. |
| [[fuzzy-matching-levenshtein-dax.md]] | Fuzzy Matching — Levenshtein Distance

Purpose

Fuzzy matching identifies strings that are approximately, but not exactl |
| [[fv.md]] | FV

Applies to: Calculated column Calculated table Measure Visual calculation Calculates the future value of an investme |
| [[gamma-function-in-dax.md]] | GAMMA — Gamma Function via Lanczos Approximation

DAX has no native GAMMA function. |
| [[gaps-and-islands-source-nayan.md]] | Gaps and Islands: Solving Consecutive Active Days in Power BI

> Type: article / tutorial
> Author: Md Mizanur Rahman Na |
| [[gaps-and-islands-theory.md]] | Gaps and Islands Theory

A framework for identifying and grouping consecutive sequences in ordered data, particularly us |
| [[gb18030-character-set.md]] | GB18030 Character Set Support

China's GB18030-2022 standard is the latest update to the Chinese character encoding stan |
| [[gcd.md]] | GCD

Applies to: Calculated column Calculated table Measure Visual calculation Returns the greatest common divisor of tw |
| [[generate-and-generateall.md]] | GENERATE and GENERATEALL

Returns the Cartesian product of table1 with the table resulting from evaluating table2 in the |
| [[generate.md]] | GENERATE

Applies to: Calculated column Calculated table Measure Visual calculation Returns a table with the Cartesian p |
| [[generateall.md]] | GENERATEALL

Returns a table with the Cartesian product between each row in table1 and the table that results from evalu |
| [[greg-deckler.md]] | Greg Deckler

Greg Deckler is a Microsoft MVP and one of the most influential voices in the Power BI and DAX community. |
| [[grouping-rows-in-dax.md]] | Grouping Rows in DAX

Using SUMMARIZECOLUMNS and GROUPBY to create grouped aggregations. |
| [[handling-errors-in-dax.md]] | Handling Errors in DAX

Managing errors gracefully in DAX measures and calculated columns. |
| [[hasonefilter.md]] | HASONEFILTER

Applies to: Calculated column Calculated table Measure Visual calculation Returns TRUE when the number of  |
| [[hour.md]] | HOUR

Applies to: Calculated column Calculated table Measure Visual calculation Returns the hour as a number from 0 (12: |
| [[hours-breakdown-in-dax.md]] | Hours Breakdown in DAX

Breaking elapsed time into component hours (business hours, overtime, etc.). |
| [[human-capital-value-added-hcva-dax.md]] | Human Capital Value Added (HCVA) in DAX

HCVA measures the net profit each employee contributes to the organization. |
| [[if.eager.md]] | IF.EAGER

Applies to: Calculated column Calculated table Measure Visual calculation Checks a condition, and returns one  |
| [[if.md]] | IF / IF.EAGER

Signature

```dax
IF(<logical_test>, <value_if_true>[, <value_if_false>])
IF.EAGER(<logical_test>, <value |
| [[ignore.md]] | IGNORE

Applies to: Calculated column Calculated table Measure Visual calculation Modifies the behavior of the SUMMARIZE |
| [[implement-dax-measure-library-architecture.md]] | Implement a DAX Measure Library Architecture

A 4-week implementation plan to transform a chaotic measures table into a  |
| [[implicit-measure-trap.md]] | Implicit Measure Trap

Dragging a numeric field directly into a visual creates an implicit measure — Power BI silently g |
| [[int.md]] | INT

Applies to: Calculated column Calculated table Measure Visual calculation Rounds a number down to the nearest integ |
| [[intersect.md]] | INTERSECT — Row Overlap

Returns the rows that appear in both tables. |
| [[intrate.md]] | INTRATE

Applies to: Calculated column Calculated table Measure Visual calculation Returns the interest rate for a fully |
| [[inverse-and-slicer-pattern-in-dax.md]] | Inverse AND Slicer Pattern

Implementing a slicer where selecting multiple values shows items that match ALL selected fi |
| [[inverse-slicer-pattern-dax.md]] | NOT / Inverse Slicer Pattern in DAX

A NOT slicer filters OUT the values selected in the slicer, rather than keeping the |
| [[ipmt.md]] | IPMT

Applies to: Calculated column Calculated table Measure Visual calculation Returns the interest payment for a given |
| [[irr-dax-xirr.md]] | Internal Rate of Return in DAX

Calculating IRR (for regular intervals) and XIRR (for irregular cash flow dates) in DAX. |
| [[isafter.md]] | ISAFTER

Applies to: Calculated column Calculated table Measure Visual A boolean function that emulates the behavior of  |
| [[isblank.md]] | ISBLANK

Applies to: Calculated column Calculated table Measure Visual calculation Checks whether a value is blank, and  |
| [[isboolean.md]] | ISBOOLEAN

Syntax

```dax
ISBOOLEAN(<value>)
```

Remarks

This function is not supported for use in DirectQuery mode wh |
| [[iscurrency.md]] | ISCURRENCY

Syntax

```dax
ISCURRENCY(<value>)
```

Remarks

This function is not supported for use in DirectQuery mode  |
| [[isdecimal.md]] | ISDECIMAL

Syntax

```dax
ISDECIMAL(<value>)
```

Remarks

This function is not supported for use in DirectQuery mode wh |
| [[isdouble.md]] | ISDOUBLE

Syntax

```dax
ISDOUBLE(<value>)
```

Remarks

This function is not supported for use in DirectQuery mode when |
| [[isempty.md]] | ISEMPTY

Applies to: Calculated column Calculated table Measure Visual calculation Checks if a table is empty. |
| [[iseven.md]] | ISEVEN

Applies to: Calculated column Calculated table Measure Visual calculation Returns TRUE if number is even, or FAL |
| [[isint64.md]] | ISINT64

Syntax

```dax
ISINT64(<value>)
```

Remarks

This function is not supported for use in DirectQuery mode when u |
| [[isinteger.md]] | ISINTEGER

Syntax

```dax
ISINTEGER(<value>)
```

Remarks

This function is not supported for use in DirectQuery mode wh |
| [[islogical.md]] | ISLOGICAL

Applies to: Calculated column Calculated table Measure Visual calculation Checks whether a value is a logical |
| [[isnumber.md]] | ISNUMBER

Applies to: Calculated column Calculated table Measure Visual calculation Checks whether a value is a number,  |
| [[isnumeric.md]] | ISNUMERIC

Syntax

```dax
ISNUMERIC(<value>)
```

Remarks

This function is not supported for use in DirectQuery mode wh |
| [[iso.ceiling.md]] | ISO.CEILING

Applies to: Calculated column Calculated table Measure Visual calculation Rounds a number up, to the neares |
| [[isodd.md]] | ISODD

Applies to: Calculated column Calculated table Measure Visual calculation Returns TRUE if number is odd, or FALSE |
| [[isonorafter.md]] | ISONORAFTER

Applies to: Calculated column Calculated table Measure Visual A boolean function that emulates the behavior |
| [[issubtotal.md]] | ISSUBTOTAL

Applies to: Calculated column Calculated table Measure Visual calculation Creates another column in a SUMMAR |
| [[iterator-functions-sumx.md]] | Iterator Functions: SUMX and Beyond

Iterator functions calculate an expression for each row, then aggregate the results |
| [[iterator-performance-pattern.md]] | Iterator Performance Pattern

Iterators (SUMX, AVERAGEX, etc.) process one row at a time, so their cost grows linearly w |
| [[iterator-performance-warning.md]] | Iterator Performance: When SUMX Is Expensive

Iterator functions are powerful but computationally expensive. |
| [[iterator-vs-aggregator-comparison.md]] | Iterator vs Aggregator Comparison

Aggregators (SUM, AVERAGE, COUNT) work directly on a column in the current filter con |
| [[iterators-dax-source.md]] | Iterators in DAX: SUMX, AVERAGEX, RANKX

> Type: article
> Author: Gulab Chand Tejwani
> Published: 2025-09-26
> URL: ht |
| [[json.md]] | JSON

Converts a JSON string into a table. |
| [[kaplan-meier-survival-estimator-dax.md]] | Kaplan-Meier Survival Estimator in DAX

Kaplan-Meier estimates the probability of survival (retention, uptime, etc.) ove |
| [[lcm.md]] | LCM

Applies to: Calculated column Calculated table Measure Visual calculation Returns the least common multiple of inte |
| [[leap-years-and-julian-days-in-dax.md]] | Leap Years and Julian Days in DAX

Handling leap year logic and converting dates to Julian Day Numbers. |
| [[left-right-mid.md]] | LEFT, RIGHT, MID, LEN

Extract or measure text. |
| [[left.md]] | LEFT

Applies to: Calculated column Calculated table Measure Visual calculation Returns the specified number of characte |
| [[len.md]] | LEN

Applies to: Calculated column Calculated table Measure Visual calculation Returns the number of characters in a tex |
| [[linest.md]] | LINEST

Applies to: Calculated column Calculated table Measure Visual calculation Uses the Least Squares method to calcu |
| [[linestx.md]] | LINESTX

Applies to: Calculated column Calculated table Measure Visual calculation Uses the Least Squares method to calc |
| [[ln.md]] | LN

Applies to: Calculated column Calculated table Measure Visual calculation Returns the natural logarithm of a number. |
| [[log.md]] | LOG

Applies to: Calculated column Calculated table Measure Visual calculation Returns the logarithm of a number to the  |
| [[log10.md]] | LOG10

Applies to: Calculated column Calculated table Measure Visual calculation Returns the base-10 logarithm of a numb |
| [[logical-functions-overview.md]] | Logical Functions in DAX

Logical functions test a condition and return a value based on the result. |
| [[logical-functions-switc.md]] | Logical Functions: IF, SWITCH, and Conditionals

Business logic is rarely binary. |
| [[lookup.md]] | LOOKUP

Syntax

```dax
LOOKUP(<expression>, <colref>, <expression>[, <colref>, <expression>]...)
``` |
| [[lookupvalue.md]] | LOOKUPVALUE

Returns the value for the row that meets all criteria specified by one or more search |
| [[lookupwithtotals.md]] | LOOKUPWITHTOTALS

Applies to: Calculated column Calculated table Measure Visual calculation Returns the value or evaluat |
| [[lower-upper-trim.md]] | LOWER, UPPER, TRIM

Transform text casing or remove whitespace. |
| [[lower.md]] | LOWER

Applies to: Calculated column Calculated table Measure Visual calculation Converts all letters in a text string t |
| [[mark-chen.md]] | Mark Chen

DAX and Power BI writer on Medium. |
| [[market-basket-analysis-dax.md]] | Market Basket Analysis in DAX

Identifies which products are purchased together in the same order. |
| [[matchby.md]] | MATCHBY

In window functions, defines the columns that are used to determine how to match data and identify the current  |
| [[math-and-trig-functions-overview.md]] | Math and Trig Functions in DAX

DAX provides a comprehensive set of mathematical and trigonometric functions. |
| [[max-maxa-maxx.md]] | MAX / MAXA / MAXX and MIN / MINA / MINX

Find the largest or smallest value — column-based or iterator-based. |
| [[max.md]] | MAX and MAXX

Returns the largest value in a column or the largest result of an expression evaluated over a table. |
| [[maxa.md]] | MAXA

Applies to: Calculated column Calculated table Measure Visual calculation Returns the largest value in a column. |
| [[maxx.md]] | MAXX

Applies to: Calculated column Calculated table Measure Visual calculation Returns the highest value that results f |
| [[mduration.md]] | MDURATION

Applies to: Calculated column Calculated table Measure Visual calculation Returns the modified Macauley durat |
| [[measure-branching-pattern.md]] | Measure Branching Pattern

Measure branching builds complex KPIs by composing them from simpler, reusable measures — rat |
| [[measure-branching-performance.md]] | Measure Branching and Performance

Measure branching can materially improve DAX query performance. |
| [[measure-branching-source.md]] | Stop Copy-Pasting DAX: The Power of Measure Branching in Power BI

> Type: article
> Author: Gulab Chand Tejwani
> Publi |
| [[measure-library-architecture-pattern.md]] | Measure Library Architecture Pattern

A comprehensive organizational pattern for structuring all DAX measures in a PBIX  |
| [[measure-library-architecture-roi.md]] | Before vs After: Measure Library Architecture ROI

Real-world before/after metrics from Tejwani's team after implementin |
| [[measure-naming-conventions.md]] | Measure Naming Conventions (DAX)

Consistent naming conventions for DAX measures that separate internal/base measures fr |
| [[mid.md]] | MID

Applies to: Calculated column Calculated table Measure Visual calculation Returns a string of characters from the m |
| [[min.md]] | MIN and MINX

Returns the smallest value in a column or the smallest result of an expression evaluated over a table. |
| [[mina.md]] | MINA

Applies to: Calculated column Calculated table Measure Visual calculation Returns the smallest value in a column. |
| [[minute.md]] | MINUTE

Applies to: Calculated column Calculated table Measure Visual calculation Returns the minute as a number from 0  |
| [[minx.md]] | MINX

Applies to: Calculated column Calculated table Measure Visual calculation Returns the lowest value that results fr |
| [[mod.md]] | MOD

Applies to: Calculated column Calculated table Measure Visual calculation Returns the remainder after a number is d |
| [[modified-dietz-return-dax.md]] | Modified Dietz Return in DAX

Modified Dietz measures portfolio return accounting for the timing of cash flows. |
| [[month.md]] | MONTH

Syntax

```dax
MONTH(<datetime>)
```

Remarks

In contrast to Microsoft Excel, which stores dates as serial numbe |
| [[mround.md]] | MRound — Multiple Rounding

Rounds a number to the nearest specified multiple. |
| [[mtbf-mttr-reliability-dax.md]] | MTBF and MTTR in DAX

Mean Time Between Failures and Mean Time to Repair — operational reliability metrics. |
| [[multi-column-aggregation-dax.md]] | Multi-Column Aggregation in DAX

Converting wide, sparse tables into tall, analysis-ready tables using DAX. |
| [[multi-column-aggregation-in-dax.md]] | Multi-column Aggregation in DAX

Aggregating across multiple columns simultaneously when a single-column SUM/COUNT is in |
| [[nameof.md]] | NAMEOF

Summarize this article for me Applies to: Calculated column Calculated table Measure Visual calculation Returns  |
| [[naturalinnerjoin.md]] | NATURALINNERJOIN

Applies to: Calculated column Calculated table Measure Visual calculation Performs an inner join of a  |
| [[naturalleftouterjoin.md]] | NATURALLEFTOUTERJOIN

Applies to: Calculated column Calculated table Measure Visual calculation Performs a join of the L |
| [[nearest-point-dax.md]] | Nearest Point Detection in DAX

Finding the closest location from a list of candidates given an origin point. |
| [[net-promoter-score-nps-dax.md]] | Net Promoter Score (NPS) in DAX

NPS® measures how likely customers are to recommend a product or service. |
| [[net-work-duration-in-dax.md]] | Net Work Duration in DAX

Calculating the time between two timestamps excluding non-working hours. |
| [[networkdays.md]] | NETWORKDAYS

Applies to: Calculated column Calculated table Measure Visual Returns the number of whole workdays between  |
| [[new-dax-functions.md]] | New DAX Functions

DAX is continuously updated with new functions. |
| [[nextweek.md]] | NEXTWEEK

Applies to: Calculated column Calculated table Measure Visual calculation ７ Note This function is discouraged  |
| [[nominal.md]] | NOMINAL

Applies to: Calculated column Calculated table Measure Visual calculation Returns the nominal annual interest r |
| [[nonvisual.md]] | NONVISUAL

Syntax

```dax
NONVISUAL(<expression>)
```

Remarks

Marks a value filter in SUMMARIZECOLUMNS as not affectin |
| [[not-in-pattern.md]] | NOT IN in DAX

DAX does not have a NOT IN operator. |
| [[not.md]] | NOT

Changes FALSE to TRUE, or TRUE to FALSE. |
| [[now.md]] | NOW

Applies to: Calculated column Calculated table Measure Visual calculation Returns the current date and time in date |
| [[nper.md]] | NPER

Applies to: Calculated column Calculated table Measure Visual calculation Returns the number of periods for an inv |
| [[odd.md]] | ODD

Applies to: Calculated column Calculated table Measure Visual calculation Returns number rounded up to the nearest  |
| [[offset.md]] | OFFSET

Applies to: Calculated column Calculated table Measure Visual calculation Returns a single row that is positione |
| [[on-time-in-full-otif-dax.md]] | On Time In Full (OTIF)

Purpose

OTIF is a supply-chain logistics KPI that measures order fulfillment quality
on two dim |
| [[or.md]] | OR

Syntax

```dax
OR(<logical1>,<logical2>)
```

Remarks

The OR function in DAX accepts only two (2) arguments. |
| [[order-cycle-time-oct-dax.md]] | Order Cycle Time (OCT) in DAX

The elapsed time from order placement to order receipt/fulfillment. |
| [[ordnance-survey-grid-in-dax.md]] | Ordnance Survey Grid in DAX

Converting UK Ordnance Survey National Grid references to lat/long. |
| [[overall-equipment-effectiveness-oee-dax.md]] | Overall Equipment Effectiveness (OEE)

Purpose

OEE is the standard manufacturing KPI for measuring how efficiently equi |
| [[parent-child-functions.md]] | Parent-Child Functions: PATH, PATHITEM, PATHLENGTH

Work with self-referencing hierarchies where each row contains a ref |
| [[path.md]] | PATH

Applies to: Calculated column Calculated table Measure Visual calculation Returns a delimited text string with the |
| [[pathitem.md]] | PATHITEM

Applies to: Calculated column Calculated table Measure Visual calculation Returns the item at the specified po |
| [[pathitemreverse.md]] | PATHITEMREVERSE

Applies to: Calculated column Calculated table Measure Visual calculation Returns the item at the speci |
| [[pathlength.md]] | PATHLENGTH

Applies to: Calculated column Calculated table Measure Visual calculation Returns the number of parents to t |
| [[pattern-1-measure-branching.md]] | Pattern 1: Measure Branching

See measure-branching-pattern for the full pattern description. |
| [[pattern-2-defensive-dax.md]] | Pattern 2: Defensive DAX

Every measure that performs division, references a measure that might be BLANK, or depends on  |
| [[pattern-4-single-source-of-truth.md]] | Pattern 4: Single Source of Truth

Every business concept has exactly ONE measure that defines it. |
| [[pattern-5-validation-loop.md]] | Pattern 5: Validation Loop

Test measures are created for every base measure to verify the calculation is correct before |
| [[pduration.md]] | PDURATION

Applies to: Calculated column Calculated table Measure Visual calculation Returns the number of periods requi |
| [[performance-first-measure-design.md]] | Performance-First Measure Design: Variables and Iterator Awareness

Correct DAX that takes 4 minutes to calculate might  |
| [[phone-number-formatting-in-dax.md]] | Phone Number Formatting in DAX

Cleaning and formatting phone numbers from raw inconsistent input. |
| [[pi.md]] | PI

Applies to: Calculated column Calculated table Measure Visual calculation Returns the value of Pi, 3.14159265358979, |
| [[pmt.md]] | PMT

Applies to: Calculated column Calculated table Measure Visual calculation Calculates the payment for a loan based o |
| [[poisson.dist.md]] | POISSON.DIST

Applies to: Calculated column Calculated table Measure Visual calculation Returns the Poisson distribution |
| [[power-log-exp.md]] | POWER, LOG, LOG10, EXP, PI

Exponentials, logarithms, and constants. |
| [[power.md]] | POWER

Applies to: Calculated column Calculated table Measure Visual calculation Returns the result of a number raised t |
| [[ppmt.md]] | PPMT

Applies to: Calculated column Calculated table Measure Visual calculation Returns the payment on the principal for |
| [[previous-next-period.md]] | PREVIOUS / NEXT: Day, Week, Month, Quarter, Year

Move the date filter backward or forward by one standard period. |
| [[previous-period-year-quarter-week.md]] | Previous Period/Year/Quarter/Week

Calculating the previous period value using the No CALCULATE approach. |
| [[previousweek.md]] | PREVIOUSWEEK

Applies to: Calculated column Calculated table Measure Visual calculation ７ Note This function is discoura |
| [[product-productx.md]] | PRODUCT and PRODUCTX

Multiply all values in a column or expression to return the product. |
| [[product.md]] | PRODUCT

Applies to: Calculated column Calculated table Measure Visual calculation Returns the product of the numbers in |
| [[productx.md]] | PRODUCTX

Applies to: Calculated column Calculated table Measure Visual calculation Returns the product of an expression |
| [[project-burndown-chart-dax.md]] | Project Burndown Chart in DAX

Burndown charts visualize cumulative work remaining vs an idealized linear burndown. |
| [[pv.md]] | PV

Calculates the present value of a loan or an investment, based on a constant interest rate. |
| [[quality-rate-defect-dax.md]] | Quality Rate in DAX

Manufacturing quality metric: good units produced as a percentage of total units started. |
| [[quarter.md]] | QUARTER

Syntax

```dax
QUARTER(<date>)
```

Remarks

If the input value is BLANK, the output value is also BLANK. |
| [[quotient.md]] | QUOTIENT

Applies to: Calculated column Calculated table Measure Visual calculation Performs division and returns only t |
| [[radians.md]] | RADIANS

Applies to: Calculated column Calculated table Measure Visual calculation Converts degrees to radians. |
| [[rand.md]] | RAND

Applies to: Calculated column Calculated table Measure Visual calculation Returns a random number greater than or  |
| [[randbetween.md]] | RANDBETWEEN

Applies to: Calculated column Calculated table Measure Visual calculation Returns a random number in the ra |
| [[range.md]] | RANGE

Applies to: Calculated column Calculated table Measure Visual calculation Returns an interval of rows within the  |
| [[rank-subtraction-grouping-trick.md]] | Rank Subtraction Grouping Trick

The core DAX insight behind Gaps and Islands streak detection: subtracting a chronologi |
| [[rank.eq.md]] | RANK.EQ

Returns the ranking of a number in a list of numbers. |
| [[rank.md]] | RANK

Returns the ranking for the current context within the specified partition, sorted by the specified order. |
| [[ranking-patterns.md]] | Ranking Patterns in DAX

DAX provides multiple ways to rank data: RANKX, RANK, and ROWNUMBER. |
| [[rate.md]] | RATE

Applies to: Calculated column Calculated table Measure Visual calculation Returns the interest rate per period of  |
| [[received.md]] | RECEIVED

Applies to: Calculated column Calculated table Measure Visual calculation Returns the amount received at matur |
| [[regression-analysis-in-dax.md]] | Regression Analysis in DAX

Implementing simple and multiple linear regression using DAX iterators. |
| [[replace.md]] | REPLACE

Applies to: Calculated column Calculated table Measure Visual calculation REPLACE replaces part of a text strin |
| [[rept.md]] | REPT

Applies to: Calculated column Calculated table Measure Visual calculation Repeats text a given number of times. |
| [[return.md]] | RETURN

Returns the result of a table expression from a DAX query or a DEFINE FUNCTION body. |
| [[right.md]] | RIGHT

Applies to: Calculated column Calculated table Measure Visual calculation RIGHT returns the last character or cha |
| [[role-playing-dimensions-pattern.md]] | Role-Playing Dimensions: Single Date Table vs Duplicated

When a fact table has multiple date columns (e.g., InvoiceDate |
| [[rolling-periods-in-dax.md]] | Rolling Periods in DAX

Computing rolling sums, averages, or counts over a sliding time window. |
| [[rollup.md]] | ROLLUP

Syntax

```dax
ROLLUP ( <groupBy_columnName> [, <groupBy_columnName> [, … ] ] )
SUMMARIZE(<table>, <groupBy_colu |
| [[rollupgroup.md]] | ROLLUPGROUP

Applies to: Calculated column Calculated table Measure Visual Modifies the behavior of the SUMMARIZE and SU |
| [[rollupissubtotal.md]] | ROLLUPISSUBTOTAL

Applies to: Calculated column Calculated table Measure Visual calculation Pairs rollup groups with the |
| [[round-trunc-int.md]] | Rounding: ROUND, ROUNDDOWN, ROUNDUP, TRUNC, INT

Control decimal precision and truncation. |
| [[round.md]] | ROUND

Syntax

```dax
ROUND(<number>, <num_digits>)
```

Remarks

If num_digits is greater than 0 (zero), then number is |
| [[rounddown.md]] | ROUNDDOWN

Applies to: Calculated column Calculated table Measure Visual Rounds a number down, toward zero. |
| [[roundup.md]] | ROUNDUP

Applies to: Calculated column Calculated table Measure Visual Rounds a number up, away from 0 (zero). |
| [[rownumber.md]] | ROWNUMBER

Applies to: Calculated column Calculated table Measure Visual calculation Returns the unique ranking for the  |
| [[rri.md]] | RRI

Applies to: Calculated column Calculated table Measure Visual calculation Returns an equivalent interest rate for t |
| [[sales-measure-library-coding-challenge.md]] | Sales Measure Library Coding Challenge

Hands-on exercise building a production-ready DAX sales analytics measure librar |
| [[sample.md]] | SAMPLE

Applies to: Calculated column Calculated table Measure Visual calculation Returns a sample of N rows from the sp |
| [[search-find.md]] | SEARCH and FIND

Find the position of one text string inside another. |
| [[search.md]] | SEARCH — Case-insensitive Text Search

Returns the starting position of a substring within a text string. |
| [[second.md]] | SECOND

Applies to: Calculated column Calculated table Measure Visual calculation Returns the seconds of a time value, a |
| [[selectcolumns.md]] | SELECTCOLUMNS — Column Selection

Adds or selects columns from a table expression. |
| [[shipping-delay-dax.md]] | Shipping Delay: Real-World Role-Playing Example

The source article's practical example: calculating the average number  |
| [[sign.md]] | SIGN

Applies to: Calculated column Calculated table Measure Visual calculation Determines the sign of a number, the res |
| [[simple-linear-regression-in-dax.md]] | Simple Linear Regression in DAX

Calculating trend lines and predictions using linear regression formulas. |
| [[sin.md]] | SIN

Applies to: Calculated column Calculated table Measure Visual calculation Returns the sine of the given angle. |
| [[sinh.md]] | SINH

Applies to: Calculated column Calculated table Measure Visual calculation Returns the hyperbolic sine of a number. |
| [[skip-keyword.md]] | SKIP — Exclude from Sort

Excludes specific rows from ORDER BY ordering without removing them from the result. |
| [[sln.md]] | SLN

Applies to: Calculated column Calculated table Measure Visual calculation Returns the straight-line depreciation of |
| [[sqrt.md]] | SQRT

Applies to: Calculated column Calculated table Measure Visual calculation Returns the square root of a number. |
| [[sqrtpi.md]] | SQRTPI

Applies to: Calculated column Calculated table Measure Visual calculation Returns the square root of (number  pi |
| [[startof-endof.md]] | STARTOF / ENDOF: Week, Month, Quarter, Year

Return the first or last date of the current context period. |
| [[startofmonth.md]] | STARTOFMONTH

Applies to: Calculated column Calculated table Measure Visual calculation ７ Note This function is discoura |
| [[startofquarter.md]] | STARTOFQUARTER

Applies to: Calculated column Calculated table Measure Visual calculation ７ Note This function is discou |
| [[startofweek.md]] | STARTOFWEEK

Applies to: Calculated column Calculated table Measure Visual calculation ７ Note This function is discourag |
| [[startofyear.md]] | STARTOFYEAR

Applies to: Calculated column Calculated table Measure Visual calculation ７ Note This function is discourag |
| [[static-vs-dynamic-aggregations.md]] | Static vs Dynamic Aggregations: When to Use Each

The decision between Power Query and DAX often comes down to one quest |
| [[statistical-functions-overview.md]] | Statistical Functions in DAX

DAX includes aggregation, standard deviation, variance, and distribution functions. |
| [[storage-engine-vs-formula-engine-in-dax.md]] | Storage Engine vs Formula Engine in DAX

Understanding the two processing engines that execute DAX queries. |
| [[streak-detection-in-dax.md]] | Streak Detection in DAX

Identifying consecutive runs of TRUE values or repeating patterns in a sequence. |
| [[streak-leaderboard-top-n-users.md]] | Streak Leaderboard — Top-N Users by Longest Consecutive Active Days

Combining the Gaps and Islands streak algorithm wit |
| [[sum.md]] | SUM

Signature

```dax
SUM(<column>)
```

Parameters

| Parameter | Description |
|-----------|-------------|
| `<column |
| [[sumx-vs-sum-gotcha.md]] | SUMX on a Single Column: The 27x Performance Anti-Pattern

Pattern: Using SUMX to iterate over a table and sum a single  |
| [[sumx.md]] | SUMX Function

Iterates over a table row-by-row, evaluates an expression for each row, then sums the results. |
| [[svg-star-rating-dax.md]] | SVG Star Rating in DAX

Purpose

DAX can generate Scalable Vector Graphics (SVG) — text-based, resolution-independent
im |
| [[syd.md]] | SYD

Applies to: Calculated column Calculated table Measure Visual calculation Returns the sum-of-years' digits deprecia |
| [[t.dist.2t.md]] | T.DIST.2T

Syntax

```dax
T.DIST.2T(X,Deg_freedom)
```

Remarks

This function is not supported for use in DirectQuery m |
| [[t.dist.md]] | T.DIST

Applies to: Calculated column Calculated table Measure Visual calculation Returns the Student's left-tailed t-di |
| [[t.dist.rt.md]] | T.DIST.RT

Applies to: Calculated column Calculated table Measure Visual calculation Returns the right-tailed Student's  |
| [[t.inv.2t.md]] | T.INV.2T

Syntax

```dax
T.INV.2T(Probability,Deg_freedom)
```

Remarks

This function is not supported for use in Direc |
| [[t.inv.md]] | T.INV

Applies to: Calculated column Calculated table Measure Visual calculation Returns the left-tailed inverse of the  |
| [[tan.md]] | TAN

Applies to: Calculated column Calculated table Measure Visual Returns the tangent of the given angle. |
| [[tanh.md]] | TANH

Applies to: Calculated column Calculated table Measure Visual calculation Returns the hyperbolic tangent of a numb |
| [[tejwani-5000-dax-measures-performance-source.md]] | Tejwani — 5,000 DAX Measures Performance Analysis

Empirical study of 5,247 DAX measures across 89 production reports. |
| [[tejwani-dax-content-critique-source.md]] | DAX Best Practice Critique — Tejwani

Meta-level: stop writing "10 tips" DAX posts because patterns without context are  |
| [[tewjani-5-dax-patterns-source.md]] | The 5 DAX Patterns Senior Analysts Use — Tejwani

> Type: architectural guide / intermediate
> Author: Gulab Chand Tejwa |
| [[tewjani-dax-content-critique-source.md]] | DAX Best Practice Critique — Tejwani

Meta-level: stop writing "10 tips" DAX posts because patterns without context are  |
| [[tewjani-measure-branching-source.md]] | Measure Branching in Power BI — Gulab Chand Tejwani

> Type: pattern guide / beginner
> Author: Gulab Chand Tejwani
> Pu |
| [[tewjani-role-playing-dimensions-source.md]] | Role-Playing Dimensions in DAX — Gulab Chand Tejwani

> Type: pattern guide / beginner
> Author: Gulab Chand Tejwani
> P |
| [[tewjani-time-intelligence-source.md]] | Time Intelligence in DAX — Tejwani

> Type: time intelligence guide / beginner
> Author: Gulab Chand Tejwani
> Published |
| [[tewjani-treatas-source.md]] | TREATAS in DAX — Tejwani

> Type: virtual relationship technique / intermediate
> Author: Gulab Chand Tejwani
> Publishe |
| [[the-dax-concepts-that-actually-save-you-time-source.md]] | The DAX Concepts that Actually Save You Time in Power BI

A Medium article by Daniel Olatunji targeting analysts who hav |
| [[time-intelligence-common-mistakes.md]] | Time Intelligence: Common Mistakes

Time intelligence is powerful but has three sharp edges that catch most beginners. |
| [[time-intelligence-functions-overview.md]] | Time Intelligence Functions Overview

Time intelligence functions perform calculations over date ranges: year-to-date, p |
| [[time-intelligence-functions.md]] | Time Intelligence Functions

Time intelligence is where DAX delivers the most business value — comparing periods, calcul |
| [[time-intelligence-source.md]] | Time Intelligence in DAX: The Secret Behind YTD, QTD, and SamePeriodLastYear

> Type: article
> Author: Gulab Chand Tejw |
| [[time-intelligence-star-schema.md]] | Time Intelligence Star Schema: Single Date Dimension

Build one central Date table and relate every fact table to it. |
| [[time-warping-in-dax.md]] | Time Warping in DAX

Projecting a measure onto a different time axis — for example, mapping all events to "Day 1, Day 2, |
| [[time-zones-in-dax.md]] | Time Zones in DAX

Converting UTC timestamps to local time and handling multi-timezone reporting. |
| [[time.md]] | TIME

Applies to: Calculated column Calculated table Measure Visual calculation Converts hours, minutes, and seconds giv |
| [[timevalue.md]] | TIMEVALUE

Applies to: Calculated column Calculated table Measure Visual calculation Converts a time in text format to a |
| [[timezone-conversions-dax.md]] | Timezone Conversion in DAX

Converts a source time from one timezone to multiple destination timezones using UTC as the  |
| [[today-now.md]] | TODAY, NOW, UTCTODAY, UTCNOW

Return the current date and/or time. |
| [[today.md]] | TODAY

Applies to: Calculated column Calculated table Measure Visual calculation Returns the current date. |
| [[tojson.md]] | TOJSON

Applies to: Calculated column Calculated table Measure Visual Returns a table as a string using JSON format. |
| [[top-n-others-union-pattern.md]] | Top N + Others Union Pattern

Combine a Top N group and an "Others" group into a single bar chart row, using `UNION` to  |
| [[top-n-parameter-slicer-pattern.md]] | Top N Parameter Slicer Pattern

Let users pick the N value (Top 5, Top 10, Top 15) from a slicer instead of hardcoding i |
| [[topn.md]] | TOPN

Applies to: Calculated column Calculated table Measure Visual calculation Returns the top N rows of the specified  |
| [[transitive-closure-dax.md]] | Transitive Closure in DAX

Finding all pairs of entities within a given distance threshold — a graph connectivity proble |
| [[transitive-closure-in-dax.md]] | Transitive Closure in DAX

Finding all reachable nodes in a network/hierarchy, even when direct relationships don't exis |
| [[treatas-dynamic-segmentation-pattern.md]] | TREATAS Dynamic Segmentation Pattern

Uses TREATAS to apply a parameter table's selected values as a filter to a fact ta |
| [[treatas-dynamic-segments-whatif.md]] | TREATAS for Dynamic Segments and What-If Scenarios

TREATAS can create dynamic segment selectors and what-if analyses —  |
| [[treatas-function.md]] | TREATAS Function

Applies a set of values from one expression as a filter to a target column — without requiring an acti |
| [[treatas-in-dax-source.md]] | TREATAS in DAX: Connecting Unrelated Tables Like Magic

> Type: article
> Author: Gulab Chand Tejwani
> Published: 2025- |
| [[treatas-performance-pitfalls.md]] | TREATAS: Performance and Pitfalls

TREATAS re-creates filter maps on every measure evaluation — not free. |
| [[treatas-strictness-gotcha.md]] | TREATAS Strictness — Data Type Alignment and Blank Handling

TREATAS silently fails or produces unexpected results when  |
| [[trim.md]] | TRIM

Applies to: Calculated column Calculated table Measure Visual calculation Removes all spaces from text except for  |
| [[trimmean.md]] | TRIMMEAN — Trimmed Mean

Returns the mean of the interior of a data set after excluding a percentage from the top and bo |
| [[true.md]] | TRUE

Applies to: Calculated column Calculated table Measure Visual calculation Returns the logical value TRUE. |
| [[trunc-int.md]] | TRUNC / INT — Truncation Functions

Removes the decimal portion of a number, returning the integer part. |
| [[trunc-vs-int-dax.md]] | TRUNC vs INT: The Negative Number Bug

For positive numbers, `TRUNC` and `INT` behave identically — both return the inte |
| [[trunc.md]] | TRUNC

Applies to: Calculated column Calculated table Measure Visual calculation Truncates a number to an integer by rem |
| [[udf-lambda-syntax.md]] | DAX UDF / Lambda Syntax

DAX User-Defined Functions (UDFs) allow parameterized reusable expressions within DEFINE FUNCTI |
| [[udfs-dont-automatically-improve-performance.md]] | UDFs Don't Automatically Improve Performance

A UDF is a reusable expression, not a performance shortcut. |
| [[udfs-dont-fix-the-model.md]] | UDFs Don't Fix the Model

Wrapping broken DAX in a named function does not fix the underlying semantic model. |
| [[udfs-vs-copy-paste-pattern.md]] | UDFs vs Copy-Paste Pattern

UDFs eliminate the primary failure mode of copy-paste: silent, independent drift of duplicat |
| [[unicode.md]] | UNICODE

Applies to: Calculated column Calculated table Measure Visual calculation Returns the number (code point) corre |
| [[union-intersect-except.md]] | UNION, INTERSECT, EXCEPT

Set operations on tables. |
| [[union.md]] | UNION — Combine Tables

Stacks two or more tables vertically, keeping all rows. |
| [[unix-times-in-dax.md]] | Unix Times in DAX

Converting Unix timestamps (seconds/milliseconds since 1970-01-01) to datetime. |
| [[unnecessary-iterator-pattern.md]] | Unnecessary Iterator Pattern

Using SUMX/AVERAGEX/COUNTX/MAXX/MINX to aggregate a single column that already exists — wh |
| [[upper.md]] | UPPER

Applies to: Calculated column Calculated table Measure Visual calculation Converts a text string to all uppercase |
| [[userculture.md]] | USERCULTURE

Applies to: Calculated column Calculated table Measure Visual calculation Returns the locale (language code |
| [[username.md]] | USERNAME

Applies to: Calculated column Calculated table Measure Visual calculation Returns the domain name and username |
| [[userobjectid.md]] | USEROBJECTID

Applies to: Calculated column Calculated table Measure Visual calculation Returns the current user's Objec |
| [[userprincipalname.md]] | USERPRINCIPALNAME

Applies to: Calculated column Calculated table Measure Visual calculation Returns the user principal  |
| [[utcnow.md]] | UTCNOW

Applies to: Calculated column Calculated table Measure Visual calculation Returns the current UTC date and time. |
| [[utctoday.md]] | UTCTODAY

Applies to: Calculated column Calculated table Measure Visual calculation Returns the current UTC date. |
| [[val-vs-expr-parameter-evaluation.md]] | VAL vs EXPR Parameter Evaluation Modes

Every UDF parameter has an evaluation mode. |
| [[value.md]] | VALUE

Converts a text string representing a number into a numeric value. |
| [[values.md]] | VALUES

Signature

```dax
VALUES(<TableNameOrColumn>)
```

Parameters

| Parameter | Description |
|-----------|-------- |
| [[vdb.md]] | VDB

Applies to: Calculated column Calculated table Measure Visual calculation Returns the depreciation of an asset for  |
| [[weekday-weeknum-yearfrac.md]] | WEEKDAY, WEEKNUM, YEARFRAC

Extract day-of-week, week number, or fractional year between two dates. |
| [[weekday.md]] | WEEKDAY

Applies to: Calculated column Calculated table Measure Visual calculation Returns a number from 1 to 7 identify |
| [[weeknum.md]] | WEEKNUM

Applies to: Calculated column Calculated table Measure Visual calculation Returns the week number for the given |
| [[when-measure-library-architecture-is-essential.md]] | When Measure Library Architecture Is Essential

Decision framework for when the 4-layer DAX measure library architecture |
| [[why-stopped-dax-best-practice-source.md]] | Why I Stopped Writing "Best Practice" DAX Posts

> Type: article
> Author: Gulab Chand Tejwani
> Published: 2025-06-30
> |
| [[window-functions-overview.md]] | Window Functions Overview

Window functions operate over a set of rows defined by an ORDERBY clause. |
| [[window.md]] | WINDOW

Applies to: Calculated column Calculated table Measure Visual calculation Returns multiple rows which are positi |
| [[x-aggregators-sumx-minx-maxx.md]] | X Aggregators: SUMX, MINX, MAXX, AVERAGEX

Iterator functions that take a table (or table expression) as their first arg |
| [[xirr.md]] | XIRR

Applies to: Calculated column Calculated table Measure Visual calculation Returns the internal rate of return for  |
| [[xnpv.md]] | XNPV

Applies to: Calculated column Calculated table Measure Visual calculation Returns the present value for a schedule |
| [[year.md]] | YEAR

Applies to: Calculated column Calculated table Measure Visual calculation Returns the year of a date as a four dig |
| [[yearfrac.md]] | YEARFRAC

Applies to: Calculated column Calculated table Measure Visual calculation Calculates the fraction of the year  |

| [[calendar-dax.md]] | CALENDAR — DAX Date Table Generator

Returns a single-column date table between a start and end date |
| [[calendarauto-dax.md]] | CALENDARAUTO — DAX Auto Date Table

Auto-generates a date table covering all dates in the model |
| [[dynamic-pl-measure.md]] | Dynamic P&L Measure

Single Matrix measure handling both detail accounts and calculated subtotals via conditional row-type detection |
| [[ytd-kpi-measures-pl.md]] | YTD KPI Measures for P&L Dashboard

TOTALYTD measures: Total YTD Revenue, Gross Profit, Operating Profit (value + %), Net Profit |
| [[selector-datatable-disconnected-table.md]] | Selector DATATABLE (Disconnected Helper Table)

DATATABLE literal with Category + Sort Order in same call; separate column creates circular dependency |
| [[position-measures-stacked-chart.md]] | Position Measures (Position 1-N)

Position 1 = selected via SELECTEDVALUE; Position k via rank arithmetic TargetRank = IF(k<SelRank,k,k+1) |
| [[circular-dependency-datatable-gotcha.md]] | Circular Dependency — DATATABLE Sort Column Gotcha

Separate Sort Order calculated column reads Category -> circular dependency; fix: same DATATABLE with literals |
| [[movingaverage-visual-calc.md]] | MOVINGAVERAGE (Visual Calculation)

Rolling window average within a visual; current row + N-1 preceding rows; visual-level scope vs model measures |
| [[isatlevel-guard-pattern.md]] | ISATLEVEL Guard Pattern

Returns TRUE at specified hierarchy level only; prevents misleading values at rollup rows; use with MOVINGAVERAGE/RUNNINGSUM |
| [[format-visual-calc-returns-text.md]] | FORMAT in Visual Calculations — Returns Text

FORMAT() converts numeric output to text; breaks sorting and numeric downstream calculations; format in visual pane instead |
| [[non-additive-measures-audit.md]] | Non-Additive Measures Audit

Detect non-additive fields via information_schema query; replace with additive components; semantic layer fix speeds queries 14sec to 1.2sec |
| [[calculation-items-apply-only-to-measure-references.md]] | Calculation Items Apply Only to Measure References

CG items activate only on direct measure references — silently skipped on constants and non-measure expressions.
| [[cg-precedence-application-not-evaluation.md]] | CG Precedence = Application Order, Not Evaluation Order

Higher precedence CG applies first — controls transformation chain, not evaluation stack.
| [[report-filter-vs-measure-cg-behaviour.md]] | Report Filter vs Measure: Different CG Application Behaviour

Same CG produces different results depending on report filter vs measure invocation — precedence governs only in report filter path.
| [[nested-calculate-does-not-change-cg-application-order.md]] | Nested CALCULATE Does Not Change CG Application Order

Nesting CALCULATE with CG args cannot override precedence — the CG fires following precedence regardless.
| [[measure-that-applies-cg-overrides-precedence.md]] | Measure That Applies a CG Overrides Precedence

A measure with CALCULATE + CG internally fires that CG at measure evaluation time, bypassing precedence.
| [[avoiding-pitfalls-calculation-groups-precedence-ferrari-source.md]] | Avoiding Pitfalls in Calculation Groups Precedence (Ferrari)

Detect non-additive fields via information_schema query; replace with additive components; semantic layer fix speeds queries 14sec to 1.2sec |
| [[measure-branching-naming-conventions.md]] | Measure Branching Naming Conventions

Use [[calculation-items-apply-only-to-measure-references]] pattern — name the branch target, not the modifier — for measures that apply CGs internally.

|| Note | Description |
||------|-------------|
|| [[max-date-pattern-rolling-window.md]] | Max Date Pattern (Rolling 7-Day Window)

Using MAX(DateColumn) as a dynamic anchor for rolling N-day windows — the foundation for all rolling-period measures |
|| [[emoji-in-dax-string-concatenation.md]] | Emoji in DAX String Concatenation

DAX handles Unicode emoji in string literals correctly at expression level; rendering issues are a Power BI visual limitation, not a DAX limitation |
|| [[datesinperiod-rolling-12-month-window.md]] | DATESINPERIOD Rolling 12-Month Window

DATESINPERIOD for rolling N-month windows: anchor via StartDate, sign of Number controls direction — compared to Max Date rolling window pattern |

## Measures — Dynamic KPI Card (Bittar, 2025)

|| Note | Description |
||------|-------------|
|| [[ot-hours.md]] | OT Hours

SUM over OvertimeHours — the base aggregation for all OT metrics |
|| [[employee-count.md]] | Employee Count

DISTINCTCOUNT over EmployeeID — denominator for per-capita OT metrics |
|| [[ot-hours-per-fte.md]] | OT Hours per FTE

DIVIDE([OT Hours], [Employee Count]) — base per-capita OT metric |
|| [[ot-hours-per-fte-this-week.md]] | OT Hours per FTE This Week

Rolling 7-day OT per FTE using CALCULATE + FILTER with Max Date anchor |
|| [[ot-hours-per-fte-last-week.md]] | OT Hours per FTE Last Week

Prior-week OT per FTE: same window shifted 7 days back |
|| [[ot-hours-per-fte-variance.md]] | OT Hours per FTE Variance

Simple subtraction of This Week minus Last Week |
|| [[ot-hours-per-fte-variance-pct.md]] | OT Hours per FTE Variance %

DIVIDE(variance, Last Week) — week-over-week % change |
|| [[ot-hours-this-week.md]] | OT Hours This Week

Total OT hours in last 7 days (absolute, not per FTE) |
|| [[high-ot-employees-last-7-days.md]] | High OT Employees (Last 7 Days)

COUNTROWS of ADDCOLUMNS(SUMMARIZE) filtered by threshold — per-employee OT aggregation |
|| [[highlight-headers.md]] | Highlight Headers

SWITCH on SELECTEDVALUE(Highlights[Order]) — maps button order to formatted highlight text |
|| [[column-value.md]] | Column Value

SWITCH on SELECTEDVALUE(Highlights[Order]) — drives which metric the chart displays |
|| [[column-color.md]] | Column Color

SWITCH(TRUE()) on highlight order + threshold comparisons — returns hex color names |
|| [[graph-title.md]] | Graph Title

SWITCH on SELECTEDVALUE(Highlights[Order]) — static strings for chart title |
|| [[graph-subtitle.md]] | Graph Subtitle

SWITCH on SELECTEDVALUE(Highlights[Order]) — delegates to per-highlight subtitle measures |

## Measures — Chart Label Formatting (Bittar, 2025)

|| Note | Description |
||------|-------------|
|| [[turnover-rate.md]] | Turnover Rate

DATESINPERIOD 12-month rolling turnover rate: DIVIDE(CALCULATE(Leavers), CALCULATE(Headcount)) |
|| [[turnover-rate-last-month.md]] | Turnover Rate Last Month

Prior period rolling 12-month rate: EOMONTH(MaxDate,-1) as DATESINPERIOD anchor |
|| [[turnover-rate-variance.md]] | Turnover Rate Variance

Turnover Rate minus Turnover Rate Last Month — negative = improvement |
|| [[turnover-variance-positive.md]] | Turnover Variance_Positive

IF(Variance < 0, Variance) — dummy series for favorable outcome (turnover down) |
|| [[turnover-variance-negative.md]] | Turnover Variance_Negative

IF(Variance >= 0, Variance) — dummy series for unfavorable outcome (turnover up/flat) |
|| [[label-variance.md]] | Label Variance

IF + FORMAT + ↑↓ arrow prefix — formatted variance string for chart label |
|| [[label-color-constants.md]] | Label Color Constants

Hex color constants (#31D286, #F05660, #79797C) for label font/background formatting |

## Measures — Chart Data Labels (Bittar, 2024)

|| Note | Description |
||------|-------------|
|| [[maximum-date.md]] | Maximum Date

MAX over date column — dynamic anchor for current-period measures; adapts on every data refresh |
|| [[process-duration.md]] | Process Duration (Current Month)

CALCULATE + FILTER on MaxDate — sums process duration days for the current period |
|| [[date-last-month.md]] | Date Last Month

EDATE([Maximum Date], -1) — prior period anchor, shared across branching measures |
|| [[process-duration-previous-month.md]] | Process Duration Previous Month

CALCULATE + FILTER on Date Last Month — prior period duration using the shared anchor measure |
|| [[process-duration-variation.md]] | Process Duration Variation

Current minus prior — base variance; negative = improvement (duration decreased) |
|| [[formatted-process-duration-variation.md]] | Formatted Process Duration Variation

SWITCH(TRUE()) + string concatenation with ±sign and pluralized day/days |
|| [[color-process-duration-variation.md]] | Color Process Duration Variation (Hex Constants)

IF on variation sign → hex color string; green for decrease, red for increase |
|| [[maximum-value-y-axis-headroom.md]] | Maximum Value (Y-Axis Headroom)

MAXX(ALL, measure) + 35% padding — prevents data label overlap by expanding Y-axis scale |
|| [[color-vacancy-rate-variation.md]] | Color Vacancy Rate Variation (IF on KPI Variance Sign)

IF(variance > 0, [Color Dark Red], [Color Dark Green]) — conditional hex for KPI detail sub-values; applied via measure fx, not visual color fx |

## Patterns — SVG Pills via UDF (Bittar, 2025)

|| Note | Description |
||------|-------------|
|| [[svg-pill-two-udf-architecture.md]] | SVG Pill — Two-UDF Architecture

Two-udf pattern: UDF_EncodeSVG (url-encoding) + UDF_SVGPillCanvas (drawing); UDFs own geometry, measures own semantics |
|| [[udf-encodesvg.md]] | UDF_EncodeSVG — URL-Encode Raw SVG String

SUBSTITUTE chain for %, #, <, >, ", ', space, :, /, ?, =, & → data:image/svg+xml;utf8 prefix; called as final step inside every SVG-drawing UDF |
|| [[udf-svgpillcanvas.md]] | UDF_SVGPillCanvas — Draw SVG Pill (Rect + Dot + Text)

7-param function: label, bgColor, borderColor, textColor, showBorder(0/1), dotColor, showDot(0/1); canvas 200×28px, pill 24px tall, 12px corner radius |
|| [[task-status-pill-svg.md]] | Task Status Pill — SELECTEDVALUE + Color Maps → UDF Call

SELECTEDVALUE(Tasks[Status]) → dedicated color measures → UDF_SVGPillCanvas(showBorder=1, showDot=0); bg color carries status signal |
|| [[task-priority-pill-svg.md]] | Task Priority Pill — Neutral Pill + Dot Color Carries Signal

SELECTEDVALUE(Tasks[Priority]) + SWITCH on dotColor; neutral pill (white bg), showDot=1, dot color carries priority signal (High→dark red, Medium→amber, Low→green) |

## Patterns — KPI Colors via UDF (Bittar, 2025)

|| Note | Description |
||------|-------------|
|| [[kpi-color-palette-as-dax-measures.md]] | KPI Color Palette: Colors as DAX Measures (Theme-Agnostic)

Five baseline measures: _Color Dark/Light Green/Red + _Color Text Secondary; palette as measures enables copy-paste and theme independence |
|| [[statuscolorpct-udf-architecture.md]] | StatusColorPct — Three-Parameter Architecture

UDF with _value (metric), _inverse (directionality), _mode (font/background); normalize + SWITCH(TRUE()) pattern |
|| [[statuscolorpct.md]] | StatusColorPct — Conditional Hex Color for KPI Indicators

DEFINE FUNCTION StatusColorPct(_value, _inverse, _mode): IF(_inverse, -_value, _value) → SWITCH branches returning palette measures by mode |
|| [[inverse-flag-metric-type-kpi-colors.md]] | Metric-Specific Inverse Flag in KPI Color UDFs

_inverse=FALSE for income (higher=green); _inverse=TRUE for expenses/vacancy (higher=red); same UDF, different calls |
|| [[kpi-color-font-background-one-liners.md]] | One-Liner UDF Call per Color Property (Font + Background)

Two calls per metric: Font Color X = StatusColorPct(value, inverse, "Font") and Background Color X = StatusColorPct(value, inverse, "Background") |

## Functions — UDF Library (Bittar, 2025)

|| Note | Description |
||------|-------------|
|| [[udf-10-must-have-catalog.md]] | UDF Hub: 10 Must-Have DAX UDFs (Bittar, 2025)

Catalog of 14 UDFs: CompareOverPeriodRange, VarAbs, StatusColor, AutoDateTable, RollingTotal, RollingAverage, PercentileBoundsCustom, BucketLabelFromBounds, SparklineSVG_LastNDays, TopNWithinCurrentGroup, RankWithinCurrentGroup, NarrativeTopChangeCore, NormalizeLabel, Humanize, HumanizeWithDecimals |
|| [[compareoverperiodrange.md]] | CompareOverPeriodRange — Whole-Period Time Comparison (YoY/QoQ/MoM/WoW/DoD)

MAX('Date'[Date]) anchor; DATESBETWEEN for current/prior periods; mode=VALUE/DELTA/PCT; config: date table column |
|| [[varabs-statuscolor-udfs.md]] | VarAbs + StatusColor — Variance and Conditional Status Color UDFs

VarAbs: actual-reference; StatusColor: SWITCH on tolLow/tolHigh thresholds → #E15759/#59A14F/#BAB0AC |
|| [[autodatetable.md]] | AutoDateTable — Calendar Table with Fiscal Column Support

CALENDAR + ADDCOLUMNS; fiscalYear via MOD(shift) formula; IsToday/IsCurrentMonth flags; mark as date table |
|| [[rollingtotal-rollingaverage.md]] | RollingTotal + RollingAverage — Rolling Window UDFs

DATESINPERIOD with unit switch (DAY/WEEK/MONTH/QUARTER/YEAR); RollingAverage divides by unit-aware DISTINCTCOUNT denominator |
|| [[percentile-buckets-udf.md]] | PercentileBuckets UDF — Dynamic Quintile/Decile Bucketing

PERCENTILEX.INC per q; BucketLabelFromBounds uses REPT(UNICHAR(8203)) for auto-sorting bucket labels |
|| [[humanize-udf.md]] | Humanize + HumanizeWithDecimals — K/M/B Number Abbreviation

FORMAT divide by 1K/1M/1B with 0.## mask; handles negatives and blanks |
|| [[sparklinesvg-lastndays.md]] | SparklineSVG_LastNDays — Gradient SVG Sparkline

ADDCOLUMNS + RANKX for XY coords; first→last direction → red/green gradient; UDF_EncodeSVG wrapper for Power BI image rendering |
|| [[topn-rank-within-group-udf.md]] | TopNWithinCurrentGroup + RankWithinCurrentGroup — Dynamic Top-N Within Filter Context

ADDCOLUMNS+TOPN/RANKX within passed TABLE; CONTAINS for visual filter; Dense rank for `<=N` filter |
|| [[normalizelabel-udf.md]] | NormalizeLabel — Trim + Clean Invisible Characters

TRIM + SUBSTITUTE(UNICHAR(160)) + SUBSTITUTE(UNICHAR(9)); prevents LOOKUPVALUE mismatches from Excel/HTML copy-paste |
|| [[narrative-topchange-udf.md]] | NarrativeTopChangeCore + Wrappers — Auto-Generated KPI Insight Text

SWITCH on MAXX/MINX extreme variance across dimension; shareCutoff threshold for attribution text; wrapper binds dim/attr columns |

## Patterns — Dynamic KPI Highlights  (Bittar, 2025)

|| Note | Description |
||------|-------------|
|| [[high-ot-flag-highlight.md]] | High OT Flag Highlight

DAX pattern: ADDCOLUMNS(SUMMARIZE) per-employee threshold filter + emoji string concatenation for button slicer callout label |
|| [[biggest-rise-highlight.md]] | Biggest Rise Highlight

DAX pattern: MAXX(ALL) to find top unit by variance + per-shift attribution via ADDCOLUMNS + 60% share threshold SWITCH |
|| [[top-unit-highlight.md]] | Top Unit Highlight

DAX pattern: MAXX(ALL) to find highest-OT unit + per-shift breakdown via ADDCOLUMNS + KEEPFILTERS |
|| [[lowest-fill-rate-highlight.md]] | Lowest Fill Rate Highlight

DAX pattern: SUMMARIZE(VALUES) + MINX for lowest fill rate + double-layer shift attribution with unfilled slot calculation |

## Patterns — Chart Label Formatting (Bittar, 2025)

|| Note | Description |
||------|-------------|
|| [[dummy-measures-for-label-background.md]] | Dummy Measures for Label Background

Split a measure into Positive/Negative dummies via IF — each added to chart as separate series for per-series background color formatting |
|| [[variance-arrow-label.md]] | Variance Arrow Label

IF + FORMAT + ↑↓ arrow prefix to display signed variance as a formatted percentage string |
|| [[label-font-color-switch.md]] | Label Font Color (SWITCH(TRUE()) on Variance)

SWITCH-TRUE returning hex color names based on variance sign — applied via per-series font color binding |

## Context & CALCULATE  (51 notes)

| Note | Description |
|------|-------------|
| [[ALL, ALLEXCEPT, ALLSELECTED, and REMOVEFILTERS in Power BI What’s the Difference.md]] | These four DAX functions look similar but behave differently. |
| [[CALCUHATE.md]] | CALCUHATE — Why CALCULATE is Inessential

CALCULATE is presented in most DAX literature as the most important function. |
| [[CALCULATE in Power BI The Most Important Function in DAX Explained with Examples.md]] | CALCULATE is the heart of DAX — it changes filter context, enables complex calculations, and unlocks advanced analytics. |
| [[Calculated objects in Power BI.md]] | (Article for beginners)

Data Analysis Expressions (DAX) is a very powerful language used for modeling in Power BI. |
| [[Power BI Demystified Row Context vs. Context Transition Explained with Examples.md]] | Most learners get stuck on DAX because of context. |
| [[Using Visual Calculation To Easily Calculate Avg 3 Month Sales In Power BI(.pbix included).md]] | Calculating rolling averages is a common requirement in sales analysis, especially when managers want to smooth out fluc |
| [[all-vs-removefilters-performance.md]] | ALL vs REMOVEFILTERS Performance Pattern

Using `ALL()` when only filter removal is needed causes the table to be materi |
| [[allexcept.md]] | ALLEXCEPT

Signature
```
ALLEXCEPT(<table>, <column>[, <column>[, …)
```

Parameters

| | Parameter | Type | Description |
| [[allnoblankrow.md]] | ALLNOBLANKROW

From the parent table of a relationship, returns all rows but the blank row, or all distinct values of a  |
| [[allselected.md]] | ALLSELECTED

> Extended 2026-07-27 — slicer-awareness teaching from Advanced Power BI DAX Measures (Jesse Ruiz)

Signatu |
| [[calcuate-the-calculate-counterculture.md]] | CALCUHATE — The CALCULATE Counterculture

Greg Deckler's contrarian stance: CALCULATE is inessential, overhyped, and mak |
| [[calculate-alternative-no-calculate-case.md]] | CALCULATE Alternative: No CALCULATE Case

Every CALCULATE use case can be expressed without CALCULATE. |
| [[calculate-context-modifier.md]] | CALCULATE: The Context Modifier

CALCULATE is the most important DAX function. |
| [[calculate-context-transition-core.md]] | CALCULATE and Context Transition: The Core Function

CALCULATE is the one function that runs the whole show. |
| [[calculate-internal-context-transition.md]] | CALCULATE Internals — Why It's Opaque

DAX for Humans calls CALCULATE "devilishly complex." Its filter expressions form  |
| [[calculate-nested-keephilters-gotcha.md]] | CALCULATE Nested KEEPFILTERS — Arbitrary Override Rules

Nested CALCULATE functions follow counterintuitive precedence r |
| [[calculate-pattern-library.md]] | CALCULATE Pattern Library

Six patterns covering the most common uses of CALCULATE. |
| [[calculate-table.md]] | CALCULATETABLE

Signature
```
CALCULATETABLE(<expression>[, <filter1> [, <filter2> [, …])
```

Parameters

| | Parameter |
| [[calculate.md]] | CALCULATE

> Extended 2026-07-27 — context transition teaching from Advanced Power BI DAX Measures (Jesse Ruiz) and The  |
| [[calculated-column-performance-impact.md]] | Calculated Column Performance Impact

Calculated columns add data to the model. |
| [[calculated-column-row-context.md]] | Calculated Column: Row Context

Calculated columns evaluate one row at a time. |
| [[calculatetable.md]] | CALCULATETABLE

Syntax

```dax
CALCULATETABLE(<expression>[, <filter1> [, <filter2> [, …])
``` |
| [[circular-dependencies-in-dax.md]] | Circular Dependencies in DAX

Resolving the error when two or more measures reference each other in a loop. |
| [[context-transition-with-calculate.md]] | Context Transition with CALCULATE

The mechanism by which CALCULATE converts an active row context into an equivalent fi |
| [[dax-allselected-cardinality-trap.md]] | ALLSELECTED Cardinality Trap

The "Best Practice" That Breaks Production

Widely-shared advice: use ALLSELECTED for "fle |
| [[dax-calculate-function.md]] | CALCULATE() — Apply Filter Context to DAX Aggregations

`CALCULATE()` evaluates an expression under a modified filter co |
| [[dax-calculated-column-use-cases.md]] | DAX Calculated Column Use Cases

Calculated columns belong in the data model when the result is a property of each row — |
| [[earlier-captures-outer-row-context.md]] | EARLIER Captures Row Context Across Iterator Boundaries

EARLIER resolves to the current row's value from the outer iter |
| [[earlier-earliest-nested-contexts.md]] | EARLIER and EARLIEST with Nested Row Contexts

Context Ladder Rules

Each iterator adds a new level to the row context s |
| [[earlier-function.md]] | EARLIER Function

Accesses the value of a column from the OUTER row context within a nested iterator or CALCULATE contex |
| [[earlier-in-dax-source.md]] | Understanding EARLIER in DAX: The Time Machine You Didn't Know You Had

> Type: article
> Author: Gulab Chand Tejwani
>  |
| [[earlier-real-world-patterns.md]] | EARLIER Real-World Patterns

Pattern 1: Running Total by Group

Classic use case — cumulative sum partitioned by a categ |
| [[earlier-row-context-mechanism.md]] | EARLIER Row Context Mechanism

The Core Rule

EARLIER only works with two nested row contexts:
- Outer loop → the calcul |
| [[earlier-vs-earliest-gotcha.md]] | EARLIER/EARLIEST Refers to Earlier Row Context That Doesn't Exist

Error message: "EARLIER/EARLIEST refers to an earlier |
| [[earlier-vs-var-comparison.md]] | EARLIER vs VAR Comparison

The Problem with EARLIER

- Works only in calculated columns (not measures)
- Hard to read wi |
| [[earlier.md]] | EARLIER

Signature

```dax
EARLIER(<column>[, <number>])
```

Parameters

| Parameter | Description |
|-----------|----- |
| [[earliest.md]] | EARLIEST

Syntax

```dax
EARLIEST(<column>)
```

Remarks

The EARLIEST function is similar to EARLIER, but lets you spec |
| [[filter-functions-all-allselected.md]] | Filter Functions: ALL and ALLSELECTED

Removing filters is as important as applying them. |
| [[filter-functions-allexcept-keepfilters.md]] | Filter Functions: ALLEXCEPT and KEEPFILTERS

ALLEXCEPT removes all filters except the ones you specify. |
| [[keepfilters.md]] | KEEPFILTERS

Signature
```
KEEPFILTERS(<expression>)
```

Parameters

| | Parameter | Type | Description |
|---|-------- |
| [[lookup-values-no-calculate.md]] | Lookup Values in DAX (No CALCULATE)

Replacing VLOOKUP/RELATED-style lookups with explicit FILTER + MAXX/MINX when there |
| [[lookup-without-calculate-filter-maxx.md]] | LOOKUP without CALCULATE: FILTER + MAXX/MINX

Using `FILTER` + `MAXX`/`MINX` as a row-by-row lookup pattern — finding th |
| [[measure-branching-calculate-composition.md]] | CALCULATE and Measure Branching Composition

CALCULATE is the primary tool for extending branched measures with filter c |
| [[nested-calculate-direct-filters-pattern.md]] | Nested CALCULATE → Direct Filters Pattern

Using nested CALCULATE + ALL() + FILTER() to remove all filters and reapply o |
| [[nested-calculate-gotcha.md]] | Nested CALCULATEs: The 8x-Per-Level Performance Killer

Pattern: CALCULATEs wrapped inside CALCULATEs, causing redundant |
| [[no-calculate-banana-pattern.md]] | No CALCULATE Banana Pattern

The foundational DAX pattern: `FILTER` a table into a variable, then aggregate it with an X |
| [[no-calculate-dax-pattern.md]] | No CALCULATE DAX Pattern

A DAX pattern that solves the majority of calculation problems without ever using CALCULATE. |
| [[no-calculate-time-intelligence-pattern.md]] | No CALCULATE Time Intelligence Pattern

Performing period-over-period calculations without CALCULATE or DAX time intelli |
| [[removefilters.md]] | REMOVEFILTERS

Removes all filters from a table or column, restoring the full context. |
| [[tewjani-earlier-source.md]] | Understanding EARLIER in DAX

The function everyone feared — until variables (VAR) came to the rescue. |
| [[var-calculate-filter-composition.md]] | VAR with CALCULATE and FILTER

VAR composes naturally with `CALCULATE` and `FILTER` — variables store intermediate resul |

| [[dax-measure-to-business-rule-extraction.md]] | DAX Measure → Business Rule Extraction

Converting DAX CALCULATE/IF/SWITCH measures into structured business rule JSON for AI agent consumption |
## Date & Time  (73 notes)

| Note | Description |
|------|-------------|
| [[EDATE.md]] | EDATE

Returns the date that is the specified number of months before or after a start date. |
| [[calendar-and-calendarauto.md]] | CALENDAR and CALENDARAUTO

Creates a single-column table of dates between a start and end date. |
| [[calendar.md]] | CALENDAR

Applies to: Calculated column Calculated table Measure Visual calculation Returns a table with a single column |
| [[calendarauto.md]] | CALENDARAUTO

Applies to: Calculated column Calculated table Measure Visual calculation ７ Note This function is discoura |
| [[closingbalance.md]] | CLOSINGBALANCEWEEK/MONTH/QUARTER/YEAR

Evaluate a measure at the last date of the period — useful for stock/cumulative m |
| [[closingbalancemonth.md]] | CLOSINGBALANCEMONTH

Applies to: Calculated column Calculated table Measure Visual calculation ７ Note This function is d |
| [[closingbalancequarter.md]] | CLOSINGBALANCEQUARTER

Applies to: Calculated column Calculated table Measure Visual calculation ７ Note This function is |
| [[closingbalanceweek.md]] | CLOSINGBALANCEWEEK

Applies to: Calculated column Calculated table Measure Visual calculation ７ Note This function is di |
| [[closingbalanceyear.md]] | CLOSINGBALANCEYEAR

Applies to: Calculated column Calculated table Measure Visual calculation ７ Note This function is di |
| [[date-datevalue.md]] | DATE, DATEVALUE, DAY, MONTH, YEAR, QUARTER

Construct or extract parts from a date value. |
| [[date-table-calendar-addcolumns.md]] | Calendar Table Creation: CALENDAR and ADDCOLUMNS

Creating a complete date/calendar table in DAX using `CALENDAR()`, `CA |
| [[date-table-creation-in-dax.md]] | Date Table Creation in DAX

Creating a dedicated date dimension table in DAX using CALENDAR and ADDCOLUMNS. |
| [[date.md]] | DATE

Applies to: Calculated column Calculated table Measure Visual calculation Returns the specified date in datetime f |
| [[dateadd-datesbetween-datesinperiod.md]] | DATEADD, DATESBETWEEN, DATESINPERIOD

Shift dates or build custom date ranges for CALCULATE filters. |
| [[dateadd.md]] | DATEADD

Applies to: Calculated column Calculated table Measure Visual calculation This function is discouraged for use  |
| [[datediff.md]] | DATEDIFF

Applies to: Calculated column Calculated table Measure Visual Returns the number of interval boundaries betwee |
| [[datesbetween.md]] | DATESBETWEEN

Applies to: Calculated column Calculated table Measure Visual calculation This function is discouraged for |
| [[datesinperiod.md]] | DATESINPERIOD

Applies to: Calculated column Calculated table Measure Visual calculation ７ Note This function is discour |
| [[datesmtd-datesqtd-datesytd.md]] | Period-to-Date: DATESYTD, DATESMTD, DATESQTD, DATESWTD

Return a table of dates from the start of the period to the curr |
| [[datesmtd.md]] | DATESMTD

Applies to: Calculated column Calculated table Measure Visual calculation ７ Note This function is discouraged  |
| [[datesqtd.md]] | DATESQTD

Applies to: Calculated column Calculated table Measure Visual calculation ７ Note This function is discouraged  |
| [[dateswtd.md]] | DATESWTD

Applies to: Calculated column Calculated table Measure Visual calculation This function is discouraged for use |
| [[datesytd.md]] | DATESYTD

Applies to: Calculated column Calculated table Measure Visual calculation This function is discouraged for use |
| [[datevalue.md]] | DATEVALUE

Applies to: Calculated column Calculated table Measure Visual calculation Converts a date in text format to a |
| [[dax-datedif.md]] | DATEDIF

Calculates the difference between two dates in a specified unit (year, month, or day). |
| [[dax-datediff.md]] | DATEDIFF

Returns the number of interval boundaries crossed between two dates. |
| [[dax-lastdate.md]] | LASTDATE

Returns the last (maximum) date in the current filter context for a date column. |
| [[dax-totalytd.md]] | TOTALYTD

Evaluates the year-to-date value of an expression. |
| [[delivery-date-accuracy-dax.md]] | Delivery Date Accuracy in DAX

Measuring how accurately promised delivery dates match actual delivery dates. |
| [[dynamic-date-switching-with-switch.md]] | Dynamic Date Switching with SWITCH + SELECTEDVALUE

Combine USERELATIONSHIP with SWITCH and SELECTEDVALUE to let users c |
| [[edate-eomonth.md]] | EDATE and EOMONTH

Shift dates by months, or return the last day of a month. |
| [[eomonth.md]] | EOMONTH

Applies to: Calculated column Calculated table Measure Visual calculation Returns the date in datetime format o |
| [[firstdate.md]] | FIRSTDATE

Applies to: Calculated column Calculated table Measure Visual calculation ７ Note This function is discouraged |
| [[firstnonblank.md]] | FIRSTNONBLANK

Applies to: Calculated column Calculated table Measure Visual calculation ７ Note

Syntax

```dax
FIRSTNON |
| [[firstnonblankvalue.md]] | FIRSTNONBLANKVALUE

Applies to: Calculated column Calculated table Measure Visual calculation ７ Note

Syntax

```dax
FIR |
| [[info.calendarcolumngroups.md]] | INFO.CALENDARCOLUMNGROUPS

Applies to: Calculated column Calculated table Measure Visual calculation DAX query Returns a |
| [[info.calendarcolumnreferences.md]] | INFO.CALENDARCOLUMNREFERENCES

Applies to: Calculated column Calculated table Measure Visual calculation DAX query Retur |
| [[info.calendars.md]] | INFO.CALENDARS

Applies to: Calculated column Calculated table Measure Visual calculation DAX query Returns a table with |
| [[isdatetime.md]] | ISDATETIME

Syntax

```dax
ISDATETIME(<value>)
```

Remarks

This function is not supported for use in DirectQuery mode  |
| [[lastdate.md]] | LASTDATE

Applies to: Calculated column Calculated table Measure Visual calculation ７ Note This function is discouraged  |
| [[lastnonblank.md]] | LASTNONBLANK

Applies to: Calculated column Calculated table Measure Visual calculation ７ Note

Syntax

```dax
LASTNONBL |
| [[lastnonblankvalue.md]] | LASTNONBLANKVALUE

Applies to: Calculated column Calculated table Measure Visual calculation ７ Note

Syntax

```dax
LAST |
| [[nextday.md]] | NEXTDAY

Applies to: Calculated column Calculated table Measure Visual calculation ７ Note This function is discouraged f |
| [[nextmonth.md]] | NEXTMONTH

Applies to: Calculated column Calculated table Measure Visual calculation ７ Note This function is discouraged |
| [[nextquarter.md]] | NEXTQUARTER

Applies to: Calculated column Calculated table Measure Visual calculation ７ Note This function is discourag |
| [[nextyear.md]] | NEXTYEAR

Applies to: Calculated column Calculated table Measure Visual calculation ７ Note This function is discouraged  |
| [[offset-based-date-calculations-deckler.md]] | Offset-Based Date Calculations (Deckler)

Integer offset columns on a date table as a replacement for all DAX time intel |
| [[offset-based-date-calculations.md]] | Offset-based Date Calculations

Using integer offsets to shift date context instead of DAX time intelligence functions. |
| [[openingbalance.md]] | OPENINGBALANCEWEEK/MONTH/QUARTER/YEAR

Evaluate a measure at the first date of the period (opening balance) — complement |
| [[openingbalancemonth.md]] | OPENINGBALANCEMONTH

Applies to: Calculated column Calculated table Measure Visual calculation ７ Note This function is d |
| [[openingbalancequarter.md]] | OPENINGBALANCEQUARTER

Applies to: Calculated column Calculated table Measure Visual calculation ７ Note This function is |
| [[openingbalanceweek.md]] | OPENINGBALANCEWEEK

Applies to: Calculated column Calculated table Measure Visual calculation ７ Note This function is di |
| [[openingbalanceyear.md]] | OPENINGBALANCEYEAR

Applies to: Calculated column Calculated table Measure Visual calculation ７ Note This function is di |
| [[parallelperiod.md]] | PARALLELPERIOD

Applies to: Calculated column Calculated table Measure Visual calculation ７ Note This function is discou |
| [[period-to-date-offset-pattern.md]] | Period-to-Date Offset Pattern

Using `CurrYearOffset`/`CurrQuarterOffset`/`CurrMonthOffset`/`CurrWeekOffset` columns to  |
| [[previousday.md]] | PREVIOUSDAY

Applies to: Calculated column Calculated table Measure Visual calculation ７ Note This function is discourag |
| [[previousmonth.md]] | PREVIOUSMONTH

Applies to: Calculated column Calculated table Measure Visual calculation ７ Note This function is discour |
| [[previousquarter.md]] | PREVIOUSQUARTER

Applies to: Calculated column Calculated table Measure Visual calculation ７ Note This function is disco |
| [[previousyear.md]] | PREVIOUSYEAR

Applies to: Calculated column Calculated table Measure Visual calculation ７ Note This function is discoura |
| [[reverse-year-to-date-dax.md]] | Reverse Year-to-Date

Purpose

Reverse Year-to-Date (Reverse YTD) decomposes a cumulative YTD figure
back into its indiv |
| [[reverse-year-to-date-in-dax.md]] | Reverse Year-To-Date in DAX

Calculating the remaining days in the current period — opposite of YTD. |
| [[sameperiodlastyear-parallelperiod.md]] | SAMEPERIODLASTYEAR and PARALLELPERIOD

Shift a date period one year back, or by a parallel period of any interval. |
| [[sameperiodlastyear-vs-parallelperiod.md]] | SAMEPERIODLASTYEAR vs PARALLELPERIOD vs PREVIOUSMONTH

Three DAX approaches for period-over-period comparisons — each ha |
| [[sameperiodlastyear-yoY.md]] | SAMEPERIODLASTYEAR: Year-over-Year Comparison

SAMEPERIODLASTYEAR shifts the current date range back exactly one year —  |
| [[sameperiodlastyear.md]] | SAMEPERIODLASTYEAR

> Extended 2026-07-27 — context from Advanced Power BI DAX Measures and DAX Coding Challenge (Jesse  |
| [[time-intelligence-date-table-requirements.md]] | Date Table: Requirements for Time Intelligence

DAX doesn't see dates like humans do — `Sales[Date]` is just numbers to  |
| [[time-intelligence-ytd-pattern.md]] | YTD Calculation with ALLSELECTED() Protection

Uses DATESYTD() inside CALCULATE with optional ALLSELECTED() wrapping to  |
| [[totalmtd.md]] | TOTALMTD

> Extended 2026-07-27 — retail analytics context from Advanced Power BI DAX Measures (Jesse Ruiz)

Applies to: |
| [[totalqtd.md]] | TOTALQTD

Applies to: Calculated column Calculated table Measure Visual calculation ７ Note This function is discouraged  |
| [[totalwtd.md]] | TOTALWTD

Applies to: Calculated column Calculated table Measure Visual calculation ７ Note This function is discouraged  |
| [[totalytd.md]] | TOTALYTD

> Extended 2026-07-27 — retail analytics context from Advanced Power BI DAX Measures (Jesse Ruiz)

Syntax

``` |
| [[treatas-multi-date-metrics.md]] | Multi-Date Metrics via TREATAS

A single Date table slicer drives multiple KPI measures — each targeting a different dat |
| [[ytd-qtd-mtd-functions.md]] | YTD, QTD, and MTD: Time Period Functions in DAX

Three functions that expand the date range dynamically — showing progre |

| [[calendar-dax.md]] | CALENDAR — DAX Date Table Generator

Returns a single-column date table between a start and end date |
| [[calendarauto-dax.md]] | CALENDARAUTO — DAX Auto Date Table

Auto-generates a date table covering all dates in the model |
| [[dax-vs-m-date-table-quick-reference.md]] | DAX vs M Date Table Quick Reference

Side-by-side comparison of DAX and Power Query approaches for building Date Tables |
| [[udf_encodesvg-url-encoder-for-svg.md]] | UDF_EncodeSVG — URL Encoder for SVG

Encodes raw SVG strings so Power BI can render them as image URLs via `data:image/svg+xml;utf8,...` |
| [[udf_svgpillcanvas-generic-pill-renderer.md]] | UDF_SVGPillCanvas — Generic Pill Renderer

Draws an SVG pill: background, border, text, optional dot. Used by [[task-status-pill-measure]] and [[task-priority-pill-measure-with-dot]]. |
| [[svg-pill-pattern-udf-based.md]] | SVG Pill Pattern (UDF-based)

Reusable pill rendering across reports by separating the UDF (drawing) from measures (semantics: colors, labels, borders). |
| [[udf-separation-principle-drawing-vs-semantics.md]] | UDF Separation Principle

Drawing (geometry, padding, dot position) belongs in the UDF. Semantics (which color, which text, when dot appears) belongs in measures. |
| [[svg-pill-geometry-dynamic-sizing.md]] | SVG Pill Geometry

`_pillW = _textLen * _charW + _hPad + _extraLeft` — pill width auto-expands to fit label text. |
| [[task-status-pill-measure.md]] | Task Status Pill Measure

Drops `SELECTEDVALUE(Tasks[Status])` into `UDF_SVGPillCanvas`. Status Border Color drives both border and dot color. |
| [[task-priority-pill-measure-with-dot.md]] | Task Priority Pill Measure (with dot)

Neutral white pill; dot color carries the priority signal. SWITCH maps High/Medium/Low to accent colors. |
| [[udf-svg-pill-setup-checklist.md]] | UDF SVG Pill Setup Checklist

Steps: Enable UDFs in Preview, define UDFs in DQV, Update model with changes, set Data Category = Image URL, set Image size Height=28 / Width=200. |
| [[compareoverperiodrange-udf-whole-period-time-comparisons.md]] | CompareOverPeriodRange UDF — Whole-Period Time Comparisons

Anchors on MAX visible date, defines full current and prior periods, returns VALUE/DELTA/PCT. |
| [[varabs-udf-variance-from-reference.md]] | VarAbs — Variance from Reference

`actual - reference` for target or prior-period variance calculations. |
| [[statuscolor-udf-variance-based-status-color.md]] | StatusColor — Variance-Based Status Color

Three-way SWITCH: underperforming → red, exceeding → green, neutral → gray. Applied via conditional formatting by field value. |
| [[turnover-rate-12m-rolling-window.md]] | Turnover Rate (12M Rolling Window)

Rolling 12-month turnover rate via `DATESINPERIOD`. Anchor on max date; prior period via `EOMONTH(-1)`. |
| [[positive-negative-dummy-measure-split.md]] | Positive/Negative Dummy Measure Split

`IF`-split pattern: `_Positive` and `_Negative` variants of the same measure for independent chart styling. |
| [[label-variance-if-arrow-format.md]] | Label Variance — Arrow + % Text Formatting

`"↑ " & FORMAT(ABS(_Var), "0.00%")` — direction arrow and formatted percentage for data labels. |
| [[label-font-color-variance-based.md]] | Label Font Color — Variance-Based Color

`SWITCH(TRUE(), variance > 0, dark_red, variance < 0, dark_green, secondary)` — font color by variance. |
| [[how-to-conditionally-format-chart-label-backgrounds-in-power-bi-source.md]] | How to Conditionally Format Chart Label Backgrounds in Power BI

No fx for label background → split measure into dummies, style each series independently. |
| [[autodatetable-udf-calendar-table-generator.md]] | AutoDateTable — Calendar Table Generator

One-call Date table with DateKey, Year/Month/Quarter, Start/EndOfMonth, WeekNo, YearMonth, Fiscal variants, and Today/CurrentMonth flags. |
| [[rolling-total-udf.md]] | RollingTotal — Rolling Window Total

Trailing N-period total anchored on MAX visible date. Supports DAY/WEEK/MONTH/QUARTER/YEAR units. |
| [[rolling-average-udf.md]] | RollingAverage — Rolling Window Average

Trailing N-period average with grain-aware denominator. Weeks implemented as 7×N days. |
| [[percentile-buckets-udf-pattern.md]] | Percentile Buckets UDF Pattern

Three-function chain: `PercentileBoundsCustom` → `BucketIndexFromBounds` → `BucketLabelFromBounds`. Dynamic quintile/bin bucketing that rebuilds on filter context change. |
| [[percentileboundscustom-udf.md]] | PercentileBoundsCustom — Dynamic Percentile Cutpoints

Returns Min/P1/P2/P3/P4/Max for any measure over a table. |
| [[bucketindexfrombounds-udf.md]] | BucketIndexFromBounds — Bucket Band Index

Maps value to band index 0..5 using pre-computed percentile bounds. |
| [[bucketlabelfrombounds-udf.md]] | BucketLabelFromBounds — Bucket Label Generator

`"a – b"` range labels with zero-width space prefix for correct text sort. |
| [[sparklinesvg_lastndays-udf.md]] | SparklineSVG_LastNDays — SVG Gradient Sparkline

Renders last N days of any measure as an SVG sparkline with red/green direction coloring. |
| [[humanize-udf-short-scale-number-formatting.md]] | Humanize — Short-Scale Number Formatting

Converts large values to K/M/B strings. Handles negatives and blanks. |
| [[top-n-within-group-udf-pattern.md]] | Top-N Within Group UDF Pattern

`TopNWithinCurrentGroup` + `RankWithinCurrentGroup` — replace per-measure Top-X logic with reusable ranking. |
| [[topnwithincurrentgroup-udf.md]] | TopNWithinCurrentGroup — Top-N Items Table

Returns a table of top N items ranked by score, scoped to current group context. |
| [[rankwithincurrentgroup-udf.md]] | RankWithinCurrentGroup — Item Rank

Dense rank of current item within current group context. |
| [[kpi-narrative-text-udf-pattern.md]] | KPI Narrative Text UDF Pattern

`NarrativeTopChangeCore` + wrappers — auto-generates insight text (e.g., "🔺 Biggest rise in OT/FTE: ICU +12.6%"). |
| [[narrativetopchangecore-udf.md]] | NarrativeTopChangeCore — KPI Narrative Formatter

Core narrative formatter: finds extreme variance, attributes to sub-dimension, formats insight string. |
| [[normalizelabel-udf-text-cleanup.md]] | NormalizeLabel — Text Cleanup UDF

Strips non-breaking spaces (UNICHAR 160), tabs, and extra whitespace from text fields before joins. |
| [[svg-pill-geometry-dynamic-sizing.md]] | SVG Pill Geometry (Dynamic Sizing)

How pill width, height, dot position, and text offset are computed from the label string. |
| [[power-bi-new-user-defined-functions-10-must-have-source.md]] | Power BI's New User Defined Functions: 10 Must-Have You'll Use in Every Report

Isabelle Bittar's master UDF library: 10 reusable functions for time comparisons, rolling windows, SVG sparklines, KPI narratives, and more. |
| [[udf-separation-principle-drawing-vs-semantics.md]] | UDF Separation Principle (Drawing vs. Semantics)

Design principle: UDFs handle drawing; measures handle business logic (colors, labels). |
| [[udf-svg-pill-setup-checklist.md]] | UDF SVG Pill Setup Checklist

Step-by-step checklist to enable UDFs, define the two UDFs, and configure the table visual. |
| [[one-udf-to-build-all-your-svg-pills-in-power-bi-source.md]] | One UDF to Build All Your SVG Pills in Power BI

> Type: article · Author: Isabelle Bittar · Published: 2025-11-27 |

## Math & Trig  (54 notes)

| Note | Description |
|------|-------------|
| [[atan2-dax-no-native.md]] | ATAN2 — Four-Quadrant Arctangent (No Native DAX Function)

DAX provides ATAN but lacks the companion ATAN2 function foun |
| [[bearing-calculation-in-dax.md]] | Bearing Calculation in DAX

Calculating the compass bearing from one lat/long to another. |
| [[bearing-direction-dax.md]] | Bearing and Direction in DAX

Calculating the compass direction (bearing) between two geographic points using DAX. |
| [[calculate-vs-no-calculate-performance.md]] | CALCULATE vs No CALCULATE — Performance Comparison

Greg Deckler's performance argument for the No CALCULATE approach. |
| [[calculated-column-vs-calculated-field.md]] | Calculated Column vs. |
| [[calculated-column-vs-measure-decision-tree.md]] | Calculated Column vs Measure: Decision Tree

Four questions that reliably determine whether a given calculation belongs  |
| [[calculated-column-vs-measure-total-sums.md]] | Calculated Column vs Measure: Total Sum Error

The most counterintuitive DAX mistake beginners make: storing a percentag |
| [[calculated-columns-vs-measures-performance.md]] | Calculated Columns vs Measures — Performance Tradeoffs

Using calculated columns for values that could be measures cause |
| [[cartesian-to-polar-conversion.md]] | Cartesian to Polar Conversion in DAX

Converting Cartesian coordinates (x, y) to polar coordinates (radius, angle) using |
| [[cartesian-to-polar-coordinates-in-dax.md]] | Cartesian to Polar Coordinates in DAX

Converting Cartesian (x, y) coordinates to polar (r, theta) format. |
| [[cross-fact-treatas-virtual-relationships.md]] | Cross-Fact TREATAS Virtual Relationships

Problem

Two fact tables from different systems (`fctPayrollVehicles` + `LN Eq |
| [[dax-measure-documentation-template.md]] | DAX Measure Documentation Template

The standard documentation template for DAX measures, with three documentation level |
| [[dax-measure-folder-structure-template.md]] | DAX Measure Folder Structure Template

The canonical folder structure for organizing a shared DAX measure library by bus |
| [[dax-udf-boilerplate-define-function.md]] | DAX UDF Boilerplate (DEFINE FUNCTION)

Ready-to-use function definition boilerplates for common UDF scenarios. |
| [[dax-userelationship.md]] | USERELATIONSHIP

Temporarily overrides the default active relationship between two tables and activates a specified inac |
| [[distance-calculation-dax-overview.md]] | Distance Calculations in DAX — Overview

DAX has no native spatial functions, but all geographic calculations can be imp |
| [[duration-calculations-in-dax.md]] | Duration Calculations in DAX (No Native Duration)

DAX has no native duration data type. |
| [[geomean.md]] | GEOMEAN

Applies to: Calculated column Calculated table Measure Visual calculation Returns the geometric mean of the num |
| [[geomeanx.md]] | GEOMEANX

Applies to: Calculated column Calculated table Measure Visual calculation Returns the geometric mean of an exp |
| [[haversine-distance-dax.md]] | Haversine Distance in DAX

The Haversine formula calculates the great-circle distance between two points on Earth's surf |
| [[haversine-distance-in-dax.md]] | Haversine Distance in DAX

Calculating the great-circle distance between two lat/long coordinates. |
| [[info.calculationgroups.md]] | INFO.CALCULATIONGROUPS

Applies to: Calculated column Calculated table Measure Visual calculation DAX query Returns a ta |
| [[info.calculationitems.md]] | INFO.CALCULATIONITEMS

Applies to: Calculated column Calculated table Measure Visual calculation DAX query Returns a tab |
| [[info.objecttranslations.md]] | INFO.OBJECTTRANSLATIONS

Applies to: Calculated column Calculated table Measure Visual calculation DAX query Returns a t |
| [[info.relatedcolumndetails.md]] | INFO.RELATEDCOLUMNDETAILS

Applies to: Calculated column Calculated table Measure Visual calculation DAX query Returns a |
| [[info.relationshipindexstorages.md]] | INFO.RELATIONSHIPINDEXSTORAGES

Applies to: Calculated column Calculated table Measure Visual calculation DAX query Retu |
| [[info.relationships.md]] | INFO.RELATIONSHIPS

Applies to: Calculated column Calculated table Measure Visual calculation DAX query Returns a table  |
| [[info.relationshipstorages.md]] | INFO.RELATIONSHIPSTORAGES

Applies to: Calculated column Calculated table Measure Visual calculation DAX query Returns a |
| [[info.view.relationships.md]] | INFO.VIEW.RELATIONSHIPS

INFO.VIEW.RELATIONSHIPS contains information about the relationships in the model, such as the  |
| [[linear-interpolation-in-dax.md]] | Linear Interpolation in DAX

Estimating values between two known data points using a linear model. |
| [[lookupvalue-and-related.md]] | LOOKUPVALUE and RELATED: Cross-Table Lookups

Use LOOKUPVALUE when relationships don't exist or can't be used. |
| [[measures-vs-calculated-columns.md]] | Measures vs Calculated Columns: When to Use Each

The fork that separates working models from bloated ones. |
| [[no-calculate-vs-calculate-comparison.md]] | No CALCULATE vs CALCULATE Comparison

Side-by-side comparison of the same calculation written both ways. |
| [[no-calculate-vs-calculate-deckler.md]] | No CALCULATE vs CALCULATE (Deckler's Thesis)

Two fundamentally different approaches to DAX calculation: the No CALCULAT |
| [[olatunji-dax-time-savers-source.md]] | DAX Concepts That Save Time — Daniel Olatunji

> Type: fundamentals guide / beginner
> Author: Daniel Olatunji
> Publish |
| [[pattern-3-context-isolation.md]] | Pattern 3: Context Isolation

Measures are wrapped in CALCULATE with explicit ALL() or ALLSELECTED() to prevent unintend |
| [[power-query-vs-dax-calculated-columns.md]] | Power Query vs DAX Calculated Columns

Columns can be created in two places in Power BI: Power Query (M language) and th |
| [[related-in-iterators-performance.md]] | RELATED in Iterators Performance Pattern

Using `RELATED()` inside an iterator (SUMX, AVERAGEX, etc.) causes one Storage |
| [[related.md]] | RELATED

Signature

```dax
RELATED(<column>)
```

Parameters

| Parameter | Description |
|-----------|-------------|
|  |
| [[relatedtable.md]] | RELATEDTABLE

Evaluates a table expression in a context modified by the given filters. |
| [[samplecartesianpointsbycover.md]] | SAMPLECARTESIANPOINTSBYCOVER

Applies to: Calculated column Calculated table Measure Visual calculation Returns a sample |
| [[table-manipulation-functions-overview.md]] | Table Manipulation Functions Overview

DAX provides a rich set of table manipulation functions that create, combine, fil |
| [[table-relationships-in-dax.md]] | Table Relationships in DAX

Tabular data models support relationships between tables that DAX can traverse to retrieve r |
| [[treatas-uselationship-crossfilter.md]] | TREATAS vs USERELATIONSHIP vs CROSSFILTER

Three functions for situations where the standard relationship model doesn't  |
| [[treatas-virtual-relationships.md]] | TREATAS: Virtual Relationships in DAX

TREATAS applies filter values from one table onto another as if a relationship ex |
| [[treatas-vs-userelationship-comparison.md]] | TREATAS vs USERELATIONSHIP vs CROSSFILTER

Three DAX mechanisms for controlling cross-table filter flow without adding p |
| [[udfs-vs-calculation-groups.md]] | UDFs vs Calculation Groups

When to use DAX user-defined functions and when to use calculation groups — the two reuse me |
| [[uselationship-common-mistakes.md]] | USERELATIONSHIP: Common Mistakes

USERELATIONSHIP is powerful but has sharp edges. |
| [[uselationship-function.md]] | USERELATIONSHIP()

USERELATIONSHIP activates an existing inactive relationship between two tables — temporarily, within  |
| [[userelationship-function.md]] | USERELATIONSHIP Function

Activates an existing inactive relationship between two tables for the duration of a CALCULATE |
| [[userelationship-source.md]] | RELATIONSHIP in DAX: Unlocking Role-Playing Dimensions

> Type: article
> Author: Gulab Chand Tejwani
> Published: 2025- |
| [[userelationship.md]] | USERELATIONSHIP

Applies to: Calculated column Calculated table Measure Visual calculation Specifies the relationship to |
| [[userexplicitrelationship.md]] | USERELATIONSHIP

Signature

```dax
USERELATIONSHIP(<column1>, <column2>)
```

Parameters

| Parameter | Description |
|- |
| [[visual-calculations.md]] | Visual Calculations (Preview)

Visual calculations allow DAX formulas to be written directly in a report visual, without |

| [[total-sales-dax-measure.md]] | Total Sales DAX Measure

SUM-based total revenue measure: core financial KPI for retail dashboards |
| [[total-profit-dax-measure.md]] | Total Profit DAX Measure

SUM-based total profit measure used alongside Total Sales to evaluate true business performance |
| [[total-orders-dax-measure.md]] | Total Orders DAX Measure

DISTINCTCOUNT-based order count: distinct customer orders vs. line item rows |
| [[average-order-value-dax.md]] | Average Order Value (AOV) DAX Measure

DIVIDE-based average revenue per order: key metric for purchasing behavior analysis |
## Statistical  (72 notes)

| Note | Description |
|------|-------------|
| [[Iterators in DAX SUMX, AVERAGEX, RANKX and How They Use Row & Filter Context.md]] | Understanding iterators is the key to mastering DAX. |
| [[RANKX.md]] | RANKX

Returns the ranking of a number in a list of numbers. |
| [[approximatedistinctcount.md]] | APPROXIMATEDISTINCTCOUNT

Applies to: Calculated column Calculated table Measure Visual calculation Returns an estimated |
| [[average-vs-averagea-vs-averagex.md]] | AVERAGE vs AVERAGEA vs AVERAGEX

Three Variants

| Function | Scope | Non-Numeric Values |
|----------|-------|--------- |
| [[average.md]] | AVERAGE and AVERAGEX

Returns the arithmetic mean of values in a column or of an expression evaluated over a table. |
| [[averagea.md]] | AVERAGEA

Applies to: Calculated column Calculated table Measure Visual calculation Returns the average (arithmetic mean |
| [[averagex-iterator-pattern.md]] | AVERAGEX Iterator Pattern

Core Pattern

`AVERAGEX(table, expression)` = iterator: evaluate `expression` for each row, t |
| [[averagex.md]] | AVERAGEX Function

Iterates over a table row-by-row, evaluates an expression per row, then returns the average of those  |
| [[better-median-workaround-dax.md]] | Better MEDIAN Workaround

Two approaches to correct the `MEDIAN` function's data-type error when used in calculated colu |
| [[better-median-workaround-in-dax.md]] | Better MEDIAN Workaround in DAX

DAX's MEDIAN function has issues with BLANK values and integer vs. |
| [[blank-vs-zero-in-averages.md]] | BLANK() vs 0 in Averages

BLANK() and 0 are not equivalent in DAX aggregations — BLANK propagates correctly through aver |
| [[conditional-variance-display-percent-hide.md]] | Conditional Variance Display (−100% Hide)

A DAX pattern that suppresses alarming -100% variance visuals by returning BL |
| [[count-countex-countblank.md]] | COUNT, COUNTA, COUNTAX, COUNTBLANK, COUNTX

Count rows or values — choose the right function for the data type. |
| [[count.md]] | COUNT

Applies to: Calculated column Calculated table Measure Visual calculation Counts the number of rows in the specif |
| [[counta.md]] | COUNTA

Applies to: Calculated column Calculated table Measure Visual calculation Counts the number of rows in the speci |
| [[countax.md]] | COUNTAX

Applies to: Calculated column Calculated table Measure Visual calculation The COUNTAX function counts non-blank |
| [[countblank.md]] | COUNTBLANK

Applies to: Calculated column Calculated table Measure Visual calculation Counts the number of blank cells i |
| [[counting-occurrences-in-dax.md]] | Counting Occurrences in DAX

Counting how many times a character or substring appears in a text field. |
| [[countrows.md]] | COUNTROWS

Signature

```dax
COUNTROWS([<table>])
```

Parameters

| Parameter | Description |
|-----------|------------ |
| [[countx.md]] | COUNTX

Applies to: Calculated column Calculated table Measure Visual calculation Counts the number of rows that contain |
| [[dax-aggregate-functions-average-min-max.md]] | AVERAGE(), MIN(), MAX() — DAX Aggregate Measures

These three DAX aggregation functions operate on entire columns (or co |
| [[dax-countrows.md]] | COUNTROWS

Counts the number of rows in a table — either the entire table or a filtered subset. |
| [[dax-debugging-checklist-variance.md]] | DAX Debugging Checklist — Variance / Cross-Fact Measures

> "Most DAX problems are not syntax problems. |
| [[dax-distinctcount.md]] | DISTINCTCOUNT

Counts the number of unique values in a column. |
| [[dax-grain-mismatch-variance.md]] | DAX Grain Mismatch — Variance Measure Breakdown

The Problem

Two measures evaluated at different grains:

```
Payroll C |
| [[dax-var.md]] | VAR

Declares a named variable (intermediate result) inside a DAX expression. |
| [[dax-variables-var-return.md]] | DAX Variables (VAR/RETURN)

Named intermediate values declared inside a DAX expression that avoid repetition, improve re |
| [[distinctcount.md]] | DISTINCTCOUNT

Signature

```dax
DISTINCTCOUNT(<column>)
```

Parameters

| Parameter | Description |
|-----------|----- |
| [[distinctcountnoblank.md]] | DISTINCTCOUNTNOBLANK

Remarks

Unlike DISTINCTCOUNT function, DISTINCTCOUNTNOBLANK does not count the BLANK value. |
| [[info.variations.md]] | INFO.VARIATIONS

Summarize this article for me Applies to: Calculated column Calculated table Measure Visual calculation |
| [[mark-chen-average-functions-source.md]] | Unraveling AVERAGE, AVERAGEA, AVERAGEX

Mark Chen's naming-convention guide to the three AVERAGE variants. |
| [[mark-chen-cross-fact-variance-source.md]] | Cross-Fact Variance DAX — Mark Chen Case Study

Real-world: compare payroll vehicle hours vs equipment hours from differ |
| [[median.md]] | MEDIAN

Applies to: Calculated column Calculated table Measure Visual calculation Returns the median of numbers in a col |
| [[medianx.md]] | MEDIANX — Iterator-based Median

Returns the median of values from a table expression. |
| [[movingaverage.md]] | MOVINGAVERAGE

Applies to: Calculated column Calculated table Measure Visual calculation Returns a moving average calcul |
| [[percentile-functions-in-dax.md]] | PERCENTILEX — Iterator-based Percentile

Returns the value at a given percentile from an iterator expression. |
| [[percentile.exc.md]] | PERCENTILE.EXC

Applies to: Calculated column Calculated table Measure Visual calculation Returns the k-th percentile of |
| [[percentile.inc.md]] | PERCENTILE.INC

Applies to: Calculated column Calculated table Measure Visual calculation Returns the k-th percentile of |
| [[percentilex.exc.md]] | PERCENTILEX.EXC

Applies to: Calculated column Calculated table Measure Visual calculation Returns the percentile number |
| [[percentilex.inc.md]] | PERCENTILEX.INC

Applies to: Calculated column Calculated table Measure Visual calculation Returns the percentile number |
| [[rankx-var-performance-pattern.md]] | RANKX with VAR Performance Pattern

Cache intermediate results in RANKX using VAR to avoid repeated evaluation of the ra |
| [[sales-to-budget-variance-percent.md]] | Sales-to-Budget Variance (% VAR)

A DAX pattern that calculates the percentage variance between actual sales and a budge |
| [[stdev.p.md]] | STDEV.P

Applies to: Calculated column Calculated table Measure Visual calculation Returns the standard deviation of the |
| [[stdev.s.md]] | STDEV.S

Applies to: Calculated column Calculated table Measure Visual calculation Returns the standard deviation of a s |
| [[stdevx-p-varx-p.md]] | STDEVX.P / VARX.P — Population Std Dev & Variance

Iterator functions that return the population standard deviation and  |
| [[stdevx.p.md]] | STDEVX.P

Applies to: Calculated column Calculated table Measure Visual calculation Returns the standard deviation of th |
| [[stdevx.s.md]] | STDEVX.S

Applies to: Calculated column Calculated table Measure Visual calculation Returns the standard deviation of a  |
| [[tewjani-var-source.md]] | VAR in DAX — Gulab Chand Tejwani

> Type: pattern guide / beginner
> Author: Gulab Chand Tejwani
> Published: 2025-11-03 |
| [[use-countrows-instead-of-count.md]] | Use COUNTROWS Instead of COUNT

When counting rows in a table, prefer COUNTROWS over COUNT. |
| [[use-variables-in-dax-formulas.md]] | Use Variables to Improve DAX Formulas

Variables (VAR) store intermediate results, improve performance, readability, and |
| [[var-anti-patterns-limits.md]] | VAR: Anti-Patterns and Limits

VAR is powerful, but it has specific limits. |
| [[var-dax-reading-complexity.md]] | VAR: The Habit That Saves Hours

VAR lets you calculate something once, store it under a name, and reuse that name throu |
| [[var-in-dax-source.md]] | Stop Repeating Yourself in DAX: The Power of Variables (VAR)

> Type: article
> Author: Gulab Chand Tejwani
> Published: |
| [[var-in-dax.md]] | VAR in DAX: Readability and Performance

DAX VAR statements name intermediate calculation results, making DAX both faste |
| [[var-performance-benefit.md]] | VAR Performance Benefit

Every time DAX evaluates an expression, it runs the full calculation. |
| [[var-syntax-and-pattern.md]] | VAR / RETURN: Syntax and Pattern

`VAR` stores an expression's result in a named variable; `RETURN` delivers the final r |
| [[var-table-variables.md]] | Table Variables in DAX

DAX `VAR` can hold table expressions — not just scalar values. |
| [[var-variable.md]] | VAR (Variables)

Defines a named variable that stores an intermediate result within a DAX expression. |
| [[var.p.md]] | VAR.P

Applies to: Calculated column Calculated table Measure Visual calculation Returns the variance of the entire popu |
| [[var.s.md]] | VAR.S

Applies to: Calculated column Calculated table Measure Visual calculation Returns the variance of a sample popula |
| [[varx.p.md]] | VARX.P

Applies to: Calculated column Calculated table Measure Visual calculation Returns the variance of the entire pop |
| [[varx.s.md]] | VARX.S

Applies to: Calculated column Calculated table Measure Visual calculation Returns the variance of a sample popul |
| [[weighted-average-in-dax.md]] | Weighted Average in DAX

Calculating a weighted average where each value contributes proportionally to its weight. |
| [[pearson-correlation-coefficient.md]] | Pearson Correlation Coefficient

A measure of linear relationship between two numeric variables, ranging from -1 to +1. |
| [[correlation-core-pearson-measure.md]] | Correlation — Core Pearson Correlation Measure

Calculates Pearson r between two variables, resolving them dynamically from the Matrix visual axis. |
| [[correlation-lower-triangle-no-diagonal.md]] | Correlation (Lower Triangle, No Diagonal)

Wraps the Correlation measure to hide the upper triangle and diagonal of the matrix. |
| [[correlation-color-buckets.md]] | Correlation Color (Buckets)

Returns a hex color based on fixed |r| buckets — background color for the correlation matrix. |
| [[correlation-font-color.md]] | Correlation Font Color

Returns white or black font color based on background brightness of the color bucket. |
| [[color-palette-measures-static-hex-strings.md]] | Color Palette Measures (Static Hex Strings)

Static hex color measures used as building blocks for DAX-driven conditional formatting. |
| [[variablesx-variablesy-disconnected-selector-tables.md]] | VariablesX / VariablesY — Disconnected Selector Tables

Two DATATABLE-based calculated tables listing variable names for the Matrix visual axes. |
| [[selected-x-name-selected-y-name.md]] | Selected X Name / Selected Y Name

Captures the currently selected variable name from the Matrix visual row and column axes. |
| [[x-value-y-value-dynamic-variable-mapping.md]] | X Value / Y Value — Dynamic Variable Mapping

Maps selected variable name to its numeric value from the data table for scatter chart axes. |
| [[scatter-title.md]] | Scatter Title — Dynamic Chart Title

Concatenates two selected variable names into a dynamic scatter chart title. |
| [[scatter-subtitle-html-dynamic-label-badge.md]] | Scatter Subtitle (HTML) — Dynamic Label Badge

Generates HTML subtitle for scatter chart tooltip: color-coded badge + plain-language sentence. |
| [[dynamic-chart-title-from-metric-dimension-selections.md]] | Dynamic Chart Title from Metric + Dimension Selections

`SELECTCOLUMNS(ALLSELECTED(...))` + `CONCATENATEX` composing `"📊 [Metric] by [Dimension]"` from field parameter selections. |
| [[bar-color-by-metric-type-variation-vs-absolute.md]] | Bar Color by Metric Type (Variation vs. Absolute)

`SELECTEDVALUE('Metric'[Order])` + `SWITCH` maps to the variation measure, then applies green/red based on sign. |
| [[pearson-correlation-coefficient-in-dax.md]] | Pearson Correlation Coefficient in DAX

Implements the Pearson formula using DAX iteration functions — no external libraries. |
| [[correlation-matrix-in-power-bi-dax-only.md]] | Correlation Matrix in Power BI (DAX-only)

Build a fully dynamic, interactive correlation matrix using only DAX and the Matrix visual. |
| [[dax-color-bucket-conditional-formatting-matrix.md]] | DAX Color Bucket Conditional Formatting (Matrix)

Apply discrete color buckets to a correlation matrix using DAX measures instead of a gradient. |
| [[how-to-build-a-correlation-matrix-in-power-bi-using-only-dax-source.md]] | How to Build a Correlation Matrix in Power BI Using Only DAX

> Type: article · Author: Isabelle Bittar · Published: 2025-08-24 |

## Text  (25 notes)

| Note | Description |
|------|-------------|
| [[CONCATENATEX.md]] | CONCATENATEX

Concatenates the result of an expression evaluated for each row of a table, using a specified delimiter be |
| [[CONTAINSSTRING.md]] | CONTAINSSTRING

Returns TRUE if a text string contains a specified substring. |
| [[What is Filter Context in Power BI A Complete Guide with Examples and Visuals.md]] | Filter context controls every calculation in DAX. |
| [[concatenate-concatenatex.md]] | CONCATENATE and CONCATENATEX

Join text strings together. |
| [[concatenate.md]] | CONCATENATE

Applies to: Calculated column Calculated table Measure Visual calculation Joins two text strings into one t |
| [[contains-containsstring.md]] | CONTAINS and CONTAINSSTRING

Test whether values or substrings exist within data. |
| [[containsstringexact.md]] | CONTAINSSTRINGEXACT

Applies to: Calculated column Calculated table Measure Visual Returns TRUE or FALSE indicating whet |
| [[context-transition-architecture.md]] | Context Transition Architecture

Every CALCULATE creates a context transition — row context becomes filter context. |
| [[dax-context-row-filter.md]] | DAX Context: Row Context and Filter Context

DAX context is simply the set of filters that determine which rows are avai |
| [[dax-context.md]] | DAX Context

DAX formulas evaluate within a context — the set of conditions that determines which rows are visible and w |
| [[filter-context-vs-row-context.md]] | Filter Context vs Row Context

The two evaluation contexts in DAX that determine how formulas are calculated — and the d |
| [[info.formatstringdefinitions.md]] | INFO.FORMATSTRINGDEFINITIONS

Applies to: Calculated column Calculated table Measure Visual calculation DAX query Return |
| [[isnontext.md]] | ISNONTEXT

Applies to: Calculated column Calculated table Measure Visual calculation Checks if a value is not text (blan |
| [[isstring.md]] | ISSTRING

Applies to: Calculated column Calculated table Measure Visual calculation Checks if a value is text, and retur |
| [[istext.md]] | ISTEXT

Applies to: Calculated column Calculated table Measure Visual calculation Checks if a value is text, and returns |
| [[measure-filter-context.md]] | Measure: Filter Context

Measures don't evaluate row-by-row — they aggregate all the rows currently visible under the ac |
| [[replace-substitute.md]] | REPLACE and SUBSTITUTE

Replace text by position or by content. |
| [[rollupaddissubtotal.md]] | ROLLUPADDISSUBTOTAL

Syntax

```dax
ROLLUPADDISSUBTOTAL ( [<grandtotalFilter>], <groupBy_columnName>, <name> [, 
[<group |
| [[row-context-vs-filter-context.md]] | Row Context vs Filter Context

Context is what determines which rows DAX looks at. |
| [[row-vs-filter-context-core.md]] | Row Context vs Filter Context: The Core Distinction

The concept that separates analysts who fight DAX from those who wr |
| [[selectedmeasureformatstring.md]] | SELECTEDMEASUREFORMATSTRING

Remarks

This function can only be referenced in expressions for calculation items in calcu |
| [[substitute.md]] | SUBSTITUTE

Applies to: Calculated column Calculated table Measure Visual calculation Replaces existing text with new te |
| [[substitutewithindex.md]] | SUBSTITUTEWITHINDEX

Syntax

```dax
SUBSTITUTEWITHINDEX(<table>, <indexColumnName>, <indexColumnsTable>,[<orderBy_expres |
| [[test-dax-udf-multiple-calling-contexts.md]] | Test DAX UDF from Multiple Calling Contexts

Minimum test cases to validate a UDF before trusting it in production. |
| [[text-extraction-patterns-in-dax.md]] | Text Extraction Patterns in DAX

Using LEFT, RIGHT, MID, FIND, and SEARCH together to parse and extract text. |

## Table Manipulation  (39 notes)

## Patterns — Dynamic KPI Highlights  (Bittar, 2025)

|| Note | Description |
||------|-------------|
|| [[high-ot-flag-highlight.md]] | High OT Flag Highlight

DAX pattern: ADDCOLUMNS(SUMMARIZE) per-employee threshold filter + emoji string concatenation for button slicer callout label |
|| [[biggest-rise-highlight.md]] | Biggest Rise Highlight

DAX pattern: MAXX(ALL) to find top unit by variance + per-shift attribution via ADDCOLUMNS + 60% share threshold SWITCH |
|| [[top-unit-highlight.md]] | Top Unit Highlight

DAX pattern: MAXX(ALL) to find highest-OT unit + per-shift breakdown via ADDCOLUMNS + KEEPFILTERS |
|| [[lowest-fill-rate-highlight.md]] | Lowest Fill Rate Highlight

DAX pattern: SUMMARIZE(VALUES) + MINX for lowest fill rate + double-layer shift attribution with unfilled slot calculation |

## Patterns — Chart Label Formatting (Bittar, 2025)

|| Note | Description |
||------|-------------|
|| [[dummy-measures-for-label-background.md]] | Dummy Measures for Label Background

Split a measure into Positive/Negative dummies via IF — each added to chart as separate series for per-series background color formatting |
|| [[variance-arrow-label.md]] | Variance Arrow Label

IF + FORMAT + ↑↓ arrow prefix to display signed variance as a formatted percentage string |
|| [[label-font-color-switch.md]] | Label Font Color (SWITCH(TRUE()) on Variance)

SWITCH-TRUE returning hex color names based on variance sign — applied via per-series font color binding |


| Note | Description |
|------|-------------|
| [[columnstatistics.md]] | COLUMNSTATISTICS

Applies to: Calculated column Calculated table Measure Visual This function is discouraged for use in  |
| [[custom-matrix-hierarchy-in-dax.md]] | Custom Matrix Hierarchy in DAX

Controlling row hierarchy expansion in Power BI Matrix visuals with DAX. |
| [[customdata.md]] | CUSTOMDATA

Applies to: Calculated column Calculated table Measure Visual calculation Returns the content of the CustomD |
| [[customer-acquisition-cost-cac-dax.md]] | Customer Acquisition Cost (CAC) in DAX

The total cost to acquire one new customer — a foundational SaaS and e-commerce  |
| [[customer-churn-rate-dax.md]] | Customer Churn Rate in DAX

Churn rate measures what percentage of customers leave within a given time period. |
| [[customer-lifetime-value-ltv-dax.md]] | Customer Lifetime Value (LTV/CLV) in DAX

LTV predicts the total revenue a customer will generate over their entire rela |
| [[datatable.md]] | DATATABLE

Declare an inline table of static data values in a DAX expression. |
| [[dax-error-handling-iferror-iserror.md]] | DAX Error Handling — IFERROR and ISERROR

DAX does not fail silently — errors break visuals. |
| [[dax-iferror.md]] | IFERROR

Returns a specified value if an expression evaluates to an error; otherwise, returns the expression's result. |
| [[dax-vs-generateseries-streak-comparison.md]] | DAX Streak Detection: GENERATESERIES vs Gaps and Islands

Two fundamentally different approaches to detecting consecutiv |
| [[detailrows.md]] | DETAILROWS

Evaluates a Detail Rows Expression defined for a measure and returns the data. |
| [[disconnected-tables-deckler.md]] | Disconnected Tables (Deckler)

Purpose

Disconnected tables are dimension or parameter tables deliberately left with
no  |
| [[disconnected-tables-in-dax.md]] | Disconnected Tables in DAX

Using tables with no active model relationships to drive dynamic calculations. |
| [[externalmeasure.md]] | EXTERNALMEASURE

Applies to: Calculated column Calculated table Measure Visual calculation Invokes a measure defined in  |
| [[generateseries-and-datatable.md]] | GENERATESERIES and DATATABLE

Inline table creation functions for constants. |
| [[generateseries.md]] | GENERATESERIES — Number Sequences

Generates a single-column table of sequential numbers. |
| [[groupby.md]] | GROUPBY — Manual Grouping in Iterators

Groups rows and computes aggregations within iterator functions. |
| [[iferror.md]] | IFERROR

Signature

```dax
IFERROR(<value>, <value_if_error>)
```

Parameters

| Parameter | Description |
|-----------| |
| [[info.detailrowsdefinitions.md]] | INFO.DETAILROWSDEFINITIONS

Applies to: Calculated column Calculated table Measure Visual calculation DAX query Returns  |
| [[info.groupbycolumns.md]] | INFO.GROUPBYCOLUMNS

Applies to: Calculated column Calculated table Measure Visual calculation DAX query Returns a table |
| [[info.perspectivetables.md]] | INFO.PERSPECTIVETABLES

Applies to: Calculated column Calculated table Measure Visual calculation DAX query Returns a ta |
| [[info.storagetablecolumns.md]] | INFO.STORAGETABLECOLUMNS

Applies to: Calculated column Calculated table Measure Visual calculation DAX query Returns a  |
| [[info.storagetables.md]] | INFO.STORAGETABLES

Summarize this article for me Applies to: Calculated column Calculated table Measure Visual calculat |
| [[info.tablepermissions.md]] | INFO.TABLEPERMISSIONS

Applies to: Calculated column Calculated table Measure Visual calculation DAX query Returns a tab |
| [[info.tables.md]] | INFO.TABLES

Applies to: Calculated column Calculated table Measure Visual calculation DAX query Returns a table with in |
| [[info.tablestorages.md]] | INFO.TABLESTORAGES

Applies to: Calculated column Calculated table Measure Visual calculation DAX query Returns a table  |
| [[info.view.tables.md]] | INFO.VIEW.TABLES

INFO.VIEW.TABLES contains information about the tables in the model, such as the table name, descripti |
| [[iserror.md]] | ISERROR

Applies to: Calculated column Calculated table Measure Visual calculation Checks whether a value is an error, a |
| [[new-returning-customers-dax.md]] | New, Lost, and Returning Customers in DAX

Identifies customers who are newly acquired, lost (churned), or returning in  |
| [[orderby-partitionby-matchby.md]] | ORDERBY, PARTITIONBY, and MATCHBY

Article - 07/26/2023

These functions can only be used with DAX Window functions: IND |
| [[orderby.md]] | ORDERBY — Row Ordering in Iterators

Specifies the sort order for an iterator function result. |
| [[partitionby.md]] | PARTITIONBY — Iterator Grouping

Defines groups within an iterator for independent ordering. |
| [[runningsum.md]] | RUNNINGSUM

Applies to: Calculated column Calculated table Measure Visual calculation Returns a running sum calculated a |
| [[summarize.md]] | SUMMARIZE

Syntax

```dax
SUMMARIZE(ResellerSales_USD, DateTime[CalendarYear], ProductCategory[ProductCategoryName], "Sa |
| [[summarizecolumns.md]] | SUMMARIZECOLUMNS — Aggregation Table

Creates a summary table with grouped rows and optional aggregations. |
| [[table-constructor-pattern-in-dax.md]] | Table Constructor Pattern in DAX

Using row constructors to create inline tables for slicers, parameters, and small look |
| [[tableof.md]] | TABLEOF

Summarize this article for me Applies to: Calculated column Calculated table Measure Visual calculation Returns |
| [[time-tables-in-dax.md]] | Time Tables in DAX

Creating a time dimension table for minute-level or hour-level granularity. |
| [[window-functions-orderby-partitionby-matchby.md]] | Window Functions: ORDERBY, PARTITIONBY, MATCHBY

ORDERBY, PARTITIONBY, and MATCHBY are companion functions used exclusiv |

## Financial  (54 notes)

| Note | Description |
|------|-------------|
| [[absenteeism-rate-dax.md]] | Absenteeism Rate in DAX

Absenteeism measures unexpected employee unavailability (sick days, no-shows) as distinct from  |
| [[advanced-patterns-ranking-abc-pareto.md]] | Advanced Patterns: Ranking, ABC Analysis, and Pareto

Combining DAX building blocks into real-world analytical patterns. |
| [[amordegrc.md]] | AMORDEGRC

Applies to: Calculated column Calculated table Measure Visual calculation Returns the depreciation for each a |
| [[amorlinc.md]] | AMORLINC

Applies to: Calculated column Calculated table Measure Visual calculation Returns the depreciation for each ac |
| [[beta.dist.md]] | BETA.DIST

Applies to: Calculated column Calculated table Measure Visual calculation Returns the beta distribution. |
| [[beta.inv.md]] | BETA.INV

Applies to: Calculated column Calculated table Measure Visual Returns the inverse of the beta cumulative proba |
| [[chisq.dist.md]] | CHISQ.DIST

Applies to: Calculated column Calculated table Measure Visual calculation Returns the chi-squared distributi |
| [[chisq.dist.rt.md]] | CHISQ.DIST.RT

Applies to: Calculated column Calculated table Measure Visual calculation Returns the right-tailed probab |
| [[chisq.inv.md]] | CHISQ.INV

Applies to: Calculated column Calculated table Measure Visual calculation Returns the inverse of the left-tai |
| [[chisq.inv.rt.md]] | CHISQ.INV.RT

Applies to: Calculated column Calculated table Measure Visual calculation Returns the inverse of the right |
| [[confidence.norm.md]] | CONFIDENCE.NORM

The confidence interval is a range of values. |
| [[confidence.t.md]] | CONFIDENCE.T

Applies to: Calculated column Calculated table Measure Visual calculation Returns the confidence interval  |
| [[coupdaybs.md]] | COUPDAYBS

Applies to: Calculated column Calculated table Measure Visual calculation Returns the number of days from the |
| [[coupdays.md]] | COUPDAYS

Applies to: Calculated column Calculated table Measure Visual calculation Returns the number of days in the co |
| [[coupdaysnc.md]] | COUPDAYSNC

Applies to: Calculated column Calculated table Measure Visual calculation Returns the number of days from th |
| [[coupncd.md]] | COUPNCD

Applies to: Calculated column Calculated table Measure Visual calculation Returns the next coupon date after th |
| [[coupnum.md]] | COUPNUM

Returns the number of coupons payable between the settlement date and maturity date, rounded up to the nearest  |
| [[couppcd.md]] | COUPPCD

Applies to: Calculated column Calculated table Measure Visual calculation Returns the previous coupon date befo |
| [[cumipmt.md]] | CUMIPMT

Applies to: Calculated column Calculated table Measure Visual calculation Returns the cumulative interest paid  |
| [[cumprinc.md]] | CUMPRINC

Applies to: Calculated column Calculated table Measure Visual calculation Returns the cumulative principal pai |
| [[dax-key-normalization-trim.md]] | Key Normalization — Leading Spaces Break Cross-System Joins

The Bug

One system stores job numbers as:
```
"23540"
```
 |
| [[dax-kpi-create-key-performance-indicator.md]] | DAX KPI: Create Key Performance Indicator in PowerPivot

A KPI in PowerPivot establishes a target value and threshold ra |
| [[dollarde.md]] | DOLLARDE

Applies to: Calculated column Calculated table Measure Visual calculation Converts a dollar price expressed as |
| [[dollarfr.md]] | DOLLARFR

Applies to: Calculated column Calculated table Measure Visual calculation Converts a dollar price expressed as |
| [[earned-value-management-evm-dax.md]] | Earned Value Management (EVM) in DAX

EVM combines scope, schedule, and cost into a unified project performance framewor |
| [[employee-turnover-rate-etr-dax.md]] | Employee Turnover Rate (ETR) in DAX

ETR measures the percentage of employees who leave an organization within a defined |
| [[fifo-first-in-first-out-dax.md]] | FIFO Inventory Costing in DAX

First In, First Out inventory valuation — consuming the oldest inventory first. |
| [[financial-functions-overview.md]] | Financial Functions in DAX

DAX financial functions perform financial calculations like net present value, rate of retur |
| [[gini-coefficient-dax.md]] | Gini Coefficient in DAX

The Gini coefficient measures income or wealth inequality within a distribution (0 = perfect eq |
| [[hidden-cost-of-messy-measures.md]] | The Hidden Cost of Messy Measures

The three costs of a disorganized DAX measure library: wasted search time, formula in |
| [[info.kpis.md]] | INFO.KPIS

Applies to: Calculated column Calculated table Measure Visual calculation DAX query Returns a table with info |
| [[inventory-aging-buckets-0-1-1-2-5-weeks.md]] | Inventory Aging Buckets (0–1, 1–2, 5+ Weeks)

A DAX pattern that classifies sales by how old the sold inventory is at ti |
| [[ispmt.md]] | ISPMT

Applies to: Calculated column Calculated table Measure Visual calculation Calculates the interest paid (or receiv |
| [[iterator-cost-principle.md]] | Iterator Cost Principle

Iterators (SUMX, AVERAGEX, MAXX, MINX, COUNTX, etc.) are powerful but carry row-by-row evaluati |
| [[measure-totals-problem-dax.md]] | Measure Totals Problem in DAX

Grand totals in matrix visuals don't always equal the sum of the visible row values — bec |
| [[norm.dist.md]] | NORM.DIST

Applies to: Calculated column Calculated table Measure Visual calculation Returns the normal distribution for |
| [[norm.inv.md]] | NORM.INV

Applies to: Calculated column Calculated table Measure Visual calculation The inverse of the normal cumulative |
| [[norm.s.dist.md]] | NORM.S.DIST

Applies to: Calculated column Calculated table Measure Visual calculation Returns the standard normal distr |
| [[norm.s.inv.md]] | NORM.S.INV

Applies to: Calculated column Calculated table Measure Visual calculation Returns the inverse of the standar |
| [[oddfprice.md]] | ODDFPRICE

Returns the price per $100 face value of a security having an odd (short or long) first period. |
| [[oddfyield.md]] | ODDFYIELD

Returns the yield of a security that has an odd (short or long) first period. |
| [[oddlprice.md]] | ODDLPRICE

Applies to: Calculated column Calculated table Measure Visual calculation Returns the price per $100 face val |
| [[oddlyield.md]] | ODDLYIELD

Applies to: Calculated column Calculated table Measure Visual calculation Returns the yield of a security tha |
| [[permut.md]] | PERMUT

Applies to: Calculated column Calculated table Measure Visual calculation Returns the number of permutations for |
| [[price.md]] | PRICE

Returns the price per $100 face value of a security that pays periodic interest. |
| [[pricedisc.md]] | PRICEDISC

Applies to: Calculated column Calculated table Measure Visual calculation Returns the price per $100 face val |
| [[pricemat.md]] | PRICEMAT

Applies to: Calculated column Calculated table Measure Visual calculation Returns the price per $100 face valu |
| [[tbilleq.md]] | TBILLEQ

Applies to: Calculated column Calculated table Measure Visual calculation Returns the bond-equivalent yield for |
| [[tbillprice.md]] | TBILLPRICE

Applies to: Calculated column Calculated table Measure Visual calculation Returns the price per $100 face va |
| [[tbillyield.md]] | TBILLYIELD

Applies to: Calculated column Calculated table Measure Visual calculation Returns the yield for a Treasury b |
| [[the-measure-totals-problem-in-dax.md]] | The Measure Totals Problem in DAX

When a measure returns correct values per row but incorrect values at the total level |
| [[yield.md]] | YIELD

Returns the yield on a security that pays periodic interest. |
| [[yielddisc.md]] | YIELDDISC

Applies to: Calculated column Calculated table Measure Visual calculation Returns the annual yield for a disc |
| [[yieldmat.md]] | YIELDMAT

Applies to: Calculated column Calculated table Measure Visual calculation Returns the annual yield of a securi |

## Bitwise  (5 notes)

## Gotchas  (Bittar, 2025)

|| Note | Description |
||------|-------------|
|| [[emoji-in-dax-string-concatenation.md]] | Emoji in DAX String Concatenation

DAX handles Unicode emoji in string literals correctly; rendering issues are a Power BI visual limitation, not a DAX limitation |

| Note | Description |
|------|-------------|
| [[bitand.md]] | BITAND

Applies to: Calculated column Calculated table Measure Visual calculation Returns a bitwise AND of two numbers. |
| [[bitlshift.md]] | BITLSHIFT

Applies to: Calculated column Calculated table Measure Visual calculation Returns a number shifted left by th |
| [[bitor.md]] | BITOR

Returns a bitwise OR of two numbers. |
| [[bitrshift.md]] | BITRSHIFT

Applies to: Calculated column Calculated table Measure Visual calculation Returns a number shifted right by t |
| [[bitxor.md]] | BITXOR

Applies to: Calculated column Calculated table Measure Visual calculation Returns a bitwise XOR of two numbers. |

## Information  (56 notes)

| Note | Description |
|------|-------------|
| [[SELECTEDVALUE.md]] | SELECTEDVALUE

Returns the single value selected by a slicer or filter context, or a specified alternate result when mul |
| [[dax-selectedvalue-totals-iterators.md]] | SELECTEDVALUE in Totals — Why It Breaks and How to Fix

Why SELECTEDVALUE Works at Row Level

At row level (one Vehicle  |
| [[hasonevalue.md]] | HASONEVALUE

Applies to: Calculated column Calculated table Measure Visual calculation Returns TRUE when the context for |
| [[info-functions.md]] | INFO Functions (Model Introspection)

DAX INFO functions return metadata about the data model. |
| [[info.alternateofdefinitions.md]] | INFO.ALTERNATEOFDEFINITIONS

Applies to: Calculated column Calculated table Measure Visual calculation DAX query Returns |
| [[info.annotations.md]] | INFO.ANNOTATIONS

Applies to: Calculated column Calculated table Measure Visual calculation DAX query Returns a table wi |
| [[info.attributehierarchies.md]] | INFO.ATTRIBUTEHIERARCHIES

Applies to: Calculated column Calculated table Measure Visual calculation DAX query Returns a |
| [[info.calcdependency.md]] | INFO.CALCDEPENDENCY

Applies to: Calculated column Calculated table Measure Visual calculation DAX query Returns a table |
| [[info.catalogs.md]] | INFO.CATALOGS

Applies to: Calculated column Calculated table Measure Visual calculation DAX query Returns a table with  |
| [[info.changedproperties.md]] | INFO.CHANGEDPROPERTIES

Applies to: Calculated column Calculated table Measure Visual calculation DAX query Returns a ta |
| [[info.columnpartitionstorages.md]] | INFO.COLUMNPARTITIONSTORAGES

Applies to: Calculated column Calculated table Measure Visual calculation DAX query Return |
| [[info.columnpermissions.md]] | INFO.COLUMNPERMISSIONS

Applies to: Calculated column Calculated table Measure Visual calculation DAX query Returns a ta |
| [[info.columns.md]] | INFO.COLUMNS

Applies to: Calculated column Calculated table Measure Visual calculation DAX query Returns a table with i |
| [[info.columnstorages.md]] | INFO.COLUMNSTORAGES

Applies to: Calculated column Calculated table Measure Visual calculation DAX query Returns a table |
| [[info.csdlmetadata.md]] | INFO.CSDLMETADATA

Summarize this article for me Applies to: Calculated column Calculated table Measure Visual calculati |
| [[info.cultures.md]] | INFO.CULTURES

Applies to: Calculated column Calculated table Measure Visual calculation DAX query Returns a table with  |
| [[info.datacoveragedefinitions.md]] | INFO.DATACOVERAGEDEFINITIONS

Summarize this article for me Applies to: Calculated column Calculated table Measure Visua |
| [[info.datasources.md]] | INFO.DATASOURCES

Applies to: Calculated column Calculated table Measure Visual calculation DAX query Returns a table wi |
| [[info.dependencies.md]] | INFO.DEPENDENCIES

Applies to: Calculated column Calculated table Measure Visual calculation DAX query Returns a table w |
| [[info.dictionarystorages.md]] | INFO.DICTIONARYSTORAGES

Applies to: Calculated column Calculated table Measure Visual calculation DAX query Returns a t |
| [[info.excludedartifacts.md]] | INFO.EXCLUDEDARTIFACTS

Applies to: Calculated column Calculated table Measure Visual calculation DAX query Returns a ta |
| [[info.expressions.md]] | INFO.EXPRESSIONS

Applies to: Calculated column Calculated table Measure Visual calculation DAX query Returns a table wi |
| [[info.extendedproperties.md]] | INFO.EXTENDEDPROPERTIES

Applies to: Calculated column Calculated table Measure Visual calculation DAX query Returns a t |
| [[info.functions.md]] | INFO.FUNCTIONS

Summarize this article for me Applies to: Calculated column Calculated table Measure Visual calculation  |
| [[info.hierarchies.md]] | INFO.HIERARCHIES

Applies to: Calculated column Calculated table Measure Visual calculation DAX query Returns a table wi |
| [[info.hierarchystorages.md]] | INFO.HIERARCHYSTORAGES

Applies to: Calculated column Calculated table Measure Visual calculation DAX query Returns a ta |
| [[info.levels.md]] | INFO.LEVELS

Applies to: Calculated column Calculated table Measure Visual calculation DAX query Returns a table with in |
| [[info.linguisticmetadata.md]] | INFO.LINGUISTICMETADATA

Applies to: Calculated column Calculated table Measure Visual calculation DAX query Returns a t |
| [[info.measures.md]] | INFO.MEASURES

Applies to: Calculated column Calculated table Measure Visual calculation DAX query Returns a table with  |
| [[info.model.md]] | INFO.MODEL

Applies to: Calculated column Calculated table Measure Visual calculation DAX query Returns a table with inf |
| [[info.parquetfilestorages.md]] | INFO.PARQUETFILESTORAGES

Applies to: Calculated column Calculated table Measure Visual calculation DAX query Returns a  |
| [[info.partitions.md]] | INFO.PARTITIONS

Applies to: Calculated column Calculated table Measure Visual calculation DAX query Returns a table wit |
| [[info.partitionstorages.md]] | INFO.PARTITIONSTORAGES

Applies to: Calculated column Calculated table Measure Visual calculation DAX query Returns a ta |
| [[info.perspectivecolumns.md]] | INFO.PERSPECTIVECOLUMNS

Applies to: Calculated column Calculated table Measure Visual calculation DAX query Returns a t |
| [[info.perspectivehierarchies.md]] | INFO.PERSPECTIVEHIERARCHIES

Applies to: Calculated column Calculated table Measure Visual calculation DAX query Returns |
| [[info.perspectivemeasures.md]] | INFO.PERSPECTIVEMEASURES

Applies to: Calculated column Calculated table Measure Visual calculation DAX query Returns a  |
| [[info.perspectives.md]] | INFO.PERSPECTIVES

Applies to: Calculated column Calculated table Measure Visual calculation DAX query Returns a table w |
| [[info.properties.md]] | INFO.PROPERTIES

Applies to: Calculated column Calculated table Measure Visual calculation DAX query Returns a table wit |
| [[info.querygroups.md]] | INFO.QUERYGROUPS

Applies to: Calculated column Calculated table Measure Visual calculation DAX query Returns a table wi |
| [[info.refreshpolicies.md]] | INFO.REFRESHPOLICIES

Applies to: Calculated column Calculated table Measure Visual calculation DAX query Returns a tabl |
| [[info.rolememberships.md]] | INFO.ROLEMEMBERSHIPS

Applies to: Calculated column Calculated table Measure Visual calculation DAX query Returns a tabl |
| [[info.roles.md]] | INFO.ROLES

Applies to: Calculated column Calculated table Measure Visual calculation DAX query Returns a table with inf |
| [[info.segmentmapstorages.md]] | INFO.SEGMENTMAPSTORAGES

Applies to: Calculated column Calculated table Measure Visual calculation DAX query Returns a t |
| [[info.segmentstorages.md]] | INFO.SEGMENTSTORAGES

Applies to: Calculated column Calculated table Measure Visual calculation DAX query Returns a tabl |
| [[info.storagefiles.md]] | INFO.STORAGEFILES

Applies to: Calculated column Calculated table Measure Visual calculation DAX query Returns a table w |
| [[info.storagefolders.md]] | INFO.STORAGEFOLDERS

Summarize this article for me Applies to: Calculated column Calculated table Measure Visual calcula |
| [[info.userdefinedfunctions.md]] | INFO.USERDEFINEDFUNCTIONS

Applies to: Calculated column Calculated table Measure Visual calculation DAX query Returns a |
| [[info.view.columns.md]] | INFO.VIEW.COLUMNS

Summarize this article for me Applies to: Calculated column Calculated table Measure Visual calculati |
| [[information-functions-overview.md]] | Information Functions Overview

Information functions inspect the current context to determine what values, filters, or  |
| [[iscrossfiltered.md]] | ISCROSSFILTERED

Applies to: Calculated column Calculated table Measure Visual calculation Returns TRUE when the specifi |
| [[isfiltered.md]] | ISFILTERED

Applies to: Calculated column Calculated table Measure Visual calculation Returns TRUE when the specified ta |
| [[isinscope-isfiltered.md]] | ISINSCOPE, ISCROSSFILTERED, ISFILTERED, HASONEFILTER, HASONEVALUE

Detect filter context state — which columns are activ |
| [[isselectedmeasure.md]] | ISSELECTEDMEASURE

Applies to: Calculated column Calculated table Measure Visual calculation Used by expressions for cal |
| [[selectedmeasure.md]] | SELECTEDMEASURE

Applies to: Calculated column Calculated table Measure Visual calculation Used by expressions for calcu |
| [[selectedmeasurename.md]] | SELECTEDMEASURENAME

Applies to: Calculated column Calculated table Measure Visual calculation Used by expressions for c |
| [[use-selectedvalue-instead-of-values.md]] | Use SELECTEDVALUE Instead of VALUES

Test whether a column is filtered to exactly one value using SELECTEDVALUE, not HAS |

| [[selectedvalue-workaround-field-parameters.md]] | SELECTEDVALUE Workarounds for Field Parameters

Three workarounds for GroupByColumns incompatibility: MAX, SUMMARIZE+SELECTCOLUMNS, calculated column |
| [[dax-function-taxonomy.md]] | DAX Function Taxonomy

DAX function categories: Aggregation, Filter (CALCULATE), Time Intelligence, Date, Text, Logical, Math/Stat, Table manipulation, Parent/Child |
| [[dax-real-world-use-cases.md]] | DAX Real-World Use Cases

Dynamic KPIs (CALCULATE), YoY growth (SAMEPERIODLASTYEAR), ABC analysis (RANKX+SWITCH), RLS (USERPRINCIPALNAME) |
## Relationships & Data Modeling  (1 notes)

| Note | Description |
|------|-------------|
| [[allcrossfiltered.md]] | ALLCROSSFILTERED

Applies to: Calculated column Calculated table Measure Visual calculation Clear all filters which are  |

## Debugging & Evaluation  (8 notes)

| Note | Description |
|------|-------------|
| [[dax-debugging-evaluateandlog.md]] | EVALUATEANDLOG — DAX Debug Print

`EVALUATEANDLOG` logs intermediate DAX values to the external trace log while still re |
| [[dax-debugging-tocsv.md]] | TOCSV Debugging Pattern

A No CALCULATE debugging technique: use `TOCSV()` in the `RETURN` statement to visualize a tabl |
| [[dax-debugging-with-evaluateandlog-and-tocsv.md]] | DAX Debugging with EVALUATEANDLOG and TOCSV

Inspecting intermediate DAX values by logging them to output. |
| [[dax-sample-model.md]] | DAX Sample Model: Adventure Works DW 2020

The Adventure Works DW 2020 Power BI Desktop sample model is designed to supp |
| [[evaluate.md]] | EVALUATE — DAX Query Execution

Returns a table from a DAX query. |
| [[evaluateandlog.md]] | EVALUATEANDLOG

Returns the value of the first argument and logs it in a DAX Evaluation Log profiler event. |
| [[performance-analyzer-debugging.md]] | Performance Analyzer Debugging in DAX

Using Power BI Performance Analyzer to identify slow visuals and DAX bottlenecks. |
| [[tocsv.md]] | TOCSV

Applies to: Calculated column Calculated table Measure Visual Returns a table as a string in CSV format. |

## Governance & Metadata  (5 notes)

| Note | Description |
|------|-------------|
| [[bim-file-ai-dax-generation.md]] | Generate DAX with AI Using a BIM File

A workflow for using AI chatbots (ChatGPT, Copilot, etc.) to generate accurate, m |
| [[field-as-raw-data-column.md]] | Field as Raw Data Column

Fields are the columns that come directly from your data source — the raw material Power BI us |
| [[fields-measures-janvi-source.md]] | Fields, Measures, and Calculated Columns — Janvi Gupta

> Type: tutorial / beginner guide
> Author: Janvi Gupta
> Publis |
| [[isinscope.md]] | ISINSCOPE

Applies to: Calculated column Calculated table Measure Visual calculation Returns true when the specified col |
| [[measure-governance-process.md]] | Measure Governance Process

The recurring operational cadence that keeps a DAX measure library organized after the initial build |

## Patterns — Custom Sorting (Bittar, 2023)

|| Note | Description |
||------|-------------|
|| [[custom-measure-sort-unichar-rept.md]] | Custom Measure Sort Order: UNICHAR(8203) + REPT() Invisible Prefix

UNICHAR(8203)=ZWSP prefix via REPT in SWITCH branches; more spaces=sorted earlier; sort column by itself to activate |
|| [[rept-unichar-8203-zwsp.md]] | REPT(UNICHAR(8203), N) — Invisible Zero-Width Space Prefix

REPT(UNICHAR(8203), N) prepends N invisible ZWSP characters; U+200B; used for custom lexical sort in measure values |
|| [[progress-status-switch-four-tier.md]] | Progress Status SWITCH: Four-Tier Sequence via UNICHAR Padding

Ahead/On schedule/Slightly behind/Behind SWITCH with 4/3/2/1 ZWSP prefixes → sort order: Ahead→On→Slightly→Behind |

## AI & Advanced Analytics  (9 notes)

| Note | Description |
|------|-------------|
| [[advanced-power-bi-dax-measures-retail-analytics-source.md]] | Advanced Power BI DAX Measures for Retail Analytics (Parts 1–2)

Two-part Medium series by Jesse Ruiz covering foundatio |
| [[ai-assisted-dax-development.md]] | AI-assisted DAX Development (BIM Prompting)

Using large language models to generate accurate, context-aware DAX code by |
| [[contains.md]] | CONTAINS

Applies to: Calculated column Calculated table Measure Visual calculation Returns true if values for all refer |
| [[containsrow.md]] | CONTAINSROW

Returns TRUE if a row exists in a table. |
| [[dax-copilot.md]] | Copilot for DAX Queries

Article - 12/10/2024

Copilot in Power BI can write and explain DAX queries in DAX query view o |
| [[dax-in-operator-containsrow.md]] | DAX IN Operator and CONTAINSROW

The `IN` operator tests whether a value exists in a set of values, replacing verbose `O |
| [[order-fulfillment-dax.md]] | Order Fulfillment Analysis in DAX

Comprehensive order fulfillment analysis: what was ordered, what shipped, what arrive |
| [[pathcontains.md]] | PATHCONTAINS

Applies to: Calculated column Calculated table Measure Visual calculation Returns TRUE if the specified it |
| [[time-intelligence-quick-reference-retail-analytics.md]] | Time Intelligence Quick Reference (Retail Analytics)

A condensed reference for the time intelligence functions used in retail analytics |

## Patterns — Dynamic Date Granularity (Bittar, 2024)

|| Note | Description |
||------|-------------|
|| [[maximum-date-week-month-anti-blank.md]] | Maximum Date/Week/Month: MAX + CALCULATE + FILTER Anti-Blank

MAX on fact date for single-date; CALCULATE(MAX, FILTER(fact, <>BLANK())) for Weekly/Monthly to prevent blanks suppressing valid calendar periods |
|| [[dynamic-granularity-aggregation-switch.md]] | Dynamic Granularity Aggregation: SWITCH on SELECTEDVALUE(field_param)

SELECTEDVALUE('Date Granularity'[...]) returns full column string; match against literal strings; CALCULATE+FILTER per granularity branch |
|| [[prior-period-per-granularity-switch.md]] | Prior-Period Calculation Per Granularity (Date−1, Week−7, EDATE)

Prior offsets: Daily→date-1, Weekly→date-7, Monthly→EDATE(date,-1); SWITCH branches mirror dynamic-granularity-aggregation-switch.md pattern |
|| [[in-progress-period-detection.md]] | "In Progress" Period Detection (Weekly+6 > MaxDate, EOMONTH > MaxDate)

Weekly: Maximum Week + 6 > Maximum Date; Monthly: EOMONTH(Maximum Month,0) > Maximum Date; appends "(In Progress)" to time frame label |

## Snippets — Bar Chart Axis Titles (Bittar, 2023)

|| Note | Description |
||------|-------------|
|| [[empty-constant-measure.md]] | Empty = 0 — Zero-Constant Measure for X-Axis Spacing

Literal 0 on a disabled axis creates bar-width control without displaying data; used to host custom label measures |
|| [[data-label-selectedvalue-concat.md]] | Data Label = SELECTEDVALUE(Category) & ": " & [Metric]

SELECTEDVALUE extracts category name in current filter context; concatenation with metric produces self-contained inline bar label |



## Patterns — Dynamic Format Strings (Bittar, 2025)

|| Note | Description |
||------|-------------|
|| [[dynamic-format-string-numeric-preserved.md]] | Dynamic Format String: Number Stays Numeric While Display Changes

FORMAT() converts to text (loses numeric behavior); Dynamic Format via SWITCH keeps value numeric while changing display; supports K/M/B/T, emojis, direction indicators |
|| [[auto-scale-kmbt-dynamic-format.md]] | Auto-Scaling K/M/B/T via SWITCH + Dynamic Format

SWITCH(TRUE(), >=1e12→T, >=1e9→B, >=1e6→M, >=1e3→K); format strings: one comma=K, two=M, three=B, four=T |
|| [[emoji-direction-dynamic-format.md]] | Emoji/Unicode Direction Indicators in Dynamic Format

Format string positive;negative;zero parts: emoji or UNICHAR(9650/9660) triangles; for color-consistent arrows use UNICHAR not emoji |
|| [[emoji-status-dynamic-format.md]] | SWITCH-Based Emoji Status Labels in Dynamic Format

Threshold-based SWITCH selects emoji by band (>0.05→🥳, <-0.05→😬, else→😐); format string preserves numeric value; better than direction-only indicators |


## Patterns — Display Active Slicers (Bittar, 2023)

|| Note | Description |
||------|-------------|
|| [[display-applied-filters-dax.md]] | Display Applied Filters via DAX: ISFILTERED + CONCATENATEX + ALLSELECTED

ISFILTERED guards per slicer column; CONCATENATEX+ALLSELECTED renders active selections as text; enables "Filter: >Country: USA,Canada" display at report top |


## Patterns — DAX-Driven Dynamic Images (Bittar, 2025)

|| Note | Description |
||------|-------------|
|| [[dax-driven-dynamic-image-measure.md]] | DAX-Driven Dynamic Images: One Measure → Infinite Visual States

Measure returns URL or SVG string; Image Visual renders it; SWITCH(TRUE()) selects image state; data:image/svg+xml;utf8 encoding for inline SVG; adapts to filter context |


## Gotchas — Same-Day Status Transitions (Nayan, 2026)

|| Note | Description |
||------|-------------|
|| [[same-day-status-trap-min-date.md]] | Same-Day Status Trap: MIN(Date) > CurrentDate Fails on Identical Dates

Naive MIN(date) > current_date silently ignores same-day transitions; identical dates have no chronological order without a tie-breaker; results in zero or inflated days-in-status |
|| [[extract-step-number-atomic.md]] | Extract Step Number from Status Name: VALUE(LEFT(FIND(".", status)-1))

Converts numeric prefix ("2. Discussion") to integer; FIND(".") locates period; LEFT extracts substring; VALUE() enables numeric comparison; IFERROR fallback = 0 |
|| [[days-in-status-step-tiebreaker.md]] | Days in Status: MINX + FILTER + OR(Date Future, SameDate + Step Higher)

MINX+FILTER virtual table finds next status; OR(future_date, same_date AND step_higher) resolves same-day ties; ISBLANK→TODAY() for open rows; auto-increments on refresh |
|| [[overdue-status-flag-snippet.md]] | Overdue Flag: `_isLatestStatus + IN + days_in_status > N`

| [[RAND-and-RAND-BETWEEN-Tips-Boniface-Muchendu-source.md]] | RAND() and RAND.BETWEEN() Tips (Boniface Muchendu)

Source note: random decimal (0–1) and random integer range (min–max) DAX functions; mock data generation and rank tiebreaking.

| [[RAND-function.md]] | RAND()

Generates a random decimal between 0 and 1. No parameters. Volatile — recalculates on every refresh.

| [[RANDBETWEEN-function.md]] | RAND.BETWEEN()

Generates a random integer between a min and max value (inclusive). Volatile.

| [[Tie-Breaking-RAND-Pattern.md]] | Tie-Breaking with RAND()

Using RAND() as a secondary sort key to break duplicate ranks in RANKX().

| [[RAND-Volatile-Gotcha.md]] | RAND() and RAND.BETWEEN() Are Volatile

Both functions recalculate on every refresh and interaction — no seed, disrupts caching, performance impact on large datasets.

| [[Mock-Data-Generation-RAND.md]] | Mock Data Generation with RAND()

| [[Plus-Zero-Blanks-Atomic.md]] | `+ 0` Fix for Blank Values

Appending +0 to a measure coerces blank to 0 via BLANK+0=0. Chart-unsafe — converts blanks to zeros.

| [[IF-Implicit-Blank-Check-Pattern.md]] | `IF([Measure], [Measure], "N/A")` — Implicit Blank Check

IF's first argument is boolean — passing a measure directly treats BLANK as FALSE. Compact alternative to ISBLANK.

| [[Choosing-Blank-Value-Strategy.md]] | Choosing a Blank Value Strategy

| [[ALL-REMOVEFILTERS-Power-BI-Boniface-Muchendu-source.md]] | ALL and REMOVEFILTERS in Power BI (Boniface Muchendu)

Source note: ALL and REMOVEFILTERS definitions, syntax, return values, comparison.

| [[ALL-Function-DAX.md]] | ALL() DAX

Removes filters and returns a table/column. Syntax, return value, ALL as table expression in SUMX.

| [[REMOVEFILTERS-Function-DAX.md]] | REMOVEFILTERS() DAX

Removes filters, returns nothing. Syntax, no-return-value limitation, SUMX incompatibility.

| [[ALL-vs-REMOVEFILTERS.md]] | ALL vs REMOVEFILTERS

Side-by-side: return value, SUMX compatibility, modern DAX idiom preference.

| [[Removing-Slicer-Filters-ALL.md]] | Removing Slicer Filters with ALL

| [[ALL-ALLSELECTED-ALLEXCEPT-Boniface-Muchendu-source.md]] | ALL, ALLSELECTED and ALLEXCEPT DAX Filter Function (Boniface Muchendu)

Source note: ALLSELECTED (query-level vs external filters), ALLEXCEPT (table-first, selective keep), comparison matrix.

| [[ALLSELECTED-Function-DAX.md]] | ALLSELECTED() DAX

Query-level filter removal, keeps external slicer selections. Syntax, external vs query-level filter distinction, % of page total.

| [[ALLEXCEPT-Function-DAX.md]] | ALLEXCEPT() DAX

Removes all table filters except specified columns. Table-first parameter order. All-regions-but-one-year pattern.

| [[ALL-ALLSELECTED-ALLEXCEPT-Comparison.md]] | ALL vs ALLSELECTED vs ALLEXCEPT

| [[SWITCH-REPT-UNICHAR-Custom-Sorting.md]] | SWITCH + REPT(UNICHAR(8203)) Custom Measure Sorting

REPT(UNICHAR(8203)) zero-width space prefix trick for sorting non-numeric text by numeric rank in Power BI.

| [[Survey-Sentiment-Scorecard.md]] | Survey Sentiment Scorecard: AVG + SWITCH

AVERAGE(SentimentScore) + SWITCH(TRUE()) with REPT/UNICHAR for sortable sentiment labels. Thresholds and cross-filter behaviour.

Side-by-side: filter behaviour matrix, decision guide, syntax comparison, % of grand/page/year denominators.

CALCULATE + ALL pattern, multiple tables, % of total pattern, REMOVEFILTERS equivalent.

Comparison of +0, Card Visual, and IF approaches — chart-safety, custom text, scope.

Using RAND.BETWEEN() to generate realistic random test data during development.

_isLatestStatus=ISBLANK(nextDate); status IN activeStatuses; days_in_status>threshold; all three must be TRUE; use in conditional formatting |
