---
created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
note_type: atomic
tags: [big-data, hadoop, architecture]
---

# Apache Hadoop: HDFS + MapReduce Architecture

Hadoop is an open-source distributed file system and processing framework designed to store and analyze data at web scale across commodity hardware clusters.

## Definition

Hadoop has two core components, introduced in Ch1 by Dunlop:

- **HDFS (Hadoop Distributed File System):** Stores data across multiple nodes in a cluster. Files are split into blocks (default 128 MB or 256 MB) and replicated across nodes for fault tolerance.
- **MapReduce:** The processing model. Map phase distributes work across nodes; Reduce phase aggregates results. Used for batch processing large datasets.

## Key Points

- Hadoop is the dominant open-source big data infrastructure — Microsoft Azure HDInsight is Microsoft's managed Hadoop-on-cloud implementation
- Hadoop handles unstructured and semi-structured data at scale (logs, sensor data, web clicks) — complementing SQL/RDBMS workloads
- Apache Hive, built on top of Hadoop, provides SQL-like query capability (HiveQL) against HDFS data — enables non-programmers to query massive datasets
- Apache Spark supersedes MapReduce as the preferred processing engine — but Hadoop/HDFS remains the dominant storage layer
- Commercial Hadoop distributions: Cloudera, Hortonworks, MapR; cloud-managed: AWS EMR, Azure HDInsight, Google Dataproc

## Examples

- HDInsight provisioned in Azure, Hive query run against web log data, results exported to Power Query for Excel analysis (Ch11 workflow)
- GE collects 50 million data points per day from 1.4 million medical devices and 28,000 jet engines on Hadoop infrastructure

## Related

- apache-hadoop-hdfs-mapreduce-architecture is this note
- [[hdinsight-power-query-pivot-table-power-map-pipeline]] — end-to-end Azure → Excel workflow
- [[azure-hdinsight-provision-cluster-hive-query-download-results]] — specific provisioning steps
