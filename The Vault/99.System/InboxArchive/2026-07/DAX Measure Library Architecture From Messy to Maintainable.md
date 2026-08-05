---
title: "DAX Measure Library Architecture: From Messy to Maintainable"
source: "https://medium.com/towards-artificial-intelligence/dax-measure-library-architecture-from-messy-to-maintainable-97e0aca852a9"
author:
  - "[[Gulab Chand Tejwani]]"
published: 2026-01-19
created: 2026-07-27
description: "How we stopped wasting $93,600 per year searching for measures we’d already built"
Processed: "Unprocessed"
---
## How we stopped wasting $93,600 per year searching for measures we’d already built

![](99.System/Attachments/1!2fMUOK-kTVRQXZW5g5Ypug.png.webp)

DAX Measure Library Architecture

The Slack message appeared at 2:37 PM on a Tuesday.

“Hey, do we have a measure for customer lifetime value? I can’t find it.”

I knew we had it. Somewhere. I’d built it myself three months ago for the sales dashboard.

I opened the model. Scrolled through the measures pane. 147 measures. No organization. No folders. Just an alphabetical wall of text.

`[Customer LTV]`? Nope. `[LTV]`? Not there. `[Lifetime Value]`? Missing.

After 20 minutes of searching, I found it: `[CLV_Total_Final_v2]`

My colleague’s response: “Why didn’t you just rebuild it? Would’ve been faster.”

He was right. And that’s when I realized something was fundamentally broken.

**We had spent months building a library of reusable calculations, and nobody could find anything in it.**

What’s the point of building measures if your team can’t use them? What’s the benefit of creating sophisticated DAX if it gets rebuilt from scratch in every new model because nobody knows it exists?

That Tuesday afternoon changed how I think about DAX libraries. Not as a collection of measures, but as an architecture. A system. Something you design, not something that just happens.

Today, I’m going to show you how to transform your chaotic measures table into a maintainable library that your entire team can actually use.

## The Hidden Cost of Messy Measures

Before we dive into the architecture, let me tell you what that messy measures table cost us.

**Time waste:** I calculated it once. Our team of 6 analysts spent an average of 4 hours per week searching for, recreating, or debugging measures that already existed somewhere in our models.

4 hours × 6 people × 52 weeks = **1,248 hours per year**

At an average cost of $75/hour (conservative for data analysts), that’s **$93,600 in wasted salary** just because we couldn’t find our own work.

**Inconsistency**: Even worse, we’d rebuild the same measure differently. Customer lifetime value calculated three different ways across three dashboards. All “correct,” but all different.

Finance used one formula. Sales used another. Marketing had their own version.

When the CFO asked “What’s our average customer lifetime value?” we had three answers. None of them matched.

**Knowledge loss:** When Sarah left the company, she took 4 years of domain knowledge with her. The measures she’d built? Still in the models. But nobody knew what they did, why they existed, or how to modify them.

We found measures like:

- `[Calc_Adjusted_Rev_Final]` (what's "adjusted"?)
- `[Test_Metric_2]` (is this still a test?)
- `[DO_NOT_USE_OLD]` (then why is it in the model?)

**That was our breaking point.**

Either we built a system for organizing DAX, or we’d keep drowning in our own technical debt.

![](99.System/Attachments/1!qVrdmqgKJNQktbPWz1ZPqQ.png.webp)

The Cost of Chaos

## The Architecture Framework: Four Layers of Organization

After studying how successful development teams organize code libraries, I adapted their patterns to DAX.

The framework has four layers:

**Layer 1: Folder Structure** (Visual organization) **Layer 2: Naming Conventions** (Findability) **Layer 3: Documentation Standards** (Understanding) **Layer 4: Governance Process** (Sustainability)

![](99.System/Attachments/1!Gyli44QJ_3iGliMS7K5RCQ.png.webp)

The 4-Layer Architecture Framework

Let me walk you through each layer with real examples from the library we built.

## Layer 1: Folder Structure (The Visual Organization)

**The Problem:**

Most analysts organize measures like this:

```c
📁 Measures
   - Customer LTV
   - Sales This Year
   - Profit Margin
   - Sales Last Year
   - Customer Count
   - Revenue per Customer
   - Sales vs Target
   ... 147 measures in one flat list
```

Good luck finding anything.

**The Solution:**

We implemented a hierarchical folder structure based on **business function** and **calculation type.**

Here’s what we built:

```c
📁 _Base Measures
   📁 Sales
      - _Sales Amount
      - _Sales Quantity
      - _Sales Cost
   📁 Customer
      - _Customer Count
      - _Active Customers
      - _New Customers
   📁 Product
      - _Product Count
      - _Product Categories
   📁 Date
      - _Current Date
      - _Fiscal Year Start
📁 Time Intelligence
   📁 Sales
      - Sales LY
      - Sales YTD
      - Sales MTD
      - Sales QTD
   📁 Customer
      - Customers LY
      - Customer Growth YoY
📁 Comparisons & Variance
   📁 Sales
      - Sales vs LY
      - Sales vs LY %
      - Sales vs Target
      - Sales vs Target %
📁 KPIs & Metrics
   📁 Customer
      - Customer Lifetime Value
      - Customer Acquisition Cost
      - Customer Retention Rate
   📁 Sales
      - Revenue per Customer
      - Average Order Value
      - Conversion Rate
📁 Utilities
   - Selected Period Text
   - Has Data
   - Row Count
📁 Formatting
   - Format Percentage
   - Format Currency
   - Format Variance
```

**Why This Works:**

1. **Prefixes show hierarchy**: `_Base Measures` comes first alphabetically
2. **Business function folders**: Sales, Customer, Product (matches how people think)
3. **Calculation type sub-organization**: Time intelligence vs. KPIs vs. Comparisons
4. **Clear progression**: Base → Time Intelligence → Comparisons → KPIs

**The Real-World Impact:**

“Do we have customer lifetime value?” → Opens “KPIs & Metrics” → “Customer” → There it is. **12 seconds instead of 20 minutes**.

New analyst joins the team. → Opens model. Sees clear folder structure. Understands organization immediately. **No confusion, no retraining**.

## The Folder Structure Rules We Follow

After two years of refining this, here are the rules that made it sustainable:

**Rule 1: Base measures ALWAYS start with underscore**

`_Sales Amount` not `Sales Amount`

Why? Base measures should be internal-use-only. The underscore signals “this is a building block, not a final metric.”

**Rule 2: Maximum 3 levels of folders**

```c
✅ Good:
📁 KPIs & Metrics → Customer → Customer LTV
```
```c
❌ Too deep:
📁 KPIs → Financial → Customer → Acquisition → Cost per Customer
```

If you need more than 3 levels, your categories are too granular.

**Rule 3: Folders match business language, not technical terms**

```c
✅ Good: Sales, Customer, Product
❌ Bad: Fact_Sales, Dim_Customer, Aggregations
```

Business users should understand the organization without a data dictionary.

**Rule 4: Utilities and Formatting get their own folders**

These are measures that support other measures but aren’t business metrics:

- `[Selected Period Text]` (displays filter context)
- `[Has Data]` (validation check)
- `[Format Currency]` (display formatting)

Don’t bury them in business folders. They’re infrastructure.

**Rule 5: Time Intelligence gets a dedicated folder**

Every LY, YTD, MTD, QTD measure goes here. Period.

Don’t scatter them across business folders. Time intelligence is a calculation TYPE, not a business function.

## The Story That Made Folders Click

Six months after implementing folders, we hired two new analysts: Alex (experienced) and Jordan (fresh from certification).

I gave them the same task: “Add year-over-year growth percentage for sales and customer count to the executive dashboard.”

**Jordan (without folder training):** 45 minutes. Built measures from scratch. Worked, but used different formulas than our standard.

**Alex (I showed the folder structure for 5 minutes):** 12 minutes. Found `_Sales Amount` in Base Measures. Found `Sales LY` in Time Intelligence. Created the variance measure following the pattern. Perfect.

The difference? **Architecture enables speed.**

Alex didn’t need to be a DAX expert. She just needed to follow the pattern that was already visible in the organization.

## Layer 2: Naming Conventions (The Findability Layer)

Folders help you browse. Naming conventions help you search.

**The Problem We Had:**

Same measure, five different names:

- `Customer Lifetime Value`
- `CLV`
- `LTV_Customer`
- `Customer_LTV_Total`
- `Lifetime Value (Customers)`

When someone searched for “lifetime value,” they found three of them. Missed two.

**The Solution: Naming Convention Framework**

We created a simple formula that every measure follows:

```c
[Business Object] [Metric Name] [Modifier] [Time Period]
```

**Examples:**

```c
✅ Customer Lifetime Value
✅ Sales vs Target %
✅ Revenue per Customer
✅ Profit Margin %
✅ Inventory Turnover Ratio
```

Breaking it down:

**Business Object (optional for context):**

- Customer, Sales, Product, Inventory
- Use when the metric applies to a specific domain

**Metric Name (required):**

- Lifetime Value, Conversion Rate, Margin
- The actual thing being measured

**Modifier (optional for calculation type):**

- vs Target, vs LY, per Customer
- Shows what kind of comparison or calculation

**Time Period (optional, only when baked in):**

- YTD, MTD, QTD, LY
- Only use if the time period is fixed in the measure

**Special Prefixes:**

```c
_ → Base measure (internal use)
# → Temporary/Test measure
! → Needs review/fix
```

**Examples in Practice:**

```c
_Sales Amount               (Base measure)
Sales LY                    (Time intelligence)
Sales vs LY                 (Comparison)
Sales vs LY %               (Comparison with format)
Sales Growth Rate           (KPI)
Revenue per Customer        (Ratio metric)
Customer Retention Rate     (KPI)
```

**What We Avoid:**

```c
❌ Calc_Rev_v2_final
❌ SALES_AMOUNT_2024
❌ my_test_measure
❌ DO_NOT_USE
❌ temp123
```

If you need to label something temporary, use the `#` prefix and delete it within the sprint.

## The Naming Convention Test

Here’s how we test if a measure name is good:

**Question 1**: Can someone find it by searching the most obvious term?

- If they search “lifetime value,” will they find it? ✅
- If they search “CLV,” will they find it? ❌ (Use description for abbreviations)

**Question 2**: Does the name describe WHAT, not HOW?

- ✅ “Customer Lifetime Value” (what it measures)
- ❌ “Sum of Revenue by Customer with SUMX” (how it’s calculated)

**Question 3**: Is it consistent with similar measures?

- If you have “Sales vs Target,” don’t also have “Target Variance — Revenue”
- Pick one pattern and stick to it

**Question 4**: Would a new team member understand it?

- Show the name to someone not on your team
- If they ask “what does that mean?”, the name fails
![](99.System/Attachments/1!n3yv8drDYGC6jTsVe16V6g.png.webp)

The Naming Convention Formula

## Layer 3: Documentation Standards (The Understanding Layer)

Good names and folders tell you WHERE and WHAT.

Documentation tells you WHY and HOW.

**The Problem:**

I found this measure in one of our older models:

```c
Adjusted Revenue = 
CALCULATE(
    [_Sales Amount],
    Sales[Status] = "Completed",
    Sales[Type] <> "Internal"
)
```

What’s “adjusted”? Why exclude internal? When should I use this instead of regular revenue?

Nobody knew. The analyst who built it had left 6 months ago.

**The Solution: Documentation Template**

We created a standard documentation format using measure descriptions:

```c
PURPOSE: What business question does this answer?
USAGE: When should this be used (and when NOT)?
DEPENDENCIES: What measures/tables does it rely on?
BUSINESS RULES: What filters or logic are applied?
OWNER: Who built it / who maintains it?
LAST MODIFIED: When was it last changed?
```

**Real Example:**

```c
Customer Lifetime Value = 
VAR AvgOrderValue = [Average Order Value]
VAR AvgFrequency = [Average Purchase Frequency]
VAR AvgLifespan = [Average Customer Lifespan]
VAR LTV = AvgOrderValue * AvgFrequency * AvgLifespan
RETURN
    LTV
```
```c
/* DOCUMENTATION
PURPOSE: Estimates total revenue a customer will generate over their relationship with the company
USAGE: Use for customer segmentation and acquisition cost decisions. NOT for actual revenue reporting.
DEPENDENCIES: [Average Order Value], [Average Purchase Frequency], [Average Customer Lifespan]
BUSINESS RULES: Only includes completed orders. Excludes returns and internal transactions.
FORMULA: AOV × Purchase Frequency × Customer Lifespan
OWNER: Sarah Chen (sarah.chen@company.com)
LAST MODIFIED: 2024-12-15
*/
```

**Why This Works:**

New analyst opens the measure. Immediately understands:

- What it does (PURPOSE)
- When to use it (USAGE)
- What it depends on (DEPENDENCIES)
- Who to ask if there’s a question (OWNER)

No guessing. No rebuilding from scratch.

**The Documentation Levels**

Not every measure needs extensive documentation. We use three levels:

**Level 1: Base Measures**

- Minimal documentation
- Purpose is obvious from the name
```c
_Sales Amount = SUM(Sales[Amount])
// Base measure for all sales calculations
```

**Level 2: Business Metrics**

- Medium documentation
- Explain any business rules
```c
Active Customers = 
CALCULATE(
    DISTINCTCOUNT(Sales[CustomerID]),
    Sales[OrderDate] >= TODAY() - 365
)
/* 
Active = purchased within last 365 days
Used for retention analysis
See Customer Analytics dashboard
*/
```

**Level 3: Complex KPIs**

- Full documentation template
- Everything someone needs to understand and maintain it

## The Documentation Story

Last month, our CFO questioned the customer churn rate we reported.

“Your dashboard shows 12% churn. Finance calculated 18%. Which is right?”

In the old days, this would’ve started a week-long investigation.

With documentation:

1. Opened the measure
2. Read the PURPOSE: “Monthly churn rate based on subscription cancellations”
3. Read BUSINESS RULES: “Excludes paused subscriptions and accounts in collections”
4. Called Finance: “Are you including paused subs?”
5. Finance: “Yes, we count those as churned”

Problem identified in 10 minutes.

Not a data error. Just different business definitions. Documentation made the difference crystal clear.

![](99.System/Attachments/1!iEHHoJ7zrHVU0ZDnKl-OPw.png.webp)

Documentation Template

## Layer 4: Governance Process (The Sustainability Layer)

You can build the perfect folder structure, naming convention, and documentation.

But if there’s no process to maintain it, chaos returns in 6 months.

**The Problem We Had:**

Beautiful organized library. Then:

- New analyst joins, doesn’t know the conventions
- Deadline pressure, someone adds a quick measure without organizing
- 3 months later, we have `Temp_Sales_v2` buried in the KPIs folder

**The Solution: Measure Governance Process**

We implemented a simple 3-step approval process:

**Step 1: Measure Proposal** Before building, answer:

- What business question does this answer?
- Does a similar measure already exist?
- Where will it fit in the folder structure?
- What should it be named?

**Step 2: Peer Review** Another analyst reviews:

- Is the logic correct?
- Does it follow naming conventions?
- Is it properly documented?
- Is it in the right folder?

**Step 3: Library Addition** Only after review, the measure gets added to the shared library.

**But What About Deadlines?**

We created an “exploratory” approach:

```c
📁 _Exploration
   📁 Alex_CustomerAnalysis
      - #Test Revenue Metric
      - #Cohort Analysis v1
```

Prefix with `#` = temporary. Personal folder = won't be reused yet.

When the analysis is done and the measure is proven: → Clean it up → Move to proper folder → Remove the # prefix → Add documentation

This way, people can move fast without breaking the library.

## The Governance Framework That Works

After 18 months, here’s what actually stuck:

**The Weekly Measure Review (15 minutes)**

Every Friday at 4 PM:

- Quick scan of new measures added that week
- Check for naming convention violations
- Flag measures in “\_Exploration” older than 2 weeks
- Celebrate good examples

**The Monthly Library Audit (30 minutes)**

First Monday of the month:

- Search for measures with `#` prefix
- Review “Utilities” for measures that should move
- Check for duplicate measures
- Update documentation for modified measures

**The Quarterly Cleanup Sprint (2 hours)**

Once per quarter:

- Delete deprecated measures (after confirming no visuals use them)
- Consolidate similar measures
- Update folder structure if business needs changed
- Train new team members on conventions

**The Library Champion Role**

We rotate this monthly. Responsibilities:

- Lead the weekly review
- Answer questions about conventions
- Update the style guide when patterns emerge
- Advocate for good practices

Not a policeman. A coach.

## The Architecture in Action: A Real Example

Let me show you how this works with a real scenario from last month.

**The Request:**

“We need to track customer engagement score for the C-suite dashboard.”

**Step 1: Check if it exists**

Search: “engagement”

- Found `Customer Engagement Rate` in KPIs folder
- Read documentation: “Based on website visits only”
- Not what we need. Our engagement includes website, email, and product usage.

**Step 2: Propose the measure**

Filled out the template:

- Business Question: “How engaged are our customers across all touchpoints?”
- Similar Measures: `Customer Engagement Rate` (different scope)
- Folder Location: `KPIs & Metrics → Customer`
- Proposed Name: `Customer Engagement Score`

**Step 3: Build with documentation**

```c
Customer Engagement Score = 
VAR WebVisits = [Web Engagement Points]
VAR EmailEngagement = [Email Engagement Points]  
VAR ProductUsage = [Product Usage Points]
VAR TotalPoints = WebVisits + EmailEngagement + ProductUsage
VAR MaxPossible = 100
VAR Score = DIVIDE(TotalPoints, MaxPossible, 0) * 100
RETURN
    Score
```
```c
/* DOCUMENTATION
PURPOSE: Composite score measuring customer engagement across all channels
USAGE: C-suite dashboard, customer health monitoring. Range: 0-100
DEPENDENCIES: [Web Engagement Points], [Email Engagement Points], [Product Usage Points]
BUSINESS RULES: 
  - Web: 40 points max (page views, time on site)
  - Email: 30 points max (opens, clicks)
  - Product: 30 points max (logins, feature usage)
FORMULA: (Web + Email + Product) / 100 * 100
OWNER: Alex Rivera (alex.rivera@company.com)
CREATED: 2024-11-15
REVIEWED BY: Sarah Chen
*/
```

**Step 4: Peer review**

Sarah checked:

- ✅ Naming follows convention
- ✅ Documentation complete
- ✅ Logic matches business definition
- ✅ In correct folder
- ⚠️ Suggested: Add a measure for each component score

**Step 5: Library addition**

Added to:

```c
📁 KPIs & Metrics
   📁 Customer
      - Customer Engagement Score ← New
      - Customer Engagement - Web ← Added per review
      - Customer Engagement - Email ← Added per review  
      - Customer Engagement - Product ← Added per review
```

**Total time:** 90 minutes from request to deployment.

**Result**: C-suite dashboard launched on schedule. Three weeks later, Sales team reused the same measure for their customer health analysis. Zero rework.

## The Power of “Build Once, Use Everywhere”

Here’s what happened after we implemented the full architecture:

**Month 1–3: Initial Setup**

- Reorganized 147 measures into folder structure
- Standardized naming conventions
- Added documentation to top 20 most-used measures
- Created governance process

Time invested: ~40 hours across the team

**Month 4–12: Sustainability Phase**

- New measures followed conventions automatically
- Weekly reviews caught violations early
- Library grew to 203 measures (all organized)
- Zero time spent searching for measures

**Year 2: The Payoff**

**Metric 1: Reuse Rate**

Before architecture:

- 89% of measures built from scratch
- Average time to find existing measure: 18 minutes
- Often faster to rebuild than find

After architecture:

- 67% of new measures built from existing components
- Average time to find existing measure: 2 minutes
- Reuse is now the default

**Metric 2: Onboarding Time**

Before:

- New analyst productive: 4–6 weeks
- Required 1-on-1 training on every measure
- Made mistakes from misunderstanding measures

After:

- New analyst productive: 1–2 weeks
- Self-service learning from documentation
- Mistakes reduced by 70%

**Metric 3: Consistency**

Before:

- Customer Lifetime Value calculated 3 different ways
- Profit margin formulas varied by dashboard
- “What’s our churn rate?” = 4 different answers

After:

- One authoritative measure per metric
- Consistent definitions across all dashboards
- Single source of truth

**The ROI Calculation:**

Time saved per week: 4 hours × 6 analysts = 24 hours/week Annual savings: 24 × 52 = 1,248 hours At $75/hour = **$93,600 per year**

Initial investment: 40 hours Ongoing maintenance: 1 hour/week = 52 hours/year Total cost: 92 hours = **$6,900**

**ROI: 1,257% in year one**

But the bigger benefit? Trust in the data. Confidence in the metrics. Speed of delivery.

## The Common Mistakes (And How to Avoid Them)

After helping 5 other teams implement this architecture, here are the mistakes I see repeatedly:

**Mistake 1: Over-organizing too early**

Don’t create 50 folders for a model with 20 measures.

Start simple:

- Base Measures
- Time Intelligence
- KPIs & Metrics

Add folders when you have 10+ measures in a category.

**Mistake 2: Inconsistent enforcement**

The architecture only works if EVERYONE follows it.

One person breaking conventions = back to chaos in 3 months.

Solution: Make it part of code review. No exceptions.

**Mistake 3: Documentation without context**

Bad documentation:

```c
// Calculates customer lifetime value
```

Good documentation:

```c
/* 
PURPOSE: Estimates total revenue per customer over their lifespan
USAGE: Marketing budget decisions, NOT financial reporting
DIFFERS FROM: [Actual Customer Revenue] (this is predictive)
*/
```

Documentation should answer questions a confused analyst will have.

**Mistake 4: Governance without flexibility**

If your process is too rigid, people will work around it.

We learned: Allow exploration. Require cleanup before sharing.

**Mistake 5: Building the architecture, then abandoning it**

The weekly review isn’t optional. The moment you skip it, measures start appearing in wrong places.

Sustainability requires consistency.

## The Architecture Template: Your Starting Point

Here’s the exact folder structure we use. Copy it, adapt it to your business:

```c
📁 _Base Measures
   📁 [Business Domain 1]
   📁 [Business Domain 2]
   📁 Date
📁 Time Intelligence
   📁 [Business Domain 1]
   📁 [Business Domain 2]
📁 Comparisons & Variance
   📁 [Business Domain 1]
   📁 [Business Domain 2]
📁 KPIs & Metrics
   📁 [Business Domain 1]
   📁 [Business Domain 2]
📁 Utilities
   - [Helper measures]
📁 Formatting
   - [Display measures]
📁 _Exploration
   📁 [Your Name]_[Project]
```

**Replace \[Business Domain\] with YOUR domains:**

- Sales, Customer, Product, Finance, Operations, Marketing, etc.

**Start with 3–5 domains. Add more as needed.**

## The Team Conversation You Need to Have

Before implementing this architecture, gather your team and discuss:

**Question 1: What are our business domains?**

Don’t use technical terms (Fact\_Sales, Dim\_Customer). Use business language (Sales, Customer, Product).

**Question 2: What’s our naming pattern?**

Agree on one convention. Write it down. Make examples.

**Question 3: How will we handle exploration?**

People need space to experiment without breaking the library. Define where that space is.

**Question 4: Who reviews new measures?**

Don’t make it one person’s job. Rotate. Share responsibility.

**Question 5: What happens to old measures?**

When someone finds `[DO_NOT_USE_OLD]`, what's the process? Delete? Deprecate? Document why it's still there?

**Get alignment BEFORE you start reorganizing.**

## The Implementation Roadmap

Here’s the 4-week plan we followed:

**Week 1: Foundation**

- Document current state (screenshot the chaos)
- Define folder structure
- Agree on naming conventions
- Create documentation template

**Week 2: Reorganization**

- Move measures into folders
- Rename measures that violate conventions
- Add basic documentation to top 20 measures
- Update all visuals (they’ll break when you rename)

**Week 3: Process**

- Document the governance process
- Schedule recurring reviews
- Assign first library champion
- Train team on conventions

**Week 4: Refinement**

- First weekly review
- Catch early violations
- Adjust conventions based on feedback
- Celebrate wins

**After Week 4: Sustainability**

The weekly cadence continues. The conventions become habit. The architecture becomes invisible — it just works.

## The Measure That Made This Click

After implementing the architecture, a new analyst (Jordan) joined the team.

Her first task: “Add a year-over-year comparison of customer acquisition cost to the marketing dashboard.”

I didn’t help her. I wanted to see if the architecture worked.

**What Jordan did:**

1. Opened the model
2. Saw the folder structure
3. Found `Customer Acquisition Cost` in `KPIs & Metrics → Customer`
4. Read the documentation
5. Found `Customer Acquisition Cost LY` in `Time Intelligence → Customer`
6. Created `Customer Acquisition Cost vs LY` following the pattern she saw
7. Placed it in `Comparisons & Variance → Customer`
8. Added documentation following the template

**Time**: 22 minutes, including time to read existing measures.

**Result**: Perfect. No errors. Followed all conventions. Needed zero correction.

When I asked how she knew what to do:

“The organization made it obvious. I just followed the pattern.”

That’s when I knew the architecture worked.

## Your Turn: The 30-Day Challenge

Here’s what I want you to do:

**Week 1: Audit**

- Count your measures
- Screenshot your current organization
- List your top 10 most-used measures
- Ask your team: “Can you find \[specific measure\] in under 1 minute?”

**Week 2: Design**

- Define 3–5 business domains
- Create folder structure
- Write naming convention rules
- Design documentation template

**Week 3: Implement**

- Reorganize top 20 measures
- Rename violations
- Add documentation
- Update visuals

**Week 4: Process**

- First team review
- Document learnings
- Adjust conventions
- Celebrate progress

**Don’t try to fix everything at once.**

Start with your most-used measures. Get those right. Then expand.

## The Question I Get Asked Most

“This seems like a lot of overhead. Is it worth it?”

My answer: **It depends on your team size and model complexity.**

**When it’s NOT worth it:**

- Solo analyst
- 20 measures or fewer
- Simple, well-understood calculations
- Model rarely changes

**When it’s ESSENTIAL:**

- Team of 2+ analysts
- 50+ measures
- Models shared across departments
- Frequent new measure requests
- High turnover

But here’s the thing: Even solo analysts benefit.

Because the “team” isn’t just current you. It’s future you. The person who looks at `[Calc_Rev_Final_v3]` in 6 months and has no idea what it does.

Architecture is a gift to your future self.

## The Real Transformation

Six months ago, our Slack channel had daily messages:

“Where’s the customer lifetime value measure?” “Do we have sales vs target?” “Why are there three profit margin calculations?”

Today?

Silence.

Not because people stopped needing measures. Because they can find them.

The architecture transformed DAX from a collection of calculations into a library. A system. A shared resource that makes everyone more productive.

And the best part?

New analysts look at our models and say: “This is so well organized. How long did it take to build?”

The answer: “Eight years of mistakes. But only 4 weeks to implement the solution.”

You don’t need 8 years.

You just need 4 weeks and a commitment to sustainability.

**What’s your biggest challenge with organizing DAX measures? Drop it in the comments and let’s discuss solutions.**

**And if this framework helped you rethink how you structure your measures library, share it with another analyst who’s drowning in their measures table. We’ve all been there.**