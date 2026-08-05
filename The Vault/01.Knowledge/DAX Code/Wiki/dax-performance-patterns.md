---
created: 2026-07-26
updated: 2026-08-02
source: dax.pdf
note_type: pattern
tags: [dax, performance, best-practices, optimization]
---

# DAX Performance Best Practices

## Measure vs Calculated Column

- Use **measures** for aggregations that respond to filters
- Use **calculated columns** for row-by-row operations that don't need to respond to filters
- Expensive row-by-row calculations → calculated column

## Filter Arguments in CALCULATE

Prefer **Boolean expressions** over FILTER() as filter arguments:

```dax
-- Faster
CALCULATE([Sales], 'Product'[Color] = "Red")

-- Slower
CALCULATE([Sales], FILTER('Product', 'Product'[Color] = "Red"))
```

Use FILTER() when iterating (inside SUMX, MAXX, etc.).

## Column Filtering vs Table Filtering

Filter the **smallest table** possible:

```dax
-- Prefer: Filter dimension table
CALCULATE([Sales], 'Product'[Color] = "Red")

-- Avoid: Filter large fact table
CALCULATE([Sales], FILTER('Sales', RELATED('Product'[Color]) = "Red"))
```

## REMOVEFILTERS vs ALL

Both remove filters, but:

- **REMOVEFILTERS**: Only removes — cleaner intent
- **ALL**: Returns the unfiltered values (useful when you need the values)
- Use **REMOVEFILTERS** when you only need to clear filters
- Use **ALL** when you also need the unfiltered column/table

## Variables and Performance

Variables can improve performance by:
- Avoiding repeated expression evaluation
- Making the query plan clearer to the engine

```dax
-- Repeated expression: bad
[Total] / [Total All Time]

-- With variable: good
VAR TotalAll = [Total All Time]
RETURN DIVIDE([Total], TotalAll)
```

## SUMX vs CALCULATE

```dax
-- Preferred for simple column sums
[Sales] := SUM('Sales'[Amount])

-- SUMX needed for row-by-row expressions
Total Cost = SUMX('Sales', 'Sales'[Qty] * 'Sales'[UnitCost])
```

## DIVIDE vs Division Operator

Use DIVIDE for safe division — it handles division by zero:

```dax
-- Safe: returns BLANK on divide by zero
Ratio = DIVIDE([Numerator], [Denominator])

-- Risky: returns error on divide by zero
Ratio = [Numerator] / [Denominator]
```

## Avoid Repeated Function Calls in Iterators

```dax
-- Bad: RELATED called for every row
SUMX('Sales', RELATED('Product'[Cost]) * 'Sales'[Qty])

-- Better: depends on the model, but RELATED is evaluated once per row either way
-- The key is to filter first, then aggregate
```

## Use DATESYTD vs Manual Rolling Sum

```dax
-- Built-in: DATESYTD
YTD Sales = CALCULATE([Sales], DATESYTD('Date'[Date]))

-- Manual equivalent (slower)
YTD Sales Manual =
CALCULATE(
    [Sales],
    FILTER(
        ALL('Date'),
        'Date'[Date] <= MAX('Date'[Date])
        && YEAR('Date'[Date]) = YEAR(MAX('Date'[Date]))
    )
)
```

## Related

- [[calculate]]
- [[sumx]]
- [[avoid-using-filter-as-filter-argument]]
