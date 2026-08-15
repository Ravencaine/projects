---
title: "Enhancing Power BI Reports with AI: A Focus on Accessibility"
source: "https://smart-frames.co.uk/2026/07/01/before-ai-builds-your-power-bi-report-tell-it-this/?utm_source=powerbiweekly&utm_medium=email&utm_campaign=newsletter"
author:
  - "[[Juls]]"
published: 2026-07-01
created: 2026-08-08
description: "Discover how AI transforms Power BI reporting with improved accessibility and design principles for enhanced user experiences."
Processed: "Unprocessed"
---
AI is rapidly changing the way we build Power BI reports. What began with asking ChatGPT or Copilot to write a DAX measure or explain an error has evolved into something far more powerful. Today, AI can suggest report layouts, recommend visuals, generate measures, and even build an entire dashboard from a simple prompt. With Microsoft’s latest developments in Fabric Apps, this is being pushed even further, allowing users to describe an analytical application in natural language and have much of the experience generated automatically.

The more capable these tools become, the clearer it is that strong results come from how well we describe what we want, not how fast you can assemble a report.

I’ve experienced this first-hand while vibe coding PBIX A11y and the other platforms I’ve built in Lovable. It has shown me something important: prompting isn’t just a convenience layer anymore. It behaves much more like a design specification, the place where structure, behaviour and intent are defined before anything is built.

## Vibe Coding Taught me Something About Prompting

From the outset, I set one clear requirement: every page must meet WCAG 2.2 Level AA.

I made this explicit in my prompts every time I asked the AI to build a new page or feature. Accessibility was not a side note; it was a core constraint. And yet, despite repeating it, accessibility issues still surfaced.

Buttons would occasionally fail colour contrast checks. Text would drift into shades too light against their backgrounds. Interactive elements were sometimes too small to be comfortably usable. Focus indicators disappeared after redesigns. At times, the AI even removed an accessibility fix it had correctly implemented only a few prompts earlier.

This wasn’t the model ignoring instructions. It was doing what large language models do: optimising for the current request while balancing everything else in the conversation. Not to mention I wasn’t giving it enough to work with. WCAG covers a huge range of criteria, and my prompt simply wasn’t specific enough.

## AI Doesn’t Remember Everything Forever

One of the easiest assumptions to make is that AI retains all instructions consistently throughout a project. In reality, it doesn’t.

Every model operates within a context window, which is the limited amount of conversation it can actively reference when generating a response. As a project grows, earlier instructions gradually lose influence. New prompts take priority, older requirements become less prominent, and details that once felt established can quietly fade.

I saw this repeatedly while building websites through vibe coding. After dozens of iterations refining layouts, adding features and fixing bugs, accessibility constraints would slowly erode. A button that previously met contrast requirements might reappear in a lighter shade. A component that once had proper keyboard focus could be rebuilt without it. Nothing dramatic changes in isolation, but small regressions accumulate over time.

That’s when it becomes clear that accessibility cannot be a one-time instruction at the start of a project. It has to be reinforced continuously.

The same principle applies directly to Power BI development with AI assistance.

If you ask AI to build a sales dashboard, you will likely get something that looks polished. KPI cards, trend charts, slicers and tables are arranged in a way that feels logical and production-ready. On the surface, it appears complete.

What it often lacks is the detail that makes it genuinely accessible: meaningful alt text, sufficient colour contrast, logical tab order, appropriately sized interactive elements, or a deliberate preference for native visuals over custom ones where appropriate.

Not because AI cannot do these things, but because they were never explicitly carried through every step of the build.

As AI becomes more embedded in report creation, the prompt effectively becomes the design specification. If accessibility is not continuously reinforced within that specification, it will not consistently carry through the output.

## What to Consider When Prompting for AI Built Dashboards

A good way to start is by establishing the core accessibility criteria for the project. And if you’re not sure where to begin, that’s absolutely fine. I’ve taken the PBIX A11y accessibility audit and reverse engineered it into something more useful at the start of the process: prompting.

In practice, this means accessibility stops being a validation step and becomes part of how the dashboard is described to the AI from the beginning. The result is a more accessible default output, rather than something that needs significant correction later.

These are the core areas I always include when prompting an AI to generate or modify a dashboard:

- Colour contrast (including WCAG-based thresholds against the chosen background)
- Meaningful and dynamic alt text for visuals and slicers
- Visual density and information hierarchy to ensure clarity and scannability
- Clear page, visual and axis titles so structure and intent are explicit
- Readable font sizes that scale appropriately with the canvas
- Logical tab order for predictable keyboard navigation
- Appropriately sized interactive elements for usability
- Preference for native Power BI visuals unless a custom visual is genuinely required

These criteria are the same foundation used in PBIX A11y as accessibility audit checks for Power BI reports. The key shift is that they are no longer only applied after a dashboard is built. Instead, they are reverse engineered into the prompt so they shape the output from the start.

For this reason, I’ve also created a free tool within PBIX A11y called the ***[Accessibility Prompt Builder](https://pbiaudits.com/accessibility-prompt-builder)*.** It helps translate these principles into a structured set of inputs that generates a ready-to-use accessibility prompt for when you are working on AI-built dashboards.

It focuses on the same core considerations: canvas size, layout structure, information hierarchy, colour contrast based on WCAG calculations, font sizing, tab order, interactive element sizing, and whether custom visuals are being used.

This ensures accessibility is not something added after the fact, but something embedded directly into the instructions that generate the report in the first place.

## Prompting Isn’t Proof (and Why It Still Needs Auditing)

However strong a prompt is, it is never the end of the process.

AI can significantly improve the starting point of a Power BI report, but it does not guarantee a fully accessible output. Results can vary between runs, and accessibility can still degrade as a report evolves through multiple rounds of edits, refinements and feature additions.

This is why prompting and auditing need to work together rather than be treated as alternatives. Prompting reduces the number of issues introduced at the point of creation by embedding accessibility into the instructions from the start. Auditing then ensures the final report actually meets the standard it was designed to achieve.

This distinction matters because accessibility is not a static output condition. It is something that can drift over time, especially in AI-assisted workflows where changes are incremental and continuous rather than rebuilt from scratch.

In practice, that means the prompt becomes the design specification, and the audit becomes the verification layer. One shapes intent, the other confirms execution.

## Wrap-Up

One of the most important lessons from vibe coding is that accessibility is not a single instruction. It is a continuous requirement that must be reinforced throughout the lifecycle of a project.

The same is increasingly true in Power BI development. As AI takes on a larger role in building reports, prompting is no longer just about describing the data or the visuals you want. It is part of designing the experience itself.

This is why I’ve taken the PBIX A11y accessibility audit and reverse engineered it into something more useful at the start of the process: prompting, supported by a dedicated [Accessibility Prompt Builder](https://pbiaudits.com/accessibility-prompt-builder). It ensures that the same principles used to audit a finished report are also used to shape it before it exists.

So the next time you ask AI to build a report, don’t just describe the metrics or visuals. Describe how you expect people to experience it. Then treat the output as a first draft shaped by intent, not a finished product.

Thank you for joining me on this journey. Until next time, let’s keep crafting accessible and ethical insights that make a difference!