---
created: 2026-07-26
source: dax.pdf
note_type: pattern
tags: [dax, pattern, window-functions, orderby, partitionby]
---

# Window Functions: ORDERBY, PARTITIONBY, MATCHBY

ORDERBY, PARTITIONBY, and MATCHBY are companion functions used exclusively with DAX window functions (INDEX, OFFSET, WINDOW, RANK, ROWNUMBER) to define how rows are ordered and grouped.

## Purpose

Window functions operate on a set of rows relative to the current row. ORDERBY/PARTITIONBY/MATCHBY define what "relative" means: which rows form the window and how they are ordered.

## Components

- `ORDERBY` — defines sort columns and direction within each partition
- `PARTITIONBY` — divides the table into groups (partitions) so window operations run independently per group
- `MATCHBY` — explicitly identifies rows when ORDERBY/PARTITIONBY columns cannot uniquely identify rows

## Structure

```dax
WindowFunction(
    <delta_or_n>,
    <table>,
    ORDERBY([Column], ASC|DESC [, ...]),
    PARTITIONBY([Column] [, ...]),
    MATCHBY([Column] [, ...])
)
```

## Example

```dax
-- Year-over-Year sales per color using OFFSET + PARTITIONBY + ORDERBY
YoY By Color :=
ADDCOLUMNS(
    SUMMARIZECOLUMNS(
        DimProduct[Color],
        DimDate[CalendarYear],
        "Sales", SUM(FactInternetSales[SalesAmount])
    ),
    "YoY Sales",
    VAR CurrentSales = [Sales]
    VAR PrevSales = SELECTCOLUMNS(
        OFFSET(-1,
            SUMMARIZECOLUMNS(DimProduct[Color], DimDate[CalendarYear], "Sales", SUM(FactInternetSales[SalesAmount])),
            ORDERBY(DimDate[CalendarYear]),
            PARTITIONBY(DimProduct[Color])
        ),
        [Sales]
    )
    RETURN
        CurrentSales - PrevSales
)
```

### MATCHBY: When Rows Are Not Unique

```dax
-- Use MATCHBY when ORDERBY columns don't uniquely identify rows
SELECTCOLUMNS(
    OFFSET(-1,
        FactInternetSales,
        ORDERBY(FactInternetSales[SalesAmount], DESC),
        PARTITIONBY(FactInternetSales[ProductKey]),
        MATCHBY(FactInternetSales[SalesOrderNumber], FactInternetSales[SalesOrderLineNumber])
    ),
    "PrevSaleAmount",
    FactInternetSales[SalesAmount]
)
```

## How They Interact

1. `PARTITIONBY` divides the table into independent groups
2. `ORDERBY` sorts rows within each group
3. `MATCHBY` disambiguates rows when the combination of ORDERBY + PARTITIONBY columns is not unique
4. If `MATCHBY` is not specified, ORDERBY + PARTITIONBY columns are used to identify rows

If PARTITIONBY is omitted, ORDERBY automatically includes all columns from the relation not in PARTITIONBY.

## Related

- [[offset]] — function
- [[window-functions-overview]] — function
- [[window]] — function
- [[rankx]] — function
- [[rownumber]] — function
