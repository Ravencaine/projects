---
created: 2026-07-29
updated: 2026-08-02
source: DAX for Humans (Greg Deckler, Packt 2025)
note_type: pattern
tags: [dax, kpi, customers, ltv, clv, cltv]
---

# Customer Lifetime Value (LTV/CLV) in DAX

LTV predicts the total revenue a customer will generate over their entire relationship with the business. Foundation for customer segmentation and acquisition cost justification.

## Purpose

LTV = average order value × purchase frequency × customer lifespan × margin. Customers with high LTV justify higher acquisition costs and marketing investment. Customers with low LTV may need different treatment or retention strategies.

## Formula

```dax
Yearly Churn Rate = 0.15   -- hardcoded assumption

LTV =
    VAR __Customers = COUNTROWS( DISTINCT( 'Lifetime Value'[Customer] ) )
    VAR __MinDate = MIN( 'Lifetime Value'[Date] )
    VAR __MaxDate = MAX( 'Lifetime Value'[Date] )
    VAR __Years =
        IF(
            ( __MaxDate - __MinDate ) >= 1,
            YEAR( __MaxDate ) - YEAR( __MinDate ) + 1
        )
    VAR __AvgPurchaseFrequency =
        DIVIDE(
            COUNTROWS( 'Lifetime Value' ),
            __Years,
            BLANK()
        )
    VAR __AvgPurchaseValue = AVERAGE( 'Lifetime Value'[Value] )
    VAR __AvgCustomerValue = __AvgPurchaseValue * __AvgPurchaseFrequency
    VAR __AvgCustomerLifespan = 1 / [Yearly Churn Rate]
    VAR __Result =
        DIVIDE(
            __AvgCustomerValue * __AvgCustomerLifespan,
            __Customers,
            BLANK()
        )
    RETURN
        __Result
```

## How It Works

1. **Customers**: distinct count of all customers in scope
2. **Years**: number of years the data spans
3. **Avg Purchase Frequency**: total transactions / years
4. **Avg Purchase Value**: average transaction value (AVERAGE, not AVERAGEX — simple column average)
5. **Avg Customer Value**: frequency × value per year
6. **Avg Customer Lifespan**: 1 / yearly churn rate (e.g., 15% churn → 6.67 year lifespan)
7. **LTV**: annual value × lifespan ÷ customer count

## Notes

- **Hardcoded churn rate**: Deckler hardcodes 15% yearly churn. A more dynamic approach would calculate actual churn from the data (see [[customer-churn-rate-dax]]).
- **Alexis Olson patron tip**: Use DISTINCTCOUNT instead of COUNTROWS(DISTINCT(...)) for cleaner code.
- **Works at aggregate and individual level**: LTV works in a Card (all customers) and can be adapted for per-customer LTV using TREATAS or similar.
- LTV × target margin = net LTV after costs

## Related

- [[customer-churn-rate-dax]] — churn rate as LTV input
- [[net-promoter-score-nps-dax]] — customer satisfaction
- [[market-basket-analysis-dax]] — purchase pattern analysis
