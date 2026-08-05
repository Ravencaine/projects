---
created: 2026-08-02
source: Elevate Your Power BI Bar Charts with 6 Simple Improvements.md
note_type: pattern
tags: [powerbi, dax, dynamic-title, filter-context, insight]
---

# Insight-Driven Dynamic Chart Title

A DAX measure that finds the top value in the current filter context and embeds it into a natural-language chart title, replacing a static descriptive label with a narrative insight.

## Purpose

Instead of "Vacant positions by Region," the title becomes "The Montreal region has the most vacant teaching positions." The measure scans the current visual's data, identifies the top performer, and returns a sentence describing it. The title updates automatically as filters change.

## Structure

```dax
Title =
VAR _TopValue =
    CALCULATE(
        MAXX(
            DISTINCT('Postes vacants'[Région administrative]),
            [Vacant positions]
        )
    )
VAR _TopRegion =
    CALCULATE(
        FIRSTNONBLANK(DISTINCT('Postes vacants'[Région administrative]), 1),
        FILTER(
            DISTINCT('Postes vacants'[Région administrative]),
            [Vacant positions] = _TopValue
        )
    )
RETURN
    "The " & _TopRegion & " region has the most vacant teaching positions. "
```

## How It Works

1. `MAXX(DISTINCT(...), [Vacant positions])` — finds the maximum value across all regions in the current filter context.
2. `FILTER(DISTINCT(...), [Vacant positions] = _TopValue)` — identifies which region(s) hold that maximum.
3. `FIRSTNONBLANK(DISTINCT(...), 1)` — returns the name of the top region (handles ties by returning the first non-blank).
4. The `CALCULATE` wrapper forces re-evaluation under the adjusted filter context produced by FILTER.
5. Concatenate into a natural-language string for the visual's title field.

## Key Rules

- The outer `CALCULATE` around both MAXX and FIRSTNONBLANK is essential: it creates the filter context for the FILTER expression to operate within.
- When multiple regions tie for top, `FIRSTNONBLANK` returns the first alphabetically or by data order.
- Applied to the visual's Title → Dynamic title → Field value.

## Related

- [[dynamic-chart-subtitle-from-filter-context]]
- [[conditional-bar-color-highlight-top]]
- [[6-bar-chart-elevations]]
