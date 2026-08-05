---
title: "Power BI Matrix Slicer: Highlight Months & Fix Totals"
source: "https://databear.com/power-bi-matrix-slicer/"
author:
  - "[[Boniface Muchendu]]"
published: 2026-03-13
created: 2026-08-04
description: "Learn to build a Power BI matrix slicer that highlights months, hides rows without sales, and keeps totals accurate using DAX."
Processed: "Unprocessed"
---
The **Power BI matrix slicer** is a common requirement in real-world reports, but it quickly becomes complex when business users want dynamic behavior. In this scenario, the **Power BI matrix slicer** must highlight a selected month, hide products without sales for that month, and still return accurate totals. This article walks through how to solve this challenge using a disconnected slicer and advanced DAX techniques, proving that a **Power BI matrix slicer** can be both flexible and reliable when built correctly.

##### The Business Requirement

A customer request sounded simple at first:

- Display products on rows and months on columns in a matrix
- Select a month from a slicer
- Highlight the selected month’s column
- Hide products with no sales for that month
- Ensure totals remain correct

Individually, these tasks are manageable. Combined, they introduce evaluation-context challenges that require careful modeling and DAX design.

##### Data Model Setup with a Disconnected Slicer

The foundation of this solution is a **disconnected slicer table**.

##### Model Overview

- **DimProduct** → connected to FactSales
- **DimTime** → connected to FactSales
- **SlicerMonths** → disconnected copy of DimTime

The slicer table contains only the fields needed for month selection. Because it is disconnected, it does not automatically filter FactSales, giving you full control through DAX.

This approach is essential when working with a Power BI matrix slicer that must drive conditional logic rather than direct filtering.

##### Formatting DAX for Readability

Before building logic, formatting matters. Clean DAX is easier to debug and extend. Using tooling to auto-format DAX ensures consistency and follows best practices promoted by the Power BI community.

Readable DAX becomes especially important when measures grow in complexity, as they do in this scenario.

##### Highlighting the Selected Month Column

To highlight the selected month in the matrix:

1. Capture the selected year and month from the disconnected slicer
2. Compare it to the actual year and month in DimTime
3. Return a color value only when they match

This measure is then applied as **conditional formatting** to the matrix background color.

##### Result

- Selecting March highlights the March column
- Selecting April highlights the April column
- No selection returns no formatting

This creates an intuitive visual cue without altering the underlying data.

##### Suppressing Rows Without Sales

The next challenge is hiding products that have no sales in the selected month.

##### Key Techniques Used

- **ISINSCOPE** to detect matrix row level vs total level
- **Virtual tables** to evaluate product sales
- **REMOVEFILTERS** to bypass column context and evaluate the selected month globally

This logic ensures:

- Product rows disappear when they have no sales for the selected month
- The matrix remains responsive to slicer changes

This step is critical to making the Power BI matrix slicer behave like a true analytical control rather than a static filter.

##### Fixing Totals Correctly

Totals are where many DAX solutions fail.

To fix totals:

- Product-level logic evaluates only qualifying products
- Total-level logic re-evaluates all qualifying products for the selected month
- Filters from visible rows are removed to avoid undercounting

The result:

- January excludes products with no January sales
- March includes additional products that do have sales
- Totals dynamically adjust and remain accurate

This ensures business users trust the numbers they see.

##### Final Result

With all measures in place:

- Month selection highlights the correct column
- Products without sales disappear automatically
- Totals recalculate correctly for each selection
- The report behaves exactly as requested

This solution demonstrates how powerful DAX can be when paired with a thoughtful model design.

##### Why This Matters for Power BI Developers

Advanced matrix behavior is one of the most requested Power BI features in enterprise reports. Mastering techniques like disconnected slicers, virtual tables, and context control separates beginner models from production-ready solutions.

If you want to deepen your Power BI and Fabric skills, structured learning makes a significant difference. You can explore professional **Power BI training** through this comprehensive program:  
**[Power BI Training by DataBear](https://databear.com/power-bi-training/)**