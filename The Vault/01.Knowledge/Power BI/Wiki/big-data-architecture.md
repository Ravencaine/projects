---


title: "Big Data Architecture Concepts"
created: 2026-07-28
updated: 2026-08-02
tags: [big-data, concept, reference]
note_type: atomic
description: "Key big data architecture concepts from Dunlop — Hadoop HDFS, MapReduce, Apache Spark, Hive, schema on read, NoSQL CAP Theorem, NewSQL, SQL++."


source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"

---

# Big Data Architecture Concepts

## Hadoop

**Hadoop** = open-source distributed file system (HDFS) + programming framework (MapReduce) for processing large datasets across commodity hardware.

### HDFS (Hadoop Distributed File System)
- Stores data across multiple nodes
- Data is split into blocks (default 64/128 MB) and replicated
- Designed for throughput over latency

### MapReduce
- Two-phase processing: Map (filter/sort) + Reduce (aggregate)
- Designed for batch processing
- Apache Hive provides SQL-like query layer on top of MapReduce

## Apache Spark

Successor to MapReduce — in-memory processing for faster batch and streaming workloads. Supports SQL, machine learning (MLlib), graph processing (GraphX), and streaming.

## Schema on Read vs. Schema on Write

| | Schema on Write | Schema on Read |
|--|--|--|
| Definition | Schema defined before data is stored | Schema applied when data is read |
| Used by | Relational databases | NoSQL / Hadoop |
| Trade-off | Enforces structure at load time | Flexible at load, structure at query time |

## NoSQL

"NoSQL" = non-relational or not-only-SQL. Includes:
- Document stores (MongoDB)
- Key-value stores (Redis)
- Column-family stores (Cassandra)
- Graph databases (Neo4j)

### CAP Theorem
A distributed system can only guarantee two of three: **Consistency**, **Availability**, **Partition tolerance**. Since network partitions are unavoidable in distributed systems, the choice is between CP (consistent + partition-tolerant) and AP (available + partition-tolerant).

## NewSQL

Combines relational architecture with NoSQL scalability. Examples: Google Spanner, CockroachDB, NuoDB.

## SQL++ / N1QL

Extends traditional SQL to query semi-structured JSON data. Backward-compatible with SQL. N1QL (pronounced "Nickel") is the Couchbase implementation.

## Source Reference

Chapter 1, *Beginning Big Data with Power BI and Excel 2013* (Dunlop, Apress 2015).
