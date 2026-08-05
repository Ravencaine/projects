---
title: "🚨 How to Do Anomaly Detection in Power BI (No External Tools Needed!)"
source: "https://medium.com/the-bi-corner/how-to-do-anomaly-detection-in-power-bi-no-external-tools-needed-b12973e58b2b"
author:
  - "[[Isabelle Bittar]]"
published: 2025-08-09
created: 2026-08-04
description: "A hands-on case study using Python and Isolation Forest — run entirely inside Power Query to flag suspicious employee expenses."
Processed: "Unprocessed"
---
## A hands-on case study using Python and Isolation Forest — run entirely inside Power Query to flag suspicious employee expenses.

![](99.System/Attachments/1!UbelLw-InByn2LmA3AeMAQ.png.webp)

By Isabelle Bittar for KI Data Science

**🎁PBIX available at the end of this article!**

### Introduction

Anomaly detection is a powerful technique that helps organizations spot irregular patterns in their data — especially when they’re trying to identify and localize problems early to take corrective action. There are so many practical use cases: flagging suspicious employee timesheets, detecting inventory spikes or drops, monitoring website or app traffic — you name it.

In a recent HR project I worked on, the goal was to catch potentially suspicious employee expenses — think unusually high meal costs, duplicate entries, or charges submitted outside of typical business hours.

For this project, I was working with a log of expense data that included details like the date and time of each transaction, payment method, vendor, and expense category. I used Python inside Power Query to build an anomaly detection model using the Isolation Forest algorithm from `scikit-learn` —a popular machine learning library in Python

Here’s a short demo of the dashboard:

In this article, I’ll walk you through how I built it.

### What Is Anomaly Detection — and Why Isolation Forest?

At its core, **anomaly detection** is about finding data points that stand out from the norm — values or behaviors that don’t follow the expected pattern. These anomalies can signal errors, fraud, or just unusual activity that’s worth a closer look. Depending on the context, anomalies might be rare but important (like a data breach), or they might be subtle patterns that only show up when you look at multiple variables together.

To tackle this, I used a technique called **Isolation Forest**. Unlike traditional models that try to profile what’s “normal” and then look for deviations, Isolation Forest takes a different approach: it tries to isolate anomalies by randomly splitting the data. Since anomalies are few and different, they get isolated much faster than regular points. The algorithm builds a series of decision trees and calculates how many splits it takes to isolate each point — fewer splits usually mean the point is more likely to be an anomaly.

This method made a lot of sense for my project for a few reasons:

- The dataset was relatively small and tabular, with structured fields like vendor, amount, and timestamp.
- I didn’t have labeled examples of “fraudulent” expenses, so I needed an unsupervised approach.
- Isolation Forest works well even when anomalies are subtle or context-specific (like repeated entries at odd hours).

It was lightweight, easy to tune, and a great fit for embedding directly into Power BI through Power Query.

### Setting Up the Data in Power BI

To get started, I had a CSV file of employee expenses that included key fields like:

- Transaction ID
- Date & Time
- Employee Name & Department
- Expense Category & Vendor
- Amount
- Payment Type & Method
![](99.System/Attachments/1!tTSgk_Iob4TIgNUDspf5vQ.png.webp)

Initial Dataset Loaded in Power Query

I loaded this file into Power BI using **Power Query**. After the standard initial steps — like promoting headers and changing data types — I added a **Python script** directly in the query editor to run the anomaly detection.

![](99.System/Attachments/1!cY8PXv6ESHCPzRnbAkOu9g.png.webp)

Running a Python Script in Power Query

### 🐍 Running a Python Script in Power Query

Here’s the full Python script I used, step by step:

```c
# 'dataset' holds the input data for this script
import pandas as pd
from sklearn.ensemble import IsolationForest

# Drop rows with nulls in key fields
df = dataset.dropna(subset=['Amount', 'Category', 'Department', 'PaymentType', 'Time'])

# Convert Time to hour group
def group_hour(time_str):
    try:
        hour = int(time_str.split(':')[0])
    except:
        hour = 0  # Fallback for invalid formats
    if 6 <= hour <= 9:
        return 'Morning'
    elif 10 <= hour <= 13:
        return 'Midday'
    elif 14 <= hour <= 17:
        return 'Afternoon'
    elif 18 <= hour <= 21:
        return 'Evening'
    else:
        return 'Night'

df['HourGroup'] = df['Time'].apply(group_hour)

# Select and one-hot encode relevant features
features = df[['Amount', 'Category', 'Department', 'PaymentType', 'HourGroup']]
X = pd.get_dummies(features)

# Fit Isolation Forest model
model = IsolationForest(n_estimators=100, contamination=0.02, random_state=42)
anomaly_scores = model.fit_predict(X)

# Add results to original data
df['AnomalyScore'] = anomaly_scores

# Merge results back into full original dataset
df_full = dataset.copy()
df_full['HourGroup'] = df['HourGroup']
df_full['AnomalyScore'] = df['AnomalyScore']
df_full['CardNumber'] = df['CardNumber']

# Output
result = df_full
```

After running the script, I expanded the `df_full` output table in Power Query and got back the same dataset, but now with two new columns:

- **HourGroup**, which categorizes the time of each expense
- **AnomalyScore**, where a value of `-1` means the expense was flagged as unusual

### 🔍 Breaking Down What the Script Is Doing (and Why)

Each part of the script is designed to prep the data in a way that helps the model spot strange or suspicious patterns.

- **Dropping nulls**: We removed rows missing key info like *amount* or *time*, since these are critical for detecting odd behavior.
- **HourGroup feature**: Instead of looking at raw time values (e.g., “14:36”), we bucketed each expense into general time periods like *Morning* or *Evening*. This makes it easier to detect, say, expenses made late at night or outside of work hours.
- **Feature selection**: We used five fields for our model:
- `Amount`: to catch outliers in how much was spent
- `Category`: to know what type of item was bought
- `Department`: to understand team-specific patterns
- `PaymentType`: since fraud might look different depending on the method
- `HourGroup`: for that time-of-day context
- **One-hot encoding**: Since machine learning models can’t work directly with text, we converted each category (like “Meals” or “Travel”) into separate columns using a method called *one-hot encoding*. This just means turning each unique value into a column with a 0 or 1. For example, if an expense is categorized as *Meals*, the “Meals” column gets a 1, and the others get 0. This makes the data model-friendly.
- **Isolation Forest**: Finally, we used the Isolation Forest algorithm from the `scikit-learn` (sklearn) library. This model looks at all the values and figures out which rows seem most "isolated" or different from the rest—flagging them with a score of `-1`.

### 📊 Visualizing the Results in Power BI

Once the anomaly scores were added to the dataset, it was time to bring everything to life in Power BI. My goal with the report design was simple: make it easy for users to **spot suspicious transactions**, **see where they’re coming from**, and **take action quickly**.

At the top of the dashboard, I added a few key metrics:

![](99.System/Attachments/1!rUqA62oamCCXHQvWsYDzoQ.png.webp)

Key Metrics Added at the Top of the Report in Power BI

- **Total Anomaly Amount** over the selected period
- **Anomaly Count and Percentage** of total transactions
- Breakdowns **by Payment Type**, **Vendor**, and **Employee** to help pinpoint trends.

Each bar charts is fully interactive — clicking on any bar filters the transaction table below in real time.

**The Transaction Table**

![](99.System/Attachments/1!DCcRzXzW2xzKMQVt2iMQGA.png.webp)

Transaction Table in Power BI

The centerpiece of the dashboard is a clean, scrollable table showing all transactions with fields like:

- Employee name
- Amount and timestamp
- Vendor and payment info
- Anomaly detection status

I used conditional formatting to make anomalies really stand out. If a transaction was flagged (AnomalyScore = -1), a clear yellow/orange pill labeled **“Anomaly Detected”** is shown. For normal transactions, a simple green **“Normal”** tag appears.

This structure makes it easy to quickly scan through dozens (or hundreds!) of records and zero in on the ones that need attention.

If you’re interested in creative design ideas for your Power BI tables, check out this article where I dive deeper into some of my favorite approaches:

## [Better UX for Large Data Tables in Power BI](https://medium.com/the-bi-corner/better-ux-for-large-data-tables-in-power-bi-292d4dfc6862?source=post_page-----b12973e58b2b---------------------------------------)

### Because even the most boring tables deserve great design

medium.com

### 🛠️ Customizing the Model for Your Organization

The great thing about using Python in Power BI is that the logic is flexible and easy to adapt.

Here are a few ways you could customize this project to better fit your own organization:

- **Adjust the sensitivity** of the model by tweaking the `contamination` parameter in Isolation Forest. (Lower values mean fewer anomalies flagged; higher values are more sensitive.)
- **Modify or add features** based on the data you have. For example, you could bring in project codes, travel destinations, or user roles to improve detection.
- **Tweak time groupings** if your business operates outside the traditional 9–5 model. For example, hospitality or shift-based teams might need different hour buckets.
- **Add labels for review**: If your team wants to verify anomalies manually, you could create a “Review Status” column where reviewers confirm whether an anomaly is legitimate or not.
- **Trigger alerts**: With Power Automate, you could even send anomaly alerts to a manager when flagged expenses pass a certain threshold.

### 💡 Lessons Learned and Final Thoughts

A few things that I reinforced during this project:

- **Good features matter.** Isolation Forest doesn’t know what an “expense” is — it just looks at patterns in the numbers. The better context you give it, the better it performs.
- **You don’t need labeled data** to get started. Unsupervised learning like this is great for spotting issues without needing a long history of confirmed fraud cases.
- **Design makes a difference.** Users won’t take action on anomalies if they can’t quickly identify them. Clear visuals, intuitive filters, and bold indicators made this dashboard something people actually wanted to use.

This was a fun project to build — and honestly, pretty fast to do as well!😅 Machine learning projects aren’t always as complicated as we sometimes perceive them to be.

**👉** [**Download the PBIX file**](https://drive.google.com/file/d/1k1vaVM8MQip99yOlGbx1-zQHiJG0f_ST/view?usp=sharing) **to explore the setup, test the model, or adapt it to your own reporting needs.**

If you’re curious about other ways to use Python in Power BI, here’s another recent article where I show how I applied a similar approach for forecasting:

## [💡 My Favorite Way to Forecast in Power BI](https://medium.com/the-bi-corner/my-favorite-way-to-forecast-in-power-bi-634d1221df24?source=post_page-----b12973e58b2b---------------------------------------)

### How I used Power Query and Python to build a reusable, customizable forecasting model — no Premium needed

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