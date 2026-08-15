---
title: "Power BI Design Skills: Why Accessibility Still Starts with the Prompt"
source: "https://community.fabric.microsoft.com/t5/Power-BI-Community-Blog/Power-BI-Design-Skills-Why-Accessibility-Still-Starts-with-the/ba-p/5299070?utm_source=powerbiweekly&utm_medium=email&utm_campaign=newsletter"
author:
published: 2026-07-17
created: 2026-08-08
description: "The way we create Power BI reports is changing. Microsoft's new Power BI Report Design skill, distributed through the Skills for Fabric marketplace"
Processed: "Unprocessed"
---
The way we create Power BI reports is changing.

Microsoft's new Power BI Report Design skill, distributed through the Skills for Fabric marketplace as part of the Power BI authoring plugin, is currently in preview. It's built for AI coding agents such as GitHub Copilot CLI, VS Code Copilot, Claude Code and Cursor, working directly with PBIP project files. The skill supplies opinionated design guidance for Power BI reports, covering page archetypes, chart selection, colour, typography, layout, accessibility considerations, anti-pattern detection and an opinionated theme preset. It then hands that design brief to a separate authoring skill, which handles the actual report file mechanics.

This is a different way of working to typing a request into Copilot chat inside Power BI Desktop. It sits in the agentic, developer-tooling layer for now, aimed at report authors comfortable installing a plugin and working with project files rather than the everyday report-building experience most of us are used to. But the direction of travel is clear, and it's worth understanding now: instead of manually making every design decision, we describe our intent and let the skill translate that into a structured report brief.

Microsoft's own documentation notes the skill works best when the user's intent is design-shaped rather than file-shaped, with example prompts like "Build a sales report for the executive team" or "Design an ops monitoring page for the on-call rotation." That's a useful confirmation: the natural-language, intent-first way of prompting this article talks about isn't a stretch. It's how the skill is designed to be used. If you want to read more about, it is worth checking the Microsoft Learn page [What is the Power BI Report Design skill?](https://learn.microsoft.com/en-us/power-bi/developer/agentic/power-bi-report-design-skill-overview)

As these capabilities mature and make their way into more mainstream workflows, one thing becomes even more important: the quality of the output depends on the quality of the guidance we provide. Even with accessibility included as part of the Design skill, we still need to prompt for the accessibility and usability outcomes we want to achieve, because good design is not just about how a report looks. It is about how effectively people can understand and use it.

## Design Guidance Needs Human Context

The Report Design skill can support many aspects of effective report design. It can help identify appropriate page structures, recommend suitable visuals, apply consistent styling and detect common design issues. These capabilities can help report authors create more coherent and professional experiences.

Design decisions, though, are always connected to context. A report used by an executive making strategic decisions will have different requirements from a report used by an operational team monitoring daily activity, and the same is true of accessibility. The skill can apply accessibility guidance, but it doesn't know the specific needs of your audience, the environment the report will be used in, or the decisions your users need to make. That understanding has to come from the person writing the prompt, which is exactly why prompting is becoming such an important part of the design process.

## Accessibility Is More Than a Checklist

The inclusion of accessibility guidance within the Design skill is an important step forward, but accessibility isn't a single feature that can simply be enabled. It's a series of design decisions that shape the entire user experience. As report authors, we still need to consider and communicate requirements such as:

- sufficient colour contrast between text, visuals and backgrounds
- avoiding colour as the only way to communicate meaning
- readable typography and appropriate font sizing
- clear page and visual titles
- logical navigation
- layouts that reduce unnecessary cognitive effort

These aren't purely technical requirements. They shape how quickly and easily someone can understand information, and a report that follows accessibility principles is more likely to support users when they need to find information quickly, interpret data accurately and make decisions confidently.

## Accessibility Supports Real-World Use

When we talk about accessibility, it's easy to associate it only with supporting people with disabilities. That's a fundamental reason it matters, but it isn't the only one.

Reports get used in working environments, and those environments are rarely ideal. Someone might be reviewing a dashboard between meetings, trying to make a decision under pressure. They could be working in a busy office full of distractions, viewing a report on a laptop with poor screen brightness, or trying to interpret data at the end of a long day when mental fatigue is affecting concentration.

Accessibility helps people far beyond those with permanent disabilities. Throughout the working day, we all encounter situations that make information harder to process, whether we're under pressure, switching between meetings, dealing with distractions or viewing a report on a less-than-ideal screen. In these moments, accessible design becomes good design: strong colour contrast makes content easier to read, clear layouts reduce unnecessary cognitive effort, consistent navigation helps users find information quickly, and meaningful labels remove ambiguity. These choices improve the experience for everyone, regardless of their circumstances, which is exactly why accessibility shouldn't be treated as separate from design. It's part of creating a report that works in the real world, and that's what makes it worth carrying into how we prompt, whichever tool ends up doing the authoring.

## Prompt for the Experience, Not Just the Report

As AI becomes more involved in report creation, whether through an agent working on PBIP files today or a more mainstream Copilot experience tomorrow, prompting becomes part of the design skillset. A prompt that only describes the output gives the agent information about what to create. A prompt that describes the intended experience gives it the context needed to make better design decisions.

For example:

"Create an executive dashboard showing project performance."

This explains the purpose of the report. But adding:

"Create an accessible executive dashboard designed for quick decision-making. Prioritise readability, use accessible colour combinations, avoid relying on colour alone to communicate information, include meaningful titles and alternative text, minimise visual clutter and ensure information can be understood in different working environments."

gives the agent much more to work with. The difference isn't just the final appearance. It's the experience created for the people using the report.

But even a prompt like that isn't quite enough on its own. "Use accessible colour combinations" tells the agent your intent, not what to actually build. Without specific contrast ratios, exact hex values, minimum font sizes or target sizes, the agent is left to interpret "accessible" itself, and that's exactly the kind of judgement call that shouldn't be left to guesswork.

## Making Accessibility Easier to Include in Prompts

This is something I explored further in my previous article, [*Before AI Builds Your Power BI Report, Tell It This*](https://smart-frames.co.uk/2026/07/01/before-ai-builds-your-power-bi-report-tell-it-this/), where I looked at why accessibility needs to be included in AI prompts from the beginning rather than treated as a final review step. As these design capabilities move from developer preview towards everyday use, I believe this becomes even more important: the better we communicate accessibility requirements now, the better AI can support us in creating inclusive experiences later.

This is also why I built the [Accessibility Prompt Builder](https://pbiaudits.com/accessibility-prompt-builder) within PBIX A11y, a free tool that helps report authors add accessibility considerations directly into their prompts, with guidance covering colour contrast, typography, layout, visual clarity and usability. It isn't there to replace accessibility knowledge or design judgement. It's there to make it easier for more people to include accessibility at the point where design decisions begin.

Here's an example of what the tool generates, based on a report's canvas size and colour palette:

ACCESSIBILITY REQUIREMENTS FOR THIS POWER BI REPORT

(Accessibility only. This does not cover the report's metrics, data model or visual choices. Add those separately.)

Canvas: 1280×720px.

**1\. Colour contrast**: targeting WCAG 2.1 Level AA. Use at least 4.5:1 contrast for normal text (3:1 for large text 18pt and above), and at least 3:1 contrast for borders, icons, UI elements and data colours against their background. Use Verdana as the typeface throughout.

Background: #fcf7eb (light mode).

Colour 1 #4B2E7E vs background: 9.86:1, safe for normal text, large text, UI elements and chart colours.

Colour 2 #2e7f5c vs background: 4.56:1, safe for normal text, large text, UI elements and chart colours.

Colour 3 #8f8a99 vs background: 3.14:1, safe for large text (18pt+), UI elements and chart colours, not normal body text.

Colour 4 #168aa2 vs background: 3.78:1, safe for large text (18pt+), UI elements and chart colours, not normal body text.

Colour 5 #d31717 vs background: 5.03:1, safe for normal text, large text, UI elements and chart colours.

**2\. Alt text**: write alt text for every visual that explains both what it shows and the key takeaway, not just the chart type. This page has slicers (Reporting Month, Department), so make the alt text dynamic: build it from a measure so it updates automatically as the reader changes the Reporting Month, Department selection, rather than using a fixed description written for one state.

**3\. Layout**: keep visual coverage below roughly 75% of the canvas, with no overlapping visuals. Structure the page in three levels of importance: Level 1 is the page title and main KPIs at the top; Level 2 adds visuals that give depth to those KPIs; Level 3 holds more granular detail like timelines, trends or tables. If there isn't room for all three levels, move Level 3 to a drill-through or tooltip page.

**4\. Titles**: give every visual a clear, non-empty visible title, label both axes on every chart that has them, and add a text or card heading near the top of the page that names the page.

**5\. Font size**: use a minimum of 12pt for all text (scaled from a 12pt baseline at 1280×720 for this 1280×720 canvas). Apply to titles, data labels and axis labels.

**6\. Tab order**: set a unique, logical tab order for every visual, and exclude purely decorative shapes from the tab sequence.

**7\. Target size**: make all interactive elements (buttons, slicers, navigators, icon-only controls) at least 24px (scaled from the 24px WCAG minimum for this canvas). Aim for 40px or larger for icon-only controls without a visible text label (scaled from the 40px recommendation).

**8\. Colour-blindness**: avoid colour combinations that are hard to distinguish for the most common forms of colour-blindness (red/green, blue/yellow). Don't rely on colour alone to convey meaning, pair it with labels, icons, patterns or text. Once the report is built, screenshot the key charts and run them through a colour-blindness simulator to confirm.

Note: accessibility requirements only. Add your own brief for metrics, KPIs and visual choices.

That's the level of specificity that turns "make it accessible" from a vague instruction into something an AI agent, or a human designer, can actually act on: exact contrast ratios against your background colour, a defined visual hierarchy, a minimum touch target size, a reminder to make alt text dynamic rather than static. You paste it alongside your own brief for metrics, data model and visual choices, since the tool deliberately stays out of those decisions.

**Point 2** is worth calling out on its own. **Dynamic alt text, alt text built from a DAX measure** so it updates automatically as a reader changes a slicer, isn't something the Design skill generates for you. It's a data modelling task, not a layout or styling one, so it falls outside what any design-focused AI capability is built to do. That's exactly why it's easy to forget: it doesn't show up when you're thinking about colour, layout or typography, yet a static alt text description that's only accurate for one filter state can end up misleading a screen reader user the moment they change a selection. It has to be planned and built deliberately, and it's one of the accessibility requirements most likely to get missed if we only prompt for what a Design skill can influence.

## Good Prompting Is Becoming a Design Skill

The future of Power BI report creation isn't about replacing report authors or designers. It's about giving us new ways to express our design intent. Power BI's emerging Design skills provide a powerful foundation, including accessibility considerations, but they work best when combined with human understanding and clear instructions. We still need to explain who the report is for, what decisions it supports and what experience we want users to have.

Accessibility isn't something we add after a report has been designed. It's part of the design decision itself, and as AI becomes more capable, knowing how to prompt for inclusive experiences is becoming an essential design skill.

Try the [Accessibility Prompt Builder](https://pbiaudits.com/accessibility-prompt-builder) next time you brief an AI agent or Copilot on a report, and see how much difference a well-built prompt makes.

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