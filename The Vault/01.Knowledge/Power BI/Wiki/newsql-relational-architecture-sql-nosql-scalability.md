---
created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
note_type: atomic
tags: [newsql, database, scalability]
---

# NewSQL: Relational Architecture + SQL + NoSQL Scalability

NewSQL systems aim to deliver the ACID guarantees and SQL interface of traditional relational databases, combined with the horizontal scalability and fault tolerance of NoSQL architectures.

## Definition

NewSQL is a class of modern database systems that bridge the gap between:
- **Relational/SQL:** Fixed schema, ACID transactions, standard SQL interface
- **NoSQL:** Horizontal scale-out across commodity nodes, automatic sharding, high availability

Dunlop (Ch5) introduces NewSQL as a compromise architecture — relational at the core but designed for the same distributed deployment model as NoSQL.

## Key Points

- NewSQL targets applications that need both transactional consistency and web-scale performance — order processing, financial systems, real-time inventory
- Google Spanner is a canonical NewSQL example: globally distributed, strongly consistent, uses atomic clocks for global transaction ordering
- CockroachDB and TiDB are open-source NewSQL systems inspired by Spanner
- VoltDB targets in-memory transactional workloads with sub-millisecond latency
- NewSQL systems typically avoid the legacy overhead of Oracle/MySQL while maintaining SQL compatibility

## Examples

- An e-commerce platform needs ACID transactions (no overselling inventory) at Black Friday scale — NewSQL handles both
- A financial trading platform needs serializable transactions with microsecond latency across geographically distributed data centers

## Related

- [[nosql-cap-theorem]] — the foundational trade-off NewSQL attempts to resolve
- [[sql-plus-plus-and-n1ql]] — SQL++ as a query language for semi-structured data, complementary to NewSQL
- [[star-schema-fact-table-dimension-tables-in-powerpivot]] — relational modeling concepts within PowerPivot
