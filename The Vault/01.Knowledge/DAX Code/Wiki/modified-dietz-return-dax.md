---
created: 2026-07-29
updated: 2026-08-02
source: DAX for Humans (Greg Deckler, Packt 2025)
note_type: pattern
tags: [dax, kpi, finance, dietz, return, investment, portfolio]
---

# Modified Dietz Return in DAX

Modified Dietz measures portfolio return accounting for the timing of cash flows. More accurate than simple return when deposits/withdrawals occur mid-period.

## Purpose

Simple return = (Ending − Beginning) / Beginning. This ignores when money was added or removed. Modified Dietz weights cash flows by how long they were in the portfolio.

Formula: (B − A − F) / (A + Weighted Flows)

Where:
- A = beginning balance
- B = ending balance
- F = net cash flows (positive = inflow, negative = outflow)
- Weighted Flows = Σ(flow × (T − t) / T) — weight by fraction of period the money was invested

## Formula

```dax
Modified Dietz Return =
    VAR __A = MAXX( FILTER( 'Portfolio', [Category] = "Initial Value" ), [Value] )
    VAR __B = MAXX( FILTER( 'Portfolio', [Category] = "Ending Value" ), [Value] )
    VAR __F = SUMX( FILTER( 'Portfolio', [Category] = "Flow" ), [Value] )
    VAR __InitDate = MAXX( FILTER( 'Portfolio', [Category] = "Initial Value" ), [Date] )
    VAR __EndDate = MAXX( FILTER( 'Portfolio', [Category] = "Ending Value" ), [Date] )
    VAR __T = ( __EndDate - __InitDate ) * 1. + 1

    VAR __Table =
        ADDCOLUMNS(
            FILTER( 'Portfolio', [Category] = "Flow" ),
            "__WF",
            DIVIDE( ( __EndDate - [Date] ) * 1. + 1, __T ) * [Value]
        )
    VAR __WF = SUMX( __Table, [__WF] )

    VAR __Return = DIVIDE( __B - __A - __F, __A + __WF, 0 )

    RETURN __Return
```

## Example

| Date | Category | Value |
|------|----------|-------|
| 1/1/2024 | Initial Value | $2,000 |
| 3/31/2024 | Flow | +$1,000 |
| 10/1/2024 | Flow | −$1,600 |
| 12/31/2024 | Ending Value | $2,400 |

- A = $2,000, B = $2,400, F = −$600 (net)
- T = 366 days
- Weighted Flow = $1,000 × (276/366) + (−$1,600) × (91/366) = $554.64
- Modified Dietz = (2400 − 2000 − (−600)) / (2000 + 554.64) = $1,000 / $2,554.64 = **42.52%**

Compare to XIRR: 42.16%. Modified Dietz is close but computationally simpler (no iterative solver).

## Notes

- Format as percentage (multiply by 100 in display or use % formatting)
- MAXX + FILTER extracts single values from categories
- The weighting factor (T − t) / T is the proportion of the period remaining after the flow date

## Related

- [[irr-dax-xirr]] — XIRR for exact IRR (iterative)
- [[compound-interest-future-value-dax]] — compound growth
- [[reverse-year-to-date-dax]] — forecasting
