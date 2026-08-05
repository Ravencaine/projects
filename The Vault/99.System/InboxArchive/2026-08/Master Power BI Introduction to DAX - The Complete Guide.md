---
title: "Master Power BI: Introduction to DAX — The Complete Guide"
source: "https://medium.com/microsoft-power-bi/master-power-bi-introduction-to-dax-the-complete-guide-93d52ce1846c"
author:
  - "[[Janvi Gupta]]"
published: 2026-01-05
created: 2026-07-29
description: "From Basic Measures to Advanced Calculations"
Processed: "Unprocessed"
---
## From Basic Measures to Advanced Calculations

## Your Data Model is Perfect. Now Make It Answer Questions.

You’ve built a solid data model. Your tables are organized in a clean star schema. Relationships connect everything properly. You tested it, and the numbers are accurate.

But here’s what you realize: your model just sits there. It has raw data — OrderDate, Quantity, Amount — but it doesn’t answer the questions your stakeholders actually ask:

1. What’s our year-to-date revenue compared to last year?
2. Which products are underperforming this quarter?
3. What’s the average order value for enterprise customers?

Your data model is like a well-organized library. DAX is what lets you actually read the books.

![](99.System/Attachments/1!fUsOK_GnLekWoxeiVIQ1xA.png.webp)

This is where DAX comes in. DAX (Data Analysis Expressions) is the language that turns your organized data into business insights. It’s what transforms “here’s a bunch of sales records” into “revenue is up 23% compared to last year.”

If you followed along with our data modeling series, you already have the foundation. Now we’re going to make that foundation work for you.

**🎁** [**Get friend links for all of our 1000> Power BI learning articles here**](https://powerbi-masterclass.short.gy/learning-database?utm_source=medium&utm_medium=medium-post&utm_campaign=database-medium-post-start) **🎁**

## 📑 What We’ll Cover

## 1\. DAX Foundations — What It Is & Why It Matters

## What is DAX?

DAX stands for Data Analysis Expressions. It’s the formula language used in Power BI, Excel Power Pivot, and Analysis Services.

Think of it this way:👉 If your data model is a car’s engine, DAX is how you drive it. The engine can be perfectly built, but without knowing how to drive, you’re not going anywhere.

## Why DAX is NOT Excel Formulas

This is the biggest misconception. You know Excel formulas, so DAX should be easy, right?

Not quite.

**In Excel:**

```c
=SUM(B2:B100)
```

You reference specific cells. The formula calculates those exact cells. Always.

**In Power BI DAX:**

```c
Total Revenue = SUM(Orders[Amount])
```

You reference a column, but what gets calculated changes based on context — what’s selected in slicers, what’s shown in the visual, and which filters are applied.

**The Excel mindset:** “Sum cells B2 through B100” = Always the same result

**The DAX mindset:** “Sum the Amount column, but only for whatever is currently filtered” = Result changes based on context

This context awareness is what makes DAX powerful — and initially confusing.

## What DAX Does for You

**Aggregations:** Sum, count, average your data

**Comparisons:** This year vs last year, actual vs budget, this product vs category average

**Calculations:** Profit margins, growth rates, moving averages

**Business Logic:** “If revenue is over $1M, mark as ‘Enterprise’; otherwise ‘SMB’”

**Time Intelligence:** Year-to-date, quarter-over-quarter, rolling 12 months

## 2\. Your First Basic Measures

Let’s create practical measures using our e-commerce model from the data modeling series.

**Reminder of our tables:**

- Orders (fact table): OrderID, OrderDate, CustomerID, ProductID, Quantity, TotalAmount
- Customers (dimension): CustomerID, CustomerName, CustomerCity, CustomerSegment
- Products (dimension): ProductID, ProductName, ProductCategory
- Date (dimension): Date, Year, Quarter, Month, etc.

### Creating Your First Measure

**Method 1: Using the Modeling Tab**

1. Click on the **Orders** table in the Fields pane (right side)
2. Go to the **Modeling** tab in the ribbon
3. Click **New Measure**
4. The formula bar appears
![](99.System/Attachments/1!xCzW4R7VsmDjeKj-UzwBRw.png.webp)

**Method 2: Right-Click**

1. Right-click on **Orders** table
2. Select **New Measure**

### Basic Aggregation Measures

**Total Revenue**

```c
Total Revenue = SUM(Orders[TotalAmount])
```

What it does: Adds up all values in the TotalAmount column (respecting current filters)

**Total Orders**

```c
Total Orders = COUNTROWS(Orders)
```

What it does: Counts how many rows are in the Orders table (respecting current filters)

Why not COUNT(Orders\[OrderID\])? COUNTROWS is faster and doesn’t require specifying a column.

**Average Order Value**

```c
Average Order Value = AVERAGE(Orders[TotalAmount])
```

What it does: Calculates the average of TotalAmount column

**Alternative approach using your other measures:**

```c
Average Order Value = DIVIDE([Total Revenue], [Total Orders], 0)
```

The third parameter (0) is what to return if Total Orders is zero (avoiding divide-by-zero errors).

**Total Quantity Sold**

```c
Total Quantity = SUM(Orders[Quantity])
```

**Unique Customers**

```c
Total Customers = DISTINCTCOUNT(Orders[CustomerID])
```

What it does: Counts unique customer IDs (if customer C001 has 10 orders, counts them once)

**Unique Products Sold**

```c
Products Sold = DISTINCTCOUNT(Orders[ProductID])
```

### Testing Your Measures

Create a Card visual for each measure:

1. Go to Report view
2. Add a **Card** visual
3. Drag **\[Total Revenue\]** into the Fields well
4. Repeat for other measures
![](99.System/Attachments/1!tKV1bqtMYOuxyGkhENbg-A.png.webp)

Verify these numbers match your source data.

## Creating a Measures Table

Professional practice: Keep all measures organized in one place.

**Create a dedicated measures table:**

1. **Modeling** tab → **New Table**
2. Enter this DAX:
```c
_Measures = ROW("Helper", 1)
```
1. Right-click the “Helper” column → **Hide**

Now you have a table called \_Measures (the underscore puts it at the top of the field list).

**Move your measures:**

1. Click a measure in the Orders table
2. In the Properties pane, change **Home Table** to **\_Measures**
3. Repeat for all measures
![](99.System/Attachments/1!bApPtqDtlZDa70-GBjKw8Q.png.webp)

Now all your measures are organized in one clean location.

## 3\. Measures vs Calculated Columns

This is the first decision you’ll make with every DAX calculation: Should this be a measure or a calculated column?

## Calculated Columns — Evaluated Row by Row

A calculated column adds a new column to your table. It calculates once when you create it (or when data refreshes), and the result is stored.

**When to use:** You need a value for each row that doesn’t change based on filters.

**Example:  
**In your Orders table, you have UnitPrice and Quantity. You want TotalAmount for each order.

```c
TotalAmount = Orders[UnitPrice] * Orders[Quantity]
// or
Total Revenue = SUM(Orders[Sales])
```

This creates a new column. Order 106320 always shows $1,045. Order 169194 always shows $45. It doesn’t change.

![](99.System/Attachments/1!klGgqy4GzqKet-I4u2AkDA.png.webp)

I already have sales column.

**Another example — Full Name:**

In your Customers table:

```c
FullName = Customers[FirstName] & " " & Customers[LastName]
```

Result: “John Smith”, “Sarah Johnson”, etc. Stored permanently in the table.

**Characteristics:**

- Calculated once, stored in the table
- Takes up file space
- Can be used in slicers and filters
- Row context (calculates row by row)

## Measures — Evaluated Based on Context

A measure doesn’t add a column. It’s a calculation that occurs on the fly, based on what’s currently being viewed or filtered.

**When to use:** You need a value that changes based on the user's selection.

**Example:** Total Revenue measure.

```c
Total Revenue = SUM(Orders[TotalAmount])
```

This doesn’t add a column. It calculates when you use it in a visual.

- No filters? Shows total of ALL orders: $2,657,000
- Filter to 2024? Shows only 2024 orders: $1,823,000
- Filter to “Office Supplies”? Shows only Office Supplies orders: $719.05k

Same measure, different results based on context.

![](99.System/Attachments/1!jh4sYohPIwv8NcMMliWIpQ.png.webp)

![](99.System/Attachments/1!tfZtwQMkMaHX6aJ03qpqDA.png.webp)

Total Revenue by Category and Customer name.

**Characteristics:**

- Calculated on-the-fly
- Doesn’t take up storage space
- Changes based on filters and context
- Filter context (respects what’s selected)

## The Decision Tree

**Ask yourself: Does this value need to change based on what the user selects?**

**YES** → Use a Measure

- Total Revenue (changes based on date range, product, customer)
- Count of Orders (changes based on filters)
- Average Order Value (changes based on context)

**NO** → Use a Calculated Column

- Full Name (John Smith is always John Smith)
- Age Category based on birthdate (“Adult”, “Senior”)
- Profit per order (Order 1001’s profit doesn’t change based on filters)

## Common Mistake: Using Calculated Columns for Aggregations

**Wrong approach:**

```c
// Calculated Column in Orders table
TotalRevenue = SUM(Orders[Amount])  // ❌ This doesn't make sense
```

This tries to calculate a sum for each row. What sum? Each row is just one value.

**Right approach:**

```c
// Measure
Total Revenue = SUM(Orders[Amount])  // ✅ Correct
```

**Rule of thumb:**

If you’re using SUM, COUNT, AVERAGE, MIN, MAX → You almost always want a **measure**, not a calculated column.

## 4\. Understanding Context — The Key to Everything

This is where DAX gets different from Excel. Understanding context is the difference between writing DAX formulas that work and scratching your head wondering why your numbers are wrong.

### What is Context?

Context is what determines which rows DAX looks at when calculating a measure.

Think of it like this: You’re standing in a grocery store. Someone asks, “How much do the apples cost?”

Your answer depends on context:

- Which apple are they pointing at? (row context)
- Are they asking about organic or regular? (filter context)
- Just this store or all stores in the chain? (filter context)

Same question, different answers based on context.

### The Two Types of Context

**1\. Row Context** — “I’m looking at this specific row”  
**2\. Filter Context** — “I’m only considering rows that match these criteria”

## Row Context — Calculated Columns

When you create a calculated column, DAX evaluates it row by row.

**Example:**

```c
// Calculated column in Orders table
Order Size Category = 
IF(Orders[TotalAmount] > 1000, "Large", "Small")
```

As DAX evaluates each row:

- Row 1: TotalAmount = $2,400 → “Large”
- Row 2: TotalAmount = $125 → “Small”
- Row 3: TotalAmount = $300 → “Small”

Each row is evaluated independently. DAX “knows” which row it’s on.

**Another example:**

```c
// Calculated column in Orders table
Profit = Orders[TotalAmount] - (Orders[Quantity] * Products[UnitCost])
```

Wait — this references the Products table. How does it know which product?

Because of the relationship! DAX follows the relationship from Orders to Products using row context.

For Order 1001 (ProductID = 1):

- Looks at the Products table
- Finds the row where ProductID = 1
- Gets the UnitCost
- Calculates profit

This works because of **row context**.

## Filter Context — Measures

When you create a measure, it calculates based on what’s currently filtered.

**Example:**

```c
Total Revenue = SUM(Orders[TotalAmount])
```

**Scenario 1: No filters  
**You put this in a card visual. No slicers selected.  
Result: $2,657,000 (sum of ALL orders)

**Scenario 2: Year slicer set to 2024  
**Same measure, same visual.  
Result: $1,823,000 (sum of only 2024 orders)

**Scenario 3: Year = 2024 AND Category = “Laptops”  
**Same measure, same visual.  
Result: $1,247,000 (sum of only 2024 laptop orders)

**The measure didn’t change. The filter context changed.**

### How Visuals Create Filter Context

A table visual with ProductCategory and Total Revenue:

```c
Category     | Total Revenue
Laptops      | $1,847,000
Monitors     | $523,000
Accessories  | $287,000
```

For the “Laptops” row:

- Power BI automatically filters to Category = “Laptops”
- Your measure calculates with that filter applied
- Shows $1,847,000

For the “Monitors” row:

- Power BI filters to Category = “Monitors”
- Your measure recalculates
- Shows $523,000

**The visual creates filter context automatically for each row.**

### Multiple Filters Combine

You have:

- A table with ProductCategory (creates filter context per row)
- A slicer with Year = 2024 (creates filter context for entire page)
- A slicer with CustomerSegment = “Enterprise” (creates another filter context)

When calculating Total Revenue for the “Laptops” row:

DAX considers: Category = “Laptops” AND Year = 2024 AND Segment = “Enterprise”

All filters combine. The measure calculates only for rows matching ALL conditions.

### Why This Matters

This is correct:

```c
Total Revenue = SUM(Orders[TotalAmount])
```

It respects filter context. Changes based on what’s selected.

**This is confusing (and wrong):**

```c
// Trying to filter inside the measure incorrectly
Total Revenue Laptops = SUM(Orders[TotalAmount]) 
// Where's the laptop filter? This doesn't work.
```

You can’t just reference a product name. You need to explicitly change the filter context, which we’ll cover in the CALCULATE section.

## Quick Context Test

Create two measures:

```c
Test Measure = SUM(Orders[TotalAmount])
```
```c
Test Column = Orders[TotalAmount]  // ❌ This will be an error
```

The second one errors because in a measure, you can’t directly reference a column value. There’s no row context — measures operate in filter context.

To reference a specific row’s value in a measure, you need iterator functions (covered later).

## 5\. CALCULATE — The Function That Changes Everything

If you learn one DAX function well, make it CALCULATE. It’s the most important function in DAX.

### What CALCULATE Does

CALCULATE lets you modify the filter context.

Think of it like this: Your measure normally respects all filters. CALCULATE says, “Actually, ignore some of those filters and apply these specific ones instead.”

**The syntax:**

```c
CALCULATE(
    <expression>,
    <filter1>,
    <filter2>,
    ...
)
```

### Your First CALCULATE — Filtering to One Value

**Scenario:** You want to show laptop revenue specifically, regardless of what category is selected.

```c
Laptop Revenue = 
CALCULATE(
    [Total Revenue],
    Products[ProductCategory] = "Furniture"
)
```

**What happens:**

You put this in a card visual.

User selects “Monitors” in a category slicer.

Regular \[Total Revenue\] shows: $523,000 (monitor revenue)

\[Furniture Revenue\] shows: $7,42,000 (Furniturerevenue, ignoring the monitor filter)

**CALCULATE overrode the category filter and forced it to “Furniture”.**

![](99.System/Attachments/1!A7vBSBfqS0vVgZkhiMqgcg.png.webp)

### Multiple Filter Conditions

**Scenario:** Revenue for enterprise customers buying laptops.

```c
Enterprise Laptop Revenue = 
CALCULATE(
    [Total Revenue],
    Products[ProductCategory] = "Furniture",
    Customers[CustomerSegment] = "Enterprise"
)
```

Both conditions must be true. This is an AND condition.

### OR Conditions

**Scenario:** Revenue from either New York or Boston customers.

```c
NY or Boston Revenue = 
CALCULATE(
    [Total Revenue],
    OR(
        Customers[CustomerCity] = "New York",
        Customers[CustomerCity] = "Boston"
    )
)
```

Or using the || operator:

```c
NY or Boston Revenue = 
CALCULATE(
    [Total Revenue],
    Customers[CustomerCity] = "New York" || Customers[CustomerCity] = "Boston"
)
```

### Filtering by Multiple Values

**Scenario:** Revenue for Laptops, Monitors, and Tablets.

```c
Tech Products Revenue = 
CALCULATE(
    [Total Revenue],
    Products[ProductCategory] IN {"Laptops", "Monitors", "Tablets"}
)
```

The IN operator checks if the value is in the list.

### Real Business Example: Same Store Sales

You opened new stores in 2024. You want to see revenue growth only from stores that existed in both 2023 and 2024 (excluding new stores).

```c
Same Store Revenue 2024 = 
CALCULATE(
    [Total Revenue],
    Date[Year] = 2024,
    Stores[OpenDate] < DATE(2024, 1, 1)
)
```

Only stores that opened before January 1, 2024 are included.

### Using CALCULATE with Other Measures

**Scenario:** What percentage of revenue comes from enterprise customers?

```c
Enterprise Revenue = 
CALCULATE(
    [Total Revenue],
    Customers[CustomerSegment] = "Enterprise"
)
```
```c
Enterprise Revenue % = 
DIVIDE(
    [Enterprise Revenue],
    [Total Revenue],
    0
)
```

When you put \[Enterprise Revenue %\] in a visual:

- With no filters: Shows enterprise % of total company revenue
- Filtered to “Laptops”: Shows enterprise % of laptop revenue
- Filtered to “2024”: Shows enterprise % of 2024 revenue

The measure adapts to context while also applying its own filter.

### Common CALCULATE Mistake

**Wrong:**

```c
// Trying to filter the fact table directly
Wrong Laptop Revenue = 
CALCULATE(
    [Total Revenue],
    Orders[ProductID] = 1  // ❌ Which product is ID 1? Hard to maintain.
)
```

**Right:**

```c
// Filter the dimension table
Furniture Revenue = 
CALCULATE(
    [Total Revenue],
    Products[ProductCategory] = "Furniture"  // ✅ Clear and maintainable
)
```

Always filter dimension tables, not fact tables. It’s clearer and follows the relationship automatically.

### CALCULATE Pattern Library

Here are patterns you’ll use constantly:

**1\. Specific value:**

```c
CALCULATE([Measure], Table[Column] = "Value")
```

**2\. Greater than:**

```c
CALCULATE([Measure], Table[Column] > 1000)
```

**3\. Between two values:**

```c
CALCULATE([Measure], Table[Column] >= 100, Table[Column] <= 500)
```

**4\. Multiple values (OR):**

```c
CALCULATE([Measure], Table[Column] IN {"Value1", "Value2"})
```

**5\. NOT equal:**

```c
CALCULATE([Measure], Table[Column] <> "Value")
```

**6\. Combining filters:**

```c
CALCULATE(
    [Measure],
    Table1[Column1] = "Value1",
    Table2[Column2] > 100
)
```

## 6\. Time Intelligence — Analyzing Data Over Time

Time intelligence is where DAX really shines. Comparing periods, calculating year-to-date totals, growth rates — this is what stakeholders ask for constantly.

### The Requirement: A Proper Date Table

Before you can use time intelligence functions, you need a proper Date table with these characteristics:

1. **Continuous dates** — No gaps (every single day present)
2. **Marked as a Date table** — Told Power BI “this is my calendar”
3. **One active relationship to your fact table** — Connected via OrderDate, TransactionDate, etc.

We created this in the data modeling series. If you skipped it, here’s a quick version:

```c
Date = 
ADDCOLUMNS(
    CALENDAR(DATE(2023, 1, 1), DATE(2025, 12, 31)),
    "Year", YEAR([Date]),
    "Quarter", "Q" & FORMAT([Date], "Q"),
    "Month", MONTH([Date]),
    "MonthName", FORMAT([Date], "MMMM"),
    "YearMonth", FORMAT([Date], "YYYY-MM")
)
```

Then: Table Tools → Mark as Date Table → Select “Date” column

## Year-to-Date (YTD)

**Business question:** “What’s our revenue so far this year?”

```c
Revenue YTD = 
TOTALYTD(
    [Total Revenue],
    Date[Date]
)
```

**How it works:**

If Today is September 15, 2017.

Regular \[Total Revenue\] with Year = 2017 filter: Shows all of 2017

\[Revenue YTD\]: Shows only January 1 to September 15, 2017

**In a visual:**

![](99.System/Attachments/1!NC0YDpcFgddQAfuli_MysQ.png.webp)

Revenue YTD accumulates. By September, it’s the sum of Jan + Feb + Mar + … + Sep.

![](99.System/Attachments/1!NMlxAwCUQ_CAs7c8mjcdfA.png.webp)

## Month-to-Date (MTD)

**Business question:** “How are we doing so far this month?”

```c
Revenue MTD = 
TOTALMTD(
    [Total Revenue],
    Date[Date]
)
```

If today is September 15:

- \[Total Revenue\] filtered to September: Shows entire September
- \[Revenue MTD\]: Shows only September 1–15

## Quarter-to-Date (QTD)

```c
Revenue QTD = 
TOTALQTD(
    [Total Revenue],
    Date[Date]
)
```

We’re in Q3 (July, August, September). Today is September 15.

\[Revenue QTD\] shows July 1 through September 15.

## Previous Year Same Period

**Business question:** “What was revenue this time last year?”

```c
Revenue PY = 
CALCULATE(
    [Total Revenue],
    SAMEPERIODLASTYEAR(Date[Date])
)
```

**How it works:**

You’re looking at September 2017.

\[Total Revenue\]: Shows September 2017 revenue

\[Revenue PY\]: Shows September 2016 revenue

**In a table:**

```c
Month         | Revenue 2017 | Revenue PY (2016)
January       | $180,000     | $145,000
February      | $195,000     | $158,000
March         | $210,000     | $172,000
```

## Year-over-Year Growth

**Business question:** “How much did we grow compared to last year?”

```c
Revenue Growth % = 
VAR CurrentRevenue = [Total Revenue]
VAR PreviousRevenue = [Revenue PY]
RETURN
    DIVIDE(
        CurrentRevenue - PreviousRevenue,
        PreviousRevenue,
        0
    )
```

**Breaking it down:**

`VAR` creates variables (we'll cover these more in optimization)

Calculate current revenue and previous revenue, then find the percentage change.

**Result:**

```c
Month         | Revenue 2024 | Revenue PY   | Growth %
January       | $180,000     | $145,000     | 24.1%
February      | $195,000     | $158,000     | 23.4%
March         | $210,000     | $172,000     | 22.1%
```

## Previous Month

**Business question:** “How did we do last month?”

```c
Revenue Previous Month = 
CALCULATE(
    [Total Revenue],
    PREVIOUSMONTH(Date[Date])
)
```

You’re viewing September 2017. This shows August 2017.

## Month-over-Month Growth

```c
Revenue MoM Growth % = 
VAR CurrentMonth = [Total Revenue]
VAR PreviousMonth = [Revenue Previous Month]
RETURN
    DIVIDE(
        CurrentMonth - PreviousMonth,
        PreviousMonth,
        0
    )
```

## Rolling 12 Months

**Business question:** “What’s our revenue for the last 12 months?”

This isn’t about calendar year. It’s literally the last 365 days.

```c
Revenue L12M = 
CALCULATE(
    [Total Revenue],
    DATESINPERIOD(
        Date[Date],
        LASTDATE(Date[Date]),
        -12,
        MONTH
    )
)
```

**How it works:**

Today is September 15, 2017.

This calculates revenue from September 15, 2016 through September 15, 2017.

Different from YTD (which is calendar year Jan 1 to today).

## Fiscal Year Handling

**Scenario:** Your fiscal year starts April 1, not January 1.

When someone says “Year to Date,” they mean April 1 to today, not January 1 to today.

```c
Revenue Fiscal YTD = 
TOTALYTD(
    [Total Revenue],
    Date[Date],
    "3/31"  // Fiscal year ends March 31
)
```

The third parameter tells DAX when your fiscal year ends.

## Common Time Intelligence Mistakes

**Mistake 1: Using time intelligence without a proper Date table**

```c
// ❌ This will error
Revenue YTD = TOTALYTD([Total Revenue], Orders[OrderDate])
```

TOTALYTD requires a Date table marked as a date table. It won’t work with a date column in your fact table.

**Mistake 2: Multiple active relationships to Date table**

If Orders\[OrderDate\] and Orders\[ShipDate\] both connect to Date\[Date\], only one can be active.

Time intelligence functions use the active relationship.

If you need YTD for ShipDate, create separate measures using USERELATIONSHIP:

```c
Revenue YTD by Ship Date = 
CALCULATE(
    TOTALYTD([Total Revenue], Date[Date]),
    USERELATIONSHIP(Orders[ShipDate], Date[Date])
)
```

**Mistake 3: Forgetting BLANK handling**

```c
// If PY has no data, this shows -100%
Revenue Growth % = ([Total Revenue] - [Revenue PY]) / [Revenue PY]
```

**Better:**

```c
Revenue Growth % = 
VAR CurrentRevenue = [Total Revenue]
VAR PreviousRevenue = [Revenue PY]
RETURN
    IF(
        ISBLANK(PreviousRevenue),
        BLANK(),
        DIVIDE(CurrentRevenue - PreviousRevenue, PreviousRevenue)
    )
```

## 7\. Logical Functions & Conditional Calculations

Business logic isn’t always straightforward. Sometimes you need: “If this, then that. Otherwise, this other thing.”

### IF Function

**Syntax:**

```c
IF(<logical_test>, <value_if_true>, <value_if_false>)
```

**Simple example: Order Size Category**

```c
Order Size = 
IF(
    [Total Revenue] > 1000,
    "Large Order",
    "Small Order"
)
```

If revenue is over $1,000, mark as “Large Order”. Otherwise, “Small Order”.

**Business example: Sales Target Status**

You have a monthly target of $150,000.

```c
Target Status = 
IF(
    [Total Revenue] >= 150000,
    "Target Met ✓",
    "Below Target"
)
```

Put this in a card visual. Turns green when you hit target, red when below.

### Nested IF

**Scenario:** You want three categories: Large, Medium, Small.

```c
Order Category = 
IF(
    [Total Revenue] > 1000,
    "Large",
    IF(
        [Total Revenue] > 500,
        "Medium",
        "Small"
    )
)
```

**How it evaluates:**

1. Is revenue > $1,000? Yes → “Large”
2. If no, is revenue > $500? Yes → “Medium”
3. If no → “Small”

**Result:**

- $1,200 → Large
- $750 → Medium
- $300 → Small

### SWITCH — Better Than Nested IF

When you have many conditions, SWITCH is cleaner.

**Syntax:**

```c
SWITCH(
    <expression>,
    <value1>, <result1>,
    <value2>, <result2>,
    ...,
    <default_result>
)
```

**Example: Customer Segment Discount**

```c
Discount Rate = 
SWITCH(
    Customers[CustomerSegment],
    "Enterprise", 0.15,
    "SMB", 0.10,
    "Startup", 0.05,
    0  // Default: no discount
)
```

**Much cleaner than:**

```c
Discount Rate = 
IF(
    Customers[CustomerSegment] = "Enterprise",
    0.15,
    IF(
        Customers[CustomerSegment] = "SMB",
        0.10,
        IF(
            Customers[CustomerSegment] = "Startup",
            0.05,
            0
        )
    )
)
```

**Another example: Priority Level**

```c
Priority = 
SWITCH(
    TRUE(),
    [Total Revenue] > 10000, "Critical",
    [Total Revenue] > 5000, "High",
    [Total Revenue] > 1000, "Medium",
    "Low"
)
```

Using SWITCH with TRUE() as the first parameter lets you test multiple conditions (like nested IFs).

### AND / OR / NOT

**AND — All conditions must be true**

```c
High Value Enterprise = 
IF(
    AND(
        Customers[CustomerSegment] = "Enterprise",
        [Total Revenue] > 50000
    ),
    "Yes",
    "No"
)
```

Both conditions must be true: Enterprise AND revenue over $50K.

**OR — At least one condition must be true**

```c
Coastal Customer = 
IF(
    OR(
        Customers[CustomerCity] = "New York",
        Customers[CustomerCity] = "Los Angeles",
        Customers[CustomerCity] = "Miami"
    ),
    "Coastal",
    "Inland"
)
```

**Combining AND/OR:**

```c
Premium Customer = 
IF(
    AND(
        OR(
            Customers[CustomerSegment] = "Enterprise",
            [Total Revenue] > 100000
        ),
        Customers[AccountStatus] = "Active"
    ),
    "Premium",
    "Standard"
)
```

“Premium” if they’re either Enterprise OR have revenue over $100K, AND their account is active.

**NOT — Reverse a condition**

```c
Not Churned = 
IF(
    NOT(Customers[AccountStatus] = "Cancelled"),
    "Active Customer",
    "Churned"
)
```

### ISBLANK — Handling Missing Data

**Check if a value is blank:**

```c
Has Email = 
IF(
    ISBLANK(Customers[Email]),
    "No Email",
    "Has Email"
)
```

**Better pattern — Avoid dividing by blank:**

```c
Average Deal Size = 
IF(
    ISBLANK([Total Orders]),
    BLANK(),
    DIVIDE([Total Revenue], [Total Orders])
)
```

If there are no orders, don’t show “Error” or “#DIV/0”, just show blank.

**Even better — use DIVIDE’s third parameter:**

```c
Average Deal Size = DIVIDE([Total Revenue], [Total Orders], BLANK())
```

### IFERROR — Catching Errors

**Scenario:** You’re calculating a percentage, but sometimes the denominator is zero.

```c
Market Share % = 
IFERROR(
    [Our Revenue] / [Total Market Revenue],
    0
)
```

If the division fails (denominator is zero or BLANK), return 0 instead of an error.

**Another example:**

```c
Growth Rate = 
IFERROR(
    ([This Year] - [Last Year]) / [Last Year],
    BLANK()
)
```

If last year has no data, show blank instead of error.

## Real Business Example: Traffic Light KPI

**Scenario:** You want a visual indicator:

- Green: Revenue above target
- Yellow: Revenue within 10% of target
- Red: Revenue below 90% of target
```c
Performance Indicator = 
VAR Target = 150000
VAR ActualRevenue = [Total Revenue]
VAR PercentOfTarget = DIVIDE(ActualRevenue, Target, 0)
RETURN
    SWITCH(
        TRUE(),
        PercentOfTarget >= 1, "🟢 Above Target",
        PercentOfTarget >= 0.9, "🟡 Near Target",
        "🔴 Below Target"
    )
```

**In a table:**

```c
Month      | Revenue    | Performance
January    | $165,000   | 🟢 Above Target
February   | $142,000   | 🟡 Near Target
March      | $128,000   | 🔴 Below Target
```

## Creating Dynamic Titles

**Scenario:** You want your chart title to change based on what year is selected.

```c
Dynamic Title = 
"Revenue for " & 
IF(
    ISFILTERED(Date[Year]),
    SELECTEDVALUE(Date[Year]),
    "All Years"
)
```

Result:

- No year selected: “Revenue for All Years”
- 2017 selected: “Revenue for 2017”
- Multiple years selected: “Revenue for All Years”

Put this measure in the chart title field (not as a value, but as the title itself).

## 8\. Filter Functions — Controlling What Gets Calculated

CALCULATE changes filters. But sometimes you need more control — removing filters entirely, keeping only certain filters, or creating complex filter conditions.

### ALL — Remove Filters

ALL removes filters from a table or column.

**Scenario: Show percentage of total**

```c
Revenue % of Total = 
DIVIDE(
    [Total Revenue],
    CALCULATE([Total Revenue], ALL(Products))
)
```

**How it works:**

In a table visual with ProductCategory:

```c
Category     | Revenue    | % of Total
Laptops      | $1,847,000 | 69.5%
Monitors     | $523,000   | 19.7%
Accessories  | $287,000   | 10.8%
Total        | $2,657,000 | 100%
```

For the Furniture Row:

- Numerator: \[Total Revenue\] = $1,847,000 (just laptops)
- Denominator: CALCULATE(\[Total Revenue\], ALL(Products)) = $2,657,000 (all products, filter removed)
- Result: 69.5%

**Another example: Show grand total**

```c
Company Total Revenue = 
CALCULATE(
    [Total Revenue],
    ALL()
)
```

ALL() with no parameter removes ALL filters from the entire model.

### ALLSELECTED — Respect Visual Filters

**The difference between ALL and ALLSELECTED:**

**ALL:** Ignores everything, even visual-level filters

**ALLSELECTED:** Ignores row-level filters but respects page/report filters

**Scenario:** You have a Year slicer set to 2017, and a table showing categories.

```c
Revenue % of Filtered Total = 
DIVIDE(
    [Total Revenue],
    CALCULATE([Total Revenue], ALLSELECTED(Products))
)
```

Result:

- Denominator considers only 2017 (respects the Year slicer)
- But ignores the category filter from the table rows
- Shows each category as % of 2024 total, not % of all-time total

**When to use:**

- % of total where “total” means “what the user is currently looking at”
- Ranking within filtered context

### ALLEXCEPT — Remove All Filters Except…

**Scenario:** Show total revenue by year, ignoring all other filters except year.

```c
Revenue by Year Only = 
CALCULATE(
    [Total Revenue],
    ALLEXCEPT(Date, Date[Year])
)
```

This removes filters from everything except Date\[Year\].

If a user selects:

- Year = 2017
- Quarter = Q1
- Month = January

This measure shows total for ALL of 2017, not just January.

**Another example: Customer lifetime revenue**

```c
Customer Lifetime Revenue = 
CALCULATE(
    [Total Revenue],
    ALLEXCEPT(Orders, Orders[CustomerID])
)
```

No matter what date range is selected, this shows the customer’s total revenue across all time.

### REMOVEFILTERS — Modern Alternative to ALL

REMOVEFILTERS is clearer and more explicit than ALL.

**Instead of:**

```c
CALCULATE([Total Revenue], ALL(Products))
```

**Use:**

```c
CALCULATE([Total Revenue], REMOVEFILTERS(Products))
```

They do the same thing, but REMOVEFILTERS is more readable.

**Remove filters from specific columns:**

```c
CALCULATE(
    [Total Revenue],
    REMOVEFILTERS(Date[Month]),
    REMOVEFILTERS(Date[Quarter])
)
```

### FILTER — Create Custom Filter Conditions

FILTER evaluates a table row by row and returns only rows that meet a condition.

**Scenario:** Revenue from high-value orders only (over $1,000 each).

```c
High Value Revenue = 
CALCULATE(
    [Total Revenue],
    FILTER(
        Orders,
        Orders[TotalAmount] > 1000
    )
)
```

**How it works:**

1. FILTER looks at every row in Orders
2. Checks if TotalAmount > 1000
3. Returns only rows that match
4. SUM calculates on those filtered rows

**Another example: Active customers only**

```c
Active Customer Revenue = 
CALCULATE(
    [Total Revenue],
    FILTER(
        Customers,
        Customers[AccountStatus] = "Active"
    )
)
```

**Combining FILTER with other conditions:**

```c
Enterprise High Value Revenue = 
CALCULATE(
    [Total Revenue],
    FILTER(
        Orders,
        Orders[TotalAmount] > 1000
    ),
    Customers[CustomerSegment] = "Enterprise"
)
```

Both conditions apply: Enterprise customers AND orders over $1,000.

### KEEPFILTERS — Combine Filters Instead of Replacing

Normally, CALCULATE replaces existing filters.

**Example:**

User selects “Furniture” in a slicer.

```c
Monitor Revenue = 
CALCULATE(
    [Total Revenue],
    Products[ProductCategory] = "Furniture"
)
```

This REPLACES the “Furniture” filter with “Monitors”. Shows monitor revenue even though the user selected Furniture.

**But with KEEPFILTERS:**

```c
Monitor Revenue = 
CALCULATE(
    [Total Revenue],
    KEEPFILTERS(Products[ProductCategory] = "Monitors")
)
```

This COMBINES the filters: “Furniture” AND “Monitors”.

Since no product is both a Furniture and a monitor, this returns BLANK.

**When to use:**

- When you want filters to intersect rather than replace
- Preventing measures from showing data users didn’t select

### Real Business Example: Top N Products

**Scenario:** Show only top 5 products by revenue, regardless of other filters.

```c
Top 5 Product Revenue = 
CALCULATE(
    [Total Revenue],
    FILTER(
        ALLSELECTED(Products),
        RANKX(
            ALLSELECTED(Products),
            [Total Revenue]
        ) <= 5
    )
)
```

**Breaking it down:**

1. ALLSELECTED(Products) — Get all products in current filter context
2. RANKX — Rank each product by revenue
3. FILTER — Keep only products ranked 5 or better
4. Calculate revenue for those products

Put this in a card visual: Shows combined revenue of top 5 products only.

### Filter Function Decision Tree

**Question: What do I want to do with filters?**

**Remove all filters from a table/column:** → Use REMOVEFILTERS or ALL

**Remove all filters except specific ones:** → Use ALLEXCEPT

**Respect user’s visual selections but ignore row context:** → Use ALLSELECTED

**Create a custom condition row by row:** → Use FILTER

**Combine new filter with existing instead of replacing:** → Use KEEPFILTERS

## 9\. Iterator Functions — Row-by-Row Calculations

Sometimes you need to calculate something for each row, then aggregate the results. That’s what iterator functions do.

### The Problem Simple Aggregations Can’t Solve

**Scenario:** Calculate total profit.

You have:

- Orders\[TotalAmount\] (revenue)
- Products\[UnitCost\]
- Orders\[Quantity\]

Profit per order = TotalAmount — (Quantity × UnitCost)

**Why this doesn’t work:**

```c
// ❌ Wrong
Total Profit = SUM(Orders[TotalAmount]) - SUM(Orders[Quantity]) * Products[UnitCost]
```

This tries to use a single UnitCost for all orders. But each order has a different product with a different cost.

**You need to calculate profit for EACH ORDER, then sum those profits.**

That’s an iterator function.

### SUMX — Calculate for Each Row, Then Sum

**Syntax:**

```c
SUMX(
    <table>,
    <expression>
)
```

**Correct profit calculation:**

```c
Total Profit = 
SUMX(
    Orders,
    Orders[TotalAmount] - (Orders[Quantity] * RELATED(Products[UnitCost]))
)
```

**How it works:**

1. Looks at first row of Orders
- Order 1001: TotalAmount = $2,400, Quantity = 2
- Uses RELATED to get UnitCost from Products table = $1,000
- Calculates: $2,400 — (2 × $1,000) = $400

2\. Looks at second row

- Order 1002: TotalAmount = $125, Quantity = 5
- UnitCost = $20
- Calculates: $125 — (5 × $20) = $25

3\. Continues for all rows

4\. Sums all the individual profits: $400 + $25 + … = Total Profit

**Another example: Revenue with Discount**

```c
Revenue After Discount = 
SUMX(
    Orders,
    Orders[TotalAmount] * (1 - RELATED(Customers[DiscountRate]))
)
```

Each order gets its customer’s specific discount rate applied.

### AVERAGEX — Calculate for Each Row, Then Average

**Scenario:** Average profit per order.

```c
Average Profit per Order = 
AVERAGEX(
    Orders,
    Orders[TotalAmount] - (Orders[Quantity] * RELATED(Products[UnitCost]))
)
```

Calculates profit for each order, then averages them.

**Why not just Total Profit / Total Orders?**

Sometimes that works. But AVERAGEX gives you more control and handles complex scenarios.

### COUNTX — Count Rows Where Condition is True

```c
High Value Orders = 
COUNTX(
    Orders,
    IF(Orders[TotalAmount] > 1000, 1, BLANK())
)
```

**How it works:**

- Looks at each order
- If TotalAmount > $1,000, returns 1
- Otherwise returns BLANK
- Counts the 1s (BLANKs are not counted)

**Alternative (clearer):**

```c
High Value Orders = 
COUNTROWS(
    FILTER(
        Orders,
        Orders[TotalAmount] > 1000
    )
)
```

This is often easier to read than COUNTX.

### MINX and MAXX

**Scenario:** Find the lowest profit margin on any order.

```c
Lowest Profit Margin = 
MINX(
    Orders,
    DIVIDE(
        Orders[TotalAmount] - (Orders[Quantity] * RELATED(Products[UnitCost])),
        Orders[TotalAmount]
    )
)
```

Calculates profit margin for each order, returns the minimum.

### Real Business Example: Weighted Average

**Scenario:** Average price paid per product, weighted by quantity.

**Wrong approach:**

```c
Average Price = AVERAGE(Orders[UnitPrice])
```

This treats each order equally. An order for 1 unit has the same weight as an order for 100 units.

**Right approach:**

```c
Weighted Average Price = 
DIVIDE(
    SUMX(Orders, Orders[Quantity] * Orders[UnitPrice]),
    SUM(Orders[Quantity])
)
```

**Breaking it down:**

1. SUMX calculates Quantity × Price for each order, then sums
- Order 1: 2 × $1,200 = $2,400
- Order 2: 5 × $25 = $125
- Total: $2,525
1. Divide by total quantity (7 units)
2. Result: $360.71 average price per unit (weighted)

This is different from AVERAGE(Orders\[UnitPrice\]) which would be $612.50.

## Performance Warning

Iterator functions are powerful but expensive.

**Why:**

They calculate row by row. For a million-row table, they perform a million calculations.

**When to avoid:**

- Large fact tables (millions of rows)
- Complex nested iterators
- If a calculated column can do the same thing (calculate once during refresh instead of every query)

**When iterators are necessary:**

- The calculation must be dynamic (changes based on filters)
- You need aggregations that simple SUM/AVERAGE can’t do
- Weighted calculations, profit margins, etc.

### Optimization tip:

**❌ SLOW - Calculates the same complex expression multiple times:**

```c
Profit Analysis = 
VAR HighValueProfit = 
    SUMX(
        FILTER(Orders, Orders[TotalAmount] > 1000),
        Orders[TotalAmount] - (Orders[Quantity] * RELATED(Products[UnitCost]))
    )
VAR TotalProfit = 
    SUMX(
        Orders,
        Orders[TotalAmount] - (Orders[Quantity] * RELATED(Products[UnitCost]))
    )
RETURN
    DIVIDE(HighValueProfit, TotalProfit)
```

**Why it's slow:** The profit calculation `Orders[TotalAmount] - (Orders[Quantity] * RELATED(Products[UnitCost]))` runs twice—once for high-value orders, once for all orders.

**✅ FAST — Uses a calculated column to avoid repeated calculation:**

Create a calculated column once.

```c
// Calculated column in Orders table (calculated once during refresh)
Profit = Orders[TotalAmount] - (Orders[Quantity] * RELATED(Products[UnitCost]))
```

**Then use simple aggregation measures:**

```c
Total Profit = SUM(Orders[Profit])

High Value Profit = 
CALCULATE(
    SUM(Orders[Profit]),
    Orders[TotalAmount] > 1000
)

Profit from High Value Orders % = 
DIVIDE([High Value Profit], [Total Profit])
```

**Why it’s faster:** Profit calculation happens once during refresh (stored in the column), not every time someone interacts with the report.

## 10\. Advanced Patterns & Real-World Scenarios

Now let’s combine everything you’ve learned into patterns you’ll use constantly.

### Pattern 1: Running Total

**Scenario:** Cumulative revenue by date.

```c
Running Total Revenue = 
CALCULATE(
    [Total Revenue],
    FILTER(
        ALLSELECTED(Date),
        Date[Date] <= MAX(Date[Date])
    )
)
```

**How it works:**

In a table with dates:

```c
Date       | Revenue  | Running Total
Jan 1      | $5,000   | $5,000
Jan 2      | $7,200   | $12,200
Jan 3      | $4,100   | $16,300
```

For Jan 2 row:

- MAX(Date\[Date\]) = Jan 2
- FILTER keeps all dates <= Jan 2
- Calculates revenue for Jan 1 + Jan 2 = $12,200

### Pattern 2: Ranking

**Scenario:** Rank products by revenue.

```c
Product Rank = 
RANKX(
    ALLSELECTED(Products),
    [Total Revenue],
    ,
    DESC
)
```

**Result in a table:**

```c
Product     | Revenue    | Rank
Laptop Pro  | $847,000   | 1
Monitor 4K  | $523,000   | 2
Mouse       | $287,000   | 3
```

**Top N Filter:**

Show only top 5 products:

```c
Top 5 Products = 
IF(
    [Product Rank] <= 5,
    [Total Revenue],
    BLANK()
)
```

Put this measure in a visual. Only products ranked 5 or better show values.

### Pattern 3: ABC Analysis

**Scenario:** Classify customers by revenue contribution.

**Category A:** Top 20% of customers generating 80% of revenue  
**Category B:** Next 30% generating 15% of revenue  
**Category C:** Remaining 50% generating 5% of revenue

```c
Customer Category = 
VAR CustomerRevenue = [Total Revenue]
VAR AllRevenue = CALCULATE([Total Revenue], ALLSELECTED(Customers))
VAR PercentOfTotal = DIVIDE(CustomerRevenue, AllRevenue)
VAR CumulativePercent = 
    CALCULATE(
        DIVIDE([Total Revenue], AllRevenue),
        FILTER(
            ALLSELECTED(Customers),
            [Total Revenue] >= CustomerRevenue
        )
    )
RETURN
    SWITCH(
        TRUE(),
        CumulativePercent <= 0.80, "A - High Value",
        CumulativePercent <= 0.95, "B - Medium Value",
        "C - Low Value"
    )
```

**Result:**

```c
Customer        | Revenue    | Category
TechCorp        | $450,000   | A - High Value
GlobalCo        | $380,000   | A - High Value
StartupXYZ      | $12,000    | C - Low Value
```

### Pattern 4: Same Period Last Year (Advanced)

**Scenario:** Compare to same period last year, even with missing data.

```c
Revenue SPLY = 
VAR CurrentPeriod = [Total Revenue]
VAR PreviousPeriod = 
    CALCULATE(
        [Total Revenue],
        DATEADD(Date[Date], -1, YEAR)
    )
RETURN
    IF(
        NOT(ISBLANK(CurrentPeriod)),
        PreviousPeriod,
        BLANK()
    )
```

**Why the IF check:**

If current period has no data, don’t show last year’s data either (avoids misleading comparisons).

### Pattern 5: Pareto (80/20) Analysis

**Scenario:** Which products contribute 80% of revenue?

```c
Cumulative Revenue % = 
VAR CurrentProductRevenue = [Total Revenue]
VAR AllRevenue = CALCULATE([Total Revenue], ALLSELECTED(Products))
VAR ProductsWithHigherRevenue = 
    FILTER(
        ALLSELECTED(Products),
        [Total Revenue] >= CurrentProductRevenue
    )
VAR CumulativeRevenue = 
    CALCULATE(
        [Total Revenue],
        ProductsWithHigherRevenue
    )
RETURN
    DIVIDE(CumulativeRevenue, AllRevenue)
```

**Then create:**

```c
Pareto Group = 
IF(
    [Cumulative Revenue %] <= 0.80,
    "Top 80%",
    "Bottom 20%"
)
```

**Result:**

```c
Product     | Revenue    | Cumulative % | Group
Laptop Pro  | $847,000   | 31.9%        | Top 80%
Monitor 4K  | $523,000   | 51.6%        | Top 80%
...
USB Cable   | $12,000    | 99.5%        | Bottom 20%
```

Focus your efforts on products in the “Top 80%” group.

### Pattern 6: Dynamic Segmentation

**Scenario:** Let users define “high value” threshold with a slicer.

**Step 1: Create a disconnected parameter table**

Modeling → New Table:

```c
Revenue Threshold = 
GENERATESERIES(10000, 100000, 10000)
```

This creates a table with values: 10000, 20000, 30000, …, 100000

**Step 2: Create a measure that reads the selected threshold**

```c
Selected Threshold = SELECTEDVALUE('Revenue Threshold'[Value], 50000)
```

Default is $50,000 if nothing selected.

**Step 3: Use it in your logic**

```c
Customer Segment = 
IF(
    [Total Revenue] >= [Selected Threshold],
    "High Value",
    "Standard"
)
```

Now users can slide the threshold up or down, and the segmentation updates live.

### Pattern 7: New vs Returning Customers

**Scenario:** Identify which customers are new this period.

```c
Customer Type = 
VAR FirstOrderDate = 
    CALCULATE(
        MIN(Orders[OrderDate]),
        ALLEXCEPT(Orders, Orders[CustomerID])
    )
VAR CurrentPeriodStart = MIN(Date[Date])
RETURN
    IF(
        FirstOrderDate >= CurrentPeriodStart,
        "New Customer",
        "Returning Customer"
    )
```

**How it works:**

1. Find customer’s first order date ever
2. Check if it’s within the current filtered period
3. If yes, they’re new. If no, they’re returning.

### Pattern 8: Churn Analysis

**Scenario:** Customers who purchased last year but not this year.

```c
Churned Customers = 
VAR CustomersLastYear = 
    CALCULATETABLE(
        VALUES(Orders[CustomerID]),
        DATEADD(Date[Date], -1, YEAR)
    )
VAR CustomersThisYear = 
    VALUES(Orders[CustomerID])
RETURN
    COUNTROWS(
        EXCEPT(CustomersLastYear, CustomersThisYear)
    )
```

**Breaking it down:**

1. Get list of customers who ordered last year
2. Get list of customers who ordered this year
3. EXCEPT finds customers in first list but not second
4. Count them

### 11\. Optimization & Best Practices

You can write DAX that works. But can you write DAX that works *fast*?

### Use Variables (VAR)

Variables improve performance and readability.

**Without variables:**

```c
Profit Analysis = 
VAR HighValueProfit = 
    SUMX(
        FILTER(Orders, Orders[TotalAmount] > 1000),
        Orders[TotalAmount] - (Orders[Quantity] * RELATED(Products[UnitCost]))
    )
VAR TotalProfit = 
    SUMX(
        Orders,
        Orders[TotalAmount] - (Orders[Quantity] * RELATED(Products[UnitCost]))
    )
RETURN
    DIVIDE(HighValueProfit, TotalProfit)
```

The profit calculation runs twice — once for numerator, once for denominator.

**With variables:**

```c
// Calculated column in Orders table (calculated once during refresh)
Profit = Orders[TotalAmount] - (Orders[Quantity] * RELATED(Products[UnitCost]))
```
```c
Total Profit = SUM(Orders[Profit])

High Value Profit = 
CALCULATE(
    SUM(Orders[Profit]),
    Orders[TotalAmount] > 1000
)

Profit from High Value Orders % = 
DIVIDE([High Value Profit], [Total Profit])
```

Profit calculates once, stored in variable, used twice. Much faster.

**Variables also improve readability:**

```c
Customer Lifetime Value = 
VAR TotalRevenue = [Total Revenue]
VAR TotalOrders = [Total Orders]
VAR AvgOrderValue = DIVIDE(TotalRevenue, TotalOrders)
VAR EstimatedLifetimeOrders = 12
RETURN
    AvgOrderValue * EstimatedLifetimeOrders
```

Easy to read and understand.

### Avoid Expensive Iterators When Possible

**Slow:**

```c
Total Profit = 
SUMX(
    Orders,
    Orders[TotalAmount] - (Orders[Quantity] * RELATED(Products[UnitCost]))
)
```

**Faster (if possible):**

Create a calculated column in Power Query or as a DAX calculated column:

```c
// Calculated column in Orders table
Profit = Orders[TotalAmount] - (Orders[Quantity] * RELATED(Products[UnitCost]))
```

Then:

```c
// Measure
Total Profit = SUM(Orders[Profit])
```

The calculation happens once during refresh, not every query.

**When this doesn’t work:**

If the calculation needs to be dynamic (e.g., profit after a discount that changes based on promotions), you need the iterator.

### Filter on Dimensions, Not Facts

**Slow:**

```c
Laptop Revenue = 
CALCULATE(
    [Total Revenue],
    FILTER(Orders, RELATED(Products[ProductCategory]) = "Laptops")
)
```

FILTER scans the entire Orders table (potentially millions of rows).

**Fast:**

```c
Laptop Revenue = 
CALCULATE(
    [Total Revenue],
    Products[ProductCategory] = "Laptops"
)
```

Filters the Products table (maybe 50 rows), relationship does the rest.

### DIVIDE Instead of Division Operator

**Don’t use:**

```c
Margin = [Profit] / [Revenue]
```

If Revenue is zero, this errors.

**Use:**

```c
Margin = DIVIDE([Profit], [Revenue], 0)
```

Safer and handles BLANK/zero gracefully.

### Avoid Calculated Columns When Measures Work

**Wrong:**

```c
// Calculated column
Total Revenue Column = SUM(Orders[TotalAmount])  // ❌ This doesn't work
```

**Right:**

```c
// Measure
Total Revenue = SUM(Orders[TotalAmount])  // ✅
```

Calculated columns:

- Take up storage
- Calculated during refresh (slower refreshes)
- Can’t be filtered dynamically

Measures:

- No storage needed
- Calculated on-demand
- Respect filters

**Use calculated columns only when:**

- You need the value in slicers/filters
- The value is truly static (like FullName from FirstName + LastName)
- You’re categorizing data (like “High/Medium/Low” based on a threshold)

## Best Practices Checklist

**Naming:**

- \[ \] Measures start with what they calculate: “Total Revenue”, not “Revenue Total”
- \[ \] No spaces in table or column names (or use brackets consistently)
- \[ \] Calculated columns end with a noun: “Profit Amount”, “Order Category”

**Structure:**

- \[ \] All measures in a dedicated \_Measures table
- \[ \] Related measures grouped (all revenue measures together)
- \[ \] Complex measures use variables for clarity

**Performance:**

- \[ \] Variables used to avoid recalculating same expression
- \[ \] Iterators only when necessary
- \[ \] Filters applied to dimension tables, not fact tables
- \[ \] DIVIDE used instead of / for division

**Error Handling:**

- \[ \] DIVIDE includes third parameter for zero/BLANK handling
- \[ \] IF checks for ISBLANK where appropriate
- \[ \] Growth % measures handle missing previous period data

**Documentation:**

- \[ \] Complex measures include comments
- \[ \] Business logic explained
- \[ \] Assumptions documented

**Example of well-structured measure:**

```c
/* 
    Customer Lifetime Value Estimate
    Assumes average customer lifespan of 3 years
    Based on current average order frequency and value
    Updated: 2024-09-15
*/
Customer Lifetime Value = 
VAR AvgOrderValue = DIVIDE([Total Revenue], [Total Orders], 0)
VAR AvgOrdersPerYear = 
    DIVIDE(
        [Total Orders],
        DISTINCTCOUNT(Date[Year]),
        0
    )
VAR EstimatedYears = 3
VAR EstimatedLifetimeOrders = AvgOrdersPerYear * EstimatedYears
RETURN
    AvgOrderValue * EstimatedLifetimeOrders
```

Clean, documented, uses variables, handles division safely.

## Key Takeaways

**What you’ve learned:**

✅ **DAX Foundations** — It’s not Excel; context matters more than anything

✅ **Measures vs Columns** — When to use each (almost always measures for aggregations)

✅ **Basic Aggregations** — SUM, COUNT, AVERAGE, DISTINCTCOUNT

✅ **Context** — Row context (calculated columns) vs Filter context (measures)

✅ **CALCULATE** — The most powerful function, modifying filter context

✅ **Time Intelligence** — YTD, MTD, previous year, growth rates, rolling periods

✅ **Logical Functions** — IF, SWITCH, AND, OR, handling blanks and errors

✅ **Filter Functions** — ALL, ALLSELECTED, ALLEXCEPT, FILTER, REMOVEFILTERS

✅ **Iterators** — SUMX, AVERAGEX for row-by-row calculations

✅ **Advanced Patterns** — Running totals, ranking, ABC analysis, Pareto

✅ **Optimization** — Variables, avoiding expensive calculations, best practices

## Your DAX Journey Starts Now

Don’t try to memorize everything. You won’t.

Instead, bookmark this guide and refer back when you need to:

- Compare this year to last year → **Time Intelligence section**
- Create conditional logic → **Logical Functions** section
- Calculate something row by row → **Iterator Functions** section
- Control which filters apply → **Filter Functions** section

**The best way to learn DAX:**

1. Start with basic measures (SUM, COUNT)
2. Add CALCULATE when you need filtering
3. Learn time intelligence for business metrics
4. Practice on real data with real business questions

Every complex measure you see is just a combination of these building blocks.

## What’s Next in the Series?

Now that you can calculate anything, it’s time to show it beautifully.

**Master Power BI: Creating Effective Visualizations**

- Choosing the right chart type for your data
- Formatting that improves understanding (not just looks pretty)
- Making visuals interactive
- Design principles that make reports users actually want to use

## Final Thoughts

DAX looks intimidating. It’s a different way of thinking than Excel formulas.

But here’s the truth: You don’t need to master all of DAX to be effective. The measures in this guide — basic aggregations, CALCULATE, time intelligence, and some logical functions — cover 80% of what you’ll ever need.

Learn those well. The rest you can look up when you need it.

**Connect with me on LinkedIn** for more Power BI content focused on real problems and practical solutions.

**Or you can schedule a call on Topmate: J** [**anvi Gupta**](https://topmate.io/janvigupta)

![](99.System/Attachments/0!pjyLPPNwlX303hdG.gif)

Dream big, but start small..!

**💡** [**MUST TRY — Power BI GPT — Personal Power BI Learning Coach**](https://powerbi-masterclass.short.gy/pbi-gpt?utm_source=medium&utm_campaign=pbi-gpt-medium-post-end) **💡**

> Don’t forget to subscribe to
> 
> 👉 [Power BI Publication](https://powerbi-masterclass.short.gy/publication?utm_source=medium&utm_medium=medium-post&utm_campaign=publication-medium-post-end)
> 
> 👉 [Power BI Newsletter](https://powerbi-masterclass.short.gy/newsletter-medium?utm_source=medium&utm_medium=medium-post&utm_campaign=newsletter-medium-medium-post-end)
> 
> and join our Power BI community:

## [Microsoft Power BI Masterclass | Linktree](https://linktr.ee/powerbi.masterclass?utm_source=medium&utm_medium=medium-post&utm_campaign=linktree-medium-post-end&source=post_page-----93d52ce1846c---------------------------------------)

### Let’s share our Microsoft Power BI experience. Learn together. Grow together.

linktr.ee

**Power BI Masterclass Article Classification**

**Level:** Beginner

**Category:** DAX

**Tags:** Tutorial, DAX