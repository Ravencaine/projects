---
title: "Deep dive into Power BI reporting with the new date picker slicer option (Preview)"
source: "https://community.fabric.microsoft.com/t5/Power-BI-Updates-Blog/Deep-dive-into-Power-BI-reporting-with-the-new-date-picker/ba-p/5295674?utm_source=powerbiweekly&utm_medium=email&utm_campaign=newsletter"
author:
published: 2026-07-16
created: 2026-08-08
description: "Report authors often need date filters that automatically keep reports focused on the most relevant data without requiring ongoing maintenance. The"
Processed: "Unprocessed"
---
Report authors often need date filters that automatically keep reports focused on the most relevant data without requiring ongoing maintenance. The new date picker slicer makes this easier by supporting dynamic relative date ranges that move forward as data refreshes, while still allowing report viewers to explore different date ranges, individual dates, and custom periods when needed.

Most reports have a date and report viewers want to see the latest data or pick their own date ranges. The date picker style of the slicer visual gives report authors and report viewers options to do it all.

Set up a relative range, such as last 30 days from the last date available. Anchor it on the last date, first date, or today with offset options to do last 30 days, starting 5 days back, if you want. This relative range automatically moves forward as your data refreshes and more data comes in. Publish the report and it’s the default relative range.

Your report viewers remain free to explore beyond what you have set up as the default relative range. They can pick their own relative range or pick their own date range. They can pull up a **single calendar** to pick the start and end date **or even a single date** to filter the other visuals. The **slider** is also available, giving you a quick way to adjust the range. The slider has an improvement too; you can set the start and end then move the whole range back and forth to offset the range manually!

The slicer lets you know what is happening. There are two summaries available. The top summary shows you the date range the data column is filtered to. If a relative range falls outside of the available data, it only shows the dates inside the available data, and an informational tooltip explains the date range is incomplete. The lower summary shows you the relative or manual range you have selected. That way you always know what you entered and what you are seeing.

The functionality is robust and so is the formatting. Choose to show the lower summary or not. Choose to show the slider or not. Choose the styling of the calendar button, the summaries, and slider. The dates themselves also follow the date formatting you have specified for that column, or you can choose a new format going to General > Data format! As the calendar to enter the relative and manual range is an overlay, you can make this powerful slicer take up minimal space on your report, freeing you up to showcase your other visuals.

What happens to the other visuals is also improved. If you have a relative date range applied, it continues to apply even when the visual is pinned to a dashboard. The relative date option in filter pane or in the slicer would convert it to manual range, so if you want that static behavior, you can still get it that way. The date picker relative ranges stay with the visual when pinned, so the visual continues to roll forward as new data comes in. And as always, you can pick which visuals it impacts or not with edit interactions.  

## How to enable the date picker for your report

You can enable **Date picker** in the Slicer visual via **Visual** > **Slicer settings** > **Options** in the Format pane. This only shows up when you have a date column added to the slicer.

If you don’t see it, be sure to turn on the preview. Go to **File** > **Options and settings** > **Options** > **Preview features** and select **Date picker slicer**. During preview, you can create Date picker slicers only in Power BI Desktop. After you publish a report, you can view and edit these slicers in the Power BI service.

Now let’s look at some scenarios once you have it on.  

## Walkthrough: Show the last full month based on the latest date

Many reports bring data in as it comes but when you show the most current month, it shows a sharp decline as the month isn’t complete yet.

![DataZoe_0-1784088970942.png](https://community.fabric.microsoft.com/t5/image/serverpage/image-id/1355570i79244FDE80731D6D/image-size/large?v=v2&px=999 "DataZoe_0-1784088970942.png")

*Figure: A report showing a sharp drop in the current month because the month is still incomplete, demonstrating why a rolling full-month date range is useful.*

Let’s configure the range to show the last 24 full months.

1. Select the calendar button to the left of the visual
2. Select relative
3. Set it so it says, “Date is in the **Last** **24 Months (Calendar)** from **Last** **date** offset by **0** Months (Calendar)”
4. Select Apply

![DataZoe_1-1784088970943.png](https://community.fabric.microsoft.com/t5/image/serverpage/image-id/1355569iB9259A8371C05A14/image-size/large?v=v2&px=999 "DataZoe_1-1784088970943.png")

*Figure: The date picker configured to show the last 24 full calendar months from the latest available date, so the report updates automatically as new data arrives.*

Now you have a relative range that will move forward automatically when the full month is complete and you can compare your month’s year over year completely.

![DataZoe_2-1784088985855.png](https://community.fabric.microsoft.com/t5/image/serverpage/image-id/1355571iE09EB1B6B4FB761B/image-size/large?v=v2&px=999 "DataZoe_2-1784088985855.png")

*Figure: The report now compares complete months year over year, with the slicer summaries showing both the filtered date range and the selected relative range.*

The summaries tell you both what dates are showing and the relative range you picked. The calendar icon shifts to the relative calendar icon, and the slider gives you an indication of the portion of the range you are viewing.

When you check the filters on the visuals they show the relative range, not the static range. If I pin this to a dashboard, it continues to show that relative range as new data arrives.

## Walkthrough: How to handle date range beyond the values

Let’s look at an example where the date extends into the future. This is common with a date table that is ready for future or forecast data.

Here my units sold stop on April 14th, so there is a sharp decline again for the partial month. The dates extend through mid-July so the relative range is valid but not what I want for this scenario.

![DataZoe_3-1784088998886.png](https://community.fabric.microsoft.com/t5/image/serverpage/image-id/1355572iC6AF09422FFEA2FA/image-size/large?v=v2&px=999 "DataZoe_3-1784088998886.png")

*Figure: A date table that extends beyond the available sales data can make the relative range include future dates, creating an incomplete comparison period.*

You can account for this by using the filter pane and filters on this visual.

1. Select the date picker slicer
2. Open the **Filter** pane
3. Drag over the **Units sold** column or measure
4. Set filter type to **Advanced filter** and set show items when the value **is not blank**, then **Apply filter**

![DataZoe_4-1784089019944.png](https://community.fabric.microsoft.com/t5/image/serverpage/image-id/1355573iA4BD953D2CECCD5C/image-size/large?v=v2&px=999 "DataZoe_4-1784089019944.png")

*Figure: Filtering the slicer to dates where units sold is not blank limits the relative range to dates with actual data.*

Now the last date adjusts to the last date with units sold and filters the relative range to the last full month with units sold. The visual now shows again full months to compare to.

## Walkthrough: Format the slicer to be more compact

This date slicer can be formatted to take up just a single line!

![DataZoe_5-1784089042832.png](https://community.fabric.microsoft.com/t5/image/serverpage/image-id/1355575i907EFFD16EAE25C6/image-size/large?v=v2&px=999 "DataZoe_5-1784089042832.png")

*Figure: The date picker slicer can be formatted into a compact single-line control while still giving viewers access to relative and manual date ranges.*

1. Select the date slicer
2. Open the Format pane
3. Turn off the slicer header, note this also takes the clear all button off the visual so be sure to add a clear all slicers button.
4. Turn off the slider
5. Expand Text and turn off Summary
6. Expand Date Range and change font size to 18.
7. Expand Button and turn off Border, expand icon set it to Blue and 30 size
8. Go to Insert ribbon and choose Buttons dropdown and “Clear all slicers”, then change it to use icon instead of text.
9. Position the slicer and button above the visual to have a minimal date picker experience.

![DataZoe_6-1784089042834.png](https://community.fabric.microsoft.com/t5/image/serverpage/image-id/1355574iE03F5281C166FEBC/image-size/large?v=v2&px=999 "DataZoe_6-1784089042834.png")

*Figure: The date picker slicer can be formatted into a compact single-line control showing the selected range and can be utilized with the clear all slicers button to offer a quick way to clear selections.*

Selecting the calendar button on the right lets you pick a relative or manual range for your slicer without taking up a lot of space.

## Walkthrough: The report viewer can use the full functionality

Report viewers get the most out of this date slicer. They can pick their own relative range, choose a manual range, a single date, or clear the slicer easily.

- Pick a different relative range, then reset back to the published relative range when I want

![DataZoe_7-1784089063847.png](https://community.fabric.microsoft.com/t5/image/serverpage/image-id/1355577iDD8D7A2C38F4952D/image-size/large?v=v2&px=999 "DataZoe_7-1784089063847.png")

*Figure: Report viewers can change the published default by choosing their own relative range.*

- Pick a manual range from the calendar

![DataZoe_8-1784089063849.png](https://community.fabric.microsoft.com/t5/image/serverpage/image-id/1355576iA53672B11FE51BD4/image-size/large?v=v2&px=999 "DataZoe_8-1784089063849.png")

*Figure: Report viewers can change the published default by choosing their own manual range.*

- Pick a single date by selecting the same date twice.  
	![DataZoe_9-1784089081189.png](https://community.fabric.microsoft.com/t5/image/serverpage/image-id/1355578i7E5421011ABF64E6/image-size/large?v=v2&px=999 "DataZoe_9-1784089081189.png")  
	*Figure: Report viewers can change the published default by choosing their own single date.*
- Use the slider to quickly adjust the range.

![DataZoe_10-1784089081192.png](https://community.fabric.microsoft.com/t5/image/serverpage/image-id/1355579i35DDB3BA31A71417/image-size/large?v=v2&px=999 "DataZoe_10-1784089081192.png")

*Figure: Report viewers can change the published default by choosing their own range using the slider.*

If the report author leaves the Filter pane visible, viewers can also modify or clear filters on the slicer itself, such as removing the "is not blank" restriction added earlier.

Once they are done, they can reset the filters at the top of the page. If you find they would prefer it to reset automatically each time the report loads, you can also toggle on not keeping viewer filters persisted.

In the web this can be enabled in reading view, File > Settings.

![DataZoe_11-1784089093830.png](https://community.fabric.microsoft.com/t5/image/serverpage/image-id/1355580i00FF28827D2D9DA5/image-size/large?v=v2&px=999 "DataZoe_11-1784089093830.png")

*Figure: Viewer filter persistence controls whether report consumers return to their previous slicer choices or start from the report’s default settings, can be turned on in in the web report editing experience.*

And in Desktop it can be found in the Options dialog in current file report settings.

![DataZoe_12-1784089093835.png](https://community.fabric.microsoft.com/t5/image/serverpage/image-id/1355581i1BDFB9314430D61B/image-size/large?v=v2&px=999 "DataZoe_12-1784089093835.png")

*Figure: Viewer filter persistence controls whether report consumers return to their previous slicer choices or start from the report’s default settings, can be turned on in Desktop via the Options dialog.*

By default, report viewers filters persist so they can continue where they left off last time.

## Next steps

The date picker gives you full control over what date range you want to review while automatically keeping pace with new data as it arrives. Whether you're building executive scorecards, operational dashboards, or self-service reports, the date picker helps balance sensible defaults with viewer flexibility. It reduces manual maintenance while making it easier for report consumers to explore data on their own terms.

- **Learn more**: Explore the [Slicer visual in Power BI](https://learn.microsoft.com/power-bi/visuals/power-bi-visualization-slicer-visual) and [Create a relative date slicer and filter in Power BI](https://learn.microsoft.com/power-bi/visuals/desktop-slicer-filter-date-range) documentation.
- **Turn it on**: Enable **Date picker slicer** in **File** > **Options and settings** > **Options** > **Preview features** in Power BI Desktop.
- **Provide feedback**: [Your feedback](https://community.fabric.microsoft.com/t5/Desktop/Share-your-thoughts-on-date-picker-option-in-the-slicer-visual/m-p/5196792/highlight/true#M1469885) is important during preview.