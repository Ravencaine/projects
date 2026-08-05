---
created: 2026-08-02
updated: 2026-08-02
source: Building an Executive Retail Sales Dashboard in Power BI.md
note_type: pattern
tags: [power-bi, pattern, kpi, card, executive-dashboard]
---

# Executive KPI Card Row

A horizontal row of single-value cards at the top of a dashboard, each displaying one critical KPI with a label, value, and optional comparison to a target or prior period.

## Purpose

Provides executives with an instant health check of business performance without requiring them to read charts or interpret data. Each card is a single measure rendered as a large number with context.

## Components

- **KPI Card visual** (or card + multi-row matrix)
- **Primary measure:** the KPI value (Total Sales, Total Profit, Total Orders, AOV)
- **Optional trend indicator:** arrow (up/down) or sparkline
- **Optional comparison:** vs. last year, vs. target, vs. prior period
- **Optional delta:** absolute or percentage change

## Structure

```
┌──────────────┐  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐
│ Total Sales  │  │ Total Profit │  │ Total Orders │  │  Avg Order   │
│  $1,234,567  │  │   $234,567   │  │    12,345    │  │    Value     │
│  ▲ 12% YoY   │  │  ▼ 3% YoY    │  │  ▲ 8% YoY    │  │   $102.40    │
└──────────────┘  └──────────────┘  └──────────────┘  └──────────────┘
```

## DAX Measures

```dax
Total Sales         := SUM ( Sales[Sales] )
Total Profit        := SUM ( Sales[Profit] )
Total Orders        := DISTINCTCOUNT ( Sales[Order ID] )
Average Order Value := DIVIDE ( [Total Sales], [Total Orders] )

-- YoY comparison (requires Calendar table):
Sales YoY Change :=
    DIVIDE (
        [Total Sales] - CALCULATE ( [Total Sales], SAMEPERIODLASTYEAR ( 'Calendar'[Date] ) ),
        CALCULATE ( [Total Sales], SAMEPERIODLASTYEAR ( 'Calendar'[Date] ) )
    )
```

## Variations

- **Multi-period KPI card**: show current value + value from same period last year
- **Target vs. actual card**: show progress bar inside the card
- **Status card**: colour-code based on threshold (green/yellow/red)

## Related

- [[retail-kpi-framework]] — `atomic`
- [[total-sales-dax-measure]] — `function`
- [[total-profit-dax-measure]] — `function`
- [[total-orders-dax-measure]] — `function`
- [[average-order-value-dax]] — `function`
