---
title: "Power Bi Alerts with DAX at Power Automate"
source: "https://community.fabric.microsoft.com/t5/Power-BI-Community-Blog/Power-Bi-Alerts-with-DAX-at-Power-Automate/ba-p/5314017?utm_source=powerbiweekly&utm_medium=email&utm_campaign=newsletter"
author:
published: 2026-07-23
created: 2026-08-08
description: "To query a Power BI Service semantic model, you need access to the dataset. There are several ways to do this, since it ultimately involves sending a"
Processed: "Unprocessed"
---
To query a Power BI Service semantic model, you need access to the dataset. There are several ways to do this, since it ultimately involves sending a request through the Power BI REST API.

[https://learn.microsoft.com/en-us/rest/api/power-bi/datasets/execute-queries-in-group](https://learn.microsoft.com/en-us/rest/api/power-bi/datasets/execute-queries-in-group)

Although we'll use Power Automate in this example, you could just as easily use an Azure Function or any other service capable of making API requests.

The first step is to verify that your DAX query returns the expected results. A convenient way to do this is with DAX Studio, which allows you to execute queries against tabular semantic models. If your dataset is hosted on a dedicated capacity, you can connect to it directly. If you're using Power BI Pro, you can open the original Power BI Desktop (.pbix) file and connect DAX Studio to it instead.

In my case, I want to receive a daily update every morning showing how this year's sales are performing. To do that, I'll execute a measure that returns a single row and a single column, filtered and formatted as needed. The DAX query looks something like this:

```markup
EVALUATE
    SUMMARIZE(
        FILTER('Orders',
        RELATED('Tablecalendar'[Year])= YEAR(NOW()))
    , "Venta", FORMAT( SUM(Orders[Sales]), "#,0.00")
)
```

I'll sum the sales from my fact table and filter them by the year of the current date using the related Calendar table. I'll also format the result with thousands separators and two decimal places.

Once I've confirmed the expected value, I can open Power Automate and create a scheduled (recurring) flow.

Next, we'll add the Run a query against a dataset action. This performs the same function as the Power BI REST API endpoint mentioned earlier. To process the tabular results, we'll add a Create CSV table action or Create HTML table, which converts the query output into a table. This gives us a structured output that we can use when composing the notification.

The Run a query against a dataset action lets you select the workspace, the semantic model (dataset), and provides a text box where you can paste the DAX query. For the Create CSV table action, we'll use only the first row, since the query is expected to return a single value.

![ibarrau_0-1784733058757.png](https://community.fabric.microsoft.com/t5/image/serverpage/image-id/1356555i89603A96F7F4609D/image-dimensions/871x542?v=v2 "ibarrau_0-1784733058757.png")

***Note**: If you want to build a more complex table, you can refer to the Power Automate documentation or community forums for additional guidance.*

Finally, we can send the results by email or as a Microsoft Teams message to a group or channel, ensuring the relevant stakeholders are kept informed about sales performance. Simply add the Output dynamic content from the Create CSV table action to the body of the email or Teams message.

![ibarrau_1-1784733249996.png](https://community.fabric.microsoft.com/t5/image/serverpage/image-id/1356556iA7C0DD59D1B653E5/image-dimensions/666x557?v=v2 "ibarrau_1-1784733249996.png")

Using this approach, you can create alerts or notifications for any result returned by a DAX query against a Power BI semantic model.

***Note**: None of the Power Automate actions used in this solution require a Premium license. You can build the entire flow using the standard Power Automate features included with Microsoft 365.*

I hope you find this useful for staying informed about the metrics that matter most through the communication channel of your choice, without relying solely on Power BI email subscriptions or mobile app notifications. I'm currently using this solution as main alert solution from KPIs.

[Original post in spanish at LaDataWeb](https://blog.ladataweb.com.ar/powerautomate-enviar-notificacion-de-una-dax-query/)

Top Kudoed Posts

| Subject | Kudos |
| --- | --- |
| ## Data Days \| Create | 58 |
| ## Data Days \| Connect | 47 |
| ## Power BI Dataviz World Champs \| Round 3 | 29 |
| ## Power BI Dataviz World Champs Barcelona \| Round 2 | 26 |
| ## Power BI Dataviz World Champs Barcelona \| Round 1... | 23 |

[View All](https://community.fabric.microsoft.com/t5/forums/kudosleaderboardpage/board-id/community_blog/timerange/one_month/page/1/tab/posts)

Latest Articles

- [Need a Running Total for Just One Chart? Power BI'...](https://community.fabric.microsoft.com/t5/Power-BI-Community-Blog/Need-a-Running-Total-for-Just-One-Chart-Power-BI-s-Visual/ba-p/5342327)
- [Data Days Contests | Announcing SQL + AI Promptath...](https://community.fabric.microsoft.com/t5/Power-BI-Community-Blog/Data-Days-Contests-Announcing-SQL-AI-Promptathon-Winners/ba-p/5341906)
- [The Hidden Architecture of Power BI Publishing Exp...](https://community.fabric.microsoft.com/t5/Power-BI-Community-Blog/The-Hidden-Architecture-of-Power-BI-Publishing-Explained/ba-p/5333695)
- [Power BI Dataviz World Champs Barcelona | Round 2...](https://community.fabric.microsoft.com/t5/Power-BI-Community-Blog/Power-BI-Dataviz-World-Champs-Barcelona-Round-2-Winners/ba-p/5332826)
- [Power BI Copilot Custom Instructions: Prep Data fo...](https://community.fabric.microsoft.com/t5/Power-BI-Community-Blog/Power-BI-Copilot-Custom-Instructions-Prep-Data-for-AI/ba-p/5332193)
- [Power BI Dataviz World Champs | Round 3](https://community.fabric.microsoft.com/t5/Power-BI-Community-Blog/Power-BI-Dataviz-World-Champs-Round-3/ba-p/5323477)
- [Community Sticker Challenge Barcelona 2026](https://community.fabric.microsoft.com/t5/Power-BI-Community-Blog/Community-Sticker-Challenge-Barcelona-2026/ba-p/5311346)
- [Power BI Copilot Set Limits](https://community.fabric.microsoft.com/t5/Power-BI-Community-Blog/Power-BI-Copilot-Set-Limits/ba-p/5321290)
- [Tired of Viewers Clicking "+" on Every Row? Power...](https://community.fabric.microsoft.com/t5/Power-BI-Community-Blog/Tired-of-Viewers-Clicking-quot-quot-on-Every-Row-Power-BI-s/ba-p/5322597)
- [Power Bi Alerts with DAX at Power Automate](https://community.fabric.microsoft.com/t5/Power-BI-Community-Blog/Power-Bi-Alerts-with-DAX-at-Power-Automate/ba-p/5314017)

Archives

- [08-02-2026 - 08-08-2026](https://community.fabric.microsoft.com/t5/Power-BI-Community-Blog/bg-p/community_blog/date/8-2-2026%2012%3A00%20AM)
- [07-26-2026 - 08-01-2026](https://community.fabric.microsoft.com/t5/Power-BI-Community-Blog/bg-p/community_blog/date/7-26-2026%2012%3A00%20AM)
- [07-19-2026 - 07-25-2026](https://community.fabric.microsoft.com/t5/Power-BI-Community-Blog/bg-p/community_blog/date/7-19-2026%2012%3A00%20AM)
- [07-12-2026 - 07-18-2026](https://community.fabric.microsoft.com/t5/Power-BI-Community-Blog/bg-p/community_blog/date/7-12-2026%2012%3A00%20AM)
- [07-05-2026 - 07-11-2026](https://community.fabric.microsoft.com/t5/Power-BI-Community-Blog/bg-p/community_blog/date/7-5-2026%2012%3A00%20AM)
- [06-28-2026 - 07-04-2026](https://community.fabric.microsoft.com/t5/Power-BI-Community-Blog/bg-p/community_blog/date/6-28-2026%2012%3A00%20AM)
- [06-21-2026 - 06-27-2026](https://community.fabric.microsoft.com/t5/Power-BI-Community-Blog/bg-p/community_blog/date/6-21-2026%2012%3A00%20AM)
- [06-14-2026 - 06-20-2026](https://community.fabric.microsoft.com/t5/Power-BI-Community-Blog/bg-p/community_blog/date/6-14-2026%2012%3A00%20AM)
- [06-07-2026 - 06-13-2026](https://community.fabric.microsoft.com/t5/Power-BI-Community-Blog/bg-p/community_blog/date/6-7-2026%2012%3A00%20AM)
- [05-31-2026 - 06-06-2026](https://community.fabric.microsoft.com/t5/Power-BI-Community-Blog/bg-p/community_blog/date/5-31-2026%2012%3A00%20AM)
- [05-24-2026 - 05-30-2026](https://community.fabric.microsoft.com/t5/Power-BI-Community-Blog/bg-p/community_blog/date/5-24-2026%2012%3A00%20AM)
- [05-17-2026 - 05-23-2026](https://community.fabric.microsoft.com/t5/Power-BI-Community-Blog/bg-p/community_blog/date/5-17-2026%2012%3A00%20AM)
- [05-10-2026 - 05-16-2026](https://community.fabric.microsoft.com/t5/Power-BI-Community-Blog/bg-p/community_blog/date/5-10-2026%2012%3A00%20AM)
- [View Complete Archives](https://community.fabric.microsoft.com/t5/blogs/blogarchivespage/blog-id/community_blog)