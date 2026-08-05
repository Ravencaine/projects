---
created: 2026-08-01
updated: 2026-08-02
source: "TREATAS in DAX - Connecting Unrelated Tables Like Magic.md"
note_type: atomic
tags: [dax, treatas, dynamic-segments, what-if, FILTER, SELECTEDVALUE, intermediate]
---

# TREATAS for Dynamic Segments and What-If Scenarios

TREATAS can create dynamic segment selectors and what-if analyses — no physical join, no data duplication.

## Dynamic Segment Selector Pattern

Build a Segment Selector table (MinSales, MaxSales, SegmentName):

```c
Selected Segment Sales =
VAR MinVal = SELECTEDVALUE(Segments[MinSales])
VAR MaxVal = SELECTEDVALUE(Segments[MaxSales])
RETURN
    CALCULATE(
        [Total Sales],
        TREATAS(
            FILTER(
                Sales,
                Sales[SalesAmount] >= MinVal &&
                Sales[SalesAmount] <= MaxVal
            ),
            Sales[SalesAmount]
        )
    )
```

User picks a segment in a slicer → measure dynamically applies a range filter.

## How It Works

1. `SELECTEDVALUE(Segments[MinSales])` → reads the slicer selection (minimum value)
2. `FILTER(Sales, condition)` → creates a table of Sales rows matching the range
3. `TREATAS(table_expression, target_column)` → treats that result as a filter on Sales[SalesAmount]
4. `CALCULATE` → re-evaluates `[Total Sales]` under the range filter

## What-If Scenario Pattern

```c
What-If Discounted Sales =
VAR DiscountPct = SELECTEDVALUE('Discount Parameter'[Discount], 0)
RETURN
    CALCULATE(
        SUMX(
            Sales,
            Sales[Amount] * (1 - DiscountPct)
        ),
        TREATAS(
            FILTER(
                ALL(Sales),
                Sales[Amount] > 1000
            ),
            Sales[Amount]
        )
    )
```

User controls the discount via a parameter table → measure responds dynamically.

## Virtual Scenario Joins

Combine with SELECTCOLUMNS and CALCULATETABLE for on-the-fly scenario joins:

```c
Scenario Comparison =
VAR ScenarioTable =
    SELECTCOLUMNS(
        { ("Scenario A", 0.10), ("Scenario B", 0.20), ("Scenario C", 0.30) },
        "Scenario", [Value1],
        "Discount", [Value2]
    )
RETURN
    SUMX(
        ScenarioTable,
        CALCULATE(
            [Total Sales] * (1 - [Discount]),
            TREATAS(ScenarioTable, Sales[Scenario])
        )
    )
```

User picks which scenario drives the calculation.

## Best Practices

- **Always wrap TREATAS in CALCULATE**: never use standalone
- **Use SELECTEDVALUE** for user-driven parameters (slicers, what-if inputs)
- **FILTER creates the intermediate table**: combine with TREATAS for range/set conditions
- **Document the virtual relationship**: teams need to understand which tables are logically joined

## Related

- [[treatas-virtual-relationships]] — core TREATAS + VALUES pattern
- [[treatas-uselationship-crossfilter]] — when TREATAS fits vs alternatives
- [[treatas-performance-pitfalls]] — performance with FILTER + TREATAS
