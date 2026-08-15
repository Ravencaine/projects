---
title: "A Practical Workflow for Building Better Power BI Dashboards with ChatGPT and Copilot"
source: "https://medium.com/microsoft-power-bi/a-practical-workflow-for-building-better-power-bi-dashboards-with-chatgpt-and-copilot-ad9f2f65a0cd"
author:
  - "[[James Bryant]]"
published: 2026-04-28
created: 2026-08-09
description: "How to use ChatGPT for thinking, Copilot for building, and both together to create more useful dashboards."
Processed: "Unprocessed"
---
## How to use ChatGPT for thinking, Copilot for building, and both together to create more useful dashboards.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*rkcL0J6rSygRPHCHS2RT5A.png)

Most dashboard articles start too late.

They start with the chart.

Pick a visual. Add a KPI card. Write a measure. Rearrange the page. Maybe ask AI to help speed things up.

That can be useful, but it skips the part where most dashboards actually go wrong.

They do not fail because someone picked the wrong chart. They fail because the thinking behind the dashboard was weak before Power BI ever opened. The business question was fuzzy. The data was messy. Too many KPIs made it onto the page. Or the visuals looked polished but did not help anyone decide what to do next. That is exactly the weakness the current draft identifies, and it is the right place to start.

This is where ChatGPT and Copilot can be genuinely useful, but not in the same way.

Treating them like interchangeable AI tools is the mistake.

Copilot is strongest inside Power BI. It helps you move faster once you are already in the report: generating visuals, suggesting DAX, and accelerating execution.

ChatGPT is more useful outside Power BI, where the work is often less structured: clarifying the question, shaping the workflow, drafting logic, prototyping cleanup steps, and pressure-testing whether the dashboard is telling the right story. That division is already central to your draft and is supported by the book’s own Copilot-versus-ChatGPT examples.

Used together, they are much more practical than either one used alone.

ChatGPT is most useful before and around the dashboard build.

It helps when you need to:

- turn a vague requirement into a clearer objective
- narrow down which metrics actually matter
- clean or structure messy data before it reaches Power BI
- draft DAX or Power Query logic that you can review
- explain tradeoffs and sharpen the narrative behind the dashboard

That matters because real dashboard work is messy long before the first visual appears.

A dashboard is rarely broken because the line chart should have been a bar chart. It is broken because nobody defined what the dashboard was supposed to help someone understand.

Copilot is most useful once you are inside Power BI and want less friction between idea and implementation.

It helps when you need to:

- generate a visual from a plain-language prompt
- create or refine DAX measures
- apply transformations in Power Query
- adjust layouts more quickly
- keep the work inside the Microsoft environment

That is why Copilot works best once the model is loaded and the problem is already reasonably well framed.

The short version is simple:

**Use ChatGPT for reasoning and prototyping.**  
**Use Copilot for execution and iteration inside Power BI.**

That is the workflow.

**🎁** [**Get friend links for all of our 1500> Power BI learning articles here**](https://powerbi-masterclass.short.gy/learning-database?utm_source=medium&utm_medium=medium-post&utm_campaign=database-medium-post-start) **🎁**

Here is the version that feels most realistic.

Before opening Power BI, use ChatGPT to tighten the business question.

Instead of:

“Build me a sales dashboard.”

Try:

“Help me design a sales dashboard for a VP of Sales who needs to know whether growth is coming from stronger pipeline coverage, better close rates, or bigger average deal size. Suggest the 5 to 7 most useful metrics and explain why.”

That does two important things. It reduces noise, and it forces the dashboard to be built around a decision instead of a blank page.

If the data is messy or the metric definition is unclear, use ChatGPT before you ever start building visuals.

That is especially important when the underlying dataset is unreliable.

In the rideshare example from the book, the dataset includes duplicate ride records, missing driver ratings, fare anomalies, and inconsistent timestamp formats. The case study specifically describes **247 duplicate rides, 18% missing driver ratings, fares showing $0 or over $500, and mixed date formats**.

That is not a visualization problem. That is a data-preparation problem.

And if that work is skipped, the dashboard can still look good while the story underneath is wrong.

Once the data model is in place, Copilot becomes much more useful.

You can prompt it to generate a first-pass visual, supporting metrics, and a draft layout directly in Power BI.

That is where it shines.

After the visuals are built, use ChatGPT as an external reviewer.

Paste in a screenshot or summarize what the dashboard shows and ask:

“What is this dashboard saying clearly, what is still confusing, and what question would an executive ask next?”

That step is underrated, but it is where dashboards often move from technically complete to actually useful.

Once the story is clearer, go back into Power BI and use Copilot to tighten the page, refine measures, or simplify the layout.

This back-and-forth is where the workflow becomes practical:

That is a much better working model than asking one tool to do everything.

Take the SaaS metrics example from the book.

The core question is whether the business should spend more on acquisition or retention based on what is happening in monthly ARR and churn. The book already provides a strong version of this prompt for both Copilot and ChatGPT.

Here is our SaaS data: monthly ARR over 12 months, new customer count, and churned customer count. Please analyze the trend, identify any unusual churn or growth periods, compare acquisition versus retention ROI, and recommend strategy going forward. Also include any risk factors or benchmarks we should watch.

- Month 6 showed a meaningful churn spike, with roughly **8% customer churn**
- Acquisition recovered some of that weakness later in the year, especially in months 9 through 12
- But relying on acquisition to offset retention weakness is risky
- Recommendation: prioritize retention improvements, especially onboarding, customer success outreach, and cohort monitoring, while continuing acquisition with closer ROI review

A strong response would not just summarize the numbers. It would point to the business implication.

For example:

That is useful because it goes beyond chart generation. It explains what may be happening and what leadership should care about.

- a line chart of monthly ARR
- annotations for major churn months such as month 6 and month 11
- a bar overlay showing churn versus new acquisition
- a supporting ARR growth measure
- a short first-pass recommendation to balance retention and acquisition based on the pattern

Show me subscription revenue trend over the last 12 months, highlight churn spikes, and recommend whether focus should be on acquisition or retention.

Inside Power BI, Copilot can respond with:

That is the distinction in action.

Copilot helps you get to a usable page faster.  
ChatGPT helps you think more clearly about what the page means.

The SaaS case is useful because it shows analysis and decision support.

The rideshare case is useful because it shows reality.

The book’s rideshare example walks through natural-language prompts for removing duplicates, managing missing values, correcting anomalies, and standardizing timestamps. It even gives sample responses such as removing duplicate records, filling blanks using mean or mode imputation, correcting unusual fares using historical averages, and standardizing timestamps to a single format.

That is exactly the kind of workflow practitioners need.

Not every dashboard project starts with strategy. Many start with a dataset that cannot be trusted yet.

And that is why the rideshare example is so valuable. It shows that ChatGPT is not just useful for brainstorming and summaries. It can help structure the cleanup work that makes the dashboard worth building in the first place.

The future of dashboard work is not just faster dashboard creation.

It is better thinking before the build, cleaner execution during the build, and clearer interpretation after the build.

That is why the combination of ChatGPT, Copilot, and Power BI is so useful when used well. Not because it removes the need for judgment, but because it gives thoughtful analysts a faster and more practical way to apply it.

That is the real workflow.

These examples come from the book, [Smart Dashboards with Power BI, ChatGPT and Copilot](https://www.amazon.com/Smart-Dashboards-Power-ChatGPT-Copilot/dp/B0GSH3BBLK), which goes deeper into practical workflows for using AI and Power BI together in real dashboard projects.

**💡** [**MUST TRY — Power BI GPT — Personal Power BI Learning Coach**](https://powerbi-masterclass.short.gy/pbi-gpt?utm_source=medium&utm_campaign=pbi-gpt-medium-post-end) **💡**

**Power BI Masterclass Article Classification**

**Level:** Intermediate

**Category:** AI

**Tags:** Tutorial, AI