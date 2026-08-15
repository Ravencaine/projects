---
title: "Building a Product Hierarchy Analytics Dashboard in Power BI: A Beginner’s Journey"
source: "https://medium.com/@mitalimunot64/building-a-product-hierarchy-analytics-dashboard-in-power-bi-a-beginners-journey-6b3c72375d41"
author:
  - "[[Mitalimunot]]"
published: 2026-08-09
created: 2026-08-09
description: "More"
Processed: "Unprocessed"
---
*How I turned a messy product catalog into a clean, interactive story — one chart at a time.*

## Why I Built This

Every retail dataset has a hidden problem: products don’t just belong to one category. A pair of headphones is “Electronics,” sure — but it’s also “Audio & Video,” and more specifically, “Earbuds & Headphones.” Most spreadsheets flatten all of this into a single messy column, and by the time you’re trying to answer a simple question like *“Which product types are most seasonal?”* you’re already lost in the noise.

That’s the problem I set out to solve with this project: a **Product Hierarchy Analytics Dashboard** built in Power BI, designed to take a flat product list and turn it into something you can actually explore — category by category, layer by layer.

The dataset itself is simple on paper: 74 products, each tagged with a three-level hierarchy —

**Primary Category → Secondary Category → Tertiary Category**

(For example: *Personal Care → Hair Care → Shampoo*.)

But simple data doesn’t mean simple insight. The real work was in deciding *how* to visualize that hierarchy so someone — a teacher, a classmate, a recruiter — could look at it for ten seconds and understand the whole product landscape.

I ended up building two connected dashboard pages, each answering a different kind of question.

## Page 1: The Executive Dashboard — “Give Me the Big Picture”

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*XCBfhXKx7XegMaMww8-9Mw.png)

Page 1 of my dashboard

This is the page I’d show first if someone had thirty seconds and wanted to understand the whole catalog. At the top, four KPI cards do the initial heavy lifting:

- **74** Total Products
- **8** Primary Categories
- **26** Secondary Categories
- **31** Tertiary Categories

Those four numbers alone tell a story — the catalog isn’t shallow (it’s not just 8 flat buckets) but it’s not overwhelming either. It’s *structured*.

Below the KPIs, I laid out four visuals that each answer one specific question:

- **Products by Primary Category** (horizontal bar chart) — which top-level categories actually have the most products? At a glance, Personal Care and Sports & Fitness dominate the shelf.
- **Category Distribution** (donut chart) — the same idea, but as a proportion of the whole catalog. This is the “percentage view” for anyone who thinks in shares rather than counts.
- **Products by Secondary Category** (treemap) — this is where it gets interesting. A treemap lets you see all 26 secondary categories at once, sized by how many products they hold, and it makes the *size differences* between categories immediately obvious in a way a bar chart of 26 items never could.
- **Products by Product Type** (bar chart) — the most granular slice on this page, showing individual product types like Accessories, Cookware, or Face Wash.

I also added four filter panels — **Primary Category, Product Type, Seasonal Relevance,** and **Target Demographic** — so this page isn’t just a static report. Anyone viewing it can slice the whole dashboard down to, say, “just Toys & Baby Products for a Winter audience,” and every chart updates instantly.

**The goal of this page, in one sentence:** *give a first-time viewer the shape of the entire catalog before they ask a single question.*

## Page 2: Product Hierarchy Analysis — “Let Me Dig In”

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*XTtBZTAtY5nG6ciezkcF_Q.png)

Page 2 of my dashboard

If the first page is the summary, this second page is the deep dive. It’s built for someone who already knows roughly what they’re looking for and wants to drill down.

At the top, instead of one filter panel, there are three — **Primary, Secondary,** and **Tertiary Category** — stacked side by side. This matters more than it sounds: it means you can filter top-down through the *entire hierarchy* in a couple of clicks. Pick “Personal Care” on the left, and the secondary list narrows to things like Hair Care and Skincare; pick one of those, and the tertiary list narrows further still.

Below the filters sit three more visuals:

- **Products by Purchase Frequency** — a simple bar chart splitting products into Occasionally, Weekly, and Monthly purchases. This is a subtle but genuinely useful business question: *which categories are habitual buys versus occasional ones?*
- **Seasonal Relevance Distribution** — a donut chart showing how much of the catalog is tied to a season (Winter, Summer, Back-to-School, etc.) versus being “Year-round.”
- **Products by Tertiary Category** — another treemap, but this time at the most granular level of the hierarchy, so you can see exactly which micro-categories (like Face Wash, Diapers & Wipes, or Bottles & Sterilizers) are pulling their weight.

And at the very bottom is the page’s real payoff: a **detailed data table** listing every product with its full hierarchy path, product type, and price range, all in one row. After exploring the visuals, this table is where you go to actually see the raw products behind the numbers — no more guessing what’s hiding inside a chart segment.

**The goal of this page, in one sentence:** *let someone go from “I have a question about a specific category” to “here’s the exact list of products that answer it” in three clicks.*

## What I Actually Learned Building This

If I’m being honest with myself (and with my teacher), the biggest lesson wasn’t about Power BI’s chart types — it was about **designing for a reader, not for myself.**

A few concrete takeaways:

1. **Hierarchy needs hierarchy in the UI too.** I originally tried cramming Primary, Secondary, and Tertiary filters into a single dropdown. It technically worked, but nobody could reason about it. Splitting them into three separate, cascading filter panels made the *structure of the data* visible in the *structure of the interface* — which is really the whole point of a hierarchy dashboard.
2. **Treemaps beat bar charts once you cross ~15 categories.** My Secondary Category bar chart with 26 bars was unreadable — tiny labels, no way to compare sizes at a glance. Switching to a treemap solved this instantly because area is a much more intuitive way to compare 20+ things than a wall of skinny bars.
3. **Two pages is a UX decision, not a technical one.** I could have crammed everything onto one page. I didn’t, because a summary view and a drill-down view serve two different mental modes — “orient me” versus “let me investigate.” Splitting them kept each page focused and each page fast.
4. **KPI cards are underrated as a first impression.** Those four numbers at the top of the Executive Dashboard take five seconds to build and probably do 30% of the communication work in the entire project.

## Tools Used

- **Power BI** for the dashboard itself — visuals, filters (slicers), and the cross-filtering interactivity between charts
- A structured **product catalog dataset** with three hierarchical category levels, product type, price range, purchase frequency, seasonal relevance, and target demographic fields

## Wrapping Up

This project started as a simple assignment — visualize a product hierarchy — but it ended up teaching me a lot more about *reading design* than about Power BI syntax. The dashboards aren’t complicated. There’s no fancy DAX wizardry, no exotic chart type. What makes them work is that every visual answers one clear question, and the two pages are ordered the way a real person’s curiosity actually flows: **overview first, details second.**

If you’re working on something similar, my honest advice is to sketch your questions before you touch a single chart. Once you know exactly what question each visual needs to answer, picking the right chart type — and explaining it to your teacher afterward — gets a lot easier.