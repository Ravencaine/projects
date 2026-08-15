---
title: "Top 5 Excel Formulas Every Power BI Developer Should Know"
source: "https://medium.com/write-a-catalyst/top-5-excel-formulas-every-power-bi-developer-should-know-2f562acf8157"
author:
  - "[[Anurodh Kumar]]"
published: 2025-05-10
created: 2026-08-11
description: "More"
Processed: "Unprocessed"
---
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*I2afHQTEldh7KMrstn7qYg.png)

## 1\. VLOOKUP / XLOOKUP

## Use Case: Merging tables before import

Before bringing data into Power BI, you might need to combine tables in Excel (especially if using flat files like CSVs).

```c
=XLOOKUP(A2, Table2[ID], Table2[Name])
```

✅ Helpful when creating relationships or checking data integrity.

## 2\. TEXT()

## Use Case: Formatting dates or numbers

```c
=TEXT(A2, "YYYY-MM")
```

✅ Useful for creating custom date keys (e.g., “2024–03”) for mapping or joining with calendar tables in Power BI.

## 3\. IF / IFS

## Use Case: Creating conditional columns

```c
=IF(B2 > 1000, "High", "Low")
```

✅ Helps simulate DAX calculated columns in Excel before importing data.

## 4\. CONCATENATE / TEXTJOIN

## Use Case: Creating composite keys or merging values

```c
=TEXTJOIN("-", TRUE, A2, B2, C2)
```

✅ Useful when data lacks a unique ID and you need to combine multiple fields to create one.

## 5\. LEN / TRIM / CLEAN

## Use Case: Data cleaning

```c
=TRIM(CLEAN(A2))
```

✅ Removes extra spaces or non-printable characters, preventing mismatches in Power BI joins.