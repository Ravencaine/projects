---
title: "Power BI Field parameters for dynamic views"
source: "https://databear.com/power-bi-field-parameters-for-dynamic-views/"
author:
  - "[[Annamarie Van Wyk]]"
published: 2025-10-07
created: 2026-08-04
description: "Learn how to use Power BI field parameters to give you dynamic views in your report. No need for multiple visuals or drill downs."
Processed: "Unprocessed"
---
### How to Build Dynamic Daily, Weekly, Monthly Views in Power BI (Using Field Parameters)

If you’ve ever built a Power BI report and found yourself duplicating charts for **daily, weekly, monthly, or yearly** views — you’re not alone. It’s one of the most common (and frustrating) dashboard challenges: *“Can we see this by day? Actually, make it by week. No wait — what about monthly?”*

Instead of building **five versions** of the same visual, you can do it all with one — thanks to **Field [Parameters](https://databear.com/powerbi-the-good-the-wonderful-the-magnificent/ "The good, the wonderful, the magnificent Power BI!!!")**.

Let’s unpack how to set it up and make your visuals update dynamically with just a slicer.

#### What Are Field Parameters?

[Field Parameters](https://learn.microsoft.com/en-us/power-bi/guidance/data-translation-implement-field) are like a shape-shifter for visuals.  
They let you swap out fields — like Date, Week, Month, or Year — **dynamically** without writing a single line of DAX logic to handle each case.

Think of creating a slicer that says: “Show me this chart by Day / Week / Month / Quarter / Year.”

When the user changes the selection, your visuals automatically adjust.  
It’s clean, flexible, and user-friendly — basically everything we want in [Power BI](https://databear.com/power-bi-solutions/power-bi-inventory-analysis/ "Inventory Analysis").

You will need a date table that already has all of the necessary date combinations.

![Date_table_DAX](99.System/Attachments/Date_table_DAX.jpg)

#### Create Your Field Parameter

- Go to the **Modeling** tab → click **New parameter → Fields.**
- In the dialog box, give it a name like **“Date Selector.”**
- Select your date table, then add these fields (or whichever you have):
	- `Daily`
		- `Weekly`
		- `Monthly`
		- `Quarterly`
		- `Yearly`
- Click **Create.**![](99.System/Attachments/Field_Parameter_Create.jpg)
- Power BI will automatically:
	- Add a slicer to your report with all those options, and
		- Create a new table (something like `Date Selector`) that controls which field is active.

#### Build Your Visual

Now for the fun part.

1. Add a chart — say, **Sales over time**.
2. Drag your **Field Parameter** (Date View Selector) to the **X-axis**.
3. Add your measure (like `Total Sales`) to the **Values**.

Boom.  
Your chart now changes automatically depending on whether the user selects Day, Week, Month, Quarter, or Year in the slicer.

No multiple visuals. No bookmarks. Just one chart that does it all.

Video Player  <video width="800" height="462" src="https://databear.com/wp-content/uploads/2025/11/Ezgif.Com-Video-To-Gif-Converter-1.mp4?_=1" controls=""><source type="video/mp4" src="https://databear.com/wp-content/uploads/2025/11/Ezgif.Com-Video-To-Gif-Converter-1.mp4?_=1"> <a href="https://databear.com/wp-content/uploads/2025/11/Ezgif.Com-Video-To-Gif-Converter-1.mp4">https://databear.com/wp-content/uploads/2025/11/Ezgif.Com-Video-To-Gif-Converter-1.mp4</a></video>

00:01

00:09

#### Combine with Measures

Want to go further?  
You can use a similar approach with **Measure Parameters** — letting users toggle between metrics like *Sales, Profit, or Units Sold* while also switching between daily and monthly views.

Imagine:  
A single chart where users can pick *“Show me Profit by Quarter”* or *“Units Sold by Week”* — all in one clean design.  
That’s peak interactivity.

#### Why Field Parameters Are a Game-Changer

- **Fewer visuals:** One visual replaces five.
- **Easier maintenance:** Update once, apply everywhere.
- **Cleaner UX:** Users feel in control without overwhelming navigation.
- **Smarter storytelling:** You can let the data breathe at different time scales.

Next time someone says, *“Can you make it show weekly instead?”* You’ll just smile and say, *“Already done.”*

Don’t forget to check out our [training page](https://databear.com/power-bi-training/).