---
created: 2026-07-29
updated: 2026-08-02
source: DAX for Humans (Greg Deckler, Packt 2025)
note_type: pattern
tags: [dax, finance, compound-interest, future-value, investment]
---

# Compound Interest and Future Value in DAX

Financial calculations for compound interest and future value.

## Future Value Formula

```
FV = PV × (1 + r)^n
```

Where:
- PV = present value (initial investment)
- r = periodic interest rate
- n = number of periods

## Future Value in DAX

```dax
Future Value =
    VAR __PV = [PresentValue]
    VAR __Rate = [AnnualRate] / 12   // monthly rate
    VAR __Periods = [Years] * 12      // total months
    VAR __FV = __PV * POWER( 1 + __Rate, __Periods )
    RETURN __FV
```

## Compound Interest (Total Interest Earned)

```dax
Total Interest =
    VAR __FV = [Future Value]
    VAR __PV = [PresentValue]
    RETURN __FV - __PV
```

## Effective Annual Rate

When interest is compounded more frequently than annually:

```dax
Effective Annual Rate =
    VAR __NominalRate = [AnnualRate]
    VAR __CompoundingPeriods = [PeriodsPerYear]
    VAR __EAR = POWER( 1 + __NominalRate / __CompoundingPeriods, __CompoundingPeriods ) - 1
    RETURN __EAR
```

## Related

- [[modified-dietz-return-dax]] — investment return calculation
- [[irr-dax-xirr]] — internal rate of return
- [[reverse-year-to-date-dax]] — revenue forecasting
