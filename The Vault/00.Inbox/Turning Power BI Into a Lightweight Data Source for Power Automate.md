---
title: "Turning Power BI Into a Lightweight Data Source for Power Automate"
source: "https://medium.com/@jmwestendorp/turning-power-bi-into-a-lightweight-data-source-for-automate-ea1b01307bd2"
author:
  - "[[Jacob Westendorp]]"
published: 2026-08-02
created: 2026-08-11
description: "How Power BI and Power Automate work together to deliver small, well‑shaped signals where they matter"
Processed: "Unprocessed"
---
## How Power BI and Power Automate work together to deliver small, well‑shaped signals where they matter

*This article was written with assistance from AI. Read my note on AI writing at the bottom of this article*

Power BI is often treated as a destination — a place where data lands, gets modeled, and waits for someone to open a report. But the platform can do more than sit quietly behind a dashboard. With the right pattern, a dataset can participate directly in the flow of work, surfacing exactly the metric you need at the moment you need it.

One capability that makes this possible is Power Automate with a Power BI connector to run a DAX query. Instead of relying on scheduled refreshes, threshold‑based alerts, or manual report checks, you can query your dataset on demand and push a small, targeted signal into the tools where work happens. It’s a lightweight way to let a model speak — not just store information.

I use this pattern frequently for datasets built from files in SharePoint or OneDrive, especially when those files update irregularly. Power Automate can handle the housekeeping, such as triggering a refresh when a file changes. But the more interesting part is what happens after the refresh: you can query the dataset directly and send a concise snapshot of the current state to Teams, email, or any other workflow surface.

I frequently use Power Automate alongside Power BI for small, intermittent reporting scenarios. A common example is a dataset built from files stored in SharePoint or OneDrive — files that aren’t updated on a predictable schedule. In these cases, an Automate flow can handle the housekeeping, such as triggering a dataset refresh when a file is saved.

What caught my attention recently, though, was a lesser-known capability of the Power BI connector: Run a query against a dataset. This function unlocks the ability to query your Power BI model directly using DAX and return the results as a data stream that can be consumed elsewhere — such as a messaging or notification app. With just a bit of DAX, you can pull targeted outputs like last refresh timestamps, current-period values, or other high‑value metrics and push them exactly where they’re needed.

Power BI Desktop plays a key role in making this approach efficient. You can create and validate your measures there, then use the DAX Query View to refine and test the EVALUATE statement that will ultimately run inside Power Automate. Once you’re happy with the results, the query can be pasted straight into your flow.

Let’s pull all this together with a simple example.

The full flow is shown below, but the action that matters most is Run a query against a dataset.

![Screenshot of a Power Automate workflow with actions including dataset refresh and “Run a query against a dataset,” illustrating how DAX results move through the flow.](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*mpMZCDEVtKvQDvdTL9uhUw.png)

A Power Automate flow using “Run a query against a dataset” to pull targeted metrics from a Power BI model.

```c
EVALUATE
ROW(
 "Max_Date",max(Data[Report End of Month]),
 "Value This Month",[Current Month Value],
 "Percent Change",[Distinct Value Monthly % Chg]
)
```

The DAX itself is deliberately simple: a single row with three named values that represent exactly what the downstream message needs to display.

Where things become more interesting is the output from the Run a query against a dataset action. Rather than returning just the table, the connector wraps the results in a JSON array containing a significant amount of metadata — status codes, headers, and execution details.

As you can see below, the actual results table is nested inside this response. The task now is simply to extract that table from the array and shape it into something that can be easily consumed by a Teams.

![Screenshot of JSON output from the Power BI connector showing metadata fields and a nested rows array containing the DAX query results.](https://miro.medium.com/v2/resize:fit:1204/format:webp/1*4TLlTfunXQxDCwLhIT6-cQ.png)

The query output is wrapped in a JSON array containing metadata and a nested table of results.

Because this query returns only a small amount of data, a Select action is all that’s needed to target the rows array in the response and project just the fields required for the final message.

By using First table rows as the source and mapping each metric to a named output, you end up with clean, reusable values that can be passed directly to a Compose action.

![Screenshot of a Select action in Power Automate mapping fields from the query output using item() expressions.](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*aFc-n81MtYyjfuztlkd20g.png)

A Select action extracts the first row of the query results and maps each metric into clean, reusable fields.

While most of the mapping can be done with dynamic content, a small amount of manual expression work is required — dynamic elements can’t always be mapped directly in a Select action.

The basic structure uses an item reference to the query output, for example: item()?\[‘\[Max\_Date\]’\]

One small but important detail is that the query output wraps each measure name in square brackets (\[\]), and the reference must match that name exactly for the mapping to succeed.

Once this step runs, the output is dramatically simplified and ready to use in a message payload.

![Screenshot of a Compose action and a Teams message connector showing formatted output from the DAX query.](https://miro.medium.com/v2/resize:fit:1304/format:webp/1*9OiENcg1HlLVOOkhKrl7Tg.png)

The shaped metrics are composed into a message and posted directly into Teams, delivering context where work happens.

From this point on, the remaining steps are standard Power Automate actions. The shaped output can be passed into a Compose action to format the message and then posted to Teams or email as desired.

The real takeaway is the pattern: using Run a query against a dataset to turn a Power BI model into a lightweight, on‑demand data source. With a small amount of DAX and minimal shaping, Power BI can move beyond dashboards and become an active participant in automated workflows and notifications.

This pattern fills a gap that standard Power BI alerts don’t always address. Instead of broadcasting notifications broadly, it allows you to send a targeted, lightweight message containing only the metrics that matter, exactly when an upstream event occurs. There’s no dashboard to open, no threshold to tune, and no inbox clutter — just timely context delivered where work is already happening.

Stepping back, this pattern is part of a broader shift in how I’ve been using Power BI this year. The first article showed how a single datapoint can trigger an alert. This one shows how a scoped dataset can move through a workflow and surface exactly the context that matters. Once you see Power BI as something that can listen and speak, you start noticing all the places where a small, well‑shaped signal can remove friction. It becomes less about dashboards and more about interaction. Less about static reporting and more about letting the model participate in the flow of work.

The next step is extending that idea beyond alerts and into real operational context. When the data you care about needs human input or shared ownership, the pattern changes. Power BI still defines the population, but the interaction surface shifts to something collaborative. That is where SharePoint and Power Automate start working together to keep a living dataset aligned with the people who manage it. That is the direction I explore in the next article.

### A note on AI writing

I think one thing that gets lost in the “AI wrote this” conversation is how AI tools can function as training wheels. When I look back at what I wrote in early 2026, it’s cringy and obviously AI‑shaped. But it got me writing, it gave me a voice to start from, even when I wasn’t sure of myself. I could plunk out a rough draft and use AI to edit, transform, and craft my writing. It was great in that the tools used language, structure, and form that made my idea seem more impressive and artificially smooth.

Except it did not, not really, it puffed up and hyperbolized simple ideas and used more and more words to describe complex ideas until they lost meaning. Even with careful line by line editing, the writing was still not my own. I see that now and am working to develop as a better writer on my own. While I still use AI, I am consciously using less and less as I find a more authentic tone in my own work.