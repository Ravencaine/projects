---
title: "Why I Stopped Writing “Best Practice” DAX Posts (And What I Write Instead)"
source: "https://medium.com/towards-artificial-intelligence/why-i-stopped-writing-best-practice-dax-posts-and-what-i-write-instead-f32e9e8fd77d"
author:
  - "[[Gulab Chand Tejwani]]"
published: 2026-06-09
created: 2026-07-27
description: "A confession from someone who’s been doing this for 20 years: the most useful thing I ever did for my consulting practice was stop pretending that DAX patterns exist in a vacuum."
Processed: "Unprocessed"
---
## A confession from someone who’s been doing this for 20 years: the most useful thing I ever did for my consulting practice was stop pretending that DAX patterns exist in a vacuum.

![](99.System/Attachments/1!Y3ZohWGi-CR_t9WqVQdOwA.png.webp)

Why I Stopped Writing — Best Practice

It was late on a Thursday when my phone buzzed.

The message was from Rajesh, the head of analytics at a manufacturing company in Nagpur I’d been advising for six months. They were implementing a new Power BI rollout — 340 users, 47 factories, a data model I’d helped them architect from scratch.

His message: *“Gulab bhai, we followed the ‘best practice’ from that blog post. Now every report is timing out. What do we do?”*

The blog post he was referring to? A well-known Medium article with the headline “10 DAX Best Practices That Will Transform Your Power BI Reports.” It had significant engagement — the kind of viral post that gets widely shared. The author was clearly knowledgeable. The advice seemed sound.

And it nearly broke a production implementation.

Let me tell you what happened. And then let me explain why I haven’t written a “10 DAX Tips” post in three years — and what I write instead.

## The “Best Practice” That Wasn’t

(Names and identifying details are generalized to protect client confidentiality. The technical scenario is real.)

Rajesh’s team had implemented a recommendation from that blog post: use ALLSELECTED extensively to create “flexible” measures that respond dynamically to user filters. The specific pattern looked something like this:

```c
Flexible Revenue = 
CALCULATE(
    SUMX(
        FactSales,
        FactSales[Quantity] * FactSales[UnitPrice]
    ),
    ALLSELECTED(DimProduct[ProductCategory]),
    ALLSELECTED(DimDate[Year]),
    ALLSELECTED(DimCustomer[Region])
)
```

The blog post described this as “best practice” for creating reports where the user controls the context with slicers, but the measure calculations remain “stable.” It was presented as an elegant, production-ready pattern.

What the blog post didn’t mention: ALLSELECTED with multiple dimensions creates a cross-join context that grows exponentially with the number of selected values. In Rajesh’s model, with 12 product categories, 8 years of dates, and 23 regions — that’s potentially 12 x 8 x 23 = 2,208 context combinations, each triggering a full table scan.

Their report was timing out because every visual was effectively running 2,000+ DAX queries simultaneously.

The fix — which I implemented at 1 AM that Thursday night over a screenshare with Rajesh’s team — was to remove ALLSELECTED from two of the three contexts, replacing them with VALUES() for the dimensions that genuinely needed user flexibility and keeping ALLSELECTED only where the cardinality was controlled.

The timing dropped from 47 seconds to 1.2 seconds.

The blog post hadn’t lied. It had presented a pattern without its context. And in data modeling, context is everything.

![](99.System/Attachments/1!eKxCvceuspxH1l6_saUBPw.png.webp)

The Pattern

## What “Best Practice” DAX Content Actually Looks Like

Let me be specific about what I’m describing, because I don’t want to be unfair.

The “best practice” DAX content I’m talking about typically follows a consistent formula:

The “10 Tips” Format:

1. “Use CALCULATE for all your filters”
2. “Avoid FILTER inside CALCULATE — use filter arguments instead”
3. “Use SUMX instead of SUM for row-by-row calculations”
4. “Use variables (VAR) to make your code readable”
5. “Avoid row context in measure definitions”
6. “Use ALL() to remove filters when needed”
7. “Use time intelligence functions for date calculations”
8. “Use DIVIDE instead of the / operator to handle blanks”
9. “Use REMOVEFILTERS instead of ALL when you don’t mean ALL”
10. “Test your measures with different filter contexts”

These aren’t wrong. Most of them are genuinely good advice, presented by authors who understand DAX.

The problem isn’t that the advice is bad. The problem is that the advice is contextless.

“TIP 2: Avoid FILTER inside CALCULATE” is presented as a universal rule. But in reality:

- FILTER inside CALCULATE is slower when you’re filtering large tables
- FILTER inside CALCULATE is sometimes the ONLY way to achieve complex filter logic
- FILTER inside CALCULATE with specific cardinality patterns can be faster than filter arguments
- The performance difference only matters above certain data volumes

A reader in a 50,000-row dataset will never see the performance issue that makes Tip 2 relevant. A reader at 50 million rows will hit it immediately — and the tip alone won’t tell them why, or what to do instead.

The reader takes Tip 2 as gospel. They stop using FILTER entirely. Then they hit a scenario where FILTER is the correct tool, and they don’t know it.

This is how pattern-matching without context creates worse developers than no advice at all.

## Why Patterns Without Context Are Dangerous

Let me give you another example that I see constantly in consulting work.

The “best practice” advice around SUM vs SUMX typically goes like this:

“SUMX is slower than SUM because SUMX iterates row-by-row. Always use SUM when you can.”

This is… mostly true. SUMX is indeed an iterator. It does process row by row. In many scenarios, SUM is more efficient.

But here’s what the “best practice” doesn’t tell you:

SUM doesn’t work when you need row-by-row calculation. If you need `Quantity * UnitPrice` added together, you can't SUM(Quantity) and SUM(UnitPrice) — you need to multiply them first, then sum.

The “best practice” reader learns “SUMX is slow, avoid it.” They learn this as a rule. Then they encounter a pricing calculation and write:

```c
-- What they try (following the "best practice")
Incorrect Price = SUM(FactSales[Quantity]) * SUM(FactSales[UnitPrice])
```
```c
-- What they actually get: 
-- Total Quantity in context * Total Revenue in context
-- This is mathematically wrong. It's not "revenue" — it's nonsense.
```

They’ve followed the best practice. The measure runs. The number looks plausible. Nobody catches the error until the finance team asks why revenue is 300x higher than last quarter.

The correct approach:

```c
Correct Price = 
SUMX(
    FactSales,
    FactSales[Quantity] * FactSales[UnitPrice]
)
```

SUMX is the ONLY correct tool for this calculation. The “best practice” pushed the reader away from the only correct answer.

I’ve seen this exact error in six different client environments. Each time, the developer was following “best practice” advice from a popular blog post. Each time, the error sat undetected for months because the measure “ran fine” and the numbers “looked reasonable.”

![](99.System/Attachments/1!NHOqLj3n8TM83Cr48CvqXQ.png.webp)

What Context Looks Like

## The Cardinality Problem: Why Your Pattern Fails in My Model

Here’s the core issue that no “10 DAX Tips” post ever addresses:

**The same DAX pattern can succeed or fail entirely based on the cardinality of your data model.**

Let me walk through this concretely.

## Scenario A: Low Cardinality Model

You have:

- FactSales: 150,000 rows
- DimProduct: 250 products
- DimDate: 1,095 days (3 years)
- DimStore: 15 stores

A measure using ALL(DimProduct) to calculate “% of Total” works beautifully. The intermediate results are small. The calculation is fast. You write a blog post about this pattern. It works for your readers who have similar-sized models.

## Scenario B: High Cardinality Model

You have:

- FactSales: 85,000,000 rows
- DimProduct: 45,000 SKUs (with variants)
- DimDate: 2,190 days (6 years)
- DimStore: 340 locations

That exact same measure now creates massive intermediate tables. ALL(DimProduct) on 45,000 products inside a visual with 340 stores and 6 years of dates generates 45,000 x 340 x 6 = 91.8 million context combinations.

The measure either times out or returns wrong results due to memory pressure.

**The pattern is identical. The outcome is opposite. The only difference is cardinality.**

Now think about who writes “best practice” DAX content:

- Technical architects with well-designed models
- Authors who work on demos and sample datasets
- Bloggers optimizing for readability, not production scale
- Writers whose patterns worked in their environment

And who READS “best practice” DAX content:

- Developers building production models with real data volumes
- Consultants working across client environments of all sizes
- Analysts who inherited messy models and need solutions NOW
- People whose cardinality profile looks nothing like the demo environment

The “best practice” gap isn’t about who writes the content being wrong. It’s about **the entire format being wrong for the audience’s needs.**

When I was starting out, I followed every “best practice” I read. I implemented ALLSELECTED everywhere. I avoided SUMX. I used FILTER arguments exclusively.

Then I took my first real consulting engagement — a 12-million-row dataset at a logistics company in Bangalore — and watched my “best practice” measures crash a production server.

That was the day I started questioning everything I’d learned from blog posts.

## What I Write Instead

After that Bangalore incident, I made a deliberate shift. I stopped writing pattern-focused content. I started writing context-first content.

Here’s what that looks like in practice:

## Instead of: “10 Tips for CALCULATE”

I write: “When CALCULATE’s Filter Argument Beats FILTER (And When It Doesn’t)”

This post explores:

- Why filter arguments are generally faster (context compression)
- The specific scenarios where FILTER inside CALCULATE is faster (complex conditions, correlated subqueries)
- How cardinality of the filtered table determines which approach wins
- A decision framework for choosing at design time, not debugging time

The reader leaves understanding not just what to do, but WHEN to do it and WHEN NOT TO.

## Instead of: “SUM vs SUMX: The Ultimate Guide”

I write: “The Pricing Calculation Mistake That Costs Companies ₹50 Lakh Per Year”

This post explores:

- Why SUMX is non-negotiable for row-by-row multiplication
- The specific business impact of getting pricing calculations wrong
- How to identify when you’re accidentally using the wrong aggregation
- A validation framework to catch these errors before they hit production

The reader leaves knowing how to catch their own errors, not just what the correct pattern is.

## Instead of: “Master ALL() and REMOVEFILTERS()”

I write: “The ALLSELECTED Trap That Breaks Production Reports”

This post explores:

- What ALLSELECTED actually does (it’s not what most people think)
- Why multiple ALLSELECTED contexts create exponential complexity
- How to identify when your model has crossed the cardinality threshold
- A debugging methodology for “why is my report slow” that doesn’t just say “use less ALLSELECTED”

The reader leaves with a debugging skill, not just a syntax rule.

![](99.System/Attachments/1!ibPmlHa2z2458TGKeFJQWQ.png.webp)

The Shift

## The Results: How This Shift Changed My Blog

I’ll be honest about what happened when I changed my approach.

**The “best practice” posts performed well by standard metrics.** Views were consistent. Claps were steady. The comments were polite: “Great tips!” “Very informative!” “Saved for later!”

**The context-first posts performed differently.**

Views were more volatile — lower floor, higher ceiling. Some posts underperformed. Others went unexpectedly viral. Comments were longer, more specific, more engaged. Readers shared their own scenarios. Practitioners asked follow-up questions that led to deeper content.

The posts that performed best were the ones where I said things like:

- “This pattern will cost you 2 seconds per visual. In small models, that’s nothing. In large models, that’s your refresh budget gone.”
- “This advice only applies if your fact table exceeds 10 million rows. Below that, it doesn’t matter.”
- “The documentation says X. In practice, I’ve seen it fail when Y.”

The “best practice” posts got 400–600 views per week. The context-first posts got 150–800 views per week — with occasional posts hitting 3,000+ views when they hit a nerve.

But here’s what mattered more: **the quality of inbound inquiries changed.**

After “best practice” posts, I got: “Can you help us implement CALCULATE?” (generic, low-value)

After context-first posts, I got: “We have a 45-million-row fact table with 340 store locations and we’re hitting timeout issues with ALLSELECTED — can you consult?” (specific, high-value)

I started attracting the clients I actually wanted to work with: practitioners with real problems, specific constraints, and the context to understand my recommendations.

The shift cost me reach. It gained me relevance.

For my consulting practice, that was the right trade.

## The Honest Argument: 95% of Power BI Medium Content Is Pattern-Matching Without Context

Let me say this clearly: I’m not criticizing the authors.

Most Power BI content on Medium is written by people who genuinely know DAX. They understand the patterns. They write clearly. Their advice is technically correct in the contexts they describe.

The format itself is the problem.

A 10-tips post cannot capture context. Tips are, by design, context-stripped. They’re meant to be memorable, repeatable, applicable. That compression is a feature for teaching — and a bug for applying.

Here’s what I estimate the split looks like across Power BI Medium content:

![](99.System/Attachments/1!f32fpU9xb-Gn8tjWrb-OeA.png.webp)

The 95% figure in my title is an estimate, but I don’t think it’s wrong.

The vast majority of Power BI content is written by people sharing patterns that worked for them. The context — their specific data model, their cardinality, their organizational constraints — stays internal. Readers get the pattern without the context.

This isn’t malicious. It’s just how blog writing works. You share what you know. You can’t share every condition under which your advice applies.

But it creates a systematic bias in the ecosystem. Developers learn patterns. They apply them. They hit edge cases the patterns didn’t prepare them for. They blame themselves for not following the “best practice” correctly.

The pattern wasn’t wrong. The context was missing.

![](99.System/Attachments/1!QH3TmtwOpMVAO-vrb6HLmQ.png.webp)

What I Write Now

## Why This Differentiates My Content Permanently

Here’s my honest assessment of my own work:

**My “best practice” posts from 3–4 years ago are just like everyone else’s.** They’re technically correct. They’re well-written. They’re context-stripped. They follow the formula. They perform OK.

My current content is different because I made a deliberate choice to stop optimizing for views and start optimizing for relevance.

The trade is real:

- I write fewer posts (context-rich content takes longer to produce)
- My posts have lower consistency in performance (more volatile, more niche)
- My total viewership is lower than if I’d stuck with the formula

But:

- My inbound inquiries are higher-quality
- My reader relationships are deeper
- My content actually solves problems instead of teaching patterns
- My content differentiates me from the “10 Tips” authors I was competing with

This is brand-building, not traffic-chasing.

When a reader lands on my post and sees “This pattern will fail in your production model, and here’s exactly why and when” — they know they’re reading something different. They know I’m not selling them a framework. I’m sharing what I’ve learned from watching frameworks fail.

That reader becomes a subscriber. That subscriber becomes a client. Or they recommend me to someone who becomes a client.

The formulaic content gives you views. The context-rich content gives you authority.

I chose authority.

## The Practitioner Verdict

Let me give you a framework for evaluating DAX content — including mine — through a practitioner’s lens:

![](99.System/Attachments/1!zHNGP8w1M5RBo9jNbrQjQw.png.webp)

The best DAX content — the 5% worth reading — answers these questions explicitly. It says: “This works when X. It breaks when Y. Here’s how to tell the difference.”

The formulaic content says: “Use this pattern. It’s best practice.”

The practitioner distinction is whether you can leave the article knowing whether it applies to your situation.

![](99.System/Attachments/1!p4cmev5Z_r8CksXuIGbUSg.png.webp)

The Practitioner Verdict

## What This Means For You

If you’re a Power BI practitioner reading this:

Be suspicious of content that gives you rules without conditions.

“Never use FILTER inside CALCULATE” isn’t advice. It’s a heuristic that will fail you in specific scenarios.

“Use FILTER inside CALCULATE when your filter condition is complex or involves correlated references” is advice. It comes with a condition. It tells you when to apply it.

The condition is the value. The rule is the bait.

Build your own decision framework. Don’t memorize patterns. Understand why the pattern works. Then you can adapt it when context changes — which it always does.

Test in your environment. A pattern that works in a 150,000-row demo might fail in your 15-million-row production model. The only way to know is to test, not to assume the pattern transfers.

Find authors who write about failures. The bloggers worth following aren’t the ones who show you perfect implementations. They’re the ones who show you what broke, why it broke, and how they fixed it. That’s the content that transfers to your environment.

Question everything you’ve bookmarked as “best practice.” Go back through your saved articles. Ask yourself: “Does this tell me when NOT to use this pattern?” If the answer is no, the article is incomplete — and potentially dangerous.

## A Note on Why I Made This Shift

I want to be transparent about my motivations, because authenticity matters in brand positioning.

I started writing Power BI content in 2019. Like everyone else, I wrote “10 Tips” posts. They performed well. The formula was clear: find a common DAX pattern, explain it simply, give 10 variations or tips, end with a call to action.

My first few posts in that format did fine. 400–600 views per week. Modest subscriber growth. Occasional consulting inquiries of the generic variety: “Can you help us with Power BI?”

Then something changed.

I started taking on more complex consulting work — production environments, large-scale implementations, enterprise clients with data teams that had already tried the “best practice” approach and hit walls.

I started seeing the same patterns fail, again and again.

ALLSELECTED breaking reports. SUM instead of SUMX producing wrong numbers. FILTER inside CALCULATE being demonized when it was the correct tool. REMOVEFILTERS vs ALL being presented as interchangeable when they’re fundamentally different.

Every failure traced back to someone following contextless advice from the same ecosystem of “10 Tips” content.

That’s when I realized: the content that teaches patterns is not the content that helps practitioners.

The content that helps practitioners shows them how to evaluate whether a pattern applies to their situation.

The first type gets views. The second type builds authority.

For a consulting practice, authority is worth more than views.

## What I’ll Keep Writing

I stopped writing “best practice” posts because they weren’t helping people. They were helping people pass the interview question about best practices without helping them solve the production problem that comes after.

What I’ll keep writing:

- Real scenarios with specific cardinality constraints
- Honest acknowledgment of when my advice applies and when it doesn’t
- DAX that works in production environments, not just demos
- Stories about what failed (mine and my clients’) and what we learned
- Debugging methodology that transfers across model sizes
- Honest assessment of tradeoffs, including the tradeoff between simplicity and correctness

What I won’t write:

- “10 Tips for Better DAX”
- “The One Pattern Every Power BI Developer Must Know”
- “Master CALCULATE in 5 Minutes”
- “The Ultimate Guide to \[Any DAX Function\]”
- Any post that promises simplicity in a complex domain

DAX is not simple. Power BI at production scale is not simple. Data modeling in enterprise environments is not simple.

The content that helps practitioners isn’t the content that makes DAX sound simple. It’s the content that makes the complexity manageable.

The content that helps practitioners says: “Here’s why this is hard. Here’s how to think about it. Here’s how to know when you’re doing it right.”

That’s what I’m here for.

## The Invitation

If you’re a Power BI practitioner who’s been burning through “10 Tips” posts without solving your actual problems, I want to offer something different.

My content won’t always be easy to read. Context-rich explanations are longer than rules. Understanding the “when” is more complex than memorizing the “what.”

But when you encounter a production issue at 11 PM — and you will, if you work in this space long enough — the content that will help you isn’t the post that gave you 10 rules.

It’s the post that taught you how to think.

That’s what I’m building here.

Not a library of patterns. A library of reasoning.

*Have you seen “best practice” advice fail in your production environment? I’d love to hear the story — drop it in the comments.*

*If you found this useful, follow me for more practitioner-first Power BI content. Previous posts cover the $180K Power BI error, Copilot’s 4/10 DAX score, the data model mistake costing $100K+, and more real-world analytics lessons from 20 years of consulting.*