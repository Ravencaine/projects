---

created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
tags: [dax, pattern, measure, total, aggregation, grand-total]
note_type: pattern

---

# The Measure Totals Problem in DAX

When a measure returns correct values per row but incorrect values at the total level.

## Why It Happens

Most measures use iterators that evaluate row-by-row. At the grand total, there is no single row — DAX sums the unfiltered table, which is different from summing the individual row results.

## Example

```dax
-- Row-level: correct
Margin % := DIVIDE( [Profit], [Revenue] )

-- Grand total: sums individual margins (wrong)
-- Should be: DIVIDE( SUM(Profit), SUM(Revenue) )
```

## Solution: HASONEVALUE Guard

```dax
Margin % Correct :=
VAR __TotalProfit = SUM( 'Sales'[Profit] )
VAR __TotalRevenue = SUM( 'Sales'[Revenue] )
RETURN
IF(
    HASONEVALUE( 'Product'[Product] ),
    DIVIDE( [Profit], [Revenue] ),
    DIVIDE( __TotalProfit, __TotalRevenue )
)
```

## Notes

- Always check total-level values — don't assume the visual total is correct
- The fix depends on the specific measure logic

## Related

- [[no-calculate-dax-pattern]]
- [[grouping-rows-in-dax]]
