---
title: "How to Change the data source in Power BI"
source: "https://medium.com/microsoft-power-bi/how-to-change-to-data-source-in-power-bi-59a7b21f1a95"
author:
  - "[[Simon Harrison - Analytics]]"
  - "[[Power BI]]"
  - "[[SQL]]"
published: 2022-08-03
created: 2026-08-09
description: "More"
Processed: "Unprocessed"
---
(And keep all your existing visuals, calculated columns and measures working)

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*0458ryTdXef5hXqSMN30OQ.png)

If you have been working with a static dataset in Power BI and you need to change it to become refreshable, this article outlines the steps and benefits of doing so

If you follow this carefully you will ensure that all of your existing visuals, calculated columns and measures will continue to work, making the change seamless

Always make a copy of your PBIX file before you start….just in case

At first glance there is no obvious way to change the data source

We will follow theses steps

1. Add a new refreshable data source
2. Copy the connection details from the new source
3. Apply the connection details to the old data source
4. Delete the new data source

**Step 1 — add the new refreshable data source**

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*l8LRQ06LQK68lloMZ_ugsQ.png)

**Step 2 — Copy the connection details from the new source**

You now have two data sources, the second one being your new refreshable connection

We will grab the details of this new connection

Right click and select edit query, then go to advanced editor

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*17xwPYLaU9EMEwTuMrl-yA.png)

**In the advanced editor**

Copy the code from this entire block

![](https://miro.medium.com/v2/resize:fit:1234/format:webp/1*7iqFKOE-c6LNfheMM3H1Tw.png)

Then close the advanced editor

**Step 3 — Apply the connection details to the old data source**

**Still in the power Query Editor**

Select the original dataset, and go into **its** advanced editor

**In the Advanced Editor**

Highlight all of the code

And paste the new code from the clipboard

Click ‘Done’, then Close and Apply

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*5SezYqH1ruC-QguGBJRnDQ.png)

**Step 4 — Now delete the second dataset**

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*-ewSSdCkMmqIlfPaDKHbbw.png)

The original CSV dataset is now replaced with the SQL connected dataset

Any calculated fields will still work and all visuals which referred to the original dataset will still work

**The Alternative**

The alternative would be to add the new refreshable data set, then you would have to individually change every visual, calculated field and measure to refer to your new data set. This would be a lot of work and not without risk of error, as well as being very boring

For more Business Intelligence tips covering SQL, Power Bi and Excel subscribe or follow our You Tube Channel

#PowerBI #PowerBIDataSource #PowerBITips

> Don’t forget to subscribe to
> 
> 👉 [Power BI Newsletter](https://medium.com/microsoft-power-bi/newsletters/microsoft-power-bi-weekly)
> 
> and join our Power BI community
> 
> 👉 [Power BI Masterclass](https://linktr.ee/powerbi.masterclass)