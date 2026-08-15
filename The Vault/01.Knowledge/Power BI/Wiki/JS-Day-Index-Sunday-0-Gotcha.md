---
created: 2026-08-11
updated: 2026-08-11
source: How I Built a Calendar Heatmap in Power BI with Plotly.js.md
note_type: gotcha
tags: [javascript, plotly, heatmap, timezone]
---

# JS getDay() Returns Sunday = 0

JavaScript's `Date.getDay()` returns 0 for Sunday, not 1. Failing to account for this causes the entire Sunday column to map to row index 0 in the heatmap matrix — overwriting Monday's values.

## Expected Behaviour

Day index should be Monday=1, Tuesday=2, …, Sunday=7 — matching the heatmap's y-axis array `['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']`.

## Actual Behaviour

```javascript
// Without the fix:
new Date('2026-08-09').getDay();  // returns 0 (Sunday)

// Using getDay() directly as array index:
z[0][week-1] = row.value;  // places Sunday's value in the Monday row
```

## Why It Happens

JavaScript's `Date.prototype.getDay()` follows the POSIX convention: Sunday is 0, Monday is 1, …, Saturday is 6.

The heatmap y-axis expects Monday at index 0, so Sunday's `getDay() = 0` incorrectly targets the Monday slot.

## How to Handle It

Always remap Sunday from 0 to 7:

```javascript
function getDayNumber(date) {
    let d = new Date(date);
    let day = d.getDay();
    return day === 0 ? 7 : day;  // Sunday=0 → Sunday=7
}

// Then use: z[day-1][week-1] = row.value;
```

## Related Gotchas

- JavaScript `Date` constructor parses `"yyyy-mm-dd"` as UTC; if your DAX `FORMAT` uses local time, dates near midnight may shift by one day. Use explicit `new Date(year, month-1, day)` or normalize to UTC consistently.
