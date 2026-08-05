---
title: "Power BI RELATED and RELATEDTABLE: Join & Aggregate DAX"
source: "https://databear.com/power-bi-related-relatedtable-dax/"
author:
  - "[[Boniface Muchendu]]"
published: 2026-04-22
created: 2026-08-04
description: "Master Power BI RELATED and RELATEDTABLE DAX. Learn to pull values or aggregate data (with SUMX) across tables for accurate results."
Processed: "Unprocessed"
---
If you’ve ever needed to create a calculated column in Power BI using data that lives on a **different table**, you know that VLOOKUP won’t work. The solution lies in mastering the essential DAX functions: **Power BI RELATED and RELATEDTABLE**.

These two powerful tools allow you to seamlessly work across multiple tables in your data model. Whether you need to pull a single value or aggregate data based on relationships, understanding **RELATED** and **RELATEDTABLE** is the key to building smarter, more dynamic reports.

##### Understanding the Relationship Rulebook

Before writing any DAX, you must understand the structure of your data model, specifically the **direction** of your relationships.

In Power BI, tables are usually connected by **one-to-many** (or many-to-one) relationships.

In our example model, we have two tables: **Customers** and **Orders**.

- The **Customers** table is on the **One** side ($\mathbf{1}$), as each Customer ID appears only once.
- The **Orders** table is on the **Many** side ($\mathbf{\ast}$), as a single customer can place many orders.

The direction of this relationship dictates which DAX function you must use:

| **Function** | **Direction of Data Flow** | **Primary Use Case** |
| --- | --- | --- |
| **`RELATED`** | **Many** ($\mathbf{\ast}$) $\rightarrow$ **One** ($\mathbf{1}$) | Pull a **single value** (e.g., Customer Name) into the many side. |
| **`RELATEDTABLE`** | **One** ($\mathbf{1}$) $\rightarrow$ **Many** ($\mathbf{\ast}$) | Return a **filtered table** (for aggregation) from the many side to the one side. |

##### PART 1: Using the RELATED Function

The **`RELATED`** function is used when you want to retrieve a **single value** from a related table into the current row context. This is the **many-to-one** relationship movement.

##### Scenario: Bring Customer Name into the Orders Table

The **Orders** table contains the `Customer ID`, but not the `Customer Name`. We want to see the customer’s name next to every order.

Because the **Orders** table is on the **many** side and the **Customers** table (where the Name resides) is on the **one** side, we use `RELATED`.

##### DAX Formula (New Column on the Orders Table):

Code snippet

```markdown
Customer Name = RELATED('Customers'[Customer Name])
```

The formula successfully uses the shared `Customer ID` to look up the corresponding `Customer Name` in the `Customers` table, much like a VLOOKUP, but more robust because it relies on the model’s relationships.

##### PART 2: Using the RELATEDTABLE Function

The **`RELATEDTABLE`** function works in the opposite direction. It allows you to start on the **one** side of the relationship (e.g., **Customers**) and retrieve a **table of related rows** from the **many** side (e.g., **Orders**).

Because `RELATEDTABLE` returns an entire table, it is almost always paired with an **aggregation function** (like `COUNTROWS` or the powerful **X-functions**) to summarize that related data.

##### Scenario A: Count Total Orders Per Customer

The goal is to count exactly how many orders each individual customer has placed. This calculated column is created on the **Customers** table.

##### The Wrong Way: Using Unfiltered DAX

If you try to simply use `COUNTROWS` without navigating the relationship:

Code snippet

```markdown
Order Count Bad Column = COUNTROWS(Orders)
```

This returns the **total number of rows in the entire Orders table** (e.g., 4) for every single customer—it doesn’t filter by the customer.

##### The Right Way: Using RELATEDTABLE

We use `RELATEDTABLE` to filter the **Orders** table down to *just* the orders for the current customer before counting the rows.

##### DAX Formula (New Column on the Customers Table):

Code snippet

```markdown
Order Count Good Column = COUNTROWS( RELATEDTABLE(Orders) )
```

**How it works:** For each row in the **Customers** table, `RELATEDTABLE(Orders)` returns a filtered version of the Orders table containing only the relevant orders. `COUNTROWS` then counts those specific rows.

##### PART 3: Advanced Aggregation with X-Functions

When performing calculations more complex than a simple count (like summing sales amounts that account for quantity), you must use **Iterator (X) functions** alongside `RELATEDTABLE`.

##### X-Functions vs. Non-X Functions

| **Type** | **Example** | **What It Does** |
| --- | --- | --- |
| **Non-X** | `SUM()` | Calculates the sum of a **column**. |
| **Iterator (X)** | `SUMX()` | Calculates an **expression** row-by-row over a **table**, then aggregates the results. |

##### Scenario B: Calculate Total Sales per Customer (Accounting for Quantity)

The goal is to find the true total sales for each customer by calculating `Amount * Quantity` for every order, and then summing those results.

##### DAX Formula (New Column on the Customers Table):

Code snippet

```markdown
Total Sales Good Column = 
SUMX(
    RELATEDTABLE(Orders),
    Orders[Order Amount] * Orders[Quantity]
)
```

This ensures the calculation is **iterated** and **filtered** correctly:

1. **`RELATEDTABLE(Orders)`** filters the orders to the current customer.
2. **`SUMX`** runs the expression (`Amount * Quantity`) for every order in that filtered set.
3. The final result is the accurate total sales attributable to that customer.

##### Scenario C: Calculating Average Sales Per Order

You can use the same pattern with `AVERAGEX` to find the average value of each order placed by a customer.

##### DAX Formula (New Column on the Customers Table):

Code snippet

```markdown
Average Per Order Good Column = 
AVERAGEX(
    RELATEDTABLE(Orders),
    Orders[Quantity] * Orders[Order Amount]
)
```

##### Conclusion

Mastering the **Power BI RELATED and RELATEDTABLE** DAX functions is a cornerstone of effective development.

- Use **`RELATED`** to grab an **individual value** from the ‘one’ side (e.g., Customer Region).
- Use **`RELATEDTABLE`** (often with an X-function) to **aggregate rows** from the ‘many’ side (e.g., Total Sales).

Once you master these two functions, you unlock your ability to traverse complex data models effortlessly and build robust, accurate reports in Power BI.

##### Ready to Level Up Your DAX Skills?

If you’re serious about taking your data modeling and analysis to the next level, deep-dive training is essential.

Check out this fantastic resource for in-depth, hands-on learning:

[Power BI Training from DataBear](https://databear.com/power-bi-training/)