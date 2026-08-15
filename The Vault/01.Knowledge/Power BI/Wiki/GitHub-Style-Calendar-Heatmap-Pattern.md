---
created: 2026-08-11
source: How I Built a Calendar Heatmap in Power BI with Plotly.js.md
note_type: pattern
tags: [power-bi, data-visualization, plotly, html-content, calendar, heatmap]
---

# GitHub-Style Calendar Heatmap Pattern

Combines DAX + HTML Content visual + Plotly.js to render a GitHub-style calendar heatmap — week columns × weekday rows, colored by activity intensity.

## Purpose

Power BI has no native calendar heatmap visual. This pattern bridges DAX data generation, JavaScript date math, and Plotly heatmap rendering inside the HTML Content visual to produce a fully interactive, slicer-responsive heatmap.

## Components

1. **CONCATENATEX** — serialises a date table into a JSON string passed into HTML Content
2. **HTML Content visual** — hosts the Plotly.js chart
3. **Plotly CDN loader** — dynamic `<script>` injection for self-contained deployment
4. **JavaScript ISO week algorithm** — maps dates to 7×53 grid coordinates
5. **Plotly heatmap trace** — renders the matrix as a colour-coded grid

## Structure

### DAX — JSON Bridge Measure

```dax
GitHub Heatmap HTML =
VAR JsonData =
    CONCATENATEX(
        calendar_3years_2022_2024,
        "{date:'" &
        FORMAT( calendar_3years_2022_2024[Date], "yyyy-mm-dd" ) &
        "',value:" &
        calendar_3years_2022_2024[Value] &
        "}",
        ","
    )
RETURN
"
<!-- Container -->
<div id='heatmap' style='width:100%;height:450px;'></div>

<script>
(function(){
    function loadPlotly(callback){
        if (typeof Plotly !== 'undefined') { callback(); }
        else {
            var s = document.createElement('script');
            s.src = 'https://cdn.plot.ly/plotly-2.27.0.min.js';
            s.onload = callback;
            document.head.appendChild(s);
        }
    }

    loadPlotly(function(){
        var rawData = [" & JsonData & "];

        function getISOWeek(date) {
            const d = new Date(date);
            d.setHours(0,0,0,0);
            d.setDate(d.getDate() + 3 - (d.getDay() + 6) % 7);
            const week1 = new Date(d.getFullYear(), 0, 4);
            return 1 + Math.round(((d - week1) / 86400000
                   - 3 + (week1.getDay() + 6) % 7) / 7);
        }

        function getDayNumber(date) {
            let day = new Date(date).getDay();
            return day === 0 ? 7 : day;  // Sunday=7, Mon=1 ... Sat=6
        }

        var weeks = 53, days = 7;
        var z = Array.from({length: days}, () => Array(weeks).fill(null));

        rawData.forEach(row => {
            z[ getDayNumber(row.date) - 1 ][ getISOWeek(row.date) - 1 ] = row.value;
        });

        var trace = {
            type: 'heatmap',
            z: z,
            x: Array.from({length: weeks}, (_,i) => i + 1),
            y: ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'],
            colorscale: 'Viridis',  // swap for Blues, RdYlGn, Cividis
            hovertemplate: '<b>Week %{x}</b><br>%{y}<br>Value %{z}<extra></extra>',
            colorbar: { title: 'Activity' }
        };

        var layout = {
            title: 'GitHub-Style Calendar Heatmap',
            xaxis: { title: 'Week Number', side: 'bottom' },
            yaxis: { title: '', autorange: 'reversed' },  // Monday on top
            height: 400
        };

        Plotly.newPlot('heatmap', [trace], layout);
    });
})();
</script>
"
```

## Example

1. Create a date table with `Date` and `Value` columns (e.g., sales per day).
2. Add the HTML Content visual to the canvas.
3. Drop the `GitHub Heatmap HTML` measure into the visual.
4. Plotly renders the 7×53 heatmap. Slicers on the date table filter the data dynamically.

## Variations

- **Color scales:** `Viridis` (default), `Blues`, `RdYlGn`, `Cividis`, or custom RGB arrays
- **Y-axis order:** `autorange: 'reversed'` puts Monday at the top (matches GitHub); remove for Sunday-at-top
- **Tooltip format:** customise `hovertemplate` for currency, dates, percentage formats
- **Dynamic title:** inject DAX measure values into the `layout.title` string via JS interpolation

## Related

- [[Dynamic-Alerts]] — same CONCATENATEX + HTML Content pattern, different JS output
- [[Source-Alerts-in-Action]] — HTML Content visual pattern in practice
