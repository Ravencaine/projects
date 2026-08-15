---
title: "Dashboards, DirectQuery and what you should know about refreshing"
source: "https://www.flip-design.de/?p=1305"
author: "flip-design.de"
date: "2026-08-11"
tags: [imported, power-bi, flip-design]
created: "2026-08-11"
---

Dashboards, DirectQuery and what you should know about refreshing | flip-it.de :: SQL, BI and more A colleague said to me, that we can create a live dashboard in Power BI which displays actual data from database. I said NO! This post will show you, what you can do to achieve this goal. I’ve created a Power BI report which consumes data via DirectQuery from a SQL Database and a Measure for a change detection which make a refresh every five seconds. So, if I add a row to the table, I see the actual number of them very quickly. I’ve inserted a new row and aftern5 seconds you see the result inside the report. You need for this scenario a Premium capacity or PPU. Next, I’ve created a Dashboard and pinned the card and the whole report page to it. To compare this two possibilities, by pinning a card to the dashboard, you lose the background color. But both visualisations will not refresh when you add new rows. To see them, you must refreesh the dashboard. Interesting is, the card refreshes the data, the embedded report not. By pressing F5 or waiting several minutes, you get the visuals synchronized. By adding the dashboard or the report to an APP, you have the same behavior. One option could be, you built a Power BI Embedded application, another could be, you wait for the possibility from Power BI to do the refresh of a dashboard automatically. But, in my point of view, the users should be using the report… Comments are closed.

---
*Source: [flip-design.de](https://www.flip-design.de/?p=1305)*
