---
created: 2026-08-11
updated: 2026-08-11
source: "11-Power-BI-Tips-Guy-in-a-Cube-Transcript.md"
note_type: reference
tags: [power-bi, tips, keyboard-shortcuts, tabular-editor, reference]
---

# Guy in a Cube — 11 Power BI Tips (Ranked #1-#11)

Patrick (Guy in a Cube) ranks 11 Power BI tips by practical value, surprise factor, and real-world usefulness.

## The 11 Tips (Worst → Best)

| Rank | Tip | Category |
|------|-----|----------|
| #11 | Turn off Auto Date/Time when adding date columns | Model hygiene |
| #10 | Replace deeply nested IFs with SWITCH(TRUE, ...) | DAX |
| #9 | No DAX — push static calculations to SQL/Power Query | Architecture |
| #8 | PQ parameters to switch dev/test/prod | Power Query |
| #7 | Test mode parameters (true/false + row count) during dev | Power Query |
| #6 | Dedicated Measure Table for organization | Model |
| #5 | Bulk edit measures in Model view (multi-select) | Model |
| #4 | Tabular Editor: reuse Time Intelligence calculation groups | External tool |
| #3 | Ctrl+G in Power Query — jump to any column | Power Query |
| #2 | Field Parameters — dynamic dimension/measure switching | Modeling |
| #1 | **Ctrl+Shift+Alt in Tabular Editor:** bulk rename across measures | External tool |

## Key Rules

- **Auto Date/Time:** creates hidden date tables per date column — bloat. Mark as date table, then switch relationship from integer key to actual date → reduces hidden tables
- **SWITCH(TRUE):** order matters — highest threshold first, stops at first TRUE
- **Static calculations belong upstream:** no filter context needed = push to SQL/Power Query
- **Ctrl+Shift+Alt** in Tabular Editor/DAX formula editor: bulk rename matching text across selected measures. Watch for unintended matches inside names

## Related

- [[switches-for-nested-if-pattern]] — SWITCH(TRUE) pattern from DAX Code KB
- [[dim-date-dax-calendar]] — building a proper date dimension
