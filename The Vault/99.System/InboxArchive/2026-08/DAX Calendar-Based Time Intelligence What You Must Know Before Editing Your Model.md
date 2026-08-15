---
title: "DAX Calendar-Based Time Intelligence: What You Must Know Before Editing Your Model"
source: "https://medium.com/riccardo-perico/dax-calendar-based-time-intelligence-what-you-must-know-before-editing-your-model-51f14c653c76"
author:
  - "[[Riccardo Perico]]"
published: 2025-11-20
created: 2026-08-03
description: "Don’t delete that column!"
Processed: "Unprocessed"
---
## Don’t delete that column!

## Prelude

If we compare DAX with other technologies in the Microsoft data ecosystem, we can say that it is relatively stable: it does not release rapid or continuous changes like other platforms such as Microsoft Fabric.  
In a sense, DAX and semantic modeling can be compared to Analysis Services and Transact-SQL: stable components with well-paced feature updates.

Anyway, in September, Microsoft announced two new preview features for DAX and semantic modeling: [**User-Defined Functions (UDF)**](https://learn.microsoft.com/en-us/power-bi/transform-model/desktop-user-defined-functions-overview?wt.mc_id=MVP_449122) and [**Calendar-based Time Intelligence**](https://learn.microsoft.com/en-us/power-bi/transform-model/desktop-time-intelligence#calendar-based-time-intelligence-preview?wt.mc_id=MVP_449122).  
In this post we will focus on the second one not to analyze every detail, but to highlight an important point: **you must be careful when modifying a model that uses this feature**.

All details about the feature, its setup, and its behavior can be easily found online.

In addition to the official documentation, I strongly recommend reading the [SQLBI article and watching their video](https://www.sqlbi.com/articles/introducing-calendar-based-time-intelligence-in-dax/), which explain the **conceptual logic behind calendar-based time intelligence and its correlation with the filter context**.

As noted by [Marco Russo](https://www.linkedin.com/in/sqlbi/), the feature is still in preview and may change, especially regarding its implementation in Power BI Desktop.

**We implemented it for a customer using a custom week-based calendar** for revenue, cost, and stock analysis. We appreciated how easy the setup was and how clean the resulting DAX remained, even with a sparse calendar.

Without going too deep the key benefits we got were:

- Works with any calendar: **custom weeks in our case**
- **No structural assumptions**: Power BI does not impose rules
- Sparse date support: **we haven’t days at all in the calendar**

## Be careful when modifying the model

However, there is a critical point, especially for business users with less technical background that, I’m sure, they’ll love this feature.

**You must be cautious when modifying the structure of the date table** used by the calendar-based time intelligence feature.

Power BI Desktop correctly handles **column renaming**, because the underlying **lineage tag** remains the same. The user can leverage Power Query to rename a column, for example, going from “Month of Year” to “Month of Years” and Power BI Desktop will mange it with no issues.

![](99.System/Attachments/1!3M7YMWRY4NZUpwvu8eERgA.png.webp)

Image showing the calendar setup window before the rename

![](99.System/Attachments/1!zo5IRfDYyXQ_x6GU5QLC1Q.png.webp)

Image showing the calendar setup window after the rename

Below **TMDL snippet to show that the lineage tag didn’t change** after column renaming.

```c
column 'Month of Year'
            dataType: string
            lineageTag: d32df0ee-107e-4e5d-abda-69cb4ead6d6c
            summarizeBy: none
            sourceColumn: Month of Year
 
column 'Month of Years'
            dataType: string
            lineageTag: d32df0ee-107e-4e5d-abda-69cb4ead6d6c
            summarizeBy: none
            sourceColumn: Month of Years
```

Otherwise, if a user **deletes and recreates** a column instead of renaming it, the lineage changes and the issue appears during the **processing phase** (Close & Apply in Power Query) that will fail with:

> **“CalendarColumnReference object referes to a column that has been deleted”**

![](99.System/Attachments/1!SNmHrBsnrDbJl94Webdtjw.png.webp)

Image showing CalendarColumnReference error

This obviously happens because a column used in the calendar definition no longer exists.

What is less obvious is that with the current implementation, **users can get stuck**:

- Processing fails
- **The new column does not yet exist in the model** since the processing failed
- The calendar UI does not show missing references
- **Users must manually delete broken mappings**
- Then refresh and remap everything again

This becomes more complex when multiple calendars or when significant structural changes are involved.

Using standard calendar definitions or tools like [Bravo for Power BI](https://www.sqlbi.com/tools/bravo-for-power-bi/) reduces the risk of having to change the date table structure.

Advanced users can use **TMDL** **View** to directly fix inconsistencies with few clicks, but this approach may be not suitable for business users.

## Conclusions

Calendar-based time intelligence is powerful but requires care. Problems arise when a calendar column is deleted instead of renamed, causing missing references that block model processing. Understanding how Power BI handles internal lineage, following consistent standards, and avoiding destructive changes are essential to prevent these issues.