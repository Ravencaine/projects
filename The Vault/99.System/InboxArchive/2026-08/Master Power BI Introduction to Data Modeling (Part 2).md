---
title: "Master Power BI: Introduction to Data Modeling (Part 2)"
source: "https://medium.com/microsoft-power-bi/master-power-bi-introduction-to-data-modeling-part-2-c48c9043280f"
author:
  - "[[Janvi Gupta]]"
published: 2025-12-26
created: 2026-07-29
description: "More"
Processed: "Unprocessed"
---
## Building, Testing & Troubleshooting Your First Data Model.

You Know the Theory. Now Let’s Build Something Real.

![](99.System/Attachments/1!Pq14pBYtBV269PvnRDzmyA.png.webp)

In Part 1, you learned what data modeling is, how relationships work, and why star schema beats everything else. You understand cardinality, filter direction, and the difference between fact and dimension tables.

But here’s the thing: reading about relationships is like reading about riding a bike. You don’t actually know how until you fall off a few times.

> If you haven’t read Part 1 then check it out: [**Introduction to Data Modeling**](https://medium.com/microsoft-power-bi/master-power-bi-introduction-to-data-modeling-0410bdb8c080)**!**

In Part 2, we’re going to build a complete data model from scratch. You’ll see exactly where things go wrong, how to catch problems before they break your reports, and how to fix the issues that trip up everyone.

> If you’re not a member, you can access it here using the [**Friend Link**](https://medium.com/microsoft-power-bi/master-power-bi-introduction-to-data-modeling-part-2-c48c9043280f?sk=3e996e404b413c52f1650f1dbe72550a)

By the end, you’ll have a tested, working model and a troubleshooting checklist you can use on every project.

Let’s build.

**🎁** [**Get friend links for all of our 1000> Power BI learning articles here**](https://powerbi-masterclass.short.gy/learning-database?utm_source=medium&utm_medium=medium-post&utm_campaign=database-medium-post-start) **🎁**

## 📑 What We’ll Cover in Part 2

## 1\. Building a Complete Model: E-commerce Example

### The Business Scenario

You run an online electronics store. Right now, all your sales data lives in one Excel file that looks like this:

![](99.System/Attachments/0!K8CxA5R_-ve1DMCJ.png.webp)

**The file has 9,995 rows and these problems:**

- “William Brown” appears 37 times (they’re a good customer)
- “Office Supplies” is written 6,026 times in the Category column
- File size: 1.8 MB
- When William Brown changes its email, you need to update 37 rows
- When you want to add “Customer Industry,” you need to add it to all 9,995 rows

**Your job:** Turn this into a proper Power BI data model that’s fast, accurate, and easy to maintain.

### Step 1: Identify What You’re Measuring (Your Fact Table)

Ask yourself: **“What business event am I tracking?”**

Answer: **Customer orders** (sales transactions)

That’s your fact table. It should contain:

- The transaction identifier (OrderID)
- When it happened (OrderDate)
- Foreign keys to other tables (CustomerID, ProductID)
- The numbers you want to measure (Quantity, TotalAmount)

**What NOT to include:**

- Customer names (that’s descriptive info → goes in Customers dimension)
- Product names (that’s descriptive info → goes in Products dimension)
- Categories (that’s descriptive info → goes in Products dimension)

### Step 2: Create Your Dimension Tables

**Customers Dimension:** What describes the customer?

- CustomerID (the key)
- CustomerName
- CustomerEmail
- CustomerCity
- CustomerSegment (we’ll add this: “Consumer”, “Corporate,” “Home Office”)

**Products Dimension:** What describes the product?

- ProductID (the key)
- ProductName
- ProductCategory (“Office Supplies”, “Furniture”, “Technology”)
- ProductBrand
- UnitCost (for profit calculations later)

**Date Dimension:** What describes the date?

- Date (the key)
- Year
- Quarter
- Month
- MonthName
- DayOfWeek
- IsWeekend

### Step 3: Transform Your Flat Table in Power Query

**Here’s how to split it:**

**👉 Load your Excel file into Power BI:**

1. Home → Get Data → Excel
2. Select your file
3. Check the table → Transform Data (opens Power Query)
![](99.System/Attachments/1!JqqyY_6blshKVyXV2d-H0g.png.webp)

**👉 Create the Orders (Fact) table:**

1. Right-click the query → Duplicate (name it “Orders”)
2. Remove columns you don’t need:
- Remove: CustomerName, CustomerEmail, CustomerCity
- Remove: ProductName, ProductCategory, ProductBrand
- Keep: OrderID, OrderDate, CustomerID, ProductID, Quantity, UnitPrice, TotalAmount

**👉 Create the Customers table:**

1. Right-click original query → Duplicate (name it “Customers”)
2. Remove columns: OrderID, OrderDate, ProductID, ProductName, ProductCategory, Quantity, UnitPrice, TotalAmount
3. Keep: CustomerID, CustomerName, CustomerEmail, CustomerCity
4. Right-click CustomerID → Remove Duplicates
5. Your table shrinks from 5,000 rows to about 150 unique customers
![](99.System/Attachments/1!5tGhxrVRr76QT4XryOKB3A.png.webp)

**👉 Create the Products table:**

1. Right-click original query → Duplicate (name it “Products”)
2. Remove columns: OrderID, OrderDate, CustomerID, CustomerName, CustomerEmail, Quantity, TotalAmount
3. Keep: ProductID, ProductName, ProductCategory, ProductBrand, UnitCost
4. Remove Duplicates on ProductID
5. Your table shrinks from 5,000 rows to about 45 unique products

**👉 Create the Date table:**

You can either:

- Extract unique dates from OrderDate and expand them with date attributes
- Or use a DAX calculated table (we’ll do this after loading)

**Close & Apply** to load all tables into your model.

### Step 4: Create a Date Table (Using DAX)

In Report view:

1. Modeling tab → New Table
2. Enter this DAX:
```c
Date = 
ADDCOLUMNS(
    CALENDAR(DATE(2014,1,1), DATE(2017,12,31)), 
// Manually added the date as per my data.
//you can make calendar table using min and max date of order table.

    "Year", YEAR([Date]),
    "Quarter", "Q" & FORMAT([Date], "Q"),
    "Month", MONTH([Date]),
    "MonthName", FORMAT([Date], "MMMM"),
    "DayOfWeek", WEEKDAY([Date]),
    "DayName", FORMAT([Date], "DDDD"),
    "IsWeekend", IF(WEEKDAY([Date]) IN {1,7}, "Yes", "No")
)
```

3\. Press Enter

You now have a Date table with 1,096 rows (3 years of dates) and helpful columns.

![](99.System/Attachments/1!QVgBycryq_W3dKr2uWkTMg.png.webp)

Mark it as a Date table:  
1\. Select the Date table  
2\. Table Tools → Mark as Date Table  
3\. Select "Date" as the date column

### Step 5: Build the Relationships

Switch to Model View.  
You should see four tables: Orders, Customers, Products, and Date

![](99.System/Attachments/1!ThKPYE8_Qk998Si4O9ZjGQ.png.webp)

Create the relationships:

**Relationship 1: Customers to Orders**  
\- Drag CustomerID from Customers table  
\- Drop on CustomerID in Orders table  
\- Verify: Shows "1" on Customers side, "\*" on Orders side

**Relationship 2: Products to Orders**  
\- Drag ProductID from Products table  
\- Drop on ProductID in Orders table  
\- Verify: Shows "1" on Products side, "\*" on Orders side

**Relationship 3: Date to Orders**  
\- Drag Date from Date table  
\- Drop on OrderDate in Orders table  
\- Verify: Shows "1" on Date side, "\*" on Orders side

Your final model looks like this:

![](99.System/Attachments/1!AuVa7EHWI56Rk93VM_2awg.png.webp)

**File size check:**

- Before: 2.8 MB (one flat table)
- After: 0.9 MB (star schema with relationships)
- You just saved 68% space while making it easier to maintain.

### Step 6: Create Your First Measures

Click on the Orders table, then:

**Modeling → New Measure**

```c
Total Revenue = SUM(Orders[TotalAmount])
```
```c
Total Orders = COUNTROWS(Orders)
```
```c
Average Order Value = DIVIDE([Total Revenue], [Total Orders], 0)
```
```c
Total Quantity Sold = SUM(Orders[Quantity])
```
```c
Total Customers = DISTINCTCOUNT(Orders[CustomerID])
```

Pro tip: Create a separate table just for measures:

1. Modeling → New Table
2. Name it "\_Measures" (the underscore puts it at the top of the field list)
3. Enter: \`\_Measures = ROW("X", 1)\`
4. Cut and paste your measures into this table
5. Hide the "X" column

Now all your measures are organized in one place.

![](99.System/Attachments/1!G8pyKG7EE0zMuSXlh76Owg.png.webp)

Table View

![](99.System/Attachments/1!yn8HkE4CUNypBdFIRsH-8g.png.webp)

Report View — X column is not visible

## 2\. Testing Your Data Model

Don’t build ten visuals yet. Test your model first.

### Test 1: The Basic Table Test

Create a table visual with:

- Rows: ProductCategory (from Products)
- Values: \[Total Revenue\]
![](99.System/Attachments/1!ZnNF4P6womnv4kQvzTJ2vg.png.webp)

See in PBI Report

![](99.System/Attachments/1!bsCybRW_RYrtOTAUAvVt0w.png.webp)

Sales generated by Furniture

**What to check:**

Do you see all product categories?

Does the total at the bottom match your Excel total?

Any unexpected blanks?

If your total shows 10x too high, you have a relationship problem. Stop and fix it before continuin

### Test 2: The Slicer Test

Add a slicer with Year (from Date table)

Select 2017.

![](99.System/Attachments/1!zjXo8r1uwSQ_2ck4zi_YYg.png.webp)

**What to check:**

Does the table update to show only 2017 data?

Does the total decrease?

If nothing changes, your Date relationship isn’t working.

### Test 3: The Cross-Filter Test

Add another table visual:

- Rows: CustomerName (from Customers)
- Values: \[Total Revenue\]

Add a slicer with ProductCategory

Select “Technology.”

![](99.System/Attachments/1!Znqi0jvvpiJP5hUxTyQP0Q.png.webp)

**What to check:**

The product table shows only **Technology**.

The customer table displays only customers who have purchased Technology.

Both totals match🙌

If the customer table doesn’t update, check your relationship directions.

### Test 4: The Blank Test

Look at your visuals. Do you see any rows labeled “(Blank)”?

**If yes:**

Orders table has a CustomerID that doesn’t exist in Customers table

Or a ProductID that doesn’t exist in Products table

Or the data types don’t match

**How to find the problem:**

1. Create a table visual with OrderID and CustomerID from Orders
2. Filter to show only blanks in the CustomerName column
3. You’ll see which OrderIDs have invalid CustomerIDs
4. Fix the source data

### Test 5: The Measure Test

Check your measures make sense:

```c
// This should equal Total Orders
Check = [Total Revenue] / [Average Order Value]
```
![](99.System/Attachments/1!60YIzr7rTjAQ48m4IShAug.png.webp)

If \[Check\] doesn’t equal \[Total Orders\], something’s wrong with your measures or relationships.

## 3\. Common Problems & How to Fix Them

### Problem 1: Numbers Are 10x Too High

**You see:**

Expected total: $2,657,000

Actual total: $26,570,000

**Cause:** Many-to-many relationship duplicating data.

**How to diagnose:**

1. Go to Model view
2. Look for relationships showing “\*” on both sides
3. Or check if you have two paths between tables

**The fix:**

Delete the extra relationship causing the loop. Keep only direct, clean one-to-many paths.

**Example:**

If you connected Orders → Products → Categories AND Orders → Categories directly, delete the direct Orders → Categories link.

### Problem 2: Slicers Don’t Filter Visuals

**You see:**

Select “Enterprise” in Customer Segment slicer

Sales chart doesn’t change

**Cause:** Either no relationship exists, or the filter direction is wrong.

**How to diagnose:**

1. Go to Model view
2. Check if there’s a line connecting Customers and Orders
3. If yes, check which direction the arrow points

**The fix:**

**If no line exists:**

Create the relationship (Customers\[CustomerID\] → Orders\[CustomerID\])

**If the line exists but the arrow points the wrong way:**

Click the relationship → Properties → Change “Cross filter direction” to “Single” and make sure the arrow points from Customers to Orders.

### Problem 3: (Blank) Rows Everywhere

For example, Customer Name with Revenue showing:

- TechWorld: $450,000
- (Blank): $120,000
- GlobalCo: $230,000

**Cause:** OrderID 1234 has CustomerID “C999”, but there’s no customer C999 in the Customers table.

**How to diagnose:**

Create a table with:

- OrderID (from Orders)
- CustomerID (from Orders)
- CustomerName (from Customers)
- Filter to show only blanks in CustomerName

**The fix:**

**Option 1:** Add the missing customer to Customers table

**Option 2:** If CustomerID “C999” is invalid, fix it in the source data

**Option 3:** Use this measure to exclude blanks:

```c
Revenue (Excl Blanks) = 
CALCULATE(
    [Total Revenue],
    NOT(ISBLANK(Customers[CustomerName]))
)
```

### Problem 4: Can’t Create Second Date Relationship

**You try:**

Connect Orders\[ShipDate\] to Date\[Date\], but Power BI says “A relationship already exists.”

**Cause:** You already connected Orders\[OrderDate\] to Date\[Date\]. Only one can be active.

**The fix:**

1. Create the second relationship (it will be inactive/dotted line)
2. Create a separate measure:
```c
Revenue by Ship Date = 
CALCULATE(
    [Total Revenue],
    USERELATIONSHIP(Orders[ShipDate], Date[Date])
)
```

Now you can choose which date to analyze by: OrderDate (default) or ShipDate (using the specific measure).

## 4\. Using Calculated Columns for Relationships

Sometimes your tables don’t have matching columns to create a relationship. You need to create one.

### Scenario: Creating a Month-Year Key

**Problem:**

- Your Orders table has OrderDate (full date: 2024–03–15)
- Your Budget table has Month and Year as separate columns
- You need to connect them

**Solution: Create a matching key**

**In Orders table, create calculated column:**

```c
MonthYear = 
FORMAT(Orders[OrderDate], "YYYY-MM")
```

Result: “2024–03”

**In Budget table, create calculated column:**

```c
MonthYear = 
Budget[Year] & "-" & FORMAT(Budget[Month], "00")
```

Result: “2024–03”

**Now create relationship:** Orders\[MonthYear\] → Budget\[MonthYear\]

### Scenario: Extracting Just the Date from DateTime

**Problem:**

- Orders table has DateTime: 2024–03–15 14:32:18
- Date table has just dates: 2024–03–15
- Can’t create relationship (types don’t match)

**Solution:**

**In Orders table, create calculated column:**

```c
OrderDateOnly = INT(Orders[OrderDateTime])
```

or

```c
OrderDateOnly = DATE(
    YEAR(Orders[OrderDateTime]),
    MONTH(Orders[OrderDateTime]),
    DAY(Orders[OrderDateTime])
)
```

**Now create relationship:** Orders\[OrderDateOnly\] → Date\[Date\]

### When to Use Power Query Instead

**Use calculated columns (DAX) when:**

- You need to use RELATED() to pull data from another table
- The calculation depends on relationships

**Use Power Query (M) when:**

- Simple transformations (text manipulation, date extraction)
- The calculation doesn’t need relationships
- You want better compression and performance

**Example in Power Query:**

Instead of a DAX calculated column, do this in Power Query:

1. Select OrderDateTime column
2. Transform → Date → Date Only
3. Rename to OrderDate

This is more efficient than a calculated column.

## 5\. Troubleshooting Quick Reference

![](99.System/Attachments/1!VnYDv60P7d1Or-mbyf253w.png.webp)

### The Debugging Process

**When something’s wrong:**

**1\. Check the Model View first**

- Look for broken relationships (red exclamation marks)
- Verify cardinality (should be 1:\* or \*:1)
- Check for many-to-many (\*)

**2\. Create a simple test visual**

- Table with dimension + measure
- Does it show correct data?

**3\. Add one slicer**

- Does it filter the table?
- If not, relationship problem

**4\. Check source data totals**

- Compare Power BI total to Excel/source
- Difference = relationship issue

**5\. Isolate the problem**

- Remove all visuals except one
- Add elements back one at a time
- Find which relationship causes issues

## Key Takeaways

Let’s recap what we’ve learned:

**1\. Data modeling isn’t optional in Power BI — it’s the foundation** Without proper relationships, your measures will show wrong numbers, your filters won’t work, and your reports will be frustrating to use.

**2\. Excel thinking doesn’t translate to Power BI** One big flat table worked in Excel. In Power BI, split data into connected fact and dimension tables.

**3\. Star schema solves 90% of scenarios** One fact table in the center (transactions), dimension tables around it (descriptive attributes). Simple, fast, maintainable.

**4\. One-to-many relationships are your best friend** Avoid many-to-many unless you have a specific business reason and understand the implications.

**5\. Test your model before building visuals** Create a simple table visual, add a slicer, verify numbers match your source data. Catch relationship problems early.

**6\. Wrong relationships = wrong numbers, every time** That $47 million problem? It’s always a relationship issue. Check Model view first when numbers look weird.

## Connection to Your Power BI Journey

You’ve now completed the foundation of Power BI:

✅ **You learned to connect and transform data** in Power Query  
✅ **You learned to create measures and calculations** that work correctly  
✅ **You now know how to structure data models** that make those measures accurate.

Let’s understand more about DAX in the next blog. 🙌

If you have any questions, please share them in the comments below, or **connect with me on LinkedIn —** [**Janvi Gupta**](https://www.linkedin.com/in/janvisgupta/) **😊**

**You can also schedule a call on Topmate: J** [**anvi Gupta**](https://topmate.io/janvigupta)

![](99.System/Attachments/0!eLaYLA5u8JTRasSV.gif)

Dream big, but start small..!

**💡** [**MUST TRY — Power BI GPT — Personal Power BI Learning Coach**](https://powerbi-masterclass.short.gy/pbi-gpt?utm_source=medium&utm_campaign=pbi-gpt-medium-post-end) **💡**

> Don’t forget to subscribe to
> 
> 👉 [Power BI Publication](https://powerbi-masterclass.short.gy/publication?utm_source=medium&utm_medium=medium-post&utm_campaign=publication-medium-post-end)
> 
> 👉 [Power BI Newsletter](https://powerbi-masterclass.short.gy/newsletter-medium?utm_source=medium&utm_medium=medium-post&utm_campaign=newsletter-medium-medium-post-end)
> 
> and join our Power BI community:

## [Microsoft Power BI Masterclass | Linktree](https://linktr.ee/powerbi.masterclass?utm_source=medium&utm_medium=medium-post&utm_campaign=linktree-medium-post-end&source=post_page-----c48c9043280f---------------------------------------)

### Let’s share our Microsoft Power BI experience. Learn together. Grow together.

linktr.ee

**Power BI Masterclass Article Classification**

**Level:** Beginner

**Category:** Data Model

**Tags:** Tutorial, Data Model