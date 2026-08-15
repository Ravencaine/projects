---
title: "How to Build Interactive Cards in Power BI with the New Visual Features"
source: "https://datatraining.io/blog/new-card-visual"
author:
  - "[[datatraining]]"
published:
created: 2026-08-13
description: "With the March 2025 update, Power BI introduced powerful enhancements to the Card visual, opening up new ways to build interactive, visually rich, and dynamic dashboards. In this walkthrough, we’ll build an employee overview card system, complete with search, images, and conditional formatting. The best part? No workarounds or hacks, just native features."
Processed: "Unprocessed"
---
With the March 2025 update, Power BI introduced powerful enhancements to the Card visual, opening up new ways to build interactive, visually rich, and dynamic dashboards. In this walkthrough, we’ll build an employee overview card system, complete with search, images, and conditional formatting. The best part? No workarounds or hacks, just native features.

power bi dax new card conditional\_formatting

**Getting Started with the New Card Visual**  
  
Make sure you're using the March 2025 version or later. You’ll need the updated **Card (new)** visual to follow this tutorial.  
  

We’ll build a dashboard showing employee profiles with slicers for search and filtering, dynamic images, and formatted text elements.

![](https://lwfiles.mycourse.app/datatraining-public/2c5aca650ab98a412af5068acb67801b.png)

**Setting Up Filters and Slicers**  
  
Start by inserting the following slicers:

- Dropdown slicers for Office and Position.
- **Text search slicer** for employee names (a newer addition to Power BI).

**  
Inserting and Configuring the Card Visual  
  
**

1. Insert the **new card visual.**
2. For the categories, select the employee name (e.g., "Name and Surname").
3. Use the same field again for the **callout value.**

Next, let's make the magic happen.

![](https://lwfiles.mycourse.app/datatraining-public/d657f597af55f13f667467adec6c169f.png)

**Dynamic Colors Using Conditional Formatting**  
  
The March 2025 update lets us apply conditional formatting **based on the filter context**. You can now assign different colors or images depending on the current item.  
  
1\. Create a measure (e.g., CF test) that returns a color based on employee name.

![](https://lwfiles.mycourse.app/datatraining-public/789d8064e215bcc49c9e068dccd88580.png)

2\. Go to **Formatting > Small Multiples Header > Background.**

3\. Turn on conditional formatting using the **FX** button and select your measure.

![](https://lwfiles.mycourse.app/datatraining-public/fcfb7327d81d91b8e39c0d806faf7d13.png)

**Adding Dynamic Images  
**  
To show a unique image for each employee:

1. Go to **Formatting > Images.**
2. Enable Image and switch to **Image URL**.
3. Either use a measure that returns the correct URL or bind a column with image links.

*Tip*: Make sure your image URLs are **publicly accessible.  
  
**

Then style:

- Set image size to ~100px.
- Set image position to **left of text.**
- Add spacing between image and text (e.g., 30px).

![](https://lwfiles.mycourse.app/datatraining-public/679206db6dcd48830191ff38355f0c97.png)

**Reference Labels for Additional Info  
**  
Let’s add more information like position, office, email, and phone.

1. Go to **Reference Labels.**
2. Select the series ("Name and Surname").
3. Add the fields: Position, Office, Email, and Phone.

![](https://lwfiles.mycourse.app/datatraining-public/6342b9936cb1379054026a90d9c9b3ec.png)

To clean it up:

- Turn off the titles (e.g., "First Position", "First Office").
- Turn off the background color and borders.
- Change text color and font style as needed.

You can also **emphasize specific fields**, such as making the position bold with Segoe UI Semibold.  

**Final Layout Adjustments  
**  

1. Go to **Small Multiples > Layout.**
2. Switch from single column to **grid** layout.
3. Set max rows to 2 and columns to 3.
4. Enable **Continuous scroll** (instead of paginated) to avoid hidden pages.

To keep all cards the same size:

- Turn on " **Fix number of tiles** " under layout options.

Also, customize:

- Row and column spacing.
- Card padding and border radius (e.g., 10px).
- Border colors and alignments.

![](https://lwfiles.mycourse.app/datatraining-public/bf509e10c9c3aa09e8e853e4066ac957.png)

**Bonus: Add Icons to Reference Labels**  
Make your cards pop with icons:

1. Turn on the **title** for a reference label (e.g., email).
2. Set to **Custom** and paste a Unicode icon (via Win +.) or copy from a site like [emptycharacter.com](https://emptycharacter.com/) for spacing.

Repeat for phone, office, etc.

![](https://lwfiles.mycourse.app/datatraining-public/5954293e80d05ce52a81bd729bcdf4a1.png)

*Tip:* Add empty characters before the text to indent and align fields without changing layout.

**  
Wrap-Up  
  
**

This new version of the card visual unlocks interactive dashboards that were previously difficult or even impossible to build natively. Whether you're building dashboards for HR, projects, or products, this approach makes your reports smarter and more engaging.

**  
Hope you like it!**

Give it a try and see how it works for you! I’d love to hear what you think or see how you use this trick in your own reports.

How to Power BI

![](https://www.youtube.com/watch?v=igDhSdq7GVU)