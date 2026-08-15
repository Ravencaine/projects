---

created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
tags: [power-bi, pattern, project, cost-performance, cpi]
note_type: pattern

---

# Cost Performance Index (CPI) in DAX

Measuring cost efficiency by comparing earned value to actual cost.

## Formula

```
CPI = Earned Value (EV) / Actual Cost (AC)
```

## DAX Pattern

```dax
Cost Performance Index :=
VAR __EV = [Earned Value]
VAR __AC = [Actual Cost]
RETURN
DIVIDE( __EV, __AC )
```

## Interpretation

| CPI | Status |
|-----|--------|
| > 1.0 | Under budget (good) |
| = 1.0 | On budget |
| 0.8-1.0 | Slightly over budget |
| < 0.8 | Significantly over budget |

## To-Complete CPI (TCPI)

The CPI needed to complete the project on budget:

```dax
TCPI :=
DIVIDE(
    [Budget at Completion] - [EV],
    [Budget at Completion] - [AC]
)
```

## Notes

- CPI is the primary indicator of cost health
- TCPI > current CPI means the project needs to improve cost performance to finish on budget

## Related

- [[earned-value-management-evm-dax]]
- [[schedule-variance-and-spi-in-dax]]
- [[project-roi-and-payback-period-in-dax]]
