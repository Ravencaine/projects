---
title: "Integrate your Power BI report into Power Automate flows"
source: "https://medium.com/automates/integrate-your-power-bi-report-into-power-automate-flows-b13e2b623aac"
author:
  - "[[Javid R.]]"
published: 2025-03-08
created: 2026-08-09
description: "More"
Processed: "Unprocessed"
---
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*SIpJEc3XF5H0XZLAi7QhFg.png)

> End users of Power BI reports may have concerns like: “ **When I check Power BI report, I want to get feedback on certain items there. Is it possible to send an email automatically?**” or “ **People sometimes miss checking all reports which they need to check. Is it possible that they get notified about certain KPIs?**”. If you have been lately approached with similar concern, in this blog I will share with you 2 ways of integrating Power BI and Power Automate to satisfy such needs in your organization.

*To read the full story for free, click* [*here*](https://medium.com/@rzayevjavid/integrate-your-power-bi-report-into-power-automate-flows-b13e2b623aac?sk=ace051160ef99903ddd36ae377933243)*.*

Firstly, I will start with **Power Automate visual**. Both Power BI Service and Power BI Desktop has Power Automate visual which end users can use to run flows. You can access it through Visualizations pane:

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*RTHUPSheMQoVZstDbwaX8Q.png)

You will see the below window opened in your report page. Environment in which the flow will be built is set to your default environment — you may need to change the environment based on end users.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*2GaeabGVLxl34SVHtAQyIQ.png)

You need to add data for Power Automate as you normally add columns for other Power BI visuals.

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*8otgS4ieYa68Pw9_90mWwQ.png)

Later, you go to the visual, click three dots for “More Options” and select “Edit”.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*DdI5gQxS8l0oYj-cDPjA_w.png)

Now you can check either Templates and find something related there or use your ready flow by selecting and applying or can start from scratch by creating instant cloud flow as I preferred. In any case trigger for the flow will be set to “On Power BI button clicked”.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*FW8WGAHpL7jhaiALBV-PIw.png)

![](https://miro.medium.com/v2/resize:fit:1200/format:webp/1*7ynuegZ3LMZ59yPlt3zLbA.png)

If you check what trigger retrieves you will find out that several dynamic values are available for use for following actions.

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*1a201MlYylZtBbSjDONA_A.png)

You can use “Power BI data” dynamic value to retrieve all columns and their according values in a tabular form. I used it and put it into “Create HTML table” action, so I can use its output to send email(s).

![](https://miro.medium.com/v2/resize:fit:1194/format:webp/1*U8qopQ2DAifBPghdt5H7TQ.png)

I set up necessary actions to send emails to several managers whom certain data concerns. So, after all when the end user filters data and clicks the button as below:

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*aQUANMfckY9pnnPZGPz9iA.png)

what receiver will get looks like below:

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*hLHcqywvJGKtlYF_ejChbw.png)

Now let’s talk about second way of Power BI and Power Automate integration. It goes through **running queries in Power Automate against dataset** available in Power BI Service and retrieving values in tabular form.

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*LuuoLB0_yVRnb8ZlJDNX1A.png)

Either you can write query by yourself or copy it from Power BI Desktop as following. You go and click “Optimize -> Performance analyzer” ribbon and later click sequentially “Start recording”, “Refresh visuals” and “Stop”. After you expand “Table”, you can “Copy query” to use it in Power Automate or “Run in DAX query view” to see the query and its result and modify it in real-time basis if needed.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*0-2o3cfH3mR0y0WBzlbCSQ.png)

If you have filters on data, then query will retrieve filtered data. But, let’s assume you send this data to different stakeholders in different frequency. In this case, using filters on visual within Power BI is not a good option, that is why you will need to apply filters within query.

Besides, this query by default retrieves limited number of items, which you will see when you bump into TOPN function within query. This is not a good option either as your data might exceed that limit.

After you add filters and remove limit, you can add the query into “Query text” section in “Run a query against a dataset” action, which in my case looks like below:

```c
DEFINE
    VAR FirstDayPreviousMonth = EOMONTH(TODAY(),-2)+1
    VAR LastDayPreviousMonth = EOMONTH(TODAY(), -1)
 VAR __DS0FilterTable = 
  FILTER(
   KEEPFILTERS(VALUES('Financials'[Sale Date])),
   AND(
    'Financials'[Sale Date] >= FirstDayPreviousMonth,
    'Financials'[Sale Date] <= LastDayPreviousMonth
   )
  )

 VAR __DS0FilterTable2 = 
  FILTER(KEEPFILTERS(VALUES('Financials'[Profit])), 'Financials'[Profit] < 0)

 VAR __DS0Core = 
  SELECTCOLUMNS(
   KEEPFILTERS(
    FILTER(
     KEEPFILTERS(
      SUMMARIZECOLUMNS(
       'Contact Details'[Responsible Manager],
       'Financials'[Segment],
       'Financials'[Country],
       'Financials'[Product],
       'Financials'[Discount Amount],
       'Financials'[Profit],
       'Financials'[Sale Date],
       __DS0FilterTable,
       __DS0FilterTable2,
       "CountRowsFinancials", COUNTROWS('Financials')
      )
     ),
     OR(
      OR(
       OR(
        OR(
         OR(
          OR(
           NOT(ISBLANK('Contact Details'[Responsible Manager])),
           NOT(ISBLANK('Financials'[Segment]))
          ),
          NOT(ISBLANK('Financials'[Country]))
         ),
         NOT(ISBLANK('Financials'[Product]))
        ),
        NOT(ISBLANK('Financials'[Discount Amount]))
       ),
       NOT(ISBLANK('Financials'[Profit]))
      ),
      NOT(ISBLANK('Financials'[Sale Date]))
     )
    )
   ),
   "'Contact Details'[Responsible Manager]", 'Contact Details'[Responsible Manager],
   "'Financials'[Segment]", 'Financials'[Segment],
   "'Financials'[Country]", 'Financials'[Country],
   "'Financials'[Product]", 'Financials'[Product],
   "'Financials'[Discount Amount]", 'Financials'[Discount Amount],
   "'Financials'[Profit]", 'Financials'[Profit],
   "'Financials'[Sale Date]", 'Financials'[Sale Date]
  )

EVALUATE
 __DS0Core

ORDER BY
 'Contact Details'[Responsible Manager],
 'Financials'[Segment],
 'Financials'[Country],
 'Financials'[Product],
 'Financials'[Discount Amount],
 'Financials'[Profit],
 'Financials'[Sale Date]
```

You can use “First table rows” dynamic value to retrieve table columns and their corresponding values.

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*aFzftVEs0xptrvxojIwyhw.png)

You can also add actions to group and send data which concerns only the segment in their responsibility and maybe change CSS a bit as well to send the table data in a good-looking manner.

In my case, after building necessary actions, what managers received looks like below:

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*SpKnIXZJzcomhJmMZ8lr0A.png)

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*dJvCcacUU2HLwqK-C28Psg.png)

So, building your own logics via using these methods, you can integrate Power BI and Power Automate easily.

*I will continue to show how to use Power Automate for your automation needs. If you found this post helpful, you can support this blog post with clapping and your comments.*

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*0PPXNY4dMjRimzdF.png)

*This story is published on* [***autoMATEs***](https://medium.com/automates)*. Follow us to stay informed about the latest automation tool updates and practical tips.*

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*0PPXNY4dMjRimzdF.png)