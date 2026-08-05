---
created: 2026-07-29
updated: 2026-08-02
source: "[[Author-Isabelle-Bittar|Isabelle Bittar]]"
note_type: source
tags: [source, alerts, custom-alerts, COVID-WHO, DAX-alerts, HTML-content]
related: [Dynamic-Alerts, CONCATENATEX, CONTAINSSTRING, HTML-Content-Visual]
---

# Alerts in Action: Integrating Custom Alerts in Power BI

## Source

- **Article:** "Alerts in Action: Powering Real-Time Insights by Integrating Custom Alerts in Power BI"
- **Author:** [[Author-Isabelle-Bittar|Isabelle Bittar]]
- **Published:** 2024-03-15 (date extracted from source metadata)
- **Source URL:** Medium / Microsoft Power BI publication
- **PBIX:** Available for download from article

## Summary

The article builds a COVID-19 WHO regional alerts dashboard demonstrating how to create an interactive alert system in Power BI using:
- The **HTML Content** custom visual to render dynamic icons and formatted alert messages.
- `CONCATENATEX` to generate an HTML list of regions exceeding a threshold.
- `CONTAINSSTRING` to toggle between alert and clear icons.
- `CALCULATE + FILTER` to identify regions with metrics above the alert threshold.

## Key Extracts

### The Alert Pattern
1. Create a DAX measure that returns HTML with an `<li>` element per region above threshold.
2. Assign the measure to the HTML Content visual's text field.
3. Create a second measure that checks whether the HTML list is empty using `CONTAINSSTRING`.
4. Use the boolean result to switch between alert (red) and clear (green) Font Awesome icons.

### WHO Regional Alert Example
```dax
Alert Regions =
    CONCATENATEX(
        FILTER(ALLSELECTED('WHO Regions'[Region]), [Cases] > [Alert Threshold]),
        "<li>" & 'WHO Regions'[Region] & " (" & FORMAT([Cases], "#,##0") & " cases)</li>",
        ""
    )
```

### Key Design Insight
> "The alert system should tell users *where* the problem is, not just *that* a problem exists."

## Knowledge Notes Derived From This Source

- [[Dynamic-Alerts]] — the full pattern note
- [[CONCATENATEX]] — building the HTML list
- [[CONTAINSSTRING]] — detecting alert state
- [[HTML-Content-Visual]] — Font Awesome icon rendering
- [[SWITCH]] — extending with multiple alert levels

## Notes

- The WHO COVID data example is specific, but the pattern transfers to any domain (sales alerts, inventory alerts, performance alerts).
- The article also covers formatting the alert card with conditional color borders — similar to the [[Process-Tracker-Dynamic-Fill]] shape-coloring approach.
