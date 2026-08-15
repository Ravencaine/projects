---
title: "DAX Tip & Tricks — Use USERPRINCIPALNAME() in RLS to dynamically filter data by the logged-in user"
source: "https://medium.com/microsoft-power-bi/dax-tip-tricks-use-userprincipalname-in-rls-to-dynamically-filter-data-by-the-logged-in-user-a6972c2aaf5d"
author:
  - "[[Tomas Kutac]]"
published: 2026-03-21
created: 2026-08-12
description: "Stop creating hundreds of roles manually — one DAX expression is all you need to secure your entire Power BI model."
Processed: "Unprocessed"
---
## Stop creating hundreds of roles manually — one DAX expression is all you need to secure your entire Power BI model.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*I0R18vsaBR7ki0ZZi5fjLA.png)

**🎁** [**Get friend links for all of our 1500> Power BI learning articles here**](https://powerbi-masterclass.short.gy/learning-database?utm_source=medium&utm_medium=medium-post&utm_campaign=database-medium-post-start) **🎁**

When you’re building Power BI reports for organizations with hundreds or thousands of users, static row-level security quickly becomes unmanageable. Imagine maintaining individual roles for every employee in a company — it’s simply not scalable.

Dynamic Row-Level Security (RLS) solves this problem elegantly. Instead of creating a separate role for each user, you define a single role that automatically filters data based on who is currently viewing the report. The mechanism behind it is straightforward: Power BI’s DAX `USERPRINCIPALNAME()` function identifies the logged-in user, and a simple filter expression matches that identity against a user table in your data model.

**How It Works**

The setup requires two key components: a user/profile table (containing usernames that match Power BI account identities) and proper relationships between that table and your fact tables. In Power BI Desktop, you create a single security role with a filter expression like `[Username] = USERPRINCIPALNAME()` on the user table. Because the relationships propagate the filter across the model, this one-line expression restricts the entire dataset to only the rows relevant to the logged-in user.

After publishing to the Power BI Service, you assign all users to that single role. The “dynamic” part means users only see data if the underlying dataset contains a matching record for their username — no manual per-user configuration required.

**Key Considerations**

A few things to keep in mind when implementing dynamic RLS:

Your data model must have properly defined relationships. If any table lacks a relationship to the security table, its data will remain unfiltered — a potential security gap. Additionally, users with edit permissions on the workspace will bypass RLS entirely, so share reports using read-only methods (apps, viewer role, or direct sharing). Finally, `USERPRINCIPALNAME()` only returns meaningful values in the Power BI Service, not during local development in Desktop — use the "View as Role" feature for testing.

**Bottom Line**

Dynamic RLS is one of the most practical security patterns in Power BI. A single role definition, one DAX expression, and a well-structured data model are all you need to deliver personalized, secure report views to an entire organization — without the overhead of maintaining individual roles.

See one of the best tutorials for this topic by RADACAD:

**💡** [**MUST TRY — Power BI GPT — Personal Power BI Learning Coach**](https://powerbi-masterclass.short.gy/pbi-gpt?utm_source=medium&utm_campaign=pbi-gpt-medium-post-end) **💡**

> Don’t forget to subscribe to
> 
> 👉 [Power BI Publication](https://powerbi-masterclass.short.gy/publication?utm_source=medium&utm_medium=medium-post&utm_campaign=publication-medium-post-end)
> 
> 👉 [Power BI Newsletter](https://powerbi-masterclass.short.gy/newsletter-medium?utm_source=medium&utm_medium=medium-post&utm_campaign=newsletter-medium-medium-post-end)
> 
> and join our Power BI community:

## [Microsoft Power BI Masterclass | Linktree](https://linktr.ee/powerbi.masterclass?utm_source=medium&utm_medium=medium-post&utm_campaign=linktree-medium-post-end&source=post_page-----a6972c2aaf5d---------------------------------------)

### Let’s share our Microsoft Power BI experience. Learn together. Grow together.

linktr.ee

**Power BI Masterclass Article Classification**

**Level:** Beginner

**Category:** Data Model

**Tags:** Tips & Tricks, Data Model