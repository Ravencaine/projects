---
title: "Excel HYPERLINK function • My Online Training Hub"
source: "https://www.myonlinetraininghub.com/excel-hyperlink-function"
author:
  - "[[Mynda Treacy]]"
published: 2025-11-11
created: 2026-08-09
description: "How to use the Excel HYPERLINK function to create clickable shortcuts, clean reports, navigate sheets, and build dynamic links."
Processed: "Unprocessed"
---
If your workbooks ever feel like a maze, the Excel HYPERLINK function can turn them into a smooth, one-click navigation experience. In this tutorial, you’ll learn how to use HYPERLINK to clean up messy URLs, navigate between sheets, open external files or folders, and even create dynamic links that respond to your selections.

By the end, you’ll know how to transform your spreadsheets into interactive tools that save you time and impress your boss.

## Watch the Excel HYPERLINK Function Video

![](https://www.youtube.com/watch?v=l17wuWa2JFo)

[![Subscribe YouTube](https://d13ot9o61jdzpp.cloudfront.net/images/subscribe.png)](https://www.youtube.com/c/MyOnlineTrainingHub?sub_confirmation=1)  
![](https://www.youtube.com/watch?v=subscribe_embed)

## Get the Free Example File

Enter your email address below to download the free file.

By submitting your email address you agree that we can email you our Excel newsletter.

## What Is the HYPERLINK Function?

Excel’s HYPERLINK function lets you create clickable links, not just for web pages, but also for internal sheet navigation and file shortcuts.

**Syntax:**

```
=HYPERLINK(link_location, [friendly_name])
```
- **link\_location:** The destination URL, file path, or cell reference.
- **friendly\_name:** \[Optional\] The text you want displayed (instead of the raw link).

## 1\. Clean Up Messy URLs in Reports

If your reports are filled with long, ugly URLs like this:

![a screenshot of URLs in Excel](https://d13ot9o61jdzpp.cloudfront.net/images/01-hyperlink-function.png)

a screenshot of URLs in Excel

You can replace them with neat anchor text like **“View Report”** resulting in a cleaner, neater report free of clutter:

![how to shorten URLs in Excel?](https://d13ot9o61jdzpp.cloudfront.net/images/02-hyperlink-function.png)

how to shorten URLs in Excel?

**Formula:**

```
=HYPERLINK([@[Report Link]], "View Report")
```

This formula creates a clickable label while keeping the actual URL hidden in another column (which you can safely hide). It makes your reports look professional and much easier to read.

**Pro Tip:** Always test your links before sending the file to someone else. Excel won’t tell you if a URL is broken.

## 2\. Build a Table of Contents to Navigate Between Sheets

When your workbook has multiple sheets, clicking back and forth wastes time.

![how to build a table of contents in Excel?](https://d13ot9o61jdzpp.cloudfront.net/images/03-hyperlink-function.png)

how to build a table of contents in Excel?

Instead, create a **Table of Contents (TOC)** sheet with clickable links to each tab.

**Example:**

```
=HYPERLINK("#"&C6&"!A1", C6&" Report")
```
![An Excel Table of Contents using the HYPERLINK function](https://d13ot9o61jdzpp.cloudfront.net/images/04-hyperlink-function.png)

An Excel Table of Contents using the HYPERLINK function

Here’s what’s happening:

- The **#** tells Excel it’s an internal link.
- **C6** contains the sheet name (e.g. “North”).
- **!A1** is the target cell within that sheet.
- The friendly name shows as “North Report”.

This technique helps others navigate your workbook without getting lost.

**Bonus:** You can also create navigation buttons using shapes:

1. Insert a rectangle → type the sheet name.
2. Press **Ctrl+K** → “Place in This Document”.
3. Select the sheet you want to link to.
4. Repeat for all sheets.
5. Colour code shapes to indicate which is the currently selected sheet.
![how to hide sheet tabs in Excel?](https://d13ot9o61jdzpp.cloudfront.net/images/05-hyperlink-function.png)

how to hide sheet tabs in Excel?

**Tip:** You can even **hide the sheet tabs** (File → Options → Advanced → Display options for this workbook) to make your dashboard look sleek and controlled.

## 3\. Link Directly to Files and Folders

The HYPERLINK function isn’t just for websites — it can also open files or folders directly from Excel.

**Examples:**

```
=HYPERLINK("C:\Project Gemini\Specifications.pdf", "Customer Requirements")
```
```
=HYPERLINK("C:\Reports\", "Open Reports Folder")
```

This trick lets you create a single Excel hub for all project files. It’s perfect for teams that constantly share supporting documents, contracts, or images.

**Note:** Use OneDrive or SharePoint paths for shared workbooks so everyone can access the same links.

## 4\. Create Dynamic Hyperlinks with XLOOKUP

You can even use formulas to create **dynamic links** that update based on a selection.

Imagine you have an order database and a dropdown list of Order IDs. You can use **XLOOKUP** to return details for the selected order and a HYPERLINK that jumps straight to the matching row:

![how to create dynamic hyperlinks in Excel?](https://d13ot9o61jdzpp.cloudfront.net/images/06-hyperlink-function.png)

how to create dynamic hyperlinks in Excel?

**Formula:**

```
=IFERROR(
HYPERLINK("#"&CELL("address",
XLOOKUP(D6,Orders[OrderID],Orders[OrderID])),
"Go to "&'Dynamic Hyperlinks'!D6),
"Order not found")
```

How it works:

- **XLOOKUP** finds the matching Order ID and returns its cell reference.
- **CELL("address", …)** gets that cell’s address.
- **#** makes it an internal link.
- The friendly name shows as “Go to \[Order ID\]”.

Clicking the link takes you directly to that order in your database. No scrolling, no searching.

## Common Mistakes to Avoid

1. **Broken File Paths:**  
	Excel doesn’t check whether the linked file actually exists. Always double-check your paths and test them before sharing.
2. **Sheet Names with Spaces:**  
	If your sheet name includes spaces (e.g., *Sales Data*), wrap it in single quotes:
```
=HYPERLINK("#'Sales Data'!A1", "Open Sales Sheet")
```

**Tip**: It’s good practice to always include quotes, just in case.

## Take It Further

If you love turning workbooks into interactive tools that *do the work for you*, you’ll love my [Advanced Excel Formulas Course](https://www.myonlinetraininghub.com/advanced-excel-formulas-course).

You’ll master formulas like **[LET](https://www.myonlinetraininghub.com/excel-let-function)**, **[LAMBDA](https://www.myonlinetraininghub.com/excel-lambda-function)**, **[IFERROR](https://www.myonlinetraininghub.com/excel-iferror-puts-an-end-to-messy-workarounds)**, and **[XLOOKUP](https://www.myonlinetraininghub.com/excel-xlookup-function)** to automate workflows and eliminate repetitive manual steps.