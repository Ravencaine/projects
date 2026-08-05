---


title: "Azure HDInsight and Power Query"
created: 2026-07-28
updated: 2026-08-02
tags: [power-bi, azure, pattern]
note_type: atomic
description: "Exporting Hive query results from Azure HDInsight to Power Query — fixed-width parsing, column renaming, Pivot Tables. From Dunlop Chapter 11."


source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"

---

# Azure HDInsight and Power Query

Export data from Hadoop on Azure into Excel via Power Query for analysis.

## Architecture

```
Azure HDInsight (Hadoop Cluster)
  → Hive Query (SELECT * FROM hivesampletable)
  → Download to local file (fixed-width format)
  → Power Query (import + parse + rename)
  → Excel (Pivot Table, Power Map)
```

## Key Steps

### 1. Provision Hadoop Cluster on Azure
- Create Azure Storage Account (blob storage)
- Set cluster name, admin password (10+ chars, uppercase, number, special)
- Takes ~20 minutes to provision

### 2. Run Hive Query
```
HDInsight Query Console → Hive Editor → Submit
SELECT * FROM hivesampletable
```

### 3. Download Results
- Download button on Job screen
- Result: fixed-width text file (no delimiters)
- Power Query automatically parses fixed-width fields into columns

### 4. Load into Power Query

```
Power Query → From File → From Text → browse to file
```

Power Query **auto-parses** the fixed-width fields into separate columns (no manual delimiter needed).

### 5. Rename Columns in Query Editor

```
Right-click column → Rename
Column2 → Datetime
Column4 → OS
Column5 → Manufacturer
```

## Source Reference

Chapter 11, *Beginning Big Data with Power BI and Excel 2013* (Dunlop, Apress 2015).
