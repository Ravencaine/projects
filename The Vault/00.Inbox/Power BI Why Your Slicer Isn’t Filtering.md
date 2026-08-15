---
title: "Power BI: Why Your Slicer Isn’t Filtering"
source: "https://www.selectdistinct.co.uk/2026/07/06/power-bi-slicer-not-filtering-fixes/?utm_source=powerbiweekly&utm_medium=email&utm_campaign=newsletter"
author:
  - "[[Elle Harrison]]"
published: 2026-07-06
created: 2026-08-08
description: "Is your Power BI slicer not filtering? Learn how to troubleshoot interactions, relationships, and filter direction to fix your report quickly."
Processed: "Unprocessed"
---
## Business Analytics Blog

Ever built a Power BI report, added a slicer, and then… nothing happens?

![](https://www.youtube.com/watch?v=0BTNgNj8jXc)

You click the slicer, but your visuals remain unchanged. It can be extremely frustrating, but usually, it’s down to one of these three common setup mistakes.

## 1.Slicer Interactions Are Off

Sometimes, the slicer and the visual just aren’t talking to each other.

### The Fix:

Step 1: Select your **Slicer**

![Power BI Weather dashboard showing two slicers](https://www.selectdistinct.co.uk/wp-content/uploads/2026/07/image.png)

Power BI Weather dashboard showing two slicers

Step 2: Go to the top ribbon and select the **Format** tab.

Step 3: Click **Edit Interactions**

![Screenshot of Power BI ribbon circling Format and Edit Interactions](https://www.selectdistinct.co.uk/wp-content/uploads/2026/07/image-2.png)

Screenshot of Power BI ribbon circling Format and Edit Interactions

You will see small icons appear above your other visuals.

Make sure the **Filter** icon (the funnel) is selected.

![Power BI slicer showing filter selected](https://www.selectdistinct.co.uk/wp-content/uploads/2026/07/image-3.png)

Power BI slicer showing filter selected

If the **None** icon (circle with a line) is active, the slicer is set to ignore that visual.

![Power BI slicer with None selected](https://www.selectdistinct.co.uk/wp-content/uploads/2026/07/image-4.png)

Power BI slicer with None selected

## 2\. No Data Relationship

If your slicer is coming from a different table than the data in your visual, Power BI needs a bridge to connect them.

If there is no relationship between those two tables, the filter cannot pass through.

## The Fix:

Step 1: Go to the **Model view** (the icon on the far left that looks like a diagram).

![Screenshot of Model view in Power BI](https://www.selectdistinct.co.uk/wp-content/uploads/2026/07/image-5.png)

Screenshot of Model view in Power BI

Step 2: Check if there is a line connecting your Slicer table to your Visual’s data table.

![1 to many relationship in Power BI](https://www.selectdistinct.co.uk/wp-content/uploads/2026/07/image-6.png)

1 to many relationship in Power BI

Step 3: If not, drag and drop the common field (e.g. Date or Category ID) from one table to the other to create the relationship.

**A Real-World Example:** Think of it like this: we have a Compass Directions table and a Worksop Weather table. By drawing a line between them, we create a “1-to-many” relationship.

![1 to many relationship example using two tables](https://www.selectdistinct.co.uk/wp-content/uploads/2026/07/image-7.png)

1 to many relationship example using two tables

**The Concept:** This link acts as the bridge that allows a slicer to talk to the data. Because the tables are linked, when a user picks a value in the slicer, Power BI knows exactly which records to filter.

If that line is missing, the tables do not know they are related, and the dashboard will remain frozen regardless of slicer interaction

## 3\. The Filter Direction Problem

Sometimes the relationship is there, but the filter hits a wall because it’s only set to travel one way.

**The Fix:**

**Step 1:** In Model view, double-click the relationship line connecting your tables.

**Step 2:** Check the Cross-filter direction in the menu that appears.

**Step 3:** While you can set this to “Both,” it is generally best to avoid it

![Manage relationships in Power BI](https://www.selectdistinct.co.uk/wp-content/uploads/2026/07/image-8.png)

Manage relationships in Power BI

In our Worksop Weather project, we stick to “Single” direction. It’s all we need for the slicer to work.

If you find yourself needing “Both,” it’s usually a sign that your data model needs a rethink, not a settings change. Keep your model clean and your filters will behave.

## Summary – Troubleshooting Your Slicer

If your slicer is not filtering your visual, check these three common areas:

| **Issue** | **What to Check** | **Where to Go** |
| --- | --- | --- |
| Slicer Interactions | Check filter is active | Format Tab: Edit Interactions |
| Data Relationships | Confirm a (bridge) line exists between tables | Model View |
| Filter Direction | Check if the flow is set to “Single” | Model View: Relationship Properties |

## Slicer Still Not Working?

If you have checked these three things and your slicer is still behaving strangely, your data might have a mismatch (e.g. the slicer is set to “Text” but the visual is looking for “Numeric” values).

![Format visual changing the data format](https://www.selectdistinct.co.uk/wp-content/uploads/2026/07/image-9.png)

Format visual changing the data format

## Conclusion: Keep Your Model Tidy

Power BI slicers are incredibly powerful, but they rely on a healthy data model to function correctly.

By keeping these three pillars: **Interactions, Relationships, and Filter Direction** in mind, you can troubleshoot almost any “frozen” slicer in minutes. Save this guide to your favourites for the next time you’re troubleshooting a build

Remember: a clean, logical data model is the secret to a fast, reliable, and frustration-free dashboard.