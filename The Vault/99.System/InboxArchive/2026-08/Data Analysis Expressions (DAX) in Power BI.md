---
title: "Data Analysis Expressions (DAX) in Power BI"
source: "https://medium.com/@dibyanshusharma16/data-analysis-expressions-dax-in-power-bi-968ecef4335b"
author:
  - "[[Dibyanshu Sharma]]"
published: 2025-12-21
created: 2026-08-03
description: "More"
Processed: "Unprocessed"
---
DAX Cheat Sheet Link — [https://docs.google.com/spreadsheets/d/1vIPbh7mz8ZQcLxXDkrTuxBwHvgRlQYQ9\_OIqurzPKKs/edit?usp=sharing](https://docs.google.com/spreadsheets/d/1vIPbh7mz8ZQcLxXDkrTuxBwHvgRlQYQ9_OIqurzPKKs/edit?usp=sharing)

![](99.System/Attachments/1!ENfkKW836wi23YYENwEtvQ.png.webp)

DAX Guide (Good website to understand dax) — [https://dax.guide/calculate/](https://dax.guide/calculate/)

![](99.System/Attachments/1!2BIFxIrErvsjnu60uK1zgA.png.webp)

## The Nature of DAX

DAX is a formula language used in Power BI, Azure Analysis Services, and Power Pivot in Excel. It is designed to perform dynamic aggregation on large datasets. Unlike SQL, which is primarily a declarative language for retrieving sets of data, DAX is a functional language designed to calculate scalar values and tables based on user-interaction contexts. When a user filters a report by “Year = 2024” and “Region = North,” the DAX engine dynamically recalculates every measure on the canvas to reflect this specific slice of reality. This dynamic responsiveness is what separates a static report from an interactive analytical model.

The language comprises functions, operators, and constants that can be combined in formulas to calculate and return values. It is instrumental in creating new information from data already present in the model, whether through calculated columns, measures, or calculated tables.

## 2\. Architectural Foundations: The VertiPaq Engine

To understand why DAX behaves the way it does, one must understand the underlying storage engine. Power BI uses the VertiPaq engine, an in-memory columnar database.

## 2.1 Columnar Storage vs. Row Storage

Traditional databases (like SQL Server) store data in rows. To retrieve the “Sales Amount” for a specific transaction, the database reads the entire row. VertiPaq, however, stores data in columns. If a query requests the sum of “Sales Amount,” the engine scans only that specific column, ignoring the rest of the table structure. This architecture allows for massive compression and speed, particularly for aggregation operations like `SUM` or `AVERAGE`. However, it implies that operations requiring row-by-row context (iterators) must be explicitly handled by the engine, creating a performance distinction between "aggregators" and "iterators" that will be explored in later sections.

## 2.2 Compression and Encoding

The engine compresses data using techniques like Value Encoding (storing the mathematical difference from a base value), Hash Encoding (creating a dictionary of unique values), and Run-Length Encoding (compressing repeated values). This has practical implications for DAX developers: columns with high cardinality (many unique values, like IDs or high-precision timestamps) compress poorly and slow down the model. Therefore, DAX functions that generate high-cardinality columns (like calculated columns with unique identifiers) should be used judiciously.

## 2.3 The Tabular Object Model (TOM)

DAX operates within a semantic model known as the Tabular Object Model. This model consists of:

- **Tables**: Collections of columns.
- **Relationships**: Connections between tables, typically One-to-Many, which allow filters to propagate from dimension tables (e.g., Customers, Products) to fact tables (e.g., Sales).
- **Measures**: Formulas that calculate results dynamically based on the current filter context.
- **Calculated Columns**: Static columns computed at data refresh time and stored in the model.

## 3\. The Physics of DAX: Evaluation Contexts

The single most critical concept in DAX is **Evaluation Context**. It is the environment in which a formula is calculated. Without mastering context, DAX formulas will produce numbers that look correct but are fundamentally wrong. There are two primary types of context: **Row Context** and **Filter Context**.

## 3.1 Row Context

Row context can be thought of as “the current row.” It is the knowledge of the specific record being processed.

- **In Calculated Columns**: Row context exists automatically. If you write `Price * Quantity` in a calculated column, DAX knows to take the price from the current row and multiply it by the quantity from the *same* row.
- **In Measures**: Row context does *not* exist automatically. Measures operate on aggregates. To use row context in a measure, you must create it explicitly using an iterator function (ending in ‘X’, like `SUMX` or `FILTER`).

## 3.2 Filter Context

Filter context represents the set of active filters at the moment of calculation. It is the result of the user’s interaction with the report.

- **Sources of Filter Context**:
1. **Slicers**: A user selects “2023” in a year slicer.
2. **Visual Coordinates**: A bar chart typically filters data by the category on its axis (e.g., “Product A”).
3. **Cross-Highlighting**: Clicking a pie chart segment filters other visuals.
4. **Page/Report Filters**: Fixed filters applied in the filter pane.
5. `CALCULATE`: The DAX function that can programmatically add, remove, or modify filter context.

## 3.3 Context Transition

This is the advanced mechanism where a Row Context is transformed into a Filter Context. This happens automatically when a measure is used inside another expression or when `CALCULATE` is invoked. It is the secret sauce that allows measures to be reused effectively but can also lead to circular dependency errors if not managed correctly.

## 4\. Aggregation Functions: The Core Arithmetic

Aggregations are the most basic yet essential operations in DAX. They reduce a column of values into a single scalar number.

## 4.1 Basic Aggregators

The standard aggregators are intuitive and mirror Excel functionality, but with the power of the VertiPaq engine behind them.

**Table 4.1: Standard Aggregation Functions**

![](99.System/Attachments/1!X-fhV11wccCAGQYavPiBMA.png.webp)

![](99.System/Attachments/1!W47G2TTGddQnpPKPAZd1WQ.png.webp)

![](99.System/Attachments/1!WdU93lEb1ea1mBO6Fnw0Mg.png.webp)

![](99.System/Attachments/1!RiHufFe2wQnqqDswYFTvqg.png.webp)

![](99.System/Attachments/1!sGtyvjWDiVVpp5gG41F7wQ.png.webp)

![](99.System/Attachments/1!za1S7IPdAtwGeErhPwQiBA.png.webp)

![](99.System/Attachments/1!-sIhFpy55PYfCLygsXiveA.png.webp)

![](99.System/Attachments/1!3WYl5NNdz2lbDyAcAozA1g.png.webp)

## 4.2 Iterator Functions (The “X” Functions)

While aggregators scan columns, iterators loop through tables row by row. This is necessary when a calculation must happen *before* the aggregation. For example, to calculate total revenue, one cannot simply `SUM(Price) * SUM(Quantity)` because that would multiply the total price of everything by the total quantity of everything. Instead, one must multiply Price \* Quantity for *each row* and then sum the results. This is the purpose of `SUMX`.

![](99.System/Attachments/1!Vc1BQABBbql8smt3EQnGjA.png.webp)

![](99.System/Attachments/1!6oqcTDgj9GSnOicVrn1N5g.png.webp)

![](99.System/Attachments/1!TBRz9pRMv4wSTofKCJP6-g.png.webp)

![](99.System/Attachments/1!MXxCHfaDssQrbRMoNxPw8Q.png.webp)

![](99.System/Attachments/1!qgc_5x3trZeYHGm5oT3s0w.png.webp)

**Deep Dive: SUM vs. SUMX** The distinction between `SUM` and `SUMX` is a classic interview question and a fundamental architectural decision. `SUM` is an aggregation function; `SUMX` is an iterator.

- **Performance**: `SUM` is generally faster because the VertiPaq engine can sum a stored column directly using compressed statistics. `SUMX` forces the engine to materialize a context for every row, perform the calculation, and then aggregate.
- **Recommendation**: If a calculated column for “Total Line Amount” exists in the table, use `SUM`. If it does not, use `SUMX` to calculate it on the fly to save storage space (RAM), trading CPU cycles for memory.

## 4.3 Statistical Aggregations

DAX includes a suite of statistical functions for deeper analysis.

![](99.System/Attachments/1!YTwhY1G85vAHsb5itewkBA.png.webp)

## 5\. Filter Functions: Controlling the Logic

If Aggregations are the engine of DAX, Filter functions are the steering wheel. They allow the developer to modify the context in which data is aggregated, enabling comparisons like “Sales vs. Last Year” or “Red Products as % of All Products.”

## 5.1 The CALCULATE Function

`CALCULATE` is the most powerful function in DAX. It is the only function that can modify the filter context for a calculation.

**Syntax**: `CALCULATE(<Expression>, <Filter1>, <Filter2>,...)`

**Mechanism**:

1. **Copy**: It takes a snapshot of the current filter context.
2. **Modify**: It applies the filter arguments provided.
- If a new filter is on a column not currently filtered, it is **added**.
- If a new filter is on a column already filtered, the old filter is **overwritten** (replaced), unless `KEEPFILTERS` is used.
1. **Evaluate**: It evaluates the expression in this new, modified context.

**Example**: `CALCULATE(SUM(Sales[Amount]), Product[Color] = "Red")` This measure calculates the sum of sales, but it forces the color to be Red, regardless of what the user has selected in a slicer. If the user selects "Blue," `CALCULATE` overrides "Blue" with "Red."

## 5.2 Filter Modifiers

These functions are typically used as arguments inside `CALCULATE`.

**Table 5.1: Filter Modifier Functions**

![](99.System/Attachments/1!W7xhF91ZZfQCXOHQn4QymA.png.webp)

![](99.System/Attachments/1!ffayo7sX-Y8iFdjaHJ8ZVA.png.webp)

**Deep Dive: The** `FILTER` **Function** `FILTER` is an iterator that returns a table.

- **Syntax**: `FILTER(<table>, <condition>)`
- **Usage**: It is often passed to `CALCULATE`.
- **Performance Tip**: `FILTER` scans every row of the table provided. Therefore, `FILTER('Sales',...)` (scanning millions of rows) is much slower than `FILTER('Products',...)` (scanning thousands of rows). Always try to filter the dimension table, not the fact table. The relationship will propagate the filter efficiently.

## 6\. Time Intelligence: Analyzing Trends

Time Intelligence refers to calculations that span time periods: Year-to-Date (YTD), comparisons (YoY), and moving averages. DAX simplifies this via specialized functions that assume a properly marked **Date Table** exists in the model.

## 6.1 Prerequisites: The Date Table

For Time Intelligence to work, the model must have a separate Date table (Calendar dimension) marked as a “Date Table” in the model settings. This table must have contiguous dates (no gaps) covering the entire period of analysis.

## 6.2 Standard Period Aggregations

These functions modify the date context to accumulate values over time.

![](99.System/Attachments/1!BK6gfQql4GDZHnVEkXcxPw.png.webp)

## 6.3 Comparison and Shifting Functions

These functions shift the date window to allow for comparison.

**Table 6.2: Shifting Functions**

![](99.System/Attachments/1!7HDcw6dF85AGCXjU-cFMow.png.webp)

## 6.4 Constructing Dates

Sometimes you need to build dates or calculate durations.

**Table 6.3: Date Construction & extraction**

![](99.System/Attachments/1!1aC7J41Zqh1lqoQndsNJfg.png.webp)

## 7\. Logical and Information Functions

These functions provide decision-making capabilities (IF/THEN) and state awareness (Is this value blank? Is this row filtered?).

## 7.1 Conditional Logic

**Table 7.1: Logical Functions**

![](99.System/Attachments/1!NEkTiYDS8WFUE7hn7yloXg.png.webp)

## 7.2 Information Functions

These functions allow measures to understand the visual context they are rendering in.

**Table 7.2: Information Functions**

![](99.System/Attachments/1!DGOnmf4YMgjxnmu8oxgYlw.png.webp)

![](99.System/Attachments/1!YPJ4P0eT2W6x5LKm7RZkVg.png.webp)

## 8\. Relational and Lookup Functions

Power BI’s strength lies in its relational model. These functions allow DAX to traverse the web of relationships between tables.

## 8.1 Traversing the Model

DAX uses specific functions to “jump” between tables. Note that you cannot simply reference `'TableB'[Column]` from `'TableA'` without these.

**Table 8.1: Relationship Functions**

![](99.System/Attachments/1!iNfUYuRh2Mmzwjs7lbRhuw.png.webp)

## 8.2 Lookups Without Relationships

Sometimes tables are not physically related in the model (disconnected tables).

- `LOOKUPVALUE`: Works like Excel's `VLOOKUP` or SQL's `SELECT` statement.
- **Syntax**: `LOOKUPVALUE(<Result_Col>, <Search_Col>, <Search_Val>,...)`
- **Use Case**: Fetching values when no relationship exists or when circular dependency prevents a relationship.
- **Performance**: Generally slower than `RELATED`. Use `RELATED` whenever a physical relationship exists.

## 9\. Table Manipulation and Virtual Tables

Advanced DAX often involves creating temporary “virtual” tables in memory to perform multi-step analysis. These are not visible to the user but are used within measures.

**Table 9.1: Table Functions**

![](99.System/Attachments/1!57fCcZLs-TMb-bD4QVkfIg.png.webp)

**Strategic Insight: Virtual Tables for Debugging** You can visualize these table functions by creating a “Calculated Table” in Power BI Desktop. This is an excellent way to debug complex DAX: create a physical table to see exactly what `FILTER` or `SUMMARIZE` is returning before embedding it into a measure.

## 10\. Parent-Child Hierarchies

Standard hierarchies (Year > Quarter > Month) are simple. Parent-Child hierarchies (Employee > Manager) where the depth is variable and recursive require specialized “PATH” functions. This is common in HR (Org Charts) and Finance (Chart of Accounts).

**Table 10.1: Path Functions**

![](99.System/Attachments/1!pjVPlvJFKCWTmKgzGm3GZg.png.webp)

**Flattening Strategy**: To use a Parent-Child hierarchy in a standard visual, the best practice is to “flatten” it using calculated columns. Create “Level 1”, “Level 2”, “Level 3” columns using `PATHITEM`, and then build a standard hierarchy in the model.

## 11\. Text and Data Transformation

While Power Query (M) is the preferred place for data cleaning, DAX provides text functions for dynamic presentation logic in reports.

**Table 11.1: Text Functions**

![](99.System/Attachments/1!jETBoHS6BhcANLQnncFHog.png.webp)

## 12\. Optimization and Best Practices

Writing DAX that works is step one. Writing DAX that is fast is step two.

## 12.1 Variables (VAR / RETURN)

Variables are the single best optimization tool.

- **Performance**: A variable is calculated *once* and stored in memory. If you reference the variable 5 times in your return statement, it does not re-calculate.
- **Readability**: They allow you to name intermediate steps.
- **Debugging**: You can change the `RETURN` statement to output a variable to check its value.
- **Context Freezing**: Variables are evaluated in the context where they are defined. This is useful for capturing a value *before* a context transition occurs.

**Example**:Profit Margin = VAR TotalSales = SUM(Sales\[Amount\]) VAR TotalCost = SUM(Sales\[Cost\]) RETURN DIVIDE(TotalSales — TotalCost, TotalSales)

## 12.2 Avoiding Bi-Directional Relationships

Bi-directional filters (Both directions) can cause performance issues and ambiguity. Prefer single-direction relationships and use `CROSSFILTER` in specific measures if upward propagation is needed.

## 12.3 Reducing Cardinality

High cardinality columns (like exact timestamps or unique GUIDs) consume massive memory. If a DateTime column is split into two columns (Date and Time), the cardinality drops significantly, improving compression and performance.

## The Unified DAX Cheatsheet: Reference View

This section consolidates the most critical functions into a dense reference format for quick lookup, satisfying the “One View” requirement.

DAX Cheat Sheet Link — [https://docs.google.com/spreadsheets/d/1vIPbh7mz8ZQcLxXDkrTuxBwHvgRlQYQ9\_OIqurzPKKs/edit?usp=sharing](https://docs.google.com/spreadsheets/d/1vIPbh7mz8ZQcLxXDkrTuxBwHvgRlQYQ9_OIqurzPKKs/edit?usp=sharing)

![](99.System/Attachments/1!ENfkKW836wi23YYENwEtvQ.png.webp)

DAX Guide (Good website to understand dax) — [https://dax.guide/calculate/](https://dax.guide/calculate/)

![](99.System/Attachments/1!2BIFxIrErvsjnu60uK1zgA.png.webp)