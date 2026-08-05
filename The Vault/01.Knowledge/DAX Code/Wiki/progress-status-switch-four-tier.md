---
created: 2026-08-02
source: Power BI: Elevating Data Visualization with Custom Measure Sorting
note_type: pattern
tags: [dax, pattern, switch, sorting, progress, status]
---

# Progress Status SWITCH: Four-Tier Sequence via UNICHAR Padding

A SWITCH-based progress measure that returns one of four status labels, with ZWSP prefixes encoding the desired sort order.

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

**Sort sequence produced:** Ahead → On schedule → Slightly behind → Behind

**Padding convention used:** 4/3/2/1 spaces — more significant status gets more padding (sorted first). Any consistent spacing scheme works as long as it decreases in the direction of the intended sort.

**Requirement:** Sort the column by itself (Sort by Column → same column) after adding the measure.
