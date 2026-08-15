---
created: 2026-07-26
updated: 2026-08-11
note_type: index
tags: [excel, index]
---

# Excel — Knowledge Base Index

This is the index for the Excel knowledge base. 57 notes grouped by type.

## Formulas & Functions  (26 notes)

| Note | Description |
|------|-------------|
| [[QUESTIONS.md]] | Open Questions

(None yet — questions surface here after ingestion, health checks, or during note-writing.)

Open questi |
| [[ai-in-excel-three-feature-tiers.md]] | AI in Excel: Three Feature Tiers

AI capabilities in Excel fall into three tiers: built-in features (Flash Fill, Analyze Data), Copilot, and Python in Excel.
| [[analysis-toolpak-statistical-functions.md]] | Excel Analysis ToolPak: Statistical Functions

Enabling the Analysis ToolPak

```
File → Options → Add-Ins → Manage Exce |
| [[beyond-vlookup-excel-bi.md]] | Beyond VLOOKUP: Unleashing Excel's True Data Power for Business Analysis

> Type: article
> Author: Harsh Gupta
> Publis |
| [[choose-merges-non-adjacent-columns.md]] | CHOOSE Merges Non-Adjacent Columns into a Virtual Array

`CHOOSE({1,2}, range1, range2)` stacks two non-adjacent columns |
| [[dax-68-95-99-rule.md]] | The 68-95-99 Rule (Three Sigma Rule of Thumb)

A mnemonic for interpreting standard deviation in a normal distribution:  |
| [[day-of-week-formula.md]] | Day of Week from Date in Excel

Formula

```
=TEXT(A3, "dddd")   ' Full name: Monday, Tuesday, ... |
| [[excel-as-bi-tool.md]] | Excel as a Business Intelligence Tool

Excel is a fully capable Business Intelligence (BI) platform for teams already fa |
| [[excel-averageif.md]] | AVERAGEIF and AVERAGEIFS

AVERAGEIF

Returns the arithmetic mean of cells that meet a single condition. |
| [[excel-copy-without-incrementing.md]] | How to Copy in Excel Without Auto-Incrementing

Excel is a fantastic tool for organizing, analyzing, and manipulating da |
| [[excel-data-forms.md]] | Excel Data Forms

A built-in form interface for viewing, adding, and filtering records in an Excel Table (defined with C |
| [[excel-data-validation.md]] | Data Validation in Excel

Restricts what data can be entered in a cell. |
| [[excel-quick-analysis-lens.md]] | Excel 2013 Quick Analysis Lens

Excel 2013 recommends analytical tools automatically. |
| [[excel-status-bar.md]] | Excel Status Bar Customization

The status bar at the bottom of the Excel window shows statistics for the currently sele |
| [[filter-function-excel.md]] | FILTER Function (Excel)

Returns a filtered array based on one or more conditions — without helper columns or VBA. |
| [[filter-function-multi-match.md]] | FILTER: Multiple Matches with Multiple Criteria

XLOOKUP returns only the first match. |
| [[harsh-gupta.md]] | Harsh Gupta

> Type: article
> Sources: 1 article in the vault

Bio

Harsh Gupta writes on Medium about Excel, data anal |
| [[index-match-multi-criteria-array.md]] | INDEX/MATCH with Boolean Array Multiplication

INDEX/MATCH with array multiplication handles multiple criteria without h |
| [[integrating-python-excel.md]] | In the ever-evolving landscape of data analysis, professionals are always on the lookout for tools that combine power wi |
| [[let-xmatch-index-lookup.md]] | LET + XMATCH + INDEX: Named Sub-Expressions for Clarity and Speed

LET names intermediate calculations inside a formula. |
| [[msquery-excel.md]] | MSQuery: SQL Against External Databases

Microsoft Query (MSQuery) lets you write raw SQL queries against Access, Excel, |
| [[power-query-etl-workflow.md]] | Power Query ETL Workflow

Connect to data sources, clean and transform data, then load it into a usable format — all wit |
| [[proper-for-scrubbing.md]] | Proper() for Data Scrubbing

`PROPER()` capitalizes the first letter of each word and makes all other letters lowercase. |
| [[python-in-excel-workflow.md]] | Python in Excel Workflow

Step-by-step workflow for using Python (pandas, Matplotlib, scikit-learn) inside Excel via the |
| [[sumproduct-multi-criteria-summing.md]] | SUMPRODUCT: Multi-Criteria Conditional Summing

SUMPRODUCT multiplies boolean arrays by values — useful for summing all  |
| [[vstack-flatten-columns-unique.md]] | VSTACK Flatten Columns into Unique List

Merges two or more separate column ranges into a single deduplicated list using |
| [[countif-project-progress.md]] | COUNTIF — Count Cells Matching a Criterion

Counts task rows by status value for dashboard KPIs. |
| [[sumifs-conditional-project-sums.md]] | SUMIFS — Conditional Sum Across Multiple Criteria

Conditional summing for budget tracking and resource analysis. |
| [[xlookup-modern-lookup.md]] | XLOOKUP — Modern Dynamic Lookup

Replacement for VLOOKUP/INDEX-MATCH; supports exact and approximate matches. |
| [[countifs-multi-criterion-project-tasks.md]] | COUNTIFS — Multi-Criterion Count

Multi-condition counting for segmented task analysis. |
| [[xlookup-multi-criteria-concatenation.md]] | XLOOKUP Multi-Criteria via Concatenation

XLOOKUP was designed for single-criterion lookups. |
| [[insert-basic-formulas-spire-xls.md]] | Insert Basic Formulas (Spire.XLS)

`.Formula` property for arithmetic, cell references, range references.
| [[insert-array-formulas-spire-xls.md]] | Array Formulas via FormulaArray (Spire.XLS)

`FormulaArray` + `CalculateAllValue()` for LINEST and matrix operations.
| [[insert-named-ranges-spire-xls.md]] | Named Ranges in Spire.XLS

`NameRanges.Add()` for self-documenting, maintainable formulas.
| [[format-formula-cells-spire-xls.md]] | Format Formula Cells (Spire.XLS)

Background colour, borders, and number formats on formula cells.
| [[cross-sheet-formula-references-spire-xls.md]] | Cross-Sheet Formula References (Spire.XLS)

`SheetName!CellRange` syntax for multi-worksheet formulas.
| [[subtotal-function-excel.md]] | SUBTOTAL (Excel)

Aggregate with hidden-row awareness; function codes 1–11 and 101–111.
| [[spire-xls-python-api-reference.md]] | Spire.XLS Python API Quick Reference

Cheat sheet: imports, Workbook lifecycle, cell ops, named ranges.
| [[automate-excel-formulas-python-alle-y-source.md]] | Automate Excel Formulas with Python (Alle Y)

Source: Spire.XLS article — arithmetic, built-in, array, named-range formulas.

## Data Analysis  (8 notes)

| Note | Description |
|------|-------------|
| [[dynamic-dropdown-unique-sort-filter.md]] | Dynamic Dropdown with UNIQUE + SORT + FILTER

Creates a sorted, deduplicated, blank-free dropdown list from a source col |
| [[histogram-from-pivot-table.md]] | Histogram from Pivot Table

Steps

1. |
| [[pivot-table-grand-totals.md]] | Pivot Table: Grand Totals and Subtotals

Subtotals

Access via: `Pivot Table Tools → Design → Subtotals`

| Option | Res |
| [[pivot-tables.md]] | Pivot Tables

An interactive table that aggregates, counts, averages, or sums data across categories instantly — no form |
| [[sort-unique-choose-non-adjacent-columns.md]] | SORT-UNIQUE-CHOOSE for Non-Adjacent Column Pairs

Deduplicate and alphabetically sort pairs of non-adjacent columns in a |
| [[sorting-non-adjacent-column-pairs-source.md]] | Sorting Non-Adjacent Column Pairs in Excel

Deduplicating and alphabetically sorting pairs of non-adjacent columns using |
| [[two-condition-filter.md]] | Two-Condition FILTER Pattern

Filters an array using two independent conditions combined with AND logic — like a SQL `WH |
| [[unique-filter-blanks.md]] | Remove Duplicates Ignoring Blanks

Deduplicates a column range while automatically excluding empty cells — in a single f |

## AI & Project Management  (15 notes)

| Note | Description |
|------|-------------|
| [[ai-in-excel-three-feature-tiers.md]] | AI in Excel: Three Feature Tiers

Built-in AI, Copilot, and Python in Excel — capabilities and requirements. |
| [[countif-project-progress.md]] | COUNTIF — Count Cells Matching a Criterion

Counts task rows by status value for dashboard KPIs. |
| [[sumifs-conditional-project-sums.md]] | SUMIFS — Conditional Sum Across Multiple Criteria

Conditional summing for budget tracking and resource analysis. |
| [[xlookup-modern-lookup.md]] | XLOOKUP — Modern Dynamic Lookup

Replacement for VLOOKUP/INDEX-MATCH; supports exact and approximate matches. |
| [[countifs-multi-criterion-project-tasks.md]] | COUNTIFS — Multi-Criterion Count

Multi-condition counting for segmented task analysis. |
| [[four-layer-project-workbook.md]] | Four-Layer Project Workbook

Integrated planning template, task tracker, dashboard, and timeline architecture. |
| [[dynamic-status-dashboard.md]] | Dynamic Status Dashboard

Formula-driven project dashboard using COUNTIF/SUMIFS/XLOOKUP against Excel Tables. |
| [[live-formula-gantt-chart.md]] | Live Formula Gantt Chart

Gantt chart that updates automatically via conditional formatting and live formulas. |
| [[ai-assisted-project-estimation.md]] | AI-Assisted Project Estimation

Using historical project data and AI to improve task duration and resource estimates. |
| [[ai-feature-decision-guide.md]] | AI Feature Decision Guide

Quick reference for choosing Flash Fill, Analyze Data, Copilot, or Python in Excel. |
| [[ai-guardrails-for-excel.md]] | AI Guardrails for Excel

Step-by-step workflow for safely integrating AI into Excel project workbooks. |
| [[ai-cannot-fix-messy-workbook.md]] | AI Cannot Fix a Messy Workbook

AI cannot salvage a structurally broken workbook; foundation must be fixed first. |
| [[ai-appears-accurate-while-wrong.md]] | AI Can Appear Accurate While Being Wrong

AI outputs can look correct while being logically wrong; validation is mandatory. |
| [[excel-as-project-workspace.md]] | Excel as Project Workspace

Excel evolving from static task repository to dynamic AI-augmented project workspace. |
| [[ai-in-excel-project-management-source.md]] | AI in Excel for Project Management — Source

Synthesising article: six sources on AI-augmented project management in Excel. |

## Visualization  (9 notes)

| Note | Description |
|------|-------------|
| [[Excel-to-Google-My-Maps-Integration.md]] | Excel to Google My Maps Integration

Export Excel location data to Google My Maps: single-sheet prep, column mapping (address/city/state/country), import, pin styling, multi-layer setup, reimport workflow, sharing. Tony Phillips, How-To Geek 2026. |
| [[conditional-formatting.md]] | Conditional Formatting Pattern

Apply visual rules to data so patterns, outliers, and threshold breaches are immediately |
| [[excel-recommended-charts.md]] | Excel 2013: Recommended Charts

Excel 2013 analyzes the shape of your data and suggests the most appropriate chart type. |
| [[scatter-chart-trendline-r-squared.md]] | Scatter Chart: Trendline and R²

Creating a Scatter Chart

```
Insert → Scatter (X, Y) or Bubble Chart → Scatter
```

Ad |
| [[scatter-chart-with-r-squared-trendline.md]] | Scatter Chart with R-Squared Trendline in Excel

A scatter chart (X/Y plot) shows the relationship between two numeric v |
| [[xml-json-format-excel.md]] | XML and JSON Format in Excel

XML Format

Excel can import XML data directly. |
| [[dynamic-auto-sorting-bar-chart-excel.md]] | Dynamic Auto-Sorting Bar Chart in Excel

Build a bar chart replacing a pie chart: values inside bars + percentages outside, auto-sorting via SORT(), dynamic total in chart title |
| [[In-Cell-Bar-Chart-REPT.md]] | In-Cell Bar Chart with REPT

Creates a proportional bar chart inside a cell using the block character `█` repeated relative to a maximum value; Consolas font, conditional formatting colour. |
| [[REPT-In-Cell-Bar-Charts.md]] | REPT: In-Cell Bar Charts

`REPT(text, number_of_times)` repeats text to create bar charts directly inside cells — no chart objects needed. |
| [[integrating-python-excel-source.md]] | Integrating Python into Excel: A New Era of Data Analysis

Source note: Python via =PY() in Excel 365, xl() for pandas DataFrames, Anaconda runtime, cloud execution. |

## Automation & Macros  (3 notes)

| Note | Description |
|------|-------------|
| [[descriptive-statistics-mean-median-mode-variance-stddev.md]] | Descriptive Statistics: Mean, Median, Mode, Variance, Standard Deviation

Reference for the five core descriptive statis |
| [[excel-analysis-toolpak-descriptive-statistics-histogram.md]] | Excel Analysis ToolPak: Enable, Descriptive Statistics, Histogram

The Analysis ToolPak is an Excel add-in that provides |
| [[inferential-vs-descriptive-statistics.md]] | Descriptive Statistics

Descriptive Statistics

Summarizes data with key calculated values:

| Statistic | Description | |

## Author Notes  (5 notes)

| Note | Description |
|------|-------------|
| [[Author-Mynda-Treacy.md]] | Mynda Treacy

Excel educator; MyOnlineTrainingHub.com. 11 sources in vault. Known for formulas, Power Query, dashboards. |

> Type: article
> Author: Mark Chen
> Published: 2024-11-07
> |
| [[mark-chen-five-methods-source.md]] | Five Methods to Master Multi-Criteria Lookups — Mark Chen

> Type: tutorial
> Author: Mark Chen
> Published: 2025-05-28
 |
| [[mark-chen-mastering-excel-superpower-source.md]] | Mastering Excel's Superpower: FILTER, UNIQUE, SORT, and CHOOSE (a.k.a. |
| [[mark-chen-multi-criteria-lookup-source.md]] | Multi-Criteria Lookups — Mark Chen

| [[10-Excel-Data-Cleaning-Hacks-DigitalBYKewat-source.md]] | 10 Excel Data Cleaning Hacks (DigitalBYKewat)

Source note: 10 hacks — TRIM/CLEAN, Flash Fill, duplicate highlighting, Excel Table, text case, Find & Replace, Text to Columns, blank highlighting, Data Validation, 3-min checklist.

| [[TRIM-CLEAN-Functions.md]] | TRIM and CLEAN Functions

TRIM removes spaces, CLEAN removes non-printable ASCII. CLEAN(TRIM()) combo. CHAR(160) limitation — use SUBSTITUTE.

| [[Flash-Fill-Ctrl-E.md]] | Flash Fill: Ctrl+E Pattern

Ctrl+E pattern detection — one manual example, Excel fills the rest. Use cases: name formatting, email extraction, phone formatting. Static values, not formulas.

| [[Highlight-Duplicates-Conditional-Formatting.md]] | Highlight Duplicates with Conditional Formatting

Home → Conditional Formatting → Duplicate Values. Inspect before Remove Duplicates — legitimate duplicates vs errors.

| [[Excel-Table-Ctrl-T.md]] | Excel Table: Ctrl+T

Ctrl+T converts range to Excel Table. Auto-expanding formulas, filter dropdowns, structured references, row shading.

| [[Text-Case-Functions.md]] | Text Case Functions: PROPER/UPPER/LOWER

PROPER capitalises each word, UPPER all caps, LOWER all lower. Prevents case-splitting in Pivot Tables. Combine with TRIM.

| [[Find-Replace-Ctrl-H.md]] | Find & Replace: Ctrl+H

Ctrl+H Replace All for NULL/N/A/Unknown placeholders. Workflow, common values, when NOT to use.

| [[Text-to-Columns.md]] | Text to Columns

Data → Text to Columns, Delimited mode. Comma, Space, Pipe separators. Power Query equivalent: Split Column → By Delimiter.

| [[Highlight-Blank-Cells.md]] | Highlight Blank Cells via Conditional Formatting

New Rule → Blanks. Bright fill on blank cells. Blank vs empty string "". Limits.

| [[Data-Validation-Dropdown.md]] | Data Validation: Prevent Bad Inputs

Data → Data Validation → List. Dropdown restrict inputs, Input Message, Error Alert. Named range option.

| [[3-Minute-Data-Cleaning-Checklist.md]] | 3-Minute Data Cleaning Checklist

7-step 3-minute routine: Backup → TRIM → Duplicates → Standardise → Blanks → Table → Verify totals.

| [[Data-Cleaning-Keyboard-Shortcuts.md]] | Data Cleaning Keyboard Shortcuts

Ctrl+T, Ctrl+E, Ctrl+H, Ctrl+Arrow, Ctrl+Shift+L, Alt+=, F4 — with context for each step.

> Type: tutorial
> Author: Mark Chen
> Published: 2024-11-14
> URL: https://medium.c |

| [[Source-6-Excel-Features-Tony-Phillips.md]] | 6 Excel Features I Use In Every Spreadsheet (Tony Phillips) |
| [[Custom-Number-Formats.md]] | Custom Number Formats — display without changing values |
| [[Slicer-Excel-Tables.md]] | Slicers in Excel Tables — visual button-based filtering |
| [[Power-Query-Get-Transform.md]] | Power Query (Get & Transform) — repeatable ETL pipeline |
| [[source-excel-postgres-weekend-yadullah.md]] | Excel Postgres Weekend Yadullah — Source (Data Modeling)

Excel → Postgres migration; Yadullah Abidi, MakeUseOf 2026-07-29. |
||| [[excel-vlookup-fragility.md]] | Excel VLOOKUP Fragility Atomic

3 failure modes: multi-sheet cross-reference, deleted-cell formula drift, filter fat-finger; all silent. |
||| [[excel-optional-safeguards.md]] | Excel Optional Safeguards Atomic

Data validation + Power Pivot optional and overridable; no enforced FK; habits break under deadline. |
||| [[Source-5-Hidden-Excel-Formula-Rules-Mynda-Treacy.md]] | Source: 5 Hidden Excel Formula Rules — Mynda Treacy


||| [[Helper-Columns-Build-for-Humans.md]] | Helper Columns: Build for Humans


||| [[Boolean-Logic-Replaces-IF.md]] | Boolean Logic Replaces IF


||| [[LET-Makes-Formulas-Readable.md]] | LET Makes Formulas Readable


||| [[LAMBDA-Custom-Functions-via-Name-Manager.md]] | LAMBDA: Reusable Custom Functions via Name Manager


||| [[Think-in-Arrays-Not-Rows.md]] | Think in Arrays, Not Rows

||| [[Source-6-Better-Alternatives-to-IF-Mynda-Treacy.md]] | Source: 6 Better Alternatives to IF — Mynda Treacy

||| [[IFS-vs-Nested-IF-Order-Matters.md]] | IFS vs Nested IF: Order Matters

||| [[XLOOKUP-vs-IF-for-Lookup-Tables.md]] | XLOOKUP vs IF for Lookup Tables

||| [[SWITCH-vs-IF-One-Value-Multiple-Matches.md]] | SWITCH vs IF: One Value, Multiple Matches

||| [[CHOOSE-for-Position-Based-Mapping.md]] | CHOOSE for Position-Based Mapping

||| [[SUMIFS-COUNTIFS-Replace-IF-Helper-Columns.md]] | SUMIFS/COUNTIFS Replace IF Helper Columns

||| [[LET-for-Deduplication.md]] | LET for Deduplication

||| [[Source-10-Custom-Number-Formatting-Tricks-Mynda-Treacy.md]] | Source: 10 Custom Number Formatting Tricks — Mynda Treacy

||| [[Four-Section-Number-Format-Structure.md]] | Four-Section Number Format Structure

||| [[Scale-Numbers-to-K-or-M.md]] | Scale Numbers to K or M

||| [[Inline-Colors-in-Number-Format.md]] | Inline Colors in Number Format

||| [[Pass-Fail-via-Number-Format.md]] | Pass/Fail via Number Format

||| [[Hide-Zero-Values-with-Format.md]] | Hide Zero Values with Format

||| [[Symbol-Arrows-in-Number-Format.md]] | Symbol Arrows in Number Format

||| [[Phone-Number-Format-Preserving-Zeroes.md]] | Phone Number Format Preserving Zeroes

||| [[Custom-Date-Formats.md]] | Custom Date Formats

||| [[Inline-Units-via-Number-Format.md]] | Inline Units via Number Format

||| [[Hide-All-Cell-Values-Format.md]] | Hide All Cell Values (;;;;)

||| [[Leading-Trailing-Characters-in-Format.md]] | Leading/Trailing Characters in Number Format

||| [[Source-Advanced-Conditional-Formatting-Formulas-Mynda-Treacy.md]] | Source: Advanced CF Using Formulas — Mynda Treacy

||| [[Mixed-References-for-Row-Formatting.md]] | Mixed References for Row Formatting

||| [[ISBLANK-Double-Unary-for-Row-Validation.md]] | ISBLANK + Double Unary for Row Validation

||| [[SEARCH-for-Keyword-Detection-in-CF.md]] | SEARCH for Keyword Detection in CF

||| [[TODAY-for-Dynamic-Date-Alerts.md]] | TODAY() for Dynamic Date Alerts

||| [[COUNTIF-Expanding-Range-for-Duplicates.md]] | COUNTIF Expanding Range for Duplicates

||| [[COUNTIFS-for-Multi-Column-Duplicates.md]] | COUNTIFS for Multi-Column Duplicates

||| [[MOD-SUBTOTAL-for-Filter-Aware-Banding.md]] | MOD(SUBTOTAL) for Filter-Aware Banding

||| [[Rule-Priority-in-CF-Manager.md]] | Rule Priority in CF Manager

||| [[Source-Dynamic-Excel-Report-4-Formulas-Mynda-Treacy.md]] | Source: Dynamic Report with 4 Formulas — Mynda Treacy

||| [[UNIQUE-SORT-Dynamic-Dropdowns.md]] | UNIQUE + SORT for Dynamic Dropdowns

||| [[FILTER-Boolean-AND-OR-Logic.md]] | FILTER Boolean AND/OR Logic

||| [[Dependent-Dropdown-via-FILTER-UNIQUE-SORT.md]] | Dependent Dropdown via FILTER → UNIQUE → SORT

||| [[GROUPBY-CHOOSECOLS-TAKE-Top-N-Summary.md]] | GROUPBY + CHOOSECOLS + TAKE for Top-N

||| [[SPILL-Error-Cell-in-Spill-Range.md]] | #SPILL! Error — Cell in Spill Range

||| [[No-Dynamic-Arrays-Inside-Formatted-Tables.md]] | No Dynamic Arrays Inside Formatted Tables

||| [[Excel-365-Version-Requirements-Dynamic-Functions.md]] | Excel 365 Version Requirements for Dynamic Functions

||| [[Source-Automated-Excel-Database-Mynda-Treacy.md]] | Source: Automated Excel Database — Mynda Treacy

||| [[Form-Database-Automation-Architecture.md]] | Form-Database-Automation Architecture

||| [[XMATCH-for-Form-Level-Duplicate-Detection.md]] | XMATCH for Form-Level Duplicate Detection

||| [[COUNTA-UNIQUE-for-Duplicate-Warning-Banner.md]] | COUNTA(UNIQUE) for Duplicate Warning Banner

||| [[Data-Entry-Form-Best-Practices.md]] | Data Entry Form Best Practices

||| [[Office-Scripts-Form-Database-Automation.md]] | Office Scripts for Form-Database Automation

||| [[Source-Dynamic-Drop-Down-Lists-Mynda-Treacy.md]] | Source: Dynamic Drop-Down Lists — Mynda Treacy

||| [[Auto-Updating-Dropdowns-via-Excel-Table.md]] | Auto-Updating Dropdowns via Excel Table

||| [[Named-Ranges-TOCOL-Cross-Sheet-Dropdowns.md]] | Named Ranges + TOCOL for Cross-Sheet Dropdowns

||| [[Cascading-Dropdowns-SORT-FILTER-XLOOKUP.md]] | Cascading Dropdowns with SORT + FILTER + XLOOKUP

||| [[XLOOKUP-AutoFill-Related-Data-from-Dropdown.md]] | XLOOKUP for Auto-Filling Related Data

||| [[FILTER-UNIQUE-SORT-Excluding-Dropdown-Items.md]] | FILTER + UNIQUE + SORT for Excluding Dropdown Items

||| [[TOCOL-Ignore-Blanks-for-Clean-Dropdown-Lists.md]] | TOCOL with Ignore Blanks for Clean Dropdown Lists

||| [[Search-as-You-Type-in-Modern-Excel-Dropdowns.md]] | Search-as-You-Type in Modern Excel Dropdowns

||| [[Source-Excel-File-Protection-Tricks-Mynda-Treacy.md]] | Source: Excel File Protection Tricks — Mynda Treacy

||| [[Unlock-Input-Cells-Protect-Sheet-Workflow.md]] | Unlock-Input-Cells-Protect-Sheet Workflow

||| [[Locked-Hidden-Protect-Sheet.md]] | Locked + Hidden + Protect Sheet

||| [[Protect-Sheet-vs-Protect-Workbook.md]] | Protect Sheet vs Protect Workbook

||| [[Very-Hidden-Sheets-VBA-Editor.md]] | Very Hidden Sheets via VBA Editor

||| [[Document-Inspector-Remove-Personal-Information.md]] | Document Inspector: Remove Personal Information

||| [[Encrypt-Workbook-with-Password.md]] | Encrypt Workbook with Password

||| [[Excel-Protection-Methods-Security-Comparison.md]] | Excel Protection Methods: Security Comparison

|||| [[Source-REPT-In-Cell-Charts-Mynda-Treacy.md]] | Source: Excel REPT Function In Cell Charts — Mynda Treacy

In-cell bar charts, progress bars, star ratings. Formula-driven without chart objects. Monospaced font required. |
|||| [[Source-HYPERLINK-Function-Mynda-Treacy.md]] | Source: Excel HYPERLINK Function — Mynda Treacy

||| [[CELL-address-Dynamic-Cell-Reference-Retrieval.md]] | CELL("address") for Dynamic Cell Reference Retrieval

||| [[HYPERLINK-Syntax-Sheet-Name-Quoting.md]] | HYPERLINK Syntax and Sheet-Name Quoting

||| [[Sheet-Navigation-TOC-HYPERLINK.md]] | Sheet Navigation TOC via HYPERLINK + #

||| [[File-Folder-Hyperlinks.md]] | File and Folder Hyperlinks via HYPERLINK

||| [[Dynamic-Hyperlink-XLOOKUP-CELL.md]] | Dynamic Hyperlink to Matching Row via HYPERLINK + XLOOKUP + CELL

||| [[Broken-File-Paths-HYPERLINK-Does-Not-Validate.md]] | Broken File Paths — HYPERLINK Does Not Validate

||| [[CtrlK-Static-vs-Formula-Dynamic-Hyperlink.md]] | Ctrl+K Static vs Formula-Based Dynamic Hyperlink

||| [[excel-great-for-analysis-not-long-term-storage.md]] | Excel Great for Analysis Not Long Term Storage Atomic

Right for ad-hoc/share/non-SQL; wrong for systems of record; personal tool vs shared system. |
| [[Source-5-Boring-Excel-Functions-Mynda-Treacy.md]] | Source: 5 Boring Excel Functions — Mynda Treacy

Mynda Treacy / My Online Training Hub (2026-07-21). Five underrated Excel functions: ABS (misleading % change), SIGN (double-counting in SUMPRODUCT OR), REPT (in-cell bar charts), TRUNC (whole quantities, not INT), CELL (dynamic worksheet name). No Microsoft 365 required. |
| [[ABS-Absolute-Value.md]] | ABS: Absolute Value

=ABS(number). Removes sign. Fixes % change formula when prior year is negative. Invoice tolerance: =IF(ABS(Invoice-PO)<=PO*0.1,"OK","Check"). Available in all Excel versions. |
| [[SIGN-Function-OR-Logic-SUMPRODUCT.md]] | SIGN: OR Logic in SUMPRODUCT

=SIGN((Units>100)+(Price>20)). SIGN collapses OR condition sum: 0→0, 1→1, 2→1. Prevents double-counting rows where both conditions are TRUE. |
|| [[REPT-Function.md]] | REPT — Repeat Text

=REPT(text, number_times). Repeats text N times. Decimals truncated (rounds down). Use with ROUND for percentages. No M365 required. |
|| [[REPT-In-Cell-Bar-Charts-REPT.md]] | In-Cell Bar Chart with REPT

=REPT("█", [@Sales]/MAX([Sales])*20). Proportional bar chart inside cells; combine with CF for colour thresholds. Requires Consolas. |
|| [[Progress-Bar-REPT-LET.md]] | Progress Bar with REPT + LET

=LET(width,20, filled,ROUND([@[Completion Rate]]*width,0), REPT("█",filled)&REPT("▒",width-filled)). Two-section progress bar: filled + remainder. |
|| [[Star-Rating-REPT.md]] | Star Rating with REPT

=REPT("★",[@Score])&REPT("☆",5-ROUNDDOWN([@Score],0)). Filled/unfilled stars from numeric score. UNICHAR(9733/9734) generates symbols. |
|| [[REPT-Rounds-Decimals-Down.md]] | REPT Rounds Decimals Down, Not Nearest

=REPT("█",3.9) returns 3 blocks. REPT truncates — use ROUND, ROUNDDOWN, or ROUNDUP before passing to REPT. |
|| [[REPT-vs-Conditional-Formatting-Data-Bars.md]] | REPT vs CF Data Bars

CF Data Bars: faster setup, built-in axis. REPT: formula-driven length, progress bars, star ratings, CF font colour combination. |
|| [[Monospaced-Font-for-REPT-Bars.md]] | Monospaced Font Required for REPT Bar Alignment

Non-monospaced fonts make REPT bars appear uneven. Use Consolas, Courier New, or Lucida Console. |
| [[TRUNC-vs-INT-Negative-Numbers.md]] | TRUNC vs INT: Negative Number Behavior

TRUNC moves toward zero (-150.50 → -150). INT always rounds down (-150.50 → -151). Always use TRUNC when negatives are possible. TRUNC splits dollars/cents, MOD calculates remainder. |
| [[CELL-Function-Dynamic-Worksheet-Name.md]] | CELL: Dynamic Worksheet Name

=MID(CELL("filename",A1), FIND("]",CELL("filename",A1))+1, 31). Extracts sheet name from workbook path. Dynamic report titles that update on sheet rename. Requires saved workbook. |


## References — File Import Functions (Mynda Treacy, 2026-02)

||| [[IMPORTCSV-IMPORTTEXT-Reference.md]] | IMPORTCSV and IMPORTTEXT: Spill-Based File Import Functions |

IMPORTCSV for CSV files; IMPORTTEXT for custom-delimiter or fixed-width text files. Both return dynamic arrays that spill into the grid — no Power Query, no hidden steps. Parameters: skip_rows, take_rows, locale, encoding. Refresh via Data tab → Refresh All. Full transparency: every import decision visible in the formula bar. |

## Patterns — Dynamic Array Processing (Mynda Treacy, 2026-02)

||| [[IMPORTCSV-CHOOSECOLS-GROUPBY-Summarization-Pattern.md]] | LET + CHOOSECOLS + GROUPBY on Imported Text File |

Chain IMPORTTEXT into LET + CHOOSECOLS + GROUPBY for in-formula summarization — no intermediate tables. LET stores the import; CHOOSECOLS extracts columns; GROUPBY groups and sums. Works entirely in the grid. FILTER before GROUPBY for conditional summaries. |

## Sources — Excel (Mynda Treacy, 2026-02)

||| [[Source-Treacy-IMPORTCSV-IMPORTTEXT.md]] | IMPORTCSV and IMPORTTEXT Functions Explained |

Two new Excel import functions: IMPORTCSV (CSV) and IMPORTTEXT (delimiter/fixed-width). LET + CHOOSECOLS + GROUPBY on imported data. When to use vs Power Query. MyOnlineTrainingHub. 2026-02-03. |
||| [[Source-Google-Maps-Excel-Integration-Tony-Phillips.md]] | Google Maps + Excel Integration

Export Excel location data to Google My Maps: single-sheet prep, column mapping, import, pin styling, layers, reimport. Tony Phillips, How-To Geek 2026-07-29. |


## Imported from Raindrop / Medium Reading List
- [[6-effective-excel-visualizations-you-can-build-in-under-10-minutes|6 effective Excel visualizations you can build in under 10 minutes]]
- [[6-excel-ui-changes-you-need-to-make-before-starting-your-next-spreadsheet|6 Excel UI changes you need to make before starting your next spreadsheet]]
- [[6-ways-to-recover-lost-work-in-microsoft-excel|6 ways to recover 'lost' work in Microsoft Excel]]
- [[Author-Mynda-Treacy|Author Mynda Treacy]]
- [[CHANGELOG|Changelog]]
- [[a-framework-for-tactical-software-in-excel-vba-build-whole-universes-with-only-a|A Framework for Tactical Software in Excel VBA Build whole universes with only a knife and string. Don’t Hang Up This]]
- [[a-framework-for-tactical-software-in-excel-vba-by-mark-ceraldi-feb-2026-level-up|A Framework for Tactical Software in Excel VBA | by Mark Ceraldi | Feb, 2026 | Level Up Coding]]
- [[analyse-monthly-figures-with-excel-vba-i-work-with-excel-in-my-day-job-and-am-al|Analyse monthly figures with Excel VBA I work with Excel in my day job and am always on the lookout for ways that I can]]
- [[beyond-basic-excel-formulas-why-lambda-helper-functions-are-the-new-normal|Beyond basic Excel formulas: Why LAMBDA helper functions are the new normal]]
- [[boris-workflow-is-excellent-his-colleagues-do-it-differently-git-worktrees-two-c|Boris’ workflow is excellent. His colleagues do it differently. Git worktrees, two-Claude review, voice dictation, and]]
- [[excel-has-a-better-way-to-filter-databut-most-people-ignore-it|Excel has a better way to filter data—but most people ignore it]]
- [[forget-the-zoom-slider-use-this-2-second-excel-trick-to-see-exactly-what-you-nee|Forget the zoom slider: Use this 2-second Excel trick to see exactly what you need]]
- [[from-spreadsheet-to-slides-automating-excel-and-powerpoint-with-claude-ai-a-prac|From Spreadsheet to Slides: Automating Excel and PowerPoint with Claude AI A practical guide to saving hours of manual]]
- [[how-i-turned-an-ugly-spreadsheet-into-an-ai-assisted-app-with-antigravity-my-vib|How I Turned an Ugly Spreadsheet into an AI Assisted App with Antigravity My vibe coded app “TalkScount” demo I have a]]
- [[how-to-name-excel-objects-like-a-software-dev|How to name Excel objects like a software dev]]
- [[i-finally-started-using-python-in-excel-and-i-should-have-sooner|I finally started using Python in Excel and I should have sooner]]
- [[i-found-a-better-way-than-pivottables-in-excel-and-its-not-a-function|I found a better way than PivotTables in Excel, and it's not a function]]
- [[i-thought-ai-was-just-for-chat-until-i-used-it-to-automate-excel-and-powerpoint|I thought AI was just for chat – until I used it to automate Excel and PowerPoint]]
- [[importcsv-importtext-excel-university|IMPORTCSV IMPORTTEXT - Excel University]]
- [[picking-up-money-with-excel-vba-introduction-this-article-invites-non-programmer|Picking up Money with Excel VBA Introduction This article invites non-programmers to learn coding at work by building]]
- [[standing-in-the-narrowing-gap-where-ai-still-needs-us-in-november-2022-i-tried-c|Standing in the Narrowing Gap Where AI Still Needs Us In November 2022, I tried ChatGPT for the first time. I asked it]]
- [[stop-building-rigid-excel-formulas-use-isomitted-to-create-more-adaptable-tools|Stop building rigid Excel formulas: Use ISOMITTED to create more adaptable tools]]
- [[stop-dragging-formulas-in-excel-use-makearray-to-generate-them-dynamically|Stop dragging formulas in Excel: Use MAKEARRAY to generate them dynamically]]
- [[stop-using-pie-charts-in-excel-build-this-dynamic-bar-chart-instead|Stop using pie charts in Excel: Build this dynamic bar chart instead]]
- [[the-3-tab-rule-how-to-structure-your-excel-file-like-a-software-developer|The 3-tab rule: How to structure your Excel file like a software developer]]
- [[the-excel-formula-i-use-whenever-na-takes-over-a-sheet|The Excel formula I use whenever #N/A takes over a sheet]]
- [[these-7-conditional-formatting-formulas-turn-excel-into-an-automated-alert-syste|These 7 conditional formatting formulas turn Excel into an automated alert system]]
- [[this-excel-tool-can-predict-future-trendsbut-you-probably-never-knew-it-existed|This Excel tool can predict future trends—but you probably never knew it existed]]
- [[this-terminal-tool-is-my-favorite-way-to-view-spreadsheets-on-my-computer|This terminal tool is my favorite way to view spreadsheets on my computer]]
- [[when-not-to-use-tables-in-excel-5-scenarios-where-regular-ranges-are-better|When not to use tables in Excel: 5 scenarios where regular ranges are better]]
- [[you-dont-need-vba-to-auto-refresh-your-power-queries-in-excel|You don't need VBA to auto-refresh your Power Queries in Excel]]
- [[you-need-to-know-what-the-hash-sign-does-in-excel-formulas|You need to know what the hash sign does in Excel formulas]]
- [[your-excel-pivottable-isnt-complete-until-you-add-these-two-pro-level-features|Your Excel PivotTable isn't complete until you add these two pro-level features]]
- [[youre-picking-the-wrong-charts-let-excels-new-agent-mode-decide-for-you|You're picking the wrong charts — let Excel's new Agent Mode decide for you]]


## Imported from Raindrop / Medium Reading List
- [[6-excel-features-i-use-in-every-spreadsheet-i-create|6 Excel features I use in every spreadsheet I create]]
- [[excel-was-my-database-for-15-years-and-postgres-ended-that-in-a-weekend|Excel was my database for 15 years, and Postgres ended that in a weekend]]
- [[google-maps-took-my-excel-spreadsheet-to-the-next-level-with-this-little|Google Maps took my Excel spreadsheet to the next level with this little]]
- [[how-to-connect-to-an-excel-workbook-in-power-bi-desktop-go-analytics|[How To] Connect to an Excel Workbook in Power BI Desktop – Go Analytics]]
- [[i-made-a-dynamic-excel-timeline-in-10-minutes-and-you-can-too|I made a dynamic Excel timeline in 10 minutes (and you can too)]]
- [[i-started-using-python-in-excel-for-boring-tasks-and-it-completely-changed-my-wo|I started using Python in Excel for boring tasks, and it completely changed my workflow]]
- [[i-stopped-manually-naming-ranges-in-excelthis-little|I stopped manually naming ranges in Excel—this little]]
- [[the-easy-guide-to-excel-automation-with-office-scripts|The Easy Guide To Excel Automation With Office Scripts]]


## Imported from Raindrop / Medium Reading List
- [[automate-unlocked-for-excel-users-part-collection-functions-7cb477d51e51|Automate Unlocked For Excel Users Part Collection Functions 7cb477d51e51]]
- [[automate-unlocked-for-excel-users-part-logical-comparison-and-math-functions-5c6|Automate Unlocked For Excel Users Part Logical Comparison And Math Functions 5c605f91013a]]
- [[automate-unlocked-for-excel-users-string-functions-2dd27a0d2e2e|Automate Unlocked For Excel Users String Functions 2dd27a0d2e2e]]
- [[criteria-lookups-in-excel-five-methods-to-master-a6c22aaa5df0|Criteria Lookups In Excel Five Methods To Master A6c22aaa5df0]]
- [[excel-automation-batch-merge-multiple-excel-files-ff2cee74f799|Excel Automation Batch Merge Multiple Excel Files Ff2cee74f799]]
- [[excel-chaos-to-ai-insights-real-data-analyst-workflow-with-excel-sql-python-gene|Excel Chaos To Ai Insights Real Data Analyst Workflow With Excel Sql Python Generative Ai Ce9ee1aed9f2]]
- [[excel-data-cleaning-hacks-that-save-hours-every-week-36a6f48995ee|Excel Data Cleaning Hacks That Save Hours Every Week 36a6f48995ee]]
- [[excel-formulas-and-functions-with-python-complete-guide-e8eff4634d9e|Excel Formulas And Functions With Python Complete Guide E8eff4634d9e]]
- [[excel-formulas-every-power-bi-developer-should-know-2f562acf8157|Excel Formulas Every Power Bi Developer Should Know 2f562acf8157]]
- [[excel-how-to-copy-without-incrementing-65a4b508d22b|Excel How To Copy Without Incrementing 65a4b508d22b]]
- [[excel-lambda-functions-select-distinct-2da159618dbb|Excel Lambda Functions Select Distinct 2da159618dbb]]
- [[excel-time-saving-hacks-for-daily-work-ebe3224493f9|Excel Time Saving Hacks For Daily Work Ebe3224493f9]]
- [[excel-to-power-bi-my-personal-roadmap-for-an-easy-transition-without-losing-my-s|Excel To Power Bi My Personal Roadmap For An Easy Transition Without Losing My Sanity 643e3d162011]]
- [[excels-superpower-fileèsùter-unique-sort-and-choose-data-magic-b5dbeeb02f0d|Excels Superpower Fileèsùter Unique Sort And Choose Data Magic B5dbeeb02f0d]]
- [[excels-superpower-filter-unique-sort-and-choose-data-magic-b5dbeeb02f0d|Excels Superpower Filter Unique Sort And Choose Data Magic B5dbeeb02f0d]]
- [[hacked-power-bi-to-let-users-copy-paste-data-directly-to-excel-709386b1fd4a|Hacked Power Bi To Let Users Copy Paste Data Directly To Excel 709386b1fd4a]]
- [[how-to-connect-to-an-excel-workbook-in-power-bi-desktop-go-analytics|[How To] Connect to an Excel Workbook in Power BI Desktop – Go Analytics]]
- [[in-excel-for-project-management-smarter-gantt-charts-and-trackers-154af9d95273|In Excel For Project Management Smarter Gantt Charts And Trackers 154af9d95273]]
- [[lists-in-excel-select-distinct-a5d8adb629a8|Lists In Excel Select Distinct A5d8adb629a8]]
- [[multi-criteria-lookups-in-excel-with-xlookup-and-sumproduct-58bcc2dd2606|Multi Criteria Lookups In Excel With Xlookup And Sumproduct 58bcc2dd2606]]
- [[non-adjacent-column-pairs-in-excel-c8ac3473fee2|Non Adjacent Column Pairs In Excel C8ac3473fee2]]
- [[python-into-excel-new-era-of-data-analysis-211e25377693|Python Into Excel New Era Of Data Analysis 211e25377693]]
- [[replaced-47-excel-files-with-one-power-bi-model-heres-what-actually-happened-d7f|Replaced 47 Excel Files With One Power Bi Model Heres What Actually Happened D7f1fba4db98]]
- [[to-automatically-audit-excel-files-using-python-593512425f68|To Automatically Audit Excel Files Using Python 593512425f68]]
- [[to-convert-csv-to-excel-xlsx-in-pow2ùer-automate-da0e40d9953d|To Convert Csv To Excel Xlsx In Pow$2ùer Automate Da0e40d9953d]]
- [[vlookup-unleashing-excels-true-data-power-for-business-analysis-33e9c54a66c4|Vlookup Unleashing Excels True Data Power For Business Analysis 33e9c54a66c4]]
- [[vs-excel-formulas-whats-the-real-difference-ddde000ea666|Vs Excel Formulas Whats The Real Difference Ddde000ea666]]
[[6-excel-features-i-use-in-every-spreadsheet-i-create]]
[[Author-Mynda-Treacy]]
[[CHANGELOG]]
[[excel-was-my-database-for-15-years-and-postgres-ended-that-in-a-weekend]]
[[google-maps-took-my-excel-spreadsheet-to-the-next-level-with-this-little]]
[[how-to-connect-to-an-excel-workbook-in-power-bi-desktop-go-analytics]]
[[i-made-a-dynamic-excel-timeline-in-10-minutes-and-you-can-too]]
[[i-started-using-python-in-excel-for-boring-tasks-and-it-completely-changed-my-wo]]
[[i-stopped-manually-naming-ranges-in-excelthis-little]]
[[the-easy-guide-to-excel-automation-with-office-scripts]]
