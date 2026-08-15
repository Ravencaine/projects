---
created: 2026-08-11
updated: 2026-08-11
source: How I Built a Calendar Heatmap in Power BI with Plotly.js.md
note_type: workflow
tags: [powerbi, plotly, heatmap, html-content, visualization, tutorial]
---

# Build Calendar Heatmap in Power BI

Step-by-step workflow to create a GitHub-style calendar heatmap using the HTML Content visual and Plotly.js.

## Prerequisites

- Power BI Desktop
- HTML Content visual installed (AppSource: HTML Content by BV)
- A date table with at least `Date` (date) and `Value` (numeric) columns

## Steps

### 1 — Prepare the data table

Ensure you have a date table that covers the full year you want to visualize, with a numeric column representing daily activity.

```
calendar_3years_2022_2024[Date]  →  date
calendar_3years_2022_2024[Value]  →  numeric measure
```

### 2 — Create the DAX measure

Create a new measure on any table (or create a dedicated measure table):

```dax
GitHub Heatmap HTML =

VAR JsonData =
    CONCATENATEX(
        calendar_3years_2022_2024,
        "{date:'" & FORMAT(calendar_3years_2022_2024[Date], "yyyy-mm-dd") & "',value:" & calendar_3years_2022_2024[Value] & "}",
        ","
    )

RETURN
"
<!-- Container -->
<div id='heatmap' style='width:100%;height:450px;'></div>

<script>
(function(){

    function loadPlotly(callback){
        if(typeof Plotly !== 'undefined'){ callback(); }
        else {
            var script = document.createElement('script');
            script.src = 'https://cdn.plot.ly/plotly-2.27.0.min.js';
            script.onload = callback;
            document.head.appendChild(script);
        }
    }

    loadPlotly(function(){
        var rawData = [" & JsonData & "];

        function getISOWeek(date) {
            const d = new Date(date);
            d.setHours(0,0,0,0);
            d.setDate(d.getDate() + 3 - (d.getDay() + 6) % 7);
            const week1 = new Date(d.getFullYear(),0,4);
            return 1 + Math.round(((d - week1) / 86400000 - 3 + (week1.getDay() + 6) % 7) / 7);
        }

        function getDayNumber(date){
            let d = new Date(date);
            let day = d.getDay();
            return day === 0 ? 7 : day;
        }

        var weeks = 53;
        var days = 7;
        var z = Array.from({length: days}, () => Array(weeks).fill(null));

        rawData.forEach(row => {
            var week = getISOWeek(row.date);
            var day = getDayNumber(row.date);
            z[day-1][week-1] = row.value;
        });

        var trace = {
            type: 'heatmap',
            z: z,
            x: Array.from({length: weeks},(_,i)=>i+1),
            y: ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'],
            colorscale: 'Viridis',
            hovertemplate: '<b>Week %{x}</b><br>%{y}<br>Value %{z}<extra></extra>',
            colorbar: { title: 'Activity' }
        };

        var layout = {
            title: 'GitHub-Style Calendar Heatmap',
            xaxis: { title: 'Week Number', side:'bottom' },
            yaxis: { title: '', autorange:'reversed' },
            height: 400
        };

        Plotly.newPlot('heatmap',[trace],layout);
    });

})();
</script>
"
```

### 3 — Add the HTML Content visual

1. Add the **HTML Content** visual to your report canvas
2. Drag the `GitHub Heatmap HTML` measure into the **Values** field
3. Resize and position the visual as desired

### 4 — Verify interactivity

- Hover over any cell to see week number, day name, and value via the custom tooltip
- The visual responds to Power BI slicers (filter context flows into the measure)
- Change the `colorscale` value in the JS to experiment with palettes

## Variations

| Variation | Change |
|-----------|--------|
| Multi-year heatmap | Add more rows to the source date table; matrix still 7×53 |
| Custom colors | Replace `'Viridis'` with `'Blues'`, `'RdYlGn'`, or custom colorscale array |
| Filtered view | Add a slicer and ensure the measure respects filter context |
| Larger cells | Increase `height` in `layout` and `style` height on the container div |

## Common Errors

- [[JS-Day-Index-Sunday-0-Gotcha]] — JavaScript `getDay()` returns Sunday=0; forgetting this causes all Sunday data to map to array index 0, overwriting Monday

## Related

- [[Calendar-Heatmap-Plotly-Power-BI]] — `pattern`
- [[GitHub-Heatmap-DAX-HTML-Snippet]] — `snippet`
- [[JS-Day-Index-Sunday-0-Gotcha]] — `gotcha`
