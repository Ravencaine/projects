---
title: "Power BI Feature News — Dynamic String Format for Measures"
source: "https://medium.com/microsoft-power-bi/power-bi-feature-news-dynamic-string-format-for-measures-ce1dd3176598"
author:
  - "[[Tomas Kutac]]"
published: 2023-04-26
created: 2026-08-12
description: "More"
Processed: "Unprocessed"
---
This new feature allows dynamically format displayed values for measures in Power BI visualizations. Typically we will use it in case we would like to change format of numbers based on its value or based on currency type. This helps to keep numbers in visualizations in compact format.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*GdiC5SHI7eFDq_eX4oJbCQ.png)

As this feature is still in preview we need first to activate it in Options menu:

![](https://miro.medium.com/v2/resize:fit:1348/format:webp/1*H5Mb-IAbpnIH7cc4jHVpPw.png)

Then when we choose any Measure, under Menu Measure Tools we can now set new Format —  *Dynamic:*

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*D3STKD0dlpobkS_j-qf8Aw.png)

Now we are able to use DAX language to format Measure values based on various conditions. The static format string the measure had before switching to Dynamic will be pre-populated as a string in the DAX formula bar.

## Simple scenario — condition within DAX code

Let’s say we would like to format numbers differently based on total displayed value. For this example we can use DAX function [SWITCH](https://learn.microsoft.com/en-us/dax/switch-function-dax):

```c
SWITCH (
    TRUE (),
    SELECTEDMEASURE () < 1000, “$#,##0”,
    SELECTEDMEASURE () < 1000000, “$#,##0,.0K”,
    “$#,##0,,.0M”
)
```

We will get this result in the visualization:

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*YsZ8Twqzaysd5fuvJijUVw.png)

Another scenario for Measure “Data Transferred”:

Code:

```c
SWITCH (
    TRUE (),
    SELECTEDMEASURE () < 1000, "#,##0 KB",
    SELECTEDMEASURE () < 1000000, "#,##0,.0 MB",
    "#,##0,,.0 GB"
)
```

Output:

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*-U65DtXSCOYvpnk8)

## Advanced Scenario — Conditions in separate table

But what if we would like to use specific country format? We can do it with supporting table where we will store different country formats.

Table with country formats:

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*8Stx4Oqz9D-fFAJBlVP2YQ.png)

Data model:

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*Zrmxspy6y3EWFmAas34aAg.png)

Dynamic String Format for measure using DAX function [SELECTEDVALUE](https://learn.microsoft.com/en-us/dax/selectedvalue-function):

```c
SELECTEDVALUE (
    ‘Country Currency Format Strings'[Format],
    “\$#,0.00;(\$#,0.00);\$#,0.00”
)
```

Number format will be changing automatically according its currency:

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*41ptYXRAzO5_VGo--wh4lQ.png)

That’s it for today. I hope you enjoy this article and don’t forget to give me claps… as many as you can.:-)