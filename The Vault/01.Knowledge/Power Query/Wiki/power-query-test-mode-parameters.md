---
created: 2026-08-11
updated: 2026-08-11
source: "11-Power-BI-Tips-Guy-in-a-Cube-Transcript.md"
note_type: workflow
tags: [power-bi, power-query, devops, workflow]
---

# Power Query Test Mode Parameters

Use two parameters (`TestMode` true/false + `TestRowCount`) to limit data during development, then disable for full refresh.

## Steps

1. Create `TestMode` parameter — type True/False, default `false`
2. Create `TestRowCount` parameter — type Decimal, default `10`
3. Create a new blank query wrapping the source query:

```m
let
    Source = Sql.Database(...),
    Filtered = if TestMode = true
        then Table.FirstN(Source, TestRowCount)
        else Source
in
    Filtered
```

4. Switch `TestMode` to `true` → returns only N rows
5. Switch to `false` before production refresh

## Nuance

**Watch query folding:** if Power Query pulls all rows across the network before applying `Table.FirstN`, no performance gain. The row reduction must happen at the source (SQL `TOP`, etc.) for large tables.

## Related

- [[power-query-parameters-dev-test-prod]] — server/database parameter switching
