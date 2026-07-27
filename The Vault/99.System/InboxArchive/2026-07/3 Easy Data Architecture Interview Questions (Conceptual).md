---
title: "3 Easy Data Architecture Interview Questions (Conceptual)"
source: "https://medium.com/@jjr8888/3-easy-data-architecture-interview-questions-conceptual-bc156c36e851"
author:
  - "[[Jesse Ruiz (she/they)]]"
published: 2026-05-13
created: 2026-07-27
description: "For Job Hunters in Tech"
Processed: "Unprocessed"
---
## For Job Hunters in Tech

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*AA-NxyUalSDzwJD9)

Photo by Alex wong on Unsplash

In this article, I provide readers with three data architecture interview questions. These conceptual questions test your understanding of how data systems are designed — knowledge that distinguishes engineers who can build solutions from those who just write code.

These questions came from data engineering interviews where candidates needed to discuss architectural decisions and trade-offs. Please think through your answers before viewing the explanations below.

If you’re interested in data engineering, cloud architecture and practical technical guidance, please consider following my medium page.

```sh
- explain the difference between a data lake and a data warehouse
 - what is the medallion architecture and why is it useful?
 - when would you use batch processing vs stream processing?
```

Don’t look at the answers below until you tried it yourself…(scroll down for answers)

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*LGkNO41iY5zAwp4l)

Photo by Wim van 't Einde on Unsplash

— Explain the difference between a data lake and a data warehouse

Data Lake:

\- Stores raw data in native format (JSON, CSV, Parquet, images, logs)

\- Schema-on-read: structure applied when data is queried

\- Highly scalable and cost-effective for storage

\- Supports all data types including unstructured

\- Examples: Azure Data Lake, S3, GCS

\- Risk: can become a “data swamp” without governance

Data Warehouse:

\- Stores processed, structured data optimized for analytics

\- Schema-on-write: structure enforced when data is loaded

\- Optimized for fast query performance

\- Primarily structured, tabular data

\- Examples: Synapse Dedicated Pool, Snowflake, BigQuery, Redshift

\- Cost: higher per-GB but faster queries

Modern architectures often use both: data lake for staging/raw storage, data warehouse for curated analytics. Delta Lake and Lakehouse architectures blur this line by adding warehouse features to data lakes.

#Comments: interviewers want to hear about trade-offs, not just definitions. The practical answer is that most organizations need both — cheap storage for raw data and fast queries for dashboards.

— What is the medallion architecture and why is it useful?

Medallion architecture organizes a data lake into three progressive layers:

Bronze Layer (Raw):

\- Landing zone for source data

\- No transformations — exact copy of source

\- Append-only for audit trail

\- Enables reprocessing from source if logic changes

Silver Layer (Validated):

\- Cleansed and deduplicated data

\- Business rules applied

\- Data types enforced

\- Ready for analytics teams

Gold Layer (Aggregated):

\- Pre-computed metrics and KPIs

\- Optimized for dashboard performance

\- Denormalized for fast queries

\- Business-ready reporting

Why it’s useful:

\- Separation of concerns: each layer has clear purpose

\- Reprocessing: can rebuild Silver/Gold from Bronze if rules change

\- Quality gates: validation happens in controlled stages

\- Cost optimization: aggregations reduce query costs

#Comments: medallion architecture answers the question “where does data live as it moves from raw to report-ready?” It’s not the only approach, but it’s become the standard pattern in Delta Lake and Databricks environments.

— When would you use batch processing vs stream processing?

Batch Processing:

\- Processes data in scheduled intervals (hourly, daily)

\- Higher latency but simpler to implement

\- More cost-effective for large volumes

\- Easier error handling and reprocessing

\- Use when: nightly reports, historical analysis, ETL pipelines, data not time-sensitive

Stream Processing:

\- Processes data as it arrives in real-time

\- Low latency (seconds to minutes)

\- More complex infrastructure

\- Requires handling late-arriving data

\- Use when: fraud detection, live dashboards, IoT sensors, real-time personalization

Hybrid Approach:

Many systems use both — stream processing for time-sensitive metrics and batch processing for comprehensive daily reconciliation. The Lambda architecture formalized this pattern, though Kappa architecture (stream-only) is gaining popularity.

Decision factors:

\- How fresh does data need to be?

\- What’s the cost of complexity vs value of real-time?

\- Can your team maintain streaming infrastructure?

#Comments: the honest answer is usually “batch first, stream when required.” Real-time adds significant complexity. Most business questions can wait 15 minutes for an answer.

Thanks for reading!

#tech #jobinterview #dataarchitecture #dataengineering #cloud