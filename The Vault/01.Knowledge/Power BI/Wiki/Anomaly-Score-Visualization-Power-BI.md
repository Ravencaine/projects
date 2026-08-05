---
created: 2026-08-05
updated: 2026-08-05
source: How to Do Anomaly Detection in Power BI (Isabelle Bittar)
note_type: atomic
tags: [anomaly-detection, visualization, conditional-formatting, power-bi, ux, dashboard]
---

# Anomaly Score Visualization in Power BI

Clear visual indicators — conditional formatting pills, key metric cards, and interactive bar charts — drive user adoption of anomaly detection dashboards. UX design is as important as the model itself.

## Definition

Using Power BI visuals (Table, Card, Bar Chart) with conditional formatting to surface `AnomalyScore = -1` rows as immediately actionable, high-visibility elements in a report.

## Key Points

- **Conditional formatting pills:** A dedicated column (or DAX measure) maps `AnomalyScore` to text labels: `"-1" → "Anomaly Detected"`, `"1" → "Normal"`. Apply conditional formatting with bold orange/yellow fill for anomalies, green for normal.
- **Key metric cards at the top:** Total Anomaly Amount, Anomaly Count, Anomaly % — give executives a quick summary without reading the table.
- **Interactive bar charts:** Breakdown by Payment Type, Vendor, Employee. Each bar is a filter target — clicking filters the transaction table below in real time.
- **Transaction table is the centerpiece:** All fields (Employee, Amount, Timestamp, Vendor, AnomalyScore) in one scrollable table with the anomaly pill as the most prominent visual signal.
- **Users won't act on what they can't quickly identify:** Isabelle's dashboard succeeds because it makes anomalies visually obvious — bold indicators, intuitive filters, and a clean hierarchy guide users to action fast.
- **Design matters more than model complexity:** Even a simple Isolation Forest becomes valuable when paired with a well-designed dashboard; a perfect model becomes useless if the UI buries the results.

## Related

- [[Isolation-Forest-How-It-Works]]
- [[Gestalt-Principles]]
- [[concise-consistent-titles]]
- [[background-subtle-non-competing]]
- [[anomaly-detection-supervised-versus-unsupervised]]
- [[anomaly-detection-data-requirements]]
