---
title: "We Replaced 47 Excel Files With One Power BI Model. Here’s What Actually Happened."
source: "https://medium.com/towards-artificial-intelligence/we-replaced-47-excel-files-with-one-power-bi-model-heres-what-actually-happened-d7f1fba4db98"
author:
  - "[[Gulab Chand Tejwani]]"
published: 2026-02-10
created: 2026-07-27
description: "15 hours every Monday copying data. Daily errors. Zero trust in the numbers. Here’s what actually happened when we migrated from Excel chaos to Power BI."
Processed: "Unprocessed"
---
## 15 hours every Monday copying data. Daily errors. Zero trust in the numbers. Here’s what actually happened when we migrated from Excel chaos to Power BI.

![](99.System/Attachments/1!3LhvbkjQciC5r98eAfY_qQ.png.webp)

We Replaced 47 Excel Files with One Power BI Model

Monday, 6:23 AM. My phone buzzed.

Text from the VP of Sales: “Revenue dashboard broken. Meeting with CEO in 2 hours. HELP.”

I opened my laptop. Checked the shared drive.

The file was there: `Q3_Revenue_Report_FINAL_v8_USE_THIS_ONE.xlsx`

Opened it. Macros failed to run. #REF! errors everywhere. The pivot tables showed data from August instead of September.

Someone had edited the file over the weekend. Nobody knew who. Nobody knew what they changed.

This wasn’t a one-time problem. This was our weekly crisis.

We had 47 Excel files that ran the business. Updated manually. Emailed around. Copy-pasted together. Breaking constantly.

The sales team spent 15 hours every Monday just updating spreadsheets.

That morning, the CEO made a decision that changed everything:

“Fix this. I don’t care how. We can’t run a $50M business on broken spreadsheets.”

Six months later, we had replaced all 47 files with one Power BI model.

The transformation wasn’t smooth. People fought it. Systems broke. I made mistakes I never expected.

But today? The sales team spends 30 minutes on Monday updates instead of 15 hours. Error rate dropped from daily mistakes to zero errors in three months. The CFO trusts the numbers for the first time in years.

This is the story of what actually happened when we migrated from Excel chaos to Power BI. The good. The bad. The parts nobody talks about.

## The Excel Ecosystem of Doom

Before I show you the migration, you need to understand what we were dealing with.

**The 47 Files:**

I cataloged every critical Excel file in the company. Here’s what I found:

📊 Sales Files (14 files):

- Regional sales trackers (5 files, one per region)
- Product performance dashboards (3 files)
- Sales pipeline forecasts (2 files)
- Commission calculations (4 files, different formulas per team)

💰 Finance Files (11 files):

- Monthly P&L consolidation (1 master, 5 regional inputs)
- Budget vs. actual tracking (2 files)
- Cash flow projections (3 files, one per quarter)

📦 Operations Files (9 files):

- Inventory tracking (4 files, one per warehouse)
- Fulfillment metrics (2 files)
- Vendor performance (3 files)

👥 HR Files (6 files):

- Headcount tracking (2 files)
- Recruitment pipeline (1 file)
- Performance reviews (3 files, one per department)

📈 Executive Files (7 files):

- Weekly KPI dashboard (1 master file linking to 6 others)
- Board meeting deck data (3 files)
- Strategic planning models (3 files)

**The Update Process:**

Every Monday, like clockwork:

5:30 AM — IT exports data from the ERP system to a shared folder 6:00 AM — Finance pulls sales data, copy-pastes into their workbooks 7:00 AM — Sales pulls the finance data, updates their regional trackers 8:00 AM — Operations updates inventory from another system 9:00 AM — Someone manually consolidates everything into the executive dashboard 10:00 AM — VP of Sales presents to the CEO

That’s the plan. In reality:

6:15 AM — Export fails, IT has to manually run it 7:30 AM — Finance finds data errors, has to manually fix 200+ rows 8:45 AM — Sales can’t find the latest file version, uses old data 9:20 AM — Operations discovers their formulas broke, scrambles to fix 10:00 AM — CEO meeting starts with wrong numbers

**The Human Cost:**

Sarah (Finance Manager): “I spend 6 hours every Monday just moving data around. Not analyzing it. Just copy-paste-format-pray.”

Marcus (Sales Operations): “We have version 8 of the revenue file. I think. Unless someone edited version 7 after we created version 8. Then which one is right?”

Alex (VP of Sales): “I don’t trust the numbers anymore. I see ‘revenue up 15%’ but I can’t trace where that came from. Did someone fat-finger a formula? Is it real?”

**The Breaking Point:**

September 18th, 2:14 PM.

Board meeting. CFO presenting Q3 results.

Slide 3: “Revenue up 23% quarter-over-quarter”

Board member: “That’s incredible! What drove it?”

CFO starts explaining. Pulls up the Excel file to drill into details.

The formula in cell D47 returns #REF!

The pivot table shows different numbers than the chart.

The regional breakdown doesn’t add up to the total.

“Can we… take a 10-minute break?” the CFO asked.

The break lasted 45 minutes while finance scrambled to verify the numbers.

Turned out: Revenue was up 12%, not 23%. Someone had manually overwritten a formula three weeks ago. Nobody noticed until the board meeting.

**That afternoon, the CEO called me into his office.**

“This is unacceptable. We’re making million-dollar decisions on spreadsheets held together with duct tape. I want a solution. You have 90 days.”

I had two options:

Option 1: Try to “fix” Excel. Better processes. More checks. Tighter controls.

Option 2: Rebuild everything in Power BI.

Excel wasn’t the problem. Excel at scale was the problem. More processes wouldn’t fix architectural chaos.

I chose Option 2.

![](99.System/Attachments/1!HRdxa0LyWmVdj5fndSye8w.png.webp)

The Excel Ecosystem of Doom

## Week 1–2: The Audit and Priority Matrix

I didn’t start by building anything. I started by understanding what we actually had.

**The Catalog:**

I created a spreadsheet (ironically) documenting all 47 files:

For each file I recorded:

- Purpose (what business question does it answer?)
- Owner (who maintains it?)
- Update frequency (daily, weekly, monthly?)
- Number of users (who looks at it?)
- Data sources (where does the data come from?)
- Downstream dependencies (what other files link to this?)
- Pain points (what breaks most often?)

**The Interviews:**

I spent 2 hours with each department head:

Finance (Sarah): “The P&L consolidation is our biggest nightmare. Five regional files that never match. Formulas break constantly. We spend 8 hours reconciling every month.”

Sales (Marcus): “The commission calculations are wrong 30% of the time. Sales reps don’t trust them. I manually verify every calculation. Takes me 12 hours every month.”

Operations (Jordan): “Inventory data is always 2–3 days old by the time we update the spreadsheet. We’ve ordered $180K in excess inventory this year because our data was stale.”

HR (Linda): “The headcount tracker is fine. Honestly, we could keep using Excel for this. It’s simple. It works.”

**The Priority Matrix:**

I ranked all 47 files on two dimensions:

Dimension 1: Business Impact

- High: Used by executives, affects major decisions, high error rate
- Medium: Used by managers, affects operations
- Low: Informational, low error impact

Dimension 2: Effort to Migrate

- High: Complex formulas, multiple data sources, heavy VBA
- Medium: Standard calculations, 1–2 data sources
- Low: Simple lookups, single data source

**The Results:**

High Impact + Low Effort (QUICK WINS — Do First):

- Sales pipeline dashboard
- Regional revenue trackers
- Weekly KPI dashboard

High Impact + High Effort (BIG PROJECTS — Do Second):

- P&L consolidation
- Commission calculations
- Executive board deck

Low Impact + Low Effort (EASY WINS — Do Third):

- Vendor performance
- Recruitment pipeline

Low Impact + High Effort (SKIP FOR NOW):

- HR headcount tracker (Excel is fine)
- Strategic planning models (too custom, keep in Excel)

**The Strategy:**

I wouldn’t migrate all 47 files. I’d migrate 38 files that would give us 90% of the value.

The remaining 9 files could stay in Excel. Some things don’t need to be in Power BI.

**The Timeline:**

Week 1–2: Audit ✓ Week 3–4: Build data warehouse foundation Week 5–8: Migrate Quick Wins (3 files) Week 9–14: Migrate Big Projects (3 files) Week 15–18: Migrate Easy Wins (remaining files) Week 19–20: Parallel run (Excel + Power BI side by side) Week 21: Cutover Week 22–24: Support and optimization

90 days total.

I presented the plan to the CEO.

“What if you can’t do it in 90 days?” he asked.

“Then I’ll tell you at day 75 and we’ll extend the timeline. But I won’t rush this. A broken Power BI system is worse than Excel.”

He approved.

![](99.System/Attachments/1!TAx2OZwzkHdCBaX2k-LOUg.png.webp)

The 21- Week Migration Journey

## Week 3–4: Building the Foundation (The Part Everyone Skips)

Most people want to jump straight to building reports.

I’ve learned the hard way: If the foundation is broken, everything built on top of it is broken.

**The Data Warehouse Design:**

I designed a simple star schema:

Fact Tables:

- FactSales (every sales transaction)
- FactInventory (daily inventory snapshots)
- FactFinancials (monthly financial entries)

Dimension Tables:

- DimDate (every day from 2020–2030)
- DimProduct (all products)
- DimCustomer (all customers)
- DimEmployee (all employees)
- DimRegion (all regions/territories)
- DimAccount (chart of accounts for finance)

**The ETL Process:**

I built SQL Server Integration Services (SSIS) packages to:

Extract:

- Sales transactions from ERP (every hour)
- Inventory levels from warehouse system (every 4 hours)
- Financial data from accounting system (nightly)

Transform:

- Clean product names (standardize “Widget A” vs “WidgetA” vs “WIDGET-A”)
- Validate dates (catch future dates, nulls, invalid formats)
- Calculate derived fields (profit margin, days in inventory, etc.)
- Flag anomalies (sales over $100K, negative inventory, etc.)

Load:

- Append to fact tables (incremental load)
- Update dimension tables (slowly changing dimensions)
- Log every load with timestamp and row count

**The Critical Decision: Incremental Refresh:**

The ERP system had 8 years of sales history. 14 million rows.

Loading all 14 million rows every night would take hours.

I implemented incremental refresh:

- Historical data (older than 2 years): Load once, never refresh
- Recent data (last 2 years): Refresh nightly
- Current month: Refresh every hour

This cut refresh time from 3 hours to 12 minutes.

**The Validation Layer:**

Before loading data into the warehouse, I added validation:

```c
-- Check 1: Row count shouldn't drop more than 10%
DECLARE @TodayCount INT = (SELECT COUNT(*) FROM TodaysLoad)
DECLARE @YesterdayCount INT = (SELECT COUNT(*) FROM YesterdayLoad)

IF @TodayCount < (@YesterdayCount * 0.9)
BEGIN
    RAISERROR('ERROR: Row count dropped 10%+. Check source system.', 16, 1)
    ROLLBACK
END

-- Check 2: No future dates
IF EXISTS (SELECT 1 FROM TodaysLoad WHERE OrderDate > GETDATE())
BEGIN
    RAISERROR('ERROR: Future dates found in OrderDate column.', 16, 1)
    ROLLBACK
END

-- Check 3: Sales total within expected range
DECLARE @TodayTotal MONEY = (SELECT SUM(Amount) FROM TodaysLoad)
DECLARE @HistoricalAvg MONEY = (SELECT AVG(DailyTotal) FROM HistoricalLoads)

IF @TodayTotal > (@HistoricalAvg * 3)
BEGIN
    RAISERROR('WARNING: Total sales 3x higher than historical average.', 10, 1)
    -- Don't rollback, just warn
END
```

These checks caught 6 data quality issues in the first month.

**The Documentation:**

I created a data dictionary:

Every table documented with:

- Business purpose
- Refresh frequency
- Data source
- Key fields
- Grain (what does one row represent?)
- Example queries

Every field documented with:

- Business definition
- Data type
- Source system + field
- Calculation logic (if derived)
- Business rules (if any)

**Why This Matters:**

Two months later, we hired a new analyst. Jordan.

I gave her the data dictionary. Told her to explore.

She came back 2 hours later: “I built a customer retention analysis. Is this right?”

She’d done it correctly. No help needed. Because the documentation was clear.

That’s when I knew the foundation was solid.

## Week 5–8: The First Migration (Learning Everything the Hard Way)

I started with a “Quick Win”: The Sales Pipeline Dashboard.

Low complexity. High visibility. If it worked, people would trust the system.

**The Original Excel File:**

`Sales_Pipeline_Dashboard_v3.xlsx`

Features:

- 3 pivot tables showing deals by stage
- Conditional formatting (green = healthy, red = at risk)
- VBA macro to refresh all data
- Email button to send snapshot to VP of Sales
- Last 30 days of snapshot history on hidden tabs

Used by: 8 sales managers, updated daily

**The Power BI Build — Attempt 1:**

I rebuilt it exactly as it looked in Excel.

Three visuals:

- Table showing deals by stage
- Bar chart showing pipeline value by rep
- Line chart showing pipeline trend over time

Took me 3 hours to build.

I showed it to Marcus (Sales Operations).

His response: “It looks… different. Where’s the detail I’m used to seeing?”

I showed him how to drill down into the table.

“But in Excel, I can see everything at once. Why is this better?”

**I made a critical mistake: I assumed “looks the same” would be enough.**

**The Power BI Build — Attempt 2:**

I scheduled a 1-hour session with Marcus and two sales managers.

“Show me exactly how you use the Excel file. Click by click.”

Marcus opened Excel:

1. Looks at the summary pivot: “Which stage has the most deals?”
2. Clicks into the detail: “Which deals have been stuck in Stage 2 for over 30 days?”
3. Filters by rep: “How is Jennifer’s pipeline compared to last month?”
4. Makes notes: “I type notes directly in column Z for deals at risk”
5. Exports to PDF: “I email this snapshot to my VP every Friday”

**I realized: I wasn’t replacing a dashboard. I was replacing a workflow.**

**The Power BI Build — Attempt 3 (The One That Worked):**

Page 1: Executive Summary

- Cards showing total pipeline value, # of deals, average deal size
- Bar chart: Pipeline by stage
- Line chart: Pipeline trend (last 90 days)
- Slicer: Filter by region, rep, or product

Page 2: Deal Details

- Table: Every deal with key fields
- Conditional formatting: Red for deals stuck 30+ days
- Drill-through: Click any deal to see full history

Page 3: Rep Performance

- Matrix: Reps × Stages with deal counts
- Sparklines showing trend per rep
- Bookmarks: Toggle between “This Month” and “Last Month” view

Plus:

- Subscription: Automatically emails snapshot to VP every Friday 8:00 AM
- Comments: Sales managers can add notes right in Power BI (using Power BI comments feature)

I showed this to Marcus.

“NOW we’re talking,” he said. “This is better than Excel. I can see patterns I couldn’t see before.”

**The Lesson:**

Don’t rebuild what the Excel file looks like. Rebuild what the Excel file does.

Understand the workflow, not just the visuals.

**The Rollout:**

Week 5: Built the report Week 6: Tested with Marcus Week 7: Trained 8 sales managers (30-minute sessions each) Week 8: Parallel run (Excel + Power BI both running)

During parallel run, I asked everyone to check both systems daily and report discrepancies.

Found 3 issues:

- Date logic was off (closed vs. projected close date)
- One rep’s deals weren’t showing up (filtering issue)
- Pipeline value calculations differed from Excel (rounding issue)

Fixed all three. Verified results matched Excel exactly.

Week 8, Friday 4:35 PM: Set the Excel file to read-only.

Monday morning: No complaints. Pipeline dashboard working.

**First migration: Success.**

## Week 9–14: The Big Project (Where Everything Almost Failed)

Next up: The P&L Consolidation.

This was the file that broke in the board meeting. The one that cost us credibility with the board.

**The Challenge:**

5 regional finance managers each maintained their own P&L in Excel.

Corporate finance pulled all 5 files, manually copy-pasted them into a master consolidation file.

The formulas were… creative.

Example: `=IF(ISERROR(VLOOKUP(...)), VLOOKUP(..., different range), original VLOOKUP)`

Translation: “If the lookup fails, try looking in a different place. If that fails too, just show the error.”

The file had 8,000 rows. 340 columns. 47 tabs.

**My First Attempt: Do It All At Once:**

I spent 2 weeks building a comprehensive financial data model.

Chart of accounts. Budget vs. actual. Variance analysis. Historical trends. Drill-downs by department, region, account, month.

I showed it to Sarah (Finance Manager).

She stared at it for 30 seconds.

“This is overwhelming. I don’t know where to start.”

**I made the second critical mistake: Trying to do too much at once.**

**The Better Approach: Crawl, Walk, Run:**

Phase 1 (Crawl): Just replace the consolidation

- Pull regional P&Ls from the warehouse
- Stack them vertically
- No fancy visuals, just a table
- Must match Excel exactly

Phase 2 (Walk): Add basic analysis

- Budget vs. actual comparison
- Simple variance calculations
- Filter by region, month

Phase 3 (Run): Advanced features

- Drill-downs by account
- Historical trends
- Forecasting

**Phase 1 Took 3 Weeks:**

Not because it was technically hard. Because getting the numbers to match Excel was nearly impossible.

The Excel file had years of manual adjustments:

- Cell D235 manually changed from $45,000 to $48,000 (why? nobody knows)
- Row 892 had a hardcoded adjustment of -$12,500 (also unclear why)
- Column AF had a formula that referenced a cell in a different, closed workbook

I documented every discrepancy:

- 47 cells with manual overrides
- 23 formulas referencing external files
- 12 accounts that summed incorrectly (Excel bugs? Intentional? Unknown.)

I had a choice:

Option A: Replicate every quirk in Power BI to match Excel exactly Option B: Build it “correctly” and document why it differs

**I chose Option B. This almost ended the project.**

Week 11, Tuesday 9:52 AM. Meeting with the CFO.

CFO: “Your Power BI report shows Q3 operating expenses at $2.3M. The Excel file shows $2.4M. Which is right?”

Me: “The Power BI number is correct. The Excel file has 8 manual adjustments that shouldn’t be there. I documented them all — “

CFO: “I’ve used that Excel file for 3 years. The board uses those numbers. Are you telling me I’ve been reporting wrong numbers?”

Me: “Well… yes. But — “

CFO: “Fix it. Make Power BI match Excel.”

**The Reconciliation From Hell:**

I spent the next week building a reconciliation report:

Excel Total: $2,400,000 Minus: Manual override in D235 (-$3,000) Minus: External file reference error (-$15,000) Minus: Duplicate row 892 (-$12,500) Plus: Missing account 7230 (+$45,000) … (43 more adjustments) Power BI Total: $2,300,000

I showed this to the CFO.

“So Power BI is right, but we’ve been reporting wrong numbers for 3 years?”

“Yes.”

Long silence.

“Okay. Let’s go with the Power BI numbers. But I need you to explain this to the CEO.”

**The CEO Meeting (Where I Almost Got Fired):**

Friday 2:18 PM. CEO’s office.

CEO: “The CFO tells me our financial reports have been wrong for 3 years.”

Me: “Not wrong, exactly. Excel had accumulated adjustments that — “

CEO: “Are the new numbers correct?”

Me: “Yes. I’ve verified them against the source system. The Power BI numbers are accurate.”

CEO: “Can you prove it?”

I pulled up a drill-down. Showed him account 7230. Showed the source system. Showed how Excel missed it.

CEO: “How many other errors are there?”

Me: “47 discrepancies total. Most are small. Three are material.”

CEO: “And you found all of them in 3 weeks. How did finance miss them for 3 years?”

Me: “Because in Excel, you can’t trace the data lineage. In Power BI, every number has a clear path back to the source.”

The CEO leaned back.

“Continue with the migration. But from now on, document EVERYTHING. I want to know exactly how every number is calculated.”

**Phase 2 and 3 Went Smoothly:**

After the reconciliation nightmare, the rest was easy.

Added budget vs. actual comparisons (Week 12–13). Added drill-downs and historical trends (Week 14).

Final result: A financial reporting system that the CFO trusted more than Excel.

**The Lesson:**

Expect resistance when new numbers don’t match old numbers. Even when new numbers are correct.

Document the reconciliation. Show the lineage. Prove the accuracy.

## Week 15–18: The Migration Factory (When We Hit Our Stride)

By week 15, we had a system.

Every new migration followed the same process:

**Monday:**

- Audit the Excel file
- Interview the owner
- Document the workflow
- Identify data sources

**Tuesday-Wednesday:**

- Build the data model (if needed)
- Create the report (basic version)
- Validate calculations

**Thursday:**

- User testing
- Fix discrepancies
- Refine based on feedback

**Friday:**

- Deploy to test environment
- Schedule training

**Next Week:**

- Parallel run (both systems)
- Document issues
- Prepare for cutover

We migrated 6 files per week using this process.

**Files Migrated (Week 15–18):**

Week 15:

- Inventory tracking (4 warehouse files → 1 report)
- Vendor performance tracking

Week 16:

- Commission calculations (finally!)
- Recruitment pipeline

Week 17:

- Fulfillment metrics
- Product performance dashboards

Week 18:

- Regional sales trackers (5 files → 1 report with regional filter)
- Strategic planning inputs

**The Commission Calculation Victory:**

Remember Marcus spending 12 hours every month manually verifying commission calculations?

The Excel file was a monster:

- Different formulas per sales tier
- Accelerators that kicked in at certain thresholds
- Special deals with custom commission structures
- Manual adjustments “because we promised Jennifer 15% on this deal”

I rebuilt it in DAX:

```c
Commission = 
VAR BaseTier = 
    SWITCH(
        TRUE(),
        [YTD Sales] < 500000, 0.08,
        [YTD Sales] < 1000000, 0.10,
        [YTD Sales] >= 1000000, 0.12,
        0.08
    )
VAR Accelerator =
    IF([YTD Sales] > 1000000, 0.02, 0)
VAR SpecialDealBonus =
    CALCULATE(
        SUM(Deals[BonusAmount]),
        Deals[SpecialCommission] = TRUE
    )
VAR TotalRate = BaseTier + Accelerator
VAR Commission = ([Monthly Sales] * TotalRate) + SpecialDealBonus
RETURN Commission
```

Plus a table for manual adjustments (documented with reason and approver).

Marcus tested it against 3 months of historical commissions.

Match rate: 98.7%

The 1.3% discrepancies were Excel errors (rounding issues, missed deals).

**Marcus’s response:**

“I just got 12 hours of my life back every month. What do I do with all this free time?”

**The Inventory Victory:**

Operations had 4 Excel files (one per warehouse) updated manually from the warehouse management system.

Jordan (Operations Manager) exported data every morning at 6:00 AM. Copy-pasted into Excel. Updated formulas. Sent to procurement by 8:00 AM.

By the time procurement saw it, the data was 2+ hours old.

In Power BI, we set up direct query to the warehouse system.

Real-time data. No manual updates.

First week with the new system, Jordan caught an inventory issue at 7:15 AM that would’ve cost $23K in emergency shipping.

“The old system wouldn’t have shown this until tomorrow,” she said.

**By Week 18, We Had Momentum:**

The Sales team loved their dashboards. Finance trusted the numbers. Operations was saving hours every day.

But we hadn’t won yet.

The hardest part was still coming.

## Week 19–20: The Parallel Run (Where Doubt Crept In)

Two systems running simultaneously. Excel and Power BI.

The goal: Prove Power BI was ready. Find any remaining issues. Build confidence.

**The Rules:**

1. Everyone must check BOTH systems daily
2. Report any discrepancies immediately
3. Make decisions based on Power BI, verify with Excel
4. Track which system you trust more (anonymous survey)

**Week 19 — Day 1 (Monday 5:45 AM):**

I woke up early. Checked all the reports.

Everything loaded. Numbers looked right.

5:58 AM: First email.

Sarah (Finance): “Power BI showing Q3 revenue at $12.1M. Excel shows $12.3M. Which is right?”

6:02 AM: I checked the data lineage.

Power BI pulled from the warehouse. Warehouse pulled from ERP. All matched.

Excel? Someone had manually adjusted a cell three weeks ago. The adjustment was wrong.

Power BI: Correct. Excel: Wrong.

6:05 AM: Second email.

Marcus (Sales): “Pipeline dashboard not showing Jennifer’s deals. Is it broken?”

6:08 AM: I checked. Jennifer’s region was set to “West Coast” in the ERP. The regional filter in Power BI used “Western Region.”

Data inconsistency in the source system.

Fixed the mapping. Added a data quality alert for future mismatches.

6:12 AM: Third email.

Jordan (Operations): “Why does inventory look different between systems?”

Turns out: Excel used yesterday’s 6:00 AM snapshot. Power BI showed real-time data.

Not a bug. A feature.

But nobody told Jordan it was real-time. My fault for not documenting this clearly.

**Week 19 — Days 2–5:**

17 discrepancy reports.

9 were Excel errors (manual adjustments, stale data, formula mistakes). 5 were Power BI issues (filtering bugs, calculation errors, data refresh failures). 3 were source data problems (neither system was “wrong,” source data was inconsistent).

Every issue fixed within 24 hours.

**Week 19 — The Anonymous Survey:**

End of week survey question: “Which system do you trust more?”

Results:

- Power BI: 67%
- Excel: 18%
- Not sure: 15%

Progress. But not overwhelming confidence.

**Week 20 — The Stress Test:**

Monday morning. Month-end close.

This was the real test. If Power BI could handle month-end reporting, it could handle anything.

5:30 AM: Finance began month-end close process.

Normally took them until 2:00 PM.

9:47 AM: Sarah (Finance) sent a message.

“We’re done.”

I called her. “Done with what?”

“Month-end close. The Power BI reports auto-updated as soon as we posted the journal entries. We just reviewed them for accuracy. Took 4 hours instead of 8.”

**Week 20 — Wednesday:**

Sales QBR (Quarterly Business Review).

Marcus presented pipeline and revenue analysis to the executive team.

He used Power BI. Didn’t even open Excel.

Drilled down into regions. Filtered by product. Showed trends.

One executive asked: “Can you show me just the West Coast deals over $500K?”

Marcus clicked two slicers. Data appeared instantly.

In Excel, this would’ve taken 10 minutes of filtering and copy-pasting.

**Week 20 — Friday:**

End of parallel run.

Final survey: “Are you ready to switch to Power BI only?”

Results:

- Yes: 81%
- No: 8%
- Need more time: 11%

**Decision made: We’re cutting over.**

## Week 21: The Cutover (The Scariest Day of My Career)

Friday, October 18th. 3:30 PM.

I sent the email to the entire company:

**Subject: Excel Files Moving to Read-Only Status — Monday 8:00 AM**

Effective Monday, October 21st at 8:00 AM, the following Excel files will be set to read-only:

\[List of 38 files\]

All reporting will be done through Power BI.

Excel files will remain accessible for 90 days as reference, then will be archived.

If you have questions, contact me directly.

Send.

I stared at my screen.

**Had I missed something? Was there a file someone depended on that I didn’t know about?**

3:45 PM: First reply.

“FINALLY. Those Excel files were a nightmare.” — Marcus

3:52 PM: Second reply.

“Quick question — where’s the HR headcount tracker in Power BI?” — Linda (HR)

Oh no.

I checked my migration list. HR headcount tracker was in the “Skip For Now” category.

3:54 PM: I called Linda.

“Linda, we’re keeping that in Excel. It’s working fine, doesn’t need to migrate.”

“Oh. Okay. I thought EVERYTHING was moving to Power BI.”

**Crisis averted. First of many.**

**Monday, October 21st — 6:00 AM:**

I was in the office early. Monitoring the data refresh.

All reports refreshed successfully.

6:15 AM: First user logged into Power BI. Sarah (Finance).

6:22 AM: Second user. Marcus (Sales).

6:30 AM: Ten users online.

No emails. No calls.

**Good news or bad news? Were people working, or had everyone given up?**

7:15 AM: First Slack message.

Jordan (Operations): “Just found an issue with the inventory report. Location filter isn’t working.”

7:16 AM: I checked. Bug in the slicer logic.

7:23 AM: Fixed and republished.

7:25 AM: Jordan confirmed it worked.

8:00 AM: CEO’s weekly staff meeting.

I sat in the back, laptop open, ready to troubleshoot.

CFO pulled up the financial dashboard. Worked perfectly.

VP of Sales pulled up pipeline dashboard. Worked perfectly.

COO pulled up operations metrics. Worked perfectly.

**Meeting concluded without a single issue.**

8:45 AM: CEO stopped me in the hallway.

“I didn’t hear any complaints about the dashboards. Does that mean it’s working?”

“So far, yes.”

“Good. Keep monitoring it.”

**The First Week:**

Monday-Wednesday: 23 support requests. All minor (how-to questions, filter confusion, requests for new features).

Thursday: 5 support requests.

Friday: 2 support requests.

**By Friday, people had adapted.**

**The Unexpected Win:**

Week 2 after cutover.

New analyst started. Emma.

Her first task: “Analyze customer retention by cohort.”

In the old Excel world, this would’ve taken her:

- 2 days to find the right files
- 1 day to understand the formulas
- 3 days to build the analysis
- Total: 6 days

With Power BI:

- 2 hours to explore the data model
- 3 hours to build the analysis
- Total: 5 hours

**One day vs. one week. For a brand new employee.**

## Month 2–3: The Cleanup (Fixing What We Didn’t Know Was Broken)

Cutover was successful. But we weren’t done.

**The Issues Nobody Reported:**

Week 5 post-cutover: I ran a usage analysis.

12 reports were accessed 0 times in a month.

Why build reports nobody uses?

I called the supposed owners.

“Oh, we don’t need that anymore. Sarah used to use it but she left 6 months ago.”

Deleted 12 unused reports.

**The Performance Issues:**

One report took 45 seconds to load.

Users complained. “Excel was faster.”

I optimized it:

- Removed unnecessary columns from the data model
- Created aggregated tables for summary views
- Implemented incremental refresh
- Added query folding to push filters to the source

New load time: 3.2 seconds.

**The “Can You Add…” Requests:**

Month 2: 47 feature requests.

Sample requests:

- “Can you add a comparison to last year?”
- “Can we filter by customer segment?”
- “Can we export this to PDF?”
- “Can we get alerts when inventory drops below threshold?”

I couldn’t build 47 features. I’d never finish.

**The Priority Framework:**

I created a request system:

Every request scored on:

- Impact: How many people benefit? (1–5)
- Effort: How long to build? (1–5)
- Strategic: Does this align with company goals? (1–5)

Formula: Priority = (Impact × Strategic) / Effort

Highest scores got built first.

Of 47 requests:

- Built immediately: 8 (high impact, low effort)
- Scheduled for next sprint: 12 (high impact, medium effort)
- Backlog: 18 (medium impact, various effort)
- Declined: 9 (low impact or misaligned with strategy)

**The Training We Should’ve Done Earlier:**

Month 3: I ran 3 training sessions:

Session 1: Power BI Basics (for casual users)

- How to navigate reports
- How to use filters and slicers
- How to export data
- 45 minutes, 32 attendees

Session 2: Power BI Intermediate (for power users)

- Creating personal bookmarks
- Using drill-through
- Setting up subscriptions
- Building simple reports
- 90 minutes, 18 attendees

Session 3: Power BI Advanced (for analysts)

- Understanding the data model
- Writing simple DAX
- Creating ad-hoc reports
- Best practices
- 2 hours, 8 attendees

**Feedback:**

“Why didn’t we do this on Day 1?” — Multiple people

They were right. I should’ve done training BEFORE cutover, not after.

Lesson learned.

## Month 6: The Results (What Actually Changed)

Six months after cutover. Time to measure what actually happened.

**Time Saved:**

Before (Weekly Hours on Manual Updates):

- Finance: 18 hours
- Sales: 12 hours
- Operations: 8 hours
- HR: 3 hours
- Total: 41 hours/week

After:

- Finance: 2 hours (reviewing automated reports)
- Sales: 1 hour (updating pipeline notes)
- Operations: 0.5 hours (spot-checking inventory)
- HR: 3 hours (still using Excel, didn’t migrate)
- Total: 6.5 hours/week

**Time saved: 34.5 hours/week = 1,794 hours/year**

At an average cost of $65/hour: **$116,610 saved annually**

**Error Rate:**

Before (Errors Reported):

- Month 1 (pre-Power BI): 14 errors
- Month 2: 11 errors
- Month 3: 12 errors
- Average: 12.3 errors/month

After (Errors Reported):

- Month 4 (post-cutover): 3 errors
- Month 5: 1 error
- Month 6: 0 errors
- Average: 1.3 errors/month

**89% reduction in reported errors.**

**Decision Speed:**

We tracked how long it took to answer executive questions.

Before Power BI:

- “What was revenue by region last quarter?” → 2–3 hours (find file, consolidate, verify)
- “Show me deals over $100K by sales rep” → 1 hour (filter Excel, consolidate)
- “What’s our inventory turnover by product?” → 4–6 hours (pull from multiple files)
- Average: 2.8 hours

After Power BI:

- “What was revenue by region last quarter?” → 15 seconds (click filter)
- “Show me deals over $100K by sales rep” → 10 seconds (click slicer)
- “What’s our inventory turnover by product?” → 20 seconds (change visual)
- Average: 15 seconds

**From hours to seconds.**

**Data Trust:**

Survey question: “How much do you trust the data in our reports?”

Before Power BI: 62% said “Somewhat trust” After Power BI: 87% said “Completely trust”

**The CFO’s Response:**

Month 6 board meeting.

CFO presented Q4 results. No errors. No last-minute scrambles. No “let me verify that.”

After the meeting, the CFO pulled me aside:

“For the first time in my career here, I presented numbers to the board with complete confidence. I knew exactly where every number came from. I could drill down to the transaction level if anyone asked. That’s never been possible before.”

![](99.System/Attachments/1!n3M8lEfFzerHnhNuuNIuUA.png.webp)

The Transformation

## The Things Nobody Tells You About (But You Should Know)

After migrating 38 Excel files to Power BI, here are the lessons I learned the hard way:

**Lesson 1: Excel Won’t Die Completely (And That’s Okay)**

We kept 9 files in Excel. Because some things don’t need Power BI:

- Simple lists (employee directory)
- One-time analysis (ad-hoc project planning)
- Heavy data entry (budget input templates)
- Complex modeling (financial scenario planning with heavy what-if)

Power BI isn’t the answer to everything. Some things belong in Excel.

**Trying to migrate everything is a mistake.**

**Lesson 2: The “Excel in Disguise” Trap**

Early reports looked like Excel tables. Rows and columns. No visuals.

People said: “This is just Excel in a browser. What’s the point?”

They were right.

If your Power BI reports look like Excel, you’re doing it wrong.

Power BI’s value is in:

- Visual analysis (charts, trends, comparisons)
- Interactivity (filters, drill-downs, slicers)
- Real-time data (no manual refresh)

**Don’t replicate Excel. Reimagine it.**

**Lesson 3: The Governance Problem**

Month 4: We had 67 reports in Power BI.

12 were official. 55 were created by users.

Some user reports were brilliant. Some were disasters (wrong formulas, bad data, misleading visuals).

We needed governance:

- Official reports: IT-managed, certified, trusted
- Personal reports: User-created, not certified
- Shared reports: User-created but reviewed by IT before sharing widely

Clear labels on each report showing its status.

**Without governance, Power BI becomes Excel chaos 2.0.**

**Lesson 4: The Training is Never Done**

Month 3: Comprehensive training delivered.

Month 5: New employees joined. They had no training.

Month 7: Power BI updated with new features. Nobody knew how to use them.

We implemented:

- New hire orientation (1-hour Power BI intro)
- Monthly “Tips & Tricks” sessions (30 minutes)
- Office hours (Thursdays 2–3 PM, drop-in help)
- Internal knowledge base (documented FAQs)

**Training isn’t a one-time event. It’s ongoing.**

**Lesson 5: Users Will Push the Limits**

Week 8 post-cutover.

Jordan (Operations) asked: “Can I create my own reports?”

“Absolutely. That’s the power of self-service BI.”

Week 10: Jordan created a report analyzing vendor performance by delivery speed, quality rating, and cost variance.

It was brilliant. Better than anything I’d built.

Week 12: Jordan created a report that joined 8 tables, calculated 23 measures, and took 3 minutes to load.

It was a disaster.

**Power users will create amazing things. They’ll also break things.**

We needed guardrails:

- Training on performance best practices
- Limits on data model complexity
- Review process for shared reports

**Enable users. But provide guidelines.**

**Lesson 6: The “Just One More Column” Problem**

Every week: “Can you add this field to the report?”

Sounds simple. But:

- Adding a column requires updating the data model
- Which requires updating the ETL process
- Which requires testing
- Which requires documentation
- One column = 2–3 hours of work

**Set expectations. Not every request can be “just add a column.”**

![](99.System/Attachments/1!u1x0AO_bKjMEUdko7X7tvg.png.webp)

Lessons We Learned the hard way

**Lesson 7: Excel Users Never Truly Let Go**

Month 6: Someone emailed me a report… exported from Power BI… pasted into Excel… with additional calculations added.

“Why are you doing this in Excel?” I asked.

“Because I needed to add a few custom calculations and I’m faster in Excel.”

Power BI can do those calculations. But muscle memory is powerful.

Some people will always prefer Excel for certain tasks. That’s okay.

**Lesson 8: Version Control is Critical (And We Learned This Late)**

Month 4: I updated the financial report. Changed a calculation. Published.

CFO: “Why do the numbers look different today?”

Me: “I updated the gross profit formula to — “

CFO: “Without telling anyone?”

Mistake.

We implemented change control:

- All report changes documented
- Release notes sent before publishing
- Major changes announced in weekly email
- Ability to roll back to previous version if needed

**Treat Power BI reports like production code. Version control matters.**

**Lesson 9: Mobile Wasn’t an Afterthought (It Should’ve Been a Focus)**

Month 5: VP of Sales complained.

“I can’t use these reports on my phone. They’re unreadable.”

I’d designed everything for desktop. Never tested mobile.

We retrofitted mobile layouts. Took 2 weeks.

**Should’ve designed for mobile from Day 1.**

**Lesson 10: Success Creates More Demand**

Month 3: 38 reports, 45 users Month 6: 67 reports, 127 users

More people wanted access. More departments wanted reports. More requests for features.

**Success doesn’t reduce workload. It increases it.**

But this is a good problem to have.

## The Unexpected Benefits (The Stuff We Didn’t Plan For)

Beyond time savings and error reduction, we found benefits we never anticipated:

**Benefit 1: Cross-Functional Insights**

Finance could now see real-time sales data. Sales could see real-time inventory. Operations could see real-time financials.

Example: Sales noticed high inventory levels in Q4. Reached out to Operations. Discovered excess inventory could be used for a promotion. Cleared $180K in inventory that would’ve sat for months.

**This insight was impossible in the Excel world. Data was siloed.**

**Benefit 2: Faster Onboarding**

New hires could explore data themselves instead of waiting for someone to explain Excel files.

Average onboarding time for analysts:

- Before: 4–6 weeks to productivity
- After: 1–2 weeks to productivity

**Benefit 3: Remote Work Actually Works**

When COVID hit (6 months after our migration), we were ready.

Everyone had Power BI access. Reports were cloud-based. No VPN needed to access Excel files on network drives.

Other companies struggled to adapt. We didn’t skip a beat.

**Benefit 4: Audit Trail for Compliance**

Finance audit used to take 3 weeks. Auditors requested Excel files. We’d send 47 files. They’d have follow-up questions. We’d search for answers in old email chains.

With Power BI: Complete audit trail.

- Every number traces back to source system
- Every calculation documented in DAX
- Every data refresh logged with timestamp
- Row-level security shows who accessed what when

Audit time: 3 weeks → 4 days

**Benefit 5: Competitive Advantage**

We could answer customer questions that competitors couldn’t.

Customer: “What’s your on-time delivery rate for orders over $50K in the Western region?”

Before: “Let me get back to you in 2–3 business days.” After: “96.3%. Here’s the breakdown by month. Want to see by product too?”

We won deals because we could answer questions in real-time.

**Benefit 6: Data Culture Shift**

People started asking better questions.

Instead of: “What was revenue last month?” They asked: “What was revenue by product, by region, compared to forecast, with trend over last 6 months?”

When data is accessible, curiosity increases.

## The True Cost (What We Actually Spent)

Everyone wants to know: “What did this cost?”

Here’s the full breakdown:

**Time Investment:**

- My time: 90 days × 8 hours = 720 hours
- Team time (interviews, testing, training): ~200 hours
- Total: 920 hours

At $100/hour loaded cost: **$92,000**

**Software/Infrastructure:**

- Power BI Pro licenses (45 users × $10/month × 12 months): $5,400/year
- Azure SQL Database (data warehouse): $2,400/year
- Power BI Premium (for larger datasets): $0 (didn’t need it initially)
- Total: **$7,800/year**

**Total First Year Cost: $99,800**

Annual Savings: $116,610 (from time savings alone)

ROI: 17% in year one

But the real value wasn’t the time savings.

It was the reduced errors, faster decisions, better insights, and competitive advantage.

Those are harder to quantify but far more valuable.

![](99.System/Attachments/1!aal3HlzgZ1aE9Qg6Bf-nIA.png.webp)

The Financial Impact

## What I’d Do Differently

If I had to do this again, here’s what I’d change:

**1\. Start with training, not building**

I should’ve trained users on Power BI BEFORE migrating their reports.

Let them see the vision. Get them excited. Then migrate.

**2\. Communicate more proactively**

I sent one email about the cutover. Should’ve sent weekly updates for 8 weeks prior.

People hate surprises. Over-communicate.

**3\. Build the data dictionary first**

I built reports, then documented the data model.

Should’ve been reverse: Document the data model FIRST, then build reports.

Good documentation prevents 80% of support questions.

**4\. Set up governance from Day 1**

We let users create reports freely, then added governance later when things got messy.

Should’ve established rules from the start.

**5\. Design for mobile from the start**

Retrofitting mobile layouts is painful.

Design mobile-first or at least mobile-aware from Day 1.

6\. Create a Center of Excellence sooner

Month 6: We formalized a Power BI Center of Excellence (3 people who became experts and supported others).

Should’ve done this in Month 1.

**7\. Plan for success**

I planned for the migration. I didn’t plan for what happens AFTER success.

Demand exploded. I was overwhelmed.

Should’ve planned for scale from the start.

## The Question Everyone Asks: “Should We Do This?”

After presenting at conferences, people always ask: “Should we migrate from Excel to Power BI?”

**My answer: It depends.**

**You SHOULD migrate if:**

✅ You have 10+ mission-critical Excel files ✅ Multiple people manually update data daily/weekly ✅ You’ve had errors caused by Excel in the last 3 months ✅ You spend 5+ hours/week consolidating data from multiple sources ✅ Your Excel files take 2+ minutes to open or calculate ✅ You need to share data with 10+ people regularly ✅ You make business decisions based on Excel data

**You should WAIT if:**

❌ You have 1–5 simple Excel files that work fine ❌ Your data is mostly manual entry (not from systems) ❌ You don’t have a data warehouse or clean data source ❌ Your team has no appetite for change right now ❌ You can’t dedicate 3–6 months to the migration ❌ Your data fits in Excel and performance is fine

**Excel isn’t bad. Excel at scale is bad.**

If Excel meets your needs, keep using it. Don’t migrate because Power BI is trendy.

But if Excel is causing pain, costing time, or creating errors, Power BI is worth the investment.

## Six Months Later: Where We Are Now

It’s been 18 months since we cut over from Excel to Power BI.

Here’s the current state:

**Reports in Production**: 89 (started with 38)

**Active Users**: 178 (started with 45)

**Data Sources Connected**: 12 (ERP, CRM, warehouse system, accounting, HRIS, website analytics, and more)

**Reports Still in Excel**: 9 (same ones we decided not to migrate — still don’t need Power BI)

**Average Query Response Time**: 2.3 seconds

**Errors in Last 90 Days**: 2 (both were source data issues, not Power BI issues)

**Monthly Support Tickets**: 8 (down from 47 in Month 2)

**People Who Still Complain About Power BI**: 1 (can’t please everyone)

**The CFO’s Latest Comment:**

Last board meeting, a board member asked: “How do you ensure data accuracy in your reports?”

The CFO pulled up Power BI on the projector. Showed the data lineage. Drilled down to transaction level. Showed the audit trail.

“This is how we ensure accuracy. Every number traces back to the source. Every calculation is documented. Every change is logged.”

The board member nodded. “Impressive. Most companies can’t do this.”

After the meeting, the CFO told me: “That’s the first time I’ve felt proud of our reporting capabilities. Thank you.”

**That made the 90 days of stress worth it.**

## The Final Lesson: It’s Not About the Technology

The migration from 47 Excel files to one Power BI model wasn’t a technology project.

It was a change management project.

The technology was the easy part. Building reports? Straightforward.

The hard part was:

- Convincing people to let go of Excel
- Rebuilding trust after the P&L reconciliation crisis
- Managing expectations when numbers looked different
- Training people who’d used Excel for 20 years
- Dealing with resistance from Excel loyalists
- Maintaining momentum when things broke

**The best technology in the world fails without buy-in.**

We succeeded because:

- We listened to users before building
- We involved them in testing
- We proved Power BI was better, not just different
- We supported them through the transition
- We celebrated the wins together

**The tool doesn’t matter. The people matter.**

If you’re considering this migration, remember:

You’re not replacing spreadsheets. You’re changing how people work.

Approach it with empathy. Listen more than you talk. Prove value before demanding change.

And when someone says “I miss Excel,” don’t dismiss them. Understand why. Maybe Power BI isn’t meeting their need. Maybe they need more training. Maybe that one workflow should stay in Excel.

**The goal isn’t to eliminate Excel. The goal is to use the right tool for the job.**

For 38 of our 47 files, Power BI was the right tool.

For 9 files, Excel was still the right tool.

**Both can coexist.**

***If you’re about to embark on an Excel-to-Power BI migration, I hope this helps you avoid some of my mistakes and replicate some of our wins.***

***What’s the biggest challenge holding you back from migrating? Drop a comment below.***

***And if this helped you see the migration more clearly, share it with another analyst who’s fighting with Excel chaos. We’ve all been there.***