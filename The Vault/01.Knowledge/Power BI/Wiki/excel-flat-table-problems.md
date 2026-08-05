---
created: 2026-08-01
updated: 2026-08-02
source: "Master Power BI Introduction to Data Modeling!.md"
note_type: atomic
tags: [power-bi, data-modeling, excel, beginner, flat-table, duplication]
---

# Excel Flat Table Problems in Power BI

The way Excel users structure data — one giant table with everything in it — breaks Power BI's relationship-based model.

## The Excel Flat Table

In Excel, one row contains everything: customer name, product name, category, sales amount, date, region. You can read left to right and see the complete picture.

This works in Excel because:
- You manage 10,000 rows
- VLOOKUP pulls data from other sheets
- Pivot tables handle aggregations
- File size is rarely a problem

## The Three Problems That Emerge in Power BI

### Problem 1: Ridiculous Duplication

If ABC Corp makes 1,000 purchases, you store "ABC Corp" and "New York" 1,000 times. Every row repeats the same customer and location information.

Across millions of rows, this text repetition makes files enormous.

### Problem 2: Update Nightmares

ABC Corp moves from New York to Boston. You need to update every row where ABC Corp appears. Miss one row, and your report shows ABC Corp in two cities simultaneously.

In a 10-million-row table, there will be misses.

### Problem 3: File Bloat

Storing text in millions of rows (customer names, product descriptions, categories) dramatically inflates the file. A 50MB source can become a 500MB Power BI file.

## The Power BI Solution: Split and Connect

Split the flat table into multiple related tables:

```
Sales Table      → just the transaction (OrderID, CustomerID, ProductID, Amount, Date)
Customers Table  → customer details stored once (CustomerID, Name, City, Segment)
Products Table   → product details stored once (ProductID, Name, Category, Brand)
```

Now:
- ABC Corp's details exist in exactly one place
- Updating address change = one row update
- File size shrinks dramatically
- Power BI relationships connect the tables automatically

The critical insight: these tables need to be **connected** so Power BI knows that CustomerID "1" in Sales refers to "ABC Corp" in Customers. Those connections are called **relationships**.

## Related

- [[relationship-types-one-to-many-many-to-many]] — how relationships connect split tables
- [[fact-table-vs-dimension-table]] — which tables hold transactions vs descriptions
- [[star-schema-vs-snowflake-schema]] — how to arrange the connected tables
