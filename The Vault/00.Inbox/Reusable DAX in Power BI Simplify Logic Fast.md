---
title: "Reusable DAX in Power BI: Simplify Logic Fast"
source: "https://databear.com/reusable-dax-power-bi/"
author:
  - "[[Boniface Muchendu]]"
published: 2025-12-10
created: 2026-08-04
description: "Learn how to use reusable DAX in Power BI to clean up your measures, reduce code, and simplify logic using custom user-defined functions."
Processed: "Unprocessed"
---
**Reusable DAX in Power BI** can save you hours of repetitive work. By turning common logic into reusable custom functions, you reduce duplication and simplify your models. Whether you’re managing enterprise reports or building team dashboards, **reusable DAX in Power BI** makes your code cleaner, smarter, and easier to maintain.

##### Step 1: Enable User Defined Functions in Power BI

To get started with UDFs, you’ll need to enable them:

1. Go to **File > Options > Preview Features**
2. Scroll down and enable **User Defined Functions**
3. Restart Power BI Desktop

Once enabled, you can define functions in **DAX Query View** or using **TMDL**.

##### Step 2: The Use Case Simplifying Repeated Logic

Imagine this scenario: you want to return the **top 3 products**, **top customer**, or **top sales region**. You’re using the same logic repeatedly just with different columns, measures, or top-N values.

Instead of writing several versions of nearly identical DAX measures, you can:

- Define a single **UDF**
- Pass in different parameters
- Reuse it for all similar use cases

##### Step 3: Define Your First Power BI UDF

Here’s an example function that returns a **top-N list** as a concatenated string:

```
define function _TopNItems = 
(
    _measure: scalar decimal expression, 
    _column: anyref expression, 
    _topN: numeric val
) =>
VAR _Table = 
    TOPN(
        _topN, 
        SUMMARIZECOLUMNS(_column, "Value", _measure), 
        [Value]
    )
RETURN CONCATENATEX(_Table, _column, ", ")
```

##### Breakdown:

- **\_measure**: Any DAX measure (like Total Sales)
- **\_column**: The column to rank by (like Product Name)
- **\_topN**: The number of items to return

This UDF is completely dynamic and reusable.

##### Step 4: Test Your UDF in Query View

You can call the function like this:

```
EVALUATE
ROW(
    "Top Product", _TopNItems([Total Sales], 'Product'[Product Name], 1)
)
```

Or change the column and N to return the top 2 products, top customer, etc.

UDFs let you plug in any measure, column, and number saving you from duplicating code.

##### Step 5: Convert the Result into a Measure

Want to use this in your reports?

Just create a new measure that uses your UDF:

```
Top 2 Products = _TopNItems([Total Sales], 'Product'[Product Name], 2)
```

Now, instead of 3 or 5 nearly identical measures, you can create all of them using just **one line each**.

##### Tips for Power BI UDF Parameters

When defining your function, use parameter modes carefully:

- `expression`: Evaluates the input in the current filter context (recommended for measures)
- `val`: Evaluates before the function (may result in incorrect context)

Also, prefix function and parameter names with `_` to avoid conflicts with reserved DAX keywords.

##### Key Benefits of Using Power BI UDFs

**Less Repetition**  
**Cleaner Code**  
**Reusability**  
**More Flexible Models**  
**Easier Maintenance**

Instead of duplicating logic across dozens of measures, you centralize your logic and adapt it through parameters.

##### Final Thoughts

**Power BI UDFs** are one of the most exciting additions to DAX in recent years. They make your models more scalable, your measures more maintainable, and your workflow faster.

If you’re dealing with similar DAX patterns across multiple measures, it’s time to modularize and simplify using UDFs.

##### Learn More

[**Explore Power BI Training by Data Bear**](https://databear.com/power-bi-training/)  
From fundamentals to advanced techniques like UDFs, Calculation Groups, and model optimization, their courses will help you sharpen your Power BI skills.