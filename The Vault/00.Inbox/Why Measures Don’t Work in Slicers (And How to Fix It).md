---
title: "Why Measures Don’t Work in Slicers (And How to Fix It)"
source: "https://goodly.co.in/why-measures-dont-work-in-slicers-and-how-to-fix-it/?utm_source=powerbiweekly&utm_medium=email&utm_campaign=newsletter"
author:
  - "[[Chhabra]]"
published: 2026-07-01
created: 2026-08-08
description: "If you have ever tried to use a measure in a slicer in Power BI, you already know it does not work directly. In this blog, I show you a practical workaround to use a measure in a slicer,"
Processed: "Unprocessed"
---
If you have ever tried to use a measure in a slicer in Power BI, you already know it does not work directly. In this blog, I show you a practical workaround to use a measure in a slicer, build a dynamic slicer based on measure values, and then use that slicer to drive your DAX calculations. We start by understanding why a Power BI slicer only accepts a column from a physical table and not a measure. Then we build a solution step by step using Generate Series, a disconnected table, SELECTEDVALUE, SUMMARIZECOLUMNS, FILTER, CALCULATE, COUNTROWS, CONCATENATEX, and ISINSCOPE. By the end, you will be able to filter visuals based on a measure threshold, count matching stores, and even show the names of the filtered stores. This is a very useful technique if you want to create a dynamic Power BI slicer, a measure-driven slicer, a what-if style slicer, or more advanced interactive Power BI reports using DAX.

![](https://www.youtube.com/watch?v=f0YKy9kyzfE)