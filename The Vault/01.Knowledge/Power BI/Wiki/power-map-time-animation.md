---


title: "Power Map Time Animation"
created: 2026-07-28
updated: 2026-08-02
tags: [power-bi, power-map, pattern]
note_type: pattern
description: "Power Map time animation — unpivoting data, setting a time field, playing the timeline, scene duration. From Dunlop European unemployment exercise."


source: "[[beginning-big-data-with-power-bi-and-excel-2013-dunlop|Beginning Big Data with Power BI and Excel 2013]]"

---

# Power Map: Time Animation

Power Map can animate data changes over time by setting a **time field**.

## Data Requirement: Unpivot

Time animation requires data in a **long format**: one row per location per time period:

| Country | Year | Unemployment |
|---------|------|-------------|
| Germany | 2010 | 7.0 |
| Germany | 2011 | 6.0 |
| Germany | 2012 | 5.5 |

If data is in wide format (one column per year), use Power Query **Unpivot Columns** to transform it.

## Setting Up Time Animation

1. In Power Map, select a **numeric field** for the height/size
2. Set aggregation to **No aggregation** (each row represents one observation)
3. Right-click the time/year field → **Set as Time**
4. A time control bar appears at the bottom
5. Click **Play** to animate through time periods

## Scene Duration

Adjust scene duration in:
```
Gear icon → Scene options → Duration time
```

Use the **Speed slider** at the bottom to control transition speed.

## Source Reference

Chapter 9, Exercise 9-4, *Beginning Big Data with Power BI and Excel 2013* (Dunlop, Apress 2015).
