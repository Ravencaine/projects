---
title: "Show Values in Rows in Power BI"
source: "https://medium.com/microsoft-power-bi/show-values-in-rows-in-power-bi-642930d5a512"
author:
  - "[[Simon Harrison - Analytics]]"
  - "[[Power BI]]"
  - "[[SQL]]"
published: 2023-07-27
created: 2026-08-12
description: "More"
Processed: "Unprocessed"
---
Show values in rows in the matrix visual in Power BI

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*wIkJWSldXBtijdlCibMYwg.jpeg)

The Matrix visual in Power BI is similar to a Pivot Table in Excel, but not quite as intuitive, which can lead to many users being frustrated by an apparent lack of a way to do something which is straight forward in Excel

## Start with a simple Matrix Visual

We have a simple matrix with Category set as a row

And the values aggregating for Sales Amount and Order Quantity

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*Q-6WUIJbgyKTP7pw.png)

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*8N02Avs9C1F3DQ0A.png)

Now we need to apply a setting to change the positioning of the value fields

Make sure the visual is selected on the canvas by clicking on it

Then go to the Visualizations panel and click on the Format your visual icon

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*aIk-nkA86AEAJlgw.jpg)

Scroll down to the Values Section and hit the chevron to expand the options

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*Kehxef-IRqd3SqXK.jpg)

Then scroll down to the bottom of this section, and enable the option to switch values to rows option

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*vaDenvZ-pd6ptQmO.jpg)

Your matrix visual now shows values in rows

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*EWSzcMm45uMsBF5J.jpg)

Each Value field you add to the visual will add a new measure rows within each category

If you add a Sub Category to the rows beneath the Category the visual then shows a ‘+’ icon allowing you to expand down a level

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*c_IlfSTbQMQmZ5G8.jpg)

Clicking on the plus icon expands to show the subcategories

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*O27BzIA_wM9D4JZm.jpg)

Or, you can right click on the plus icon and select expand entire level to show all of the sub categories

## Adjust the Alignment

By Default the stepped layout indentation is not too clear

To Increase the indent, go to format visual, row headers and options

Increase the value using the slider to at least 20 to make the visual easier to read

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*YwxhI68RJmk5MuQg.jpg)

After increasing this value to at least 20 the matrix is much clearer to read

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*mjaipQGPlDFW_1iJ.png)

You now know how to switch values to rows in a matrix visual in Power BI

This Power BI Tip is one of those that is not immediately apparent

We often see users who are not aware of this setting who a struggling to find the way to set the matrix up as it needs to be

If you find this useful please like and share

Subscribe to our channel to see more Power BI tips and timesavers

[https://www.youtube.com/channel/UC\_DiGjuhpRbv6fE8cqD4QBg](https://www.youtube.com/channel/UC_DiGjuhpRbv6fE8cqD4QBg)

This post was originally featured in our Business Analytics Blog

[Show Values in Rows in Power BI — Select Distinct](https://www.selectdistinct.co.uk/2023/02/27/show-values-in-rows-in-power-bi/)

> Don’t forget to subscribe to
> 
> 👉 [Power BI Newsletter](https://medium.com/microsoft-power-bi/newsletters/microsoft-power-bi-weekly)
> 
> and join our Power BI community
> 
> 👉 [Power BI Masterclass](https://linktr.ee/powerbi.masterclass)