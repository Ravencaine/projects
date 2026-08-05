---
created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
note_type: pattern
tags: [hdinsight, power-query, power-map, azure, pipeline]
---

# HDInsight → Power Query → Pivot Table → Power Map Pipeline

A four-stage end-to-end workflow that moves data from a cloud Hadoop cluster through Excel-based self-service BI tools for analysis and geographic visualization.

## Purpose

This pipeline demonstrates the full self-service BI spectrum: cloud-scale data storage and processing (HDInsight/Hive), self-service extraction (Power Query), self-service aggregation (Pivot Table), and self-service geographic visualization (Power Map). It is the book's most comprehensive integration example.

## Components

1. **Azure HDInsight**: Hadoop-on-Azure for storing and processing web-scale data
2. **Apache Hive**: SQL-like query layer on top of Hadoop; runs in the HDInsight cluster
3. **Power Query**: extracts data from the Hive output into Excel
4. **Excel Pivot Table**: aggregates the extracted data
5. **Power Map**: plots geographic dimensions on Bing Maps in 3D

## Structure

```
Azure HDInsight (Hadoop cluster)
  → Hive Query (SQL against HDFS data)
  → Download results as fixed-width text file
  → Power Query (parse, rename columns, load to sheet)
  → Excel Pivot Table (aggregate by geography + category)
  → Power Map (plot on Bing Maps in 3D)
```

## Example

1. Provision Azure HDInsight Hadoop cluster (2 nodes minimum)
2. In HDInsight Query Console → open Hive Editor → run `SELECT * FROM hivesampletable`
3. Click Job History → Download File → save to desktop
4. Excel → Power Query → From File → From Text → select downloaded file
5. Power Query auto-parses fixed-width fields into columns; rename columns (e.g., Column2 → Datetime, Column4 → OS)
6. Close & Load → data lands in spreadsheet
7. Insert → Pivot Table → drag Country/State to Rows, OS to Columns, Accesses to Values
8. Insert → Map → Launch Power Map → accept default geographic fields → drag Accesses to Height, OS to Category

## Notes

- Delete the HDInsight cluster after use to stop billing
- Power Query correctly auto-parsed the fixed-width log file — no manual delimiter configuration was needed
- Power Map requires a date field for time animation; right-click the year column → Rename → change type to Date

## Related

- [[apache-hadoop-hdfs-mapreduce-architecture]] — underlying Hadoop architecture
- [[azure-hdinsight-provision-cluster-hive-query-download-results]] — the provisioning steps
- [[power-map-install-layer-tour-bubble-heat-region-time-animation]] — Power Map features
