---
created: 2026-08-02
updated: 2026-08-02
source: How to Build a Clean P&L in Power BI — Select Distinct.md
note_type: function
tags: [dax, function, pl, kpi, ytd, revenue, gross-profit, operating-profit, measure]
---

# YTD KPI Measures for P&L Dashboard

Five DAX measures that power the executive sidebar KPI cards and trend chart alongside the P&L Matrix.

## Core Measures

### Total YTD Revenue
Returns year-to-date total revenue from all revenue accounts.

```dax
Total YTD Revenue = TOTALYTD(
    [Revenue Measure],
    'Transactions'[Date],
    ALL('Transactions'),
    "6/30"
)
```

### Total YTD Gross Profit
Revenue minus direct costs for the year to date.

```dax
Total YTD Gross Profit = [Total YTD Revenue] - [Total YTD Cost of Sales]
```

### YTD Operating Profit (Value)
Operating Profit (Revenue − Direct Costs − Operating Expenses) for the year to date.

```dax
YTD Operating Profit Value = [Total YTD Revenue] - [Total YTD Cost of Sales] - [Total YTD Operating Expenses]
```

### YTD Operating Profit (Percentage)
Operating Profit as a percentage of Revenue.

```dax
YTD Operating Profit % =
    DIVIDE(
        [YTD Operating Profit Value],
        [Total YTD Revenue],
        BLANK()
    )
```

### Total YTD Net Profit
Final bottom-line net profit for the year to date.

```dax
Total YTD Net Profit =
    [Total YTD Revenue]
    - [Total YTD Cost of Sales]
    - [Total YTD Operating Expenses]
    - [Other Expenses / Tax]
```

## Usage

- **KPI Cards**: Total YTD Revenue, Total YTD Gross Profit, YTD Operating Profit (Value), YTD Operating Profit (%)
- **Trend Chart**: YTD Operating Profit used as the line series alongside a Monthly Revenue column series

## Context

These measures drive [[pl-executive-sidebar]].

## Related

- [[pl-executive-sidebar]] — `pattern`
- [[executive-pl-statement-structure]] — `atomic`
- [[dynamic-pl-measure]] — `function`
