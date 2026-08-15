---
title: "How To get Users who are assigned to Power BI Row Level Security Roles (Report Server and Power BI online)"
source: "https://www.flip-design.de/?p=1134"
author: "flip-design.de"
date: "2026-08-11"
tags: [imported, power-bi, flip-design]
created: "2026-08-11"
---

How To get Users who are assigned to Power BI Row Level Security Roles (Report Server and Power BI online) | flip-it.de :: SQL, BI and more If you created a Power BI Report with Row Level Security (RLS), it is good idea to monitor which users are assigned to the different roles to meet requirements, such as Monitoring, Audit and Security rules. This information can be logged into a database or something like this. Report Server With the Power BI Report Server (on premises) it is easy. You have two options, you can use with PowerShell the REST API ( https://docs.microsoft.com/de-de/power-bi/report-server/rest-api ) or query the Report Server DB with T-SQL. Last one, is in my point of view, easier and more useful. So, if you use following query and assign users to roles: You get all users which are assigned to the different roles of each report are using RLS. Power BI online With Power BI online it is more difficult. Because the users are managed by the portal, but the assignments are saved inside the OLAP cube (every dataset is a OLAP cube in behind). If you want to query the users, you need a Premium or PPU capacity assigned to the workspaces. With this license, you can connect to the dataset / or cube by using tools like the DAX Studio. Here you can use this query to get the users of the cube. You don’t have the possibility to query all datasets at once. There is no PowerShell or REST API command available to do this. If you want to do this, you can iterate over your workspaces To determine which dataset has a RLS configured, you can check this by using a REST API call: But, if you download and upload the PBIX file and upload it with another name, the role assignment is lost. The assigned users are not stored inside the dataset! A little bit confusing, but the reason is very simple, Power BI files doesn’t store the assignments, a OLAP cube will do that. So, if you want to migrate a report, check the REST API, get the assignments, and re-assign the users. Comments are closed.

---
*Source: [flip-design.de](https://www.flip-design.de/?p=1134)*
