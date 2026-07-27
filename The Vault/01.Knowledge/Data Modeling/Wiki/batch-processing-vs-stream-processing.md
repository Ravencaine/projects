---
created: 2026-07-27
source: "3 Easy Data Architecture Interview Questions (Conceptual)"
source_url: "https://medium.com/@jjr8888/3-easy-data-architecture-interview-questions-conceptual-bc156c36e851"
note_type: atomic
tags: [batch, stream, lambda, kappa, data-processing]
---

# Batch Processing vs Stream Processing

Two fundamental data processing paradigms distinguished by latency, complexity, and cost trade-offs.

## Definition

**Batch processing** computes results over data accumulated over a time interval (hourly, daily). **Stream processing** computes results incrementally as each data record arrives, with latency measured in seconds to minutes.

## Key Points

**Batch Processing:**
- Higher latency but simpler to implement and maintain
- More cost-effective for large data volumes
- Easier error handling and reprocessing (can re-run the batch)
- Appropriate for: nightly reports, historical analysis, ETL pipelines, non-time-sensitive data

**Stream Processing:**
- Low latency (seconds to minutes) for near-real-time results
- More complex infrastructure; requires handling late-arriving data
- Harder to reprocess — must maintain event ordering guarantees
- Appropriate for: fraud detection, live dashboards, IoT sensors, real-time personalisation

**Hybrid (Lambda Architecture):**
- Stream processing for time-sensitive metrics (live dashboards)
- Batch processing for comprehensive reconciliation (nightly accuracy check)
- Formalised pattern; now widely used

**Kappa Architecture:**
- Stream-only approach; batch treated as a replay of the stream
- Simpler than Lambda; gaining popularity with Kafka + stream processing frameworks

## Decision Factors

- How fresh does the data need to be? (15-minute lag acceptable? → batch)
- What is the cost of complexity vs value of real-time?
- Can your team maintain and monitor streaming infrastructure 24/7?

The honest default answer: **batch first, stream when a business requirement demands it.**

## Related

- [[medallion-architecture]] — layered architecture that typically receives both batch and stream inputs
- [[data-lake-vs-data-warehouse]] — storage patterns that host processed data
