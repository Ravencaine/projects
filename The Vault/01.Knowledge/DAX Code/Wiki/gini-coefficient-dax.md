---
created: 2026-07-29
updated: 2026-08-02
source: DAX for Humans (Greg Deckler, Packt 2025)
note_type: pattern
tags: [dax, statistics, gini, inequality, salary, hr, finance]
---

# Gini Coefficient in DAX

The Gini coefficient measures income or wealth inequality within a distribution (0 = perfect equality, 1 = maximum inequality). Most used for nations but applicable to organizational pay equity.

## Purpose

Gini = Area A / (Area A + Area B). Graphically: area between the 45° line of perfect equality and the Lorenz curve, divided by the total area below the equality line.

Formula: Gini = (2 × sum of ranked differences) / (n × mean)

## Visual

```
Income %
100% |         ___---- Lorenz Curve
     |      __--
     |    _-  (B)
  0% |___/_______________
     0%         Population %
       (A) = inequality gap
```

## DAX Implementation

### Perfect Equality Line

```dax
Perfect Equality = MAX( 'Population'[Value] )
```

### Lorenz Curve

```dax
Lorenz Curve =
    VAR __CurrentPercent = MAX( 'Population'[Value] )
    VAR __AllEmployees = COUNTROWS( DISTINCT( ALL( 'Employees'[Employee] ) ) )
    VAR __Table =
        ADDCOLUMNS(
            'Employees',
            "__Percent",
            VAR __Salary = [Annual Salary]
            VAR __Count =
                COUNTROWS(
                    FILTER( ALL( 'Employees' ), [Annual Salary] <= __Salary )
                )
            VAR __Result = DIVIDE( __Count, __AllEmployees )
            RETURN __Result
        )
    VAR __AllIncome = SUMX( 'Employees', [Annual Salary] )
    VAR __Employees =
        SELECTCOLUMNS(
            FILTER( __Table, [__Percent] <= __CurrentPercent ),
            "__Employee", [Employee]
        )
    VAR __Income = SUMX(
        FILTER( __Table, [Employee] IN __Employees ),
        [Annual Salary]
    )
    VAR __Result = DIVIDE( __Income, __AllIncome ) + 0
    RETURN __Result
```

### Gini Coefficient (as visual difference)

```dax
Gini =
    VAR __AreaA = SUMX(
        'Population',
        ( MAX( 'Population'[Value] ) - [Lorenz Curve] )
        / COUNTROWS( 'Population' )
    )
    VAR __AreaB = SUMX(
        'Population',
        ( [Lorenz Curve] + MAX( 'Population'[Value] ) / 2 )
        / COUNTROWS( 'Population' )
    )
    RETURN DIVIDE( __AreaA, __AreaA + __AreaB )
```

## How It Works

1. **Population table**: GENERATESERIES(0, 1.01, 0.01) — 101 rows from 0% to 100% population
2. **Lorenz curve**: for each population percentile, compute % of total income held by that % of population
3. **Area A**: sum of gaps between equality line and Lorenz curve
4. **Area B**: sum under the Lorenz curve
5. **Gini**: Area A / (Area A + Area B)

## Notes

- **SELECTCOLUMNS + FILTER + IN**: creates a lookup for income at each population percentile
- Result visualised as a Line chart: Population% on X-axis, Perfect Equality + Lorenz Curve on Y-axis
- Lower Gini = more equal pay distribution
- Industry benchmarks: Gini < 0.3 = relatively equal, Gini > 0.4 = high inequality

## Related

- [[human-capital-value-added-hcva-dax]] — employee value
- [[bradford-factor-dax]] — HR metric
- [[kaplan-meier-survival-estimator-dax]] — another statistical measure
