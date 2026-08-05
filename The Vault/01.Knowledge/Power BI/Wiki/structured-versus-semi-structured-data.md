---
created: 2026-07-28
updated: 2026-08-02
source: Artificial Intelligence with Power BI (Diepeveen)
note_type: pattern
tags: [structured-data, semi-structured-data, tabular, json, nosql, azure-cosmos-db]
---

# Structured vs Semi-Structured Data

Structured data is tabular (rows and columns). Semi-structured data is key-value or document-based (JSON, NoSQL) and requires transformation before tabular analysis.

## Purpose

Knowing the data structure determines how you import and prepare it in Power Query.

## Components

| Property | Structured | Semi-Structured |
|----------|-----------|----------------|
| Format | CSV, Excel, SQL table | JSON, NoSQL (Cosmos DB) |
| Schema | Fixed columns | Flexible, self-describing |
| Storage | Azure SQL, Excel, CSV | Azure Cosmos DB, Blob Storage |
| In Power BI | Native connector | JSON expand via PQ |
| Challenge | Type mismatches | Missing keys, varying schemas |

## Structured Example

```
Country Name, Year, Life Ladder, GDP per Capita
Finland, 2019, 7.8, 45300
Denmark, 2019, 7.6, 58800
```

→ Direct import into Power BI, tabular from the start.

## Semi-Structured Example (JSON)

```json
[
  { "Country": "Finland", "Metrics": { "Year": 2019, "LifeLadder": 7.8 } },
  { "Country": "Denmark", "Metrics": { "Year": 2019 } }
]
```

→ Some documents may be missing keys (Denmark has no LifeLadder). Must expand in Power Query.

## Power Query Approach

1. **Structured**: Get Data → CSV/Excel → Load → Explore
2. **Semi-structured**: Get Data → JSON → Power Query Editor → Expand columns

## Related

- [[fixing-data-structure-pq]]
- [[power-query-expand-versus-extract]]
- structured-versus-semi-structured-data
