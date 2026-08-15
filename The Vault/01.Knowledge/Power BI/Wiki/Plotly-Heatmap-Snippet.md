---
created: 2026-08-11
source: How I Built a Calendar Heatmap in Power BI with Plotly.js.md
note_type: snippet
tags: [plotly, javascript, heatmap, html-content, cdn]
---

# Plotly.js CDN Loader + Heatmap Trace

Boilerplate for loading Plotly.js from CDN and rendering a heatmap inside the HTML Content visual.

## Code

```javascript
// --- Dynamic CDN loader (self-contained, no npm required) ---
function loadPlotly(callback) {
    if (typeof Plotly !== 'undefined') {
        callback();                         // already loaded
    } else {
        var s = document.createElement('script');
        s.src = 'https://cdn.plot.ly/plotly-2.27.0.min.js';
        s.onload = callback;
        document.head.appendChild(s);
    }
}

// --- Heatmap trace ---
loadPlotly(function() {
    var trace = {
        type: 'heatmap',
        z:    zMatrix,   // 2D array [row][col], rows = days, cols = weeks
        x:    Array.from({length: weeks}, (_, i) => i + 1),
        y:    ['Monday','Tuesday','Wednesday',
               'Thursday','Friday','Saturday','Sunday'],
        colorscale: 'Viridis',   // Blues | RdYlGn | Cividis | custom
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
```

## When to Use

- Inside the HTML Content visual when you need a heatmap that Power BI doesn't natively provide
- GitHub-style activity grids, calendar heatmaps, correlation matrices
- Any case where you want interactivity (hover tooltips, zoom, pan) without building a custom visual

## Variations

```javascript
// Custom colorscale as RGB array
colorscale: [
    [0,    'rgb(255,255,255)'],   // null / zero
    [0.25, 'rgb(230,245,254)'],
    [0.5,  'rgb(115,178,255)'],
    [0.75, 'rgb(41,128,185)'],
    [1,    'rgb(8,81,156)']
]

// Horizontal colorbar
colorbar: { title: 'Activity', orientation: 'h', len: 0.9, y: -0.2 }
```

## Related

- [[GitHub-Style-Calendar-Heatmap-Pattern]] — full pattern with matrix building and DAX bridge
- [[getDayNumber-JavaScript]] — populates the 7×53 matrix used as `z`
