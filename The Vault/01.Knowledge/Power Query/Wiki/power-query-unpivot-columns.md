---
created: 2026-07-28
updated: 2026-08-02
source: Artificial Intelligence with Power BI (Diepeveen)
note_type: function
tags: [power-query, unpivot, transform, long-format, wide-format]
---

# Table.Unpivot

Transforms columns into rows — converts a wide-format table into long format for analysis.

## Signature

```
Table.Unpivot(
  table as table,
  pivotColumns as list,
  attributeColumn as text,
  valueColumn as text
)
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| table | table | Source table |
| pivotColumns | list | Columns to unpivot (stays as-is) |
| attributeColumn | text | New column name for the unpivoted column names |
| valueColumn | text | New column name for the unpivoted values |

## Example

Before (wide format — Year columns are separate):

| Country | Year_2018 | Year_2019 | Year_2020 |
|---------|-----------|-----------|-----------|
| Finland | 7.6 | 7.8 | 7.9 |

After Unpivot (long format):

| Country | Year | Score |
|---------|------|-------|
| Finland | Year_2018 | 7.6 |
| Finland | Year_2019 | 7.8 |
| Finland | Year_2020 | 7.9 |

## Steps in Power Query Editor

1. Select the columns you want to keep (Country)
2. Transform → Unpivot Other Columns
3. Rename `Attribute` → Year, `Value` → Score

## Related

- [[fixing-data-structure-pq]]
- [[power-query-expand-versus-extract]]
- [[table_unpivot]]
