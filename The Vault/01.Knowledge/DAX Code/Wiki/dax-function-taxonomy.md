---
created: 2026-08-02
updated: 2026-08-02
source: Mastering M Language and DAX Functions in Power BI A Comprehensive Guide with Real-World Use Cases.md
note_type: reference
tags: [dax, reference, function-taxonomy, aggregate, filter, time-intelligence, iterator]
---

# DAX Function Taxonomy

DAX operates in the data model after M loads data. It understands **filter context**, **relationships**, and **row context** for dynamic calculations. Functions are grouped by category.

## Function Categories

### 1. Aggregation Functions (Basic + Iterators)
Scalar totals across rows/tables.

- Basic: `SUM`, `AVERAGE`, `COUNT`, `DISTINCTCOUNT`, `MIN`, `MAX`
- Iterators: `SUMX`, `AVERAGEX`, `COUNTX` — row-by-row evaluation

### 2. Filter Functions (Most Powerful)
Modify filter context. `CALCULATE` is the primary operator.

- `CALCULATE`, `FILTER`, `ALL`, `ALLEXCEPT`, `VALUES`, `REMOVEFILTERS`

### 3. Time Intelligence Functions
Date-based comparisons. **Requires a Date table.**

- `TOTALYTD`, `SAMEPERIODLASTYEAR`, `DATEADD`, `DATESYTD`
- `PREVIOUSMONTH`, `DATESBETWEEN`

### 4. Date and Time Functions
Build and extract dates.

- `DATE`, `YEAR`, `MONTH`, `NOW`, `TODAY`, `EOMONTH`

### 5. Text Functions
String manipulation.

- `CONCATENATE`, `LEFT`, `RIGHT`, `FORMAT`, `LEN`, `TRIM`

### 6. Logical & Information Functions
Conditions and checks.

- `IF`, `SWITCH`, `AND`, `OR`
- `ISBLANK`, `ISERROR`
- `HASONEVALUE`, `ISFILTERED`

### 7. Math, Trig, Statistical
Calculations like Excel.

- `POWER`, `SQRT`, `ROUND`
- `STDEV.P`, `RANKX`, `PERCENTILEX`

### 8. Table Manipulation Functions
Create or modify tables in memory.

- `SUMMARIZE`, `ADDCOLUMNS`, `SELECTCOLUMNS`
- `UNION`, `INTERSECT`, `TOPN`

### 9. Parent/Child & Relationship Functions
Hierarchies and model navigation.

- `PATH`, `USERELATIONSHIP`, `CROSSFILTER`

### Other Categories
- **Financial**: `NPV`, `IRR`, `PMT`
- **Info/Other**: `SELECTEDVALUE`, `USERPRINCIPALNAME` (RLS)

## Best Practices

- Learn `CALCULATE` and **Table functions** first — they solve ~70% of problems
- Use `VAR` for readability and performance
- Use Performance Analyzer and DAX Studio for testing

## Related

- [[m-language-function-taxonomy]] — `reference`
- [[dax-real-world-use-cases]] — `pattern`
