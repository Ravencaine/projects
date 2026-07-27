---
created: 2026-07-26
source: dax.pdf
note_type: concept
tags: [dax, query, dax-queries, evaluate, definer]
---

# DAX Query Language Reference

Article - 12/13/2024

A DAX query is used to retrieve data from a data model. Every query is executed when a report visual loads.

## EVALUATE

The only required keyword — returns a table:

```dax
EVALUATE
    SUMMARIZECOLUMNS(
        'Product'[Category],
        "Total Sales", [Sales Amount]
    )
```

Multiple EVALUATE statements in one query are supported.

## ORDER BY

Sort query results:

```dax
EVALUATE
    'Sales'
ORDER BY
    'Sales'[Date] DESC,
    'Sales'[Amount] DESC
```

## START AT

Start the results at a specific value:

```dax
EVALUATE
    'Sales'
ORDER BY
    'Sales'[Region]
START AT "West"
```

START AT arguments map 1:1 to ORDER BY columns. There must be exactly as many START AT arguments as ORDER BY columns.

## TOPN vs ORDER BY

TOPN has its own sort order — ORDER BY sorts the final result after TOPN:

```dax
-- TOPN sorts first (internally), ORDER BY sorts the output
EVALUATE
    TOPN(
        100,
        'Sales',
        'Sales'[Amount], DESC
    )
ORDER BY 'Sales'[Date]
```

## DEFINE

Define entities (MEASURE, VAR, TABLE, COLUMN) that apply to all EVALUATE statements:

```dax
DEFINE
    MEASURE 'Sales'[Total Sales] = SUM('Sales'[Amount])
    MEASURE 'Sales'[Avg Order] = DIVIDE([Total Sales], DISTINCTCOUNT('Sales'[OrderID]))
    VAR MaxRegion = "West"
EVALUATE
    CALCULATETABLE(
        SUMMARIZECOLUMNS('Product'[Category], "Total", [Total Sales]),
        'Sales'[Region] = MaxRegion
    )
```

> Caution: Query-scoped TABLE and COLUMN definitions are for internal use only — do not use them in production.

## Parameterized Queries

DAX queries support parameters via XMLA:

```xml
<Execute xmlns="http://schemas.microsoft.com/analysisservices/2003/engine">
  <Parameters>
    <Parameter name="RegionName">
      <Value>West</Value>
    </Parameter>
  </Parameters>
  <Command>
    <Statement>
      EVALUATE
      FILTER('Sales', 'Sales'[Region] = @RegionName)
    </Statement>
  </Command>
</Execute>
```

Parameters are prefixed with @ in the query.

## Table Constructors

Inline tables for ad-hoc data:

```dax
-- Single column
EVALUATE {"Alpha", "Beta", "Gamma"}

-- Multiple columns
EVALUATE { {1, "One"}, {2, "Two"}, {3, "Three"} }

-- Used with DEFINE
DEFINE TABLE MyTable = DATATABLE("X", INTEGER, "Y", STRING, { {1,"A"}, {2,"B"} })
EVALUATE MyTable
```

## Multiple EVALUATE Statements

One DEFINE applies to all EVALUATE statements:

```dax
DEFINE
    MEASURE 'Sales'[Total] = SUM('Sales'[Amount])
EVALUATE
    SUMMARIZECOLUMNS('Product'[Category], "Total", [Total])
EVALUATE
    SUMMARIZECOLUMNS('Customer'[Segment], "Total", [Total])
```

## Related

- [[evaluate]]
- [[dax-queries]]
- [[dax-query-language-reference]]
