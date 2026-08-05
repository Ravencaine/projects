---
created: 2026-07-26
updated: 2026-08-02
source: dax.pdf
note_type: function
tags: [dax, function, aggregation]
---

# COUNT, COUNTA, COUNTAX, COUNTBLANK, COUNTX

Count rows or values — choose the right function for the data type.

## COUNT

```dax
COUNT(<column>)
```

Counts rows with non-blank **numbers, dates, or strings**. Ignores BLANK and TRUE/FALSE.

## COUNTA

```dax
COUNTA(<column>)
```

Same as COUNT but **also counts TRUE/FALSE values** (TRUE = 1, FALSE = 0).

## COUNTAX

```dax
COUNTAX(<table>, <expression>)
```

Iterator version of COUNTA — evaluates an expression per row and counts non-blank results. Supports TRUE/FALSE.

## COUNTBLANK

```dax
COUNTBLANK(<column>)
```

Counts BLANK cells. Zero (0) is **not** a blank — it is a numeric value.

> COUNTBLANK returns BLANK when no rows exist; returns 0 when rows exist but no blanks are found.

## COUNTX

```dax
COUNTX(<table>, <expression>)
```

Iterator — counts rows where `expression` returns a non-blank **number, date, or string**. Use COUNTAX for logical values.

## DISTINCTCOUNTNOBLANK

```dax
DISTINCTCOUNTNOBLANK(<column>)
```

Counts distinct values **excluding BLANK**. Unlike DISTINCTCOUNT which includes BLANK in the count.

## Examples

```dax
-- Count rows with values
Rows With Data = COUNT('Sales'[Amount])

-- Count rows including TRUE/FALSE
Active Rows = COUNTA('Status'[IsActive])

-- Count non-blank expression results
Rows With Margin = COUNTX('Sales', [Revenue] - [Cost])

-- Count blank cells
Missing Emails = COUNTBLANK('Customer'[Email])

-- Distinct non-blank customers
Active Customers = DISTINCTCOUNTNOBLANK('Sales'[CustomerKey])
```

## Notes

- COUNTBLANK distinguishes between "no rows to check" (returns BLANK) and "rows exist but no blanks" (returns 0)
- COUNT ignores TRUE/FALSE; use COUNTA for boolean columns
- Not supported in DirectQuery mode for calculated columns or RLS rules (most variants)
- Related: [[use-countrows-instead-of-count]]

## Related

- [[use-countrows-instead-of-count]]
- [[countrows]]
- [[distinctcount]]
