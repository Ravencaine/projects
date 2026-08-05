---
title: "Subtitles in Power BI: Enhancing Visual Storytelling in Your Reports"
source: "https://databear.com/subtitles-in-power-bi-enhancing-visual-storytelling-in-your-reports/"
author:
  - "[[Boniface Muchendu]]"
published: 2023-07-02
created: 2026-08-04
description: "Explore how to use the newly introduced Subtitles feature in Power BI to enhance your reports. From storytelling and dynamic context updates to adding emojis and color-coding based on performance, the blog post covers it all."
Processed: "Unprocessed"
---
The recent Power BI update unveiled a seemingly modest yet powerful new feature – the subtitle. This function might appear small, but it holds immense potential to significantly amplify the narrative in your visualizations. I found this development particularly thrilling. Not only does it enable easier adherence to industry standards, but it also enriches your visuals with robust storytelling elements.

## Introducing Subtitles in Power BI

Traditionally, it was quite tricky to add new lines or subtitles to your titles, especially if you wanted to include formatting options. But, with this latest update, we no longer need to rely on janky workarounds; it’s natively available in Power BI.

Imagine you have a simple bar chart representing total sales based on category. With the new subtitle feature, you can add context, like “by category,” right below your title.

But that’s just the start; let’s delve deeper into how you can leverage this new feature.

## Storytelling with Subtitles

One of the first ways to use subtitles is for storytelling. You can add context or guide your users to view your visual in a certain way. Instead of just mentioning “by category,” why not narrate a story that your visual is representing? This approach aids your users in understanding what they’re viewing.

![Subtitles](99.System/Attachments/Subtitles.png)

## Visual Formatting with Subtitles

Subtitles, being part of the visual container, can be added to any visual in your report. From bar charts to card visuals, each can carry a subtitle for more context. For example, a card visual showing total sales can have a subtitle comparing it with a target value. It can be either static or dynamic, based on your requirements. You can even spice things up with emojis.

![Subtitle In Power BI with emoji](99.System/Attachments/Subtitle_In_Power_BI_with_emoji.png)

## Providing Information with Subtitles

Another smart use of subtitles is to provide instructions or information to your users. Let your users know what they can do with the bar chart, like how hovering over it will provide a percentage total.

You also have a variety of formatting options, such as aligning the subtitle to the right instead of left with the title. This provides a visual option to differentiate your title from the additional information.

![Providing Information with Subtitles in Power BI](99.System/Attachments/Providing_Information_with_Subtitles_in_Power_BI.png)

## Taking Subtitles to the Next Level – Dynamically

The real magic happens when you make the subtitles dynamic. They can change based on the context of user selections. Here’s how.

### Displaying Filters Applied with Subtitles

By using a DAX formula, you can create a dynamic element within the subtitle that changes based on user selection. Consider this formula:

*Selected Category = SELECTEDVALUE( ‘Table'\[Category Name\] )*

With this, you can display the selected category as a subtitle in your visual, updating it based on user interaction.

### Using Subtitles to Reflect KPI Status

Imagine having a target sales figure and you want your subtitle to reflect the status against that target. You can use a DAX formula to make it happen. Here’s how:

*Target Subtitle =* *IF(**SUM( ‘Table'\[Sales\] ) > 150000,**“🟢”,**“🔴”**)*

This formula compares the sum of sales with a set target (150,000 in this case). If the total sales exceed the target, it displays a green dot (🟢) emoji, otherwise a red dot (🔴).

### Changing Subtitle Color Dynamically

Adding a cherry on top, you can also change the color of your subtitles based on your selections or conditions. The same principle as above applies, but this time with color:

*Target Color = IF(SUM( ‘Table'\[Sales\] ) > 150000,”Green”,”Red”)*

## Conclusion

In summary, subtitles are a fantastic new addition to Power BI. They add context and make your visuals more informative and interactive. They allow you to narrate a story with your data, create dynamic subtitles based on user interaction, and add elements of color and emotive emoji reactions.

Stay tuned to our blog for more exciting Power BI features and tips.

You can visit the rest of our [blog](https://databear.com/blog/) posts for more insightful information on everything related to Power BI.

Learn more about Power BI by taking our training [course](https://databear.com/power-bi-training/).