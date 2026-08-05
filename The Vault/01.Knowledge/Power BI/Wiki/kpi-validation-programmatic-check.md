---
created: 2026-08-02
updated: 2026-08-02
source: Power BI Dashboard Design Principles Used by Top Companies.md
note_type: pattern
tags: [power-bi, pattern, kpi, validation, pandas, data-quality, trust, accuracy]
---

# KPI Validation — Programmatic Cross-Check

Every headline KPI on a dashboard must be cross-checked programmatically against the raw dataset before the dashboard goes in front of a stakeholder. This is the step most commonly skipped under deadline pressure — and the one that matters most.

## The Risk

A single bad number erodes confidence in every other number on the page, even the correct ones. One real case: a mislabeled default/approval flag inverted a headline default-rate metric, showing ~1% when the true figure was 99.6% — a hundred-fold error caught only because of a programmatic validation check.

## Validation Pattern (Python/pandas)

```python
import pandas as pd

raw = pd.read_csv("loans_raw.csv")

dashboard_default_rate = 0.01  # value shown in Power BI
actual_default_rate = (raw["status"] == "default").mean()

print(f"Dashboard shows: {dashboard_default_rate:.2%}")
print(f"Source data shows: {actual_default_rate:.2%}")

# Assert within tolerance
assert abs(dashboard_default_rate - actual_default_rate) < 0.001, "KPI mismatch detected"
```

## What to Validate

| KPI Type | Validation Check |
|---|---|
| **Rate metrics** (default rate, churn %) | Recalculate from raw numerators and denominators |
| **Count metrics** | Sum raw rows and compare to measure output |
| **Period comparisons** | Verify date filter produces the expected row subset |
| **Ratio metrics** | Cross-check component metrics independently |

## When to Run Validation

- **Before first stakeholder demo:** mandatory
- **After any data source change:** schema or logic changes can break measures
- **On a schedule:** automated CI check against new data loads
- **After measure edits:** validate before publishing changes

## The Principle

A dashboard is only as trustworthy as its worst unvalidated KPI. Programmatic validation is the only reliable way to catch inverted flags, double-counted rows, or date filter misconfigurations before they reach decision-makers.

## Related

- [[dashboard-design-principles-framework]] — `pattern`
- [[progressive-disclosure-pattern]] — `pattern`
- [[slicer-discipline-filter-intent]] — `pattern`
