---
created: 2026-08-01
updated: 2026-08-02
source: "Master Power BI Introduction to Data Modeling (Part 2).md"
note_type: atomic
tags: [power-bi, data-modeling, beginner, testing, quality-checks]
---

# Data Model: 5 Testing Checks

Build the model, then test it before building any visuals. Five checks that catch problems early.

## Check 1: Basic Table Test

Create a table visual with ProductCategory (from Products) and [Total Revenue].

**What to verify:**
- All product categories appear
- Total at the bottom matches Excel source total
- No unexpected blanks

**If total is 10x too high:** relationship problem. Stop and fix it before continuing.

## Check 2: Slicer Test

Add a Year slicer from the Date table. Select 2017.

**What to verify:**
- Table updates to show only 2017 data
- Total decreases proportionally

**If nothing changes:** Date relationship isn't working. Check relationship direction and data type.

## Check 3: Cross-Filter Test

Add a second table visual (CustomerName + [Total Revenue]). Add a ProductCategory slicer. Select "Technology."

**What to verify:**
- Products table shows only Technology products
- Customer table shows only customers who bought Technology products
- Both totals match

**If customer table doesn't update:** filter direction is wrong on the Products relationship.

## Check 4: Blank Test

Look at all visuals. Do any show "(Blank)"?

**Common cause:** Orders table has a CustomerID or ProductID that doesn't exist in the corresponding dimension table.

**How to find it:**
1. Create table: OrderID, CustomerID (from Orders)
2. Add CustomerName (from Customers)
3. Filter to show only blanks in CustomerName
4. Identify the OrderIDs with invalid CustomerIDs

**Fix options:**
- Add the missing customer/product to the dimension table
- Fix the invalid key in the source data
- Use a measure to exclude blanks: `CALCULATE([Total Revenue], NOT(ISBLANK(Customers[CustomerName])))`

## Check 5: Measure Logic Test

```dax
Check = [Total Revenue] / [Average Order Value]
```

**What to verify:** [Check] equals [Total Orders].

If it doesn't, something is wrong with either the measures or the relationships — the ratio of revenue to average order value should equal total order count.

## Related

- [[data-model-5-common-problems-fixes]] — what to do when checks fail
- [[role-playing-date-calculated-columns]] — testing multiple date relationships
- [[ecommerce-model-step-by-step]] — the model these tests are applied to
