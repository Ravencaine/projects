---
created: 2026-08-11
source: How I Built a Calendar Heatmap in Power BI with Plotly.js.md
note_type: snippet
tags: [javascript, date-math, iso-week, calendar, plotly]
---

# getISOWeek — JavaScript ISO Week Number

Returns the ISO 8601 week number (1–53) for a given date. Used to map calendar dates to the horizontal axis of a calendar heatmap.

## Code

```javascript
function getISOWeek(date) {
    const d = new Date(date);
    d.setHours(0, 0, 0, 0);          // normalise to midnight
    d.setDate(d.getDate() + 3 - (d.getDay() + 6) % 7);  // find Thursday of this week
    const week1 = new Date(d.getFullYear(), 0, 4);       // Jan 4 is always in week 1
    return 1 + Math.round(
        (d - week1) / 86400000 - 3 + (week1.getDay() + 6) % 7
    ) / 7;
}
```

## When to Use

- Calendar heatmaps where the x-axis represents ISO week numbers (Mon–Sun weeks)
- Any visualization that needs week-relative positioning from raw dates
- Aligning Power BI date data with GitHub-style activity grids

## How It Works

| Step | What it does |
|------|-------------|
| `setHours(0,0,0,0)` | Removes time-of-day noise |
| `d.getDay() + 6) % 7` | Converts Sunday=0 to Mon=0, ..., Sat=5 mapping |
| Move to Thursday | ISO weeks start on Monday; week 1 contains the first Thursday |
| Jan 4 rule | ISO 8601 guarantees Jan 4 is always in week 1 |
| Round / divide by 7 | Converts day offset to week number |

## Related

- [[getDayNumber-JavaScript]] — weekday index mapping (Sunday=0 → Monday=1 ... Sunday=7)
- [[GitHub-Style-Calendar-Heatmap-Pattern]] — both functions used together in the heatmap matrix
