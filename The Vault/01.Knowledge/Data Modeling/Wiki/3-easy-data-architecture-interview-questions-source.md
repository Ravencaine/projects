---
created: 2026-07-27
updated: 2026-08-02
source: "3 Easy Data Architecture Interview Questions (Conceptual)"
source_url: "https://medium.com/@jjr8888/3-easy-data-architecture-interview-questions-conceptual-bc156c36e851"
note_type: source
tags: [data-architecture, data-lake, medallion, batch, stream]
---

# 3 Easy Data Architecture Interview Questions (Conceptual)

A Medium article by Jesse Ruiz presenting three conceptual data engineering interview questions covering the difference between data lakes and data warehouses, medallion architecture, and batch vs stream processing.

> **Type:** article
> **Author:** Jesse Ruiz (she/they)
> **Published:** 2026-05-13
> **URL:** https://medium.com/@jjr8888/3-easy-data-architecture-interview-questions-conceptual-bc156c36e851
> **Routed to:** Data Modeling

## Summary

Three conceptual interview questions designed to distinguish engineers who understand architectural trade-offs from those who only know syntax. Each question comes with an explanation covering not just definitions but the practical decision factors — cost, complexity, and when each approach breaks down.

## Key Claims

- Data lakes use schema-on-read; data warehouses use schema-on-write; modern architectures use both
- Medallion architecture (Bronze/Silver/Gold) is the standard Delta Lake pattern; it enables reprocessing from Bronze when rules change
- Batch vs stream: honest default answer is batch first, stream when a business requirement demands real-time
- Lambda architecture combines batch + stream; Kappa simplifies to stream-only
- The practical interview answer for most questions is about trade-offs, not definitions

## Notable Details

- Comment from author: "most organisations need both — cheap storage for raw data and fast queries for dashboards"
- Comment: "Delta Lake and Lakehouse architectures blur the line by adding warehouse features to data lakes"
- Comment: "The honest answer is usually 'batch first, stream when required.' Most business questions can wait 15 minutes"

## Extracted Notes

Links to notes derived from this source:

- [[data-lake-vs-data-warehouse]] — `atomic` — lake vs warehouse comparison
- [[medallion-architecture]] — `atomic` — Bronze/Silver/Gold layers
- [[batch-processing-vs-stream-processing]] — `atomic` — batch vs stream
- [[lambda-kappa-architecture]] — `atomic` — hybrid patterns

## Metadata

| Field | Value |
|-------|-------|
| Source file | 3 Easy Data Architecture Interview Questions (Conceptual).md |
| Archived at | 99.System/InboxArchive/2026-07/ |
| Ingestion date | 2026-07-27 |
| Word count | ~1,100 |
