---
created: 2026-07-26
updated: 2026-08-02
source: dax.pdf
note_type: function
tags: [dax, function, time-intelligence]
---

# CLOSINGBALANCEWEEK/MONTH/QUARTER/YEAR

Evaluate a measure at the last date of the period — useful for stock/cumulative measures.

## Signatures

```dax
CLOSINGBALANCEWEEK(<expression>, <calendar>[, <filter>])
CLOSINGBALANCEMONTH(<expression>, <dates or calendar>[, <filter>])
CLOSINGBALANCEQUARTER(<expression>, <dates or calendar>[, <filter>])
CLOSINGBALANCEYEAR(<expression>, <dates or calendar>[, <filter>][, <year_end_date>])
```

## Examples

```dax
-- Closing inventory value at end of each month
Month End Inventory = CLOSINGBALANCEMONTH(
    SUMX(ProductInventory, ProductInventory[UnitCost] * ProductInventory[UnitsBalance]),
    'Date'[Date]
)

-- Closing balance at year end (fiscal June 30)
Year End Revenue = CLOSINGBALANCEYEAR([Revenue], 'Date'[Date],, "06/30")
```

## Notes

- Evaluates the expression at the **last date** of the period in the current context
- `year_end_date` defaults to December 31
- **Discouraged in visual calculations**: likely returns meaningless results
- Week functions require a calendar (ISO week date table)
- Not supported in DirectQuery mode for calculated columns or RLS rules
- Related: [[openingbalanceyear]]

## Related

- [[openingbalanceyear]]
