---
created: 2026-08-01
updated: 2026-08-02
source: "Master Power BI Introduction to Data Modeling (Part 2).md"
note_type: atomic
tags: [power-bi, data-modeling, beginner, etl, power-query, star-schema, date-table]
---

# E-Commerce Model: Step-by-Step Build

From one flat Excel file (9,995 rows, 1.8MB) to a clean star schema in Power BI. This is the exact workflow.

## Step 1: Identify the Fact Table

Ask: "What business event am I tracking?" → **Orders** (sales transactions)

The fact table should contain:
- Transaction identifier (OrderID)
- When it happened (OrderDate)
- Foreign keys to dimensions (CustomerID, ProductID)
- The numbers to measure (Quantity, UnitPrice, TotalAmount)

**What NOT to include:** Customer names, product names, categories — those are descriptive, not transactional. → dimension tables.

## Step 2: Load and Split in Power Query

Load the flat Excel file → Transform Data (opens Power Query Editor).

**Duplicate the query three times** for each dimension, then Remove Columns to isolate:

**Orders (fact):**
- Keep: OrderID, OrderDate, CustomerID, ProductID, Quantity, UnitPrice, TotalAmount
- Remove: CustomerName, CustomerEmail, CustomerCity, ProductName, ProductCategory, ProductBrand

**Customers (dimension):**
- Keep: CustomerID, CustomerName, CustomerEmail, CustomerCity
- Remove: OrderID, OrderDate, ProductID, all product columns, all numeric columns
- Right-click CustomerID → Remove Duplicates (9,995 rows → ~150 unique customers)

**Products (dimension):**
- Keep: ProductID, ProductName, ProductCategory, ProductBrand, UnitCost
- Remove: all order columns, customer columns
- Remove Duplicates on ProductID

## Step 3: Create the Date Table with DAX

After loading to the model, create a dedicated Date table:

```dax
Date =
ADDCOLUMNS(
    CALENDAR(DATE(2014,1,1), DATE(2017,12,31)),
    "Year", YEAR([Date]),
    "Quarter", "Q" & FORMAT([Date], "Q"),
    "Month", MONTH([Date]),
    "MonthName", FORMAT([Date], "MMMM"),
    "DayOfWeek", WEEKDAY([Date]),
    "DayName", FORMAT([Date], "DDDD"),
    "IsWeekend", IF(WEEKDAY([Date]) IN {1,7}, "Yes", "No")
)
```

Mark as Date Table: Table Tools → Mark as Date Table → select "Date" column.

## Step 4: Build Relationships in Model View

```
Date[Date]         ──→  Orders[OrderDate]    (1:*)
Customers[CustomerID] ──→  Orders[CustomerID]   (1:*)
Products[ProductID]   ──→  Orders[ProductID]    (1:*)
```

Single filter direction, pointing from dimension to fact.

## Step 5: Create Measures in _Measures Table

```dax
Total Revenue    = SUM(Orders[TotalAmount])
Total Orders     = COUNTROWS(Orders)
Average Order Value = DIVIDE([Total Revenue], [Total Orders], 0)
Total Quantity   = SUM(Orders[Quantity])
Total Customers  = DISTINCTCOUNT(Orders[CustomerID])
```

## The Result

| Metric | Before | After |
|--------|--------|-------|
| File size | 2.8 MB | 0.9 MB |
| Structure | Flat table | Star schema |
| Maintenance | Update 1,000 rows per customer | Update 1 row per customer |

**68% space saved** while making the data easier to maintain.

## Related

- [[fact-table-vs-dimension-table]] — how to classify each table
- [[star-schema-vs-snowflake-schema]] — the target schema shape
- [[data-model-5-testing-checks]] — verify the model works before building visuals
