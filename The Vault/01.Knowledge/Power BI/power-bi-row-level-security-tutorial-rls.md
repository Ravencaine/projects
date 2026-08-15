---
title: "Power BI Row Level Security Tutorial (RLS)"
source: "https://www.enjoysharepoint.com/power-bi-row-level-security/"
author: "enjoysharepoint.com"
date: "2026-08-11"
tags: [imported, power-bi]
created: "2026-08-11"
---

> Learn how to set up Power BI Row Level Security (RLS) with static and dynamic roles, security tables, and best practices to protect your report data.

Power BI Row Level Security Tutorial (RLS) Skip to content Row-level security (RLS) in Power BI lets you show the right rows to the right people without creating separate reports for each user or region. In this tutorial, we’ll walk through what RLS is, when to use it, how to set it up (static and dynamic), and some best practices. This Tutorial Covers: Toggle What is Row-Level Security in Power BI? Row-level security in Power BI restricts which rows of data a user can see in a report or dataset. Instead of giving everyone access to all rows, you define rules so each user only sees data that belongs to them (for example, their region, department, or customers). Typical scenarios: Sales reps should only see their own region’s sales. Managers should see their team’s data, not the whole company. External clients should only see their own data in a shared report. RLS works at the model level. That means once you define it on the dataset, the same rules apply to all reports built on that dataset. Check out Create Ribbon Chart in Power BI Types of Row Level Security (RLS): Static vs Dynamic There are two main ways to set up RLS in Power BI. Static RLS Static RLS uses hard-coded filters in your roles. Example: Role:  Filter:  Everyone assigned to this role will always see only East region data. Static RLS is fine when: You have a small number of regions or groups. Access rules rarely change. Dynamic RLS Dynamic RLS uses the logged-in user’s identity (email or username) and a security table to work out what they can see. Common patterns: Filter by user’s email using  . Map users to regions, departments, or branches in a separate “security” table and join it to your fact table. Dynamic RLS is better when: You have many users. One user may have access to multiple regions or departments. Access rules change often, and you want to manage them in data, not in Power BI roles. Read Power BI Slicer Filter Another Slicer Before You Start: Prepare Your Data Model RLS works best on a clean, relational model in Power BI. Key points: Use a star schema where possible: fact table in the center (Sales), dimension tables around it (Date, Customers, Regions, Users). Put RLS filters on dimension tables (like Region or User) rather than fact tables. Make sure relationships are correctly defined and active so filters can propagate. For dynamic RLS, you usually need a dedicated security table: Columns like:  ,  ,  , or  . Relationships from this table to the fact/dimension tables you want to secure. This lets you change access simply by updating rows in the security table, instead of editing roles. Check out Format Table Visual in Power BI Step-by-Step: Static RLS in Power BI Desktop Let’s start with a simple static RLS setup where each role can see only one region. For this, I have already created a Power BI report like the screenshot below. 1. Create a role Open your report in Power BI Desktop . Go to the Modeling tab. Click Manage roles . Click Create , and give the role a clear name, for example  or  . 2. Add a table filter Under Tables , select the table you want to filter (for example,  or  ). Next to the table, choose Add filter and pick the column you want to use (for example,  or  ). In the DAX filter box, enter an expression that returns true/false, such as:  or  Click the check icon to validate, then select Save . You can see the screenshot below the Table filter DAX expression. Now, any user assigned to this role will only see rows where the filter expression is true. 3. Test the role in Desktop On the Modeling tab, click View as . Select the role you just created. Click OK and check your visuals. You should now only see the filtered region or locations. Click Stop viewing when done. Here is a screenshot for your reference. This is a great way to confirm the filter logic is correct before publishing. Check out Create Date Range Slicer in Power BI Step-by-Step: Publish and Assign Users in the Service RLS only takes effect for end users in the Power BI Service (or Report Server). 1. Publish the report In Power BI Desktop, go to Home > Publish . Choose a workspace (ideally a shared or app workspace, not My workspace ) and publish. 2. Assign users/groups to roles Go to the Power BI Service. Open the workspace where you published the report. Find the dataset (not just the report), select the More (…) menu, and click Security . You’ll see the roles you created in Desktop. For each role, add users or security groups to the Members box and click Add / Save . Like in the screenshot below: Assigning groups instead of individual users makes maintenance easier over time. Check out Replace Blank Values with Zero in Power BI Matrix Visual Dynamic RLS with Username or Email Static RLS breaks down when you have many users or frequently changing access rules. Dynamic RLS solves this by using the logged-in user’s identity. Option 1: Simple dynamic filter on a column If your table already has a column that matches the user’s email or login, you can filter directly on that. Example: Your  table has a  column. Each row corresponds to one sales rep and their region. Steps: In Manage roles , create a role like  . Add a filter on the  table. Use a DAX filter such as:   returns the user’s login name (usually email) in the Power BI Service. Save the role and publish as before. Now, when someone opens the report, Power BI will filter  to just their row, and that filter will flow to related tables. Option 2: Security table for many-to-many access Sometimes a user needs to see multiple regions, departments, or clients. In that case, use a separate security table that maps users to allowed values. Example  table:   You might have multiple rows per user if they cover multiple regions. Steps: Add the security table to your model. Create a relationship between  and your  or  table. In Manage roles , create a role like  . Add a DAX filter on the security table, for example:  Save, publish, and assign users as usual. Now, each user will se

## Code / Examples

```
US_East_Sales
```
```
[Region] = "East"
```
```
USERPRINCIPALNAME()
```
```
UserEmail
```
```
Region
```
```
Department
```
```
CustomerID
```
```
Sales_Reps
```


---
*Source: [enjoysharepoint.com](https://www.enjoysharepoint.com/power-bi-row-level-security/)*
