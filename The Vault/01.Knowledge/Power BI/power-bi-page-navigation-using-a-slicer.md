---
title: "Power BI – Page Navigation using a Slicer"
source: "https://www.flip-design.de/?p=1065"
author: "flip-design.de"
date: "2026-08-11"
tags: [imported, power-bi, flip-design]
created: "2026-08-11"
---

Power BI – Page Navigation using a Slicer | flip-it.de :: SQL, BI and more Many reports are having multiple pages and it is mostly a problem for the business user to navigate to the right page to get the right insights. If you have report with less than 5 pages, it is easy to create an overview page with different buttons for the navigation. But in the past, I’ve seen and working with reports which includes more than 10 pages to provide insights for the different business cases. To maintain so many buttons, mostly you don’t have enough space at the pages, and it is a problem to add the description for each. So, it is a good idea to use slicers for the navigation. How this can be done? See below 😊 First, I created the report with multiple pages including an overview page For the next step to create a meta data table, I’ve added a table with the different page names and for each page a short description. With this information you can provide a page description for the user. This table must maintain if you add new pages. Next, I’ve added a single value slicer with the page names and a card with the description for the selected page. Now, you need a button to create a page navigation to the selected page. To enable the page navigation, you need a simple DAX measure to gather the selected page from the slicer: Navigation = SELECTEDVALUE(‚Table'[Page]) Now, you can configure the action of the button by using the measure. And that’s it, if you select a page from the slicer, you get some information and when you click to button, you navigate to the selected page. Comments are closed.

---
*Source: [flip-design.de](https://www.flip-design.de/?p=1065)*
