---
created: 2026-07-29
updated: 2026-08-02
source: DAX for Humans (Greg Deckler, Packt 2025)
note_type: pattern
tags: [dax, kpi, customers, acquisition, cac, marketing, sales]
---

# Customer Acquisition Cost (CAC) in DAX

The total cost to acquire one new customer — a foundational SaaS and e-commerce metric for measuring marketing efficiency and sales productivity.

## Purpose

CAC answers: "How much do we spend to win each new customer?" Combined with LTV, it gives the LTV:CAC ratio — the single most important unit economics metric. A healthy SaaS business targets an LTV:CAC of at least 3:1 (ideally 5:1+).

## Formula

```
CAC = Total Acquisition Costs / New Customers Acquired
```

Where:
- **Acquisition Costs** = Sales costs + Marketing costs + Advertising spend + Partner/referral fees + Tools/platform costs attributable to acquisition
- **New Customers** = distinct new customers acquired in the period (NOT total transactions — one customer may buy multiple times)

## Pattern

```dax
Customer Acquisition Cost =
    VAR __AcquisitionCosts =
        SUM( 'Marketing'[CampaignCost] )
        + SUM( 'Sales'[Salaries] )
        + SUM( 'Sales'[Commission] )
        + SUM( 'Marketing'[AdSpend] )
    VAR __NewCustomers =
        DISTINCTCOUNT( 'Orders'[CustomerKey] )
        -- Filter to only customers with their FIRST purchase in this period
        -- Use MIN(OrderDate) per customer to identify new vs returning
    VAR __CAC = DIVIDE( __AcquisitionCosts, __NewCustomers, BLANK() )
    RETURN __CAC
```

## Identifying New Customers (First Purchase Date)

```dax
New Customer Flag =
    VAR __FirstPurchase = MIN( 'Orders'[OrderDate] )
    VAR __ContextDate = MAX( 'Dates'[Date] )
    RETURN
        IF( __FirstPurchase = __ContextDate, 1, 0 )
```

Or via a dedicated `IsNewCustomer` column calculated in the fact table:

```dax
IsNewCustomer =
    VAR __OrderCount =
        CALCULATE(
            COUNTROWS( 'Orders' ),
            ALLEXCEPT( 'Orders', 'Orders'[CustomerKey] )
        )
    RETURN
        IF( __OrderCount = 1, "New", "Returning" )
```

## CAC by Channel

```dax
CAC by Channel =
    VAR __Channel = SELECTEDVALUE( 'Channels'[ChannelName] )
    VAR __ChannelCosts =
        CALCULATE(
            SUM( 'Marketing'[TotalCost] ),
            'Marketing'[Channel] = __Channel
        )
    VAR __NewFromChannel =
        CALCULATE(
            DISTINCTCOUNT( 'Orders'[CustomerKey] ),
            'Marketing'[Channel] = __Channel,
            'Orders'[IsNewCustomer] = "New"
        )
    RETURN DIVIDE( __ChannelCosts, __NewFromChannel, BLANK() )
```

## Blended vs CAC Payback Period

```dax
-- Blended CAC (all customers, all channels)
Blended CAC =
    DIVIDE(
        SUM( 'Marketing'[AcquisitionCost] ),
        DISTINCTCOUNT( 'Orders'[CustomerKey] )
    )

-- CAC Payback Period (months to recover acquisition cost)
CAC Payback Months =
    VAR __CAC = [Blended CAC]
    VAR __MonthlyRevenue = [Total Revenue] / DISTINCTCOUNT( 'Dates'[Month] )
    VAR __GrossProfit = __MonthlyRevenue * [Gross Margin %]
    RETURN DIVIDE( __CAC, __GrossProfit, BLANK() )
```

## Notes

- **Use DISTINCTCOUNT** not COUNTROWS — one customer can make multiple first purchases if they have multiple accounts
- **Exclude returning customers**: only count customers whose first order falls within the period
- **Fully-loaded costs**: include salaries, tools, contractor costs, not just the obvious ad spend line
- **Cohort CAC**: divide new customers by cohort month to track whether acquisition is getting cheaper or more expensive over time
- **CAC by channel** requires a channel attribution model — use LASTNONBLANK or FIRST purchase attribution
- LTV:CAC ratio = `[Customer Lifetime Value] / [CAC]` — healthy SaaS: 3:1 minimum, 5:1+ target

## Related

- [[customer-lifetime-value-ltv-dax]] — LTV:CAC ratio partner metric
- [[customer-churn-rate-dax]] — revenue retention metric
- [[net-promoter-score-nps-dax]] — leading indicator of customer satisfaction
- [[market-basket-analysis-dax]] — cross-sell and upsell opportunities
