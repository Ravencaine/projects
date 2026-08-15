---
title: "Excel REPT Function In Cell Charts • My Online Training Hub"
source: "https://www.myonlinetraininghub.com/excel-rept-function-in-cell-charts"
author:
  - "[[Mynda Treacy]]"
published: 2026-06-23
created: 2026-08-09
description: "Use the Excel REPT function to create in-cell bar charts, progress bars and star ratings. Dynamic mini charts without inserting chart objects."
Processed: "Unprocessed"
---
The Excel REPT function looks simple at first. All it does is repeat text a specified number of times.

But with the right symbols, fonts and formulas, REPT becomes a surprisingly powerful way to create mini charts directly inside cells allowing you to build dynamic dashboards like this:

![What is the REPT function in Excel?](https://d13ot9o61jdzpp.cloudfront.net/images/01-rept-function.png)

What is the REPT function in Excel?

You can use it to build:

- In-cell bar charts
- Progress bars
- Star ratings
- Simple dashboard visuals
- Compact visual summaries

Best of all, these visuals update automatically when your data changes, because they are driven entirely by formulas.

In this tutorial, you’ll learn how to use the REPT function to create visual reports in Excel without inserting a single chart object.

## Watch the Excel REPT Function Video

![](https://www.youtube.com/watch?v=7vM2Y5PboWI)

[![Subscribe YouTube](https://d13ot9o61jdzpp.cloudfront.net/images/subscribe.png)](https://www.youtube.com/c/MyOnlineTrainingHub?sub_confirmation=1)  
![](https://www.youtube.com/watch?v=subscribe_embed)

## Get the Free Example File with Mini Dashboard

Enter your email address below to download the free file.

By submitting your email address you agree that we can email you our Excel newsletter.

## What Does the REPT Function Do in Excel?

The REPT function repeats text a specified number of times.

**The syntax is:**

```
=REPT(text, number_times)
```

**For example:**

```
=REPT("-",10)
```

**Returns:**

```
----------
```

The first argument is the text you want to repeat. The second argument is the number of times to repeat it.

That text can be a normal character, such as a dash, or it can be a symbol, such as a block, star or shade character.

This is where REPT becomes useful for visual reporting.

## Important REPT Function Behaviour

There is one important detail to understand before building charts with REPT.

If you give REPT a decimal number, Excel rounds it down.

For example:

```
=REPT("█",3.9)
```

This returns 3 blocks, not 4.

That matters when you’re converting percentages, scores or sales values into visual bars. In some cases, you’ll need to use ROUND, ROUNDDOWN or another rounding function to control the result.

## Example 1: Create an In-Cell Bar Chart with REPT

Let’s say you have product sales data and you want to compare each product visually.

![How to create an in-cell bar chart in Excel using the REPT function?](https://d13ot9o61jdzpp.cloudfront.net/images/02-rept-function.png)

How to create an in-cell bar chart in Excel using the REPT function?

You could use Conditional Formatting Data Bars, but they have limitations. For example, colour coding can be harder to customise because the data bar itself is controlled by Excel’s conditional formatting settings.

With REPT, the bar is simply text inside a cell. That means you can use font formatting and conditional formatting together to create more customised effects.

**Step 1: Insert the Block Character**

To create a bar chart, use a solid block character.

You can insert it from:

Insert > Symbol

Set the font to Arial, then choose the Block Elements subset.

![How to insert symbols in Excel's REPT function?](https://d13ot9o61jdzpp.cloudfront.net/images/03-rept-function.png)

How to insert symbols in Excel's REPT function?

Insert the full block character:

█

Copy it to the clipboard so you can paste it into your formula.

**Step 2: Write the REPT Bar Chart Formula**

Assume your sales values are in an Excel Table column called Sales.

Use this formula:

```
=REPT("█",[@Sales]/MAX([Sales])*20)
```

Here’s how it works:

```
[@Sales]/MAX([Sales])
```

This divides each product’s sales by the highest sales value in the Sales column.

That gives each row a value between 0 and 1.

Then this part:

```
*20
```

sets the maximum length of the bar to 20 characters.

So the product with the highest sales gets a full 20-character bar, and the other products get shorter bars relative to that maximum value.

**Step 3: Use a Monospaced Font**

For best results, format the bar chart cells with a monospaced font, such as Consolas.

A monospaced font gives every character the same width, which makes the bars line up neatly.

Without a monospaced font, some bars may appear uneven even when the formula is correct.

**Add Conditional Formatting to REPT Bar Charts**

Because the REPT bar is text, you can apply conditional formatting based on the underlying sales value.

For example, you might use:

```
=$D7>9000
```

to format high sales values in green.

Then add more rules, such as:

```
=$D7>7000
```
```
=$D7>6000
```
```
=$D7<=6000
```

Each rule can apply a different font colour to the bar.

![How to use Conditional Formatting with REPT function in Excel?](https://d13ot9o61jdzpp.cloudfront.net/images/04-rept-function.png)

How to use Conditional Formatting with REPT function in Excel?

When using conditional formatting formulas, make sure the row reference is relative. For example, use $D7, not $D$7, so Excel checks each row in the table.

You can then open the Conditional Formatting Rules Manager and arrange the rules in the correct order.

This gives you a dynamic in-cell bar chart where both the bar length and the colour respond to the data.

## Example 2: Create a Progress Bar in Excel with REPT

A basic REPT bar chart is useful for comparing values, but you can take the idea further by creating a progress bar.

A progress bar shows both the completed portion and the remaining portion.

For example, you might use it for:

- Project completion
- Course progress
- Task status
- Budget usage
- Goal tracking
- Sales target achievement

To build this, you need two symbols:

A solid block for the completed section:

█

A lighter shade character for the remaining section:

▒

**Excel Progress Bar Formula with REPT and LET**

Assume your completion rate is in a column called Completion Rate.

Use this formula:

```
=LET(
width,20,
filled,ROUND([@[Completion Rate]]*width,0),
REPT("█",filled)&REPT("▒",width-filled))
```

This formula creates a progress bar that is always 20 characters wide.

![How to create a progress bar in Excel using the REPT function?](https://d13ot9o61jdzpp.cloudfront.net/images/05-rept-function.png)

How to create a progress bar in Excel using the REPT function?

**How the Formula Works**

The LET function allows you to name parts of the calculation, making the formula easier to read.

This part:

```
width,20
```

sets the total width of the progress bar to 20 characters.

This part:

```
filled,ROUND([@[Completion Rate]]*width,0)
```

calculates how many characters should be filled.

For example, if the completion rate is 90%, Excel calculates:

```
90% of 20 = 18
```

So the progress bar will have 18 filled blocks.

The ROUND function is important because REPT needs a whole number of characters.

Then this part creates the completed section:

```
REPT("█",filled)
```

This part creates the remaining section:

```
REPT("▒",width-filled)
```

The ampersand joins the two parts together:

```
&
```

So if the width is 20 and the completed portion is 18, the formula returns 18 solid blocks and 2 lighter shade blocks.

**Progress Bar Precision**

The width controls the level of detail.

If your progress bar is 20 characters wide, each character represents 5%.

That works well for a compact visual indicator.

However, values like 93% and 95% may look the same because they round to the same number of blocks.

If you need more precision, increase the width to 50.

You can also use narrower characters, such as the pipe symbol accessed with **SHIFT + \\**:

![How to enhance the progress bar in Excel created using REPT function?](https://d13ot9o61jdzpp.cloudfront.net/images/06-rept-function.png)

How to enhance the progress bar in Excel created using REPT function?

This allows you to create a more detailed progress bar without making the column too wide.

## Example 3: Create Star Ratings with REPT

REPT can also be used to create star ratings.

This is useful for:

- Product reviews
- Customer ratings
- Employee performance scores
- Service ratings
- Quality assessments
- Survey results

For a rating out of 5, you can use filled and unfilled stars.

Filled star:

```
★
```

Unfilled star:

```
☆
```

You can insert these symbols manually, or generate them with the UNICHAR function.

The filled star is:

```
=UNICHAR(9733)
```

The unfilled star is:

```
=UNICHAR(9734)
```

**Excel Star Rating Formula with REPT**

![How to create a star rating using Excel's REPT function?](https://d13ot9o61jdzpp.cloudfront.net/images/07-rept-function.png)

How to create a star rating using Excel's REPT function?

Assume your score is in a column called Score.

Use this formula:

```
=REPT("★",[@Score])&REPT("☆",5-ROUNDDOWN([@Score],0))
```

The first part creates the filled stars:

```
=REPT("★",[@Score])
```

If the score is 4, Excel repeats the filled star 4 times.

The second part creates the unfilled stars:

```
REPT("☆",5-ROUNDDOWN([@Score],0))
```

This subtracts the rounded down score from 5 to calculate how many empty stars are needed.

For example, if the score is 4, the formula returns 4 filled stars and 1 unfilled star.

**What About Half Stars in Excel?**

If your scores include values like 4.5, you may wonder whether you can show half stars.

Unfortunately, Excel cannot shade half of a character, and there is no standard Unicode character for a half-filled star that works reliably in every Excel setup.

The simplest and most reliable option is to round the rating to whole stars.

For example, a score of 4.5 can be shown as 4 filled stars if you’re rounding down, or 5 filled stars if you prefer to round to the nearest whole number.

For dashboard clarity, whole stars are usually easier to read and more reliable across different machines, fonts and Excel versions.

## Why Use REPT Instead of Excel Charts?

The REPT function is not a replacement for full Excel charts, but it is ideal when you want compact visuals inside a table.

Use REPT when you want to:

- Keep visuals inside worksheet cells
- Create simple dashboard indicators
- Avoid inserting chart objects
- Build compact reports
- Create dynamic formula-driven visuals
- Format visuals with standard font tools
- Combine formulas with conditional formatting

REPT charts are especially useful in dashboards where space is limited and you want users to scan the data quickly.

**REPT vs Conditional Formatting Data Bars**

Conditional Formatting Data Bars are quick and easy, but REPT gives you more control in some situations.

![How to format databars using Excel's Conditional Formatting?](https://d13ot9o61jdzpp.cloudfront.net/images/08-rept-function.png)

How to format databars using Excel's Conditional Formatting?

Data Bars are useful when you want a fast visual bar with minimal setup.

REPT is useful when you want more control over the characters, symbols, colours, layout and formula logic.

For example, with REPT you can create:

- Custom bar styles
- Progress bars with completed and remaining sections
- Star ratings
- Text-based dashboard indicators
- Formula-driven visual effects

Because the output is text, you can use normal font formatting and conditional formatting to control the appearance.

## Best Practices for REPT Charts in Excel

**Use a Monospaced Font**

Use fonts like Consolas or Courier New for bar charts and progress bars.

This keeps each character the same width and makes the bars align correctly.

**Use Excel Tables**

[Excel Tables](https://www.myonlinetraininghub.com/excel-tables) make formulas easier to read because they use structured references, such as:

```
[@Sales]
```

and:

```
[Sales]
```

Tables also automatically copy formulas down as new rows are added.

**Control the Maximum Bar Width**

Use a fixed number, such as 20 or 50, to control the length of your visual.

For example:

```
*20
```

creates a compact bar.

A larger value gives more detail but requires more column width.

**Be Careful with Decimals**

REPT rounds decimal values down.

Use ROUND, ROUNDDOWN or ROUNDUP when you need precise control over the result.

**Use Symbols That Display Reliably**

Some symbols may look different across fonts, devices and Excel versions.

For reliable results, test your symbols with the font you plan to use.

Common choices include:

█

▒

★

☆

|

## Final Thoughts

The REPT function may look basic, but it can do far more than repeat text.

With a few symbols and the right formulas, you can use REPT to create in-cell bar charts, progress bars and star ratings that update automatically when your data changes.

These formula-driven visuals are ideal for dashboards, reports and compact tables where you want quick insight without adding chart objects.

And once you understand this technique, you can adapt it to many different types of data, from sales performance and task completion to product ratings and KPI dashboards.

If you’re ready to take your Excel dashboards further, my [Excel Dashboards Course](https://www.myonlinetraininghub.com/excel-dashboard-course) shows you how to build professional, interactive dashboards from start to finish. You’ll learn how to structure your data, create meaningful visuals, add interactivity with slicers and controls, and design dashboards that are clear, polished and easy to use.

You can learn more about the [Excel Dashboards Course here](https://www.myonlinetraininghub.com/excel-dashboard-course).

## Frequently Asked Questions

### What is the REPT function in Excel?

The REPT function repeats text a specified number of times. It is commonly used for repeating characters, but it can also be used to create in-cell charts, progress bars and ratings.

### Can REPT create charts in Excel?

Yes. REPT can create simple text-based charts inside cells by repeating symbols such as blocks, stars or lines.

### How do I create a progress bar in Excel with a formula?

You can create a progress bar with REPT by repeating one symbol for the completed section and another symbol for the remaining section. A formula using LET and REPT makes this easier to manage.

### Why do my REPT bars look uneven?

Your bars may look uneven if you’re using a proportional font. Use a monospaced font, such as Consolas, so every character has the same width.

### Does REPT work with percentages?

Yes. You can multiply a percentage by a fixed width to calculate how many characters should appear in the bar. Use ROUND if you want to control how percentages are converted into whole characters.

### Can Excel show half stars with REPT?

Not reliably. Excel cannot shade half of a character, and half-star symbols are not consistent across all fonts and systems. Whole-star ratings are usually clearer and more reliable.

### Is REPT better than conditional formatting data bars?

REPT is not always better, but it gives you more flexibility. Conditional Formatting Data Bars are faster to apply, while REPT gives you more control over symbols, colours and formula logic.