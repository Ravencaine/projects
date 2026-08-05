---
created: 2026-07-29
updated: 2026-08-02
source: DAX for Humans (Greg Deckler, Packt 2025)
note_type: pattern
tags: [dax, kpi, hr, employee, turnover, retention]
---

# Employee Turnover Rate (ETR) in DAX

ETR measures the percentage of employees who leave an organization within a defined period. High turnover = lost knowledge, reduced productivity, replacement costs.

## Purpose

ETR = (Employees leaving in period / Average employees) × 100. A critical HR metric for workforce planning. Distinguish voluntary vs involuntary turnover for actionable insights.

## Formula

```dax
ETR =
    VAR __Start = MIN( 'Dates'[Date] )
    VAR __End = MAX( 'Dates'[Date] )
    VAR __StartingEmployees =
        COUNTROWS(
            FILTER(
                ALL( 'Employees' ),
                [Hire Date] <= __Start
            )
        )
    VAR __EndingEmployees =
        COUNTROWS(
            FILTER(
                ALL( 'Employees' ),
                [Hire Date] <= __End
            )
        )
    VAR __TermedEmployees =
        COUNTROWS(
            FILTER(
                ALL( 'Employees' ),
                [Hire Date] <= __End
                && [Term Date] >= __Start
                && [Term Date] <= __End
            )
        )
    VAR __AvgEmployees = ( __StartingEmployees + __EndingEmployees ) / 2
    RETURN
        DIVIDE( __TermedEmployees, __AvgEmployees, 0 ) * 100
```

## Data Model

| Column | Description |
|--------|-------------|
| Employee | Employee name |
| Hire Date | Date of hire |
| Term Date | Date of termination (9999-12-31 = still employed) |
| Annual Salary | Salary for cost calculations |

- **Dates table**: not related to Employees (disconnected)
- **Sentinel date** 9999-12-31: used for active employees (vs blank for systems that don't track active employees)

## How It Works

1. **Starting employees**: hired before the period start date
2. **Ending employees**: hired before period end date (includes new hires)
3. **Termed employees**: hire date ≤ period end AND term date falls within period
4. **Average HC**: (starting + ending) / 2
5. **ETR**: termed / average × 100

## Related

- employee-turnover-rate-etr-dax — this pattern
- [[bradford-factor-dax]] — absenteeism weighting
- [[human-capital-value-added-hcva-dax]] — value per employee
- [[customer-churn-rate-dax]] — analogous customer retention metric
