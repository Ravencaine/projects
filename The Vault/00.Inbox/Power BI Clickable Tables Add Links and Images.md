---
title: "Power BI Clickable Tables: Add Links and Images"
source: "https://databear.com/power-bi-clickable-tables/"
author:
  - "[[Boniface Muchendu]]"
published: 2025-08-12
created: 2026-08-04
description: "Power BI clickable tables let you add links and images to reports. Learn how to enhance visuals with icons, URLs, and interactive elements."
Processed: "Unprocessed"
---
Tables with nothing but text can be… well, boring. In Power BI, you can take your reports to the next level by adding clickable links and images directly into your tables and matrices. This transforms them from static data dumps into interactive dashboards that encourage exploration.

If you come from an Excel background, you already know the value of detailed tables. But with **Power BI clickable tables and images**, you can combine that detail with dynamic visuals and direct navigation. Imagine embedding county icons, school logos, or direct URLs to related resources your reports suddenly become far more engaging.

##### A Real-World Example: Bridge Directory

Let’s look at a real use case. I built a simple Power BI report using a public dataset a directory of bridges in Florida filtered to counties near Jacksonville. The goal? Display each county, the number of bridges it contains, and enhance the table with:

- **County icons** (small images representing each county)
- **Clickable contact page links** for quick access to more information

This idea came from a **Pragmatic Works hackathon** where a school district wanted something similar logos and web links for each school displayed in a Power BI matrix.![A Real-World Example: Bridge Directory](99.System/Attachments/A_Real-World_Example!_Bridge_Directory.png)

##### Preparing the Dataset

To create **Power BI clickable tables and images**, you’ll need columns in your dataset that contain:

1. **Image URLs** Links to the images or icons you want to display.
2. **Web URLs** Links to relevant resources, like contact pages.

For this bridge dataset, I merged county names with their associated icon URLs from a telephone directory website, along with official contact page URLs.![Preparing the Dataset](99.System/Attachments/Preparing_the_Dataset.png)

##### Making Image URLs Work in Power BI

1. Select your column containing image links (e.g., `IconURL`).
2. In the **Data Category** dropdown, change the category to **Image URL**.
3. Power BI will automatically render the images in your table.

You can even adjust image height under the format settings to make icons more visible.![Making Image URLs Work in Power BI](99.System/Attachments/Making_Image_URLs_Work_in_Power_BI.png)

##### Making Links Clickable in Power BI

1. Select your column containing web addresses (e.g., `ContactPage`).
2. Change the **Data Category** to **Web URL**.
3. This will make each cell clickable, opening the link in your browser.

For cleaner visuals, enable the **URL icon** option in formatting this replaces long hyperlinks with a simple clickable icon.

##### Why This Matters

Adding images and links to your reports makes them more:

- **User-friendly** Readers can quickly navigate to relevant resources.
- **Visually appealing** Icons break up the monotony of text.
- **Interactive** Clickable elements turn passive viewers into active users.

Whether you’re building a **Power BI clickable tables and images** report for public datasets, internal dashboards, or client presentations, this technique increases engagement and usability.

##### Learn More About Power BI

If you want to expand your Power BI skills, check out this **[Power BI Training](https://databear.com/power-bi-training/)** resource. You’ll find step-by-step guidance on creating visuals, optimizing performance, and building impactful dashboards.

**Conclusion:**  
With a few adjustments in Power BI, you can transform basic tables into interactive data tools. Adding clickable icons, dynamic links, and images improves navigation and makes your data stories more compelling. The next time you build a table or matrix, skip the plain text make it interactive.