---
title: "Custom Formats in Power BI"
source: "https://medium.com/microsoft-power-bi/custom-formats-in-power-bi-5536b4c4fb3d"
author:
  - "[[Simon Harrison - Analytics]]"
  - "[[Power BI]]"
  - "[[SQL]]"
published: 2023-10-05
created: 2026-08-12
description: "More"
Processed: "Unprocessed"
---
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*q0bt9JNUWZrHKs6c.png)

This article originally appeared in our blog  
[Custom Formats in Power BI — Select Distinct](https://www.selectdistinct.co.uk/2023/07/20/custom-formats-in-power-bi/)

Custom Formats in Power BI allow you to create your own specific formats so that you are not limited to the pre-defined options that come as defaults

Some organisations have specific standards for things such as date formats, these can be catered for using custom formats

For example if you want your date formats to be dd-mm-yyyy 15–05–2023, then at first glance this option is not available

This quick guide shows you how you can set the formats that you need to make your reporting more flexible and look better

## Custom Formats on Cards

Cards are a great way to feature key pieces of information

But if you have a need to use a custom format that is not one of the standard formats then its not obvious how to do it

## Show data as Millions

select the card you want to format

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*Dvq-0xwVslc3topB.png)

On the Visualizations panel, select ‘Format Visual’, then in ‘Call out Value’ select the relevant display units

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*Loov7HMxSc0Ma2bY.png)

## Prefix with a plus or minus

By default, if the field we want to show on the card is set as a percentage, it looks like this

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*36EXwyBOGBNFI3C8.png)

To change the card to look as we want it, we need to go to the model and select a custom format in there

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*W4FjrwDFxAmmP7ao.png)

By setting the format to +0%; -0% the format will prefix all positives with a plus, the semi colon; then tells it to apply a different value for negatives

It now looks as we need it to

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*6RXwScEf487MFRmK.png)

## Show values as pence

If we set the field to be a currency format, in our case GBP then the value is expected to be in £

But, earnings per share for example are reported usually in pence

(So remember to multiply by 100! in your calculation)

Then we can set a custom format to show p suffix in a similar way, in this example we have not set a negative option

By using the format code 0.0p, this sets it to 1 decimal place

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*lUXww8wZEDWXFlSS.png)

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*kgKjhLEnI_JITqqD.png)

## Custom Format Strings

Custom format strings in Power BI allow you to unlock powerful formatting options allowing you to create the specific format you need

If you are familiar with this in Excel it is very similar

The syntax of the custom format allows you to define rules for each of positive values, negatives, zero values and text

The semi colon splits the rules into

\[Positives\];\[Negatives\];\[Zero\];\[Text Values\]

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*lWUuDkyQReeoR-lY.png)

Here are some common examples

If you want to explore this in more detail, the Microsoft Learn site has some good content  
[Microsoft Learn Site](https://learn.microsoft.com/en-us/power-bi/create-reports/desktop-custom-format-strings)

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*UvkGX3vO_3-MX6_1.png)

## Custom Formats for Dates

Here is an example for a common date format

At first, date formats appear to be limited to a few common formats

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*Nzhs8oJytGfIeP6I.png)

But if we want to use the format ‘dd-mm-yyyy ‘which is a very common requirement

then we need to create it as a custom format

On the modelling tab, select the field, then in the properties you can apply this custom format

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*zoeNghsNUG89ikW3.png)

Our dates now present themselves in the required format and still behave as dates as opposed to other workarounds which create the date as text

Mastering the array of options that you can apply using custom formats can give you more control over the look and feel of your reporting in Power BI

Subscribe to our channel to see more tips and timesavers

[Select Distinct YouTube Channel](https://www.youtube.com/channel/UC_DiGjuhpRbv6fE8cqD4QBg)

Or find other useful SQL, Power BI or other business analytics timesavers in our Blog

Our Business Analytics Timesavers are selected from our day to day analytics consultancy work. They are the everyday things we see that really help analysts, SQL developers, BI Developers and many more people.

Our blog has something for everyone, from tips for improving your SQL skills to posts about BI tools and techniques. We hope that you find these helpful!

[Business Analytics Blog](https://www.selectdistinct.co.uk/business-analytics-blog/)

> Don’t forget to subscribe to
> 
> 👉 [Power BI Newsletter](https://medium.com/microsoft-power-bi/newsletters/microsoft-power-bi-weekly)
> 
> and join our Power BI community
> 
> 👉 [Power BI Masterclass](https://linktr.ee/powerbi.masterclass)