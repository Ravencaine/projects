---
created: 2026-08-13
source: "Top 10 Data Cleaning Tasks in Power BI (Power Query Editor)"
source_url: https://medium.com/write-your-world/top-10-data-cleaning-tasks-in-power-bi-power-query-editor-65c3e34c8563
note_type: gotcha
tags: [power-query, fill, null-handling]
---

# Fill Down / Up — Direction Matters

Fill Down and Fill Up use the wrong direction will propagate values into the wrong rows.

## Expected Behaviour

You expect to fill blank cells in a column using the nearest non-blank value — but the direction is not obvious from the menu name.

## Actual Behaviour

- **Fill Down**: fills blanks using the value **above** the blank cell.
- **Fill Up**: fills blanks using the value **below** the blank cell.

Mixing them up propagates values in the wrong direction, corrupting the data.

## Why It Happens

The UI labels "Down" and "Up" refer to the direction of propagation through blank rows, not the direction of the source value. Fill Down walks **down** the column filling blanks with the last non-blank value above.

## How to Handle It

Before filling, determine the data's logical direction:
- **Excel-style tables** (values carry forward from above): use Fill **Down**
- **Reverse-fill tables** (values carry backward from below): use Fill **Up**

Always preview the result with a column sample before applying to the full dataset.

## Related Gotchas

- Wrong Data Type silently breaks visuals
