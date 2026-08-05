---
created: 2026-07-26
updated: 2026-08-02
source: dax.pdf
note_type: pattern
tags: [dax, pattern, window-functions, orderby, partitionby, matchby]
---

# ORDERBY, PARTITIONBY, and MATCHBY

Article - 07/26/2023

These functions can **only** be used with DAX Window functions: INDEX, OFFSET, WINDOW, RANK, ROWNUMBER.

## ORDERBY

Defines the sort order for window functions. Without ORDERBY, the result of window functions is undefined.

```dax
ORDERBY(
    <expression> [, <order>] [, <expression> [, <order>]]...
)
```

- `expression`: Any DAX expression that returns a scalar value
- `order`: ASC (default) or DESC

ORDERBY automatically contains all columns from the relationship that are not specified in PARTITIONBY.

## PARTITIONBY

Divides the result into groups (partitions) before the window function is applied. Each partition is processed independently.

```dax
PARTITIONBY(
    <column> [, <column>]...
)
```

When PARTITIONBY is used, ORDERBY is optional - ORDERBY automatically orders by all columns not in PARTITIONBY.

## MATCHBY

Specifies which columns uniquely identify rows when you need explicit control over row identification. Use when the natural key is not clear from the data.

```dax
MATCHBY(
    <column> [, <column>]...
)
```

MATCHBY works alongside PARTITIONBY - both columns specified in MATCHBY and PARTITIONBY are used to uniquely identify rows.

## Complete Example: YoY Sales by Color

This example calculates Year-over-Year sales for each color:

```dax
EVALUATE
ADDCOLUMNS(
    SUMMARIZECOLUMNS(
        'Product'[Color],
        'Date'[Calendar Year],
        "CurrentYearSales", [Internet Total Sales]
    ),
    "YoYSalesForSameColor",
    VAR CurrentYear = 'Date'[Calendar Year]
    VAR CurrentColor = 'Product'[Color]
    RETURN
        CALCULATE(
            [Internet Total Sales],
            'Product'[Color] = CurrentColor,
            'Date'[Calendar Year] = CurrentYear - 1
        )
)
ORDER BY 'Product'[Color], 'Date'[Calendar Year]
```

Result:

| Color | Calendar Year | CurrentYearSales | YoYSalesForSameColor |
|-------|---------------|-----------------|----------------------|
| Black | 2017 | 393,885 | 393,885 |
| Black | 2018 | 1,818,835 | 142,495 |
| Black | 2019 | 3,981,638 | 1,665,803 |
| Black | 2020 | 2,644,054 | -1,337,584 |
| Red | 2017 | 2,961,198 | 2,961,198 |
| ... | | | |

## Using PARTITIONBY for Color Groups

Divide by Color, then order by Year within each color:

```dax
EVALUATE
ADDCOLUMNS(
    SUMMARIZECOLUMNS(
        'Product'[Color],
        'Date'[Calendar Year],
        "CurrentYearSales", [Internet Total Sales]
    ),
    "PreviousYearSalesForSameColor",
    VAR CurrentColor = 'Product'[Color]
    RETURN
        CALCULATE(
            [Internet Total Sales],
            'Product'[Color] = CurrentColor,
            REMOVEFILTERS('Date'[Calendar Year])
        )
)
PARTITIONBY('Product'[Color])
ORDERBY('Date'[Calendar Year], ASC)
```

Each color gets its own partition, and within each partition, REMOVEFILTERS gets the previous year.

## Using MATCHBY for Duplicate Keys

When rows need to be identified by multiple columns, use MATCHBY:

```dax
EVALUATE
ADDCOLUMNS(
    'Internet Sales',
    "PreviousSalesForSameProduct",
    OFFSET(
        -1,
        ORDERBY('Internet Sales'[Sales Order Number], 'Internet Sales'[Sales Order Line Number]),
        PARTITIONBY('Internet Sales'[Product Key]),
        MATCHBY('Internet Sales'[Sales Order Number], 'Internet Sales'[Sales Order Line Number])
    )
)
```

Here MATCHBY tells DAX that rows are uniquely identified by Sales Order Number + Sales Order Line Number.

## How PARTITIONBY + ORDERBY Work Together

1. PARTITIONBY divides the table into parts (e.g., one per Color)
2. ORDERBY sorts each part (e.g., by Year ascending)
3. OFFSET/RANK/etc. operates within each sorted partition

## Comparison: OFFSET vs WINDOW

- **OFFSET(n)**: Returns the value n rows away from the current row
- **WINDOW(from, to)**: Returns a range of rows relative to the current row

```dax
-- Previous row
OFFSET(-1, ORDERBY(...))

-- Moving average of 3 rows
AVERAGE(
    WINDOW(-1, 0, 1, ORDERBY(...))
)
```

## Related

- [[window]]
- [[offset]]
- [[rankx]]
- [[rownumber]]
- [[window-functions-overview]]
