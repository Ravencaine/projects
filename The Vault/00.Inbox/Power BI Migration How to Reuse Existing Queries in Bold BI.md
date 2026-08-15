---
title: "Power BI Migration: How to Reuse Existing Queries in Bold BI"
source: "https://medium.com/bold-bi/power-bi-migration-how-to-reuse-existing-queries-bold-bi-08cf73cc1498"
author:
  - "[[Florence Anyango Wasonga]]"
published: 2026-07-01
created: 2026-08-11
description: "More"
Processed: "Unprocessed"
---
![Power BI Migration: How to Reuse Existing Queries in Bold BI](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*tkzduEVEZgtgKwdeXVbyOA.png)

Power BI Migration: How to Reuse Existing Queries in Bold BI

> ***TL;DR:***If your Power BI dataset folds to SQL and View Native Query is available, you may be able to reuse or adapt that SQL in Bold BI® Code View subject to compatibility checks and validation. You still need to validate joins, filters, and data types, and you’ll typically rebuild visuals. Queries based on non-folding Power Query (M) steps, DAX measures, or import-only transformations usually can’t be reused as SQL.

## Introduction

Power BI migrations often start with one practical question: Can we reuse what we already built? In some cases, native SQL generated through Power BI’s query-folding process may be reusable in another analytics platform. Whether reuse is possible depends on factors such as connector support, database compatibility, permissions, and the transformations applied within Power Query. The extracted SQL can be copied, run against the same database, and validated in Bold BI before you rebuild dashboards.

If your model relies heavily on Power Query (M) steps that don’t fold, DAX measures, or import-only transformations, you’ll likely need to recreate that logic using SQL, views, or modeling within Bold BI. In this guide, we’ll walk through how to reuse Power BI queries in Bold BI, what to validate, and what to expect during the migration process.

## What is Power BI Migration?

Power BI migration is the process of moving dashboards, datasets, and analytics workflows from Microsoft Power BI to another business intelligence platform while preserving data accuracy, business logic, and user continuity.

Power BI migration can involve different approaches, including:

- **Platform transition:** Moving selected dashboards and analytics assets to another BI platform based on organizational requirements.
- **Analytics modernization:** Updating analytics experiences while retaining validated business logic where possible.
- **Embedded analytics adoption:** Integrating analytics into internal applications, customer-facing portals, or operational workflows.

The scope of migration depends on how Power BI is used within the organization, the complexity of existing assets, and the migration goals. Some components may be reusable, while others may require review, reconfiguration, or rebuilding in the target platform.

## Power BI Migration Assessment: What to Review Before You Begin

Before beginning a Power BI migration, it is important to understand the scope of the existing analytics environment. A structured assessment may help teams document current assets, identify dependencies, and prioritize migration activities based on business requirements.

Consider reviewing the following areas:

- **Business-critical dashboards:** Identify dashboards that support key business processes, operational workflows, or executive decision-making.
- **Data source dependencies:** Document connected databases, cloud services, credentials, and connection requirements.
- **Query and transformation logic:** Review SQL queries, Power Query transformations, DAX calculations, and other analytics logic used by dashboards.
- **Security and access controls:** Map user roles, permissions, sharing settings, and governance requirements.
- **Embedded analytics touchpoints:** Identify applications, portals, or workflows that depend on embedded dashboards or analytics components.
- **Usage and performance patterns**: Review dashboard usage, refresh frequency, load times, and areas that may require optimization.

Completing an assessment before migration may help teams define scope, prioritize work, and plan the migration with fewer unexpected dependencies.

## What Can Be Reused During Power BI Migration?

Not every Power BI asset can be transferred in the same way. While some components can be reused during migration, others typically need to be rebuilt or reconfigured. Understanding these distinctions early may help organizations plan migration projects more effectively and reduce the likelihood of unexpected redevelopment efforts.

![What Can Be Reused During Power BI Migration?](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*Fqbr64SDOwRBiJSNlM_rIg.png)

What Can Be Reused During Power BI Migration?

When a native SQL query is available, it may provide an opportunity for reuse because the logic already exists at the database layer. However, successful reuse depends on factors such as SQL compatibility, connector behavior, database permissions, parameter handling, and the target platform’s configuration.

## Why Reusing Existing Queries Matters

A common concern during Power BI migration is the need to rebuild years of analytics logic from scratch. Recreating this logic manually can increase migration effort, introduce risk, and extend project timelines. Reusing existing queries can help mitigate these challenges while supporting business continuity.

Where query reuse is possible, organizations may benefit from:

- Using existing query logic as a starting point for migration.
- Reducing the amount of logic that needs to be recreated manually.
- Supporting validation between the source and target systems.
- Identifying business rules already implemented in SQL.
- Providing a reference point when rebuilding analytics assets.

Actual benefits depend on the amount of reusable logic available and the level of validation, reconfiguration, or redesign required. Beyond technical savings, query reuse may help teams shift focus toward higher-value activities, such as:

- Dashboard modernization.
- User adoption and training.
- Governance improvements.
- Embedded analytics initiatives.
- Broader analytics modernization projects.

By building on validated query logic, organizations can reduce migration complexity, lower the risk of errors during redevelopment, and maintain more

## How to Migrate Power BI Queries into Bold BI

Reusing Power BI native SQL queries in Bold BI involves extracting the SQL query from Power BI, connecting Bold BI to the same data source, and validating the output before building dashboards. The following workflow is an example and may vary depending on the connector, data source, SQL compatibility, and dashboard design.

### Step 1: Connect Power BI to the data source

Start in Power BI by connecting to your existing data source, such as [Microsoft SQL Server](https://help.boldbi.com/working-with-data-sources/data-connectors/ms-sql-server/). Select the required tables and load the data needed to create the query.

### Step 2: Load the required tables into Power BI

Choose the tables you need and load them into Power BI. This prepares the data for transformation, joining, and query design.

![Choose Tables](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*ynYXEk1MTVjvzX22)

Choose Tables

### Step 3: Open Power Query Editor

In Power BI, select **Transform Data** to open Power Query Editor. This is where you can shape the imported data, apply transformations, and prepare the query logic.

![Power BI Query Editor](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*a5aQ5-9XKb80sEIu)

Power BI Query Editor

### Step 4: Merge queries if needed

If your dashboard combines data from multiple tables, use **Merge Queries as New** to create a combined dataset. Choose the appropriate tables and matching fields.

![Merge Queries](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*TyB-u9at_PcXhtaY)

Merge Queries

### Step 5: Select join type and matching columns

Choose the appropriate join type, such as **Left Outer**, and select the matching columns from both tables. This defines how the tables are merged and helps preserve the relationship used in your Power BI dataset.

![Merge Dataset](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*Mo_eOaOHrPBmR0LD)

Merge Dataset

### Step 6: Review applied steps

Check the applied steps in **Power Query Editor** to confirm that the transformations and merge operations were applied correctly. This step is important because the native query generated by Power BI depends on the transformations applied.

### Step 7: View the Native Query

In **Power Query Editor**, check whether **View Native Query** is available for the selected step. When query folding applies and the connector supports native query generation, this option may display the SQL sent to the underlying database. In some cases, the option may be unavailable or disabled because query folding has been interrupted or the connector does not support native query viewing.

![View Native Query Option](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*TL9R-dQePs8UJNLy)

View Native Query Option

### Step 8: Copy the Native SQL Query

If a native SQL query is available, review and copy it for evaluation in the target environment. Before reuse, verify database references, parameters, filters, joins, and any database-specific syntax that may require modification.

```c
select [$Outer].[CustomerID] as [CustomerID], [$Outer].[CompanyName] as [CompanyName], [$Outer].[ContactName] as [ContactName], [$Outer].[ContactTitle] as [ContactTitle], [$Outer].[Address] as [Address], [$Outer].[City] as [City], [$Outer].[Region] as [Region], [$Outer].[PostalCode] as [PostalCode], [$Outer].[Country] as [Country], [$Outer].[Phone] as [Phone], [$Outer].[Fax] as [Fax], [$Inner].[OrderID] as [Orders.OrderID], [$Inner].[CustomerID2] as [Orders.CustomerID], [$Inner].[EmployeeID] as [Orders.EmployeeID], [$Inner].[OrderDate] as [Orders.OrderDate], [$Inner].[RequiredDate] as [Orders.RequiredDate], [$Inner].[ShippedDate] as [Orders.ShippedDate], [$Inner].[ShipVia] as [Orders.ShipVia], [$Inner].[Freight] as [Orders.Freight], [$Inner].[ShipName] as [Orders.ShipName], [$Inner].[ShipAddress] as [Orders.ShipAddress], [$Inner].[ShipCity] as [Orders.ShipCity], [$Inner].[ShipRegion] as [Orders.ShipRegion], [$Inner].[ShipPostalCode] as [Orders.ShipPostalCode], [$Inner].[ShipCountry_1] as [Orders.ShipCountry_1] from [dbo].[Customers] as [$Outer] left outer join ( select [OrderID] as [OrderID], [CustomerID] as [CustomerID2], [EmployeeID] as [EmployeeID], [OrderDate] as [OrderDate], [RequiredDate] as [RequiredDate], [ShippedDate] as [ShippedDate], [ShipVia] as [ShipVia], [Freight] as [Freight], [ShipName] as [ShipName], [ShipAddress] as [ShipAddress], [ShipCity] as [ShipCity], [ShipRegion] as [ShipRegion], [ShipPostalCode] as [ShipPostalCode], [ShipCountry_1] as [ShipCountry_1] from [dbo].[Orders] as [$Table] ) as [$Inner] on ([$Outer].[CustomerID] = [$Inner].[CustomerID2])
```
![View the Native Power BI Query](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*9iWhWwxe-ftglzLC)

View the Native Power BI Query

### Step 9: Connect Bold BI to the same data source

[Log in to Bold BI](https://cloud.boldbi.com/login) and [create a new data source](https://help.boldbi.com/working-with-data-sources/creating-a-new-data-source/). Connect Bold BI to the same database used in Power BI, such as Microsoft SQL Server.

### Step 10: Enable code view in Bold BI

In the Bold BI data design interface, switch to **Code View**. This opens the query editor where you can enter custom SQL.

![Switch to Code View](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*c-wYsbkOKKj-ZtrB)

Switch to Code View

### Step 11: Paste the Power BI Native Query

Paste the SQL query into the Bold BI query editor and test it against the connected data source. Depending on the database platform, connector, driver, permissions, and SQL syntax used, adjustments may be required before the query executes successfully.

![Click Run to Execute the Query](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*2XAWpewfhsVL7JCO)

Click Run to Execute the Query

### Step 12: Execute and preview the query

Run the query in Bold BI and preview the results. Compare the output with the original Power BI dataset to confirm that the data matches.

![Preview Query Results](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*uejZSiWgAgbM7log)

Preview Query Results

### Step 13: Save the data source

Once the query executes successfully, save it as a Bold BI data source with a meaningful name. Use a naming convention that makes it easy for other team members to identify the migrated query.

![Click Save to Save the Data Source](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*P3sJlLQtLG8tJnyR)

Click Save to Save the Data Source

### Step 14: Build and preview the dashboard

Use the saved data source to [build a dashboard in Bold BI](https://www.boldbi.com/blog/10-dashboard-design-best-practices/). Add visualizations, configure widgets, and preview the dashboard to confirm that the migrated data supports the required analytics experience.

**Why this matters:** Even when the query output matches, dashboard layouts, filters, and interactions still need to be reviewed in Bold BI to ensure the final analytics experience meets user requirements.

![Preview the Dashboard](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*xS5wKPNQOG20d2As)

Preview the Dashboard

Add visualizations, configure widgets, and preview the dashboard to confirm that the migrated data supports the required analytics experience.

For a detailed walkthrough, refer to our guide on [migrating Power BI queries into Bold BI](https://support.boldbi.com/kb/article/13838/how-to-migrate-power-bi-queries-into-bold-bi#how-to-execute-power-bi-native-query-in-bold-bi%C2%AE?).

## Best Practices for Query Migration

To keep migrated queries accurate and reliable, validation should begin early in the migration process, not after dashboards have already been rebuilt.

Follow these best practices:

- **Start small:** Begin with high-value dashboards that use simpler native SQL queries. This helps teams test the migration approach before moving to more complex assets.
- **Validate early:** Compare row counts, column mappings, filters, joins, data types, calculated fields, and KPI output before rebuilding dashboards.
- **Review dependencies:** Check parameters, authentication settings, data source connections, calculated fields, and any Power BI-specific logic that may affect query behavior.
- **Maintain documentation:** Track copied queries, changes made during migration, validation results, and naming conventions so teams can review and troubleshoot later.
- **Involve business users:** Ask business stakeholders to review migrated output and dashboard results to confirm that the data still reflects expected business logic.

A phased approach helps teams validate results incrementally, reduce migration risk, and refine queries before expanding migration work.

## Ready to Reuse Your Existing Power BI Queries?

Power BI migration does not necessarily require recreating every component from the beginning. In environments where native SQL queries are available and compatible with the target platform, portions of existing query logic may be reusable after review and validation. The amount of reuse achievable depends on the underlying implementation, data sources, transformations, and analytics requirements.

To evaluate the best migration approach for your environment, start a [30-day free tria](https://www.boldbi.com/pricing/) l or request a [personalized demo](https://www.boldbi.com/get-free-demo/) to see how Bold BI aligns with your existing Power BI implementation.

## Frequently Asked Questions

1. **Can Power BI queries be reused in Bold BI?**  
	In some cases. When a native SQL query is available and compatible with the target environment, organizations may be able to reuse or adapt portions of that query logic in Bold BI. Compatibility depends on factors such as query-folding behavior, connector support, database configuration, permissions, and SQL syntax.
2. **Do Power BI dashboards migrate automatically to Bold BI?  
	**No. Dashboards and visualizations may require recreation or reconfiguration in Bold BI, depending on their design and complexity.
3. **What is the biggest benefit of reusing Power BI queries?  
	**One benefit is reduced redevelopment effort, as organizations can reuse portions of existing query logic instead of recreating it from scratch.
4. **What should I validate after migrating a query?  
	**Validate row counts, data types, joins, filters, calculated values, KPI output, and dashboard-level results to confirm accuracy.
5. **Can all Power BI queries be migrated to Bold BI?  
	**No. Some Power BI implementations contain logic that does not translate directly into reusable SQL. Examples may include non-folding Power Query transformations, DAX measures, calculated tables, semantic model features, and connector-specific functionality. Migration requirements should be evaluated based on the specific implementation.
6. **Does query reuse reduce Power BI migration costs?  
	**Query reuse can reduce effort in some cases, but total cost depends on scope, complexity, and required rebuild work.
7. **When should organizations consider Bold BI during a Power BI migration?  
	**Organizations may evaluate Bold BI during a migration when they are assessing platform options for dashboard development, embedded analytics initiatives, deployment preferences, data connectivity requirements, and reporting workflows. The right fit depends on the organization’s technical, operational, and business requirements.