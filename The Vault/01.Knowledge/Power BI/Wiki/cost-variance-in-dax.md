---

created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
tags: ["power-bi", "pattern", "project", "cost-variance", "budget", "variance"]
note_type: pattern

---

# Cost Variance in DAX

Measuring the difference between budgeted and actual costs.

## Formula

```
Cost Variance (CV) = Earned Value (EV) - Actual Cost (AC)
CV% = (CV / Budget) * 100
```

## DAX Pattern

```dax
Cost Variance :=
[EV] - [AC]

Cost Variance % :=
DIVIDE( [Cost Variance], [Budget] )
```

## Notes

- Positive CV = under budget; negative CV = over budget
- Use at WBS level for detailed project reporting

## Related

- [[earned-value-management-evm-dax]]
- [[cost-performance-index-cpi-in-dax]]
