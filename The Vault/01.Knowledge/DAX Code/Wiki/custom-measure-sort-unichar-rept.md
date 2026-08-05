---
created: 2026-08-02
source: Power BI: Elevating Data Visualization with Custom Measure Sorting
note_type: pattern
tags: [dax, pattern, sorting, measure, unicode, switch]
---

# Custom Measure Sort Order: UNICHAR(8203) + REPT() Invisible Prefix

DAX measures in table visuals can only sort alphabetically or numerically. To impose a custom lexical sort order, prepend invisible Unicode characters to each SWITCH branch result — Power BI sorts by the full string including the prefix.

**Mechanism:**
- `UNICHAR(8203)` = zero-width space (ZWSP) — invisible in the rendered visual but counted as a character by Power BI's sort
- `REPT(UNICHAR(8203), N)` prepends N ZWSP characters — more spaces = sorted earlier
- SWITCH branch ordering (most spaces → least spaces) maps to the desired sort order

**Usage pattern:**
```dax
Overall Progress =
    SWITCH(
        TRUE(),
        [Cumulative completion] > [Cumulative planned completion],
            REPT(UNICHAR(8203), 4) & "Ahead of schedule",
        [Cumulative completion] = [Cumulative planned completion],
            REPT(UNICHAR(8203), 3) & "On schedule",
        [Cumulative completion] + 0.05 >= [Cumulative planned completion],
            REPT(UNICHAR(8203), 2) & "Slightly behind schedule",
        REPT(UNICHAR(8203), 1) & "Behind schedule"
    )
```

Sort the table column on itself (Sort by Column → same column) to activate the custom order.
