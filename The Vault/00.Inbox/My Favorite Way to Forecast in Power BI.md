---
title: "💡My Favorite Way to Forecast in Power BI"
source: "https://medium.com/the-bi-corner/my-favorite-way-to-forecast-in-power-bi-634d1221df24"
author:
  - "[[Isabelle Bittar]]"
published: 2025-06-25
created: 2026-08-04
description: "How I used Power Query and Python to build a reusable, customizable forecasting model — no Premium needed"
Processed: "Unprocessed"
---
## How I used Power Query and Python to build a reusable, customizable forecasting model — no Premium needed

![](99.System/Attachments/1!YrrH_wdjkNKRfstXim3heg.png.webp)

By Isabelle Bittar for KI Data Science

🎁 *PBIX included at the end of this article!*

### Introduction

So there are many approaches you can use to do forecasting in Power BI. You can leverage other Microsoft Fabric products you connect with in Power BI, you can use some of the advanced capabilities of native Power BI visuals (such as the line chart).

In the following article, I’ll demonstrate how you can create your forecast directly in **Power Query using Python**, and then visualize the results using **any of Power BI’s native visuals** — not just the default line chart. This also gives you access to the **underlying forecast values**, including confidence intervals, for further breakdown, export (yes, even to Excel 😅), or deeper analysis.

You can view here a short demo I made for the Power BI visual shared in the cover picture of this article!

But before diving in, let’s look at the main forecasting options available in Power BI and what trade-offs they come with:

![](99.System/Attachments/1!Z4wOo3S8njp0jr-qVrK1-w.png.webp)

Overview of Different Approaches to Forecasting in Power BI

In this example, I forecasted **employee turnover** across different departments in an organization for the next 12 months based on historical values and seasonality, using the **Holt-Winters Exponential Smoothing** method.

### Step 1 — Load Initial Data Table and Create Python Script in Power Query

📥 Loading the Initial Table

I started with monthly observations of each department’s **headcount** and **number of terminations**, which I loaded into Power Query.

![](99.System/Attachments/1!ZHT9zu3TFcYCViJGZmpfxA.png.webp)

Initial Data Table Loaded in Power Query

Once my dataset was loaded, I selected **“Run Python script”** from the *Transform* tab. The Python script dialog box then opened.

![](99.System/Attachments/1!d-bkSrWD4oCgIpilJ9gmPA.png.webp)

Opening the Python Script Dialogue Box in Power Query

### 🧠 Creating the Forecast

In the dialog box, I inserted the following script, which loops through each department and forecasts turnover for the next 12 months based on seasonal patterns:

Here, I basically inserted the following code:

```c
import pandas as pd
from statsmodels.tsa.holtwinters import ExponentialSmoothing

df = dataset.copy()
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df = df.dropna(subset=['Date'])

forecast_frames = []

for dept in df['Department'].unique():
    temp = df[df['Department'] == dept].sort_values('Date')

    if len(temp) >= 12:
        model = ExponentialSmoothing(
            temp['TurnoverRate'],
            trend='add',
            seasonal='add',
            seasonal_periods=12
        )
        fit = model.fit()

        # Forecast 12 months ahead
        forecast = fit.forecast(12)
        future_dates = pd.date_range(temp['Date'].max() + pd.DateOffset(months=1), periods=12, freq='M')

        forecast_df = pd.DataFrame({
            'Date': future_dates,
            'TurnoverRate': forecast.values,
            'Department': dept,
            'Forecast': True
        })

        forecast_df['Headcount'] = None
        forecast_df['Terminations'] = None

        # Historical data
        original = temp[['Date', 'TurnoverRate', 'Headcount', 'Terminations']].copy()
        original['Department'] = dept
        original['Forecast'] = False

        all_df = pd.concat([original, forecast_df])
        forecast_frames.append(all_df)

result = pd.concat(forecast_frames)
```

### 🔍 What This Python Script Does (in Simple Terms)

This script takes historical turnover rate data by department and applies the **Holt-Winters Exponential Smoothing** method to forecast the next 12 months. It’s designed to detect both **trends** (long-term increases or decreases) and **seasonality** (recurring patterns, like yearly cycles in employee turnover).

There are many forecasting algorithms out there — like **ARIMA**, **Prophet**, or **machine learning regressors** — each with their strengths. I chose Holt-Winters because it’s particularly well-suited for **time series with seasonality**, it’s **quick to implement**, and works well with **smaller datasets**, which is often the case in department-level HR reporting.

The script loops through each department, builds a model (if there’s at least 12 months of data), and generates a 12-month forecast. It then merges the forecasted values with the historical ones into a single table, flagging each row as either actual or forecasted — so you can easily visualize and compare them in Power BI.

Once I clicked OK, it then gave me the following tables as a result of my script:

![](99.System/Attachments/1!izaEJItSmOtU9UJb7bj2iQ.png.webp)

Tables Resulting from Python Script in Power Query

### Step 2 — Expand and Clean the Python Output

Power Query then prompted me to expand the Python output. I selected the following columns from the resulting table:

- `Date`
- `TurnoverRate`
- `Department`
- `Forecast`
- `Headcount`
- `Terminations`

These give me everything I need to visualize both **historical** and **forecasted** turnover rates per department, while still keeping the context for later calculations (like company-wide turnover or total terminations).

I also set the appropriate data types and removed any helper columns like `"Name"` that Power Query sometimes includes automatically.

### Step 3 — Work With the Results in Power BI

With this setup, I can now easily:

- Filter to show only forecasted or actual values
- Visualize department-level trends using any visual, not just line charts
- Create calculated measures to customize visualizations
- Export everything to Excel if needed (my clients always ask for this 😅)

This approach gives me a clean, flexible dataset that fits perfectly into my Power BI model.

In my case, once loaded into the Power BI data model, I started building visualizations based on what users on this project needed:

- A focused view of the **last 3 months + the next 12 months** forecasted
![](99.System/Attachments/1!1Wah_dYBuR0afkmeh6Gn3Q.png.webp)

Focused View of the Last 3 Months + 12 Months Forecasted in Power BI

- A full view of **all historical values** for trend analysis
![](99.System/Attachments/1!auYAAmqx2hChztxDRgVcAg.png.webp)

Full View of All Historical Values for Trend Analysis in Power BI

- A department-level **summary of anticipated turnover by year-end**, along with expected headcount
![](99.System/Attachments/1!22tCtJA5-rjJZ5w_XyGI8g.png.webp)

Summary View of Anticipated Turnover by Year-End with Expected Headcount in Power BI

You can view my PBIX file to see the detailed DAX calculations and visuals used to develop these different views.

### Why I Like This Approach

✅ **I can use whatever visuals I want**, instead of being locked into a single forecasting visual.

✅ **I get full access to the forecasted values**, which means I can compare actual vs. forecast, calculate confidence intervals, or even flag anomalies using DAX.

✅ **It scales**: Once I set up this approach, I can reuse it for multiple KPIs — not just turnover.

✅ **It plays well with others**: Since everything runs through Power Query, I can refresh forecasts whenever the data refreshes.

### Wrapping Up

This is just one of many forecasting techniques you can use in Power BI — but it’s one I personally enjoy. It’s free, lightweight, and easy to implement for most clients without requiring any complex setup. Best of all, it offers full flexibility when it comes to analyzing and visualizing the results.

I’d love to hear from you — have you used this technique before, or do you have a different go-to approach for forecasting in Power BI? Let me know!

**👉As promised,** [**here**](https://drive.google.com/file/d/1tFpxvbgYj4xIkFbj9M5OGh_BlGUDK5p8/view?usp=sharing) **’s the PBIX file with the example visuals and tricks mentioned above.**

Enjoy using Python in Power BI? Here is one of my recent articles sharing tips on building effective Python visuals!

## [Smarter Python Visuals in Power BI: 5 UX Tips for Better Insights](https://medium.com/the-bi-corner/smarter-python-visuals-in-power-bi-5-ux-tips-for-better-insights-a73c6b358e70?source=post_page-----634d1221df24---------------------------------------)

### From violin plots to field parameters — how to make advanced data visuals both beautiful and understandable.

medium.com

## About the Author

Hi 👋 Thanks so much for reading! My name is Isabelle, and I’m an independent business consultant specializing in BI and data science 🤓. I write these articles to share what I learn on real client projects and to help others level up their Power BI and analytics skills.

☕ If you enjoy my articles and want to support me in writing more, you can [**Buy Me a Coffee**](http://buymeacoffee.com/isabittar) — every contribution means a lot and keeps this content going.

### Stay Tuned

Make sure to [**follow me on Medium**](https://medium.com/@isabittar) to access all my articles on advanced techniques in Power BI visualization.

### Connect or Follow Me Here:

- [***Medium***](https://medium.com/@isabittar)
- [***LinkedIn***](https://www.linkedin.com/in/isabelle-bittar-mba-pmp-crha-8427a2bb/)
- [***X***](https://twitter.com/KI_Datascience)