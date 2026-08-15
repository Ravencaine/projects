---
title: "Power BI, Create a TOP n Measure"
source: "https://www.flip-design.de/?p=1416"
author: "flip-design.de"
date: "2026-08-11"
tags: [imported, power-bi, flip-design]
created: "2026-08-11"
---

Power BI, Create a TOP n Measure | flip-it.de :: SQL, BI and more The situation is relatively simple. I needed a Power BI measure where I could see the top three companies with the highest sales, depending on the filters set. A colleague told me that it would be relatively simple to use a filter to only show the top three and sort the results in descending order of sales. That’s true in principle, but the problem is that if further filters are set, second place may be eliminated and the order changes. The example model is limited to one table for the sake of simplicity. Here you can add up and display the sales by category. The top three categories would be C, B and A. Category D would be in fourth place. If you now create a table in which only the top three sales are displayed by category but filter out category C, then you will also see category D in the result. In principle this is correct, but it may not be the expected result. In my case, only categories A and B should be displayed. However, if the visualization is not filtered, the result is as expected. To get the expected result, I first created a Power BI DAX measure that sums up the sales column, but takes possible filters on the category column, but ignores other filters. This creates the basis for displaying sales by category, but ignores all other filters. In the next step, the sales are sorted based on this measure, a ranking key figure is created and sorted in descending order. This gives the sales by category a number This key figure can then be used to create a table or any visualization. All four data sets are initially displayed here. The first three rows can then be filtered using the sorting key figure. Now if category A is removed from the filter, and only categories C and B are still displayed, and not category D. Comments are closed.

---
*Source: [flip-design.de](https://www.flip-design.de/?p=1416)*
