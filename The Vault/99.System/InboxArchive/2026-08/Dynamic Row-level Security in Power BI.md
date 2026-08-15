---
title: "Dynamic Row-level Security in Power BI"
source: "https://databear.com/dynamic-row-level-security-in-power-bi/"
author:
  - "[[Boniface Muchendu]]"
published: 2022-10-30
created: 2026-08-04
description: "In this article, we shall focus on Dynamic Row-level security (RLS) and how to implement it in Power BI."
Processed: "Unprocessed"
---
Row-level security (RLS) is one of the approaches used in Power BI to control access to data reports. Row-level security is applied to rows in a table and, thus, a horizontal limitation that controls data visibility. There are two types of RLS: static RLS and Dynamic RLS. In this article, we shall focus on dynamic RLS and how to implement it in Power BI.

## Dynamic Row-level security

When using dynamic RLS, users’ access to different dashboards and reports depends on their login credentials. This method of Row-level security is more complex than static RLS but more secure. Using dynamic RLS, it is possible to assign one user multiple roles or multiple roles to multiple users.

## How to implement dynamic row-level security in Power BI

Dynamic row-level security works with any data source with which Power Bi is compatible, such as an SQL server.

On the Power BI desktop, let’s start by creating two tables: transactions and sales reps, as shown below.

In our examples, the sales rep handles every transaction.

To create a table, navigate the desktop to the **home tab** and click on **add data.**

![dynamic row-level security ](99.System/Attachments/dynamic_row-level_security_.png)

Create a table with several columns (3) and label it sales Rep; kindly ensure that the data in the username column is extracted from actual Power BI accounts that you wish to secure.

![dynamic row-level security ](99.System/Attachments/dynamic_row-level_security_-1.png)

Create a second table and label it **transactions** and then Load it.

![dynamic row-level security ](99.System/Attachments/dynamic_row-level_security_-1.png)

From the table above, it is evident that the sales rep is responsible for each transaction. After loading both tables, you can check the relationships between the sales rep and transactions.

### Creating a Report

You can use a table visualization to create the report, displaying the date, amount, and name. Our aim is to ensure users will only have access to the section of the report assigned to them.

![Creating a Report](99.System/Attachments/Creating_a_Report.png)

You can use the USERPRINICIPLENAME() DAX function and check the logged-in user. This allows you to view all users currently logged in and the part of the report each is accessing.

In Power BI, assigning users roles after a report is published can be done in Power Service.

Navigate where the report is published and select **security.** Hovering over the data selection and clicking on the ellipses to view the available options.

![Creating a Report](99.System/Attachments/Creating_a_Report.png)

Added new users on the security tab the user will have access to the data sets assigned to their usernames.

![Creating a Report](99.System/Attachments/Creating_a_Report.png)

**Adding users in Power BI**

In Power BI, all new users can only be added before the report is published, by accessing the Power BI desktop’s modeling tab and selecting **managing roles.**

![Adding users in Power BI](99.System/Attachments/Adding_users_in_Power_BI-1.png)

- On managing roles, click
- Assign a unique name to the role.
- Find the table and select it.
- Select the ellipses on the table, apply a filter, and then select the column name you wish to utilize.

**![Adding users in Power BI](99.System/Attachments/Adding_users_in_Power_BI-1.png)**

In the view above, replace the value in “username with **USERPRINCIPLENAME()** and then verify the DAX expression before saving to apply for the new role, as shown in the image below.

![Adding users in Power BI](99.System/Attachments/Adding_users_in_Power_BI.png)

### Verifying new roles

Verify whether the created role is active and check the user logged in and what part of the report they have access to. Selecting the “other users” box and entering the username or email of the user you are checking. The box below “other users” is the “permissions,” which shows this user’s permissions.

Check out our [training](https://databear.com/power-bi-training/) and [consulting](https://databear.com/power-bi-consulting/) pages.

Need support? Check out our support packages [here](https://databear.com/power-bi-support-packages/).