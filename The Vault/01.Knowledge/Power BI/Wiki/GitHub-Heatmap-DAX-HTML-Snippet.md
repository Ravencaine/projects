---
created: 2026-08-11
updated: 2026-08-11
source: How I Built a Calendar Heatmap in Power BI with Plotly.js.md
note_type: snippet
tags: [powerbi, plotly, heatmap, html-content, dax]
---

# GitHub Heatmap — Full DAX Measure

Copy-paste DAX measure for a GitHub-style calendar heatmap in the HTML Content visual.

## Code

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

    // Load Plotly from CDN if not already present
    function loadPlotly(callback){
        if(typeof Plotly !== 'undefined'){
            callback();
        } else {
            var script = document.createElement('script');
            script.src = 'https://cdn.plot.ly/plotly-2.27.0.min.js';
            script.onload = callback;
            document.head.appendChild(script);
        }
    }

    loadPlotly(function(){

        var rawData = [" & JsonData & "];

        // ISO week number 1-53
        function getISOWeek(date) {
            const d = new Date(date);
            d.setHours(0,0,0,0);
            d.setDate(d.getDate() + 3 - (d.getDay() + 6) % 7);
            const week1 = new Date(d.getFullYear(),0,4);
            return 1 + Math.round(((d - week1) / 86400000 - 3 + (week1.getDay() + 6) % 7) / 7);
        }

        // Monday=1, ..., Sunday=7
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

## When to Use

- Visualize daily activity or events over a full year in a compact grid
- Replace a line chart or table when pattern recognition (not precise values) is the goal
- Requires: HTML Content visual (by HTML Content by BV

Configure the measure in the HTML Content visual's **Values** field.

## Variations

- Swap `colorscale: 'Viridis'` for `'Blues'`, `'RdYlGn'`, or a custom array
- Change `height: 400` and container `style='height:450px'` to resize
- Replace `calendar_3years_2022_2024` with your own date+value table

## Related

- [[Calendar-Heatmap-Plotly-Power-BI]] — `pattern`
- [[Build-Calendar-Heatmap-Power-BI]] — `workflow`
- [[JS-Day-Index-Sunday-0-Gotcha]] — `gotcha`
