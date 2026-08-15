---
title: "Power BI finance writeback translytical task flow"
source: "https://databear.com/power-bi-finance-writeback-translytical-task-flow/?utm_source=powerbiweekly&utm_medium=email&utm_campaign=newsletter"
author:
  - "[[Johann]]"
published: 2026-07-21
created: 2026-08-08
description: "Building finance commentary writeback in Power BI with Fabric translytical task flows: the report-state bugs, the auth trap, and where this pattern hits its ceiling."
Processed: "Unprocessed"
---
## The hard part of Power BI finance writeback wasn’t the writeback

We set out to build a finance commentary writeback report in Power BI using Fabric translytical task flows. The interaction sounds trivial: select a finance row, type an explanation, click a button, write the comment to a Fabric SQL Database, and show it back against the same row. The Python that does the insert is a dozen lines. It was the easy part, and it was working early.

![Power BI TTF writeback report](https://databear.com/wp-content/uploads/2026/07/Fianance-Writeback-2048x1141.png)

Everything that actually took the time lived in the seams between the pieces: deciding what a single comment is really attached to, keeping the finance facts immutable, getting one selected key out of a Power BI table, fixing service-side authentication that looked like a wrong server name, mapping button parameters that a published-and-tested function still would not accept, and telling a correctly-filtered empty visual apart from a broken one. Two of the most alarming “the data is gone” moments turned out not to be data failures at all.

This is the build diary we would have wanted before we started: the route that worked, the false leads, the specific platform behaviours, and the point where a translytical task flow stops being the right tool and you should reach for an application instead.

One clarification up front, because we have written separately about building forecast [writeback inside a full Fabric App](https://databear.com/fabric-apps-finance-forecast-writeback/). This is a different pattern. Here the writeback lives inside an ordinary Power BI report, driven by a data-function button against Fabric User Data Functions. It is the lighter-weight option, and a large part of what we learned is exactly where its natural ceiling sits relative to a full app. More on that at the end.

## Two apparent data failures that were really report-state failures

The most useful lesson of the build came from two bugs that both looked like the data had vanished and were both nothing of the kind. We are putting them first because they are the heart of what makes translytical reports different from ordinary ones.

The report has a one-to-many relationship from the finance view to the commentary table:

```
vw_FinanceDemo[FinanceKey] 1 → many FinanceCommentary[FinanceKey]
```

The first bug appeared the moment we added a comment count to the finance table:

```
Comment Count = COUNTROWS(FinanceCommentary)
```

Almost every finance row disappeared, leaving only the single row that had our one manually inserted test comment. It looked exactly as though the relationship had filtered the finance data down to nothing. It had not. The measure returned blank for every row with no commentary, and the visual dropped the blank rows. Converting blank to zero brought them all back:

```
Comment Count = COALESCE(COUNTROWS(FinanceCommentary), 0)
```

The second bug was subtler and more instructive. The commentary history visual showed a comment even when no finance row was selected, because nothing was restricting it. We added a `Show Selected Commentary` measure as a visual-level filter and set the finance table’s interaction to Filter, so commentary appears only when exactly one row is selected. That fixed the behaviour but created an ambiguity that matters:

A blank commentary table can mean two completely different things. Either the visual is not receiving the selected-row context (broken), or the visual is correctly filtered and that row simply has no comments yet (working). We hit this exact ambiguity during final testing: the selected-row card was populated, the commentary table was blank, and for a moment it looked like a filter failure. It was the opposite, a correctly selected row with no commentary. The blank was the right answer.

![Power BI TTF writeback report](https://databear.com/wp-content/uploads/2026/07/sinlge-row-no-comment-2048x771.png)

*Single finance row selected, selected-row card populated, commentary history correctly blank because no comments exist yet*

That is the whole character of this kind of report in one example. A translytical report is a stateful interface, and the model has to account for every state: no selection, one selection, several selections, blank input, a successful write, a failed write, and a successful write that is not yet visible. In a production version we would make the empty state explicit (“No commentary recorded for this finance row”) so that zero records can never be mistaken for a broken interaction.

## What the comment is attached to is the real design question

Microsoft’s standard tutorial uses the small AdventureWorksLT sample and writes back a product description. That is fine for showing the mechanics, but it hides the decision that actually matters in finance, because in a product-description example the target row is obvious. In a finance report the visible row might be a fact row, an aggregate, a subtotal, or a measure evaluated under several filters. Before you can write a comment, you have to define precisely what it is a comment on.

So we used the larger `AdventureWorksDW2022`, whose `FactFinance` gives real amounts by date, account, scenario, organisation and department, and we made the central modelling decision early: `FactFinance` stays immutable. A finance amount and a user’s explanation are different kinds of record. The amount is analytical data; the explanation is an auditable action with its own author, timestamp and lifecycle. They belong in different tables, so commentary went into a separate `dbo.FinanceCommentary` and the fact table was never touched.

Our first commentary design stored all the dimensional keys explicitly, date, account, organisation, department, scenario. It was descriptive but it made the button contract far too wide: a single click would have had to pass several key values reliably, with a real chance of a partial or inconsistent combination. So we collapsed the contract to a single surrogate `FinanceKey`. Power BI passes one integer; the function resolves everything else from that row.

The key stays hidden from the user. The report shows a friendly `Selected Finance Row` card with recognisable business context, while the `FinanceKey` exists only to carry the function call.

*\[Screenshot: selected finance row card showing business context while FinanceKey stays hidden\]*

This works because the demo comments against one physical finance row. It would be the wrong key for a comment like “total operating expenses for Q3 across all organisations.” An aggregate comment needs a stable aggregate grain, account plus fiscal period plus organisation scope, or a dedicated review entity. Reusing an arbitrary underlying fact key would make an aggregate comment look precise while quietly attaching it to the wrong business object. That boundary is the single most important thing to get right before extending this pattern.

## The function was short; proving its boundary was the work

The user data function, `addFinanceCommentary`, takes the three values the report can supply reliably:

```python
addFinanceCommentary(
    financeKey: int,
    commentText: str,
    createdBy: str
) -> str
```

The `-> str` return type is not incidental: Power BI data-function buttons require a string-returning function. In production that string should be a designed, user-facing result, not a raw exception dump.

We tested the function in isolation in the Fabric portal before wiring it to anything, passing a known key, a test comment and a test user. It returned `Commentary saved.` and a SQL query confirmed the row. That single isolation step paid for itself repeatedly later: once the insert was proven independently of Power BI, every subsequent failure could be attributed to selection, mapping, publication, permissions or refresh, never to the SQL.

![Power BI TTF writeback report](https://databear.com/wp-content/uploads/2026/07/comment-being-saved-2048x728.png)

*Fabric User Data Function portal test returning “Commentary saved.”  
![Power BI TTF writeback report](https://databear.com/wp-content/uploads/2026/07/comment-saved-2048x501.png)  
*

Two small platform snags cost real time here. The connection alias rejected an underscore: `finance_sql` was refused and `FinanceSql` accepted, the field only takes alphanumerics in this experience. And the Fabric interface caused a genuine terminology hunt, we were looking for a way into “Develop mode” when the item was already in Develop, shown by the mode selector at the top right. Neither is conceptually hard; both are exactly the kind of undocumented friction a diary like this exists to warn you about.

## Selecting the function did not configure the button

This was the most misleading interface state in the whole build. We chose the Data-function action, connected the published function, and the selection completed cleanly, yet hovering the button warned:

```
The data function is not properly configured.
```

Because the function was already published and had passed its portal test, this looked like the connection had failed. It had not. Selecting a function and supplying its inputs are two separate steps, and nothing on screen made that obvious. We added and mapped the three parameters by hand:

```
financeKey  → Selected FinanceKey
commentText → input slicer value
createdBy   → Writeback User
```

`Selected FinanceKey` uses `SELECTEDVALUE`, deliberately returning blank unless exactly one row is in context. The input slicer supplies the free text. `Writeback User` uses the signed-in Power BI identity. The moment all three mappings existed, the warning cleared.

![PBI writeback button](https://databear.com/wp-content/uploads/2026/07/action-button.png)

*Power BI button action settings with financeKey, commentText and createdBy mapped\]*

We then saved, republished over the existing report and semantic model, opened the report in the service, selected one finance row, typed a comment, and clicked the button. It completed, the row was written, and after the visuals refreshed the new comment appeared against the same selected `FinanceKey`. The full loop, report selection to database insert to refreshed DirectQuery visual, worked end to end.  
![Writeback comment](https://databear.com/wp-content/uploads/2026/07/comment-history.png)

*The new comment appearing in the commentary history after clicking the writeback button*

## DirectQuery was a choice, and it exposed an authentication trap

We chose DirectQuery deliberately, not by default. The point of the demo is a visible writeback loop: the user clicks and expects the comment to appear. An Import model would insert the row but not surface it until a semantic-model refresh, which breaks that expectation. DirectQuery shows the new row immediately. The trade-off is that it pushes performance pressure to query time, our simple view was fine for a sample but should not be assumed to scale to a large finance model without query, indexing, concurrency and capacity testing.

One earlier snag on the way in: we started in Power Query Online and could not find a DirectQuery option. The source was fine; the surface was wrong. The model and report interaction have to be built in Power BI Desktop, using the SQL Server connector against the Fabric SQL server and database, with DirectQuery selected there.

Publishing then exposed the trap worth remembering. Desktop connected perfectly, but the semantic-model credentials in the service were set to Basic authentication, and the resulting error complained about being unable to open server `databear.com`, which made it look like a wrong server name rather than an auth-mode problem. Switching the service-side credentials to Organisational/OAuth resolved it immediately.

![model auth](https://databear.com/wp-content/uploads/2026/07/auth.png)

*Semantic model data source settings after changing authentication from Basic to Organisational/OAuth  
![auth approved](https://databear.com/wp-content/uploads/2026/07/auth-approved.png)  
*

The lesson generalises: a successful Desktop connection only proves the Desktop connection. It says nothing about whether the published semantic model, the Fabric SQL Database, the user data function and the report viewer are all using the intended identity. We would not call this production-ready until it had been tested with a non-owner account and the Execute, data and row-level permissions verified independently.

## Getting the finance database into Fabric took a local detour

The demo data path was more involved than the tutorials suggest, because we wanted the richer warehouse sample rather than the lightweight one. The route that worked:

```
AdventureWorksDW2022.bak → local SQL Server restore → .bacpac export → Fabric SQL import
```

The machine had neither a local SQL Server nor SSMS to begin with, so those went on first. During the restore we lost track of whether “relocate all files” had been ticked; rather than restart, we just asked the database:

```sql
SELECT name, state_desc FROM sys.databases WHERE name = 'AdventureWorksDW2022';
```

It returned `ONLINE`, which settled it without redoing the step. `SqlPackage` was the next gap, and its first install route wanted a whole.NET SDK we did not otherwise need, so we used the standalone Windows package instead and exported a roughly 16 MB `.bacpac`, then imported it into an empty Fabric SQL Database with Entra interactive auth and confirmed the finance fact and dimension tables were present before building anything on top.

*Fabric SQL Database explorer showing FactFinance and the finance dimensions after import  
![database](https://databear.com/wp-content/uploads/2026/07/Database.png)  
*

This is fine for standing up a demonstration database. It is explicitly not a deployment lifecycle. For anything ongoing, the schema, views, writeback tables and permissions belong in scripts under source control; a `.bacpac` moves a starting dataset, it is not database change management.

## Debugging by proven contracts

The reason the build stayed manageable is that we proved each layer before the next depended on it, which turned a vague “why doesn’t writeback work” into a precise “which contract is proven, and which is the next unproven one.” The chain was:

```
backup → local database
local database → bacpac
bacpac → Fabric SQL
finance tables → reporting view
report selection → one FinanceKey
Power BI inputs → function parameters
function → SQL insert
SQL insert → refreshed DirectQuery visual
```

That framing is what stopped us fixing the wrong thing. When the function worked in the portal but the button warned about configuration, there was no reason to touch the SQL. When finance rows vanished after adding the count measure, there was no reason to reimport the warehouse. When the commentary table was blank for a row with no comments, there was no reason to change the relationship. Each failure could be isolated to one contract because every earlier contract was already proven.

## When this pattern is the right choice

This architecture is at its best when the user is already making a bounded decision inside Power BI and the action ties cleanly to a stable reporting object. Commentary fits perfectly: the input is small, the volume is low, the user’s context is already on screen, and the write can be stored separately with a timestamp and identity. The same shape supports a variance-review status, an owner assignment, an approval flag, an exception note, or a controlled planning adjustment held outside the system-of-record facts.

The real test is not whether Power BI can call a function. It is whether the action has a clear grain and a small, auditable contract. In our build that contract was one `FinanceKey`, one comment, one identity. It also demands a report designer willing to treat report state as application state: selection cardinality, blank inputs, error feedback, refresh latency and permissions are not edge cases here, they are the user experience.

## When it is the wrong choice

We would not use this to edit accounting actuals, post journals, or change governed ledger facts. Appending commentary or workflow metadata to a separate table is safe; mutating system-of-record transactions is a different control problem entirely.

We would also avoid it for high-volume or spreadsheet-style multi-row entry, offline work, attachment-heavy processes, long-running approvals, complex cross-field validation, or records several users edit at once. Those needs point to a Power App, a model-driven app, or a full Fabric App, with Power BI kept as the analytical surface. This is exactly the line between this pattern and the Fabric App forecast-writeback build we have written about separately: when the interaction outgrows a single bounded action, you have left translytical territory.

There are also current service limits worth knowing before you plan a team around this. During our build, only the item owner could edit and publish the function, and service-principal access to Fabric items and data sources was not supported. Those constraints shape ownership, deployment and identity design even when the report itself works fine.

## What we would change before production

The demo works end to end, but “works in a demo” and “ready for users” are different bars. We would guard the button so it is disabled when no single row is selected or the input is empty, and make the empty commentary state an explicit message rather than a blank table. We would move the schema and function code into source control with a repeatable deployment, separate commentary permissions from finance-read permissions, and have the function enforce authorisation itself rather than trusting the report interface, then test the whole thing with a non-owner account and verify row-level security, SQL permissions and function Execute permissions independently.

We would also settle the commentary lifecycle, which is currently append-only. A production owner has to decide whether comments can be edited, whether edits create versions, whether a comment can be superseded, and how deletions show up in the audit history. And we would test query performance and concurrency at realistic volumes, since DirectQuery’s responsiveness comes at the cost of depending on source-query performance at interaction time.

## The practical conclusion

The working part of this writeback demo was never the Python. It was a chain of explicit contracts across SQL, Fabric User Data Functions and Power BI, and the decisive choices were all modelling and interaction ones: keep commentary out of `FactFinance`, reduce the report-to-function contract to a single `FinanceKey`, expose context through a friendly card while hiding the key, choose DirectQuery so the write is visible, and treat report state as application state.

The most misleading failures were never backend failures. A blank count hid the finance rows. A correctly filtered empty table looked broken. A published, tested function still threw a configuration warning until its parameters were mapped. A perfect Desktop connection masked a wrong service identity. Each one tempted us to fix a layer that was already sound.

That is the decision frame we would give any finance team considering this. When the action is narrow, contextual, low-volume and auditable, a translytical task flow removes the friction of leaving Power BI and hunting down the same business context somewhere else. When the workflow starts to need a real application’s data-entry, concurrency, approval and lifecycle capabilities, build the application. Knowing which side of that line you are on, before you start, is most of the job.

Learn more about how we can help you with your [Power BI writeback requirements.](https://databear.com/power-bi-consulting/)