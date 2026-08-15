---
created: 2026-08-11
updated: 2026-08-11
source: "11-Power-BI-Tips-Guy-in-a-Cube-Transcript.md"
note_type: workflow
tags: [power-bi, power-query, devops, workflow]
---

# Power Query Dev/Test/Prod Parameters

Use `ServerName` and `DatabaseName` parameters to switch connection strings across environments without rewriting queries.

## Steps

1. Create `ServerName` parameter — type Text
2. Create `DatabaseName` parameter — type Text
3. Enable "Allow Parameters" in View tab
4. Go to Data Source Settings → Change Source → use parameters instead of hardcoded values
5. Change parameter values → applies to all queries that reference them

## Structure

```m
Source = Sql.Database(ServerName, DatabaseName, ...)
```

## Why It Matters

Once working across multiple environments (dev → test → prod), hardcoded server/database names become unmanageable. One parameter change replaces dozens of query edits.

## Related

- [[power-query-test-mode-parameters]] — test mode for row limiting during dev
