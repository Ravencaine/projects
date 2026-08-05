---
created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
note_type: atomic
tags: [nosql, database, theory]
---

# NoSQL: CAP Theorem — Consistency vs. Availability vs. Partition Tolerance

The CAP Theorem (Brewer's Theorem) defines the fundamental trade-off all distributed databases must make: no distributed data store can simultaneously guarantee all three of Consistency, Availability, and Partition Tolerance.

## Definition

- **Consistency (C):** Every read receives the most recent write or an error
- **Availability (A):** Every request receives a response — even if it's not the most recent data
- **Partition Tolerance (P):** The system continues operating despite network partitions (nodes unable to communicate)

The theorem states that a distributed system can only guarantee two of three simultaneously. Since network partitions are unavoidable in real systems, the actual choice is between **CP** (give up availability) and **AP** (give up strong consistency).

## Key Points

- NoSQL databases emerged to handle web-scale data where availability and partition tolerance matter more than immediate consistency
- "Eventual consistency" is the AP model: writes propagate asynchronously, reads may return stale data briefly
- The term "NoSQL" is a misnomer — some NoSQL systems (Couchbase N1QL, MarkLogic) support SQL-like query languages
- More accurate terms: non-relational, schema-on-read, or document store
- Common NoSQL categories: key-value (Redis, DynamoDB), document (MongoDB, Couchbase), column-family (Cassandra, HBase), graph (Neo4j)

## Examples

- Cassandra is AP — optimized for write-heavy, geographically distributed workloads (Instagram, Netflix)
- HBase is CP — strong consistency required for financial or order-processing use cases
- MongoDB defaults to CP but can be configured for AP with replica sets

## Related

- [[newsql-relational-architecture-sql-nosql-scalability]] — the NewSQL compromise
- [[sql-plus-plus-and-n1ql]] — SQL++ extending SQL to semi-structured data
- [[star-schema-fact-table-dimension-tables-in-powerpivot]] — the relational alternative to NoSQL
