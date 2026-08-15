---
title: "Dynamic Drop-Down Lists in Excel • My Online Training Hub"
source: "https://www.myonlinetraininghub.com/dynamic-drop-down-lists-in-excel"
author:
  - "[[Mynda Treacy]]"
published: 2025-10-28
created: 2026-08-09
description: "5 powerful dynamic Drop-Down Lists in Excel: update automatically, filter by category, and pull related data, saving time and reducing errors."
Processed: "Unprocessed"
---
Most people only know the basic way to create a drop-down list in Excel: typing a few values into **Data Validation**. For example:

![how to create data validation drop-downs in Excel?](https://d13ot9o61jdzpp.cloudfront.net/images/01-5-ways-to-create-drop-downs.png)

how to create data validation drop-downs in Excel?

That works if you’re just getting started, but it quickly becomes a headache. Every time new values are added, you have to go back and edit the list manually.

The good news? Excel has multiple smarter ways to build drop-downs that **update automatically, pull data from other sheets, and even change depending on your selection.** In this guide, I’ll walk you through **five powerful methods** to take your Excel drop-downs to the next level.

## Watch the Video

![](https://www.youtube.com/watch?v=2YEXzHIy_l8)

[![Subscribe YouTube](https://d13ot9o61jdzpp.cloudfront.net/images/subscribe.png)](https://www.youtube.com/c/MyOnlineTrainingHub?sub_confirmation=1)  
![](https://www.youtube.com/watch?v=subscribe_embed)

## Get the Excel Example File

Enter your email address below to download the free file.

By submitting your email address you agree that we can email you our Excel newsletter.

## 1\. Auto-Updating Drop-Downs with Tables

Instead of hard-coding values, put your list into a table. Tables in Excel are dynamic: they expand and contract as you add or remove data.

**Steps:**

1\. Enter your list into a column.

2\. Select it and go to **Home > Format as Table**.

![How to create dropdows from tables in Excel?](https://d13ot9o61jdzpp.cloudfront.net/images/02-5-ways-to-create-drop-downs.png)

How to create dropdows from tables in Excel?

3\. Create your drop-down list using **Data > Data Validation > Allow: List**.

4\. In the **Source** box, select the table column instead of typing values.

![how to create self-updating dropdowns in Excel?](https://d13ot9o61jdzpp.cloudfront.net/images/03-5-ways-to-create-drop-downs.png)

how to create self-updating dropdowns in Excel?

Now, whenever you add new items (e.g., Boston, Denver), your drop-down updates instantly.

⚠️ Note: This method only works if the list is on the same sheet. Let’s fix that next.

## 2\. Lists on Other Sheets with Named Ranges

When your lists live on a separate worksheet (for tidiness), tables alone won’t auto-update. The solution is **named ranges**.

**Steps:**

1\. Select your table column and go to **Formulas > Define Name** (e.g., DeptList).

![a screenshot of auto-expanding dropdowns in Excel](https://d13ot9o61jdzpp.cloudfront.net/images/04-5-ways-to-create-drop-downs.png)

a screenshot of auto-expanding dropdowns in Excel

2\. In your data validation, reference the name instead of the table column.

![A screenshot of data validation dialog box in Excel](https://d13ot9o61jdzpp.cloudfront.net/images/05-5-ways-to-create-drop-downs.png)

A screenshot of data validation dialog box in Excel

Now all drop-downs in the selected cells automatically include new entries.

💡 Bonus: Combine this with dynamic array formulas like SORT and UNIQUE to clean duplicates and blanks:

```
=SORT(UNIQUE(TOCOL(DepartmentTable[Department],1)))
```
![how to sort dropdown values in Excel?](https://d13ot9o61jdzpp.cloudfront.net/images/06-5-ways-to-create-drop-downs.png)

how to sort dropdown values in Excel?

Define a name for this spilled list (e.g., DepartmentList) and reference it in your drop-down.

![A screenshot of data validation dialog box in Excel](https://d13ot9o61jdzpp.cloudfront.net/images/07-5-ways-to-create-drop-downs.png)

A screenshot of data validation dialog box in Excel

## 3\. Dependent (Cascading) Drop-Downs

Want a list that changes depending on another selection? For example:

- In the Product Category column select **Electronics** → see only laptops, tablets, and monitors.
- Or select **Furniture** → see only desks, chairs, and cabinets.
![how to create dependent drop-downs in Excel?](https://d13ot9o61jdzpp.cloudfront.net/images/08-5-ways-to-create-drop-downs.png)

how to create dependent drop-downs in Excel?

This is a **dependent (or cascading) drop-down list**.

**How to set it up:**

1\. Build a lookup table of categories and products.

![A screenshot of using SORT and FILTER to spill dropdown values](https://d13ot9o61jdzpp.cloudfront.net/images/09-5-ways-to-create-drop-downs.png)

A screenshot of using SORT and FILTER to spill dropdown values

2\. Use the [SORT](https://www.myonlinetraininghub.com/excel-sort-function) and [FILTER](https://www.myonlinetraininghub.com/excel-filter-function) functions to spill the product lists based on the category in row 6:

![Creating cascading dropdowns in Excel](https://d13ot9o61jdzpp.cloudfront.net/images/10-5-ways-to-create-drop-downs.png)

Creating cascading dropdowns in Excel

3\. Use [XLOOKUP](https://www.myonlinetraininghub.com/excel-xlookup-function) to reference these spilled ranges in your data validation.

![Using XLOOKUP to create cascading dropdowns in Excel](https://d13ot9o61jdzpp.cloudfront.net/images/11-5-ways-to-create-drop-downs.png)

Using XLOOKUP to create cascading dropdowns in Excel

Result: error-proof data entry, faster selection, and a much cleaner experience.

**Note:** Check out the [video](https://www.myonlinetraininghub.com/dynamic-drop-down-lists-in-excel#vid) above for step-by-step on setting up the lookup table so that it automatically updates as you add more product categories and products.

## 4\. Drop-Downs That Fill in Related Data

Drop-downs can do more than limit choices, they can also **auto-populate related information**.

Example: Choose an employee in a drop-down, and Excel automatically fills in their **Department** and **Hourly Rate**.

**Formula:**

```
=XLOOKUP([@[Employee Name]],

EmployeeDatabaseTable[Employee Name],

EmployeeDatabaseTable[Department],"")
```

Copy across to retrieve multiple fields (e.g., Hourly Rate). This transforms your drop-downs into **interactive forms** that reduce manual entry and errors.

![A screenshot of related dropdowns in Excel](https://d13ot9o61jdzpp.cloudfront.net/images/12-5-ways-to-create-drop-downs.png)

A screenshot of related dropdowns in Excel

## 5\. Excluding Items with FILTER

Here’s where modern Excel really shines. Suppose you have a product catalogue with “Active” and “Discontinued” statuses:

![how to exclude dropdown items with FILTER function?](https://d13ot9o61jdzpp.cloudfront.net/images/13-5-ways-to-create-drop-downs.png)

how to exclude dropdown items with FILTER function?

Instead of maintaining two lists, use the [FILTER function](https://www.myonlinetraininghub.com/excel-filter-function).

**Formula:**

```
=SORT(UNIQUE(FILTER(ProductsTbl[Product],ProductsTbl[Status]="Active","")))
```
![Creating filtered dropdowns in Excel](https://d13ot9o61jdzpp.cloudfront.net/images/14-5-ways-to-create-drop-downs.png)

Creating filtered dropdowns in Excel

This ensures your drop-down always shows **only active products**, automatically sorted and de-duplicated:

![A screenshot of filtered dropdowns in Excel](https://d13ot9o61jdzpp.cloudfront.net/images/15-5-ways-to-create-drop-downs.png)

A screenshot of filtered dropdowns in Excel

Pair it with XLOOKUP to return related details (like price).

![Using XLOOKUP to fill values in Excel table](https://d13ot9o61jdzpp.cloudfront.net/images/16-5-ways-to-create-drop-downs.png)

Using XLOOKUP to fill values in Excel table

👉 In newer versions of Excel, drop-downs even let you **search as you type**, making selection even faster.

![Searching values in Excel dropdowns](https://d13ot9o61jdzpp.cloudfront.net/images/17-5-ways-to-create-drop-downs.png)

Searching values in Excel dropdowns

## Why These Methods Matter

By combining Excel tools like **Tables, Data Validation, Named Ranges, and Dynamic Array Functions**, you can build drop-downs that:

- Save time by updating themselves.
- Prevent errors with dependent filtering.
- Provide instant lookup of related data.
- Scale to hundreds or thousands of options.

This is the difference between "just knowing Excel" and **thinking like Excel**.

## Next Steps

If you want to go beyond drop-downs and master Excel at a professional level, check out my [Excel Expert Course](https://www.myonlinetraininghub.com/excel-expert-upgrade). It covers advanced formulas, dynamic arrays and more; complete with real-world projects and my personal mentoring.