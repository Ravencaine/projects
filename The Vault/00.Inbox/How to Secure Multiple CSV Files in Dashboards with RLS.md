---
title: "How to Secure Multiple CSV Files in Dashboards with RLS"
source: "https://medium.com/bold-bi/secure-multiple-csv-files-in-dashboards-with-rls-bold-bi-9bf8940f318a"
author:
  - "[[Macrine Onyango]]"
published: 2026-06-25
created: 2026-08-11
description: "More"
Processed: "Unprocessed"
---
![How to Secure Multiple CSV Files in Dashboards with RLS](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*_eXBOiRz8AUtZE_q1k1zmg.png)

How to Secure Multiple CSV Files in Dashboards with RLS

> ***TL;DR:*** *Learn how to apply row-level security (RLS) across multiple CSV files in Bold BI® by combining datasets and using user-based filters. This approach simplifies dashboard access control, reduces duplication, and ensures each user sees only relevant data.*

## Introduction

Managing dashboard access control becomes challenging when data is distributed across multiple CSV files. As usage grows, controlling what each user can see becomes essential for maintaining data security.CSV files are widely used to share analytics data, with teams exporting sales records, customer data, inventory updates, and operational metrics before building dashboards. While this approach is convenient, it introduces a key challenge: how can you prevent users from viewing restricted data without creating duplicate dashboards?

For example:

- A regional sales manager should see only region-specific data.
- A department head should access only relevant records.
- Executives may require full visibility.

Without proper control, sensitive data can be exposed.

This is where row-level security (RLS) across appended CSV datasets becomes essential. By combining datasets and applying one RLS rule, you can control access using user-based filters and maintain consistent dashboard access control.

In this article, you’ll learn how to secure multiple CSV files in dashboards using a single RLS rule in Bold BI.

## What Is Row-Level Security in Dashboards?

Row-level security (RLS) is a data access control mechanism that restricts which rows of data users can view within a dashboard. Unlike dashboard-level permissions, which determine who can open a dashboard, RLS controls what data users can see after gaining access.

For example:

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*jM5S6xSm5CkT_uoR7kfafw.png)

All users access the same dashboard, but each sees only the records they are authorized to view.

It works by applying filters tied to user identities within the dataset itself, ensuring consistent data source security across dashboards. For embedded analytics scenarios, it can also be applied programmatically using the [embedding SDK](https://help.boldbi.com/embedding-options/embedding-sdk/row-level-security/).

## Why Row-Level Security Matters for Multi-CSV Dashboard

When working with multiple CSV files, data is often spread across different datasets, such as sales, inventory, products, or operations. While combining these files into a dashboard provides a unified view, managing secure access becomes increasingly challenging as the number of users grows.

Without RLS:

- Users may gain access to records they are not authorized to view.
- Sensitive business data can be exposed to unintended audiences.
- Organizations may need to create separate dashboards for different user groups.
- Maintaining multiple dashboard versions increases administrative overhead and the risk of inconsistencies.

A more scalable approach is to combine multiple CSV files into a single data source and apply a centralized row-level security rule. When users access the dashboard, Bold BI automatically filters the data based on the defined RLS conditions, ensuring each user sees only the information relevant to their role or permissions.

Key benefits include:

- **Simplified administration:** Manage a single RLS rule instead of maintaining separate filters across multiple CSV datasets.
- **Improved scalability:** Add new users or CSV files without redesigning your security strategy.
- **Consistent user experience:** Allow everyone to access the same dashboard while viewing only the data they are authorized to see.
- **Reduced maintenance:** Eliminate the need to create and manage duplicate dashboards for different user groups.
- **Enhanced data security:** Protect sensitive information through centralized, user-based filtering.

If you’re embedding dashboards into your applications, see [Enabling Row-Level Security with Embedded BI](https://www.boldbi.com/blog/enabling-row-level-security-with-embedded-bi/) to learn how RLS can be applied in embedded analytics scenarios while maintaining secure, user-specific data access.

Next, let’s explore how to implement this setup in Bold BI.

## How to Secure Multiple CSV Files with RLS in Bold BI

Applying row-level security to a unified dataset may seem complex, but Bold BI simplifies it with built-in data preparation and filtering features. By combining files and applying filters, you can control access efficiently across users.

**Prerequisites**

- Multiple CSV files with a consistent structure for easier appending.
- A column for filtering such as region, department, or user ID.
- Access to Bold BI with appropriate [user roles.](https://help.boldbi.com/managing-resources/manage-users/)

Follow the steps below to get started.

### Step 1: Open the Data Sources page

Log in to your Bold BI dashboard. From the left navigation pane, click the **Data Sources** icon, as shown below. This opens the Data Sources page where you can create and manage all your datasets.

![Access the Data Sources page from the left navigation panel](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*GEJueFhTkXVZZiWvXLQBqg.png)

Access the Data Sources page from the left navigation panel

### Step 2: Create a new CSV data source

On the Data Sources page, click **New Data Source** in the top-right corner. From the dropdown, select **Create Data Source**, as highlighted in the image.

![Create a new data source from the data sources page](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*sa0DdL6EpL5AiIv4BBdvcQ.png)

Create a new data source from the data sources page

This will open the connector selection panel as shown below.

![Browse available connectors in the data source selection panel](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*oi27LqEwQmIaf7BHq8sOaA.png)

Browse available connectors in the data source selection panel

### Step 3: Select the CSV connector and upload your file

In the **Add Data Source** dialog, you will see a list of available connectors. Use the search bar to find **CSV**, then select the CSV connector from the results.

![Search and select the CSV connector](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*8jLBr1GkGGwLZgODPokueQ.png)

Search and select the CSV connector

### Step 4: Upload your CSV file and configure the data source

Enter a name for your data source and optionally add a description. Then upload your CSV file by either dragging it into the upload area or clicking **Browse File**.

You can also configure options such as:

- Selecting the file or folder input type.
- Choosing the separator format.
- Enabling the first row as header.
![Upload your CSV file and configure the data source](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*L977Bei7wzuQkwyr5C0x3Q.png)

Upload your CSV file and configure the data source

Once the file is uploaded successfully, click **Connect** to proceed.

### Step 5: Preview and confirm your dataset

Review the data preview carefully to ensure the columns and values are loaded correctly. Once verified, click **Connect** to create the data source and proceed to the data preparation view.

![Preview the dataset and click Connect to create the data source](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*MpZOKbBKXAu1RiEfVWPeWw.png)

Preview the dataset and click Connect to create the data source

Once verified, click **Connect** to create the data source and proceed to the Data Preparation view.

### Step 6: Append additional CSV files

In the **Data Relation** dialog, click the **Append Data** option in the top toolbar, as highlighted. This opens the **Append Data From File** dialog.

![Use the Append Data option to merge additional CSV files](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*kSWGe_tHqK-fnRDQvpBH6A.png)

Use the Append Data option to merge additional CSV files

Upload additional CSV files using the upload area. Once the files show as **Ready to append**, click **Append** to merge them into the dataset.

![Upload and append additional CSV files to the dataset](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*Mvd4AhOQV-i_duGmw06pvg.png)

Upload and append additional CSV files to the dataset

Once appended, all files function as a single unified dataset, making it possible to apply a single RLS rule across all data sources. You can refer to our detailed guide on [how to append CSV files](https://help.boldbi.com/working-with-data-sources/append-data-source/) for more advanced scenarios.

### Step 7: Apply the RLS rule to control user data access

In the data preparation interface, click the **Row-Level Security-User Filter** icon from the top toolbar, as highlighted in the image.

![Use the Row-Level Security option to configure data access rules](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*oi1BP0YCBu0IeIQyJLn9dA.png)

Use the Row-Level Security option to configure data access rules

This opens the **Setup Row-Level Security-User Filter** dialog, as shown in the image.

![Set up a new user filter](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*CG9KA63P1MRjLhSIO7uXkg.png)

Set up a new user filter

In the **Setup Row Level Security (User Filter)** dialog, select a column that defines access control, such as region or department, and map it to specific users or user groups. For example, a user assigned to the east region sees only east region data and a user assigned to the west region sees only west region data.

For example:

- A user assigned to East sees only East data.
- A user assigned to West sees only West data.

After mapping the users to their data values, click **Save.**

![Map users to data values and save](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*ssjUVP1lmAhfJjQibBubGQ.png)

Map users to data values and save

To fully secure your dashboards, especially when working with multiple CSV data sources, you can combine [row-level security](https://www.boldbi.com/blog/enabling-row-level-security-with-embedded-bi/) with [role-based access control](https://staging.boldbi.com/blog/role-based-access-control-embedded-dashboards/).

### Step 8: Use the secured data in your dashboard

Open the **Dashboard Designer** and use the dataset with the applied RLS configuration. Add charts, tables, or KPIs to visualize your data.

These filters automatically act as **dynamic dashboard filters**, ensuring each user only sees their permitted data while supporting multi-tenant dashboard security.

### Step 9: Test what each user can see

Use the Preview as option in the dashboard to test different users.

For example:

- North Manager sees only North region data.
- South Manager sees only South region data.

As shown below, the dashboard preview updates based on the selected user.

![Preview as north manager](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*0FAU7g7UorW5rAQ1UpY7IQ.png)

Preview as north manager

![Preview as south manager](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*aiW6vK9YBwL9c5iA7iQwxw.png)

Preview as south manager

Refer to this [guide](https://support.boldbi.com/kb/article/17564/how-to-apply-row-level-security-with-multiple-csv-files-in-bold-bi) for detailed guidance on how to apply row-level security to multiple CSV files in Bold BI.

## Practical Use Cases of Row-Level Security in Multi-CSV Dashboards

The following examples demonstrate how a single dashboard can securely serve different users by displaying only the data they are authorized to access.

### Retail and Inventory Analytics

[Retail teams](https://www.boldbi.com/dashboard-examples/retail/) often combine multiple CSV files, such as sales, inventory, and product data, into a single dashboard to get a unified view of operations. With RLS, this shared data is filtered based on the logged-in user.

**View 1: Admin**

The **Admin** has unrestricted access to the complete dataset across all organizations. They can switch between organizations, such as **Alpha Electronics**, **Beta Enterprise**, **Gamma** Industries, and Delta Industries, while maintaining full visibility into every category, product, and business trend.

![Admin view in the Retail Inventory Management Dashboard](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*byrNMYdEJgGutgtkdYbARw.png)

Admin view in the Retail Inventory Management Dashboard

**View 2: General manager**

The **General Manager** at **Alpha Electronics** views the same dashboard layout, but the data is filtered based on their assigned scope, such as a specific region or store. While the dashboard visuals remain the same, only authorized data is displayed. Different General Managers can also have different levels of access based on their assigned permissions.

![General Manager view in the Retail Inventory Management Dashboard](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*1JwBRcY5m0PkEfKGdeWYhA.png)

General Manager view in the Retail Inventory Management Dashboard

This approach lets multiple CSV datasets power a single dashboard while ensuring each user sees only relevant data.

### Healthcare Operations

[Healthcare teams](https://www.boldbi.com/dashboard-examples/healthcare/) bring together multiple CSV files, such as appointments, hospital records, and operational data, into a single dashboard for a consolidated view. With row-level security, access to this shared data is controlled based on the logged-in user’s permissions.

**View 1: Admin**

The **Admin** has unrestricted access across all healthcare networks, enabling a complete overview of hospitals, departments, patient activity, and operational metrics. They can switch between healthcare organizations while retaining full visibility into the underlying data.

![Admin view in the Hospital Management Dashboard](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*WNsijrJ1ew5KYNnXaCxwdw.png)

Admin view in the Hospital Management Dashboard

**View 2: General manager**

A **General Manager** at **Alpha Healthcare** sees the same dashboard layout, but the data is filtered according to their assigned scope, such as specific hospitals or departments. While the visuals remain consistent, only authorized data is displayed. Even within the same healthcare network, different managers may see different data based on their assigned permissions.

![eneral Manager view in the Hospital Management Dashboard](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*yww12dN8hDisVZUFzhnveQ.png)

General Manager view in the Hospital Management Dashboard

This setup allows one dashboard to securely serve multiple users while reusing the same CSV data sources.

Next, let’s look at the common challenges and how you can ensure your setup remains efficient, secure, and easy to manage as your data and users grow.

## Common Challenges and Best Practices for Securing CSV-Based Dashboards

While applying row-level security is straightforward, certain issues can impact accuracy and performance. Addressing these early and following best practices helps maintain a secure and scalable setup.

**Common challenges**

When applying row-level security to consolidated CSV data, the following issues can arise:

- **Schema mismatch:** Differences in column names or data types can cause append failures.
- **Missing security column:** Required fields such as region or department may be absent.
- **Incorrect user mappings:** Mismatched values can expose incorrect data.
- **Empty dashboard results:** Filters that do not match any records can result in blank visuals.
- **Duplicate records:** Improper data preparation can introduce duplicate rows.

**Best practices**

To ensure a secure and maintainable setup, follow these best practices:

- Standardize CSV structures before combining files.
- Use consistent and meaningful fields such as Region or Department for access control.
- Maintain user mappings with consistent formatting and values.
- Validate datasets before applying security rules.
- Test dashboard access regularly when updating users or data.

## Get Started with Secure Dashboard Access with Bold BI

Managing a secure dashboard becomes more challenging when multiple CSV files are involved, especially when different users need access to different subsets of data. Bold BI® makes it easy to combine CSV datasets, apply row-level security, and deliver personalized dashboards from a single, scalable platform. By combining multiple CSV datasets and applying a single Row-Level Security rule, organizations can deliver personalized dashboards, reduce maintenance, and secure sensitive information without creating duplicate dashboards.

With Bold BI, you can:

- Combine multiple CSV files into a unified dashboard environment.
- Apply row-level security (RLS) to control data visibility for specific users and roles.
- Secure sensitive data without creating separate dashboards for different audiences.
- Personalize dashboard views with dynamic, user-based filtering.
- Support [multi-tenant](https://www.boldbi.com/blog/harnessing-multitenancy-empowering-insights-with-embedded-bi/) analytics for teams, departments, and customers.
- Simplify [data governance](https://www.boldbi.com/blog/governed-self-service-bi-prevents-data-sprawl/) while maintaining flexibility and control.
- Scale securely as your users, dashboards, and CSV data sources grow.

Whether you’re building internal analytics solutions or customer-facing analytics portals, Bold BI helps you create secure CSV dashboards that automatically display the right data to the right users.

Ready to secure your CSV dashboards with row-level security? Start your [free trial](https://www.boldbi.com/pricing/) or request a [personalized demo](https://www.boldbi.com/get-free-demo/) to see how row-level security can help you secure CSV dashboards at scale.

## Frequently Asked Questions

1. **What is row-level security?**

Row-level security (RLS) is a data filtering mechanism that ensures users only see the rows of data they are authorized to access within a dashboard.

**2\. How do I secure dashboard access?**

Securing a dashboard typically involves two layers. Role-based access control determines who can access the dashboard, while row-level security controls what data users can see after accessing it.

3\. **Can one RLS rule work across multiple datasets?**

Yes. When multiple datasets (such as CSV files) are combined into a single data source, a single RLS rule can be applied to control data visibility across the entire dataset.

**4\. What happens when new users are added?**

Simply update the user mappings associated with the RLS rule. There is no need to create new dashboards or duplicate datasets.