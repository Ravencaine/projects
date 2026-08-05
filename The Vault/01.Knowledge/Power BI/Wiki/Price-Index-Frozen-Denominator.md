---
created: 2026-07-29
updated: 2026-08-02
source: "[[Author-Isabelle-Bittar|Isabelle Bittar]]"
note_type: pattern
tags: [price-index, frozen-denominator, CALCULATE-ALL, rates, indexes]
related: [CALCULATE, ALL, CALCULATETABLE]
---

# Price Index (Frozen Denominator via CALCULATE + ALL)

Calculates a price index by dividing the current price by a frozen base-period denominator — using `CALCULATE(..., ALL(Date))` to remove the date filter while preserving all other filters.

## The Problem

When showing a price index over time, the denominator should stay fixed at the base period (e.g., January 2020), but a normal division would also apply the date filter to the denominator, making the ratio always 1.

## The Solution

```dax
Price Index =
VAR _CurrentPrice = SUM('Stock Data'[Price])
VAR _BasePrice =
    CALCULATE(
        SUM('Stock Data'[Price]),
        'Stock Data'[Date] = DATE(2020, 1, 1)
    )
VAR _BasePriceAllDates =
    CALCULATE(
        SUM('Stock Data'[Price]),
        ALL('Stock Data'[Date])  // remove only the date filter
    )
RETURN
    DIVIDE(_CurrentPrice, _BasePriceAllDates)
```

Or with a user-selected base period:

```dax
Base Period Price =
    CALCULATE(
        MIN('Stock Data'[Price]),
        TREATAS(
            { SELECTEDVALUE('Period Table'[Period]) },
            'Stock Data'[Period]
        ),
        ALL('Stock Data'[Date])
    )

Price Index =
    DIVIDE(
        [Current Price],
        [Base Period Price]
    )
```

## Navigating Rates and Indexes

When illustrating rates (e.g., vacancy rates, growth rates) that are ratios:

1. Calculate the numerator (current value) in the current filter context.
2. Calculate the denominator using `CALCULATE(..., ALL(Date))` to freeze it.
3. Use `DIVIDE` for safe division.
4. Format the result as a percentage.

## Notes

- `ALL('Date'[Date])` removes only the date filter — product, region, and category filters remain active.
- Use `ALLEXCEPT` instead of `ALL` if you need to preserve some filters on the date table while removing others.
- For multi-product indexes, include the product in the filter context but freeze the date.
- Bittar's "Navigating Challenges in Illustrating Rates and Indexes" article covers the conceptual reasoning and edge cases for this pattern.

## Related

- [[calculate]] — modify filter context to freeze the denominator
- [[all]] — remove filters on a column or table
- [[DIVIDE]] — safe division
- [[cross-fact-treatas-virtual-relationships]] — map values to a column without a relationship
