---
title: "ChatGPT Thinks. Copilot Builds. Power BI Proves."
source: "https://medium.com/@Jamesabryant/chatgpt-thinks-copilot-builds-power-bi-proves-827a505d5b36"
author:
  - "[[James Bryant]]"
published: 2026-05-12
created: 2026-08-09
description: "More"
Processed: "Unprocessed"
---
A practical Power BI workflow for building smarter dashboards with AI

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*h2oR4KmEnv2wWn__E1rgKQ.jpeg)

Most dashboards do not fail because the visuals are ugly.

They fail because the dashboard does not answer a useful question.

Someone opens Power BI, drops a few charts onto the canvas, adds a slicer, creates a KPI card, and calls it finished. The dashboard may look organized. It may even impress people in the first meeting.

But then the real questions begin.

What does this trend mean?  
Which metric should the user care about first?  
Is this measure calculated correctly?  
Can the audience act on what they see?  
Will the dashboard still work when the data grows?

This is where the combination of **ChatGPT, Microsoft Copilot, and Power BI** becomes interesting.

Not because AI magically builds perfect dashboards.

It does not.

The real value is that each tool plays a different role:

**ChatGPT helps you think through the dashboard.**  
**Copilot helps you build faster inside Power BI.**  
**Power BI helps you validate, interact, and publish the finished report.**

That is the workflow analysts should pay attention to.

## A Simple Example: Sports Performance Analytics

In Chapter 5 of *Smart Dashboards with Power BI, ChatGPT, and Copilot*, we use a sports performance dashboard to show how this workflow works in practice.

The dashboard tracks athlete performance across several measures:

- Average speed
- Maximum strength
- Average endurance
- Speed and strength comparison by athlete
- Endurance trend over time
- Endurance improvement percentage

At first glance, this looks like a simple dashboard.

But the example is useful because it mirrors a common business problem: how do we move from raw performance data to insight someone can use?

A coach does not only need to know who is fastest.

A coach needs to know who is improving, who is consistent, who may be overworked, and who needs a different training plan.

That is the same issue business teams face every day.

A sales leader does not just need revenue by region.  
They need to know where momentum is changing.

A finance team does not just need expense totals.  
They need to know what is driving the variance.

An operations team does not just need cycle time.  
They need to know where the process is breaking down.

The sports dashboard is just an easy way to see the larger point: **a good dashboard turns data into decisions.**

## Use ChatGPT Before You Build Anything

The biggest mistake in Power BI is starting with visuals too early.

Before building the dashboard, ask ChatGPT to help define the purpose.

A useful prompt might be:

*I am building a Power BI dashboard for a track and field team. The dataset includes athlete name, event date, speed, strength, endurance, and event participation. What KPIs and visuals would help a coach evaluate athlete performance and training progress?*

That prompt does not ask ChatGPT to build the dashboard.

It asks ChatGPT to help frame the dashboard.

A strong response should help identify:

- Which KPIs belong at the top
- Which visuals explain the performance story
- Which filters or slicers users need
- Which metrics may require additional context
- What questions the dashboard should answer

For this example, ChatGPT might suggest:

**KPI cards**

- Average Speed
- Maximum Strength
- Average Endurance
- Endurance Improvement %

**Core visuals**

- Bar chart comparing speed and strength by athlete
- Line chart showing endurance over time
- Slicer for athlete name
- Supporting metric for improvement over time

That is a better starting point than randomly dragging fields onto a canvas.

ChatGPT is strongest here as a planning partner. It helps you think through the dashboard logic before you start designing the report.

## Use Copilot to Build Faster Inside Power BI

Once the dashboard structure is clear, Copilot becomes useful inside Power BI.

You can ask Copilot for tasks like:

*Create a bar chart comparing athlete speed and strength.*

Or:

*Create a line chart showing endurance over time by athlete.*

Or:

*Add KPI cards for average speed, maximum strength, and average endurance.*

This is where Copilot shines.

It works inside Power BI. It can help create visuals, suggest measures, and reduce the amount of manual report-building work. Instead of clicking through every configuration step, you can use natural language to get a first version on the canvas.

But Copilot is not a substitute for review.

You still need to check:

- Did it use the right fields?
- Is the aggregation correct?
- Does the visual answer the question?
- Does the DAX calculation behave correctly with filters?
- Will the report perform well with a larger dataset?

Copilot can accelerate the build.

It cannot replace judgment.

That distinction matters.

## KPIs Are Useful, But They Can Also Mislead

The dashboard includes KPI cards for average speed, maximum strength, and average endurance.

That makes sense. KPI cards are useful because they give users a quick read before they study the charts.

But every KPI has a weakness.

Take average speed.

If the dashboard shows:

**Average Speed: 8.30 m/s**

That number is helpful, but it is incomplete.

It does not tell you whether one athlete is consistently strong or wildly inconsistent. It does not show whether speed is improving. It does not explain whether a performance drop happened after a heavy training period.

This is a common dashboard problem.

A KPI can summarize the data so aggressively that it hides the real story.

That is why KPI cards should usually be paired with context:

- A trend line
- A comparison chart
- A target or benchmark
- A filterable detail view
- A short interpretation note

This is another good use for ChatGPT.

After building the first version, ask:

*What could this KPI be hiding, and what supporting visual would help explain it?*

That prompt often leads to better dashboard design.

The goal is not to add more charts.

The goal is to add the right context.

## The Endurance Trend Is Where the Dashboard Becomes More Useful

A bar chart tells you who is stronger or faster right now.

A line chart tells you who is improving.

That is a more valuable question.

In the sports performance dashboard, the endurance-over-time visual compares athletes across days. You can quickly see whether Jay, Jordan, and Kai are improving, flattening, or falling behind.

That changes the conversation.

Instead of asking, “Who has the best endurance today?” the dashboard helps ask:

- Who is improving fastest?
- Who is plateauing?
- Who may need a different training plan?
- Is the team improving overall?
- Are certain athletes responding better to the program?

This is where dashboards become more than reporting tools.

They become coaching tools.

In business terms, this is the difference between a static report and a decision-support system.

## Making the Dashboard Smarter With DAX

Chapter 5 also introduces an Endurance Improvement measure.

The idea is simple: compare an athlete’s first recorded endurance result with the most recent result, then calculate the percentage improvement.

A simplified version of the DAX measure looks like this:

Endurance Improvement (%) =  
VAR FirstEndurance =  
CALCULATE(  
AVERAGE(‘AthletePerformance’\[Endurance (min)\]),  
FIRSTDATE(‘AthletePerformance’\[Date\])  
)  
VAR LastEndurance =  
CALCULATE(  
AVERAGE(‘AthletePerformance’\[Endurance (min)\]),  
LASTDATE(‘AthletePerformance’\[Date\])  
)  
RETURN  
DIVIDE(LastEndurance — FirstEndurance, FirstEndurance) \* 100

This is a good example of how ChatGPT and Copilot can work together.

Copilot can help draft the measure inside Power BI.

ChatGPT can explain what the measure is doing, identify assumptions, and suggest improvements.

For example, you could ask ChatGPT:

*Explain this DAX formula that is easy to understand. What assumptions does it make, and how could it produce misleading results?*

That is an important question.

Because a DAX formula can be technically valid and still wrong for the business problem.

For example:

- Should the first date mean the athlete’s first event ever?
- Should it mean the first date in the selected filter period?
- Should the measure reset when a single athlete is selected?
- Should it compare against the previous month instead of the first event?
- What happens if the first endurance value is blank?

These are not minor details.

They determine whether the dashboard can be trusted.

## Interactivity Turns the Report Into an Exploration Tool

The dashboard also includes an athlete slicer.

That may seem basic, but it is important.

A static dashboard tells everyone the same story.

An interactive dashboard lets each user investigate the part of the story that matters to them.

When a coach selects Jay, the dashboard should focus on Jay’s performance. When Jordan is selected, all visuals should update. When Kai is selected, the endurance trend and KPI cards should reflect Kai’s results.

This kind of interactivity is one of Power BI’s biggest strengths.

It allows users to move from summary to detail without needing a separate report for every question.

But again, interactivity needs to be tested.

Filters can create confusion if measures do not respond as expected. A KPI card may look correct at the team level but behave strangely when filtered to one athlete. A line chart may show misleading results if the date field is not modeled properly.

This is why the final step is always validation.

AI can help build faster.

Power BI still has to prove the answer.

## The Real Workflow: ChatGPT First, Copilot Second, Power BI Always

The best workflow is not “use AI to build my dashboard.”

That is too broad.

A better workflow looks like this:

**1\. Use ChatGPT to define the dashboard purpose.**  
Ask what decisions the dashboard should support and which KPIs matter most.

**2\. Use ChatGPT to challenge the design.**  
Ask what each metric might hide, where users might misinterpret the data, and which visuals provide the right context.

**3\. Use Copilot to build the first version inside Power BI.**  
Generate visuals, draft measures, create slicers, and speed up the initial build.

**4\. Use Power BI to validate the model.**  
Check relationships, data types, filter behavior, DAX logic, and performance.

**5\. Use ChatGPT again to refine the story.**  
Ask whether the dashboard answers the original question clearly and what should be simplified.

This loop is where the productivity gain happens.

Not because AI does the work for you.

Because AI helps you move faster through the thinking, building, testing, and refinement cycle.

## The Bigger Lesson

The future of dashboard development is not just faster chart creation.

It is better thinking.

ChatGPT helps analysts ask better questions.  
Copilot helps turn those questions into working visuals.  
Power BI provides the environment where the data model, measures, interactivity, and publishing process come together.

The mistake is treating AI like a shortcut.

The opportunity is treating AI like a second analyst — one that can brainstorm, draft, explain, challenge, and accelerate the work while you remain responsible for the final answer.

That is the shift.

Dashboards are moving from static reports to intelligent decision systems.

And the best analysts will not be the ones who simply know which button to click.

They will be the ones who know what question the dashboard is supposed to answer.