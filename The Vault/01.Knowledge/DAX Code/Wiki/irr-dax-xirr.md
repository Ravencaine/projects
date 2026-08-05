---
created: 2026-07-29
updated: 2026-08-02
source: DAX for Humans (Greg Deckler, Packt 2025)
note_type: pattern
tags: [dax, finance, irr, xirr, return, investment]
---

# Internal Rate of Return in DAX

Calculating IRR (for regular intervals) and XIRR (for irregular cash flow dates) in DAX.

## IRR (Regular Intervals)

```dax
IRR =
    VAR __CashFlows = VALUES( 'CashFlows'[Amount] )
    RETURN IR( __CashFlows )
```

DAX has a native IRR function for cash flows at regular intervals (monthly, quarterly, annually).

## XIRR (Irregular Intervals)

```dax
XIRR =
    VAR __CashFlowsWithDates =
        SELECTCOLUMNS(
            'CashFlows',
            "Date", 'CashFlows'[Date],
            "Amount", 'CashFlows'[Amount]
        )
    RETURN XIRR( __CashFlowsWithDates, [Amount], [Date] )
```

XIRR requires a table with Date and Amount columns. The dates need not be regular intervals.

## Deckler's Example (Investment Portfolio)

```dax
Investment IRR =
    VAR __Table = DATATABLE(
        "Date", DATETIME, "Value", INTEGER,
        {
            { "1/1/2024", -2000 },
            { "3/31/2024", -1000 },
            { "6/30/2024", 1500 },
            { "9/30/2024", 2500 },
            { "12/31/2024", 3000 }
        }
    )
    RETURN XIRR( __Table, [Value], [Date] )
```

## Related

- [[modified-dietz-return-dax]] — another return metric
- [[compound-interest-future-value-dax]] — compound growth
- [[reverse-year-to-date-dax]] — revenue forecasting
