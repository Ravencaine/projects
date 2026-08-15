---
title: "Power Automate for Power BI visualization"
source: "https://medium.com/@michalmolka/power-automate-for-power-bi-visualization-2c0801ce9fd5"
author:
  - "[[Michal Molka]]"
published: 2022-04-01
created: 2026-08-09
description: "More"
Processed: "Unprocessed"
---
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*r1T-eLrzs4hCRZTuc6sqgg.png)

One of useful Power Platform functionalities is Power Automate. For instance, you can create and invoke automated flows inside Power BI through a **Power Automate for Power BI visualization**. Visual is available out of the box.

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*caKYRr1MkSzMIbYI_UZ7nA.png)

The first step is to add fields from your data model which are supposed to be used in the flow. It isn’t a obligatory step, you can develop a flow without using data from the model.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*2OaPMJBor5Lsu-t1FGDs8g.png)

The next step is to edit the visualization.

You can use a template — at the bottom. In this case we create a flow from scratch. So that, pick New -> Instant cloud flow.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*2SsKzKqPnkxxub6Nd1E6LQ.png)

Our flow inserts rows to an Excel file placed on OneDrive every time it is invoked. Thus, we need to create an Excel file comprises a table with following structure.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*8DCuadmzTjJL_U4XMualMQ.png)

This table should be formatted as a table.

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*v704ywMabT31AWNhEONISw.png)

Add an **Add a row into a table** step in the flow and fill necessary fields.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*nQaJsDtJsi2jiGu6hbYppg.png)

Add values from your data model to respective fields.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*RTc2_suOnmXUNhMaWscYoQ.png)

You can save and apply your flow.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*JmksG_qImle05ARMzntBNA.png)

After you return to the main page, you need to remember to apply the flow.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*jC3-hPD99uDf0mYuo2boNg.png)

Your flow is good to go. You can adjust a button appearance.

![](https://miro.medium.com/v2/resize:fit:1266/format:webp/1*xyKPvaIAvruHAdZzvC4ctQ.png)

It is the time for a test. I’ve created a Matrix table. Let’s assume that we want to add records concerning Polk county for dates between 1/1/2019 and 7/1/2019.

![](https://miro.medium.com/v2/resize:fit:1376/format:webp/1*LfNd1xErJ2qvxwvgeL6vKQ.png)

Once you hit the button, you have new records inserted in the Excel file.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*i94DFJt0RfynTKbrYLijfA.png)

Let’s go further, make possible a report dataset refreshing directly in the report.

Create another Power Automate: a **Refresh a dataset** visualization

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*PTZ3TG7wcURf5p2wND12Zg.png)

Apply a flow to the visualization.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*v8YNNUCxkvD4RZHH7e_84g.png)

Format button and invoke.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*n_2jo9HrfcFPKNVmm2HZew.png)

The dataflow has been refreshed.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*OitlgMteUK1uCXr6IDyNSA.png)