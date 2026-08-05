---
created: 2026-07-30
updated: 2026-08-02
source: "dax4humans_ch7_new_customers.txt"
note_type: pattern
tags: [customer-analytics, new-customer, churn, acquisition]
---

# New, Lost, and Returning Customers in DAX

Identifies customers who are newly acquired, lost (churned), or returning in the current period, based on their presence in prior periods.

## Purpose

Track customer lifecycle across time periods: which customers appeared for the first time (new), which disappeared from the previous period (lost), and which reappeared after an absence (returning). Essential for growth/decline analysis and marketing effectiveness.

## Components

- `DISTINCT` — snapshot of customer IDs in current and prior periods
- `FILTER` + `ALL` — override filter context to scan all history
- `EXCEPT` — set difference to find customers in one period but not another
- `INTERSECT` — set intersection for returning customers
- `COUNTROWS` + `+ 0` — force numeric return instead of BLANK

## Structure

```dax
New Customers =
  VAR __Date      = MIN( 'Dates'[Date] )
  VAR __Current   = DISTINCT( 'Customers'[ID] )
  VAR __Previous  =
    DISTINCT(
      SELECTCOLUMNS(
        FILTER( ALL( 'Customers' ), [Date] < __Date ),
        "ID", [ID]
      )
    )
  VAR __Table     = EXCEPT( __Current, __Previous )
  VAR __Result    = COUNTROWS( __Table ) + 0
  RETURN __Result
```

```dax
Lost Customers =
  VAR __Date      = MIN( 'Dates'[Date] )
  VAR __Current   = DISTINCT( 'Customers'[ID] )
  VAR __Previous  =
    DISTINCT(
      SELECTCOLUMNS(
        FILTER( ALL( 'Customers' ), [Date] > EOMONTH( __Date, -2 ) && [Date] < __Date ),
        "ID", [ID]
      )
    )
  VAR __Table     = EXCEPT( __Previous, __Current )
  VAR __Result    = COUNTROWS( __Table ) + 0
  RETURN __Result
```

```dax
Returning Customers =
  VAR __Date           = MIN( 'Dates'[Date] )
  VAR __Current        = DISTINCT( 'Customers'[ID] )
  VAR __PreviousMonth  =
    DISTINCT(
      SELECTCOLUMNS(
        FILTER( ALL( 'Customers' ), [Date] > EOMONTH( __Date, -2 ) && [Date] < __Date ),
        "ID", [ID]
      )
    )
  VAR __Previous =
    DISTINCT(
      SELECTCOLUMNS(
        FILTER( ALL( 'Customers' ), [Date] < __Date ),
        "ID", [ID]
      )
    )
  VAR __Table =
    EXCEPT(
      INTERSECT( __Current, __Previous ),
      __PreviousMonth
    )
  VAR __Result = COUNTROWS( __Table ) + 0
  RETURN __Result
```

## Example

| Period | Customers | New | Lost | Returning |
|--------|-----------|-----|------|-----------|
| Jan 2025 | 1..24 | 24 | 0 | 0 |
| Feb 2025 | 1..25 | 1 | 0 | 0 |
| Mar 2025 | 1, 26..30 | 0 | 1 (lost 25) | 0 |

## Variations

**Return a customer list instead of a count:**
```dax
VAR __Result = CONCATENATEX( __Table, [ID], ", " )
```

**Sum revenue from new customers:**
```dax
VAR __Result = SUMX( __Table, [Revenue] )
```

**Different lookback period:** Change `EOMONTH( __Date, -2 )` to adjust how many prior months count as "previous" for the Lost and Returning definitions.

## Notes

- `+ 0` forces a numeric return — without it, `COUNTROWS` returns BLANK when the table is empty, which suppresses the visual. Adding 0 returns 0 instead.
- A new customer is defined as a customer ID that has never appeared in any prior period.
- Returning customers must have appeared before the immediately previous period (not just the last period) to count as truly returning vs. continuing.
- EXCEPT order matters: `EXCEPT(A, B)` = items in A not in B.

## Related

- [[customer-churn-rate-dax]] — related churn metric
- [[customer-lifetime-value-ltv-dax]] — customer value over time
- [[customer-acquisition-cost-cac-dax]] — acquisition cost tracking
