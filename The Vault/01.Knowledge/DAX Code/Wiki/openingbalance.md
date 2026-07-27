---
created: 2026-07-26
source: dax.pdf
note_type: function
tags: [dax, function, time-intelligence]
---

# OPENINGBALANCEWEEK/MONTH/QUARTER/YEAR

Evaluate a measure at the first date of the period (opening balance) — complementary to CLOSINGBALANCE.

## Signatures

```dax
OPENINGBALANCEWEEK(<expression>, <calendar>[, <filter>])
OPENINGBALANCEMONTH(<expression>, <dates or calendar>[, <filter>])
OPENINGBALANCEQUARTER(<expression>, <dates or calendar>[, <filter>])
OPENINGBALANCEYEAR(<expression>, <dates or calendar>[, <filter>][, <year_end_date>])
```

## Examples

```dax
-- Opening inventory at month start
Month Start Inventory = OPENINGBALANCEMONTH(
    SUMX(ProductInventory, ProductInventory[UnitCost] * ProductInventory[UnitsBalance]),
    'Date'[Date]
)

-- Opening balance at year start (fiscal June 30)
Opening FY Balance = OPENINGBALANCEYEAR([Balance], 'Date'[Date],, "06/30")
```

## Notes

- Evaluates at the **first date** of the period in the current context
- `year_end_date` defaults to December 31
- Complement of CLOSINGBALANCE — use both to capture the "from/to" range of a period
- Discouraged in visual calculations
- Week variants require a calendar (ISO week date tables)
- Not supported in DirectQuery mode for calculated columns or RLS rules
- Related: [[closingbalance]]

## Related

- [[closingbalance]]
