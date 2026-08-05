---
created: 2026-08-01
updated: 2026-08-02
source: "Master Power BI Transforming Data with Power Query Editor.md"
note_type: atomic
tags: [power-bi, power-query, beginner, unpivot, cleaning, data-types, merge, append]
---

# Power Query: 6 Transformation Categories

Six major transformation types cover almost every data cleaning scenario.

## 1. Structure Transformation

Reshaping data that isn't in analysis-friendly form.

**Example:** Monthly sales with each month as a separate column:
```
Product    Jan-2024    Feb-2024    Mar-2024
Laptop     $1,200      $1,500      $1,100
Phone      $800         $900        $750
```

**Solution:** Select month columns → Transform → Unpivot Columns
```
Product    Month       Sales
Laptop     Jan-2024    $1,200
Laptop     Feb-2024    $1,500
Phone      Jan-2024    $800
```

**Other structure transforms:** Split Column, Transpose, Reverse Rows, Group By.

## 2. Data Cleaning 🧹

Fixing dirty, inconsistent, or malformed data.

**Examples:**
- Trim whitespace: Transform → Format → Trim
- Standardise case: Transform → Format → Capitalize Each Word
- Replace values: Transform → Replace Values (find "N/A", replace with null)
- Remove duplicates: Home → Remove Rows → Remove Duplicates

**Before → After:**
```
"john SMITH"  →  "John Smith"
"$1,200.50"   →  1200.50  (after type change)
"N/A"         →  (blank)
```

## 3. Data Type Correction

Numbers stored as text, dates in wrong format, percentages as strings.

**Solution:** Click the data type icon (ABC / 123 / calendar icon) next to the column header → Select correct type.

Common corrections:
- Text → Number (for arithmetic)
- General → Date / DateTime / Time
- Text → Percentage
- Whole Number vs Decimal Number

**Warning:** Type changes fail if the column contains non-conforming values. Fix those first with Replace Values or Clean.

## 4. Combining Data

Information spread across multiple files or tables.

**Append Queries (stack rows):** Combine tables with the same columns into one:
- Home → Append Queries → Append Queries as New
- Example: Regoin1_Sales.xlsx + Regoin2_Sales.xlsx + Regoin3_Sales.xlsx → Combined_Sales

**Merge Queries (join columns):** Combine related tables on a key column:
- Home → Merge Queries → Merge Queries as New
- Similar to VLOOKUP but with a GUI and full control over join type (inner, left outer, full outer, anti)

## 5. Adding Calculated Information

Create new columns derived from existing data.

**Custom Column:** Add Column → Custom Column
```m
// Simple formula:
[Quantity] * [UnitPrice]

// Conditional:
if [Amount] > 1000 then "High Value" else "Standard"
```

**Standard transformations:** Add Column → Standard / Scientific / Trigonometry / Round — no formula needed.

## 6. Filtering and Grouping

Reduce data volume or create summaries.

**Filter Rows:** Click the dropdown arrow on a column → uncheck values to exclude. Or use Date Filters for relative date ranges (Last N months, etc.).

**Group By:** Transform → Group By
- Select columns to group by
- Choose aggregation: Sum, Average, Count Rows, Count Distinct, Min, Max
- Creates a summarised table

## Related

- [[power-query-workflow-process]] — the recommended order for applying these transformations
- [[power-query-5-core-components]] — which ribbon tabs contain each transformation
