---
title: "Power BI Date Slicer: Build Dynamic Reports with Bookmarks"
source: "https://databear.com/power-bi-relative-date-slicer/"
author:
  - "[[Boniface Muchendu]]"
published: 2025-12-10
created: 2026-08-04
description: "Discover how to use the Power BI Date Slicer to build dynamic, time-based reports and boost user experience with bookmark navigation."
Processed: "Unprocessed"
---
Power BI is packed with features that empower report creators and end-users alike but one tool that often goes under the radar is the **Power BI Date Slicer**. This powerful feature lets you filter data based on dynamic time frames like “last 30 days” or “this year,” making your reports smarter and more responsive to real-time data.

##### What Is the Relative Date Slicer?

The **Relative Date Slicer** allows you to filter data based on a moving window of time like the **last 30 days**, **next month**, or **this year**. Unlike traditional slicers that rely on manually selected dates, this dynamic slicer updates automatically based on the current date.

This functionality is incredibly useful for real-time dashboards or executive reports that need to reflect the latest data without constant updates.

##### Setting Up the Relative Date Slicer

Here’s a step-by-step breakdown:![Setting Up the Relative Date Slicer](99.System/Attachments/Setting_Up_the_Relative_Date_Slicer.png)

1. **Create a Date Table**: Use the DAX function `CALENDARAUTO()` to generate your date table.
2. **Mark It as a Date Table**:
	- Right-click on the table in the Fields pane.
		- Choose **Mark as Date Table** and select your date column.
		- This ensures compatibility with time intelligence functions.

> Note: You may lose the auto-generated hierarchy, but you can manually recreate it in the data model or directly on a visual.

##### Types of Slicers: A Quick Primer

Before diving deeper into the relative date slicer, let’s compare it with other slicer types:

- **Date Hierarchy Slicer**: Allows multi-select across years, quarters, and months.
- **Manual Hierarchies**: You can drag-and-drop fields like “Year” and “Month Name” into a visual to create custom hierarchies.

Both are powerful, but they lack the dynamic flexibility of the relative date slicer.

##### Using the Relative Date Slicer

Once your date field is added to a slicer, you can change its type by:

1. Clicking the dropdown menu in the slicer.
2. Selecting **Relative Date**.

##### Customizing the Filter:

- Choose options like:
	- Last X days/months/years
		- Next X days/months/years
		- This month/year/week
- **Include Today** toggle: This determines whether today is included in the filter.
- **Anchor Date**: Lock the slicer to a fixed reference date (e.g., start of a quarter), which is helpful for consistent reporting.

##### “Years” vs. “Calendar Years” What’s the Difference?

This is where many users get tripped up.![“Years” vs. “Calendar Years”  What’s the Difference?](99.System/Attachments/“Years”_vs._“Calendar_Years”_What’s_the_Difference.png)

- **Last 5 Years**: Goes back exactly 5 years from today (e.g., Dec 8, 2025 to Dec 8, 2020).
- **Last 5 Calendar Years**: Excludes the current year and includes full previous years (e.g., 2020–2024).

This logic also applies to:

- **Months** vs. **Calendar Months**
- **Weeks** vs. **Calendar Weeks**

Understanding the difference ensures you’re showing the exact data range users expect.

##### Bonus Trick: Use Bookmarks and the Bookmark Navigator

Want to supercharge user experience?

Here’s how you can use bookmarks to toggle between commonly viewed timeframes (e.g., last 5, 10, and 25 years).

##### Steps:

1. **Apply a Relative Date Filter** (e.g., Last 5 Years).
2. Go to **View > Bookmarks Pane** and create a new bookmark.
3. Repeat for other timeframes (10 and 25 years).
4. Insert a **Bookmark Navigator** from the **Insert > Buttons > Navigator** menu.

This creates clickable buttons users can use to switch between predefined views without fiddling with slicers!

##### When to Use the Relative Date Slicer

The relative date slicer is great for:

- Dashboards that refresh daily or weekly
- Executive reports with rolling windows
- Hiding complex slicer logic behind user-friendly bookmark buttons

You can even hide the slicer from users and use it solely for building intuitive bookmark-driven navigation.

##### Additional Resources

Looking to dive deeper?

- [**Power BI Training Courses by Data Bear**](https://databear.com/power-bi-training/) Comprehensive training for all skill levels.
- Mitchell from Pragmatic Works covers **DAX-based relative date filters** in another great video.
- Allison from Pragmatic Works offers a fantastic beginner-friendly intro to slicers in Power BI.

##### Final Thoughts

The **Relative Date Slicer** is one of the most versatile and dynamic filtering tools in Power BI. Combine it with bookmarks and the bookmark navigator to create polished, user-friendly reports that adapt with time.

Whether you’re building for executives or fellow analysts, mastering this feature will give your reports a serious edge.

**Don’t forget to explore our full library of Power BI tutorials and courses to continue leveling up your skills!**