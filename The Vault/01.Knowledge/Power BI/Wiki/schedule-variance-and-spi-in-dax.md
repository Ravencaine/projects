---

created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
tags: [power-bi, pattern, project, schedule-variance, spi]
note_type: pattern

---

# Schedule Variance and SPI in DAX

Measuring how much a project is ahead or behind schedule.

## Schedule Variance (SV)

```
SV = Earned Value (EV) - Planned Value (PV)
```

- SV > 0: project is ahead of schedule
- SV < 0: project is behind schedule
- SV = 0: on schedule

```dax
Schedule Variance :=
VAR __EV = [Earned Value]
VAR __PV = [Planned Value]
RETURN
__EV - __PV
```

## Schedule Performance Index (SPI)

```
SPI = EV / PV
```

```dax
SPI :=
DIVIDE( [Earned Value], [Planned Value] )
```

## Interpretation

| SPI | Status |
|-----|--------|
| > 1.0 | Ahead of schedule |
| = 1.0 | On schedule |
| 0.9-1.0 | Slightly behind |
| < 0.9 | Significantly behind |

## Notes

- SPI of 0.9 means 90% of planned progress was achieved
- Use SPI by phase to identify which work packages are lagging

## Related

- [[earned-value-management-evm-dax]]
- [[cost-performance-index-cpi-in-dax]]
- [[burndown-chart-in-dax]]
