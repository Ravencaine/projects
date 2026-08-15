---
title: "How To Build A Power BI Report With AI Using The Power BI MCP"
source: "https://www.f9finance.com/power-bi-mcp/"
author:
  - "[[Mike Dion]]"
published: 2026-07-22
created: 2026-08-10
description: "I handed Claude a raw file and Microsoft's new Power BI MCP and asked it to build a full report. Here's exactly how it works."
Processed: "Unprocessed"
---
Building a Power BI report has always had a dirty secret. The charts are the fun part, and they’re maybe 20% of the work. The other 80% is setup. Wiring up the data model, writing the same measures you write on every project, then nudging visuals around until the deck looks right. Usually the night before it’s due.

So I ran a test. I handed the whole job to Claude Code and [Microsoft’s brand-new Power BI MCP](https://learn.microsoft.com/en-us/power-bi/developer/mcp/), gave it a raw file, and asked one question: can an AI do the whole job now, or just the easy parts?

I gave it a full day. Here’s what happened, and how you can run the same thing yourself.

<iframe title="Power BI's New AI MCP Is Terrifyingly Good" width="720" height="405" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen="" data-src="about:blank" src="about:blank"></iframe>

## Two Huge Power BI Builds From Microsoft

There are three separate pieces here, all in Public Preview, and people are already conflating them. Keep them straight and the whole thing makes sense.

**The Power BI MCP server.** MCP stands for Model Context Protocol. In plain terms, it’s a way for an AI tool to talk to and work directly inside your software. This one lets an AI read and edit your Power BI semantic model: the tables, the columns, the relationships, the measures.

![](https://www.f9finance.com/wp-content/uploads/2026/07/image-10.webp)

**The Power BI report authoring skills.** AI skills are just markdown files that teach an AI how to do something it wasn’t naturally trained on. In this case, that’s [building and managing Power BI](https://www.f9finance.com/power-bi/) reports the way an actual developer would. There are several of them packaged together (a planner, a designer, an author), and the AI grabs the right one when it needs it.

**The Desktop Bridge.** Also in preview. It lets your AI tool work directly with Power BI Desktop, including reloading the file and taking screenshots of a rendered page so the AI can check its own work.

Put simply: the skills tell the AI *what* to do, and the MCP and Bridge let it actually *do* it inside Power BI.

> One thing worth saying up front: Microsoft’s documentation is [written around GitHub Copilot](https://www.f9finance.com/copilot-studio-agent/), because that’s Microsoft’s product. You can run the [exact same setup with Claude Code](https://www.f9finance.com/claude-code/) or with Codex from OpenAI. I used Claude Code.

## What you need before you start

Here’s the gather list before you touch anything:

- **Power BI Desktop**: the free Microsoft app where your report lives.
- **An AI coding tool**: Claude Code, Codex, or GitHub Copilot. I used Claude Code.
- **The Power BI MCP + authoring skills**: the preview tooling above. You do not have to install these by hand. You can ask your AI tool to do the whole setup for you, download, install, configure, and test. I keep the exact setup prompts in my AI Library so Claude Code wires it up in one shot.
- **Your data**: whatever you’d normally build a report from. I used the F9 Finance coffee shop set: a P&L, manager commentary, and a point-of-sale file with 4.5 million rows.

That last file matters. A single Excel worksheet caps out at about 1 million rows, so 4.5 million won’t even open. That was on purpose. I wanted to see the AI handle a file the spreadsheet most of us live in physically cannot load.

## The one setting people miss: save as.pbip

This is the step that trips everyone, so do it first.

You cannot use a normal Power BI file (.pbix) for this. You have to save your report as a **Power BI Project file (.pbip)**. When you save as a project, Power BI exposes two folders on disk, one for the report and one for the semantic model. Those folders are what the AI reads from and writes to. Without them, the tools have nothing to grab.

So before anything else: File, Save As, and choose the.pbip project format.

![](https://www.f9finance.com/wp-content/uploads/2026/07/image-11.webp)

## Step by step: how the build actually went

I ran this in three passes, the way a developer’s day actually breaks down.

### 1\. Point it at the data and let it build the model

With the blank project open and saved as.pbip, my first prompt was deliberately simple.

```
Prompt: "Connect to the open Power BI project. Use our data and build a clean, well-structured semantic model."
```

Claude found the project, found the datasets I’d pointed it to (the commentary, the P&L, and the massive POS file), ran a quick check to make sure everything was wired up, and went to work.

![](https://www.f9finance.com/wp-content/uploads/2026/07/image-12.webp)

A few minutes later it came back with a finished model. Fact tables and dimension tables, all wired together. A date table. And here’s the part I didn’t ask for: it built a couple of mapping tables on its own, and it cleaned up the messy data without being told. It even started adding measures I hadn’t requested, units per transaction, line items, transactions, units sold.

That was the first moment I sat up. Not because it was fast, but because it was careful. It caught things I would have had to fix by hand at 6pm.

**The takeaway:** the model is the boring, repetitive, first-morning-of-every-project work. It’s also the part the AI did best.

### 2\. Make it plan the report before it builds

Here’s the part I genuinely didn’t think an AI could do. A report is the right four or five views for the person reading it, and picking those takes judgment.

So I didn’t tell it what to build. I made the prompt vague on purpose, because I wanted it to do the thinking.

```
Prompt: "Add four pages to the report. Plan them out first for my approval and ask me any questions as needed. The report is for the senior leadership team of the coffee shop."
```

I told it to come back for approval before building, because I didn’t want to burn tokens generating pages I’d throw away. About five minutes later it came back with a plan: an executive summary, a P&L page, location performance, and sales and product mix. It even asked me a couple of clarifying questions, like whether the default should be the latest month and whether I wanted manager commentary surfaced. (Yes to both.)

![](https://www.f9finance.com/wp-content/uploads/2026/07/image-13.webp)

That’s not a field dump. That’s how an analyst scopes a report.

### 3\. Build the pages, then make it look like mine

Once I approved the plan, it grabbed the report authoring skill from Microsoft and started building. A few minutes later I had four full pages: an executive summary with KPIs across the top and text commentary pulled straight from my files, a financial performance page, location performance, and sales and product mix. I could flip between periods and drill down into individual locations, Astoria, Hell’s Kitchen, Lower Manhattan. A fully functional report, and I hadn’t touched Power BI once.

![](https://www.f9finance.com/wp-content/uploads/2026/07/image-13.webp)

Then the last mile. The report worked, but it didn’t look like my brand yet. So I pointed it at my own F9 brand design skill, the one that holds my colors, fonts, and formatting rules.

```
Prompt: "Use the F9 brand design skill and apply the formatting to the report."
```

Same visuals, same layout, same data. But now it was F9 green with purple accents, a charcoal background, white text, and my branded font, applied cleanly across every page. Then it did the thing I’ve wanted for two years: it reloaded the file, took screenshots of its own report, and checked its own work.

## A quick real-world case

**The situation:** A controller I worked with rebuilt the same regional P&L report by hand every single month. About half a day gone every close, because the data never came in clean.

**What changed:** We used [this kind of process to automate](https://www.f9finance.com/robotic-process-automation-finance/) the model and the refresh one time.

**The result:** That half day turned into about 20 minutes a month. Same shape as what Claude just did in one sitting.

That’s the real point. The AI isn’t replacing the judgment. It’s making the boring, repeatable 80% cheap.

## Claude Code vs the Microsoft path

|  | Microsoft’s documented path | What I ran |
| --- | --- | --- |
| AI tool | GitHub Copilot | Claude Code (also works with Codex) |
| Setup | Manual, per the docs | Asked the tool to install and configure it |
| Report format | .pbip project | .pbip project |
| Where it runs | Local | Local |

The tooling is the same underneath. The only real difference is that the official instructions assume you’re a Copilot user, and almost nobody has written down the path for everything else.

## Where it still falls down

I’m not going to pretend this is finished. It’s a preview, and it shows.

**It still makes mistakes.** Most of the build was clean, but this is not a set-it-and-forget-it tool yet. You’re still the reviewer, and you should check the numbers before anything goes to a CFO.

**Formatting-heavy asks can miss.** Broad instructions (build the model, plan the pages, apply my brand) worked well. Very specific visual tweaks are hit or miss.

**It’s Windows-only and preview-only.** The Desktop Bridge runs locally on Windows, and every piece here carries a preview or beta label. Expect versions to move.

**Cost and access:** the Power BI tooling itself is preview, and this workflow runs locally with your existing AI tool, so there’s no separate cloud bill to publish. If you later push to a Fabric workspace, that’s its own setup and its own cost.

## So, can AI build a Power BI report?

A report that normally costs the better part of a day, model, measures, layout, and theme, came together in an afternoon of me mostly drinking coffee.

The honest answer: it can do the whole job, but it can’t do it unsupervised. You still bring the judgment about what belongs in front of leadership and whether the numbers are right. What you hand off is the grind.

And that trade, keep the judgment, give away the grind, is the best deal finance has been offered in a long time.

If you want the setup prompts and the skills I used here, they’re in my AI Library, along with my free weekly Finance AI Insider newsletter. And if you’d rather build these workflows than watch me build them, that’s exactly what I teach inside Finance AI Lab.