---
created: 2026-07-28
updated: 2026-08-02
source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"
note_type: workflow
tags: [azure, hdinsight, hadoop, hive, cloud]
---

# Azure HDInsight: Provision Cluster, Run Hive Query, Download Results

The complete step-by-step workflow for setting up an Azure HDInsight Hadoop cluster, running an SQL query against Hive, and exporting results for downstream Excel analysis.

## Prerequisites

- Azure account (free 30-day trial at azure.microsoft.com/en-us/pricing/free-trial)
- Web browser to access manage.windowsazure.com

## Steps

1. **Create Azure Storage Account**
   - Azure Portal → +NEW → Data Services → Storage → Quick Create
   - Enter a unique URL name; select the nearest region; click Create Storage Account
   - After creation → Manage Access Keys → copy the Primary Access Key

2. **Provision HDInsight Hadoop Cluster**
   - +NEW → Data Services → HDInsight → Hadoop
   - Cluster name: enter a unique name
   - Version: default
   - Nodes: 2 (sufficient for learning/demo; cost is per-node)
   - Username: Admin (default); create password ≥ 10 chars with ≥ 1 capital letter, ≥ 1 number, ≥ 1 special character
   - Storage: link the Storage Account created in step 1
   - Click Create → cluster provisioning takes 15–20 minutes

3. **Run a Hive Query**
   - Portal → HDInsight → select cluster → click Query Console
   - Sign in with admin credentials
   - Click Hive Editor tab
   - Query name: enter a name
   - SQL: `SELECT * FROM hivesampletable` (or custom query)
   - Click Submit → wait for completion

4. **Download Query Results**
   - Click Job History → click the query job name
   - Click Download File → save the output (fixed-width text format, ~59,793 rows for sample data)
   - Alternatively: File Browser → navigate to cluster storage → find the output file

5. **Import into Power Query**
   - Open Excel → Power Query tab → From File → From Text
   - Browse to the downloaded file → Power Query auto-parses the fixed-width fields
   - Rename columns: right-click heading → Rename (see column mapping below)
   - Close & Load → data into spreadsheet

   | Old Name | New Name |
   |----------|----------|
   | Column2  | Datetime |
   | Column4  | OS |
   | Column5  | Manufacturer |
   | Column6  | Model |
   | Column7  | State |
   | Column8  | Country |
   | Column10 | Accesses |

6. **Delete the Cluster** (critical — billing continues until deleted)
   - Azure Portal → HDInsight → select cluster → Delete at bottom of screen

## Common Errors

- **Wrong field widths:** If Power Query mis-parses the fixed-width file, check the delimiter/width settings in Query Editor
- **Cluster timeout:** HDInsight clusters time out if idle; re-provision if the Query Console becomes unresponsive

## Related

- [[hdinsight-power-query-pivot-table-power-map-pipeline]] — the full end-to-end workflow this feeds into
- [[apache-hadoop-hdfs-mapreduce-architecture]] — underlying Hadoop/HDFS concepts
