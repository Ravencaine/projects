---
created: 2026-07-27
source: "3 Easy Data Architecture Interview Questions (Conceptual)"
source_url: "https://medium.com/@jjr8888/3-easy-data-architecture-interview-questions-conceptual-bc156c36e851"
note_type: atomic
tags: [lambda, kappa, architecture, hybrid, stream, batch]
---

# Lambda and Kappa Architecture

Two patterns for combining batch and stream processing to serve both historical accuracy and real-time speed.

## Definition

**Lambda Architecture** combines a batch layer (serving comprehensive, accurate historical views) with a streaming layer (serving low-latency approximate views). Results are merged at query time. **Kappa Architecture** simplifies this by treating all data as streams — batch processing becomes a replay of the stream through a faster processing engine.

## Key Points

**Lambda Architecture:**
- Three layers: Batch (historical truth), Speed (real-time approximation), Serving (merged query output)
- Guarantees both accuracy (batch) and recency (stream)
- Drawback: maintaining two codebases (batch and stream logic) is expensive

**Kappa Architecture:**
- One code path: the stream processor handles both real-time and historical replay
- Simpler operation — no dual stack to maintain
- Assumes ordered, immutable event streams (well-suited to Kafka)
- Best when: the business can tolerate eventual consistency at scale

**Lambda is still the safer choice** when:
- Batch and stream computations have meaningfully different logic
- Historical accuracy is legally required (audit, financial reporting)
- The team lacks mature stream processing tooling

## Related

- [[batch-processing-vs-stream-processing]] — the underlying paradigms Lambda/Kappa combine
- [[medallion-architecture]] — layered architecture often used alongside Lambda/Kappa in lakehouse deployments
