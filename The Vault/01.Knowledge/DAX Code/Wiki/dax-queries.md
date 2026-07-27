---
created: 2026-07-26
source: dax.pdf
note_type: reference
tags: [dax, reference, queries]
---

# DAX Queries

DAX queries are statements run in DAX query view (Power BI Desktop), DAX Studio, or SQL Server Management Studio (SSMS) to retrieve data from the model.

## Quick Reference

### Basic Query Structure

```dax
EVALUATE
<expression>

-- Optional modifiers
ORDER BY <column> [ASC|DESC]
START AT <value>
```

### DEFINE: Create Measures and Variables

```dax
DEFINE
    MEASURE 'Sales'[Total Sales] = SUM('Sales'[Amount])
    VAR MyVar = 100
EVALUATE
{ MyVar }
```

Measures defined in DEFINE exist only for the duration of the query.

### EVALUATE

EVALUATE returns a table. The most basic form:

```dax
EVALUATE
'Sales'
```

### ORDER BY

Sort results:

```dax
EVALUATE
'Product'
ORDER BY 'Product'[Color], 'Product'[Category]
```

### START AT

Define the starting row in sorted results:

```dax
EVALUATE
'Product'
ORDER BY 'Product'[Color]
START AT "Blue"
```

### SUMMARIZECOLUMNS in Queries

```dax
EVALUATE
SUMMARIZECOLUMNS(
    'Date'[Year],
    "Total Sales", SUM('Sales'[Amount])
)
```

### TOPN

```dax
EVALUATE
TOPN(10, 'Sales', [Total Sales], DESC)
```

## Tools

- **DAX query view**: fourth view in Power BI Desktop (with Copilot)
- **DAX Studio**: open-source query tool for Analysis Services and Power BI
- **SSMS**: DAX query editor for tabular and multidimensional models
- **Tabular Editor**: DAX Editor with syntax highlighting

## Notes

- DAX queries can run against Analysis Services Multidimensional models (unlike DAX calculation formulas)
- DAX queries are often simpler and more efficient than equivalent MDX queries
- Query-scoped MEASURE and COLUMN definitions are for internal use only
- Multiple EVALUATE statements can appear in one query script

## Related

- [[evaluate]] — function
- [[summarizecolumns]] — function
- [[dax-syntax]] — reference
