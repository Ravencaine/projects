---
created: 2026-08-02
updated: 2026-08-05
source: Elevate Your Power BI Bar Charts with 6 Simple Improvements.md
note_type: pattern
tags: [powerbi, dax, dynamic-subtitle, drilldown, filter-context]
---

# Dynamic Chart Subtitle from Filter Context

A DAX measure that generates a contextual subtitle describing the top-performing item and inviting users to drill down — updating as filter context changes.

## Purpose

The subtitle supplements the insight-driven title by surfacing a second-tier insight (top institution within the top region) and guiding users to the drill-down feature. It changes when filters are applied, keeping the user oriented.

## Structure

```dax
Subtitle =
VAR _TopValueOrganisme =
    CALCULATE(
        MAXX(
            DISTINCT('Postes vacants'[Organisme]),
            [Vacant positions]
        )
    )
VAR _TopOrganisme =
    CALCULATE(
        FIRSTNONBLANK(DISTINCT('Postes vacants'[Organisme]), 1),
        FILTER(
            DISTINCT('Postes vacants'[Organisme]),
            [Vacant positions] = _TopValueOrganisme
        )
    )
VAR _TopRegion =
    CALCULATE(
        FIRSTNONBLANK('Postes vacants'[Région administrative], 1),
        FILTER(
            'Postes vacants',
            'Postes vacants'[Organisme] = _TopOrganisme
        )
    )
RETURN
    IF(
        _TopRegion <> [Top Overall Region],
        "However " & _TopOrganisme & " from " & _TopRegion &
            " is the institution with the highest number of vacant positions. Click on the drill-down to see details.",
        [Top Organisme] & " from " & _TopRegion &
            " is the institution with the highest number of vacant positions. Click on the drill-down to see details."
    )
```

## How It Works

1. `MAXX(DISTINCT(...), [Vacant positions])` — finds the top institution's vacancy count in the current context.
2. `FILTER(DISTINCT(...), [Vacant positions] = _TopValueOrganisme)` — isolates the top institution(s).
3. `FIRSTNONBLANK(DISTINCT(...), 1)` — returns the institution name.
4. A second `CALCULATE` + `FILTER` cross-filters from institution to region — finding which region the top institution belongs to.
5. `IF` checks whether the top institution's region matches the overall top region. If not, it shifts language to "However..." to reflect that the institution sits in a different region.
6. The final sentence includes a call-to-action for the drill-down feature.

## Key Rules

- Two levels of CALCULATE+FILTER: one for the top institution, one to cross-map institution to region.
- Applied to the visual's Subtitle → Dynamic subtitle → Field value.

## Related

- [[insight-driven-dynamic-chart-title]]
- [[6-bar-chart-elevations]]
