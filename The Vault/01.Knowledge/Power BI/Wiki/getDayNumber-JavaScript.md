---
created: 2026-08-11
source: How I Built a Calendar Heatmap in Power BI with Plotly.js.md
note_type: snippet
tags: [javascript, date-math, weekday, calendar]
---

# getDayNumber — JavaScript Weekday Index

Maps a JavaScript `Date.getDay()` (Sunday=0 ... Saturday=6) to ISO Monday=1 ... Sunday=7 for calendar heatmap matrix indexing.

## Code

```javascript
function getDayNumber(date) {
    let day = new Date(date).getDay();
    return day === 0 ? 7 : day;   // Sunday → 7, Mon → 1 ... Sat → 6
}
```

## When to Use

- Building a 7-row heatmap matrix where row 0 = Monday and row 6 = Sunday (GitHub convention)
- Any calendar grid where you need consistent Monday-first weekday ordering

## Why Sunday Remaps to 7

| JS getDay() | Standard | GitHub / ISO Heatmap |
|-------------|----------|----------------------|
| 0 | Sunday | 7 (last row) |
| 1 | Monday | 1 (first row) |
| 2 | Tuesday | 2 |
| ... | ... | ... |
| 6 | Saturday | 6 |

Plotting `z[0]` as Monday requires the Monday=1 mapping. Without the remap, Sunday (0) would fall at index -1, producing a hole in the first column.

## Related

- [[getISOWeek-JavaScript]] — maps dates to week numbers (columns of the heatmap)
- [[GitHub-Style-Calendar-Heatmap-Pattern]] — both functions used together
