---
title: "Master Power BI: Introduction to Data Modeling!"
source: "https://medium.com/microsoft-power-bi/master-power-bi-introduction-to-data-modeling-0410bdb8c080"
author:
  - "[[Janvi Gupta]]"
published: 2025-12-15
created: 2026-07-29
description: "More"
Processed: "Unprocessed"
---
## You Built Perfect Measures. Your Data Is Clean. So, Why Do Your Numbers Look Like Someone Multiplied Everything by 10?

You’ve mastered Power Query transformations. You understand the difference between measures and calculated columns. You even wrote some clean DAX formulas that calculate correctly.

You create a simple bar chart showing total sales by product category. The visual looks good. But then you notice something odd: the total shows $47 million. You check your source data in Excel — it says $4.7 million. You look at the raw data in Power BI’s Data view — also $4.7 million.

So why does every chart you create show inflated numbers?

Here’s what happened: Power BI is multiplying your sales because of a relationship problem you didn’t know existed. Your Sales table connects to your Products table, which connects to your Categories table, and somewhere in that chain, there’s a many-to-many relationship that’s duplicating every row.

This is the data modeling trap that catches everyone who moves from Excel to Power BI.

**In Excel**, you put everything in one giant table — customer names, product details, sales amounts, dates — all sitting happily in adjacent columns. You use VLOOKUP to pull data from other sheets, and it works.

**In Power BI**, that approach breaks everything. Power BI expects you to split data across multiple related tables. It uses relationships instead of VLOOKUP. And if those relationships are wrong, every measure you write, every visual you create, will show incorrect numbers.

You already know how to write measures. Now you need to understand the structure those measures operate within — your data model.

**This two-part series will teach you everything about data modeling:**

In Part 1 (this one), we’ll cover the foundation — what data modeling is, how relationships work, and the patterns you’ll use 90% of the time.

In Part 2, we’ll build real models, troubleshoot problems, and make sure your numbers are always correct.

**🎁** [**Get friend links for all of our 1000> Power BI learning articles here**](https://powerbi-masterclass.short.gy/learning-database?utm_source=medium&utm_medium=medium-post&utm_campaign=database-medium-post-start) **🎁**

## 📑 What We’ll Cover in Part 1

## 1\. What Is Data Modeling?

### In Simple Terms

Data modeling is how you organize and connect your tables in Power BI so they work together properly.

![](99.System/Attachments/0!UM6jP90QEF-rHHOz.webp)

Think of it like organizing a kitchen. You could dump all your utensils, plates, and food in one giant drawer. But when you need a specific spoon, good luck finding it. Instead, you create separate drawers: one for utensils, one for plates, one for cups. Each has its place, and you know exactly where to find things.

That’s data modeling. Organized tables that connect logically.

### Why Excel Users Get Confused

In Excel, most of us learned to put everything in one table. It looks like this:

![](99.System/Attachments/1!8iiBoNL4cN0zGCXxSwu2IA.png.webp)

Excel Flat Table

One row contains everything about a transaction. You can read left to right and see the complete picture.

This worked in Excel because:

- You had maybe 10,000 rows (manageable)
- VLOOKUP pulled data from other sheets when needed
- Pivot tables handled the heavy lifting
- File size wasn’t usually a problem

But in Power BI, this creates three massive problems:

**Problem 1: Ridiculous duplication**

If ABC Corp makes 1,000 purchases, you store “ABC Corp” and “New York” 1,000 times. That’s 1,000 copies of the same information.

**Problem 2: Update nightmares**

ABC Corp moves from New York to Boston. Now you need to find and update 1,000 rows. Miss even one, and your report shows ABC Corp in two cities. Which is correct? Nobody knows.

**Problem 3: File bloat**

With millions of transactions, storing all that repeated text in every row makes your file massive. What should be a 50MB file becomes 500MB. Refreshes take forever.

### The Power BI Approach: Split and Connect

Power BI wants you to split that one big table into multiple smaller, connected tables:

**Sales Table (just the transaction)  
Customers Table (customer details, stored once)  
Products Table (product details, stored once)**

Now ABC Corp’s details exist in exactly one place. If they move to Boston, you update one row. Done.

But here’s the critical part: these tables need to be **connected** so Power BI knows that CustomerID “1” in the Sales table refers to “ABC Corp” in the Customers table.

Those connections are called **relationships**, and they’re the foundation of everything in Power BI.

## 2\. Understanding Relationships

### What Are Relationships?

Relationships are the invisible bridges between your tables. They tell Power BI: “When you see CustomerID in the Sales table, go look up that customer’s details in the Customers table.”

Think of relationships like your company’s employee ID system. Your timesheet shows employee ID 1047. Your HR system has a record for employee 1047 that contains their name, department, and salary. When your manager reviews timesheets, they don’t see “1047” — they see “John Smith, Marketing, 40 hours.” That lookup happens automatically because of how the systems are connected.

That’s exactly what relationships do in Power BI.

### Why They Matter

Without relationships, Power BI treats your tables as completely separate islands. You can’t filter one based on the other. Your measures show wrong totals. Everything falls apart.

With proper relationships:

- Filter by customer name → automatically filters their sales
- Slice by product category → sees all products in that category
- Your measures calculate correctly
- Visuals respond to each other

### How They Work in Practice

Let’s say you create a chart with:

- Customer Name (from Customers table)
- Total Sales (from Sales table)

**Behind the scenes**, Power BI:

1. Looks at the unique customers in your Customers table
2. For each customer, finds their CustomerID
3. Uses the relationship to find all rows in Sales with that CustomerID
4. Sums up those sales
5. Displays the result

All because of that relationship connecting CustomerID in both tables.

![](99.System/Attachments/0!awo4lvlkyu1NmK42.png.webp)

### The Real Difference from Excel

In Excel, if you want to show customer names next to sales amounts, you write: `=VLOOKUP(A2, Customers!A:B, 2, FALSE)`

Then you copy that formula down 10,000 rows. If customer names change, your VLOOKUP might break. If you sort one column, the VLOOKUPs don’t update.

In Power BI, you create the relationship once. Then you just write: `Total Sales = SUM(Sales[Amount])`

The relationship handles everything else. Forever. No copying formulas. No broken references when data updates.

## 3\. Types of Relationships

### 1\. One-to-Many (Use This 90% of the Time) ⭐

**What it means:  
**One record on one side connects to many records on the other side.

**Visual indicator in Model view:**

- “1” on one side
- “\*” (asterisk) on the many side

**Real-world examples:**

**One customer, many orders:**

```c
Customer: Acme Industries
Their orders: 50 orders in January, 75 in February, 60 in March...

Customers (1) ———— (*) Orders
```

Each customer appears once in the Customers table. But that same customer can place unlimited orders.

**One product, many sales:**

```c
Product: Wireless Mouse Pro
Sales: Sold 15 times on Monday, 22 times on Tuesday, 8 times on Wednesday..

Products (1) ———— (*) Sales
```

The product exists once in your Products table. But it appears in hundreds of different sales transactions.

**Why this works perfectly:**

On the “one” side (Customers), each CustomerID appears exactly once. No duplicates. Clean.

On the “many” side (Orders), CustomerID can repeat endlessly. Same customer, different orders.

This is clean, logical, and fast. Power BI’s engine loves this structure.

**This should be your default choice.** If you’re unsure what type of relationship to create, start with one-to-many. It works in almost every business scenario.

### 2\. Many-to-One (Just the Reverse)

This is the exact same as one-to-many, just described from the opposite direction.

Power BI treats many-to-one and one-to-many identically. It’s just a perspective thing. When you create a relationship, you might see it labeled as “Many-to-one (\*:1)” in the properties — that’s fine. It’s the same concept.

### 3\. Many-to-Many (The Troublemaker) ⚠️

**What it means:  
**Multiple records on both sides can match multiple records on the other side.

**Real business example: Sales Territories**

```c
Salesperson: Robert Chen
His territories: California, Oregon, Washington

Territory: California
Salespeople covering it: Robert Chen, Maria Garcia, David Kim

Salesperson: Maria Garcia
Her territories: California, Nevada, Arizona

Territory: Nevada
Salespeople covering it: Maria Garcia, James Wilson
```

Robert covers three territories. California has three salespeople. There’s no clear “one” side.

**Why this is dangerous:**

If you connect Salespeople directly to Territories with many-to-many, and then try to calculate total sales by territory, Power BI will count Robert’s California sales multiple times — once for each salesperson covering California.

**The problem illustrated:**

Robert closed a $100,000 deal in California.

With a direct many-to-many relationship:

- Robert’s sales: $100,000
- Maria’s sales: $50,000
- David’s sales: $75,000

But when you filter by “California,” instead of showing $225,000 (the correct total), Power BI might show $675,000 because it’s counting each sale multiple times based on the overlapping relationships.

**The solution: Assignment Table (Bridge table)**

Don’t connect Salespeople directly to Territories. Instead, create a table that lists each assignment:

**SalespersonTerritory Assignment Table:**

![](99.System/Attachments/1!q4uTvRzQJm6AN1zA54HJLw.png.webp)

SalespersonTerritory Assignment Table

Now you have two clean one-to-many relationships:

```c
Salespeople (1) ———— (*) Assignment (Many)
Territories (1) ———— (*) Assignment (Many)
```

Each relationship is one-to-many. No confusion. Correct counts. Your $225,000 shows as $225,000.

**Other real-world many-to-many scenarios:**

**Project assignments:**

- One employee works on multiple projects
- One project has multiple employees
- Solution: Create an EmployeeProjects assignment table

**The rule:** Always avoid direct many-to-many relationships. Use a bridge/assignment table instead. It keeps your data clean and your numbers accurate.

### 4\. One-to-One (Rarely Used)

Both sides have exactly one matching record.

**Example:**

```c
Employee (1) ———— (1) Employee Salary Details

Employee ID 1001 has exactly one salary record
That salary record belongs to exactly one employee
```

**Real scenario where you might see this:**

You have employee data split across two systems:

- **HR System:** EmployeeID, Name, Department, HireDate
- **Payroll System:** EmployeeID, Salary, BankAccount, TaxBracket

Each employee has exactly one record in each system.

**When you see this:**

Usually, these should just be one table. Why split them?

**Valid reasons to split:**

- **Security:** Keep sensitive salary data separate with restricted access
- **Performance:** Keep large text fields (like performance reviews) in a separate table
- **Source systems:** You’re connecting to two different databases that you can’t combine

**In most cases:** Just merge these into one table in Power Query. Simpler is better.

## 4\. Fact Tables vs. Dimension Tables

Before we talk about star schema, you need to understand these two types of tables. Every table in your model falls into one of these categories.

### Fact Tables: The “What Happened” Tables

Fact tables contain measurable business events — the transactions, the actions, the things you want to count or sum.

**Characteristics:**

- Mostly numbers and IDs (very little text)
- Many rows (thousands to millions)
- Each row is an event or transaction
- Grows over time (new rows added constantly)
- Contains the data you want to measure

**Real examples:**

**E-commerce sales:** Each row = one completed order

![](99.System/Attachments/1!Z_TGPoN9pqcNhSDkpu6Z0Q.png.webp)

Order Details Table

**What you measure from fact tables:**

- Total revenue: `SUM(Sales[Revenue])`
- Number of orders: `COUNTROWS(Sales)`
- Average call duration: `AVERAGE(Calls[CallDuration])`
- Defect rate: `DIVIDE(SUM(Production[DefectCount]), SUM(Production[UnitsProduced]))`

**Key point:** Fact tables answer “How much?” and “How many?”

### Dimension Tables: The Who, What, When, Where Tables

Dimension tables contain descriptive information that gives context to your facts. They’re the details that help you slice, filter, and group your measures.

**Characteristics:**

- Mostly text and categories
- Fewer rows (dozens to thousands)
- Relatively stable (changes infrequently)
- Contains the attributes you filter and group by
- Provides the “story” around the numbers

**Real examples:**

**Customer dimension:**  
Describes who the customer is and what kind of business they run.

![](99.System/Attachments/1!AYYR5SpAKbizbTnva72BsQ.png.webp)

**Products dimension:**  
Describes what the product is and where it comes from

![](99.System/Attachments/1!F74UO3FfgpTm0lWAz72YLQ.png.webp)

**Key point:** Dimension tables answer “Who?”, “What?”, “When?”, “Where?”, and “Why?”

### How to Tell Them Apart

Ask yourself:**  
1\. Does each row represent a transaction or event?**

- **Yes** → Fact table
- **No** → Dimension table

**2\. Will this table grow significantly over time?**

- **Yes** → Probably a fact table (new sales every day)
- **No** → Probably a dimension (your product list doesn’t double every week)

**3\. Am I measuring this or describing something?**

- **Measuring** → Fact (measuring sales amounts)
- **Describing** → Dimension (describing what products are)

4\. **Does this table have mostly numbers or mostly text?**

- **Numbers** → Fact
- **Text** → Dimension

### A Real Scenario

You’re building a report for a retail company. Here’s their data:

1. **Sales transactions:** 2 million rows, adds 5,000 rows per day → **Fact table**
2. **Products catalog:** 500 rows, updates occasionally when new products launch → **Dimension table**
3. **Stores:** 150 rows, rarely changes unless new stores open → **Dimension table**
4. **Customer list:** 50,000 rows, grows as new customers sign up → **Dimension table** (even though it’s large, each customer is described once)
5. **Daily inventory snapshot:** 75,000 rows (500 products × 150 stores), updated every morning → **Fact table** (it’s a snapshot of an event/state at a point in time)

### The Connection

Fact tables live at the center of your model. Dimension tables connect to them, providing context.

When you create a measure in a fact table and filter it by a dimension attribute, the relationship makes it work.

Example:

- Measure: `Total Sales = SUM(Sales[Amount])` (from fact)
- Filter: Product Category = “Electronics” (from dimension)
- Result: Total sales for electronics only

The relationship between Sales and Products makes this possible.

## 5\. Star Schema vs. Snowflake Schema

Now that you understand fact and dimension tables, let’s talk about how to arrange them.

### Star Schema (The Recommended Standard) ⭐

**What it looks like:  
**One fact table in the center. Dimension tables connected directly to it, like points on a star.

![](99.System/Attachments/0!yA6Eo2f5ZS4ZYytS.png.webp)

**Structure:**

- **Center:** Sales (fact table with transactions)
- **Points:** Stores, Products, Date, Customers (dimension tables)
- **Connections:** Each dimension connects directly to the fact table

**Real example for retail:**

**Sales (Fact — center):** TransactionID, SaleDate, StoreID, ProductID, CustomerID, Quantity, Revenue, Cost

**Stores (Dimension):** StoreID, StoreName, City, State, Region, StoreManager, SquareFeet

**Products (Dimension):** ProductID, ProductName, Category, Brand, Supplier, UnitCost

**Customers (Dimension):** CustomerID, CustomerName, Email, LoyaltyTier, SignupDate

**Date (Dimension):** Date, Year, Quarter, Month, Week, DayOfWeek, IsHoliday

**Why is it called “star”:**

Open your model in Model view, and it literally looks like a star. The fact table sits in the middle with lines radiating out to dimensions. (See the above Image..!)

**Key characteristic:** Dimensions are **denormalized** (flat). All the product info lives in one Products table — Category, Brand, Supplier — all in one place.

### Benefits of Star Schema

**1\. Instantly understandable  
**Anyone looking at your model immediately sees: “Here’s the sales transactions. Here are the things that describe those sales.”

Even non-technical stakeholders can follow it.

**2\. Blazing fast performance  
**Power BI’s engine is built for this structure. Queries run faster. Refreshes complete quicker. Everything just works better.

**3\. Simple measures**

```c
Total Revenue = SUM(Sales[Revenue])
Average Order Value = DIVIDE([Total Revenue], COUNTROWS(Sales))
```

That’s it. Clean. The relationships handle the rest.

**4\. Easy maintenance  
**Need to add “Customer Credit Rating”? Add one column to Customers. Done.

Need to add “Product Warranty Period”? Add one column to Products. Done.

You never touch the Sales fact table.

**5\. Scales beautifully  
**Works the same with 1,000 sales or 10 million sales. The structure doesn’t change.

**6\. User-friendly  
**When business users explore data, they see logical groups:

- “Sales” has the numbers
- “Products” has product info
- “Customers” has customer info

Simple and clear.

### Snowflake Schema (The Normalized Alternative)

**What it looks like:  
**Dimension tables have their own dimension tables, creating branches like a snowflake.

![](99.System/Attachments/1!sSR3kpTPm5-5nKLh1UrFRQ.jpeg.webp)

**Structure:**

- Products table → connects to Categories table → connects to Brands table
- Sales table → connect to Customers table → connects to Cities table

**Why this exists:**

This comes from traditional database design (called “normalization”). Databases do this to:

- Save storage space (store “Electronics” once instead of 500 times)
- Maintain consistency (can’t misspell “Electronics” because it exists in only one place)
- Update easily (change category name once, affects all products automatically)

**The problem in Power BI:**

What works well in a transactional database doesn’t work well in Power BI.

- Users get confused: “Why do I have three tables just for product information?”
- Queries are slower: Power BI has to hop through multiple tables
- Relationships are more complex: More places for things to break
- Harder to maintain: Changes affect multiple tables

### Star vs. Snowflake: Side-by-Side

![](99.System/Attachments/1!ulevVN9PB_IDv_cnnbVUqg.png.webp)

**The key insight:** The storage-saving benefit of snowflake schema disappears in Power BI because of its compression. “Electronics” stored 500 times compresses to nearly the same size as storing it once with 500 references.

### What to Do If You Have a Snowflake Schema

**Option 1: Flatten it in Power Query (Recommended)  
**Merge the related tables into one dimension table.

**Example: Product hierarchy**

Instead of:

- Products (ProductID, ProductName, CategoryID)
- Categories (CategoryID, CategoryName, BrandID)
- Brands (BrandID, BrandName)

Create:

- Products (ProductID, ProductName, CategoryName, BrandName)

**How to do it:** In Power Query, merge Categories into Products, then merge Brands, then remove the original reference columns.

Now users see one clean Products dimension with all the info.

**Option 2: Keep it but hide complexity**

If the database structure is managed by a database team and you can’t change it:

- Keep the snowflake structure
- But hide the intermediate tables from Report view
- Create a hierarchy in the Products table that pulls from related tables

Users see a simplified view even though the structure underneath is complex.

### Real Example: Before and After

**Before (Snowflake from database):**

```c
Brands → Categories → Subcategories → Products → Sales
```

Users trying to analyze sales by brand have to understand four relationships.

**After (Flattened Star):**

```c
Products → Sales
```

Products table now has columns: Brand, Category, and Subcategory.

Users just drag “Brand” from Products. Simple.

![](99.System/Attachments/0!4x3gCHYDw5UMdnXb.png.webp)

### The Recommendation

**Always use star schema in Power BI.**

If you’re building from scratch, use star schema.

If you import a snowflake schema from a database, flatten it in Power Query during your transformation step.

Star schema is simpler, faster, and more user-friendly. There’s almost no downside.

## 6\. Cardinality & Filter Direction

When you click on a relationship line in Model view, you’ll see two critical settings in the Properties pane: **Cardinality** and **Cross filter direction**. Let’s understand what these mean.

### Cardinality: Defining the Relationship Type

**What it is:** Cardinality tells you how many records on each side can match.

![](99.System/Attachments/0!Dcy3b-uKV5gePKaM.png.webp)

1. **Many to one (*:1) or One to many (1:*)** — What you want 90% of the time  
	**Example:** Your Sales table has 50 transactions for Customer “ABC Industries.” But the Customers table has exactly one row for ABC Industries.
2. **Many to many (\**:\**)** — Red flag

Both sides have duplicate values. Usually means you need a bridge table or there’s a data quality issue.

If you see this, stop and investigate:

- Check if the “one” side actually has duplicates
- Consider if you need a bridge/assignment table
- Verify you’re connecting the right columns

**3\. One to one (1:1)** — Rare

Each record matches exactly one record on the other side. Usually these tables should just be merged into one.

### Cross-Filter Direction: Which Way Do Filters Flow?

**What it controls:  
**When you filter one table, which other tables get filtered?

![](99.System/Attachments/0!4hFLu7eU1_o3zwpG.png.webp)

**The two options:**

1. **Single (Default — Use This)** →

Filters flow one direction only — from the “one” side to the “many” side.

```c
Customers (1) → (*) Sales

Select a customer → filters their sales ✓
Select a product → does NOT filter customers ✓
```

**Real scenario:**

You create a slicer with Customer Industry. Select “Manufacturing.”

What happens:

- Sales table shows only manufacturing customer sales ✓
- Revenue updates to show manufacturing totals ✓
- Customer list still shows all customers ✓

This is predictable and fast.

**2\. Both (Bi-directional)** ↔

Filters flow in both directions.

```c
Customers (1) ←→ (*) Sales

Select a customer → filters sales ✓
Select a product → ALSO filters customers ✓
```

Same scenario: Select “Manufacturing” → Sales filtered to manufacturing customers

But now if you also filter by a specific product, the Customer slicer updates to show only customers who bought that product. Sometimes this is what you want. Usually, it’s confusing.

**When to use Both:**

- Row-level security requirements
- Specific many-to-many scenarios with bridge tables
- You have a clear business reason and understand the impact

**Why to avoid Both (Bi-Directional):**

- Slower performance
- Unexpected filtering behavior that confuses users
- Higher risk of circular dependencies
- Harder to debug when things go wrong

**The rule:**

Always start with **Single**. Only change to **Both** if you have a specific, documented reason.

![](99.System/Attachments/0!MdiUvpuI0_zNZoLk.png.webp)

## 7\. Active vs. Inactive Relationships

### The Problem: Multiple Dates

Your Orders table has three date columns:

- **OrderDate** — when customer placed the order
- **ShipDate** — when you shipped it
- **DeliveryDate** — when customer received it

You want to analyze orders by all three dates, but you also have a Date dimension table.

**The challenge:**

Power BI only allows **one active relationship** between any two tables.

You can’t connect OrderDate, ShipDate, AND DeliveryDate all actively to the Date table.

### The Solution: One Active, Others Inactive

Create all three relationships. Mark one as active, the others as inactive.

![](99.System/Attachments/0!YWrXM73R0-hxKW98.png.webp)

**Setup:**

1. Orders\[OrderDate\] → Calendar\[Date\] — **Active** (solid line)
2. Orders\[ShipDate\] → Calendar\[Date\] — **Inactive** (dotted line)
3. Orders\[DeliveryDate\] → Calendar\[Date\] — **Inactive** (dotted line)

### How It Works

**For the active relationship:  
**Just use it normally. Create a visual with Month from the Date table and Total Orders. It automatically uses OrderDate. No special code needed.

**For inactive relationships:  
**Use USERELATIONSHIP() in a measure to temporarily activate it.

**dax:**

```c
// Activates the ShipDate relationship
Orders Shipped = 
CALCULATE(
    COUNTROWS(Orders),
    USERELATIONSHIP(Orders[ShipDate], Calendar[Date])
)// Activates the DueDate relationship
Orders Delivered = 
CALCULATE(
    COUNTROWS(Orders),
    USERELATIONSHIP(Orders[DueDate], Calendar[Date])
)
```

## Key Takeaways from Part 1

You’ve just learned the foundation of data modeling. Here’s what you now understand:

✅ **Data modeling is structure** — How you organize tables matters as much as the data itself

✅ **Relationships replace VLOOKUP** — They connect tables automatically and permanently

✅ **One-to-many is your default** — Use it 90% of the time. Avoid many-to-many without a bridge table

✅ **Fact tables = transactions, Dimension tables = descriptions** — Know the difference and structure accordingly

✅ **Star schema is the standard** — One fact in center, dimensions around it. Simple, fast, effective

✅ **Snowflake schemas should be flattened** — What works in databases doesn’t work well in Power BI

✅ **Creating relationships is straightforward** — Drag and drop in Model view, verify the cardinality

✅ **Cardinality defines the relationship type** — Make sure you see “Many to one” or “One to many”

✅ **Filter direction controls behavior** — Start with Single, only use Both when absolutely necessary

✅ **Inactive relationships solve multiple-date problems** — Use USERELATIONSHIP() to activate them in measures

If you have any questions, please share them in the comments below, or **connect with me on LinkedIn —** [**Janvi Gupta**](https://www.linkedin.com/in/janvisgupta/) **😊**

**Or you can schedule a call on Topmate: J** [**anvi Gupta**](https://topmate.io/janvigupta)

![](99.System/Attachments/0!F-9BIv-ECcJpVZU1.gif)

Dream big, but start small..!

**💡** [**MUST TRY — Power BI GPT — Personal Power BI Learning Coach**](https://powerbi-masterclass.short.gy/pbi-gpt) **💡**

> Don’t forget to subscribe to
> 
> 👉 [Power BI Publication](https://powerbi-masterclass.short.gy/publication?utm_source=medium&utm_medium=medium-post&utm_campaign=publication-medium-post-end)
> 
> 👉 [Power BI Newsletter](https://powerbi-masterclass.short.gy/newsletter-medium?utm_source=medium&utm_medium=medium-post&utm_campaign=newsletter-medium-medium-post-end)
> 
> and join our Power BI community:

## [Microsoft Power BI Masterclass | Linktree](https://linktr.ee/powerbi.masterclass?utm_source=medium&utm_medium=medium-post&utm_campaign=linktree-medium-post-end&source=post_page-----0410bdb8c080---------------------------------------)

### Let’s share our Microsoft Power BI experience. Learn together. Grow together.

linktr.ee

**Power BI Masterclass Article Classification**

**Level:** Beginner

**Category:** Data Model

**Tags:** Tutorial, Data Model