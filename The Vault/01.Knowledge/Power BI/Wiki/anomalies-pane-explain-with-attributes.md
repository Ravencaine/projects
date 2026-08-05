---
created: 2026-07-28
updated: 2026-08-02
source: Artificial Intelligence with Power BI (Diepeveen)
note_type: function
tags: [anomaly-detection, anomalies-pane, explain, attributes, drilldown]
---

# Anomalies Pane — Explain with Attributes

The Anomalies pane in Power BI explains *why* a specific anomaly occurred by attributing it to specific dimension values.

## Signature

Power BI: Analytics pane → Anomalies Pane (appears after enabling Find Anomalies)

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| Select anomaly | click from chart | Select the red dot anomaly point |
| Explain by | field selector | Select dimension(s) to attribute the anomaly to |

## Returns

A ranked list of contributing factors for the selected anomaly, showing which attribute values most contributed to the deviation.

## Steps

1. Enable Find Anomalies on a Line Chart
2. Open the **Anomalies Pane** from the Analytics pane
3. Click an anomaly red dot on the chart
4. The pane shows: "Why did this anomaly occur?" with contributing dimensions ranked
5. Add fields to "Explain by" to drill into specific dimensions (e.g., Region, Product Category)

## Notes

- **Anomaly correlations** can be spurious — the model finds statistical associations, not causal relationships
- Domain expertise is required to validate whether the attributed cause makes business sense
- Useful for investigation but conclusions should always be reviewed by an analyst

## Related

- [[anomaly-detection-visual]]
- [[anomaly-correlations-require-domain-expertise]]
- [[correlation-does-not-imply-causation]]
