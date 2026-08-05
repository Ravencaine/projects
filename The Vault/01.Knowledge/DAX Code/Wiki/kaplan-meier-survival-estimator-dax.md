---
created: 2026-07-29
updated: 2026-08-02
source: DAX for Humans (Greg Deckler, Packt 2025)
note_type: pattern
tags: [dax, statistics, survival, kaplan-meier, hr, employee-tenure]
---

# Kaplan-Meier Survival Estimator in DAX

Kaplan-Meier estimates the probability of survival (retention, uptime, etc.) over time. Originally clinical; Deckler applies it to employee tenure prediction.

## Purpose

Kaplan-Meier survival function: S(t) = ∏(1 − di/ni), where di = number of failures at time ti, ni = number at risk just before ti. For employee retention: S(t) = probability an employee survives at least t days.

## Formula

```dax
KM Survival =
    VAR __Day = MAX( 'Days'[Day] )
    VAR __Employees =
        ADDCOLUMNS(
            'Employees',
            "__Days", ( [Term Date] - [Hire Date] ) * 1. + 1
        )
    VAR __KMTable =
        ADDCOLUMNS(
            ADDCOLUMNS(
                GENERATESERIES( 1, __Day ),
                "d(i)", COUNTROWS(
                    FILTER( __Employees, [__Days] = [Value] )
                ),
                "n(i)", COUNTROWS(
                    FILTER( __Employees, [__Days] > [Value] )
                )
            ),
            "1-d(i)/n(i)",
            1 - DIVIDE( [d(i)], [n(i)], 0 )
        )
    VAR __Result = PRODUCTX( __KMTable, [1-d(i)/n(i)] )
    RETURN __Result
```

## How It Works

1. **Days table**: single column of integers 1 through N (N = days from earliest hire to today), disconnected from model
2. **__Employees**: add a column computing each employee's tenure in days
3. **GENERATESERIES**: creates one row per day (1 through current day in context)
4. **d(i)**: count of employees whose tenure equals this day (failed at this exact time)
5. **n(i)**: count of employees still employed after this day (at risk before failing)
6. **1 − d(i)/n(i)**: survival probability for this day
7. **PRODUCTX**: multiplies all (1 − di/ni) values together = cumulative survival probability

## Interpretation

- S(0) = 1.0 (100% survive at day 0)
- S(t) decreases whenever an employee leaves
- Flat regions = no departures
- Steep drops = mass attrition events

## Notes

- **PRODUCTX**: the DAX "product" function — equivalent to the ∏ (product) notation in the formula
- **GENERATESERIES(1, __Day)**: creates a row for every day, which is computationally expensive for large date ranges. Alternative: use DISTINCT tenure values only.
- Applied to employee tenure, equipment failure, customer churn, subscription survival

## Related

- [[customer-churn-rate-dax]] — discrete churn rate
- [[gini-coefficient-dax]] — another statistical distribution metric
