---
title: "Power BI Progress Bar with Card Visual"
source: "https://databear.com/power-bi-progress-bar-create-one-using-the-card-visual/"
author:
  - "[[Boniface Muchendu]]"
published: 2024-09-15
created: 2026-08-04
description: "Learn how to create a dynamic Power BI Progress Bar using the native card visual. This guide shows you how to display progress efficiently without custom visuals."
Processed: "Unprocessed"
---
Are you looking to create a Power BI Progress Bar to enhance your reports with a clean and minimalistic design, without relying on custom visuals or complicated SVG images? You’re in the right place! In this blog post, we’ll show you the easiest way to create a dynamic progress bar card using Power BI’s native card visual.

The default visuals in Power BI Desktop offer limited options for displaying progress, often leaving you with just the gauge visual. While useful, gauges might not fit every design aesthetic or space constraint. Our approach leverages the flexibility of the card visual, allowing you to present progress in a horizontal format that’s both sleek and space-efficient.

So, let’s get started and transform the way you display progress in your Power BI reports!

![Progress Bar Card in Power BI Using the Native Card Visual](99.System/Attachments/Progress_Bar_Card_in_Power_BI_Using_the_Native_Card_Visual.png)

##### Step 1: Setting Up Your Data

Before we begin, ensure you have a measure that calculates the progress percentage. For this post, we’ll create a simple measure named Percentage Progress with a manual value for demonstration purposes.

Percentage Progress = 0.68

*Note: In a real-world scenario, this measure would be a dynamic calculation based on your data model.*

##### Step 2: Creating the Progress Bar Measure

Next, we’ll create a measure that generates the progress bar using emojis. This measure will calculate the number of filled and unfilled segments based on the Percentage Progress.

##### Create the Progress Bar Measure

1. In Power BI Desktop, go to the **Modeling** tab and select **New Measure**.
2. Name the measure Progress Bar and enter the following DAX formula:
Progress Bar =  
VAR Value = ROUNDUP(\[Percentage Progress\] \* 10, 0)  
VAR Remaining = 10 – Value  
RETURN  
REPT(“■”, Value) & REPT(“□”, Remaining)

###### Explanation:

- **Value**: Calculates how many segments should be filled by multiplying the percentage by 10 and rounding up.
- **Remaining**: Calculates the number of unfilled segments.
- **RETURN**: Uses the REPT function to repeat the filled (“■”) and unfilled (“□”) symbols accordingly.

*Tip: To insert the symbols “■” and “□”, press* *Windows +. to open the emoji panel and navigate to the symbols section.*

![emoji panel and navigate to the symbols section power bi](99.System/Attachments/emoji_panel_and_navigate_to_the_symbols_section_power_bi.png)

##### Step 3: Creating the Progress Subtitle Measure

We’ll add a subtitle to indicate the remaining percentage to reach the target.

1. Create another measure named Progress Subtitle:
Progress Subtitle =  
FORMAT(1 – \[Percentage Progress\], “Percent0″) & ” from Target”

###### Explanation:

- Subtracts the Percentage Progress from 1 to get the remaining percentage.
- Formats the result as a percentage with no decimal places.
- Appends the text ” from Target”.

##### Step 4: Building the Card Visual

Now, we’ll assemble the card visual and customize it to display our progress bar and subtitle.

##### Add the Card Visual

1. In the **Visualizations** pane, select the **Card** visual.
2. Resize the card to your desired dimensions.

##### Configure the Data Fields

1. Drag the Percentage Progress measure into the **Data field** of the card.

##### Customize the Card Visual

1. Open the **Format** pane (paint roller icon).
2. Under **Callout value**:
- Change the **Font** to **Arial**.
- Set the **Text size** to **16 pt**.
- Enable **Bold**
- Change the **Color** to your preferred color (e.g., black).
1. Rename the **Callout value** label to “Progress”.

##### Add Reference Lines for Progress Bar and Subtitle

1. In the **Format** pane, go to **Data label** and expand **Reference lines**.
2. Add two reference lines:
- **Line 1**:
	- **Value**: Select the Progress Bar
		- **Label**: Set to “Progress Bar”.
		- **Font size**: Adjust as needed.
		- **Color**: Choose a color that stands out (e.g., blue).
- **Line 2**:
	- **Value**: Select the Progress Subtitle
		- **Label**: Set to “Subtitle”.
		- **Font size**: Adjust as needed.
		- **Color**: Use a lighter color (e.g., gray) to differentiate it from the main progress value.

##### Remove Unnecessary Elements

1. Under **Category label**, turn off the **Title** to remove it from the card.
2. Under **General** settings, set the **Padding** to minimize whitespace.

##### Adjust Card Shape (Optional)

1. In the **Format** pane, go to **Card** settings.
2. Under **Shape**, set the **Style** to **Rounded Rectangle**.
3. Adjust the **Corner radius** to **5 px** for a subtle rounded effect.

##### Step 5: Final Touches

- **Test Dynamic Updates**: Change the value of Percentage Progress to see how the progress bar and subtitle update automatically.
- **Formatting**: Adjust fonts, colors, and sizes to match your report’s theme.
- **Alignment**: Ensure all elements are properly aligned within the card for a polished look.

##### Conclusion

You’ve now learned how to create a dynamic progress bar card using Power BI’s native card visual. This method provides a sleek, space-efficient way to display progress without relying on external visuals or complex graphics. By harnessing simple DAX functions and Power BI’s formatting options, you can enhance your reports and provide clearer insights to your audience.

Feel free to experiment with different symbols, colors, and formats to make the progress bar uniquely yours.

Unlock your full potential with Power BI. Visit our [training page](https://databear.com/power-bi-training/) to learn more and enroll today!