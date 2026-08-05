---
created: 2026-07-29
updated: 2026-08-02
source: "[[Author-Isabelle-Bittar|Isabelle Bittar]]"
note_type: pattern
tags: [alerts, custom-alerts, custom-visual, CONCATENATEX, CONTAINSSTRING]
related: [CONCATENATEX, CONTAINSSTRING, SWITCH, HTML-Content-Visual]
---

# Dynamic Alerts (CONCATENATEX + HTML Content)

Creates an interactive alert system where a DAX measure generates an HTML list of regions or categories that have exceeded a threshold, and an icon toggles between alert and clear states.

## Data Model

- `Regions` table: `[Region]`
- `Metrics` table: `[Metric Value]`, `[Alert Threshold]`

No relationship needed — use `CALCULATE + FILTER` to cross-filter.

## DAX Measures

**Alert regions HTML:**
```dax
Alert Regions =
VAR _AlertRegions =
    CONCATENATEX(
        FILTER(
            ALLSELECTED('Regions'[Region]),
            [Metric Value] > [Alert Threshold]
        ),
        "<li>" & 'Regions'[Region] & " (" & FORMAT([Metric Value], "$#,##0") & " increase)</li>",
        ""
    )
VAR _Html =
    "<p>⚠ Alerts in the following regions:</p><ul>" & _AlertRegions & "</ul>"
RETURN
    IF(_AlertRegions = "", "No new alerts", _Html)
```

**Alert icon toggle:**
```dax
Alert Icon =
    IF(
        CONTAINSSTRING([Alert Regions], "<li>"),
        "<i style=""color:#EE6064"" class=""fa-solid fa-circle-exclamation fa-xl""></i>",
        "<i style=""color:#76E3B4"" class=""fa-solid fa-circle-check fa-xl""></i>"
    )
```

## Setup

1. Add the **HTML Content** visual to the report.
2. Drag `Alert Regions` to the visual's **Text** field well.
3. Add a second HTML Content visual for `Alert Icon`.
4. Position the icon visual next to the main visual.

## Alert Measure Variants

**Count-based alert:**
```dax
Alert Count =
    COUNTROWS(
        FILTER(
            ALLSELECTED(Regions),
            [Metric Value] > [Alert Threshold]
        )
    )
```

**Text summary alert:**
```dax
Alert Summary =
    VAR _Count =
        COUNTROWS(
            FILTER(ALLSELECTED(Regions), [Metric Value] > [Alert Threshold])
        )
    RETURN
        "⚠ " & _Count & " region(s) above threshold"
```

## Notes

- `CONCATENATEX` with `FILTER(ALLSELECTED(...), ...)` respects the user's slicer selections — only selected regions that exceed the threshold appear in the list.
- `CONTAINSSTRING` detects whether the HTML list is empty to toggle the icon — simpler than checking `_Count > 0`.
- The `<ul>` and `<li>` HTML tags render as bullet lists inside the HTML Content visual.
- `FORMAT` inside `CONCATENATEX` produces formatted numbers (currency, percentage) in the alert list.
- For performance, keep the `Regions` table small — `CONCATENATEX` iterates over all selected rows.

## Related

- [[CONCATENATEX]] — build the HTML list
- [[CONTAINSSTRING]] — detect alert state
- [[HTML-Content-Visual]] — Font Awesome icons
- [[SWITCH]] — extend with multiple alert levels
