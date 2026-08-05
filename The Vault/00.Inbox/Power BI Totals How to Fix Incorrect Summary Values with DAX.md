---
title: "Power BI Totals: How to Fix Incorrect Summary Values with DAX"
source: "https://databear.com/power-bi-totals-fix/"
author:
  - "[[Boniface Muchendu]]"
published: 2025-05-18
created: 2026-08-04
description: "Learn how to fix Power BI totals using DAX. Create accurate summaries with SUMX and virtual tables. Step-by-step guide included."
Processed: "Unprocessed"
---
**Power BI totals** often behave differently than users expect—especially those coming from Excel. While Excel simply adds up the visible values in a column, Power BI uses filter context to calculate totals, which can lead to confusing results. In this guide, you’ll learn why these discrepancies occur and how to fix them using advanced DAX techniques like `SUMX`, `HASONEVALUE`, and virtual tables.

---

##### Why the Total Row Is Wrong in Power BI

Let’s say you have a simple table that lists project revenue. Each row adds up correctly. But once you apply some conditional logic—such as only including revenue if project cost is greater than zero—the total row breaks.

Instead of summing the adjusted revenue per row, Power BI **re-evaluates the DAX expression at the total level**, which causes it to behave differently.

For example:

```
Adjusted Revenue = 
IF(
    [Total Cost] = 0,
    0,
    [Total Revenue]
)
```

This might work for each row. But at the total row, it could still show revenue for all projects, even those with zero cost—leading to an inaccurate grand total.

---

##### Understanding Filter Context in Power BI

This issue comes down to how Power BI handles **filter context**. At the row level, each project is evaluated individually. But at the total row, Power BI evaluates your DAX measure **once**, across the entire dataset. So even if one row had a condition that set revenue to zero, the total row might ignore that condition completely.

This is the core of the problem—and the first step to a proper **Power BI total row fix** is understanding this distinction.![Understanding Filter Context in Power BI](99.System/Attachments/Understanding_Filter_Context_in_Power_BI.png)

---

##### How to Detect the Total Row in DAX

To apply a different logic at the total level, we use the `HASONEVALUE()` function. This tells us if a specific row is being evaluated:

```
IF(
    HASONEVALUE(DimProjects[ProjectName]),
    [Adjusted Revenue],
    -- total row logic goes here
)
```

This way, we can separate logic for individual rows versus the total.![How to Detect the Total Row in DAX](99.System/Attachments/How_to_Detect_the_Total_Row_in_DAX.png)

---

##### Building the Fix with SUMX and Virtual Tables

Let’s fix this with a virtual table and an iterator function.

##### Step-by-Step DAX Breakdown

1. **Check if you’re in a row or total:**
	```
	HASONEVALUE(DimProjects[ProjectName])<img loading="lazy" decoding="async" class="aligncenter wp-image-42933 size-full" src="https://databear.com/wp-content/uploads/2025/05/Screenshot-2025-05-18-130918.png" alt="Check if you’re in a row or total" width="705" height="406" srcset="https://databear.com/wp-content/uploads/2025/05/Screenshot-2025-05-18-130918.png 705w, https://databear.com/wp-content/uploads/2025/05/Screenshot-2025-05-18-130918-300x173.png 300w, https://databear.com/wp-content/uploads/2025/05/Screenshot-2025-05-18-130918-150x86.png 150w" sizes="(max-width: 705px) 100vw, 705px" />
	```
2. **Create a virtual table of all projects:**
	```
	SUMMARIZE(DimProjects, DimProjects[ProjectName])<img loading="lazy" decoding="async" class="aligncenter wp-image-42934 size-full" src="https://databear.com/wp-content/uploads/2025/05/Screenshot-2025-05-18-131033.png" alt="Create a virtual table of all projects" width="606" height="378" srcset="https://databear.com/wp-content/uploads/2025/05/Screenshot-2025-05-18-131033.png 606w, https://databear.com/wp-content/uploads/2025/05/Screenshot-2025-05-18-131033-300x187.png 300w, https://databear.com/wp-content/uploads/2025/05/Screenshot-2025-05-18-131033-150x94.png 150w" sizes="(max-width: 606px) 100vw, 606px" />
	```
3. **Use SUMX to iterate through that table:**
	```
	SUMX(
	    SUMMARIZE(DimProjects, DimProjects[ProjectName]),
	    [Adjusted Revenue]
	)<img loading="lazy" decoding="async" class="aligncenter wp-image-42935 size-full" src="https://databear.com/wp-content/uploads/2025/05/Screenshot-2025-05-18-131210.png" alt="Use SUMX to iterate through that table" width="599" height="424" srcset="https://databear.com/wp-content/uploads/2025/05/Screenshot-2025-05-18-131210.png 599w, https://databear.com/wp-content/uploads/2025/05/Screenshot-2025-05-18-131210-300x212.png 300w, https://databear.com/wp-content/uploads/2025/05/Screenshot-2025-05-18-131210-150x106.png 150w" sizes="(max-width: 599px) 100vw, 599px" />
	```
4. **Combine everything into a full measure:**
	```
	Corrected Revenue = 
	IF(
	    HASONEVALUE(DimProjects[ProjectName]),
	    [Adjusted Revenue],
	    SUMX(
	        SUMMARIZE(DimProjects, DimProjects[ProjectName]),
	        [Adjusted Revenue]
	    )
	)
	```

This DAX logic ensures the total row calculates the same way the row-level values do— **finally solving the Power BI total row fix problem**.

---

##### Debugging with DAX Tricks

You can validate your virtual tables and filters using helper expressions like:

```
CONCATENATEX(
    SUMMARIZE(DimProjects, DimProjects[ProjectName]),
    DimProjects[ProjectName],
    ", "
)
```

This outputs a list of projects evaluated in the total row context—helpful for debugging.

You can also use:

```
COUNTROWS(SUMMARIZE(...))
```

to confirm how many items are in your virtual table.

---

##### Real-World Scenarios Where This Fix Applies

- **Financial statements** where certain rows are conditionally hidden or adjusted
- **Forecast vs actuals** reports where only certain data points should be included in totals
- **Sales dashboards** where discounts or refunds affect the total

Any time you’re applying conditional logic in DAX, you should be aware of how it behaves at the total level—and apply this fix accordingly.

---

##### Best Practices for Writing Total-Aware DAX

- **Always test your DAX logic at both row and total levels**
- **Use helper visuals or KPIs** to validate final values
- **Keep your virtual tables lean** —only summarize what’s necessary
- **Comment your code** to explain why you’re splitting logic for totals

---

##### Summary: Fixing Total Rows the Right Way

The total row in Power BI is not just a sum—it’s a new evaluation of your measure. That’s why conditional logic often produces unexpected results. Fortunately, using tools like `HASONEVALUE`, `SUMMARIZE`, and `SUMX`, you can build a robust **Power BI total row fix** that ensures accurate reporting every time.

Whether you’re working on executive dashboards or detailed financials, understanding how to control filter context is a must-have skill for any Power BI pro.

---

##### Learn More and Get Expert Help

If you want to dive deeper into DAX, filter context, or real-world modeling challenges, you don’t have to go it alone.

👉 [Explore expert-led training here:](https://databear.com/power-bi-training/)