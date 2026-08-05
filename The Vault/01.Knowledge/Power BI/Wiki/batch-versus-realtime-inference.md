---
created: 2026-07-28
updated: 2026-08-02
source: Artificial Intelligence with Power BI (Diepeveen)
note_type: atomic
tags: [batch-inference, realtime-inference, batch-vs-realtime, deployment-patterns]
---

# Batch vs Real-Time Inference

Two patterns for consuming ML model predictions: batch scoring on a schedule, or real-time scoring via an API endpoint.

## Definition

| Pattern | Description | Latency | Use case |
|---------|-------------|---------|---------|
| **Batch inference** | Score a large dataset on a schedule (daily, hourly) | Minutes to hours | Periodic reports, large datasets |
| **Real-time inference** | Score individual records on demand via API | Milliseconds to seconds | Interactive apps, live decisions |

## Batch Inference

- Run the model on a scheduled cadence (e.g., nightly at 2 AM)
- Score all pending records in a batch
- Store predictions in a database or table
- Power BI reads pre-computed predictions

```
Data Warehouse → Batch scoring job (nightly) → Predictions table → Power BI
```

**Advantages**: Can score millions of rows efficiently; no latency; cheaper per prediction
**Disadvantages**: Predictions are stale until next batch run

## Real-Time Inference

- Each incoming record is scored immediately via an API call
- Power BI calls the Azure ML endpoint directly on data refresh
- Used for interactive applications requiring immediate predictions

```
User action → Power BI → Azure ML endpoint → Real-time prediction
```

**Advantages**: Always fresh; immediate response
**Disadvantages**: Higher cost; latency per call; infrastructure needed for scale

## Related

- [[azure-ml-realtime-inference-pipeline]]
- [[azure-ml-model-integration-power-bi]]
