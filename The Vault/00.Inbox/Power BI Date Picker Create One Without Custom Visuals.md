---
title: "Power BI Date Picker: Create One Without Custom Visuals"
source: "https://databear.com/power-bi-on-screen-date-picker-no-custom-visual/"
author:
  - "[[Boniface Muchendu]]"
published: 2025-06-22
created: 2026-08-04
description: "Create an on-screen date picker in Power BI using only native features—no custom visuals or filter pane required."
Processed: "Unprocessed"
---
If you’re looking for a way to add an **on-screen date picker** in Power BI without relying on custom visuals or the filter pane, you’re in the right place. This detailed guide walks you through how to implement a clean, interactive single-date selector using only native Power BI features.

For those seeking a deeper understanding of Power BI, check out [Data Bear’s Power BI Training](https://databear.com/power-bi-training/).

##### Why Use an On-Screen Date Picker in Power BI?

Many users need the ability to select a **single date** not a range to filter their entire report. While Power BI’s default slicer shows a long list of dates or uses relative filters like “Today” or “Yesterday,” these options can be limiting.

Additionally, relying on the filter pane often isn’t ideal for dashboards meant for end users, especially when the pane is hidden or locked. An on-screen date picker provides a more intuitive and controlled experience.

##### Step-by-Step Guide to Building a Date Picker

##### 1\. Add the Date Field as a Slicer

Begin by dragging your `Date` field from the calendar table to the report canvas. Convert it into a slicer by selecting the slicer visualization.![Add the Date Field as a Slicer](99.System/Attachments/Add_the_Date_Field_as_a_Slicer.png)

##### 2\. Configure the Slicer to Use “After” or “Before”

Open the slicer dropdown and select either **After** or **Before**. This gives you a single date input with a calendar picker. Choosing “After” lets you define a start date, while “Before” lets you define an end date.![Configure the Slicer to Use "After" or "Before"](99.System/Attachments/Configure_the_Slicer_to_Use_!After!_or_!Before.png)

##### Understanding the Limitations of SELECTEDVALUE()

If you try to use `SELECTEDVALUE()` in your DAX measures with this slicer setup, you may notice that it returns blank. That’s because the slicer does not return a single value it returns a date range.

##### Solution: Use MIN or MAX Instead

- If you’re using **After**, apply the `MIN()` function.
- If you’re using **Before**, apply the `MAX()` function.

##### DAX Pattern for a Single-Date Filtered Measure

Here’s an example of a DAX measure that dynamically filters based on the selected date:

```
Single Day Total Sales = 
VAR _selectedDate = MIN('Calendar'[Date])  -- Use MAX for 'Before' slicer
RETURN
CALCULATE(
    [Total Sales Amount],
    TREATAS({_selectedDate}, 'Calendar'[Date])
)
```

The `TREATAS` function is used to propagate the selected date as a virtual relationship to your data model.![Understanding the Limitations of SELECTEDVALUE()](99.System/Attachments/Understanding_the_Limitations_of_SELECTEDVALUE().png)

##### Styling the On-Screen Slicer for Usability

To make the slicer more user-friendly:

- Turn off the slicer header for a cleaner appearance.
- Increase the font size to improve readability.
- Add a descriptive title such as “Select a Date.”
- Use a white rectangle behind the slicer to simulate a custom visual effect.
- Format slicer interactions consistently with the rest of the [report design](https://databear.com/power-bi-july-update/ "Power BI July Update").![Styling the On-Screen Slicer for Usability](99.System/Attachments/Styling_the_On-Screen_Slicer_for_Usability.png)

##### Apply the Pattern Across Measures

Any measure that depends on this date picker should follow the same logic. Create a dedicated folder in the fields pane (e.g., “Single Day Measures”) to keep these calculations organized and maintainable.

##### Final Results

You now have a fully interactive on-screen date picker that works across your Power BI report. No custom visuals. No reliance on the filter pane. Just native functionality implemented with thoughtful DAX and UI formatting.

##### Learn More

If you’re looking to advance your Power BI skills or train your team, visit [Data Bear’s Power BI Training](https://databear.com/power-bi-training/).