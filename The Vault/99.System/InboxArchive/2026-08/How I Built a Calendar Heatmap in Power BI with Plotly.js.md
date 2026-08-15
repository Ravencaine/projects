---
title: "How I Built a Calendar Heatmap in Power BI with Plotly.js"
source: "https://medium.com/microsoft-power-bi/how-i-built-a-github-style-calendar-heatmap-in-power-bi-c602c6d98454"
author:
  - "[[Esther]]"
published: 2026-04-02
created: 2026-08-09
description: "Plotly.js chart Changed How I Look at Data"
Processed: "Unprocessed"
---
## Plotly.js chart Changed How I Look at Data

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*FPVFmhZYl3Pgd7lonTlBTQ.png)

Plotly.js in Power BI — image by Author

I’ve always liked how GitHub visualizes activity. That simple grid of colored squares somehow tells a story instantly — when you were productive, when things slowed down, and where patterns start to emerge without forcing you to dig through numbers.

So I decided to recreate that experience inside Power BI.

What you see in the image above is my own implementation of a **GitHub-style calendar heatmap**, built using a mix of DAX, HTML, JavaScript, and Plotly.

**🎁** [**Get friend links for all of our 1500> Power BI learning articles here**](https://powerbi-masterclass.short.gy/learning-database?utm_source=medium&utm_medium=medium-post&utm_campaign=database-medium-post-start) **🎁**

## What I see when I look at this chart

At first glance, it’s just a grid. But once you understand the structure, it becomes surprisingly expressive.

- Along the bottom, I mapped **week numbers**, covering the full year.
- On the left, you see the **days of the week**, from Monday to Sunday.
- Each square represents a **single day**, and the color reflects how “active” that day was.

I used the **Viridis color scale**, which I’ve grown to appreciate because it’s both readable and visually balanced:

- Darker purple tones signal quieter days
- Greens and yellows highlight spikes in activity

What I like most is that I don’t need exact values anymore. I can *feel* the data.

## The story hidden in the colors

When I step back and look at the full heatmap, a few things immediately stand out to me:

- The **beginning of the year** feels energetic — lots of brighter colors, more consistency.
- Then there’s a noticeable **dip in the middle**, where darker tones take over. That’s a signal I wouldn’t catch as quickly in a table.
- Toward the **end of the year**, things become uneven — a mix of highs and lows, less predictable.

This is exactly why I built it. Not for decoration, but for **pattern recognition**.

## Why I didn’t settle for native visuals

Power BI is great, but it doesn’t natively support this type of calendar heatmap in a flexible way.

I had two options:

- Settle for something “close enough”
- Or build exactly what I want

## 🛠️How I created it — step by step

### Step 1 — Turning data into something JavaScript code

I started in DAX by reshaping my dataset into a JSON-like structure:

```c
VAR JsonData =
    CONCATENATEX(
        calendar_3years_2022_2024,
        "{date:'" &
        FORMAT(calendar_3years_2022_2024[Date], "yyyy-mm-dd") &
        "',value:" &
        calendar_3years_2022_2024[Value] &
        "}",
        ","
    )
```

This was the bridge between Power BI and the web world.

I load Plotly dynamically from a CDN, which makes the solution self-contained and ensures it works reliably inside the Power BI HTML Content visual.

### Step 2 — Making time “grid-friendly”

JavaScript doesn’t think in weeks the way we need here, so I had to explicitly calculate:

- The **ISO week number**
- The **day index (Monday → Sunday)**

That step is critical — without it, the heatmap falls apart.

### Step 3 — Building the matrix

I created a 7×53 structure — one row per weekday, one column per week:

```c
var z =
    Array.from({length: days},
        () => Array(weeks).fill(null)
    );
```

Then I filled it with values, placing each day exactly where it belongs.

This is where the visualization really takes shape.

### Step 4 — Letting Plotly do its thing

Finally, I used Plotly to render everything:

```c
var trace = {
    type: 'heatmap',
    z: z,
    x: Array.from({length: weeks},(_,i)=>i+1),
    y: [
        'Monday','Tuesday','Wednesday',
        'Thursday','Friday','Saturday','Sunday'
    ],
    colorscale: 'Viridis' //Blues, Reds or RdYlGn or many more
};
```
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*1Jxh4rCczZq4ktQNqAomvg.png)

Blues Colorscales — image by Author

I chose the Viridis color scale because it’s clean and perceptually balanced, but it can easily be replaced with other palettes depending on your needs. For example, you might use *Blues* for a softer, more minimal look, *RdYlGn* to clearly highlight low vs. high values, or even a custom color scale to match your company’s branding.

And just like that — the data became something I could actually *read* at a glance.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*heljmgRlbNyKXf17j9pJUg.gif)

Plotly.js heatmap and Power BI slicers

Full code:

```c
GitHub Heatmap HTML = 

// Convert the table into a JSON-like string that JavaScript can read
VAR JsonData =
    CONCATENATEX(
        calendar_3years_2022_2024,
        "{date:'" &
        FORMAT(calendar_3years_2022_2024[Date], "yyyy-mm-dd") &
        "',value:" &
        calendar_3years_2022_2024[Value] &
        "}",
        ","
    )

RETURN
"
<!-- Container where the heatmap will be rendered -->
<div id='heatmap' style='width:100%;height:450px;'></div>

<script>

(function(){

    // Load Plotly dynamically (only if it's not already loaded)
    function loadPlotly(callback){
        if(typeof Plotly !== 'undefined'){
            callback(); // Plotly already available → run immediately
        } else {
            var script = document.createElement('script');
            script.src = 'https://cdn.plot.ly/plotly-2.27.0.min.js'; //cdn
            script.onload = callback; // Run after loading
            document.head.appendChild(script);
        }
    }

    // Wait until Plotly is ready before executing the chart code
    loadPlotly(function(){

        // Inject DAX-generated data into JavaScript
        var rawData = [" & JsonData & "];

        // Convert a date into ISO week number (1–53)
        function getISOWeek(date) {
            const d = new Date(date);
            d.setHours(0,0,0,0);
            d.setDate(d.getDate() + 3 - (d.getDay() + 6) % 7);
            const week1 = new Date(d.getFullYear(),0,4);
            return 1 + Math.round(((d - week1) / 86400000
                   - 3 + (week1.getDay() + 6) % 7) / 7);
        }

        // Convert JavaScript day (Sunday=0) → Monday=1 ... Sunday=7
        function getDayNumber(date){
            let d = new Date(date);
            let day = d.getDay();
            return day === 0 ? 7 : day;
        }

        var weeks = 53; // Maximum number of weeks in a year
        var days = 7;   // Days of the week

        // Create empty 7x53 matrix (rows = days, columns = weeks)
        var z =
            Array.from({length: days},
                () => Array(weeks).fill(null)
            );

        // Fill matrix with values from dataset
        rawData.forEach(row => {
            var week = getISOWeek(row.date); // Get week index
            var day = getDayNumber(row.date); // Get day index
            z[day-1][week-1] = row.value; // Place value into correct cell
        });

        // Define the heatmap
        var trace = {
            type: 'heatmap',
            z: z, // Data matrix
            x: Array.from({length: weeks},(_,i)=>i+1), // Week numbers
            y: [
                'Monday','Tuesday','Wednesday',
                'Thursday','Friday','Saturday','Sunday'
            ],
            // Color scale can be changed:
            // 'Viridis', 'Blues', 'Cividis', 'RdYlGn', or custom palettes
            colorscale: 'Viridis',

            // Tooltip content when hovering over a cell
            hovertemplate:
                '<b>Week %{x}</b><br>%{y}<br>Value %{z}<extra></extra>',

            // Color legend
            colorbar: { title: 'Activity' }
        };

        // Layout settings
        var layout = {
            title: 'GitHub-Style Calendar Heatmap',
            xaxis: { title: 'Week Number', side:'bottom' },
            yaxis: { title: '', autorange:'reversed' }, // Monday on top
            height: 400
        };

        // Render the chart inside the 'heatmap' div
        Plotly.newPlot('heatmap',[trace],layout);

    });

})();

</script>
"
```

## What this changed for me

Before building this, I mostly relied on:

- Line charts
- Tables
- Standard KPIs

This heatmap does.

It shows:

- consistency vs. randomness
- strong periods vs. weak ones
- habits, not just outcomes

And honestly, once you start seeing your data this way, it’s hard to go back.

## ⚡If you’re thinking about building one

Think about:

- What “activity” means in your context
- What patterns you’re trying to uncover
- Whether daily granularity actually matters

I think this type of visualization only becomes powerful when it answers a real question.

**💡** [**MUST TRY — Power BI GPT — Personal Power BI Learning Coach**](https://powerbi-masterclass.short.gy/pbi-gpt?utm_source=medium&utm_campaign=pbi-gpt-medium-post-end) **💡**

> Don’t forget to subscribe to
> 
> 👉 [Power BI Publication](https://powerbi-masterclass.short.gy/publication?utm_source=medium&utm_medium=medium-post&utm_campaign=publication-medium-post-end)
> 
> 👉 [Power BI Newsletter](https://powerbi-masterclass.short.gy/newsletter-medium?utm_source=medium&utm_medium=medium-post&utm_campaign=newsletter-medium-medium-post-end)
> 
> and join our Power BI community:

## [Microsoft Power BI Masterclass | Linktree](https://linktr.ee/powerbi.masterclass?utm_source=medium&utm_medium=medium-post&utm_campaign=linktree-medium-post-end&source=post_page-----c602c6d98454---------------------------------------)

### Let’s share our Microsoft Power BI experience. Learn together. Grow together.

linktr.ee

**Power BI Masterclass Article Classification**

**Level:** Intermediate

**Category:** Data Visualization

**Tags:** Tutorial, Data Visualization