---
title: "ChatGPT + Copilot for Power BI:"
source: "https://medium.com/@Jamesabryant/chatgpt-copilot-for-power-bi-bafc01763094"
author:
  - "[[James Bryant]]"
published: 2026-05-19
created: 2026-08-09
description: "More"
Processed: "Unprocessed"
---
## The Two-Layer Workflow That Actually Works

How to use them for different jobs and why teams using only one are leaving the most valuable part on the table.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*7m_Zvo6fZQZF7KilmktShA.jpeg)

Most executive dashboards answer one question well.

**What happened?**

Revenue last quarter. Headcount changes. Pipeline coverage. That’s useful work, and it’s the easy part. But for high-stakes decisions, it’s not what executives actually need.

The question that matters is different.

*What should we be paying attention to before the decision gets made for us?*

That single shift from reporting on the past to surfacing what deserves attention now is where most “AI in BI” advice falls apart. Teams reach for ChatGPT or Copilot, expect one of them to magically produce a better dashboard, and end up with prettier charts that still answer the wrong question.

The fix is not picking the right tool. It’s using both for the right job.

## The Two-Layer Workflow

In Chapter 6 of *Smart Dashboards with Power BI, ChatGPT, and Copilot*, we call this the two-layer AI workflow. It’s a simple framing, but it changes how teams approach dashboard design from the first conversation.

**Layer 1: ChatGPT for upstream design.** This is the thinking layer, the work that happens before anyone opens Power BI. What decision should this dashboard support? What’s a leading indicator versus a lagging one? What would turn a normal signal into a real warning?

**Layer 2: Copilot for in-platform execution.** This is the building layer, the work inside Power BI. Drafting DAX measures. Suggesting visuals. Summarizing model output in plain language for stakeholders who don’t read DAX.

Most teams pick one tool and try to do both jobs with it. That’s where they lose leverage.

## Layer 1: Why ChatGPT Belongs Before the Dashboard, Not Inside It

The temptation with ChatGPT is to ask it to build the dashboard. That doesn’t work well, ChatGPT doesn’t know your decision, your audience, your risk tolerance, or your politics. You get generic output.

The real value is upstream.

Use it to pressure-test the decision logic before any visual gets built. For an M&A dashboard, that means working through questions like:

- What separates normal deal noise from a real warning sign?
- What does an executive need to grasp in 30 seconds versus what triggers a deeper review?
- Which signals are leading indicators of deal risk, and which only confirm what already happened?
- What external data sources like sentiment feeds, regulatory databases, commodity indexes would actually change the picture?

ChatGPT is good at organizing this thinking. It can take a vague request like “we need a dashboard for the deal team” and turn it into a specific framework with named signals, thresholds, and alerting rules. That framework is what you build against.

It will not replace business judgment. The team still has to bring that. But getting from blank page to working framework takes hours, not weeks.

## Layer 2: Why Copilot Earns Its Keep Inside Power BI

Once the decision logic is clear, the build phase begins and this is where Copilot does its best work.

Inside Power BI, Copilot can:

- Suggest visuals based on the questions you’re trying to answer
- Draft DAX measures from natural-language descriptions
- Build Q&A experiences that let non-technical users explore the data
- Summarize model output in plain English — for example, *“Sentiment declined 12% following FTC inquiry update”* — without requiring an analyst to write the prompt from scratch

What Copilot won’t do is rescue a weak data model or invent the framing. If nobody knows what the dashboard is supposed to help people decide, more charts won’t fix that.

Copilot is acceleration, not direction.

The two tools pair deliberately. ChatGPT helps you decide *what* to build. Copilot helps you build it *faster*.

## What This Looks Like in Practice: The M&A Example

Chapter 6 uses M&A as the running case because acquisitions show the gap between reporting and decision support more clearly than almost any other scenario.

The signals that move the needle on whether a deal closes are usually scattered. Analyst commentary is shifting tone, even while the stock holds steady. Investor sentiment looks strong, but regulators are asking tough questions. The closing timeline is starting to slip, while the headline narrative still looks fine.

A normal dashboard shows each of those in a separate tile. A smarter dashboard, one built using the two-layer workflow connects them.

**In Layer 1**, ChatGPT helps the team work out which signals matter, what thresholds should trigger alerts, and how sentiment, regulatory, and timeline data should be weighted relative to each other. This conversation happens outside Power BI, in a working document.

**In Layer 2**, Copilot translates that framework into the actual dashboard. It drafts the DAX measures behind the deal success gauge. It builds the sentiment timeline overlay. It summarizes shifts in plain language so executives can read the state of the deal in 30 seconds.

Neither tool could have produced the result alone. ChatGPT didn’t touch Power BI. Copilot didn’t decide what mattered. Together, they compressed a process that used to take weeks of analyst time into days.

## The Bigger Point

The best dashboards aren’t collections of charts. They’re decision tools.

That’s where the two-layer workflow earns its place. ChatGPT helps think through the decision. Copilot helps speed up the build. Power BI brings it together in something people can actually use.

The goal isn’t prettier visuals.

The goal is better decisions made earlier, with sharper questions, before the situation makes the choice for you.

*Chapter 6 of* [*Smart Dashboards with Power BI, ChatGPT, and Copilot*](https://www.amazon.com/Smart-Dashboards-Power-ChatGPT-Copilot/dp/B0GSH3BBLK) *walks through the full two-layer workflow with examples from M&A, chip manufacturing, and agriculture. The book is available now on Amazon.*