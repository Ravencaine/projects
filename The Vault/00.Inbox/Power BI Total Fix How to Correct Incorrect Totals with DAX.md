---
title: "Power BI Total Fix: How to Correct Incorrect Totals with DAX"
source: "https://databear.com/power-bi-total-fix/"
author:
  - "[[Boniface Muchendu]]"
published: 2025-05-18
created: 2026-08-04
description: "Need a Power BI total fix? Learn why totals can be misleading and how to correct them using DAX with SUMX, HASONEVALUE, and virtual tables."
Processed: "Unprocessed"
---
If you’re looking for a **Power BI total row fix**, you’re not alone. Many users assume that the total row in Power BI will simply sum up the visible rows—just like Excel. But in Power BI, totals are recalculated based on a different filter context, which can result in totals that don’t align with the individual values you see in your table. In this post, we’ll show you why that happens and how to correct it using DAX.

---

##### Understanding the Power BI Model

Let’s start with a simple data model:

- **Projects (Dimension table)**: List of all project names.
- **Project Revenue (Fact table)**: Revenue by project.
- **Project Cost (Fact table)**: Cost by project.

You build a basic measure:

```
Total Revenue = SUM(FactProjectRevenue[Revenue])
```

Everything looks fine—until you add business logic.![](99.System/Attachments/Screenshot-2025-05-18-120946.png)

---

##### Adding Conditional Logic That Breaks the Total

Say you only want to include revenue for projects that have incurred cost. You update your measure:

```
Adjusted Revenue = 
IF(
    [Total Cost] = 0,
    0,
    [Total Revenue]
)
```

It works row-by-row… but at the total level, it still shows **$1,100**, even though one project with no cost should have been excluded.![](99.System/Attachments/Screenshot-2025-05-18-121139.png)

---

##### Why the Total Row Doesn’t Match the Visible Sum

Power BI doesn’t total the individual row results. Instead, it **re-evaluates** your DAX expression over a broader filter context—in this case, all projects combined.

So:

- `[Total Cost]` at the total row = sum of all project costs = 65
- Since 65 ≠ 0, it returns `[Total Revenue]` for all projects = **$1,100**

What you really wanted was:

- 300 (project A) + 600 (project B) + 0 (project C) = **$900 ![](99.System/Attachments/Screenshot-2025-05-18-121317.png)**

---

##### How to Detect the Total Row in DAX

Use the `HASONEVALUE()` function to check if you’re in a specific row or the total row:

```
IF(
    HASONEVALUE(DimProjects[ProjectName]),
    [Adjusted Revenue],
    -- total logic here
)
```

This returns:

- `TRUE` for individual rows
- `FALSE` for total rows ![](99.System/Attachments/Screenshot-2025-05-18-121526.png)

---

##### Creating a Virtual Table for Accurate Totals

To fix the total, create a virtual table using `SUMMARIZE`, and calculate row-level results using `SUMX`.

Here’s the final DAX measure:

```
Adjusted Revenue with Total = 
IF(
    HASONEVALUE(DimProjects[ProjectName]),
    [Adjusted Revenue],
    SUMX(
        SUMMARIZE(DimProjects, DimProjects[ProjectName]),
        [Adjusted Revenue]
    )
)
```

Now, instead of using the default total logic, Power BI:

1. Builds a table of all projects.
2. Applies `[Adjusted Revenue]` to each row.
3. Sums the results.

**Correct total returned: $900 ![](99.System/Attachments/Screenshot-2025-05-18-121644.png)** 

---

##### Helpful Debugging Trick

To see what’s being evaluated, try:

```
CONCATENATEX(
    SUMMARIZE(DimProjects, DimProjects[ProjectName]),
    DimProjects[ProjectName],
    ", "
)
```

This displays all project names in the current filter context—great for testing your DAX.

---

##### Summary: Key Lessons

- Power BI total rows are **not** just row sums—they use different filter context.
- Use `HASONEVALUE()` to detect total rows.
- Use `SUMX` and `SUMMARIZE` to build a correct total from row-level logic.

Mastering this approach will help you avoid one of the most common DAX pitfalls and give you more control over how your totals behave.

---

##### Level Up Your Power BI Skills

If you’re ready to tackle more real-world Power BI challenges or sharpen your DAX skills, [check out this training resource:](https://databear.com/power-bi-training/)