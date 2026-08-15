---
created: 2026-08-09
updated: 2026-08-09
source: "⚡How I Built a Modern Oblique Area Chart in Power BI (Using Only Native Visuals)"
source_url: "https://medium.com/the-bi-corner/how-i-built-a-modern-oblique-area-chart-in-power-bi-using-only-native-visuals-c0986d0c6753"
published: 2025-07-23
note_type: source
tags: [power-bi, dax, visualization, native-visuals, line-chart, area-chart, error-bars, oblique, healthcare, design]
---

# Modern Oblique Area Chart in Power BI (Native Visuals) — Isabelle Bittar / KI Data Science

Source: The BI Corner (Medium). Published 2025-07-23. Author: Isabelle Bittar (BI consultant, KI Data Science) — new author, author note created.

## Summary

Build a modern oblique area chart using only native Power BI visuals — no custom visuals required. Technique layers a PNG background behind a line chart, uses CALCULATE+FILTER to compute Average/Max/Min vitals, and uses Analytics pane error bars as white fill zones above/below the data lines to create the oblique area effect.

## End-to-End Architecture

```
Data model: 'Vital Stats' table
    [Date], [Value], [Measure Type: Average/Max/Min]
         │
         ├── Measures: Average Vital, Max Vital, Min Vital
         │             (CALCULATE + FILTER on Measure Type)
         │
         ├── Max Graph Area / Min Graph Area
         │   (MAXX/MINX + ALL over Date; ±5% buffer)
         │
         └── Line Chart (native)
               ├── X-axis: Date
               ├── Values: Average Vital, Max Vital, Min Vital
               ├── Y-axis min: Min Graph Area (measure)
               ├── Y-axis max: Max Graph Area (measure)
               └── Analytics pane:
                     ├── Error band (Max Vital): Upper=Max Graph Area, Lower=Max Vital → white fill
                     └── Error band (Min Vital): Upper=Min Vital, Lower=Min Graph Area → white fill

Background: PNG (Figma) placed behind chart; chart background turned off
```

## Key Insights Extracted

**DAX Code KB:**
- [[Measure-Type-Filter-Pattern]] — `pattern` — CALCULATE + FILTER on text column Measure Type = "Average/Max/Min"; row context filter inside iteration
- [[MAXX-MINX-ALL-Date-Dynamic-Range]] — `atomic` — MAXX(ALL(table[Date]), [Max Vital]) = ALL over Date removes context so MAXX sees all dates; same for MINX
- [[Dynamic-Graph-Area-Buffer]] — `pattern` — Max+5% and Min-5% create a fixed buffer zone; error bars fill this zone in white
- [[VAR-for-Intermediate-Measure-Calculation]] — `atomic` — VAR stores intermediate result (e.g. _MaxVital); RETURN uses it; keeps complex measures readable

**Power BI KB:**
- [[Error-Bars-White-Fill-Zones]] — `pattern` — Analytics pane error bars with Upper/Lower bounds flipped: Max Vital upper=MaxGraphArea, lower=MaxVital → white fill above the line; Min Vital upper=MinVital, lower=MinGraphArea → white fill below
- [[PNG-Background-Behind-Chart]] — `reference` — Figma or web PNG → Insert Image → placed behind chart → chart background turned off
- [[Dynamic-Y-Axis-Min-Max-via-Measures]] — `reference` — Y-axis min/max fields accept measures; dynamic range driven by MAXX/MINX over ALL dates
- [[Custom-Tooltip-Page-Hidden-Measures]] — `atomic` — separate report page as tooltip → shows only intended fields; hides internal measures like Max/Min Graph Area
- [[Oblique-Area-Chart-Native-Visuals-End-to-End]] — `pattern` — full walkthrough combining all 10 elements above

## Author

- [[Author-Isabelle-Bittar]] — created (1st source)
