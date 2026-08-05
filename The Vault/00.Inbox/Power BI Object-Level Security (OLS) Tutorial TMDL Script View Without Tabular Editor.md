---
title: "Power BI Object-Level Security (OLS) Tutorial: TMDL Script View Without Tabular Editor"
source: "https://databear.com/power-bi-object-level-security-ols-tmdl-tutorial/"
author:
  - "[[Boniface Muchendu]]"
published: 2026-04-06
created: 2026-08-04
description: "Learn how to implement Object-Level Security (OLS) in Power BI using TMDL Script View no Tabular Editor required. Step-by-step tutorial for securing columns and tables."
Processed: "Unprocessed"
---
When working with sensitive data in Power BI, security quickly becomes a top priority. While many users rely on Row-Level Security (RLS), it doesn’t always go far enough.

So, what happens when you need to hide entire columns or tables instead of just filtering rows?

That’s exactly where **Object-Level Security (OLS)** comes into play.

In this guide, you’ll not only understand OLS, but you’ll also learn how to implement it directly inside Power BI Desktop using TMDL Script View without relying on external tools.

##### What Is Object-Level Security (OLS) in Power BI?

Object-Level Security allows you to restrict access to specific elements in your data model. For instance, you can hide:

- Entire tables
- Specific columns

Unlike Row-Level Security, which filters visible data, OLS ensures that restricted elements are completely invisible to the user.

As a result, sensitive data such as financial figures or internal regions remains fully protected.

##### Row-Level Security vs Object-Level Security

Although both approaches improve data security, they serve different purposes.

| Feature | Row-Level Security (RLS) | Object-Level Security (OLS) |
| --- | --- | --- |
| Controls | Rows | Tables & Columns |
| Visibility | Filtered data | Fully hidden |
| Setup | UI-based | Script-based (TMDL) |
| Use Case | Regional filtering | Sensitive data masking |

In other words, RLS controls *what users see*, whereas OLS controls *what exists* for them.

##### Why Use TMDL Script View?

In the past, implementing OLS required external tools like Tabular Editor along with XMLA endpoints. However, things have changed significantly.

Now, thanks to TMDL Script View in Power BI Desktop, you can define security rules directly within your model.

As a result:

- You reduce dependency on third-party tools
- You streamline your workflow
- You gain better control over your data model

##### Where to Find TMDL Script View

To access TMDL Script View, follow these steps:

1. Open Power BI Desktop
2. Navigate to the left-hand panel
3. Switch to **Model View**
4. Select **Script View (TMDL)**

Once inside, you’ll notice that all metadata such as tables, roles, and relationships is exposed in a structured format.

##### Step-by-Step: Implement Column-Level Security in Power BI

##### Step 1: Create a Role

First, go to **Modeling → Manage Roles**. Then, create a new role (for example, `NoSiteAccess`) and leave it empty.

This empty role will act as the foundation for your object-level rules.

##### Step 2: Open TMDL Script View

Next, navigate to Script View. After that, locate your newly created role and drag it into the editor.

At this point, you’re ready to define permissions.

##### Step 3: Define Permissions

Now, add the following script:

```
tablePermission: AlienSignals
  metadataPermission: read
  columnPermission:
    Region: none
```

##### What This Means

- The table remains accessible
- Metadata can still be read
- However, the **Region column becomes completely hidden**

Consequently, users assigned to this role will never see that column.

##### Step 4: Apply Changes

Once your script is ready, click **Apply**.

Immediately afterward, Power BI updates the model with your new security configuration.

##### Step 5: Test Your Security Setup

To validate your setup:

1. Click **View As**
2. Select your role (`NoSiteAccess`)
3. Apply the role

As expected, the Region column will disappear. Moreover, any visuals depending on it may break, which confirms the rule is working correctly.

##### Important Considerations

Before deploying OLS, keep the following in mind:

- Hidden columns are completely inaccessible not just filtered
- Visuals relying on those columns will fail
- Therefore, testing is essential before publishing

##### Real-World Use Cases

In practice, Object-Level Security is incredibly useful. For example:

- Financial dashboards can hide revenue or profit columns
- HR reports can restrict access to salary data
- Multi-tenant solutions can isolate client data
- Executive dashboards can limit operational details

Ultimately, OLS gives you precise control over what users can access.

##### Best Practices for Power BI Security

To get the most out of OLS, consider these best practices:

- Combine **RLS and OLS** for layered protection
- Use clear and descriptive role names
- Document your security logic thoroughly
- Test roles from multiple user perspectives
- Keep your model as simple as possible

By following these steps, you’ll ensure both security and maintainability.

##### Want to Master Power BI Faster?

If you’re looking to deepen your Power BI expertise, [structured learning can make a big difference](https://databear.com/power-bi-training/)