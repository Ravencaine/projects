---
title: "Star Schema vs Snowflake Schema in Power BI"
source: "https://medium.com/learning-data/star-schema-vs-snowflake-schema-in-power-bi-5711f294e584"
author:
  - "[[Komal]]"
published: 2026-07-14
created: 2026-07-27
description: "More"
Processed: "Unprocessed"
---
## When to Use Each

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*3LDvHJgZfTaYF5zQMTWCjA.jpeg)

Photo by RDNE Stock project: https://www.pexels.com/photo/television-screen-with-display-7947955/

Okay, real talk: I made a data modeling mistake in my first Power BI project.

I built a dashboard. It looked great. My boss loved it.

Then… it took **8 minutes** to refresh.

WRONG.

The problem was my **data model**. I built a Snowflake Schema when I should’ve built a Star Schema.

That’s the difference between a 2-minute refresh and an 8-minute refresh.

## So What’s a Star Schema?

**Star Schema is like a pizza.**

*Pizza (Fact Table)  
/ | \\ \\  
Crust Sauce Cheese Storage  
(dim) (dim) (dim) (dim)*

- **One central table** (the fact table)
- **Multiple dimension tables** connected to it
- **All dimensions connect directly** to the center
- **No dimensions connect to each other**

**Real example:** Sales data

*Sales (Fact Table)  
/ | \\ \\  
Product Date Customer Region Store  
(dim) (dim) (dim) (dim) (dim)*

- Sales = central fact table
- Product, Date, Customer, Region, Store = dimension tables
- All dimensions connect directly to Sales
- No dimensions connect to each other

That’s a Star Schema.

## What’s a Snowflake Schema?

**Snowflake Schema is like a snowflake.**

*Snowflake (Fact Table)  
/ | \\ \\  
Branch Branch Branch Branch  
|  
Branch  
|  
Flake*

- **One central table** (the fact table)
- **Some dimensions connect to other dimensions** (not just the center)
- **Hierarchical structure**

**Real example:** Sales with organizational hierarchy

*Sales (Fact Table)  
/ | \\ \\  
Product Date Customer Region Store  
(dim) (dim) (dim) (dim) (dim)  
|  
Manager  
(dim)  
|  
Director  
(dim)*

- Customer connects to Sales
- Region connects to Customer (not Sales)
- Manager connects to Region (not Sales)
- Director connects to Manager (not Sales)

That’s a Snowflake Schema.

## The Performance Difference

**Star Schema is faster. Snowflake Schema is slower.**

**Star Schema: 2 Queries**

Query 1: JOIN Sales + Product  
Query 2: JOIN Sales + Customer

**Snowflake Schema: 4 Queries**

Query 1: JOIN Sales + Customer  
Query 2: JOIN Customer + Region  
Query 3: JOIN Region + Manager  
Query 4: JOIN Manager + Director

More queries = slower performance.

**Real numbers:**

- Star Schema: 1.5 million rows, 2-minute refresh
- Snowflake Schema: 1.5 million rows, 8-minute refresh

That’s 4x slower.

## When to Use Star Schema

Use Star Schema when:

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*MnF-O2CPXZh43vnW6B7T4Q.png)

**Rule of thumb:** If your data is “flat” (no hierarchy), use Star Schema.

**Real example:** Sales dashboard for retail company

- Star Schema
- 2-minute refresh
- Boss: “This is fast!”
- Project won.

## When to Use Snowflake Schema

Use Snowflake Schema when:

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*cAyrwa8Y8LmWkGNTzEMUWw.png)

**Rule of thumb:** If your data has “hierarchy” (nested levels), use Snowflake Schema.

## Quick Checklist

Before you present your Power BI report, ask yourself:

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*po4RNsxtcDpUAp-JO4KHxg.png)

**My rule:** Use Star Schema 90% of the time. Use Snowflake Schema 10% of the time.

## Final Thought

**Star Schema = simpler and faster. Snowflake Schema = more complex and normalized.**

Power BI is not a database. It’s a **visualization tool**.

The best model is:

- **Simple**: You understand it in 5 minutes
- **Fast**: Refreshes in 2 minutes (not 8)
- **Scalable**: Handles 10 million rows (not 1 million)

Star Schema wins.

**Thanks for reading.** If you’re a data scientist struggling with Power BI models, drop a comment. Let’s swap tips.

**P.S.** What’s your favourite data modelling pattern? Star Schema, Snowflake Schema, or something else?

*The contents of external submissions are not necessarily reflective of the opinions or work of* [*Maven Analytics*](http://mavenanalytics.io/) *or any of its team members.*

*We believe in fostering lifelong learning and our intent is to provide a platform for the data community to share their work and seek feedback from the Maven Analytics data fam.*

[*Submit your own writing here*](https://medium.com/learning-data/how-to-get-your-work-published-by-learning-data-with-maven-analytics-7df21e466a3e?sk=020dfac485597d602e218968d9ffb395) *if you’d like to become a contributor.*

*Happy learning!*

*\-Team Maven*