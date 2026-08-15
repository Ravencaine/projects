---
title: "🔄 Incremental Refresh in Power BI — Explained Simply"
source: "https://medium.com/write-your-world/incremental-refresh-in-power-bi-explained-simply-9d2f341ab5af"
author:
  - "[[Anurodh Kumar]]"
published: 2025-06-16
created: 2026-08-12
description: "More"
Processed: "Unprocessed"
---
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*b0qvqAY1HJaB9nrcCDd9EA.png)

image by Anurodh Kumar

Incremental Refresh in Power BI allows you to refresh only new or changed data instead of the entire dataset every time. This is especially useful for large datasets — it saves time, reduces load on the data source, and speeds up the refresh process.

## ✅ Why Use Incremental Refresh?

- ⚡ Faster refreshes for large datasets
- 💾 Reduces resource consumption
- ⏱️ Avoids reloading historical data
- 🧠 Optimized performance in the Power BI Service

## 🧱 How It Works

Power BI splits your data into:

- Historical data (doesn’t change — refreshed only once)
- Incremental data (recent data — refreshed regularly)

You define this using Date/Time columns and set:

- Range of historical data (e.g., 5 years)
- How much recent data to refresh (e.g., last 5 days)

## 🔧 How to Set Up Incremental Refresh

1. Go to Power BI Desktop
2. Use Power Query to filter data using a Date/Time column
3. Create RangeStart and RangeEnd parameters
4. Apply those filters to your data
5. In Model view → Table → Incremental Refresh, define:
6. Publish to Power BI Service (only then incremental refresh works!)

## 💡 Licensing Requirements

- 🔒 Requires Power BI Pro with Premium workspace
- In Premium per user (PPU) or Premium capacity, incremental refresh is supported