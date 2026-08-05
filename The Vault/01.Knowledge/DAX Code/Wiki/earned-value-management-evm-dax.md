---
created: 2026-07-29
updated: 2026-08-02
source: DAX for Humans (Greg Deckler, Packt 2025)
note_type: pattern
tags: [dax, kpi, project-management, earned-value, evm, bcwp, bcws, spi, cpi]
---

# Earned Value Management (EVM) in DAX

EVM combines scope, schedule, and cost into a unified project performance framework. Five core metrics: PV, EV, AC, SV, CV, SPI, CPI.

## Key Metrics

| Metric | Full Name | Formula | Good? |
|--------|-----------|---------|-------|
| PV / BCWS | Planned Value / Budgeted Cost of Work Scheduled | Work × Budget Rate | baseline |
| EV / BCWP | Earned Value / Budgeted Cost of Work Performed | Work × % Complete × Budget Rate | higher = ahead |
| AC | Actual Cost | sum of actual expenditures | — |
| SV | Schedule Variance | EV − PV | positive = ahead |
| CV | Cost Variance | EV − AC | positive = under budget |
| SPI | Schedule Performance Index | EV / PV | > 1 = ahead |
| CPI | Cost Performance Index | EV / AC | > 1 = under budget |

## PV (Planned Value)

```dax
PV =
    VAR __Table =
        ADDCOLUMNS(
            ADDCOLUMNS(
                'Assignments',
                "__HourlyCost", RELATED( 'Costs'[Hourly Cost] )
            ),
            "__PV", [Work] * [__HourlyCost]
        )
    VAR __Result = SUMX( __Table, [__PV] )
    RETURN __Result
```

## EV (Earned Value)

```dax
EV =
    VAR __Table =
        ADDCOLUMNS(
            ADDCOLUMNS(
                'Assignments',
                "__HourlyCost", RELATED( 'Costs'[Hourly Cost] )
            ),
            "__EV", [Work] * [Project][% Complete] * [__HourlyCost]
        )
    VAR __Result = SUMX( __Table, [__EV] )
    RETURN __Result
```

## AC (Actual Cost)

```dax
AC = SUM( 'Assignments'[Actual Cost] )
```

## Variance and Index Measures

```dax
SV = [EV] - [PV]
CV = [EV] - [AC]
SPI = DIVIDE( [EV], [PV], 1 )
CPI = DIVIDE( [EV], [AC], 1 )
```

## Data Model

- **Project table**: ID, Work, Start, Finish, %, PV, EV
- **Assignments table**: per-resource work allocations (ID, Work, Resource)
- **Costs table**: hourly cost per resource (Resource, Hourly Cost)
- Relationships: Project → Assignments (ID), Costs → Assignments (Resource, bi-directional)

## Notes

- Budget includes salaries/wages AND physical materials
- EV uses [% Complete] from Project table, multiplied by PV = BCWP
- SPI < 1 = project is behind schedule; CPI < 1 = project is over budget
- Combined: SPI × CPI gives an overall project health score

## Related

- [[project-burndown-chart-dax]] — burndown charts
- [[modified-dietz-return-dax]] — investment return
