---
title: "Your Power BI report shows different numbers to different people. The data is fine."
source: "https://medium.com/microsoft-power-bi/your-power-bi-report-shows-different-numbers-to-different-people-the-data-is-fine-6809cd3c8336"
author:
  - "[[Lin]]"
published: 2026-03-31
created: 2026-08-09
description: "When two managers open the same dashboard and see different revenue totals, the problem is almost never the data itself."
Processed: "Unprocessed"
---
## When two managers open the same dashboard and see different revenue totals, the problem is almost never the data itself.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*4SMVugwS8wT3zDE1xSXNvA.png)

Same dashboard. Same meeting. Different truths

## Does any of this sound familiar?

- Two executives open the same report in the same meeting and see different revenue figures — one shows $4.2M for the quarter, the other shows $3.8M
- A senior manager’s numbers have been consistently lower than everyone else’s for months, even though they have full access to the workspace
- Reports worked correctly for years, then after a team restructure certain users started seeing partial or missing data
- Someone with Admin access to the workspace is still seeing a filtered view without knowing it
- The developer tests the report and everything looks right — but specific users report wrong numbers when they open it themselves

These are not data problems. The source system is fine. The database has the right numbers. The problem is inside how Power BI decides what each person is allowed to see.

**🎁** [**Get friend links for all of our 1500> Power BI learning articles here**](https://powerbi-masterclass.short.gy/learning-database?utm_source=medium&utm_medium=medium-post&utm_campaign=database-medium-post-start) **🎁**

## What is actually happening

Power BI has a feature called Row-Level Security that controls which rows of data each user can access. It is designed for situations where different people should see different slices of the business — a regional sales manager sees their region, a store manager sees their store. When built correctly, it is invisible. Each person sees exactly what they should and nothing looks unusual.

The problem surfaces when someone is accidentally placed inside a security role that was never meant for them. If your Head of Sales gets added to the South Region role by mistake, they will see only South data. The report will not tell them this is happening. No warning, no error, no indication that a filter is active. Just a smaller number where a larger one should be.

This happens most often after a team restructure, when workspace access is updated in bulk, or when a developer adds a senior user to a role temporarily for testing and never removes them. The developer tests the report as themselves and sees everything correctly. The affected executive opens the same report and sees a subset. Both are looking at the same file, the same data source, the same published report.

## What it costs

The immediate damage is a wrong number in a presentation. A revenue figure that does not match finance. A regional breakdown that does not add up to the stated total. The longer-term damage is trust. When a dashboard shows different numbers to different people and nobody can explain why, the natural conclusion is that the tool cannot be relied on. Teams quietly revert to spreadsheets. The Power BI investment continues running but stops being used for anything that matters.

## What good looks like

In a correctly configured setup, executives and anyone who should see all data are either assigned no security role at all (which in Power BI defaults to full visibility) or placed in a dedicated role that explicitly removes all filters. Every role is tested from the perspective of actual users, not just by the developer running a preview. Role assignments are reviewed whenever team structure changes.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*nYXDFvQuNtbmmB5_enB24A.png)

How RLS role assignment determines what each user sees. A user with no role gets full visibility. A user in the wrong role gets filtered data with no indication anything is restricted

## Five RLS situations that produce wrong numbers

Common role assignment mistakes, their silent business impact, and the corrective action for each

## Three things worth checking

In the Power BI service, open the semantic model, go to Security, and review which users are in which roles. Any executive, director, or cross-functional manager assigned to a regional or departmental role is a candidate for this problem.

Use the View as role feature in Power BI Desktop or the service to open the report exactly as a specific user sees it. If the view differs from what that user should see, the role assignment is the issue — not the data.

Ask your developer whether any workspace or dataset roles were changed as part of a recent team restructure or new hire onboarding. Most of these cases trace back to a routine access update that had an unintended side effect nobody caught.

## What it costs to leave it unfixed

A report that shows the right number to some people and the wrong number to others will eventually surface in a meeting where it matters. At that point the question stops being “why is this number different?” and becomes “can we trust anything this system produces?” That is a much harder conversation to recover from than fixing a role assignment.

The organizations that catch this early test reports from multiple user perspectives before publishing — not just from the developer’s own account. That single habit eliminates most of these incidents before they reach a boardroom.

## For the developer or analyst on your team

The root cause is almost always one of three things: a user placed in a role that filters their view by mistake, a dynamic RLS rule using `USERPRINCIPALNAME()` that does not match the user's actual UPN in the security table, or a FILTER expression that is broader than intended.

The most common dynamic RLS pattern:

```c
-- Entered as a table filter on 'SalesData' inside Modeling > Manage Roles.
-- This is a boolean row filter, not a measure. Power BI evaluates it per row.
-- Rows where this returns FALSE are hidden from the current user.
'SalesData'[ManagerEmail] = USERPRINCIPALNAME()
```

Watch [*‘How to create Dynamic Row-Level Security for Power BI’*](https://www.youtube.com/watch?v=Z0eeTTL7EhQ) by Christine Payton

Enter this expression directly in the role editor for the `SalesData` table - no FILTER() wrapper, no measure name. `USERPRINCIPALNAME()` returns the signed-in user's email at query time. If the email stored in `SalesData[ManagerEmail]` does not match exactly, the user sees no rows for that role.

To diagnose: in Power BI Desktop go to Modeling > View as, enter the affected user’s UPN and select their role. If data looks wrong there, the filter expression is the problem. If it looks correct there but wrong in the service, the UPN is the issue — the email in the security table does not match what Azure AD returns for that user. Guest accounts are particularly vulnerable: their Azure AD UPN includes `#EXT#` which no security table entry will match, silently returning blank or partial data.

Use `INFO.ROLES()` in DAX Studio to audit role membership across the entire model before any workspace access changes go live.

## References

1. [*Microsoft Docs: Row-level security with Power BI*](https://learn.microsoft.com/en-us/fabric/security/service-admin-row-level-security)

> Follow me on [**Medium**](https://medium.com/@dataengklin88), and [**LinkedIn**](https://www.linkedin.com/in/linthedataguy/) for updates. If something here sparks a question or saves you a debugging session, that’s exactly why I write.

**💡** [**MUST TRY — Power BI GPT — Personal Power BI Learning Coach**](https://powerbi-masterclass.short.gy/pbi-gpt?utm_source=medium&utm_campaign=pbi-gpt-medium-post-end) **💡**

> Don’t forget to subscribe to
> 
> 👉 [Power BI Publication](https://powerbi-masterclass.short.gy/publication?utm_source=medium&utm_medium=medium-post&utm_campaign=publication-medium-post-end)
> 
> 👉 [Power BI Newsletter](https://powerbi-masterclass.short.gy/newsletter-medium?utm_source=medium&utm_medium=medium-post&utm_campaign=newsletter-medium-medium-post-end)
> 
> and join our Power BI community:

## [Microsoft Power BI Masterclass | Linktree](https://linktr.ee/powerbi.masterclass?utm_source=medium&utm_medium=medium-post&utm_campaign=linktree-medium-post-end&source=post_page-----6809cd3c8336---------------------------------------)

### Let’s share our Microsoft Power BI experience. Learn together. Grow together.

linktr.ee

**Power BI Masterclass Article Classification**

**Level:** Intermediate

**Category:** Data Model

**Tags:** Tutorial, Data Model