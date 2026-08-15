---
title: "Multiple Row Level Security Roles and Object Level Security?"
source: "https://www.flip-design.de/?p=965"
author: "flip-design.de"
date: "2026-08-11"
tags: [imported, power-bi, flip-design]
created: "2026-08-11"
---

Multiple Row Level Security Roles and Object Level Security? | flip-it.de :: SQL, BI and more With Object Level Security (OLS) you can secure columns, so users who can modify reports or can access the data model can not see the column or can access via DAX to the content. Mostly hide report builders the columns, this is okay, because you can use the columns in relationships, measures, or calculated columns/tables. But when you want to protect the columns, this cannot be securely done with hiding a column. With Row Level Security (RLS) you can protect the data by using horizontal filters which are applied to the table. Now you can use OLS to protect columns. So, users cannot use data which are protected with RLS and, they cannot see columns which are protected with OLS. https://powerbi.microsoft.com/en-us/blog/object-level-security-ols-is-now-generally-available-in-power-bi-premium-and-pro/ But in the past, I see so much data models who are do not using a dynamic RLS ( https://www.flip-design.de/?p=539 ). Instead of this, they are using multiple roles for each case. Like this: But here is the problem inside. When you want to protect a column with OLS for all roles, this cannot be done. You cannot mix multiple roles when you are using OLS. Imagine you want for this scenario protect the column “Units” and you set up the OLS: Now you will receive following error message when you assign to a user multiple role: If you need are multiple roles, because you have security needs for different use cases, I suggest using one role with a dynamic security. So, you need only assign one role to each user and you can use OLS to protect also whole columns. Comments are closed.

---
*Source: [flip-design.de](https://www.flip-design.de/?p=965)*
