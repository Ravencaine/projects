---
created: 2026-08-08
updated: 2026-08-08
source: 11 Power BI Tips
note_type: atomic
tags: [power-query, parameter, development, performance]
---

# Test Mode Parameters: Limit Rows During Development

Use boolean + number parameters to limit row counts during development for faster refreshes, then disable before production.

## Definition

When developing against large tables, you don't need every row — just enough to validate transforms and the model. A `TestMode` (true/false) and `TestRowCount` (number) parameter pair gates row limits. When `TestMode = TRUE`, only the specified number of rows are returned. Turn off before the full production refresh.

## Key Points

- `TestMode` (True/False) — master switch
- `TestRowCount` (Decimal/Number) — how many rows to return when test mode is on
- Gate applied inside a blank query or by wrapping the source step in `if TestMode then ... else ...`
- Saves time during iterative development; must be disabled before production publish
- **Critical**: check query folding to ensure row reduction happens at the source, not after pulling all rows across the network
- If Power Query pulls the full dataset then only keeps N rows locally, performance savings are negated
- Goal: push the TOP/FETCH/LIMIT clause back to the source query or connector

## Example

**M code (Advanced Editor):**
```
let
    Source = if TestMode
              then Sql.Database(ServerName, DatabaseName, [Query="SELECT TOP " & Number.ToText(TestRowCount) & " * FROM Bookings"])
              else Sql.Database(ServerName, DatabaseName, [Query="SELECT * FROM Bookings"])
in
    Source
```

**Set TestRowCount = 10, TestMode = True** → returns 10 rows.
**Set TestMode = False** → returns full dataset.

## Related

- [[Power-Query-Parameters-Environment-Switch]] — related PQ parameter pattern
