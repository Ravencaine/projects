---
created: 2026-07-29
updated: 2026-08-02
source: DAX for Humans (Greg Deckler, Packt 2025)
note_type: pattern
tags: [dax, kpi, hr, fte, employee, profit]
---

# Human Capital Value Added (HCVA) in DAX

HCVA measures the net profit each employee contributes to the organization. More sophisticated than Revenue Per Employee because it accounts for costs.

## Purpose

HCVA = (Revenue − (Total Cost − Employment Costs)) / FTE. Employment costs are subtracted as an investment, not overhead, because they represent the human capital input being evaluated.

## Formula

```dax
HCVA =
    VAR __Revenue = 4000000
    VAR __TotalCost = 3900000
    VAR __LoadedCostFactor = 1.2    -- benefits multiplier (health, 401K, etc.)
    VAR __Start = DATE( 2024, 1, 1 )
    VAR __End = DATE( 2024, 12, 31 )
    VAR __TotalDays = ( __End - __Start ) * 1. + 1
    VAR __Table =
        ADDCOLUMNS(
            ADDCOLUMNS(
                ADDCOLUMNS(
                    ADDCOLUMNS(
                        'Employees',
                        "__Min",
                        IF( [Hire Date] < __Start, __Start, [Hire Date] ),
                        "__Max",
                        IF( [Term Date] > __End, __End, [Term Date] )
                    ),
                    "__Days", ( [__Max] - [__Min] ) + 1
                ),
                "__Percent", DIVIDE( [__Days], __TotalDays, 0 )
            ),
            "__FullyLoadedCost", [Annual Salary] * [__Percent] * __LoadedCostFactor,
            "__FTE", 1 * [__Percent]
        )
    VAR __TotalFTE = SUMX( __Table, [__FTE] )
    VAR __NetValue = __Revenue - ( __TotalCost - SUMX( __Table, [__FullyLoadedCost] ) )
    RETURN
        DIVIDE( __NetValue, __TotalFTE, 0 )
```

## Components

| Variable | Description |
|----------|-------------|
| Revenue | Total organization revenue |
| Total Cost | All operating costs |
| Loaded Cost Factor | 1.2× salary to include benefits (health, 401K, etc.) |
| __Min | Later of Hire Date or period start |
| __Max | Earlier of Term Date or period end |
| __Days | Days worked in period (pro-rated for joiners/leavers) |
| __Percent | Fraction of period the employee was active |
| __FullyLoadedCost | Salary × period fraction × loaded cost factor |
| __FTE | 1 × period fraction (fractional FTE for partial-year employees) |

## FTE vs Headcount

FTE accounts for:
- **Part-time employees**: a half-time employee = 0.5 FTE
- **Joiners**: employee hired mid-year = partial FTE
- **Leavers**: employee who left mid-year = partial FTE

Headcount counts each person as 1 regardless of tenure or hours. HCVA uses FTE because it represents the actual work capacity contributed.

## Related

- [[employee-turnover-rate-etr-dax]] — turnover
- human-capital-value-added-hcva-dax — this pattern
- [[gini-coefficient-dax]] — pay equity
