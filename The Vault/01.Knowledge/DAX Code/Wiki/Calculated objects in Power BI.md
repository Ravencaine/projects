---
created: 2026-07-27
source: "Calculated objects in Power BI"
source_url: https://medium.com/@2020ec0712/calculated-objects-in-power-bi-f92d04228349
note_type: source
tags: [dax-code]
---

(Article for beginners)

Data Analysis Expressions (DAX) is a very powerful language used for modeling in Power BI. There are four standard, explicit calculated objects (in terms of DAX) in Power BI — Calculated columns, Calculated tables, Measures and Calculation groups.


Calculated columns:

Calculated columns, as the name suggests, are columns added to the chosen table based on some logic written in DAX. Like the other columns in the table, this will have as **many values** as there are rows in the table because calculated columns use a **row context**. They do increase model size, although Power BI’s VertiPaq engine compresses data, so the impact may not always be significant. They are **calculated during refresh** and are **stored in the model permanently**. It is important to analyze if a DAX-based calculated column is actually required. If the same task can be performed at the source or in the Power Query layer, it should be done there because it does not affect the performance as much as a calculated column. Some scenarios where a calculated column is the only feasible solution are:

- **When a calculation depends on another DAX logic** like a calculated column or a measure — because measures are in the DAX ecosystem and Power Query cannot see them.
- **When complex cross-table logic is involved** — if something needs to be calculated based on a relationship that only exists in the model, performing the calculation using DAX is the simplest way because doing it with Power Query (using merges) can be memory-intensive for large datasets.

Calculated tables:

Calculated tables are very similar to Calculated columns. The only difference is that calculated columns return columns as results while **calculated tables return tables as results**. Calculated tables can be of two types — one, it can be a filtered dataset from existing tables. For example, from a table called ‘Students’ that has student details, you filter out all the rows where ‘Marks’ are greater than 80 and save it as a table called ‘HighPerformingStudents’. This becomes a Calculated Table. Another type of Calculated table can be a newly created table with calculated columns based on other tables in the model. For example, from a table called ‘Sales’, you calculate a column ‘SalesAmount’ as Quantity \* Price and add this column to a fresh table called ‘FinalSalesAmount’. But, creating a calculated table in such scenarios is usually not recommended unless you need a separate table for modeling purposes. Instead, you can add the column to the ‘Sales’ table itself. One of the most common use cases for calculated tables is creating **date tables**.

Measures:

Measures are the **most popular calculated objects** in a model. They are simple yet powerful and help take reporting to the next level. Unlike calculated columns and calculated tables, measures do not return multiple rows of values. They **return a single value**. A measure is calculated every time a visual requires it, based on the current filters and hence is said to use a **filter context**. What this means is that it is **not already computed and it is never stored**. Based on the filters applied each time, the dataset gets filtered and the measure is **computed afresh using the filtered dataset**. And if no filter is applied, it will work on the whole dataset. If row-level granularity is not required and an aggregated value is enough for your use case, **go for measures instead of calculated columns for good performance**. Measures **take up almost no storage space**, but they are computed on the fly each time, which can impact performance for complex calculations. When multiple visuals with multiple measures are used, the rendering time of the report could increase significantly.

Calculation groups:

When we create measures, the results may be dynamic based on filters, but the underlying calculation logic remains fixed. What if we could make even the measure’s calculation logic dynamic? This is where calculation groups come in. Calculation groups help us to create **reusable logic for existing measures** so that we **do not have to create multiple similar measures**. For example, if in the ‘Students’ table, there are different columns for marks in Math, Science etc. and each of them requires some specific calculations (say Percentage). We could create that logic in a calculation group so that we do not need to create individual measures for each of these calculations for each subject. In the future, if another subject’s marks gets added as a column to the table, creating just a base measure (sum of all values in the column) would suffice. The other calculations can be handled using calculation groups. Each item inside a calculation group is called a **calculation item**.

The crux of calculation groups lies in the **SELECTEDMEASURE()** function. It is what enables the usage of base measures like a variable inside the calculation item’s DAX logic. A calculation group does not return a value on its own, it is useful only with measures. It allows the calculation to dynamically apply to whichever measure is currently being used in a visual. Here is an example:

**Base measures:**  
□ Total Sales = SUM(Sales\[Amount\])  
□ Total Profit = SUM(Sales\[Profit\])  
□ Total Units sold = SUM(Sales\[Units\])

**Calculation items in a Calculation group called ‘Time Intelligence’:**  
□ Current Year = SELECTEDMEASURE()  
□ Previous Year = CALCULATE(  
SELECTEDMEASURE(),  
SAMEPERIODLASTYEAR(Date\[Date\])  
)  
□ YOY Growth = DIVIDE(  
SELECTEDMEASURE() — CALCULATE(SELECTEDMEASURE(),SAMEPERIODLASTYEAR(Date\[Date\])),  
CALCULATE(SELECTEDMEASURE(), SAMEPERIODLASTYEAR(Date\[Date\]))  
)

Now, **add the calculation group to a slicer**. All measures in visuals affected by this slicer will change based on the selected value. If you do not want a measure to be affected by the calculation group but still need to use it in a visual influenced by the slicer, in the base measure’s logic which you want to bypass, add a line called **REMOVEFILTERS(‘calculation\_group\_name’)**. This way, that particular measure will not be affected by the different dynamic logics of the calculation items.

To get started with these calculated objects, a basic understanding of DAX is required. Once you get a grasp of the syntax and functioning of DAX, working around with these objects becomes very easy and straightforward.

To summarize what we saw in this article:

> See also [[all]] for reference.


> See also [[calculate]] for reference.


> See also [[calculate-table]] for reference.


> See also [[filter-context-vs-row-context]] for reference.


> See also [[removefilters]] for reference.


> See also [[power-query-etl-workflow]] for reference.
