---
title: "Dynamic Format Strings in Power BI"
source: "https://databear.com/dynamic-format-strings-in-power-bi/"
author:
  - "[[Annamarie Van Wyk]]"
published: 2024-03-02
created: 2026-08-04
description: "Learn how to change the format of numbers in one measure by using the Dynamic format strings in Power BI and build beautiful reports."
Processed: "Unprocessed"
---
In this post, I’m going to show you how to use dynamic format strings in Power BI to make your measures look awesome. Dynamic format lets you change the way your measures appear in visuals based on conditions or context. For example, you can add currency symbols, abbreviate large numbers, or apply different decimal places depending on the value.

You may wonder why you would need this, but this gives you the ability to format different number format in one table or graph. For example:

To use dynamic format strings, you need to enable the feature in Power BI options (it’s still in preview as of November 2023).

## Setting up Dynamic Format strings in Power BI

Then, you need to select the measure you want to format and choose Dynamic from the Format list box in the Measure tools ribbon.

Measure Before switching to dynamic

Measure After switching to dynamic

A new list box will appear next to the DAX formula bar where you can switch between the measure expression and the format string expression. Choose Format on the drop down.

After choosing format

The format string expression is a DAX expression that returns a valid format string for your measure. You can use any DAX function or logic to create your expression, as long as it outputs a string.

Below is an example, I used the switch function.

You can see how these dynamic format strings affect the visuals in the report below:

I hope this report was helpful and informative. Dynamic format strings are a powerful and flexible way to customize your measures and make your reports more appealing and professional. If you have any questions or feedback, please let me know in the comments section. Also visit the [Microsoft page](https://learn.microsoft.com/en-us/power-bi/create-reports/desktop-dynamic-format-strings) with more details. Thanks for reading!

Don’t forget to visit our [training page](https://databear.com/power-bi-training/) to learn all you can about Power BI. Also see our other blog posts [here](https://databear.com/blog/).