---
created: 2026-07-29
updated: 2026-08-02
source: DAX for Humans (Greg Deckler, Packt 2025)
note_type: pattern
tags: [dax, kpi, customers, churn, retention]
---

# Customer Churn Rate in DAX

Churn rate measures what percentage of customers leave within a given time period. Essential for subscription businesses and closely tied to customer lifetime value (LTV).

## Purpose

Churn rate = customers who left / starting customers × 100. A rising churn rate signals product or service problems. A falling churn rate indicates improved customer retention. Always calculated for a defined period (monthly, quarterly, annually).

## Formula

```dax
Churn Rate =
    VAR __MinDate = MIN( 'Dates'[Date] )
    VAR __PMStart = EOMONTH( __MinDate, -2 ) + 1
    VAR __PMEnd = EOMONTH( __MinDate, -1 )
    VAR __StartDate = EOMONTH( __MinDate, -1 ) + 1
    VAR __EndDate = __MinDate

    -- Customers active in previous period
    VAR __PrevPeriodCustomers =
        FILTER(
            ALL( 'Dates' ),
            'Dates'[Date] >= __PMStart && 'Dates'[Date] <= __PMEnd
        )
    VAR __PrevCustomers =
        SUMMARIZECOLUMNS(
            'Churn'[Customer],
            "MaxDate", MAXX( __PrevPeriodCustomers, 'Dates'[Date] )
        )

    -- Customers active in current period
    VAR __CurrPeriodCustomers =
        FILTER(
            ALL( 'Dates' ),
            'Dates'[Date] >= __StartDate && 'Dates'[Date] <= __EndDate
        )
    VAR __CurrCustomers =
        SUMMARIZECOLUMNS(
            'Churn'[Customer],
            "MaxDate", MAXX( __CurrPeriodCustomers, 'Dates'[Date] )
        )

    -- Lost: active previous period but not current
    VAR __Lost = COUNTROWS(
        EXCEPT(
            FILTER( __PrevCustomers, [MaxDate] >= __PMStart ),
            FILTER( __CurrCustomers, [MaxDate] >= __StartDate )
        )
    )

    -- Starting customers (previous period total)
    VAR __Starting = COUNTROWS( __PrevCustomers )

    RETURN
        DIVIDE( __Lost, __Starting, 0 )
```

## Data Model

Requires:
- **Churn table**: one row per Customer per Date (sparse matrix of activity)
- **Dates table**: connected to Churn table via Date column

## How It Works

1. Identify all customers active in the previous period (MaxDate within previous month boundaries)
2. Identify all customers active in the current period
3. EXCEPT finds customers active before but not now = lost customers
4. Divide lost by starting = churn rate

## Example

| Month | Customers | Lost | Churn Rate |
|-------|-----------|------|------------|
| Jan 2025 | 1–9 + 10 | — | — |
| Feb 2025 | 1–9 + 11 | Customer 10 | 10% |
| Mar 2025 | 11–13 | 7, 8, 9 | 33% |

## Related

- [[customer-lifetime-value-ltv-dax]] — LTV uses churn as an input
- [[net-promoter-score-nps-dax]] — customer satisfaction metric
- [[employee-turnover-rate-etr-dax]] — analogous HR metric (turnover)
