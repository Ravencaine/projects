---
title: "Dynamic Data Masking in Power BI"
source: "https://evaluationcontext.github.io/posts/data-masking"
author: "evaluationcontext.github.io"
date: "2026-08-11"
tags: [imported, reading-list, reading-list]
created: "2026-08-11"
---

> Secure dynamic data masking in Power BI Import Models

Dynamic Data Masking in Power BI - Evaluation Context Skip to content Dynamic Data Masking in Power BI Secure dynamic data masking in Power BI Import Models I was recently involved in a project that needed dynamic data masking in Power BI. This reminded me of a technique I used years ago: making Row Level Security (RLS) act like Object Level Security (OLS) . I decided to write this post because there are a number of articles that suggest using DAX for dynamic data masking. There is a big issue with this approach! The masking is only applied in the reporting layer. The source data is still in the semantic model and is still queryable. It can't be said enough: obscurity is not security . This post focuses on Import models. I am not covering DirectQuery here, because in DirectQuery scenarios you can often apply masking in the source system, such as a Lakehouse or Warehouse. That introduces different considerations around SSO passthrough and gateways, which is a separate topic. Why Not Use DAX for Data Masking? ¶ The common DAX masking pattern looks something like this: There are many variations, but they all share the same issue: the original field still exists in the semantic model. That can be fine for is the masking is purely for user experience. But it does not address security. A user with Build permission, Analyze in Excel, XMLA endpoint access, a copied report, or any other route that can query the model can still query the unmasked column unless the model prevents access. The report visual might show  , but the model still contains the email address, national insurance number, salary, or any other sensitive value you are trying to protect. You also can't simply put OLS on the source column and keep a DAX measure on top of it. If a measure references a secured column, that measure is restricted as well. RLS and OLS in Power BI ¶ Before moving onto my approach, a primer. RLS filters rows. OLS restricts access to tables and columns. In both cases, users are assigned to security roles. Those roles can contain RLS rules, OLS rules, or both. RLS & OLS Row-level security and object-level security cannot be combined from different roles because it could introduce unintended access to secured data. An error is generated at query time for users who are members of such a combination of roles. -- Analysis Services Doc RLS can be static or dynamic. A role contains one or more DAX filter expressions applied to one or more tables. Those filters are applied whenever the user queries the model. Static RLS is the classic "one role per region" pattern. A user in the  role can use the same report as everyone else, but the model only returns rows for the North region. Dynamic RLS uses a security table and DAX functions such as  to resolve the user's permissions at query time. OLS allows you to specify whether users within a security role are able to read specific tables or columns. It also hides the secured metadata, so for a user without access it is as if the table or column doesn't exist. Dynamic OLS is not possible. The main problem with OLS is report visuals. If a visual contains a secured field, users without access see an error. There is a technique covered by Chris Webb to work around this using field parameters, but it is still something you need to design around. OLS is also binary. A user can read the column, or they can't. It does not return an alternative value for the same column. That makes it good for hiding sensitive objects, but less convenient when the requirement is "show the same report, but show masked values for some users". RLS as OLS ¶ If we remodel the data we are able to make RLS act like OLS. Marco Russo recently pointed out that a similar pattern is documented as  in the SQLBI+ White paper: Security in Tabular Semantic Models . The general idea is you start with a table that contains a mix of fields: some you don't want to secure, and some you do want to secure. You can split that table into two: A hub with the unsecured fields A satellite with the secured fields Then you have a couple of options. The first option is to treat the satellite as a secondary fact table. Both the hub and the satellite connect to the existing dimensions, and RLS is applied to the satellite. The second option is useful when the original table contains degenerate dimensions that you still want to apply to the secured values. In that case, keep the degenerate dimensions on the hub and relate the hub to the satellite using a common key and a one-to-many relationship. With either setup, the sensitive fields move into a table where RLS controls row access. The user can still query the unsecured hub, but access to the sensitive satellite rows is governed by the security role. Extending The Idea To Data Masking ¶ We can extend the pattern for data masking. Instead of using RLS only to remove rows, we use it to choose between masked and unmasked versions of the same row. To do this, prior to importing the data, we duplicate t

## Code / Examples

```
********
```
```
North
```
```
USERPRINCIPALNAME()
```
```
Converting OLS into RLS
```
```
isMasked
```
```
FactKey:IsMasked
```


---
*Source: [evaluationcontext.github.io](https://evaluationcontext.github.io/posts/data-masking)*
