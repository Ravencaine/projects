---
title: "6 Excel features I use in every spreadsheet I create"
source: "https://www.howtogeek.com/microsoft-excel-features-i-use-in-every-spreadsheet/?shem=dsdf,sharefoc,agadiscoversdl,,sh/x/discover/m1/4"
author:
  - "[[Tony Phillips]]"
published: 2026-07-10
created: 2026-08-08
description: "Many Excel tools are optional extras, but these six are essentials I rely on in every workbook."
Processed: "Unprocessed"
---
Excel has hundreds of features, and I still discover new ones every year. Some solve very specific problems, while others become so useful that they quietly earn a place in every workbook I create. Whether you're building your first spreadsheet or your thousandth, these are the built-in Excel features I rely on to keep my data organized, accurate, and easy to work with.

## Excel tables are the first thing I add to every workbook

### Create a reliable base for your data

Whether I'm tracking my personal budget or mapping out a project timeline, I start by turning my raw data into an [Excel table](https://www.howtogeek.com/microsoft-excel-tables-three-second-habit/) (**Ctrl+T**). While a normal range is just a block of cells, a table gives Excel a clear understanding of where my data begins and ends, and how that structure should adapt as my data changes.

Tables handle tedious structural upkeep automatically—as data grows, they expand downward to incorporate new records and copy existing formatting and formulas. Tables also replace fragile, confusing cell references like $A$2:$C$100 with readable, [structured references](https://www.howtogeek.com/microsoft-excel-structured-references/) like \[@Sales\]. From that point on, everything else I add builds on that table.

Before pressing **Ctrl+T**, ensure your [dataset is well-structured](https://www.howtogeek.com/microsoft-excel-improve-data-structure/) with a single header row, fields as columns, and records as rows. Avoid blank rows, [merged cells](https://www.howtogeek.com/dont-merge-and-center-in-excel-center-across-selection-instead/), and extra headings inside your data range, as these can prevent Excel from recognizing the table correctly.

## Data validation saves me from fixing mistakes later

### Protect your workbook from bad input

The moment my table is built, I lock down what can be typed into it. Rather than fixing typos, inconsistent spellings, and broken formatting later, I spend a minute adding [data validation rules](https://www.howtogeek.com/microsoft-excel-data-validation-everything-you-need-to-know/) (**Data > Data Validation**) *before* data entry.

A simple [drop-down list](https://www.howtogeek.com/microsoft-excel-data-validation-drop-down-lists/) prevents many common data-entry errors by forcing people to pick from an approved set of options. If I'm tracking numerical values or timelines, I add boundary rules to reject impossible dates or negative numbers. When I need to enforce more specific requirements or combine multiple conditions, I use Excel's more [advanced data validation rules](https://www.howtogeek.com/microsoft-excel-custom-data-validation-trick-didnt-know-needed/).

I always take a few extra seconds to configure [custom input messages](https://www.howtogeek.com/microsoft-excel-data-validation-input-message-notes/) and error alerts, providing helpful guidance to anyone else using the workbook and showing them exactly how to fix their input before Excel rejects it.

Microsoft 365 includes access to Office apps like Word, Excel, and PowerPoint on up to five devices, 1 TB of OneDrive storage, and more.

[$100 at Microsoft](https://www.microsoft.com/en-us/microsoft-365/p/microsoft-365-personal/cfq7ttc0k5bf)

## Conditional formatting helps me spot important trends instantly

### Surface the data that deserves attention

Once a worksheet fills up with numbers, I don't want to rely on manually scanning every row to understand what's important. I use [conditional formatting](https://www.howtogeek.com/microsoft-excel-conditional-formatting-makes-beginners-look-like-experts/) (**Home > Conditional Formatting**) as a visual layer that automatically changes how data appears based on its value, helping me understand trends, highlight important information, and catch potential problems in seconds.

I use the built-in presets to highlight duplicate values, flag past-due deadlines, compare performance with color scales, or automatically shade my top performers. I also occasionally use icon sets or data bars when I want trends to stand out without adding extra charts. For more complex projects, I use formula-based rules to [format an entire table row](https://www.howtogeek.com/microsoft-excel-format-whole-row-when-checkbox-is-checked/) based on a single cell's status, so key details stand out immediately. Once those rules are in place, Excel does the visual work for me, making large datasets much easier to understand at a glance.

## Custom number formats improve readability without changing values

### Clean up your display while preserving raw data

[Custom number formats](https://www.howtogeek.com/microsoft-excel-custom-number-format-replace-formatting-tools/) —hidden inside the **Format Cells** dialog (**Ctrl+1**)—are one of my favorite Excel features. They change how data appears on-screen while preserving the underlying value, so formulas, PivotTables, and charts continue working exactly as expected.

In my workflows, custom number formats solve three common spreadsheet problems: abbreviating large figures with clean "K" or "M" suffixes to save space, hiding distracting zero values to reduce visual clutter, and adding units like "lbs" or "hours" directly next to values without breaking calculations. Custom formats can automatically color-code positive and negative numbers, making data easier to scan without adding unnecessary formatting rules.

[Custom number formats and conditional formatting](https://www.howtogeek.com/microsoft-excel-custom-number-formatting-conditional-formatting/) solve different problems. Use custom formats when you only want to change how a value looks. Use conditional formatting when you want Excel to react to changing data, such as highlighting overdue dates or flagging high performers.

## Slicers make my spreadsheets easier to use

### Build interactive sheets for yourself and others

Excel tables automatically add filter arrows to the header row, and they're the best option when I need more advanced filtering, searching through a long list of values, or sorting data in a specific order. However, they're not always the quickest way to explore a dataset.

The problem is that filter menus are hidden behind small drop-down buttons. If I'm repeatedly switching between categories, regions, products, or other fields, opening a menu, finding the right option, and clearing the filter again becomes surprisingly tedious. It's also not always obvious at a glance when a filter has been applied and some data is currently hidden.

When I want a faster, more visual way to interact with my data, [slicers](https://www.howtogeek.com/microsoft-excel-slicers-filter-data/) (**Insert > Slicer** or **PivotTable Analyze > Insert Slicer**) are the answer. Instead of digging through drop-down menus, I can click large, clearly labeled buttons to filter my data instantly, and they make it obvious which options are active.

While many people think slicers are exclusively for [PivotTables](https://www.howtogeek.com/microsoft-excel-go-to-trick-analyze-big-data-sets-fast/), you can also insert them directly onto standard Excel tables. They're especially useful for dashboards, trackers, and reports where I want to quickly switch between views of the same dataset.

## Power Query means I never clean imported data twice

### Eliminate repetitive manual data prep

Whenever I receive data from another system, I avoid cleaning it manually twice. If you find yourself deleting the same columns, changing the same data types, and sorting the same rows over and over, you're wasting valuable time repeating work Excel can handle for you.

[Power Query](https://www.howtogeek.com/microsoft-excel-power-query-beginners-guide/) is the feature I use whenever data arrives in a messy state. Instead of manually preparing the same report every week, I convert the data into a table and open it with **Data > Get & Transform Data > From Table/Range**. As I remove columns, fix data types, filter rows, and reshape the data, Excel records those instructions in the [Applied Steps pane](https://www.howtogeek.com/microsoft-excel-power-query-applied-steps-pane-faster-data-cleanup/) so it can repeat the process later.

After the initial setup, all I have to do is update the source data and click **Refresh**. Excel automatically runs through those same steps again, turning hours of cleanup into seconds of preparation. The finished results can then be loaded straight back into an Excel table, ready for formulas, charts, and analysis.

---

### The best Excel workflows keep evolving

The tools you use most often are rarely the flashiest ones. These six features have stuck with me because they make every spreadsheet cleaner, easier to maintain, and more useful. But that doesn't mean my workflow stays the same forever. As I continue discovering new Excel capabilities, some gradually become just as essential to the way I work, including [features I wish I'd learned about years earlier](https://www.howtogeek.com/microsoft-excel-features-i-wish-id-learned-years-earlier/).